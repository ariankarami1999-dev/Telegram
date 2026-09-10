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
<img src="https://cdn5.telesco.pe/file/gw7Tg4_vfh-B8uR4AuNRTXYvezKa7no1Vc46KaIG3kxTHJeIMgmWahIZbJQrE2LrNyISWBvQM6L3bzJYkm6n-Xaka59Ah6VotXaLl0z2VBU2S52btaUi6Gk7ELruInhWbAHF3hv-N7Iy1ToqhNzs5Xqf5mdhPeHXMlBqZQbWOvXb88pRJbAVFR-2tZP6Wiq79WDm-0HP9q-iXl1u-QhDOn7XhS0b3u7GAe5_4jLy2yfjSx78G2NcEu8AbAFEM2HZG8aDrJ1h91plFZp8SbNw9g4u7qecxGpuwV94SOjZLUEZ4GwYf6AVOlFSlpQrUCAXJchwX_bv_v4LeHq6a7f9tw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 420K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 09:42:13</div>
<hr>

<div class="tg-post" id="msg-106099">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe421b6527.mp4?token=gujOmd4ip2VwRoFZdcMH9bVoS7X9YD40L1zqpc8OiFgqlJtavnBmbFfKOE6-cXCT22qHUH3c1HrRN15SPKyyVI1Sa2lwAMXP3tXUifPQB_MM6ytoo70h3ajw8RVKB0G2tm9Xw6x2hE5g8DbqpzypBFGVzwN5be_yjGjm6HdWiUu7H6j1vvd7yV9fBnj3fx_Vdyw_S5sQjXQxzcES_03MBPDZ4G3s2FWwb7P86LoqbMqChTDvm1tAZPaxYsKw93yvybTIt8QRdT7XkLumnKGC3c3CWJ176h3buscuuk-VLMLBBieIupKoxTSATh2_Cyewzcw1vebXRK6j63qrqRD5vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe421b6527.mp4?token=gujOmd4ip2VwRoFZdcMH9bVoS7X9YD40L1zqpc8OiFgqlJtavnBmbFfKOE6-cXCT22qHUH3c1HrRN15SPKyyVI1Sa2lwAMXP3tXUifPQB_MM6ytoo70h3ajw8RVKB0G2tm9Xw6x2hE5g8DbqpzypBFGVzwN5be_yjGjm6HdWiUu7H6j1vvd7yV9fBnj3fx_Vdyw_S5sQjXQxzcES_03MBPDZ4G3s2FWwb7P86LoqbMqChTDvm1tAZPaxYsKw93yvybTIt8QRdT7XkLumnKGC3c3CWJ176h3buscuuk-VLMLBBieIupKoxTSATh2_Cyewzcw1vebXRK6j63qrqRD5vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
داماد سابق علی پروین: بعد ۶ سال جدایی هنوز لادن پروین رو دوست دارم!
🔻
لادن پروین رو خیلی دوست داشتم الانم خیلی دوسش دارم. لادن سوگلی خانواده‌ بود، دليل طلاقمون قماربازی من بود. چندین فرش ابریشم زیرپامون رو تو این راه به فنا دادم و ماشین بی‌ام‌و که داشتم رفت.. لادن هیج تقصری نداشت خودم مقصر اصلی این جدایی بودم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/Futball180TV/106099" target="_blank">📅 09:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106098">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36609cb5e6.mp4?token=WnyA0R-bD2SIMnOgJqd4dqgwaYcycfabnthVbYzG0s18KuYLQOyKEvn8oZWXnFHBJIErF_m04P1_0t0EpCGSnf0G1hPluco1VPAHqJZFmlUvZOCJ4T0Q5zsK3t_qq5eXzHpkIsQ3ZFpcJ7GWq5A0tiBLBVZlQLXvYCMqicwWh_UCaPWzfIoerfkWjYUWQz6aO18TmNk6qONYupwxLkTgaF4ByAzaG009Rp-mrDKo3OMJV_u0A96WuMkO1S8_SLCpjr7qdsc15oGmbJ4JzFdpBEB0ZIeAZa8cyUstcySoj0VJPrPFfRtjFQ6TjaZ6MFC5AIdMcdQu6IH7fCPpuAIqCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36609cb5e6.mp4?token=WnyA0R-bD2SIMnOgJqd4dqgwaYcycfabnthVbYzG0s18KuYLQOyKEvn8oZWXnFHBJIErF_m04P1_0t0EpCGSnf0G1hPluco1VPAHqJZFmlUvZOCJ4T0Q5zsK3t_qq5eXzHpkIsQ3ZFpcJ7GWq5A0tiBLBVZlQLXvYCMqicwWh_UCaPWzfIoerfkWjYUWQz6aO18TmNk6qONYupwxLkTgaF4ByAzaG009Rp-mrDKo3OMJV_u0A96WuMkO1S8_SLCpjr7qdsc15oGmbJ4JzFdpBEB0ZIeAZa8cyUstcySoj0VJPrPFfRtjFQ6TjaZ6MFC5AIdMcdQu6IH7fCPpuAIqCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥲
🇮🇷
🇮🇷
بدشانسی دختر کوچولوی یزدی در حاشیه بازی چادرملو مقابل شمس‌آذر قزوین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/Futball180TV/106098" target="_blank">📅 09:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106094">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lpxlU_OTZ4CQzMAQXy_TN0-7RYO9-MYR5chu7oYtw18wb7EwKcqF0XXbQMrTtFg2o32hPnYoUhZ8Apay-BdHKtDAm6uHkGRF0RzKjElwZOcs8lwZp3Mwq3yQJ4N9vfE70zMJ35k3EkcBvn0SDGT8XgKzcbvseTe0EMQmx4izNAEGOPpZeaQ4xlGYsaoTN7K7dteWVqm0tl0Iaws3bgS_WsiWR7TXuG4mESp_Ig23Zw5F-wtAS4VbqjcsAjGFov6FL-oX_UaOv_APPppPO7HB-jU2w8Byj3Ujs5_ntfS05zr5Ni7zM93_lVCqG9eWVGwf-OtBWdzPsSriMhb2N0lA4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mUCZLZWLjPGbONFXv9JC1gER8qusld9tCxFBJqEAZqBmGQoigUSaCV42B_PenGSPJU37ZbCAfbywT2SOBIieuaokqig5pFg8Hdkrg5WnJ8HC94mnvgqp6tFO58YN76NaS3gqCzi-f6aAKfsylbFTbPk6Y4vpCDjzBj8RPYFuzmoCjtC1DOnSJg3lIQoetYgK7-iLZc7GtmB2aMm2C1r5LV9jDH7cDtct4Y_RzSv5Kv3jjUvKGZZlX5PwHvAioPBukkwkpQcdQ6l2gz7Fg4DtgCBvlml-DexWC_IkC0kdWAoVVZzh7QDqZs9kkY49YbZz-jiJW6rQFsJN6x1gRAAGag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r582HoISCC_fkU4tNNN9e-Q52gLYOl08UawjeH0zhc7aM_k5ePcfNoU56KTB7qOEnlL11yn9rMEmzEaqGvT2Wse7teM0GsqbLaeaOuPC4eHU16Y2i4gqSlY4n51gLKXpUC--CXDUbvoaBtOI3J72WQa8agXzNLcJ2K7dMkmA970NCx-t55xsD86kVym8SVj_PE5Y6d9fpbr2DK_l46JuTU_UwGhzIf_06QUzLzmCUUxHLIYJNm1WXTFLbvRPN5GzFGaWtlnEFV6VMBuWM4_sbwdkGFHmUGyobB8yIC0xhGMr_Ny8MomiehasePFImlPhFJTWAJ3-FM3y2Gc6vCf0iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rzGwwyW3xb2RP19sKNeUOH_ak5SxgSHMnM3gHmIaGqLo1kj8-ywm5vXopBMi-9Cuzakx7EYMX03a8JC8y5Re4IpyI9pIEfJIgrymxcPf61mvDkFgAP2NFv9l3UakFk_qK98_DF6nonNPZVotm7SpPtKq8BJ9nKqtcsASrx2_IaZotKlk5T4JMy9eJKT34swwuzwj9FepQmzSPQKI3XRTo0R1AnweS5wLx3G6wx567zfNCBbdIwIP7pXltlbpo1PvCxy_154GQky7KK2zrJHWv52ztrgU4HQb5msw0pVRqyG3k15MEwatlpLSISVYwAON4ybl3sylMnzvA2Pi4EFN5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇮🇷
دختر پرسپولیسی حاضر در بازی ذوب‌آهن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/Futball180TV/106094" target="_blank">📅 08:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106093">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/106093" target="_blank">📅 01:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106092">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EF1S_zMmaRQztozob56FaSImAyTf7MjUYVEcuJXDFxNHAOTSxdyF1dv9gARp-lrF5k6bwCViQq5c_CbJgOFulsczLUqSnAWrM-vsYkAcYSVUWfPpQmLEtCOxgrt0RiqD7ilHvOsM2CbS7a34NOHc4nc9oqFqbdDPLz6QztzfwtDVSiLGTNNGyUXb6jibsyrWa7N2q75EULe6_TgejI0yoNgoT6M9ZWJfsNazRqZbSGoMo2XP_X1QfwLA41UZWOaFGZcYkf5kRS7gNAK0bELqur5OgIgvfA1mU0rt9vc5gFZMpaOTrcnl9ADRbngBovzPg3waH8k07huRlcRyolAeFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/Futball180TV/106092" target="_blank">📅 01:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106091">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/Futball180TV/106091" target="_blank">📅 01:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106090">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/970c991132.mp4?token=KVmBL4K1R8sD2sHXxrM1h63g1LzQZoojdHfHPsVt95iSJRGQbxCxkpy0Rs3SFBaGKJIqRhNGPp7orhQv3F9yuMT_YLd9ZfdTm08sWYRmZ95EhpDuW-Ox-TnQJ9Zyj3lfVTb5w-XinRM5rBhqtYBVqdlYchLar3ZA0m5FSC1XMLKbo5ygABbWckHXqhUGH5pYhsOXp4TejJ_g4wouKCC7dxU15z_FhWdIY18EunWUEbW2BnCe8gmW6XnGXiBrqkwDvfRwVZ9yISAxgJOzGVWKQDkHCTrFw3Z49jfEwXRK4Iyc3ms4ygdRdv4VcJ3wfLgOYDDMG357n8jEg7Zr5-fBPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/970c991132.mp4?token=KVmBL4K1R8sD2sHXxrM1h63g1LzQZoojdHfHPsVt95iSJRGQbxCxkpy0Rs3SFBaGKJIqRhNGPp7orhQv3F9yuMT_YLd9ZfdTm08sWYRmZ95EhpDuW-Ox-TnQJ9Zyj3lfVTb5w-XinRM5rBhqtYBVqdlYchLar3ZA0m5FSC1XMLKbo5ygABbWckHXqhUGH5pYhsOXp4TejJ_g4wouKCC7dxU15z_FhWdIY18EunWUEbW2BnCe8gmW6XnGXiBrqkwDvfRwVZ9yISAxgJOzGVWKQDkHCTrFw3Z49jfEwXRK4Iyc3ms4ygdRdv4VcJ3wfLgOYDDMG357n8jEg7Zr5-fBPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤔
🖤
ایرانی بیا که یه حسرت جدید به حسرت‌های بیشمار زندگیمون اضافه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/106090" target="_blank">📅 01:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106089">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9d64db334.mp4?token=s_4Khgm1lMl8ry4JPJr0NXLYkPiE3I878HHccrebDL7hbV_ShdmlnGdRUy_JxkQr4piYsfmYL1BGVczejDQnOSi3hnBFwG4ud_qSCEQyvQu1CqFdjxqwf0Vwdi_6AhMPuC35EKTuqpHz1vShxNVLjbBVN1Hyvs9gKz_QML-eTYuKDrB9IUVAIzoto7rstFAz2ywab8Mp028ic6OcmuLAnzVLPxirRDmPG3oeBun4jqEwyNTrJWOwDxs8bDyL5uCGmkUAM6T7VkIRBKJA26POKH4RyUAo_9DJG0cyhW5QlK4OoB0k6TxsVGxrMv46UHwn5sl6t2xjrNbknPK0gRiVRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9d64db334.mp4?token=s_4Khgm1lMl8ry4JPJr0NXLYkPiE3I878HHccrebDL7hbV_ShdmlnGdRUy_JxkQr4piYsfmYL1BGVczejDQnOSi3hnBFwG4ud_qSCEQyvQu1CqFdjxqwf0Vwdi_6AhMPuC35EKTuqpHz1vShxNVLjbBVN1Hyvs9gKz_QML-eTYuKDrB9IUVAIzoto7rstFAz2ywab8Mp028ic6OcmuLAnzVLPxirRDmPG3oeBun4jqEwyNTrJWOwDxs8bDyL5uCGmkUAM6T7VkIRBKJA26POKH4RyUAo_9DJG0cyhW5QlK4OoB0k6TxsVGxrMv46UHwn5sl6t2xjrNbknPK0gRiVRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لامین‌یامال
❌
لیونل‌مسی
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/106089" target="_blank">📅 01:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106088">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
⭕️
🇺🇸
رسانه‌های مملکت: آمریکا ساعاتی‌پیش به مناطقی از سیریک حمله کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/106088" target="_blank">📅 01:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106087">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaKvwo_hwxgR3oIuzZ3HVx74FyTD7G1fjTCWmeoSZciTcMITkeKd_3kBReO1n0jJMfYWNyn81jbrSdQfzMbYvedV7bd6Fpd8WGSlWfeik9dS7gb8lsLkHqV8qTlxGO6MwGjbl4Rk-ET3G1D6QC2U2fSZcct6Iz7uwNgJ21tCfcnlONJblTo6rG90hNCBfayARVuBrck4KEFpO3PFjG_qa_hDCm7LDLMYAPDRWzafueb3t900U6Qj15ERjYYldsq8yLkxEHsG-SQVqw1Mgy-5rNJYmSYV6Ib26_PDMzWAOSe4Ei4GnGlbYJnmPk2Drpsx-9hdbCxJ0CWJKbzZX-MTTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🐐
🇫🇷
آمار فران‌تورس در بازی امشب تیمش
:
🔺
15 پاس موفق از 16 پاس. 6 شوت. 3 گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/106087" target="_blank">📅 01:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106086">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-Tz6-zxrP-vLJjA3ZDmvCtJ0fCJe_oGvmEeqGkMMlrRZ5ewOyrMDrP12Xc-IGTPbYrr0HbyAbhrCgXKxKWWcor5Bq7gu0wF_OZvVyVMkKBzelceKUOYnz64GgFz4bJPE38suUO9Y8j3SkY7-pnXqPf3u_ButG5GRtZQ--ZvyS2mq4VhfywXbH4SOVunZyLzd7LcgN4OCzs_iXWqBpyUzVQkopuXg6mPTp4Vuq1-ytDm-L4sR_eoPH6uFSYklEWZgWmgbbg--tuYUOVUKUw1Fmk-Q98AG79C7wGQHlRPsgPvZ84tAUQuylmFyEz4P5ElwEezJ_fvKlUG98CquT9x3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برای اولین بار در تاریخ، آرسنال موفق به ثبت ۱۶ بازی شکست‌ناپذیری پیاپی در لیگ‌قهرمانان شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/106086" target="_blank">📅 00:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106085">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
دیدار ذوب‌آهن و سپاهان از هفته هفتم لیگ برتر که قرار بود روز شنبه برگزار شود، لغو شد. دلیل این تصمیم حضور بازیکنان سپاهان در اردوی تیم امید برای شرکت در بازی‌های آسیایی ناگویا است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/106085" target="_blank">📅 00:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106084">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF5IzU1znFccvGbUrdpTFBCFairgVWlB4PCHtymSxnX_s6xv1ssvLScm_hiBJRUALfCkxI5aOvNJv_yyo-yqsEJDRPp7be4QtxK8gMNwRAqVTN-OeN4-QHG_U0BNJILA_SnkqqwEGXd7rlcBIHrONavYp1jfNYT86VcL2Uxvr6r4wH4L9SJyF9ZOr4VLxuPv29-uGkGETnOFAOUYvumr6ufDLVZtcp_pZE7rZrwpyF3cVRvSjCDs37uqkDWBw6AYBZ40uHNkufWybj-B75CN260Ip0Sngzsm8UAmRBZbSnDj6eisrRIaDgNjDj5YW2F-yoS_sGGITT7oTDo3j5HAKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
📊
نتایج روز دوم از هفته‌اول مسابقات لیگ‌قهرمانان اروپا به شرح زیر است:
🇪🇸
بارسلونا
5️⃣
-
1️⃣
فاینورد
🇳🇱
🇩🇪
اشتوتگارت
3️⃣
-
1️⃣
وایکینگ
🇳🇴
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
2️⃣
-
1️⃣
اتلتیکومادرید
🇪🇸
🇫🇷
پاری‌سن‌ژرمن‌
6️⃣
-
1️⃣
اسلوان
🇸🇰
🇵🇹
اسپورتینگ
3️⃣
-
1️⃣
گالاتاسرای
🇹🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
1️⃣
-
0️⃣
ناپولی
🇮🇹
…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106084" target="_blank">📅 00:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106083">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZ2CPXt5XjRWZ5fiefZXmf_3QvY7g0VrwFN1vdlOFCJAAcJcjYHQyOacN3bQWu_7YSHUVoyaobBzcyeaGLc_GWkKfky3fkBfHTkBFp1G33GIUcHot5rIQmmsZVKhUoAENNvKoQD7cmUcX_zQsgQ5zK-gMiEFar0P_tNc88f3ML1zktXOBYObgt_QUzQZ6knjSFHGCQKq4AqGVvSSoX8o9BjxQ9NVpQnKrYhj-6W63_DNQerdBr8Y5v03WL0HveY4VbFB2l8Na5Z-S1XNw0GPBuB4nL3js51Q8y5TAqXmlRC5Kc-b0Qxzems-BKSn3fP4pmKjV1K2aU8QTY2VQlsj_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
📊
نتایج روز دوم از هفته‌اول مسابقات لیگ‌قهرمانان اروپا به شرح زیر است
:
🇪🇸
بارسلونا
5️⃣
-
1️⃣
فاینورد
🇳🇱
🇩🇪
اشتوتگارت
3️⃣
-
1️⃣
وایکینگ
🇳🇴
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
2️⃣
-
1️⃣
اتلتیکومادرید
🇪🇸
🇫🇷
پاری‌سن‌ژرمن‌
6️⃣
-
1️⃣
اسلوان
🇸🇰
🇵🇹
اسپورتینگ
3️⃣
-
1️⃣
گالاتاسرای
🇹🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
1️⃣
-
0️⃣
ناپولی
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106083" target="_blank">📅 00:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106082">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/af7ad02b07.mp4?token=Gx7hZ7WlChIFfruoHxG0xuIUVcbkeLr916jL0gzstLUu06P6Uynr0aQchOHKBzgzT7-StYW7PS3hSXfqDKNm09-MGCMq0qr6FG8duXsbz7PxssF338N6LIZEXj-l9NBncK0h6l4fTMrQ4zEV9xugHwWCsG3GeRdFBDL3iQUFeoaBq1noBdwskONnwCfZ5Enbbx3P-4emEcZODzdinLGn38WW_3xAmeevdJ0F2MQYKYUXQQY8EXbjP9y5wGGeApCfk7htDJk5jdAwdRXw1lPv6BMSLKb0Jzr7Ig_oh51qIF53XAlx8fmXtd3ngZ_CeV0iOY0thY21OMeFvEL8vPkUoaXH1oyX37MtXXDVGtd3dQgu5u5rV0FXIBdZ0Hxg58bjRWNzq1NCkUVTR1gPYHnkGEu1QpaZsOEtvA2Ph3bVyORYf1Eu7UyiGvE7CeUZrVu_8EUrBqRB-6cv7ga8hz-bYho_h0to8xmGPLofQihA3PvFrgDUrglNcs30SebUdPsEw4eH3nlKsJqgqPZHMJYC9sV-2ZifRbqC1R2l2SbftaPgCZJns5aDbAJFCExhAFG0B_n0iptVeroCh2FuBYaR4s2LlxktQ_1AIzK356MSeG5P_Rv__Dr4apSzC4oAahPTPPDb0XPSotTPmIhKShzZJ4LFOkCsaNncZTgPOoVOiUU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/af7ad02b07.mp4?token=Gx7hZ7WlChIFfruoHxG0xuIUVcbkeLr916jL0gzstLUu06P6Uynr0aQchOHKBzgzT7-StYW7PS3hSXfqDKNm09-MGCMq0qr6FG8duXsbz7PxssF338N6LIZEXj-l9NBncK0h6l4fTMrQ4zEV9xugHwWCsG3GeRdFBDL3iQUFeoaBq1noBdwskONnwCfZ5Enbbx3P-4emEcZODzdinLGn38WW_3xAmeevdJ0F2MQYKYUXQQY8EXbjP9y5wGGeApCfk7htDJk5jdAwdRXw1lPv6BMSLKb0Jzr7Ig_oh51qIF53XAlx8fmXtd3ngZ_CeV0iOY0thY21OMeFvEL8vPkUoaXH1oyX37MtXXDVGtd3dQgu5u5rV0FXIBdZ0Hxg58bjRWNzq1NCkUVTR1gPYHnkGEu1QpaZsOEtvA2Ph3bVyORYf1Eu7UyiGvE7CeUZrVu_8EUrBqRB-6cv7ga8hz-bYho_h0to8xmGPLofQihA3PvFrgDUrglNcs30SebUdPsEw4eH3nlKsJqgqPZHMJYC9sV-2ZifRbqC1R2l2SbftaPgCZJns5aDbAJFCExhAFG0B_n0iptVeroCh2FuBYaR4s2LlxktQ_1AIzK356MSeG5P_Rv__Dr4apSzC4oAahPTPPDb0XPSotTPmIhKShzZJ4LFOkCsaNncZTgPOoVOiUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌پیروزی بخش آرسنال به ناپولی توسط اودگارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/106082" target="_blank">📅 00:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106081">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0e2d644ee4.mp4?token=LyALZsqDpKAU9zV1cEYi5HxgHXTmhqYU1od_NHJ6anBilYZKFlI9DCt-GwBrFNkSQqmoO3MAvsBOvKA_EQLfdwE4b1PP64q0EsM1ONs8JX5rxEof1mdsRC7aZvxTaqmbbybhR1q4GOE9Hf0L2yfQP7DhHck4Q9cO270rwJK-cYfBvfPMgowUI74ocddXM8MOsOVgeu_1XyHMl1IhjNziVfOoOr6Qhmef3KdM3Ru72B7bV2I8sg0Q0qACp6sWW3hUR7UZFE49pc0myBVbjcLp6dqtqWv9OnZ5S7tfZjW1mZAWw38Z9iSq9ydJiTPE5pRZLqwF-HwWMzkGbGtmeUyf8A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0e2d644ee4.mp4?token=LyALZsqDpKAU9zV1cEYi5HxgHXTmhqYU1od_NHJ6anBilYZKFlI9DCt-GwBrFNkSQqmoO3MAvsBOvKA_EQLfdwE4b1PP64q0EsM1ONs8JX5rxEof1mdsRC7aZvxTaqmbbybhR1q4GOE9Hf0L2yfQP7DhHck4Q9cO270rwJK-cYfBvfPMgowUI74ocddXM8MOsOVgeu_1XyHMl1IhjNziVfOoOr6Qhmef3KdM3Ru72B7bV2I8sg0Q0qACp6sWW3hUR7UZFE49pc0myBVbjcLp6dqtqWv9OnZ5S7tfZjW1mZAWw38Z9iSq9ydJiTPE5pRZLqwF-HwWMzkGbGtmeUyf8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇪🇺
الله اکبررررررررر سوپرگل اسپورتینگ رو ببینید پشماممممم چی زدددددددددددد
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106081" target="_blank">📅 00:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106080">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106080" target="_blank">📅 23:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106079">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106079" target="_blank">📅 23:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106078">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hG65tcEt6jm4Qnv-pjpCfOYg0pElJpQCY7M-pr3-WBsgrBrZ5ftxVB_BxkbbKI7S-7IJ-Fb24F90zzkyE8p52ba23WYF0J_hCE6x8bDLapUdctBjHL_gsUUuOc7Y3z6WrjBU32Ui6xJKurr3JvBSHsFVWZFs5A2uACnkUw4Hsbkybr_o-Z9nOBZ2c3I0SDwsfS0KVJliNbSLBgTBoE963l9N5gUx6vAGBnBLgjKgfb-xpfmHXRmUzHDgtAwBngP1MGyystuWpBUrR1DzjJqJ7ISmlIpar8y1L6GYLTqtMHTN-iw_UXxaxJZOlbofrPwKiKbealuDt0eIgkUiZRg25g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
▶️
🇪🇺
📊</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106078" target="_blank">📅 23:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106077">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فران تورس خارکوسه هتریکککککک کرده برای پارس</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106077" target="_blank">📅 23:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106076">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b4804a9f6.mp4?token=pyKW8XksKeZuviKMF128_gT6my6bB3qxIQd9EIUNoBaiGuvnKhDbQyVhnOKBZ264A_PIEybJH-GbhVG_pegnncVqMEtBDRbB3Q1ifEYa2jrCWD6P2BdIFIPYvx2rSHGvtUmaKMqHNyNIGStgwDYL0Moux3Uzxu3Slc_ibnANTK9IF5yJA1PoEfykEjlnouyO2-uaysCLy2qkinWTXg9LRnmcWnfIiY4vx3cbORL3AeNuBq7WePRhTXzJC2Md6FiM4yAA23UWZ9jaArNoep_UFh9aCku2x_QFXpLr9Th6ChqqySCXr9uqTEofhfdC9908-s7QyncQEvWtyVGASQe1Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b4804a9f6.mp4?token=pyKW8XksKeZuviKMF128_gT6my6bB3qxIQd9EIUNoBaiGuvnKhDbQyVhnOKBZ264A_PIEybJH-GbhVG_pegnncVqMEtBDRbB3Q1ifEYa2jrCWD6P2BdIFIPYvx2rSHGvtUmaKMqHNyNIGStgwDYL0Moux3Uzxu3Slc_ibnANTK9IF5yJA1PoEfykEjlnouyO2-uaysCLy2qkinWTXg9LRnmcWnfIiY4vx3cbORL3AeNuBq7WePRhTXzJC2Md6FiM4yAA23UWZ9jaArNoep_UFh9aCku2x_QFXpLr9Th6ChqqySCXr9uqTEofhfdC9908-s7QyncQEvWtyVGASQe1Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم لیورپول توسط مک‌آلیستر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106076" target="_blank">📅 23:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106075">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپووووووپوول دومییییییییییی</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106075" target="_blank">📅 23:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106074">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
مک آلیستررررررررررر</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106074" target="_blank">📅 23:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106073">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گلگلگلگلگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106073" target="_blank">📅 23:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106072">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVwrvd47kLt5w8ZMUKFJnDYFQuFU1ry9XMlCQjOrQeCGsIFIn8lWcWMuH3dTDquEiRMNfzDHsRoMjAIxGviPaB2sF9ZxsUJNz9XMpnqcEb0him78pyBcxusenedg2-Y59IqmVAKytPOCXeWIFmdNHnmpX4P3dXTK0BWRm9vhs4K-vFhTGojeFyJ0BUzTE_HFtl3GpzL3I_jiqGb-9hQsc0LNgeLXCxjrlMLdoQKWIrqUaVN7X8o2qNvaakD20zBeKhfwWajoCQOXiveCnm_SV3R_dVFfrRjLaTCUf5Pbpph-tV0FbJ_gMydeWwc4d_SKsP-dr7VIqZSE_gcltbEnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
نیمه‌دوم مسابقات با این نتایج آغاز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106072" target="_blank">📅 23:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106071">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPgUbDnNtMk6eOa1YLwhUe0E5XpHoIge77DymfzpojspqsVEcqT_WdhhfqDYTSDaCRUwn8uKpMpOv4GHvU2ZS1Z80d-N9sJFAkYgNbIGbhtC3eIWS6jUCrZfbcwSD3q1avWHDlGTyQ_W_T2ZmypvcmefMxtkoFWi8_qWxbeGoMgGjMQVsQJXJsCfRAlfanPungF3Hb2RzWTrSxZPK0XO5YMkwHFksy_OtGbc4Mo2w-ExyQzdPbWPNMdwedXtaOKWkb7faA_A09BiAFh3K453R9NuA9Svj7NhPXEDl1YTqGPjT98vkML5aswFkZJpcWLkxT0tJKyOYvzgCX_JJXx0sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
دیدار ذوب‌آهن و سپاهان از هفته هفتم لیگ برتر که قرار بود روز شنبه برگزار شود، لغو شد. دلیل این تصمیم حضور بازیکنان سپاهان در اردوی تیم امید برای شرکت در بازی‌های آسیایی ناگویا است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106071" target="_blank">📅 23:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106070">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64577d8800.mp4?token=CHbshMNoArjM7JFOzGNVJq0xw7yZfPKqDmAJXFYu2XR96D-uTdUvy2ABXrXZNiPhenmY8pqmhtEqKxS4yRH9xTGw5GXlD722gdx1m-M-rkaTryy0WOT_QRdDNBkyxuWuwXsOl7hhGufxLXaSybQYPkAkv0tiqdNCuvI9uqUaKX3-2-C3XuPNEOlWQpH2vdgV3xHmr62c6K9N-oTo2InxkRqkWIYj7WSm4sO6FCUoPxFftbJG5UuFEHrSZA3aS_D0t16GDzo96ok2WbcDeZdMffA3J4zxFXlXuOg6c1omlaL-bkgR06kVFgnFab1hYiWKkwNfK1HoNHKI9S2uIIjOpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64577d8800.mp4?token=CHbshMNoArjM7JFOzGNVJq0xw7yZfPKqDmAJXFYu2XR96D-uTdUvy2ABXrXZNiPhenmY8pqmhtEqKxS4yRH9xTGw5GXlD722gdx1m-M-rkaTryy0WOT_QRdDNBkyxuWuwXsOl7hhGufxLXaSybQYPkAkv0tiqdNCuvI9uqUaKX3-2-C3XuPNEOlWQpH2vdgV3xHmr62c6K9N-oTo2InxkRqkWIYj7WSm4sO6FCUoPxFftbJG5UuFEHrSZA3aS_D0t16GDzo96ok2WbcDeZdMffA3J4zxFXlXuOg6c1omlaL-bkgR06kVFgnFab1hYiWKkwNfK1HoNHKI9S2uIIjOpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول لیورپول به اتلتیکو توسط سوبوسلای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106070" target="_blank">📅 23:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106069">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ارائوخو پاس گل داد
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106069" target="_blank">📅 23:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106068">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سوبوسلایییییییییییییییی</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106068" target="_blank">📅 23:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106067">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">لیورپول زدددددددد</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106067" target="_blank">📅 23:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106066">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106066" target="_blank">📅 23:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106065">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2sc5Nz4o8fRo4nuoy8BHbTLWABvUm5tct1hgpuQFGDApRy6sdLZdXMC34BCy3hXvazC2Cd6M08h5lb-s-P1mxaV5Ozph9jetWtiC_kbPGfpMFJeSiPq1okrbCVqt5_ubqXU9KOiZiZ-H-I5ZsR6j7fiajZs064nXxdc_ZQQv4LEMba9QaNYmIs8CfjwJisd1wH2SrMPARq6YONBBuv7qayK0-MQj7duc4dHojqYGtHeiD2oF-S7t9J0VbX5DAgWyJr7XRrSVO0FQbqpxy2uas6lVTKNnH1Cb5mP2b7YvwSrb_wCus36yFsDXcsgOrgH0n5TQ4oPtNs9Dl-rE5XSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚡️
🔴
از آیفون 18 رونمایی شد.   چهار رنگ آبی، آلبالویی، مشکی و نقره‌ای.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106065" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106063">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64d71d9562.mp4?token=eZDeLMvJ488eoL5ubhm1tZi3pA0fFF95WxEbrCm6S0LykljfLFBX9MqYDPGATUcPEFeKaNjQBrvdTTk1TUSB7-wCbgzX_Y171Bi-lYcAT9W7ykQQLrFUU86PB1fvf3hCj9v-qcjnw34722_DO2Jb9ZqMz-lK1B25UywYJ4UIlLlSo_00FCLNc9S7vfyqy3SJoUSfh-2ge4SDu4Bo7xbtoiWHFxINImj8SbAzawM-THaHbLz-SWn0dwAKJeJ3znLXpN3s14YDX6VCrwTUSa-ThYLvV4KUmdx9gK_wTCrTjRKbsDf4AP4PgVReA6XJmkPN61bV0cE3Jv6FOM0z9zYQlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64d71d9562.mp4?token=eZDeLMvJ488eoL5ubhm1tZi3pA0fFF95WxEbrCm6S0LykljfLFBX9MqYDPGATUcPEFeKaNjQBrvdTTk1TUSB7-wCbgzX_Y171Bi-lYcAT9W7ykQQLrFUU86PB1fvf3hCj9v-qcjnw34722_DO2Jb9ZqMz-lK1B25UywYJ4UIlLlSo_00FCLNc9S7vfyqy3SJoUSfh-2ge4SDu4Bo7xbtoiWHFxINImj8SbAzawM-THaHbLz-SWn0dwAKJeJ3znLXpN3s14YDX6VCrwTUSa-ThYLvV4KUmdx9gK_wTCrTjRKbsDf4AP4PgVReA6XJmkPN61bV0cE3Jv6FOM0z9zYQlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
گل‌اول اتلتیکو توسط مارکوس یورنته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106063" target="_blank">📅 22:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106062">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پاس کل از آلوارز</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106062" target="_blank">📅 22:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106061">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یورنتههههههههه</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106061" target="_blank">📅 22:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106060">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اتلتیکومادرید زددددددددد</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106060" target="_blank">📅 22:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106059">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گلگلگلگگلگلگلگلگگلگاگا</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106059" target="_blank">📅 22:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106058">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbLixAHHRlKfiiWDL7WcDXkPeN7wPn5onbAjgV1ZoYX-fmNzFryfee5cEgkUdI0eLq21MMfdLMo0jzJzcUn4vCervM5kYCg5gelQXGj0T9MqiIyrCmRfoxjM4fuiVkAiFOWulu4jrztiaJaT91QhL4k60mpuSnkz1Wstm16f4W2lP55zaKk2tS1BujN57Tl4rid_mv9InfJW7jv815CHD-YVhgTGGqN7pS6HtGOQ7TjjoIOD6lpce2bzKVYNnDzmtEi26Uvld90QIxQw7Cni7IC9AWnjUITu_gSyNmZtUFuBEbpGjtQa3wWAhYML9bfKb2hnFPb4VToaTEbao3C-Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇪🇸
🇪🇸
لب خوانی صحبت های رودری در جریان دیدار بارسلونا مقابل والنسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106058" target="_blank">📅 22:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106057">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M62OZa4eFvILn47yGQfx73Xz2ao81zAey-GIRYBkDfstKGW5Pd60Gqz8tbxIbM_YIBPo9_GuTUj-mAhC3isHcmlJN3MOhH3XgIK8gIQKcP0qe36xA0gtvKdfTg-KS5qrhoE0t_8Ej7P4ApY5YdLV84aMfUK6fdE4Z-HzwW_hfjvJKZOxucG5xQwhxDYSzSlqA0b-yOtnMbrs4DFur97ut33R9ck-6i9AMxFro9b8GJngfHcKlQg6KF70sQ2N2xM-YqLOsOInxpReakCWtnCIdn2Qe33Sf8q3g7warfEXUihZTVp7CcneMraScVPYkEsM7QLGvNPR8LlC5zylC1TuAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
هفته‌اول لیگ‌قهرمانان اروپا؛ معرفی قربانی جدید تجاوزهای بارسلونا؛ فاینورد در نیوکمپ تحقیر شد؛ رافینیا و یامال مجددا درخشیدند
🇪🇸
بارسلونا
5️⃣
-
1️⃣
فاینورد
🇳🇱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106057" target="_blank">📅 22:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106056">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dcba68c3d.mp4?token=NwFYOcwVskO7aA_OU-tFjzB68dPUgnuAhmfWB4ZU3RNDFU1vFSuvJ462so3FXFMjlexiqs_biRiuCZMtK74HuMJggCn56ZJnTmmPcfZ1Rp3PqwXkriKMK31EClMBT21jJP7I3aMp2KS3CDQc_9MLgO4JWkFOlRkej-i6gfzkoJHVYaAzktHyqp4FGhcpNrOdT__QjFeCM6-zxYnCS9F9laFJTRAPeJhW4m5m5wNxsG_eH81O2FVHy6uoNGfldpevAAYZwjLTJZ8gZQ7KepkpYWsiCKRtaoIUq4t7uSJo5KJOopWxj8HEvW3YnCZ3S-scU6ESjnJYjLsId0AQvgkWew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dcba68c3d.mp4?token=NwFYOcwVskO7aA_OU-tFjzB68dPUgnuAhmfWB4ZU3RNDFU1vFSuvJ462so3FXFMjlexiqs_biRiuCZMtK74HuMJggCn56ZJnTmmPcfZ1Rp3PqwXkriKMK31EClMBT21jJP7I3aMp2KS3CDQc_9MLgO4JWkFOlRkej-i6gfzkoJHVYaAzktHyqp4FGhcpNrOdT__QjFeCM6-zxYnCS9F9laFJTRAPeJhW4m5m5wNxsG_eH81O2FVHy6uoNGfldpevAAYZwjLTJZ8gZQ7KepkpYWsiCKRtaoIUq4t7uSJo5KJOopWxj8HEvW3YnCZ3S-scU6ESjnJYjLsId0AQvgkWew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حملات بیشتری در تنگه‌هرمز از سوی ما رقم خواهد خورد. فقط کمی صبور باشید
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106056" target="_blank">📅 22:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106055">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siYKcX0gVdj-KtqI6uj7k6BDhQNY-EwVOIWfH_6K3smAMbfWgE8NBEOBQhfq5f43Sf8dKIShQR1omJcXqWmOqs6ThaYGM5BKPqcZ1Nr7TXD8ytBk5EJTCjadQkIf_w2-a2V9L7RGLLt6KGjI1ErjVcdZ_kpX_BTVl3BTE3cTljuhyugi-0Huji_2bi8vSZaV02b8eM1TcertCIuWHvmBm9h8rWJ0GIz3wjo7hT6NtHM1NWwLC9HjnSfNttfgwXbo3LeeMnmjFNiKvlEivQ5zZzMvoUh9yeKiTLZocQJjfGZSauuzUluBE9ve4IYYsTHLLQC8BgWkptkpXFpV4mygYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
هفته‌اول لیگ‌قهرمانان اروپا؛ معرفی قربانی جدید تجاوزهای بارسلونا؛ فاینورد در نیوکمپ تحقیر شد؛ رافینیا و یامال مجددا درخشیدند
🇪🇸
بارسلونا
5️⃣
-
1️⃣
فاینورد
🇳🇱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106055" target="_blank">📅 22:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106054">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcGQ6nzWy8yWO_lxaxbQ1Hg5s9Qj_jwbZGbkqTNGFBhg_HuBr14EQxuC_NN9dgOP3xddX4NID7Yt7BCDll46vGjl07CXZWFJnGit2J6IRBtUZ7-Xkh6EzNfeUUSVqJMFJx5RboIidkGZJhCNGHuOUSLbgSI53m-QWG5vEivlfaH-YeeiNJF2SdkwpOQKWkd0t_kh93m-kW0GdCXI9zbVQRJc-L2qaVWA6dcAQOpxOZB7_T4zRLV4CUw-9MKFVlvWhUAE6vjdxr1LoGCAQ8KEzu5UC6PGvfPz-yY-F-Nnn9WN_prLG0KwdPCwM46Yp-Z8ieQfFeU1yCQAYPhpaImVTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
هفته‌اول لیگ‌قهرمانان اروپا؛ معرفی قربانی جدید تجاوزهای بارسلونا؛ فاینورد در نیوکمپ تحقیر شد؛ رافینیا و یامال مجددا درخشیدند
🇪🇸
بارسلونا
5️⃣
-
1️⃣
فاینورد
🇳🇱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106054" target="_blank">📅 22:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106053">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0430c92c86.mp4?token=cc6brR8zAktXvzetBjR3rlgZQ90_5iCqpu4FXTuhhrvd_etQ9IFOzgppRFHALJ2nKo7YrgVxVacs7U-Ve84trrk_aNTPNgbI2ySaCmOlttSBNUPPyDrbyY2sP8al1rCfVJYZRLJzaW7IzkJ6S2DJcl6fD9kFz-XlOPqDSqEDoGeBQKTmAWQXMfTO_SjkicHhrZQkJC116i3o2FU_zAqxFmBvx3E2AeLed9r1i5s08K4oA8y4qhVXEXcVHjZ2aqPYqndzoUEH9HIHJBl6ktNZUyga7uj-C78bEtMupyurh5nDWdK70l4PkVHiCqJ_qFVbnXsEb81pCxNVPltEl2p1zwTtO3nP5ViqS_eWoCQSHyEh79yheMefd9EX56c3oPKWBIvE25Zs4_iydYcCzGQeLsQftWft9lHg1IH_fO6JF-5DHhkpSGZEsvxDJiRGopX_PqHOQXhmyw7wwxTWNV0Vyi_LqojPOi-VnH1BxwdRQf-yI6YyhSEdZTOHiwbiFXXPWQvjhH3KnIHHqZBwykJs8LjSHlCxJw8GV7Dw4Hm9_-X-mpJGSaOuc7S6HkV2Aazjo7AcML7DnIM5jjORj6_j3X9afWaiScFlHor7HeWkNoYQqti5JQo7myt95ABedHL90dE1hARUv3wt-LGsoOgWuY6PLcHmhsxM4zIJTLAez8A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0430c92c86.mp4?token=cc6brR8zAktXvzetBjR3rlgZQ90_5iCqpu4FXTuhhrvd_etQ9IFOzgppRFHALJ2nKo7YrgVxVacs7U-Ve84trrk_aNTPNgbI2ySaCmOlttSBNUPPyDrbyY2sP8al1rCfVJYZRLJzaW7IzkJ6S2DJcl6fD9kFz-XlOPqDSqEDoGeBQKTmAWQXMfTO_SjkicHhrZQkJC116i3o2FU_zAqxFmBvx3E2AeLed9r1i5s08K4oA8y4qhVXEXcVHjZ2aqPYqndzoUEH9HIHJBl6ktNZUyga7uj-C78bEtMupyurh5nDWdK70l4PkVHiCqJ_qFVbnXsEb81pCxNVPltEl2p1zwTtO3nP5ViqS_eWoCQSHyEh79yheMefd9EX56c3oPKWBIvE25Zs4_iydYcCzGQeLsQftWft9lHg1IH_fO6JF-5DHhkpSGZEsvxDJiRGopX_PqHOQXhmyw7wwxTWNV0Vyi_LqojPOi-VnH1BxwdRQf-yI6YyhSEdZTOHiwbiFXXPWQvjhH3KnIHHqZBwykJs8LjSHlCxJw8GV7Dw4Hm9_-X-mpJGSaOuc7S6HkV2Aazjo7AcML7DnIM5jjORj6_j3X9afWaiScFlHor7HeWkNoYQqti5JQo7myt95ABedHL90dE1hARUv3wt-LGsoOgWuY6PLcHmhsxM4zIJTLAez8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
گل‌پنجم بارسلونا توسط گابریل‌ژسوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106053" target="_blank">📅 22:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106052">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گابریل ژسوس
😂
😂
😂
😂
😂
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106052" target="_blank">📅 22:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106051">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پنجممییییییی بارساااااا</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106051" target="_blank">📅 22:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106050">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گلگلگلگگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106050" target="_blank">📅 22:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106049">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e47209925e.mp4?token=Fy0oqAH1VO9foaQfOzhxms81XdwVqo0_eef4iTzxnpGCc2iMKGFApwC-6U-LZf84WZuMg7TAXSQZ2DS1rsNdRKL3vmR7HRLqZVTFPd4B5hghQQ5yQyTCZCRWnzuBYeVjZVRo_Q_IEc0SZm_L580KT-D5aaMpZ42g6-pmhtKr-pyyxucdq1XtUDiNGqC9JNTGChWfGy7gT-OsAbrgZlcao1B30aF1M9zRILZQvvmrAq1t15GbiVFYQ835kBZWXbXQlT9RLDXGC26A0ax6-L12CkHglxfxo-_lLb4czSWtWJJxEfq8YDemw9wbTantCh08nSvk-KL1fUUzgdt5WYWDz4BIQ3stLI7CBusOJ-KgkA8ry6zVX9zZJ-dd_H8Bu9TCwm8QWtqZxUgeWnIh2LmaN_zxWmqdUsP6GLd4dO0yhYX0ae9_zTmU8kP-uXxZOEsPdbIUxc7q1__rpTrnCSHsJ9_R6wYoHHl2rFxa5w5AjPYypCsOdWMtt5cf-yc_XQVLA16MMPVWUguSQBnqa9ZzcijWoWpIpZqxfLSW8UhOxqu4Ep9pcTZwy5loZaBRs3KkhkbTBApjgF6nSKMek55HrmbJtnKEvunv_FsNRgILqTViiWNpP_B7zm71cBSSl4RaWV3dfaHu5J1ZBp2Tg4ma3VbKW40M22V3PY1YuRlelP4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e47209925e.mp4?token=Fy0oqAH1VO9foaQfOzhxms81XdwVqo0_eef4iTzxnpGCc2iMKGFApwC-6U-LZf84WZuMg7TAXSQZ2DS1rsNdRKL3vmR7HRLqZVTFPd4B5hghQQ5yQyTCZCRWnzuBYeVjZVRo_Q_IEc0SZm_L580KT-D5aaMpZ42g6-pmhtKr-pyyxucdq1XtUDiNGqC9JNTGChWfGy7gT-OsAbrgZlcao1B30aF1M9zRILZQvvmrAq1t15GbiVFYQ835kBZWXbXQlT9RLDXGC26A0ax6-L12CkHglxfxo-_lLb4czSWtWJJxEfq8YDemw9wbTantCh08nSvk-KL1fUUzgdt5WYWDz4BIQ3stLI7CBusOJ-KgkA8ry6zVX9zZJ-dd_H8Bu9TCwm8QWtqZxUgeWnIh2LmaN_zxWmqdUsP6GLd4dO0yhYX0ae9_zTmU8kP-uXxZOEsPdbIUxc7q1__rpTrnCSHsJ9_R6wYoHHl2rFxa5w5AjPYypCsOdWMtt5cf-yc_XQVLA16MMPVWUguSQBnqa9ZzcijWoWpIpZqxfLSW8UhOxqu4Ep9pcTZwy5loZaBRs3KkhkbTBApjgF6nSKMek55HrmbJtnKEvunv_FsNRgILqTViiWNpP_B7zm71cBSSl4RaWV3dfaHu5J1ZBp2Tg4ma3VbKW40M22V3PY1YuRlelP4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل‌اول فاینورد به بارسلونا دقیقه ۸۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106049" target="_blank">📅 21:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106048">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cbc91a214.mp4?token=AnOqd8IcSpvxgiETr0_9_6q9b6EIw-kDK4v49I3N8bCFZuvG_IaDTwhmal6utpG-drf3EYZq8g03sov2PN7pGrr4Y_zlM0186PlGDFdIqtJoT8MJ606-wh5UWVZ9Gbh73e5OWLxlqdPWR_5HG3lubQxkRCiTBR3cn0yYs2dnDl71CJx2IXxjkl0wRElvu9zcWHqS8GJa7L9vyeO3zUWptN4vUzlr1T7VOUuAPdyjt3dzn7KVTblzRuy3Ypa5S5zwMzkacXDBUbnURaaNt3WNaTN9akb-1RZsfD7fqp2UFVT4dz3kv2KwHp7f8TqTyQvw0ia7b3wiHbUNlO9GQmXNdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cbc91a214.mp4?token=AnOqd8IcSpvxgiETr0_9_6q9b6EIw-kDK4v49I3N8bCFZuvG_IaDTwhmal6utpG-drf3EYZq8g03sov2PN7pGrr4Y_zlM0186PlGDFdIqtJoT8MJ606-wh5UWVZ9Gbh73e5OWLxlqdPWR_5HG3lubQxkRCiTBR3cn0yYs2dnDl71CJx2IXxjkl0wRElvu9zcWHqS8GJa7L9vyeO3zUWptN4vUzlr1T7VOUuAPdyjt3dzn7KVTblzRuy3Ypa5S5zwMzkacXDBUbnURaaNt3WNaTN9akb-1RZsfD7fqp2UFVT4dz3kv2KwHp7f8TqTyQvw0ia7b3wiHbUNlO9GQmXNdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🐐
گل‌شماره ۹۷۹ اسطوره کریس‌رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106048" target="_blank">📅 21:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106047">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فاینورد بالاخره یکی زدددد</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/106047" target="_blank">📅 21:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106046">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گگلللگللگ</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/106046" target="_blank">📅 21:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106045">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/064c2da039.mp4?token=KyNUc2i9zW0bRzPl83FTw17od59UHJi6ymU6-kSbYmDjMsgU_e3vDicuk9fNbMw5dKe1u60IvNQE17G3VYgEmEVAF5bKSA3AVWyHSlLGqBXuKWc7P9QXVo_hEShxwK5vphfgdsL_BIAeeTXcbUkHI15nHRB3kT7RGn304vn2g-OPK2CIA2RgQJgoiXRBH2-g42vQmS9yRk-wsF4Ag1T-KyLY7Rqqvpw552EmZ-cyICEsWfs5JV8xXcSOzPtHddHynXNhPIKWbIa9ym3pM6KEwuXrMhCQfA_2E-z7rVjpUQVtY-fU36yscJHIqkr9PWFPC0RsBi3tLhpHEhkbquXIHw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/064c2da039.mp4?token=KyNUc2i9zW0bRzPl83FTw17od59UHJi6ymU6-kSbYmDjMsgU_e3vDicuk9fNbMw5dKe1u60IvNQE17G3VYgEmEVAF5bKSA3AVWyHSlLGqBXuKWc7P9QXVo_hEShxwK5vphfgdsL_BIAeeTXcbUkHI15nHRB3kT7RGn304vn2g-OPK2CIA2RgQJgoiXRBH2-g42vQmS9yRk-wsF4Ag1T-KyLY7Rqqvpw552EmZ-cyICEsWfs5JV8xXcSOzPtHddHynXNhPIKWbIa9ym3pM6KEwuXrMhCQfA_2E-z7rVjpUQVtY-fU36yscJHIqkr9PWFPC0RsBi3tLhpHEhkbquXIHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌چهارم و تماشایی لامین‌یامال مقابل فاینورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106045" target="_blank">📅 21:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106044">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سوپرررررررر کاشته تماشایی لامین‌یامال</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/106044" target="_blank">📅 21:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106043">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گلگلگلگلگلگللگلگلگل</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/106043" target="_blank">📅 21:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106042">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
🇮🇷
👤
برانکو ایوانکوویچ: بزودی برای تماشای یکی از بازی‌های پرسپولیس به ایران می‌آیم و عشق و علاقه خودم را به این تیم بزرگ و تماشاگرانش تقدیم میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106042" target="_blank">📅 21:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106041">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sk-9JGeZreaTcFmJ2q6xaMJG6G0WMVCB6Grdu8VYJRG3y-opfgHAkmddkiJcdWkFhRWo7MhSGk3loH8zUXV_wuHYnUp3VEZHr7SctAWJpqhPxbsbPCBAPfr1uNmjdQIbmwJfcQvjg6O9Hi0ekNy6i2fx0d82vTL1WjP4tzKAF7re1ijW_Xetqiu485ZsHABmv73_WNoC35kvm8zmhgJDtAAjvZpZ9ou2-G4pulWQzNto-PFkZthOv6F9LcnaCO9JdjwpofUIzaNwu1tq2gmr7dAtc3hAqaiIKB3-ofwmQwtLAqLMlYxH_KkyPNe9hrgWrHM3z37WWpXq0zwHulr6tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
❌
گل فاینورد آفساید اعلام شد</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106041" target="_blank">📅 21:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106040">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇳🇱
گل‌اول فاینورد به بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/106040" target="_blank">📅 21:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106039">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/890fd0d430.mp4?token=gpVf3xiDiOsoGgtyKtc0ZftMIU9mYHM9rBZPz_GWikcsaJtJkiBzFYkEBVercBLTqieNMJB7CbArvw204k2ghLh0Vlke1ET9GWZaoo3VRbIS3-qkDBZ6A6oG87joGtLTSkviVaMfSK18hibs9-Hu9UgK1F_ZLnOQRLs1YOejYva-b-fLtavCRFXHsWnFuc30h4Fh2RraTFVW7kHcS6FQv0-Ljq-PUlqMaVKA7OyFjkUoJdavJ2WuhWZCa9iytHiHc_yR3smeYXS_vXK5UpUGa8AB3PzfQ17EKSnaXUja7El9oxqBZdsLY-ovUUfejIMBDip63Ft3oyBte1cwPXQCDaL9mywGSjFYJSxZy_04le3wQfFaxmXJfubAOVeminY1tMqw8GtIh5plP9IgSv1KOdVHhjq6bs8MhS_ZJHycqAOJ7KvR0mYGe40jVtdOIeFRr-eml59AEg2eUAWB0lUS8eUjogrL-rZOppTDoVyNBKYl-x_IiYJZXP6fDv0oZBoSFAZTpcmThpsrJVSMo8h-9Tgxp5gHJ2qqk8iXnzSoCA76swDwkRkPcQDxuAFOPHR4k4CO8P-3KMh5G3lqVSqo5na03uLUQL7f0ESyhBJ1O8bmkaTovZv6Xx3ctR1pIKHGQF-9BKySbto1RFtN58rTDWwpmDpY21ZAra80-YU8hlg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/890fd0d430.mp4?token=gpVf3xiDiOsoGgtyKtc0ZftMIU9mYHM9rBZPz_GWikcsaJtJkiBzFYkEBVercBLTqieNMJB7CbArvw204k2ghLh0Vlke1ET9GWZaoo3VRbIS3-qkDBZ6A6oG87joGtLTSkviVaMfSK18hibs9-Hu9UgK1F_ZLnOQRLs1YOejYva-b-fLtavCRFXHsWnFuc30h4Fh2RraTFVW7kHcS6FQv0-Ljq-PUlqMaVKA7OyFjkUoJdavJ2WuhWZCa9iytHiHc_yR3smeYXS_vXK5UpUGa8AB3PzfQ17EKSnaXUja7El9oxqBZdsLY-ovUUfejIMBDip63Ft3oyBte1cwPXQCDaL9mywGSjFYJSxZy_04le3wQfFaxmXJfubAOVeminY1tMqw8GtIh5plP9IgSv1KOdVHhjq6bs8MhS_ZJHycqAOJ7KvR0mYGe40jVtdOIeFRr-eml59AEg2eUAWB0lUS8eUjogrL-rZOppTDoVyNBKYl-x_IiYJZXP6fDv0oZBoSFAZTpcmThpsrJVSMo8h-9Tgxp5gHJ2qqk8iXnzSoCA76swDwkRkPcQDxuAFOPHR4k4CO8P-3KMh5G3lqVSqo5na03uLUQL7f0ESyhBJ1O8bmkaTovZv6Xx3ctR1pIKHGQF-9BKySbto1RFtN58rTDWwpmDpY21ZAra80-YU8hlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل‌اول فاینورد به بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/106039" target="_blank">📅 21:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106038">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گلگلگلگلگگلگلل اول فاینوردددددددد</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/106038" target="_blank">📅 21:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106037">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d0ecaa5ad9.mp4?token=VagbBsNU4hTaWyebwcn6-Uf-xPtsNj-SjLlo6GaSJpD2gF-zysgYoQ-PirhPDolrJQuiKpxBtPlgiMGilUlyaWEhgTPJJXXEAQvIU3ju3tp2KC037j_GfDA_j_V5dbUtffe8Ce6xOQ6CAoupxPpOKo4GpehwS5USwxmqIRdibVSxCFWu-_lg6Us4Febetbx_vz68cgjQQjsw9hFp3DAAiNj9fy8ua4NFQT70l8xCT5fBjfRjD3mYqa3H0rphGJv9bgszuglLuj8AgVoVQc2cgRcPfInXfmYSvNsdwaWoCLlfju0_LM9BErWuwV6-ptqlzEGbGCTxKv2BdsP0OjR51A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d0ecaa5ad9.mp4?token=VagbBsNU4hTaWyebwcn6-Uf-xPtsNj-SjLlo6GaSJpD2gF-zysgYoQ-PirhPDolrJQuiKpxBtPlgiMGilUlyaWEhgTPJJXXEAQvIU3ju3tp2KC037j_GfDA_j_V5dbUtffe8Ce6xOQ6CAoupxPpOKo4GpehwS5USwxmqIRdibVSxCFWu-_lg6Us4Febetbx_vz68cgjQQjsw9hFp3DAAiNj9fy8ua4NFQT70l8xCT5fBjfRjD3mYqa3H0rphGJv9bgszuglLuj8AgVoVQc2cgRcPfInXfmYSvNsdwaWoCLlfju0_LM9BErWuwV6-ptqlzEGbGCTxKv2BdsP0OjR51A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
گل‌سوم بارسا روی پاس محشر پدری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/106037" target="_blank">📅 21:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106036">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پدری چه سوپر پاس گلی دادددددد
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/106036" target="_blank">📅 21:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106035">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رافینیاااااااا دبل کردددددددد</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/106035" target="_blank">📅 21:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106034">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گلگلگگلگلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/106034" target="_blank">📅 21:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106033">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUqaXpTfshmg8f79G17NFjC7fto6evSQjc1PRf-J8GA84pToIU_fkjPqxxPrwF7kZp3tKc3mXztib9CoNKEiya6li5pU6iuBQ6gs1nkswIDlFvbJ_UhxG9K1WGg9ERuhzIDmnp77nlA_PZHEhfKACUIRfNP8U2ZEtaBsyCWQAdEBE2YgaaZPi9AOowJS7wcAcr8S95A0spOIN84svtLOh9MGz8kSfXnDTk1w-mCMgznQXAKCcp17VWftV8Y-afC6hJPzthj1EFYZ42MxQ3fI6GYyN8sNW-lCGP06i9VUHpRbmOcDaEciCBZgcewsCwqg8Srh49aWMRnMHk07bVMOmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚡️
🔴
از آیفون 18 رونمایی شد.
چهار رنگ آبی، آلبالویی، مشکی و نقره‌ای.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106033" target="_blank">📅 21:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106032">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhChPXF3bs1KBBhD93tYEGyEZKfLEvoC4CkUaQJGPEY-iw1xnfO1VFev0hiKIwJJ9HcsKTe3AmnUQstjTsM5M_2G0TWsVDfvbKEY4ecyg54P0snWn2O9rCDgcGFRkvxk5g2G4JW-DU1W84DPagvmy8IREDj1Ryin3iuGSiwL1glku1_Q1Xkrx_0vuZRyOdB8cZU-mguu5kyARTAPLTCPrYFfvnW3rm8Eg4bopmqsE3XVbIe8OkH5KtOZC_SM4FCa2q8N4q4epu5AxypzJGVWcuxsgQi_wpPSuJZcVn9Zy2ZbgjKTTeoyo3Hz9OghpmV03yuo-3hIJmUC4uEtvjznyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
ترکیب لیورپول و اتلتیکومادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/106032" target="_blank">📅 21:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106031">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dO_FEGu_gOfDEJDFm6u0MHIF9tvFn6ZunfS7vxQfgg4NQ1khh8S_OQ6sPfVbwae338KDqZPgHHS4SLiHcVkdRi3FHkTGE40ZSkOQZ2Lcwt-pF6BolitQ3uNZdsIMqKSiSgdEtbTtHDVz7fz4Q7gI5GAaTd1j2AQotYHQ1HPL-NBd0SSxhq14oiFBdSDXfnZBs7G7eWfaOxHN6fy-BUPjED4Fe9EgWaXeZR4Sf9EOXU2rxJmjSmg9b1EuMkdi4b0N8lGjbii-GOkvrRieqZ_7wnwPHf982BFkrTgfNhJPBBJoO9JNHc2ZZQtWjw6tCg09r9FpBXSDm_vnJ_2AYELabw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
ترکیب تیم‌های ناپولی و آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/106031" target="_blank">📅 21:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106030">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0aFcENMJHx6Qyojh2K5NGQfNUpq3F2QKV_3WavnI9pReHOsMvyYDEnivzmwmU5yxMXNESG3M8ko0CWfp5d9XHOeI6Tk5TabhFfXHFzAQxa5IaW3SKVpxRUZDvqm8o8cW9yP7eR92yh7cEV-VXk9kLYQF_KitlmN2XlDNS5tAs3aD_W4NPzGa3gBbXUuX_3kya_FD6UDi8Qeh3yZijuO2ZrvtiADKDJ4HcoA5s3eThm_TVvngQ-UvK6FONlL5IEF-Hf0CYZsQ_3OyRtOkvif8ZYtHyy1GvVAFPw5YMUzmSgNqOmvmHMq4p1Q3nF0oYyZf0oZdN9AffpSLfJocRWfMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
پوستر باشگاه پیکان برای بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/106030" target="_blank">📅 21:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106029">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c8eea35c2d.mp4?token=UWVGbsyfibnPod5FZxCrHy_CSiusqMfaEs8jBfHB1reE1t6loR-b0ezs80eAraXxlsOjdsOGbXW_2vZCJGgUyCUSd7qDo7MC4T69asb4snzpoWignXrE4yvJJwiL3mviOkqv-GK5Htxylf7GYVTG7zrlz6Kp4QNk7qxsAF80iZrNOo8J8Y9ss7KYXoUXX52w6l1aOkAoH2qsTTnnh3cDWQsX1NTHAEp8OwWgQzaDI1sIKSJERtUCXcxDIxZPV2oIDejkrEYDQWqtBuOMD4CYt76OBCZ13_fq0Bl1547Ogqmr8MOXBSWaDwnO3K2ysjyFNw1BsThwVHHDMGCeBzcnGopWCeUvaWrqSeK-JxIf5rCijk_HlVu5PQ8TabLiH9dd6QvY8ybVOAEAg-iFAbYDsGhzRO-5fscuiygFXN4-nnWn2wImbAsIYIF1TXiX2IOIf05Eko3oXNzWcKwXFYLWVXQmvucOhq85nk6I7tX6idBimxURXOo3zZS5y-5QO-oUTgF0XQM9FgfplE0qXCkTgpdiIoRwKwrUGj9HvqeqmQSqZhFsNIJGs3f6D9fI4o2cWlH7OgrlQJwgW1GCqpUy0P2HpLJdFrIsqZgNJj3I5hi3F0xiT1bWmJIHo30qTXvUPhgitomUOycECZJD-Yh1h-WTLq2SmTGvF-oVmlIzcJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c8eea35c2d.mp4?token=UWVGbsyfibnPod5FZxCrHy_CSiusqMfaEs8jBfHB1reE1t6loR-b0ezs80eAraXxlsOjdsOGbXW_2vZCJGgUyCUSd7qDo7MC4T69asb4snzpoWignXrE4yvJJwiL3mviOkqv-GK5Htxylf7GYVTG7zrlz6Kp4QNk7qxsAF80iZrNOo8J8Y9ss7KYXoUXX52w6l1aOkAoH2qsTTnnh3cDWQsX1NTHAEp8OwWgQzaDI1sIKSJERtUCXcxDIxZPV2oIDejkrEYDQWqtBuOMD4CYt76OBCZ13_fq0Bl1547Ogqmr8MOXBSWaDwnO3K2ysjyFNw1BsThwVHHDMGCeBzcnGopWCeUvaWrqSeK-JxIf5rCijk_HlVu5PQ8TabLiH9dd6QvY8ybVOAEAg-iFAbYDsGhzRO-5fscuiygFXN4-nnWn2wImbAsIYIF1TXiX2IOIf05Eko3oXNzWcKwXFYLWVXQmvucOhq85nk6I7tX6idBimxURXOo3zZS5y-5QO-oUTgF0XQM9FgfplE0qXCkTgpdiIoRwKwrUGj9HvqeqmQSqZhFsNIJGs3f6D9fI4o2cWlH7OgrlQJwgW1GCqpUy0P2HpLJdFrIsqZgNJj3I5hi3F0xiT1bWmJIHo30qTXvUPhgitomUOycECZJD-Yh1h-WTLq2SmTGvF-oVmlIzcJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
سوپرررررررگل کریم‌آدیمی مقابل فاینورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106029" target="_blank">📅 20:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106028">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlNTgCyxX3gAaAiSevtQhBGlkAQ-x1fPLxQfD0HXhAAAl8IVZf0YEtQrCfqAVe2zJ_0Sv39N_7J97VcrcPWWA-7q-dt8Ikpxd1CpEsb1E98WRaEqclVxJJe6DKMad2r8FmoZvVFSYpvznphxlO5U4fIMRtzEoOGQz-ndNoa37lbgNFr4VZR_g9EPdLDM_vgQwUsewTSz_tfWPG94_vtPa11svKGBvS2SGAN4NdFruKKVkSTKN8an6_1Zz93DY4hIgpGEefKYwDOojCmpivTHqLH94oRDXftuSwKWN1X9K3cBgVxIRtjAqqrbTHlIsNkLk3XFlkhoovW9YKU8ielkIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شادی بعد گل کریم آدیمی
😐
🔥
😐
🔥
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106028" target="_blank">📅 20:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106027">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سوپرگلگلگلگلگلگلگگلگل کریمممممم آدیمی
😐
😐
😐
😐
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106027" target="_blank">📅 20:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106026">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گلگلگلگگلگلگغگلگغگلگلگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106026" target="_blank">📅 20:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106025">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6q0WlEMQdiDIbX6prcp3amUD_okc6dw3WaS5btUMfopM39NZRg7Z4B2wE5g1n8q_tDCyrdu9X8NH-Ke6f8PDrxRIzbboCWkS_FRLoWF7fbaQkaPPCmA9_aw2vOxfshDp8RK4Ot2MxAPIyBLyx0rylHKgjonWzSZem7jISgCaIA6MRVBQyB_HmdkRNkf7HddtXbRL70vgoPA_FEuiYM5XcUf8OUD7VncntpIWbEoBVIE0nknF41FMCXNTQ6lj-l49b1gio_IXavriN5w9EbqIXeSTJ47icJM1XEEd3tx0GJY9XY-volsTR4GAQvmH_GBV61Ufs2GqVlEfbQpwoay8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلووووووو ببینیددددددد ناموسا
😐
😐
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106025" target="_blank">📅 20:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106024">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1f0f0fa3.mp4?token=rF9F5Q-HxReHCGERtccOJjW61JeriAiiT7xRqgvy04Th5StkrP1Rc4PxzLW7cEehXhGxAsu53ma5VEv4RQB3k8B_Jt17AsT_ug5GXJwDv_L0rEs9ZTyCnw9LDkwHI3MRxORaw1mKKwE6gAA1MLWmVBixoOy3XguU9dxDtZKXV2vstMLZxTmAWDkdtLO8sz2x_hEQLE0ZKhLrZeG_xH4tNbcvvudMwZ7MfiaRAC2qh-MNYVvsvhjVJ0cym-Y0VSSsrDCFkBYVySBckjFbj5CKbv0TgLctRa2YfjSxswYLbb2VBrl6onaTQayMtnrTlkMjhB7UYKiB8hapq7ZjGCYVhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1f0f0fa3.mp4?token=rF9F5Q-HxReHCGERtccOJjW61JeriAiiT7xRqgvy04Th5StkrP1Rc4PxzLW7cEehXhGxAsu53ma5VEv4RQB3k8B_Jt17AsT_ug5GXJwDv_L0rEs9ZTyCnw9LDkwHI3MRxORaw1mKKwE6gAA1MLWmVBixoOy3XguU9dxDtZKXV2vstMLZxTmAWDkdtLO8sz2x_hEQLE0ZKhLrZeG_xH4tNbcvvudMwZ7MfiaRAC2qh-MNYVvsvhjVJ0cym-Y0VSSsrDCFkBYVySBckjFbj5CKbv0TgLctRa2YfjSxswYLbb2VBrl6onaTQayMtnrTlkMjhB7UYKiB8hapq7ZjGCYVhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلووووووو ببینیددددددد ناموسا
😐
😐
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106024" target="_blank">📅 20:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106023">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGQAL6QTR2ApEX0ka5gLxO2cASoG8a8lubLXgbLY1jmmagxzGm8Yt-eBp5eApJfO2qQz0dYeCCv5AG8-9V5wEhMjiHCqpKQQu5j_WplXZh2Q425clCv_o0pWG-zfbH3q7-iRW2ZRFmX7rIpwf-C0UbidaydCJUPNnnXv6BrFcI-9dlXl8WZy24PPQL4FkU_aKl8ZSO0Gz2qNQG7rcpXT_HfunNMVm5RmrRpB-m9i1qcon0VCL_rzNbHy9iumMEuZOf6FcsJ-kME4GG3CRtIyFS88QGsQXFBWnkW5fvJUShu0wHvUGQqoftpnZyQnKQ8rO6J1tN3E7JxaxBCuyHtCwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلایی که سر مدافعان فاینورد آورد
😐
😐
😐
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106023" target="_blank">📅 20:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106022">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اینا چرا این فصل اینقدر وحشین رحمی به هیچ تیمی ندارن
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106022" target="_blank">📅 20:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106021">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عجب سوپرگلیییییی زدددددددددد</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106021" target="_blank">📅 20:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106020">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رافینیااااااااااا</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106020" target="_blank">📅 20:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106019">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بارسلونا زددددددددذ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106019" target="_blank">📅 20:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106018">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گلگلگلگلگگلگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106018" target="_blank">📅 20:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106017">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aeda36fbc.mp4?token=X3WKJMpXM9kxBY4naYCu9770cMuvERF_T0WeiSu_BN7O__h1sPUdDUciNEon3T1aoQY9a27nRz3l4G63EYYm0GfuS_G56UqlRbqBIVQssrRVflzdvbDjDwRAB61B9rJM174Y0OAFuMuXPmWXrqauMlumv-45Jrvil5Uvvm_LAPA6V3Mq4y3yvCTCIeo9TaCc1qYVB24iG-YrwR33XWsHnm1GRYoagJNKljRWBNdpx6t1gSvWF7kuGE08tl0yqPzkurop6ED7m37ESGlMFeptXpmqEdZRg8-8ET6O-6oZjxFWUYOEc_t-O9ZocXMhQjwryhD3Ek8AbtnYWlY960sXcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aeda36fbc.mp4?token=X3WKJMpXM9kxBY4naYCu9770cMuvERF_T0WeiSu_BN7O__h1sPUdDUciNEon3T1aoQY9a27nRz3l4G63EYYm0GfuS_G56UqlRbqBIVQssrRVflzdvbDjDwRAB61B9rJM174Y0OAFuMuXPmWXrqauMlumv-45Jrvil5Uvvm_LAPA6V3Mq4y3yvCTCIeo9TaCc1qYVB24iG-YrwR33XWsHnm1GRYoagJNKljRWBNdpx6t1gSvWF7kuGE08tl0yqPzkurop6ED7m37ESGlMFeptXpmqEdZRg8-8ET6O-6oZjxFWUYOEc_t-O9ZocXMhQjwryhD3Ek8AbtnYWlY960sXcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
باشگاه سپاهان از طرح جذاب توسعه استادیوم نقش‌جهان اصفهان رونمایی کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106017" target="_blank">📅 20:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106016">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8t7eq05kP9pcKbvRwI2Sis2L1ruGLr9KvR1PsrvKpi4XPIAqDjpUM23xrhZMB7OXC9gEQvY_U8iJR6sm94LXDgV230ecmSspnsgbKs_Fqp_g0x67Ky77InLltiz4GfSF520bwgJZdZH3vlr-sjz8_oLjah4Kvh7-tKeaPeWQyAyBOwSLKmwL7IzT7WteIENquTbp9Kkbdcp4S1pPNmnnLWhOVciuNMmT7ByNFwd4ju50SplrcOuLe6rqxeC5LmXPdTrM1ynidZbR_X_qQXuLLaCkkBDHVGichCldGV4GQDMyRLu036HOrWa6RIrzgu6HsRvZFi3fhjdbh3s88xg8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
📱
استوری صالح‌حردانی بازیکن مغضوب استقلال برای دیدار فردای تیمش مقابل پیکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106016" target="_blank">📅 20:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106015">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2ncqpIj5iHHoChOwGMmlKC4zd_zVinbz_vub5RaQVI8vr5y03U-QXqcYSE8ybJgSiQMfIfv6oiVs5AxL-40PvRcBXrsP-_UdHEid4u4gVtPZSmVds1jxXAsCOuKjmyz7OxnuukcXwsg6QS6Vz1TPIAedY_Fn2KpN_sE4pGPIOfCdnACKeCBMcn-ioDEdD3xYtCSAzELvp5fWqQJrIle2hlsx7ENYK2KRF-iW7HyxAcqhqKHOQJsU4Dzj51Sh3YtIwZUxpecUsTThoSSHxfsWRkeznSepeJjSVFmD8-jaqoNKA2058r0sU4LES-Rc5I9I456ZS08sm12sM06mAE1TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
📱
استوری صالح‌حردانی بازیکن مغضوب استقلال برای دیدار فردای تیمش مقابل پیکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106015" target="_blank">📅 20:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106010">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NGbpQGelmlXkEbKwiKwJM4IWpRM1AXsR1g5pTZSUlCm2t0OnZ0tHJ0NaVJd575KvO-edxXgzP-IPokZBJpJI_hTQIHy4Bj8lGMrCU9_qQ2BIKZkmLTtJrEHWJ5q51hY2PAJX6PSiWydfdvUjbTW5uZkN3Rv0sEIeAM8-izsDR1aavuR3eqdPc5QbzmVjixCDlgsBG9tX_AeGqXLiSySkg4G6gB1JmmxYAherlWJty7CtVaXHhCLvYralkI7nyqYbeWnG49TKAUNqHnr9owbG7pWiQ5UkUrmdXr1_dJe4opwUc5MUaoSrZtW6fr6uLW0NQ960Tjpt_MhJPHEUmo2Bpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i5Jnvj3Z01c6-WJZ9pwc5eCQUhMgq8iCUuDEJ49R-ELe0Wz8r6BLi7NbZpjv4k1m5OJ2H8XYJhu52AxKrTeTOsuWcQJuTBBVmUnXeKaW_Ngt5p1bT2ZysicxsEwxnPrrWX7C0XK_B-xbPRE-NUOKqKT_aNt2HLqCVsRLrOQMuEcMn5OXToDTJ_276_f0w2jRQ-1jbgdzpKLYFJjzq4AeK3FoH_zQ2yKoUKp4NcFPwYIkG4oM4BUbMJaagiHtS27xlydXm2iedW2-Rb-uPoLM7Dj7iUroIcXdSHHWGRq0-nGdcd6WnWr2JVqaP8NzhopAe6Eqlc_J29J0s4co6uweQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ayr1XtwyJKDkI3eNPpaXduekoP4bSawyeTiol0UW3US1aMdP4RvjKczpSiR90lgaPyaq9ZPuTrtJiKUuQHHknUa1VbKTfhPs-2AzJgftBIlv109HAgGX9Z4NX65Vyy71icsJ4gvd2RLG7uIY1YRTnc8-Oqz4fY0jry5V67CWHl_l6jGRfh3cCqzFSAtaGTtutIkU7aJscRRRCpSMemM4XU1B4kn86ElY1fvnygcnLNrKXIsWxTWQpWSZ6yrCwlMqCVR__MEeJ_ihYlIUhXs6PZkwLVxVEPjByTC10LdSqaZuuquQv5R9a3-mmeVvv_x34o5uZNa4dqEK-hlOjwrFOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qlbxQanS375JUps3dB3cZZncUddwDI5soB01YhKUyCEleSsNcqXnOrY24W-xFSALbkfMfqXLEc9oMTSw7iwIZ9fua6ivER7Kd4IQ_b9tbdp_jGNHd6Y9CnKVWZS6aQHVKDZvvTpYtxQeZOZMOnbXdHRiJ-8gxXLEzhsKiDrxtnIP1dyq62Rzoz6a3WnEOrwFidpZseKoeKRP17cd_BsOq-aljkEmGOnKEG5hCrqEoyo-9F5CMFRyHQSGWeIoY6UzkqF05q9jmwwINmaORro4Nvrp8FKzW4HxgyaUn13XvyEh24qdh5peppebrN2hSKCKKxQg1Rv2r81kPgLKCUlInQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fXj_Z9D9KgFTUULad6ONeBwpi8ev4BdJG8LwA1XAlMWZruFCp38s1uIoJnUzYRnA2zYaju06w8I8B04_gaBo2eB78tRI7m_oqSeCItW4_EV0ZxqUED3SQ5uU_YjZ6gKMNL5jAmoDXSP88_Z21zZQcNFcyQve-n03AlosqwHi0EARnLtjYURM8eLtWWkI7UghKbut0KYYPL2J4gXzR1opCKbnEhV_uGdOSsnCN9GeV8IN5ceChU_Vnl-vyEruc9JYU7u5bpQR-5g_emz37Gb_7j9r0KlVApp8QDM83ctGOPhGrq-MYCGcNSvnoUozaSh4SA0dlnW-Z-mun3Evuq1mqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
👀
خانم موراتی از مجریان جذاب UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106010" target="_blank">📅 20:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106009">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0NHZ3lQKEMLjtCSW7y_c1j-Jt_1EHpWJ_R-Qag_mq_4M37p_bTAmEBuRr2vIBRPiiPrh8jdXOXogLkyPvyyefFJQn5R3_iX4lptjQTUMKvAlNJ1JmTeSfmX3-NEH4jdKAoIai8ReDSJ-LZgfcbG402KWn9keDxEx1I9pyHOBSRPlVlDUK-4WSWBHIhyjjqRu9xJbxIIjo7JKXNFo58lYJtkGY-6HpzItH9qNsK4doYs5vBeUqk5GibeukR-L5CzB6N6DwemBMAUjnbTnMxU2gFMOoi7YRfp6wXMEam1cvq6lOLtXmWyi0bhiLGmJctwH7PBpDnqOWYcQNWCHXT46w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⚪️
سردار آزمون به لیست تیم‌ملی فوتبال ایران برای فیفادی پیش‌رو دعوت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106009" target="_blank">📅 19:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106008">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLbA0HqfXfqcZkCEXxtAWj2S2oR7Ngr8MkqVZadoJk1kuPgDkVk8X8OJNqBBNq7539ha3m6cR0Jhoa-kTEeyOIBNgMEq7eyTJokofWdBS6jZRBYxT4W8iYrdYbhgiW9VWTlP3dYDWes0UtCJd77t-7c9Ye3XjIIBkymWiMEyF_W4GHsyYn9LodoHqM3RPlQF7rKFlqtUP1jIEqj2thkTgiR0ww7XRocnoRNnlnjOVMj7e7KZjfj8uoOfsT-tBhg85XwaFcSQpYaAoNxHYJMkHx1oO9Y_uyDz-mAij1e8gUuwPUjNMUQk-ntQfT0mlmkEHdW-OTO6P2cpijWKyCCW3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
🇪🇺
⚽️
آمار بارسلونا مقابل باشگاه‌های هلندی:
🏟️
۲۰ بازی؛ ۱۱ پیروزی؛ ۷ تساوی؛ ۲ شکست
⚽️
۴۵ گل زده؛ ۲۱ گل خورده؛ ۷ کلین‌شیت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106008" target="_blank">📅 19:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106007">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTYORrjf--ovBTkviajeU8yeYdQUUnVCtH5swh2Um6IQFXCkPoGkLf65Irg2fEVliI8y8W9H7ojN2Qwiw25kcOanGDVenKUILerHX7wWuSwu6DMJQrq37oNuHO0x30djSuIHlVvGL0XAt9II-pR35xrOM9VVz07NBEUJ3TkqC_fIzS_pi8BegaBb5cbuy8Bd8Pn4Qhe4NrKSYdb8pehvOGcPkHsjUzJyOqPGcGvBaKUIAs6KlHwhaARcQwu_LGYSDbLHz9z_0-5tRViu3zYtNajcbWpQ_bki-V5KvD9hBr0Aq9EiwKPWeqdJ0wdOpYDmkD5SBfN5unzloCdWNGT6Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇪🇸
ترکیب بارسلونا مقابل فاینورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106007" target="_blank">📅 19:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106006">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3Yn8xMc2p7ToIvdZJkPtmsM1atDObDe52gMZUHtQpVgXIlhpPSNoJpDFDWCbbIqc4O6jfaBj0ulsL9EmulPPl0RZhqD4C9102JYueZXNY_nCDfb3D0wVIinRDd1vODmsRClZVboDpnIrQDPHsUSiEPJRVFsWCX8hi_A-CkzLFPIzDvQBlSx4QW7JZL1yzL-Lrqso0oYQo81pTZpCEv65M8vzFus5cZ9Ej_si02shLizxzbeP9LvDSECFfztwE-F27I2oUQk6dP5oEjBMkZAP5-gZxwwgnJvVJCrZxI2xzbPjGMNpiUbK6rIOnzHWT0S9AnjEfj9zu-mXsi51pryZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇪🇸
ترکیب بارسلونا مقابل فاینورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106006" target="_blank">📅 19:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106005">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2045d20cc.mp4?token=j1ikGVZ9LGmRIBff63n0L9VUFVuHXmAC64Bjt9s23A3fBtGzKmDS32LcSuTgSBBwqIQa4M7RCd0E-vagZJEYGj3CSJDGIzza74MXOHiljHBKqV86-u_MPdzMkBFT4MWWy-UjKnTFIG3S1-54OgtiVeGWlwDrMTX2yJEnHP-x38x0TjmH5H4ua-ZY2KN7Y9-BOwGxTsqNkad3_rwlDau1AiuJmb0P1j_oaLNfAOL9RrbBZrmWygD4unZhz-vMnTucaas57P8okudiV0X8yDo5EfW5N9t1icg1EDxODP3016AHgGqgyeIWcIjcNlJONhHesYfb0w17t265uJqH6G-DoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2045d20cc.mp4?token=j1ikGVZ9LGmRIBff63n0L9VUFVuHXmAC64Bjt9s23A3fBtGzKmDS32LcSuTgSBBwqIQa4M7RCd0E-vagZJEYGj3CSJDGIzza74MXOHiljHBKqV86-u_MPdzMkBFT4MWWy-UjKnTFIG3S1-54OgtiVeGWlwDrMTX2yJEnHP-x38x0TjmH5H4ua-ZY2KN7Y9-BOwGxTsqNkad3_rwlDau1AiuJmb0P1j_oaLNfAOL9RrbBZrmWygD4unZhz-vMnTucaas57P8okudiV0X8yDo5EfW5N9t1icg1EDxODP3016AHgGqgyeIWcIjcNlJONhHesYfb0w17t265uJqH6G-DoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیزر جذاب از بازی امشب اتلتیکومادرید و لیورپول در لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106005" target="_blank">📅 18:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106004">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCPF6Xny5AqqHffPzDPUT56u8TCCYyGYt63TUPkM6Bg5oLyuhi4-6kBM7K_MXz2aR_tKHgK0VcMpQgPtMIIdo4A8rJABiISYCIzT3d1hPmxzvHIkaERFaCdIJ63_mqWlyr2PMwh3xscNIdPctPvs81rFkwvRvP29XUqYkDC4X7vWfZSJmPhnoBLWZf6HsQxnYRRRC2sbp-rark8i7Fh0moqJh0vQXorfsTMD_4tO22nKaz6ua2iW4gvWXMvwOdwWzo7MlZOQX_BEkzEhGfSeA27xUCD5XamddmMXjPSFEW4TVjjzZJZEeJ_YQEnqvb0UwQA36G2ISdiW13kRR1GywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
😳
😳
مدل موی جدید مارکوس رشفورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106004" target="_blank">📅 18:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106003">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c95f05bffb.mp4?token=SWXhphi4X4q005x0JMNfEUR9TU8quNXLylV2xmjKJqzQaU3qijdcfSzI9EEPZaFjWs5ZYBB8Q5bxNGT-tcjcp3aLPDDw12kUD432u-0_J4B79PV5-8cQQxvzKH7VQRyk2o63ZCFRn4YyAswxh5wC6090r7nut5w_tsoyoxqq2sY41NRrXwfeufLFJ4VKlv-Q9ni_DIwX2wTgOEBL3W7thQL5zJXtOvnwq8GrKv8lnIDAW5QaJSa_Sr4r07RS_eThYeLNmAWjcV3kIOe69DiTGYC74d2xPwsmsuuHGYS-tpRwsGG7ppIOKNxEiVNmkQiqGUM-PH54hrsVZ8EhcREfHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c95f05bffb.mp4?token=SWXhphi4X4q005x0JMNfEUR9TU8quNXLylV2xmjKJqzQaU3qijdcfSzI9EEPZaFjWs5ZYBB8Q5bxNGT-tcjcp3aLPDDw12kUD432u-0_J4B79PV5-8cQQxvzKH7VQRyk2o63ZCFRn4YyAswxh5wC6090r7nut5w_tsoyoxqq2sY41NRrXwfeufLFJ4VKlv-Q9ni_DIwX2wTgOEBL3W7thQL5zJXtOvnwq8GrKv8lnIDAW5QaJSa_Sr4r07RS_eThYeLNmAWjcV3kIOe69DiTGYC74d2xPwsmsuuHGYS-tpRwsGG7ppIOKNxEiVNmkQiqGUM-PH54hrsVZ8EhcREfHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
✅
سه‌قاب و سال‌ها خاطره‌سازی برای مردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106003" target="_blank">📅 18:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106002">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsJVw0mcfe6eKNmfKmyLuikzU0dySK5BmPPlbOEmxZwDO7XCKgoWlfUa_5HIertvyiIoE1bpgFw_Q6rPeMVmwNR6MpF_dHusNUnJtrhz-T4vA0MZXMFO4o1u_KjbleN-tH3Zp6qtLxOnPh5I43NyNnuDXkg81RHR4rINYDS5zxvis1E2W4JC3msB5R-hrxhTc48JSOQd9epsSvPcdFRCZh8wHEiqE3jjJE4yTSnDa59oB4zon0d6iD-sKHrq8eSNdOTOvZA4DUXN2NSXAuyAfkevOnUVsUoSigvpyEU2FxLeP5QC3nOguvFiRR4AnLqx9pZGwDlLarhq8IxzvBRDIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
❗️
تصویر جدید از استایل فاطمه‌پسندیده و عاطفه رمضانی دو بازیکن سابق تیم‌ملی بانوان ایران پس از پناهنده‌شدن به استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106002" target="_blank">📅 17:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106001">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8mC5S0hlrX1vC_aUptiIO4F--_Q-WPA2xiHKcIeyzWIgcyW-AnbLAQ08RzeuGlXtJ-tuRmvod23kgkfSHvGUxuZ19BsMEDmo9WKakvevVNcBKwdzQTzWjmN6ytqBJQcGEzVpmKvkdbwAYhcf5fuo9YKv4uWhFTNlnmmtXkF5d1owBFfMuVzlUMdt0bnkF4D9J6DN_EV9sUS97CvP4-mtJ1_NJ1Lx82T6M7ZNyVo1zs5VFjXDWv0OV4hjn_pp_2RaIJ9vxSPcITKgM3A78aPOMLRVng_rj_ybbuWHA9TtYruY_HzJNRRjyok7OkKKkHl4IdRHM3v1-gXmVYdDkWz5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇪🇸
برنامه مسابقات امروز لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106001" target="_blank">📅 17:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106000">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106000" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/106000" target="_blank">📅 17:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105999">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-SzeAXM8frUtHsvky9PqfTIgWXxsc5N6GN6z2FUr9VLY00NwfGkYN_Uw7moRNuLfzIpuXxFVMYGpo-rBH-1cVeCOP7bUB6TQsr8IvYDKCMVmbdDNxclEK4Z3Yt96sITyTT_bCg4NINLsi6Hkn4R8Q-hZZaVRRIXBpvzwcwVzDex69oMNGCxVBOj_cjssK5BGXcZvcGzJkW_jQx0rl4x23G3NNsFrBN_lyn6ZBR_r8xawoXZOK9IgfLH5LnbIc-tx6o6mNm9GgH3r-UmqP1Fqso6U5D_qqR_DN6wMqvF_XvYiHJ7ov7MnkQbctJaeEjXJElPHTnAPsD9qc45ad-z_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرسنال
🆚
ناپولی
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
آرسنال: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
⚽️
ناپولی: ۵ بازی ۱ برد، ۱ تساوی، ۳ شکست و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105999" target="_blank">📅 17:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105998">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a6458393.mp4?token=ubsKuYGsbhY3S0alTAHNVrGnKQgarWuJzQfLD0i_VCrJOGntcnEZdmj2A3GBEmSvrXJ0CjDzDvjYVtbH070YUXudRPns71ET9djbjvy6CZfK_QDQ0DEwmWqMpXhTcq2Jn7V3B_rsUJfemnT99G1kntrcPtm6b9-Mkn-bN8J5XZIHrsAaAJsZzAGTui3r5cFXxaFjTXEUy9k0Xx-5aVcZ2K2Yg0i1eKd1NOOGT8RwL3T_ZLkYjmShcHdP5LAcOASkmafj2A0t_j_wJmFoFFOqAzWtDnebeR6i0vArG2AcYYmAsWloHaLLq32oxqlDqLh018QF2Uk7oJBLPaHUIgDyRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a6458393.mp4?token=ubsKuYGsbhY3S0alTAHNVrGnKQgarWuJzQfLD0i_VCrJOGntcnEZdmj2A3GBEmSvrXJ0CjDzDvjYVtbH070YUXudRPns71ET9djbjvy6CZfK_QDQ0DEwmWqMpXhTcq2Jn7V3B_rsUJfemnT99G1kntrcPtm6b9-Mkn-bN8J5XZIHrsAaAJsZzAGTui3r5cFXxaFjTXEUy9k0Xx-5aVcZ2K2Yg0i1eKd1NOOGT8RwL3T_ZLkYjmShcHdP5LAcOASkmafj2A0t_j_wJmFoFFOqAzWtDnebeR6i0vArG2AcYYmAsWloHaLLq32oxqlDqLh018QF2Uk7oJBLPaHUIgDyRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇮🇷
🇮🇷
تیکه‌به سهراب بختیاری‌زاده به سبک‌ جالب مهدی تارتار سرمربی پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/105998" target="_blank">📅 17:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105997">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04d5f7ca29.mp4?token=OnFU7MmMmINVcL4rV8-GvbJViq210uibctsShFerJIZw763ItVVKY3B4HxqPmma9iM8I9kEVMBEbvIfdclGMGt3ze9KM1QK7yHahNti8SHmkLYeWlOOPKghBHArB0rTLUy52Kvb3-gEa8aLhcM4QRH2a6HAFFYEDAXyv9qQO3ihEyPY7eDXlxDurP87WdE2wLbnGv3YvAHT_HOlFCtPhopvlTKTcIhwOCl1GfGI4GSEGOXNipZRIe_qJGgqJc1UlDVeWuo5G9e3qQVNKv8Ly-3ULrTG7FxJ48VH4RIlJjBgGNKIxONLN_Tojr2ZBSnTeTMxGmltRfUp7m-5GoaqI9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04d5f7ca29.mp4?token=OnFU7MmMmINVcL4rV8-GvbJViq210uibctsShFerJIZw763ItVVKY3B4HxqPmma9iM8I9kEVMBEbvIfdclGMGt3ze9KM1QK7yHahNti8SHmkLYeWlOOPKghBHArB0rTLUy52Kvb3-gEa8aLhcM4QRH2a6HAFFYEDAXyv9qQO3ihEyPY7eDXlxDurP87WdE2wLbnGv3YvAHT_HOlFCtPhopvlTKTcIhwOCl1GfGI4GSEGOXNipZRIe_qJGgqJc1UlDVeWuo5G9e3qQVNKv8Ly-3ULrTG7FxJ48VH4RIlJjBgGNKIxONLN_Tojr2ZBSnTeTMxGmltRfUp7m-5GoaqI9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✔️
یامال:
🔻
"فقط کافیه تیم‌هایی که این اواخر جام بردن رو ببینید؛ تو پاری سن ژرمن همه پرس می‌کنن، اینجا تو بارسا هم سعی می‌کنیم همه‌مون پرس کنیم. در نهایت تو فوتبال امروز اگه ندوی، هر کسی هم که باشی، همه تیم‌ها میبرنت."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105997" target="_blank">📅 16:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105996">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94734143dc.mp4?token=RfMHFCZge-H7R9e5NENJt75Nkd3bpUGYIxXP5nezvGPMOe19w95BlIziEHvMKJse0HxOLWkiCVmfF_PLwTEfT_SIEBby2S69fRf_uKzw2dkoaqsahUviuLQ9pGGHKZl9O1cwz73yVlzSryvqGqzGg7ZF-dq3A5Fp1SSBrNTosrdqlVAjNhZX5BEWIf50LLMFZvqJlpqDJL0k7fTx-_p6vA4W0JAqcDV6V31rJfU7kZ5jV3HFS8b1CRfGZmT_UB4QRpFgdNHT6DuyW8Yw47W197OZE2KyFQPzmRn02YyAvOLYKGb-cTcQUSkfHNNIlfCTkTbFAwN_8M5DJZDaCEW70A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94734143dc.mp4?token=RfMHFCZge-H7R9e5NENJt75Nkd3bpUGYIxXP5nezvGPMOe19w95BlIziEHvMKJse0HxOLWkiCVmfF_PLwTEfT_SIEBby2S69fRf_uKzw2dkoaqsahUviuLQ9pGGHKZl9O1cwz73yVlzSryvqGqzGg7ZF-dq3A5Fp1SSBrNTosrdqlVAjNhZX5BEWIf50LLMFZvqJlpqDJL0k7fTx-_p6vA4W0JAqcDV6V31rJfU7kZ5jV3HFS8b1CRfGZmT_UB4QRpFgdNHT6DuyW8Yw47W197OZE2KyFQPzmRn02YyAvOLYKGb-cTcQUSkfHNNIlfCTkTbFAwN_8M5DJZDaCEW70A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
بانوان جذاب ایرانی در استادیوم‌های مملکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105996" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105995">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a6a8f2ee.mp4?token=lzRF3QFqcErzGmDvOLUBVkg0zLKAyDBHK0CSJz1584SAHKDHxzt2cJj-5nGvwi9_aiPr0dBCpz2anzadmcsmlxtH5fFDhFziDwX5EzZHVCDYO3bgHNF3ixHcO8C6H9j--hRUhv7mnvvS7mltg9rkvQ_qbjfhsXU0w59kUxy68YZGWIkZinA4wbj1vhiWTdgskwb47LwJW8CUrsoUl65naka1SRj84ZtYNv-fhBEIgUKIj6cKXw2wWFQDHowwUDZVo_UrwRGzNz2QCryXz981_-iTCsbu9WfLZ7AR-f2HrK1LwObCew6xyLJfnnRJnlXU6z3G2Oy4o7K8NHzdn318cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a6a8f2ee.mp4?token=lzRF3QFqcErzGmDvOLUBVkg0zLKAyDBHK0CSJz1584SAHKDHxzt2cJj-5nGvwi9_aiPr0dBCpz2anzadmcsmlxtH5fFDhFziDwX5EzZHVCDYO3bgHNF3ixHcO8C6H9j--hRUhv7mnvvS7mltg9rkvQ_qbjfhsXU0w59kUxy68YZGWIkZinA4wbj1vhiWTdgskwb47LwJW8CUrsoUl65naka1SRj84ZtYNv-fhBEIgUKIj6cKXw2wWFQDHowwUDZVo_UrwRGzNz2QCryXz981_-iTCsbu9WfLZ7AR-f2HrK1LwObCew6xyLJfnnRJnlXU6z3G2Oy4o7K8NHzdn318cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
🏆
لامین یامال: «لازم نیست کسی را قانع کنم که من شایسته توپ طلا هستم. هر کسی نظر خودش را دارد و من فقط به کاری که در زمین انجام داده‌ام افتخار می‌کنم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105995" target="_blank">📅 16:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105994">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f3510400.mp4?token=ZHHv9ftCbDrtNR18NNPJIgs2k2SiN-sXfK15xZ8vrQJwx1wRiQdhRTOc9oet3oGwUu_U113e48nTg4U9pmMTqZzD4myC0ECOOWHSWZUDuGeRWxNmglM3dhZy1P_S8p8BLqsexUIKU2uE8CqipD1vfYGI4-2_P4yc1PhhWxlklYtkDXtV9ktrL1LOmz3qxNBGesQ3FS9fFQiHNyXXJ876rlmTHkjE2heuqHMbMISr3TwijZzzOdAy_kiFdImnx274vSDhC-nBAPbNWM4sOXEsZQjwneRjaEOaqtSlIFq6BxMnNUGdF2yqGYmwXtQfRJJ8qhuiCDHDtUZNAcoj4EM5fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f3510400.mp4?token=ZHHv9ftCbDrtNR18NNPJIgs2k2SiN-sXfK15xZ8vrQJwx1wRiQdhRTOc9oet3oGwUu_U113e48nTg4U9pmMTqZzD4myC0ECOOWHSWZUDuGeRWxNmglM3dhZy1P_S8p8BLqsexUIKU2uE8CqipD1vfYGI4-2_P4yc1PhhWxlklYtkDXtV9ktrL1LOmz3qxNBGesQ3FS9fFQiHNyXXJ876rlmTHkjE2heuqHMbMISr3TwijZzzOdAy_kiFdImnx274vSDhC-nBAPbNWM4sOXEsZQjwneRjaEOaqtSlIFq6BxMnNUGdF2yqGYmwXtQfRJJ8qhuiCDHDtUZNAcoj4EM5fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏆
نظر هانسی‌فلیک درباره توپ طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105994" target="_blank">📅 15:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105993">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d749e34c6.mp4?token=LPQjF-JpRun6KGwrgY5yynRaEhuFl59fgMBcZJoImG7_J-8cnH5PsQ8QqfboiBQcO4HXgDhVbC7hSROhjgTTRZBMxRwZrb_mxu6asi5MJYUw2ak5J8OOp6VwCd2mUpDFAgy00QPo5s-aP3Ds63lPUpwo6fdTA2M-IBFpg0UlrgXfVlJu0-i5l3FF4uZ78CRFkjjr9_0tOU2eqGBPUxcPOKms-llpH8oAkBT8Nku9MoWi_bbh5-orECyRU5rsR8kUT9NtRTJPVKaAY054yAwhfbf3U6YCtQdtu00bXk_LY6YEQozRTI7kqI9syHxR-EOTZdTFV50LURUtFs5ULMCRRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d749e34c6.mp4?token=LPQjF-JpRun6KGwrgY5yynRaEhuFl59fgMBcZJoImG7_J-8cnH5PsQ8QqfboiBQcO4HXgDhVbC7hSROhjgTTRZBMxRwZrb_mxu6asi5MJYUw2ak5J8OOp6VwCd2mUpDFAgy00QPo5s-aP3Ds63lPUpwo6fdTA2M-IBFpg0UlrgXfVlJu0-i5l3FF4uZ78CRFkjjr9_0tOU2eqGBPUxcPOKms-llpH8oAkBT8Nku9MoWi_bbh5-orECyRU5rsR8kUT9NtRTJPVKaAY054yAwhfbf3U6YCtQdtu00bXk_LY6YEQozRTI7kqI9syHxR-EOTZdTFV50LURUtFs5ULMCRRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇪🇸
🇪🇸
لب خوانی صحبت های رودری در جریان دیدار بارسلونا مقابل والنسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105993" target="_blank">📅 15:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105992">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f76b6880.mp4?token=sqCOUg-nYJGZ4EytkRUcDdnhqsADBa_lVnbrS2vm0YB2jZwHD291a3145UdEDfW9J_ezZ6ovdO2v5gtlxQfGPzNoOHSMTanMoUWjuOW5OWNv4ElwICNU-OUoU5J-JnbeocDd8QuY-ledI9Vg0PMxi4fjY_ch069mWy3S_sMTCBfB0iOIkTx5TWvkbL9HNaQruEo-dfzxulVPQi4G_kRg1jwB6fQAkb_uIrh6-AMZGNCChd4AwnFCW7I9pDAK-pJ7QuVcJtUd7lC0HZ3NPrixGSzwEdhzIDP1xL30KqNmIW06ybrI_cDVVfgC9zHIvH7sxbAv6RqHxpDlXiuTURbCAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f76b6880.mp4?token=sqCOUg-nYJGZ4EytkRUcDdnhqsADBa_lVnbrS2vm0YB2jZwHD291a3145UdEDfW9J_ezZ6ovdO2v5gtlxQfGPzNoOHSMTanMoUWjuOW5OWNv4ElwICNU-OUoU5J-JnbeocDd8QuY-ledI9Vg0PMxi4fjY_ch069mWy3S_sMTCBfB0iOIkTx5TWvkbL9HNaQruEo-dfzxulVPQi4G_kRg1jwB6fQAkb_uIrh6-AMZGNCChd4AwnFCW7I9pDAK-pJ7QuVcJtUd7lC0HZ3NPrixGSzwEdhzIDP1xL30KqNmIW06ybrI_cDVVfgC9zHIvH7sxbAv6RqHxpDlXiuTURbCAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
ماجرای صفرهای ثابت پمپ بنزین‌ها مشخص شد؛ جدیدترین شاهکار مسئولان برره‌ای مملکت
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105992" target="_blank">📅 14:50 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

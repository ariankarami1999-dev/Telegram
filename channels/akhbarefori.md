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
<img src="https://cdn4.telesco.pe/file/EO0nGAgN7y0ioDz39dUd0ETLm18aF0ymHcc-WZ71t5mKinEnKubP5tVyT7PcYd8JKmO3K1r7i-GimMyqfB6KgF0fX0llHfYhQ6NZP5b6q6OVkvCRtYqtYtt8HntatS85WMWU3m20-2bZhNVe_6ltm0NRtpOSsQrM7D1lV5jAokEjNkfjLUxb5O3uzHbuZtp51KFFTBjNpZcSLQk438bWS_FVcXALVyVDHC4FaTWPu_I-DpHtQsaDXnPJv3nNVZ0WbyMbEpOHo5S72a23iZnfMCY6Dq4l1AHYmHB0T3eGBwZ9hkQrfQHFlW7CBbAN_k3XwpHj0_QbrBKrl5_52LX9OQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.35M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 22:18:40</div>
<hr>

<div class="tg-post" id="msg-673553">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe2ecc4084.mp4?token=vYxHvQ8Tp0Qb_iorPeuiJkrxhN7JY8ERGWSiKwl_0RnUoaHIUzlfIQvb37drP3NTTycADJCm_9wFw50UzWxyRtQVKmu9Dp_hHFmcNcqC2WLrXtcAnEZFB5UKx53EYP2fSYqV_s-4xSsXfbX9YdFeSyqFbUkdMJKgZlgbdZCxVhKYfvC9cT5EXps0ux32rR1XaQwhl1b5KPuqyhHba1aK5cCzWS8CZl-OYl1rFmuwFPJfgek1KiXc0rhpmZ6ti8cIgjGM7p0qrSSXs-uN40OExQ3is3_4SKVlN92SQZK1KXesHvz9p8FnFJOXYVOcZu2coyk68Eaa3-Q-i0u5n5W3lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe2ecc4084.mp4?token=vYxHvQ8Tp0Qb_iorPeuiJkrxhN7JY8ERGWSiKwl_0RnUoaHIUzlfIQvb37drP3NTTycADJCm_9wFw50UzWxyRtQVKmu9Dp_hHFmcNcqC2WLrXtcAnEZFB5UKx53EYP2fSYqV_s-4xSsXfbX9YdFeSyqFbUkdMJKgZlgbdZCxVhKYfvC9cT5EXps0ux32rR1XaQwhl1b5KPuqyhHba1aK5cCzWS8CZl-OYl1rFmuwFPJfgek1KiXc0rhpmZ6ti8cIgjGM7p0qrSSXs-uN40OExQ3is3_4SKVlN92SQZK1KXesHvz9p8FnFJOXYVOcZu2coyk68Eaa3-Q-i0u5n5W3lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باقری، معاون دبیر شورای‌عالی امنیت ملی: ترامپ بچه‌سوسول نیویورکی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/673553" target="_blank">📅 22:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673552">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e770738336.mp4?token=DExLzKhgXF06HP2JJ2je5syZW8y6OVb9X8tBNBGg0zC_KI96mjLeBKN7sleAA7uTqpB0Ds2l0C6sWdwhHlNeFe7rnfZfe5Tl9BKfLDFIyVg_RHguEf6qX49izGuGrB5WBXjEk76PQeQhf_NJEwJc6oDlgok6u6qE1706SsdR0clnUMlR_hZTqDuLzEUHB_QHXucquzDDXBpFWfN077OJCvlfoGzb2qs1mRqdZYjEwYscDkt2362lb6qmfssXOFaGc-R48_b16o3Ba-eRGS0OjsPLGVDXugr4LLlv85s5LqSvM557OpUX7uAyaTN2PR5xKfBKXJsgvnBp-7VOVtfFiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e770738336.mp4?token=DExLzKhgXF06HP2JJ2je5syZW8y6OVb9X8tBNBGg0zC_KI96mjLeBKN7sleAA7uTqpB0Ds2l0C6sWdwhHlNeFe7rnfZfe5Tl9BKfLDFIyVg_RHguEf6qX49izGuGrB5WBXjEk76PQeQhf_NJEwJc6oDlgok6u6qE1706SsdR0clnUMlR_hZTqDuLzEUHB_QHXucquzDDXBpFWfN077OJCvlfoGzb2qs1mRqdZYjEwYscDkt2362lb6qmfssXOFaGc-R48_b16o3Ba-eRGS0OjsPLGVDXugr4LLlv85s5LqSvM557OpUX7uAyaTN2PR5xKfBKXJsgvnBp-7VOVtfFiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تطبیق تصاویر ماهواره ای سایبرالکترونیک سپاه و سایر تصاویر ماهواره ای
🔹
ایستگاه برق در بحرین مورد حمله قرار گرفته است. ایران ادعا می‌کند که این سایت یک مرکز داده C2 ​​و هوش مصنوعی ارتش ایالات متحده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/673552" target="_blank">📅 22:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673551">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrlP5yRQwAnNSnodOeLnGVhK3LFEs-kzoIMWQ_BuG8h-WDanf_NqYUjO44sjOKW9vq-VPhG3D9gUakTMnUXCnf3fqX7rrOQZ0LcJ97GB2YIPwCLbe65_gsCH1n6iqmdxmJIBFMcVHa8TKXvIds0M2Ve3s9hrwla7qyWugiiwEFaAIT5kbkoYG5LdYSOaSLEfIjIHT6q98Ihij3u_DE4-CHgRufIhOdmBB8-ac4AvOeGgRoQcRomTMmbohFAu7t2dBXWA2XCkTiasA3c4vSZOoXVd--wRmcfCmLriq5x2lYrRLubwQEnkoDMj9FgMwZZN_8roE-qOztxrvDaXLEVbLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از موشک ایرانی در آسمان عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/akhbarefori/673551" target="_blank">📅 22:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673550">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
امتحانات نهایی پایه یازدهم تمامی رشته‌های تحصیلی، در روز چهارشنبه ۳۱ تیر ۱۴۰۵ در همه استان‌های کشور، بجز استان هرمزگان، مطابق برنامه ابلاغی برگزار خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/673550" target="_blank">📅 22:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673549">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
آژیرهای هشدار در اردن فعال شد
🔹
منابع رسانه‌ای از شنیده شدن صدای انفجارهایی در بندر عقبه اردن خبر می‌دهند.
🔹
برخی منابع از حمله به فرودگاه ملک حسین در شهر عقبه خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/673549" target="_blank">📅 22:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673547">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AplHrrjkVDQ9v9F7rLDZR_KOq-S_70pUY8BtrHkyEMqWSBkh9WzZVklGYPtvqO3YE4mP0vlqWU9lRp97Lrnomj9-IlzdjVodR0OTqq8QDVggpi-_WrThhBJstY1g5RLkWkjgxK7wHSg8qSD3KuTHIrg_5Ys5tHsOL-lJ3mla77LUhnSlkFH99Xs3gWKNFZka96jOnZoZ3B4ZstoezqGRxcKwOjMsUnprwyrkAk5nxsN81EuT_xNBXW8LIpgg4EvuNfPi6cr1C9UkOJEFM4MdGoA9d0Dz9fU7xQWmeMh39uqqFHPdlwncTC4VETsPjgaumI89wvD8l2yjgzg86J4eQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bee633326.mp4?token=ZzglwbVQgpWdJDbMncQOIWduvdeUnbBBMxzERH7gA12mojQCMMViI2fVedMc5TvSBGvsREL5f9ZOfKeYMMoQVE-TkQxMEdgypsKT5n11Wj-vmuOLjxUf4luefPwx3TGCUzKaC1XB9gm8TB-7eRJOA2E3h_QtUdcKaeBAtO__MUlNed4nSzH3jQDzPHtbIeZz4MgTOmntffO9cM0mtmQ7_9vKT6oABRw3Csxr_0nGIF2OI8irgKffsO39q8Q084BsR31T7UgMMBYt3rMqaKVpw6wCg5X1dKDIMjk7nRt77VS2Hun3Z22MdYrCjtQWTih8MMcL5RdbAgzxMzwXV-4fng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bee633326.mp4?token=ZzglwbVQgpWdJDbMncQOIWduvdeUnbBBMxzERH7gA12mojQCMMViI2fVedMc5TvSBGvsREL5f9ZOfKeYMMoQVE-TkQxMEdgypsKT5n11Wj-vmuOLjxUf4luefPwx3TGCUzKaC1XB9gm8TB-7eRJOA2E3h_QtUdcKaeBAtO__MUlNed4nSzH3jQDzPHtbIeZz4MgTOmntffO9cM0mtmQ7_9vKT6oABRw3Csxr_0nGIF2OI8irgKffsO39q8Q084BsR31T7UgMMBYt3rMqaKVpw6wCg5X1dKDIMjk7nRt77VS2Hun3Z22MdYrCjtQWTih8MMcL5RdbAgzxMzwXV-4fng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر مواضع هدف قراره گرفته تروریست های امریکایی در کردستان عراق
🔹
ماهواره‌ای از ۱۹ ژوئیه، منطقه‌ی وسیعی از یک اردوگاه تجزیه طلبان و تروریست ها را در نزدیکی سلیمانیه در منطقه‌ی کردستان عراق را نشان می‌دهد که به طور کامل سوخته است
🔹
به نظر می‌رسد یکی از ساختمان‌ها کاملاً تخریب شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/673547" target="_blank">📅 22:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673546">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صدای انفجارهای پیاپی در سراسر اردن در نتیجه حملات موشکی ایران خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/673546" target="_blank">📅 22:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673545">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBenelli Motor Iran</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZgozSmPZ43npa_g4xuo65-bIxGyyrKOJS592wKWXtdcJ0CsVBwDrPEYl0eVFe1LKcZv8V988AgWyhuzrCMJX7-GSfGfnfvmyV-L7U_vmVKySiiYU7X1SFknHfbvgc_Lgr1i5J66Wj1g3cZCo-c33S4YuwQeyTn4LBySCB42hbmTQlkN186GDllCWQdCM90HXwOhrY096Rh8KPIa2BYpPV8vLxJE4EhifoBp5sPZMrIYDNCQMTDrAxGzX1leWSBrTb6hRCPAYDVmR4S2wlyA1WDdmREJvIUcpuhIU6115K-tI1T8748AmMDy5w9XMda8pLt8rujBH3zgEZ8c_dnDug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏍️
موتورسیکلت بنلی 180S
✅
پرشتاب
✅
طراحی مدرن
برای مشاهده قیمت نقد و اقساط روی لینک زیر کلیک نمائید
👇
https://l.nikrun.com/zsx
⭕
⭕
⭕</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/673545" target="_blank">📅 22:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673544">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
آژیرهای هشدار در اردن فعال شد
🔹
منابع رسانه‌ای از شنیده شدن صدای انفجارهایی در بندر عقبه اردن خبر می‌دهند.
🔹
برخی منابع از حمله به فرودگاه ملک حسین در شهر عقبه خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/673544" target="_blank">📅 21:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673543">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
زمان جدید برگزاری انتخابات شوراها مشخص شد
سخنگوی شورای نگهبان:
🔹
زمان جدید برگزاری انتخابات هفتمین دوره شوراهای اسلامی و همچنین میان‌دوره‌ای مجلس خبرگان رهبری و مجلس شورای اسلامی حداکثر ۲ ماه پس از پایان قطعی جنگ و منوط به مصوبه قطعی شورای عالی امنیت ملی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/673543" target="_blank">📅 21:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673542">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
شبکه اسرائیلی کان: شیطان زرد به اسرائیل دستور داده است که در هیچ رویارویی نظامی با ایران شرکت نکند، مگر اینکه خود تهران ابتدا به هدف قرار دادن اسرائیل اقدام کند
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/673542" target="_blank">📅 21:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673541">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
گزارش‌هایی از حملات پهپادی به مواضع تروریست ها در شمال عراق
🔹
منابع رسانه‌ای گزارش دادند مقرهای عناصر ضد ایرانی در اطراف اربیل هدف حمله قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/673541" target="_blank">📅 21:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673540">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d0531940.mp4?token=DrIkIjydUPqiPMwR521QobyBdc-Sc1VKow2KomySLNjuCye-48Q_tlo2ssK5MJwn2DKgCwtKXbiCbb8w_UUGsyeULjW14PeI82w-WIHnR6snYlZ1wWiwtwkGsztZlVguuBpEnAUlnh3otWQXcUnBF0gTvZ7qNujlMraKUaK2nyWsOy6zts5sYyqgE-NHF3lgtj_8ZEnOz462zrIEzFbQQkJCrU2Djy6C79VltPqo1qdoBzBrQqn-T9Pz5pVtESUP6xKcD55oYSezisWr2ZjfhFHhuON9nHQri2CtetCDBZdDH-aloDX8qhl8NkDW_ef2hhnLqpyz6WS1HP1eY-zGtwxnjcK9MR_tY96o_7Pu8AVxJKh6tex5Gs4A4L48eWxSFdAGzHKOYaevVfGQ1_IKA2DWzTS3_petpbLf8TT5CmqY_8JKLnfLcekz2GeS2aHcFjrBOH8g2wEXBSv7tlag0wkupto3N2HQnzEKxOrxDMIJPjE_ulLRLQy7pd_25Vn5sDUnRicL535qO3WPYOHlPOBJzb0tqbp6lk01EYEdfafi7orNdJo0teek5QBdnhk0ZDYnFT1136YRUW1LuUgSTEPl9fx20OiRZRSGk6G4O9OQ2H89TgFykPGU8qws2ZHH8B1KlUv1m6MHz6zv14dFl2FfW4uLfGDfSNIB3zQjvKM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d0531940.mp4?token=DrIkIjydUPqiPMwR521QobyBdc-Sc1VKow2KomySLNjuCye-48Q_tlo2ssK5MJwn2DKgCwtKXbiCbb8w_UUGsyeULjW14PeI82w-WIHnR6snYlZ1wWiwtwkGsztZlVguuBpEnAUlnh3otWQXcUnBF0gTvZ7qNujlMraKUaK2nyWsOy6zts5sYyqgE-NHF3lgtj_8ZEnOz462zrIEzFbQQkJCrU2Djy6C79VltPqo1qdoBzBrQqn-T9Pz5pVtESUP6xKcD55oYSezisWr2ZjfhFHhuON9nHQri2CtetCDBZdDH-aloDX8qhl8NkDW_ef2hhnLqpyz6WS1HP1eY-zGtwxnjcK9MR_tY96o_7Pu8AVxJKh6tex5Gs4A4L48eWxSFdAGzHKOYaevVfGQ1_IKA2DWzTS3_petpbLf8TT5CmqY_8JKLnfLcekz2GeS2aHcFjrBOH8g2wEXBSv7tlag0wkupto3N2HQnzEKxOrxDMIJPjE_ulLRLQy7pd_25Vn5sDUnRicL535qO3WPYOHlPOBJzb0tqbp6lk01EYEdfafi7orNdJo0teek5QBdnhk0ZDYnFT1136YRUW1LuUgSTEPl9fx20OiRZRSGk6G4O9OQ2H89TgFykPGU8qws2ZHH8B1KlUv1m6MHz6zv14dFl2FfW4uLfGDfSNIB3zQjvKM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آژیرهای هشدار در اردن فعال شد
🔹
منابع رسانه‌ای از شنیده شدن صدای انفجارهایی در بندر عقبه اردن خبر می‌دهند.
🔹
برخی منابع از حمله به فرودگاه ملک حسین در شهر عقبه خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/673540" target="_blank">📅 21:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673538">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1953e66d3.mp4?token=btSi5D9ZJCDTUJ2jKN46jZ3pnA9QaUXMX13AKLTVCMQuEFJ9mzvfWkLDjOnmAnDrl4k5J1vEXxvX7PpGMWHV87QSNdIlEVjitWPjT6d6bagAfPmr_5MwCZQfuRQfEp4ykDV1ZDn9JN8nRg5Go_b_4iPq5YpKUO_rTV_C0WBAZkZ1wmS_Wvab4kjFg4A3upJV-b46VTqWjjg95PCUAy2csO9XC9nyfXbYv2TbGbvy-ChXX-xDMt7-vD4woVWCi_hEeUrDrtAN1Sugeh9hykewPgDvbjuE_MSLRIBIIiGF84J36BQnOmwCCk92TJFMqipmwaO4P6kxoncChnWsAXBbAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1953e66d3.mp4?token=btSi5D9ZJCDTUJ2jKN46jZ3pnA9QaUXMX13AKLTVCMQuEFJ9mzvfWkLDjOnmAnDrl4k5J1vEXxvX7PpGMWHV87QSNdIlEVjitWPjT6d6bagAfPmr_5MwCZQfuRQfEp4ykDV1ZDn9JN8nRg5Go_b_4iPq5YpKUO_rTV_C0WBAZkZ1wmS_Wvab4kjFg4A3upJV-b46VTqWjjg95PCUAy2csO9XC9nyfXbYv2TbGbvy-ChXX-xDMt7-vD4woVWCi_hEeUrDrtAN1Sugeh9hykewPgDvbjuE_MSLRIBIIiGF84J36BQnOmwCCk92TJFMqipmwaO4P6kxoncChnWsAXBbAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای اصابت ها به پایگاه هوایی موفق السلطی اردن را بین ۱۵ تا ۱۷ جولای نشان می‌دهد. یک پناهگاه هواپیماهای آمریکایی در این تصاویر به وضوح سیاه شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/673538" target="_blank">📅 21:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673537">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل: افراد نزدیک به شیطان زرد از او می‌خواهند که پیشنهاد قطر برای آتش‌بس ۱۰ روزه را بپذیرد
🔹
ایالات متحده آتش‌بس را رد نمی‌کند، اما می‌خواهد که مدت بیشتری ادامه داشته باشد و ملاحظات بیشتری در مورد تنگه هرمز وجود داشته باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/673537" target="_blank">📅 21:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673536">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای مهیب در بندر ایلات
🔹
رسانه‌های رژیم صهیونیستی در گزارش‌های فوری خود از شنیده شدن صدای انفجارهایی در شهر بندری ایلات، واقع در جنوب سرزمین‌های اشغالی خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/673536" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673535">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/673535" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673533">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c45d5722c4.mp4?token=LSaoe09XD95SuHG9vVSFq5K0AD7FFlkrYYsKJ7NqdPoyZK2dd9IHg6htE0VqXVD8CdK_EO4mCefmu-4P2eaObHBXwG9vwvjf4Cu-PM-2nYnvRxhqZ-UtD4JcQ126E_92QIbMDKdh5kE8NoK1rJa3AhFSKXrJ17L2ZezldME-gd09OXURj40Ho-4Wne5hZo2ABRbqf9CHl_VUrEeI9d3zGTSFdImb_xarQfdR6qeHfvPUQRZIjaSiJ-qeokeArN2x8QfiNUOI5BJm8J2UQz5iNovQwzoPtMK93EFwF-ryfDa-iLzv20v9jnqwSo4UH_msqdfWLXgMa9IPd9FbbmiJtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c45d5722c4.mp4?token=LSaoe09XD95SuHG9vVSFq5K0AD7FFlkrYYsKJ7NqdPoyZK2dd9IHg6htE0VqXVD8CdK_EO4mCefmu-4P2eaObHBXwG9vwvjf4Cu-PM-2nYnvRxhqZ-UtD4JcQ126E_92QIbMDKdh5kE8NoK1rJa3AhFSKXrJ17L2ZezldME-gd09OXURj40Ho-4Wne5hZo2ABRbqf9CHl_VUrEeI9d3zGTSFdImb_xarQfdR6qeHfvPUQRZIjaSiJ-qeokeArN2x8QfiNUOI5BJm8J2UQz5iNovQwzoPtMK93EFwF-ryfDa-iLzv20v9jnqwSo4UH_msqdfWLXgMa9IPd9FbbmiJtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقتصاددان آمریکایی: هیچ‌وقت بازار انرژی را تا این حد تحت فشار ندیده‌ام
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/673533" target="_blank">📅 21:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673532">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGUCcvjYktX1Xk2nx59y9hlvev4MVFrP0eaumjb1KZT7qwxQkFYZBkq37ZVBn6QGOjWhHzS0d-EpOG3DjA7rpVXjKyUj4fpejzLvl4q1qgEwxKmhc24t5cai1EQ0ygJWrDnrWvxPxgGzo2aNmDlrUizb4yYS6VWUC1sKVJkeED0dx5SYR0FdWgTaBhBkrChqmOajui8B4Oti0NxuLhwiTJHr8rqT0RE2XtHylcDAY9wyz4oBLpD9bZQWXupMi0fAwXWg4ECyXztNDI4KLsT7_kQbhNYkyFnro0kL3IV3DgkfwfcuNeE6D8qte3-wd_pgpvg467vyyEFNWNwck-d_GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این جنایتکاران که فهرستی از صدر تا ذیل‌شان موجود است، آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد
🔹
بخشی از پیام رهبر معظّم انقلاب به‌مناسبت تشییع و تدفین آقای شهید ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/673532" target="_blank">📅 21:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673531">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a83345d2e.mp4?token=STrczDjYSwwZVOYlmK12sWYQx9WCpyGDA5YiX7y4453uXXh72bNcDjzofkOiCcxFvF5NbKJDuPqNEfsa6RFIcZVJKdKFsDTtxOhgtEhSpzYdpr8fiufOG_pzfLEDwB_exDiOUu8l7dK1e_s2RlXG8Q98cZeH4BpgB6rmskbRy7WuXzl1rrrBPEqK-4TDhEZ-_2vQOs6sGjJN6Put5pWDaOilw_5jfzJlviC8_XrJb3R0kpb0goJ4Vj6zGLzKhbhhobtuFOs-QRnG143dI0vMNqufLnU_RO1lqFuKaafK7ps2YFBs5BOdTvoeBP-lGK48hxcyuXqQDhJVWAeObykKtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a83345d2e.mp4?token=STrczDjYSwwZVOYlmK12sWYQx9WCpyGDA5YiX7y4453uXXh72bNcDjzofkOiCcxFvF5NbKJDuPqNEfsa6RFIcZVJKdKFsDTtxOhgtEhSpzYdpr8fiufOG_pzfLEDwB_exDiOUu8l7dK1e_s2RlXG8Q98cZeH4BpgB6rmskbRy7WuXzl1rrrBPEqK-4TDhEZ-_2vQOs6sGjJN6Put5pWDaOilw_5jfzJlviC8_XrJb3R0kpb0goJ4Vj6zGLzKhbhhobtuFOs-QRnG143dI0vMNqufLnU_RO1lqFuKaafK7ps2YFBs5BOdTvoeBP-lGK48hxcyuXqQDhJVWAeObykKtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امام جمعه اهل سنت میرجاوه ساعت ۴ صبح توسط افراد  ناشناس ترور شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/673531" target="_blank">📅 21:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673530">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
شیطان زرد در مراسم ویژه برای اجساد نظامیان به هلاکت رسیده آمریکا شرکت خواهد کرد
🔹
کارولین لویت، سخنگوی کاخ سفید گفت که ترامپ در مراسم انتقال نظامیان کشته‌شده آمریکا به پایگاه  هوایی دوور که عصر سه‌شنبه به وقت محلی برگزار می‌شود، حضور خواهد یافت.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/673530" target="_blank">📅 21:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673529">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKoybwM7XJ4a9uOIH9Xm88S6JMXNNKwyLiTl4qEHu1XzTO8ndQu7bdggb1O_vcSS-iUiYOlwdYaUpgZob6851LSvGowy5tbQ37wJv8MsmYehBf0kaNglPGe6fiDn6RjTwwFomPp8s6qTEhwuDTFYnXBFllnpWFf3GXPCKCVauXj2eEhCFjIR39Yxb4N-h4FDz30HXCrxa92TCWRpb-_DlDGo_TeROEinO1jtHVmqhcXJiyFHt4G2B0kfxS1LqUGziQwAYaXbn1-OYRLX4493w7Y_NhGgIOW1OornqlHaDYex1EmFLfI0NQ-GM-Ca8QogvH3G-v8cwNPwWCn-iLbZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیرانوند در بین برترین‌های جام
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/673529" target="_blank">📅 21:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673528">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی انگلیس از برخورد یک پرتابۀ ناشناس به یک کشتی در نزدیکی امارات خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/673528" target="_blank">📅 21:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673527">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b1297577a.mp4?token=rLVaGe8skcieUi_cd9hv7-KgWk-cqRzlFvQaLHQhmPTn1xLD-i3309K5Fx2IlGyZ_dARyBSioP2sWTzvXBQqZY1SmPwOW__PdVnoafJgaPa0bM-Ts0FqNJzKh0SOzfxBJwsABh3OgnPGXTMknYdIkq_4F2c8L6osJlEM9mhgFF5NLt3KrMeqYkp7ZOYYd9H7vJxf0SG11vrJLRzrkES-QXDOdCOMcEBeWCeIyC0SOJkW3nDdnWOUSsb7EeKh6hORKjNYlqELruGm8PHvRyjdyWfzVh3PwgA6E4o92CyLIvd58AiFnwgkhzAIVhWCqaotzAqr5TyoUNXIOcwHkEpuLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b1297577a.mp4?token=rLVaGe8skcieUi_cd9hv7-KgWk-cqRzlFvQaLHQhmPTn1xLD-i3309K5Fx2IlGyZ_dARyBSioP2sWTzvXBQqZY1SmPwOW__PdVnoafJgaPa0bM-Ts0FqNJzKh0SOzfxBJwsABh3OgnPGXTMknYdIkq_4F2c8L6osJlEM9mhgFF5NLt3KrMeqYkp7ZOYYd9H7vJxf0SG11vrJLRzrkES-QXDOdCOMcEBeWCeIyC0SOJkW3nDdnWOUSsb7EeKh6hORKjNYlqELruGm8PHvRyjdyWfzVh3PwgA6E4o92CyLIvd58AiFnwgkhzAIVhWCqaotzAqr5TyoUNXIOcwHkEpuLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناگفته‌های معاون بازاریابی و فروش گروه سایپا از هزینه‌های تولید خودروهای ناقص/ چرا خودروساز با وجود ناقص بودن برخی خودروها، تولید را متوقف نکرد؟
🔹
معاون بازاریابی و فروش گروه سایپا توضیح می‌دهد که توقف تولید در شرایط تورمی، هزینه‌ای سنگین به شرکت تحمیل می‌کرد؛ به‌طوری‌که در صورت عدم تولید، حدود ۴۳ هزار میلیارد تومان هزینه ناشی از عقب‌ماندگی تولید ایجاد می‌شد.
🔹
به گفته وی، خودروهای فروخته‌شده هم‌اکنون تولید و در کارخانه موجود هستند و تنها بخشی از آن‌ها به دلیل کسری چند قطعه، در انتظار تکمیل و تحویل به مشتریان قرار دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/673527" target="_blank">📅 21:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673526">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f99f42ba.mp4?token=Tv8CHeErATZ74sy0CzTHPJlmcJQSmJ_rEq6Nd6EA-4GL679nc3cBEXJFbOaWpMq2dzChvxRSt7JhIDJQyvTS9J5VHt-bzO-SozMUIpNxH7NnosGsjTZfHbmAFBFMptHhKtocR-E1X2sdIt4Usx52fFnrHBvLNwkiv24ASVVVWComPg6-AKktwfPiyFtpoTx8LvoBXa-LQSw7M9yg8yWbegOnrgBKvALjdQnaJoAr6oXx6B7R8J9gOFqYVff_u4ORIOF3dPRd06WTYhKsuuL6WInQxREforlUTCgSvTa7F8WcB5QqncJwH6Do-yhi5Lxm6zdacI_8vpYv205RwT81Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f99f42ba.mp4?token=Tv8CHeErATZ74sy0CzTHPJlmcJQSmJ_rEq6Nd6EA-4GL679nc3cBEXJFbOaWpMq2dzChvxRSt7JhIDJQyvTS9J5VHt-bzO-SozMUIpNxH7NnosGsjTZfHbmAFBFMptHhKtocR-E1X2sdIt4Usx52fFnrHBvLNwkiv24ASVVVWComPg6-AKktwfPiyFtpoTx8LvoBXa-LQSw7M9yg8yWbegOnrgBKvALjdQnaJoAr6oXx6B7R8J9gOFqYVff_u4ORIOF3dPRd06WTYhKsuuL6WInQxREforlUTCgSvTa7F8WcB5QqncJwH6Do-yhi5Lxm6zdacI_8vpYv205RwT81Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی فیلم: مشق شب
🔹
ژانر: اجتماعی
🔹
خلاصه: فیلم از مجموعه‌ای از گفت‌وگوها با دانش‌آموزان دبستانی تشکیل شده است... کیارستمی از آن‌ها درباره مشق شب، تنبیه، تشویق، خانواده و مدرسه سؤال می‌کند و از خلال پاسخ‌هایشان تصویری انتقادی از نظام آموزشی و شرایط اجتماعی…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/673526" target="_blank">📅 21:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673525">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFwDkF7-T6LKLvoaXS_Xi12t4-P8bLZdNluYgay4Qaj4yW_5Gfb6b-YeYkD-B36NI3ksSBcPRHCA2mWiKMZ0haYjw8v4DDqJ2zC1qqGhhVGqZO1-Vw51WHZcl_q-npvvNlxlbjDCHlLQQWXxJRkqgdTHoQ3GsN2GyMBH-Yl5h6S87I2T0SJ0HTXecliV7xxzDte-W8b66Q5r1fJVICdCUj1dpzqF2QKV5SKSfru5-InGzn2PUSGQBD47W2ZIuSZfskvN17m-rqybH0jPd5uwBXAlXJL7ZvsAu_VIq-njT5CQusK7tAWuV21qWcxyakXiIn8ILxFM0c9JZLQx0kLlsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارن‌پالیسی: برای بازگشایی تنگه هرمز، ایران باید خود را منزوی ببیند
🔹
ایرانی‌ها مصمم هستند که کنترل تنگه هرمز را حفظ کنند. آنها این تنگه را به عنوان یک «برگ برنده» می‌بینند که به آنها قدرت نفوذ در اقتصاد جهانی می‌دهد، درد سیاسی داخلی را به ترامپ منفور تحمیل می‌کند و همسایگانش در خلیج فارس و دیگران را مجبور می‌کند که از نظر اقتصادی و سیاسی جایگاه او را بپذیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/673525" target="_blank">📅 21:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673524">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادعای
رویترز: حملات هوایی اسرائیل در تاریخ ۷ و ۹ مارس (۱۷ و ۱۹ اسفند) به دست‌کم ۱۱ محوطهٔ تاریخی ایران آسیب وارد کرده است که  ارزیابی‌های یونسکو، شامل میدان نقش‌جهان و کاخ چهلستون در اصفهان می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/673524" target="_blank">📅 21:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673523">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1ae3f6528b.mp4?token=dQ_Ag5TymGTXJXkTVwnnVDOeR0lZv8zgOSBLb_BtVXyo8uVKlHWn32HTSJdI3SNFh67ZLpDLXilzBnnIHrjji2VZvGKkSJa_3HS6-pxOCgVxdmXGpST7DGkCFRjHL_r-iFzWo1EN1VYcg0xiJc6OFf1shoxq5Lp1pxtBSjPAygWF1K79Ye10gsV8KT6E6TmkN99-r4ACuLXz6VSe2aU3r1X94ePGUOTzySazwlVxCE401RAylUsO1ADJwb84Vi1BZRzhNIt9kfdM9Hx_AMOj1OTGZcWkpvrW-7yj_OobN0X33ebVm53P_9jsmr1-yjYLDOCohGEbQ-0B79XkYWKlyZ-sm4MJ91vSBM_aWkxfoyT6vtfbClUZX1K-EGElN5eAzepEkQwWceuYgv3QiXdmjzMX-6dAi5SoDfMgVGlrFUl1Tb5t0XegE1ypeQprKNkzrtKXCreigr8KhvKdAfuMR5nCpAFApqGX2PbKyCNeKdguL9Lj0H9o9laEi9AJlYP0htof68Y4BAthFYm0EczrhgrM2NzsTZ3fdYdAG3QaNeH-L_x-iZUTspZiysvPFEwSQADY1_h2MaiTqFknevul61Q-IlEt52mQfC4RIPlzo9wIJMriIw5UNqteVPnJ9SXycN_Vw1HaPsJhIFhANovhFwxfIuZUgjGpXeUNAOFjlp4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1ae3f6528b.mp4?token=dQ_Ag5TymGTXJXkTVwnnVDOeR0lZv8zgOSBLb_BtVXyo8uVKlHWn32HTSJdI3SNFh67ZLpDLXilzBnnIHrjji2VZvGKkSJa_3HS6-pxOCgVxdmXGpST7DGkCFRjHL_r-iFzWo1EN1VYcg0xiJc6OFf1shoxq5Lp1pxtBSjPAygWF1K79Ye10gsV8KT6E6TmkN99-r4ACuLXz6VSe2aU3r1X94ePGUOTzySazwlVxCE401RAylUsO1ADJwb84Vi1BZRzhNIt9kfdM9Hx_AMOj1OTGZcWkpvrW-7yj_OobN0X33ebVm53P_9jsmr1-yjYLDOCohGEbQ-0B79XkYWKlyZ-sm4MJ91vSBM_aWkxfoyT6vtfbClUZX1K-EGElN5eAzepEkQwWceuYgv3QiXdmjzMX-6dAi5SoDfMgVGlrFUl1Tb5t0XegE1ypeQprKNkzrtKXCreigr8KhvKdAfuMR5nCpAFApqGX2PbKyCNeKdguL9Lj0H9o9laEi9AJlYP0htof68Y4BAthFYm0EczrhgrM2NzsTZ3fdYdAG3QaNeH-L_x-iZUTspZiysvPFEwSQADY1_h2MaiTqFknevul61Q-IlEt52mQfC4RIPlzo9wIJMriIw5UNqteVPnJ9SXycN_Vw1HaPsJhIFhANovhFwxfIuZUgjGpXeUNAOFjlp4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
#تماشا_کنید
🇮🇷
تجارت در مسیر خدمت
🇮🇷
🙏
خدمات حضوری و غیرحضوری بانک تجارت در اختیار مشتریان قرار دارد.
📱
tejaratbankofficial</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/673523" target="_blank">📅 21:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673522">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فرصت ویژه سرمایه‌گذاری در منطقه آزاد سرخس
با ارتقای جایگاه حقوقی منطقه سرخس به «منطقه آزاد»، این محدوده به کانون اصلی ترانزیت شرق کشور تبدیل شده است. فرصتی استثنایی برای استقرار در قلب فعالیت‌های لجستیکی و تجاری با پتانسیل رشد بالا.
✅
واگذاری هفت هکتار زمین ، کاربری انبار با شرایط
۶۰٪ نقد | ۴۰٪ تهاتر با املاک سهل‌البیع ( مشهد/تهران )
🌐
https://amlak.razavi.ir/panel/auctions?page=3
در سامانه مذکور به صفحه سوم مراجعه فرمایید
مرحله ۱۵ -صفحه ۳- شناسه قطعه ۸- بلوک ۱۶ - را جستجو کنید
📞
تماس جهت هماهنگی و مشاوره:
☎️
09153259470
☎️
09152005111</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/673522" target="_blank">📅 21:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673521">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c42e93dc5e.mp4?token=kYKOO5v9aKgeJcGfli0JAa5Z3LOVi7ViZkGThc0qcJ1gxY_0MkTuXkzdzaeEA4fizIUeMd6e4ndmo8wiLdGqu-4saXesJi92k61xl8FC1ynjJXdWlCpKEicTUOo62Yjy460iPLxZTz6PEGLLEuCQfPjGFHHr3esmC5zPPtL65_MCv6UWMdG6CbzBKW_RuwPskmCQ01-C2KNSaJ5mlHRhhga4JE_ZnrsXdZ-7cfFr8WPwWLdJcJEZMaVikPPgKjUO1iZXDzX4jqUm8bcO1UVBiA0QSGFa7pDf3tMsWMmCUgcdnXn1kYrrQXsbYnQW5TYnDOYhvoRVEUkv1Mr7CdsiZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c42e93dc5e.mp4?token=kYKOO5v9aKgeJcGfli0JAa5Z3LOVi7ViZkGThc0qcJ1gxY_0MkTuXkzdzaeEA4fizIUeMd6e4ndmo8wiLdGqu-4saXesJi92k61xl8FC1ynjJXdWlCpKEicTUOo62Yjy460iPLxZTz6PEGLLEuCQfPjGFHHr3esmC5zPPtL65_MCv6UWMdG6CbzBKW_RuwPskmCQ01-C2KNSaJ5mlHRhhga4JE_ZnrsXdZ-7cfFr8WPwWLdJcJEZMaVikPPgKjUO1iZXDzX4jqUm8bcO1UVBiA0QSGFa7pDf3tMsWMmCUgcdnXn1kYrrQXsbYnQW5TYnDOYhvoRVEUkv1Mr7CdsiZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد از مراسم تشییع رهبر شهید آشفته و خشمگین شد
وکیل سابق ترامپ:
🔹
او واقعاً از حجم گسترده حمایت مردمی از مراسم تشییع پیکر رهبر شهید به‌شدت ناراحت شد و در تمام آن مدت به‌خاطر این موضوع آشفته و خشمگین بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/673521" target="_blank">📅 20:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673519">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
آمریکا هویت دو کشته خود در اردن را اعلام کرد
🔹
ارتش تروریستی آمریکا اعلام کرد دو نظامی‌اش، «تایلر جیمز فیهان» ۲۵ ساله و «ایزابیلا گونزالس» ۱۹ ساله، در حمله ۱۷ ژوئیه ۲۰۲۶ به پایگاه «موفق سلطی» اردن کشته شده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/673519" target="_blank">📅 20:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673518">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
پیش‌فروش بلیت قطارهای مسافری نیمه اول مردادماه که قرار بود امروز آغاز شود به دلیل مشکلات فنی به فردا (سه شنبه) موکول شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/673518" target="_blank">📅 20:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673517">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
روایت تکان‌دهنده مردی که پس از کما، یک روز را در برزخ گذراند
🔹
05:20:00 شرح چگونگی رخ دادن سکته قلبی
🔹
00:16:10 ورود به تاریکی و سکوت مطلق با شنیدن صدای سوت ممتد
🔹
00:26:30 کشش در تونلی با نور سفید و زیبا
🔹
00:35:00 هدایت شدن توسط مادربزرگ به سمت دنیا به خاطر حضور مادرم کنار جسم
🔹
00:41:30 ناراحتی و بی‌قراری اموات از شیون بازماندگان
🔹
00:46:10 ادای احترام و خوش آمدگویی توسط خانم زیبا روی غیرقابل وصف
🔹
00:57:10 اهمیت محبت به حیوانات
🔹
01:06:00 تردد افراد شادمان، میان دو خانه نورانی با لباس‌های قدیمی و کلاه خود
🔹
01:12:00 سقوط به دنیا با قرار دادن نوری سبز رنگ بر روی قلبم
🔹
قسمت هفتم (مادر آمد)، فصل پنجم
🔹
#تجربه‌گر
: مهدی زنجیرانی فراهانی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/673517" target="_blank">📅 20:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673516">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای خوک هار: نتانیاهو تحت هیچ شرایطی و به هیچ وجه در زمان حضورش در آمریکا دستگیر نخواهد شد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/673516" target="_blank">📅 20:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673515">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxGbQJ9VZNPCkNVS8liBVr3azmDAP1FsG5PQlDzUBOQKG8i-9-IxJgmNzC7ulpEGoN_E8bZSRG2cUaZ462NN4FWnLJts9U_Px3X1PhvbMALSyNoOL6sl-BfvrqEZedS9-cAOmVV_jF6fWnnUgPwWHTbqZQTKRQdhJTbEGKr9IRC47ga6BZzHDr-dQntlkJ2xHUm0Bz8ikMyeb5XhRqyfdTM4UcZHrAiVXdeVQXYvDuLbL6nqn3SkAmD9vMw9P_dQe0codjhWeqoujynY5RQGaFeAKedf6BZbyJbEeFBjE1vlE1cZzT6PfrLHuIOrs16jixJZr2PPT3k3aZlxraDdjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوک هار مدعی انتقام چندبرابری از ایران شد
ترامپ در پیامی جدید در واکنش به کشته شدن سربازان آمریکایی در حملات ایران مدعی شد:
🔹
هر بار که ایران یک سرباز آمریکایی را به قتل برساند، بهای این عمل را چندین برابر پرداخت خواهد کرد! این دستورالعمل به وزیر جنگ، پیت هگست، رئیس ستاد مشترک نیروهای مسلح، دنیل کین، و تمامی فرماندهان ارشد نظامی ابلاغ شده است.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/673515" target="_blank">📅 20:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673514">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ادعای سنتکام: از زمان از سرگیری محاصره دریایی ایران، ۷ کشتی تجاری را منحرف و یکی را از کار انداخته‌ایم
🔹
ما همچنان به تلاش برای جلوگیری از خروج یا ورود کشتی‌ها به بنادر ایران ادامه می‌دهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/673514" target="_blank">📅 20:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673513">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBrl-wvCBofFWQg6BraoMfPHYoLwzRY4OeE7kg1AdcpKc2UfaRjVqWCnB38_seAsfLyNGlSHoVefE2RV6EyUwG1TldN1K8J7bKgHtJSC87GMriP07PM5Tbj-4r_gw5d38WTqX68mCslHBI-yKu9PKzE14sUv-WEYpVqbzTxkCHn6Jd2H2H1lGgOye5sbnSTZpwuV2LPkdlH8uWUrnXTixJT7Bg5DbgIaPrf2fv0Z2QPiC-afAq-wy7cr7ArCBK9JlmGXOigICLo-MWu83TJGWaC0gCgfvzFdhYce6FEnNJLc1RdPBdSZNjLf9eN2UYScLUlkxEOI-Wnb7ckLmFeJpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش اسرائیل منازل مسکونی مردم را در «جنوب لبنان» منفجر کرد
🔹
ارتش رژیم صهیونیستی در ادامه سیاست‌های تجاوزکارانه خود، عملیات تخریب وسیعی را با استفاده از مواد منفجره در اطراف شهرک «کفر تبنیت» واقع در جنوب لبنان اجرا کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/673513" target="_blank">📅 20:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673512">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5itb7LfKj8AC4jYeQdfXksmU8Ww6uZiI1uekkWyV66QFz16VMzE5PDxFN25kO8HGfQWzyLJj6pUzdCGNLBjrRmt6ekoT8NQAGZJCHlLb16BOGj_3qKFxNIKdRXDg15apr4iuEz4qwrn-uI1clVuhtL0Ky7zb1AzuaRkkCH7b1ZbIiEyfFqD1EPf7hEaLKbX4UZGMd-w1_cAtiMPjg61Q07_IOpHtIW_XTS1uLApmBLmGcQdfVwuiWHxOb63W2yXJLLZyPscMAFbRXq4vrkRohir4th4E5k3Z8QxcAR3L6diD5OTSQ98LailXxThX5uSo4jtSd4bkY9pJOWemrh3cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع حادثه دریایی در نزدیکی سواحل امارات
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/673512" target="_blank">📅 20:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673511">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
وقوع حادثه دریایی در نزدیکی سواحل امارات
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/673511" target="_blank">📅 20:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673510">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTLBe-Idnqb3EHhKg5D08563A1cVQSwkAh5NluPc6vpSPp2I-u-899BJ_A9ORCf4SPp6P32Qh5ZNtyKXCqpp9V-ELJ2-iEkay1I7MIVgb5NNi_YjEJ-8QJs_6Rc9GT06TfEljnF5hmeiBsnGHOGH_fM0SGyQ1Y1FPaU0wMmkdDlNXbA0xOxeNIJ1bXTTdAjI-REizgf5L8p1QAs3RK3q8EsZ0u5J2MaU_2ER1QNhrpLBAlz7hBjmT-s707Zj6fW2sH7rJeGb7X-mXsioB56HyRww-K-oVFhjekzD0HM7Y1uh6dlFHO-bA34FVQB91QofVswfVDhclTF86J5k8sYrfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/673510" target="_blank">📅 20:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673507">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BRikvdKPuN6DEz0sa9mOQndYKqh4RyxnZ2fhmTYpcSm14Kwz3LPdWrL9lxGhQl8vpXUhAbRMeD_l3jI3Q1B7wlUFR43CblhHWj3cT5pJ6VN2881RrjfLzZ6qQICySEm_bGGRLhcQtSxglX0VSTl61vwjQv5j8WsYZoWnemIUJ0eTa8IcbC-WaPcg8UcMB6dq_icbSGcErKIXLAu15ZfgdhVd3cqKTVRHGol96QL-9qzcEquIGyiotCDjM8AnCgMbkT4-N2V_bwAd6L7uxMywLhFb1ABTPDJ8OTwB8fv_hJUwgi0UMD-UMiFxcq5wt7rdabUuWBax_C8XpZvlhucVcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LZYSIvScN3EtJdbC-ujZ-Kh5d7srjw94YINpPCFnm_9tgiPmpHm1Fb5ZaTaLYoYQidqI0hCHGcxhlK1I7zjDlVFPQh4ajr2dBpj9rMrg1ISOk2kBiS1AWyOXKoZee31FLyctB19YurAOzl17E3NgF9WBZJJdmf-Gge8wzAtCwOuLtmf7TegbSnfwO57dFJSINKZOHIIlS7RRXMfGJ3RRyzFl3Bydp9qstV3iOTNA2HR81IplKroIde4I4pKwsOQDX4C10GQCuffSDmPXKK1Zi-h6Ei0nvjr3CmUN--tquOZADQMxxiuZJQTcbtriM0FPvggHyuxMKiXGJc3OKQMNyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چرا محبت امام علی(ع)، معیار شناخت انسان‌های خوب و بد است؟
🔹
«جاذبه و دافعه علی(ع)» از ماندگارترین آثار شهید مرتضی مطهری است؛ کتابی که نشان می‌دهد عدالت، حق‌طلبی و شخصیت بی‌مانند امیرالمؤمنین(ع) چگونه دل‌های پاک را شیفته و اهل نفاق و منفعت را از او گریزان…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/673507" target="_blank">📅 20:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673505">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoyE43U8rGJuG5rUa97NMUnFRhZDXsEEQFOF5PisePOHL4uz0b7V_nZzp_xG8oouH4_Qn0hgMPL5IXjbrTdTJAYEoAQSRA_bbTgZmBrlx85D0UQOuO2ErWpq62sCXG1TjzWR0SV7iWPBeoaP-Cf6WS4A_CmLidsB6QFKzSgVavZF4xErN32BY6_5nLd9ZQYMg1rgYa-XP1rkUD-DW6Yjn8JP_SoCZFf5BZXddRKGH6Q_D1gG__0bY4XvfdSHTtwFjP7A2fkpIq0l1e0PSiOG4gv68aeAzfvVxhPz_QsbQl1uMakiRJmfT07_Z6JwgqgrLeq4D8dpAcOu3UVi2k1Hww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار نیست همیشه فرصت، دوباره تکرار بشه...
💎
طلای اقتصادی اجرت از ۳٪
🏦
بانک طلا بدون سود و اجرت
🔄
تعویض طلای سالم با عیار ۷۵۰
👰
سرویس عروس از ۱۰ تا ۶۰ گرم
کانال رسمی ما :
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/673505" target="_blank">📅 20:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673504">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
یک واحد صنعتی در حومه شهر خمین هدف حمله دشمن قرار گرفت
معاون سیاسی امنیتی استانداری مرکزی:
🔹
این حمله حوالی ساعت ۱۹ روی داد که تلفات جانی در پی نداشت و خسارات احتمالی در دست بررسی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/673504" target="_blank">📅 19:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673503">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1rP_0ad9YLiZY1iEY0MARaHfbZYBGEtTw1raun4hLaZjtuLP1AClJq27oexlAY6S5xFnfAlSbP6I34TCDaSjVVOx4cAL-Rpd6HLDh_4lMAbHVI-XNNFX5PFMKDp6BdZcfSTPILldTM1iF2bpBGjjRmWDMOTzofqE70XmZVmqiNVYGSVlFq5FJlt2iNjwFpA9hQ8JeDABuJ3LkBpyktc2VWLPGjqnNyRDszoIqx3OJaC9QcnvWQzlK6LFniJ4BytaMpm4KMuy9qm7qLaloOV2qreLHLYXvdPOvbUDjN2xy6lPu4Hpn42D3pCjxzsQyseVZIGPvvpPhgt02HuA9-jDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه بالا بردن جام قهرمانی توسط رودری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/673503" target="_blank">📅 19:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673502">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
شکبیر سود ۲۶ هزار ریالی برای هر سهم تصویب کرد
🔹
مجمع عمومی عادی سالانه شرکت پتروشیمی امیرکبیر با حضور ۹۸.۳ درصدی سهامداران برگزار شد و ضمن تصویب صورت‌های مالی سال مالی منتهی به ۲۹ اسفند ۱۴۰۴، تقسیم سود ۲۶ هزار ریالی به ازای هر سهم، به تصویب رسید.
🔹
بر اساس گزارش عملکرد ارائه‌شده در مجمع، سود عملیاتی شرکت با رشد ۶۱ درصدی، سود خالص با رشد ۸۰ درصدی و سود ناخالص با رشد ۴۹ درصدی نسبت به سال ۱۴۰۳ همراه شد. در همین راستا، ثبت رکورد سود خالص شرکت به ۱۰.۷ همت و سود ناخالص به ۱۱.۷ همت، که حاصل افزایش درآمدهای فروش و مدیریت بهای تمام شده تولید بوده است.
🔹
مطابق این گزارش، سود هر سهم (EPS) نیز با رشد ۸۰ درصدی به ۲۹ هزار و ۹۹۹ ریال رسید و پتروشیمی امیرکبیر توانست بالاترین سطح سودآوری در تاریخ فعالیت خود را به ثبت رساند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/673502" target="_blank">📅 19:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673500">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfL32QXcdVh2aMtXVvoxcmqPsGWvpR32qthSAJOCQ-36aVPnE2gQHlTFM-eNJdxf5tvcavkmFM9XZGf8lOmQUfWPRtjJc16uNCUrcUG-cCYbQeYer05cGJp7-5gaxGKSkMQy2iTM9DAMk3-DnUPDvusZysDLTB9SkVlJ4ln1JD4DTe5SX_ryUQt0FOA2vCh-IWyVJxqWgUiTm4wX7CudmRWiMTiHJshadiP4uN-wNGwXV1WWHteZuoJMWI9corRRBl594ofPNioExui_ss1CB5QNZ53Q7B-AwVmd3sZWjQTjXQj7616Lyao_rL1QNdlpDWgOfajdtg-rEIuKTT6Jag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVj6w9rhasU9Ezh_7_8uXxi0DbpWrIXpqT79QSt9eYtAnzc_VtVOWNux5-osFL2CnLMivl2P1mwrxRWinM_KEoP3-NSMu5YbS97mffzZmfED30VMhnVUEC_Bi6CdOA-8C5NFx-IyWtt-bnoJZqEBo7mjZ8ngTmginqCIhGLP0PA33ZKUVLa2W8vVI3OECbqnpLDhLBFvpNWqFJaBbsiAUTTcIlAlM5MIKyHo4CTmBaQfPq2l_zwfXU4KkiRpdDk5Q10HsF6xKJ7Onbxkmld0uEySXteAfJuoSde5oLh-VlAWFk0B5oaoxrBx0EFlsKZDTjT7ONLtlWAMMzBnnGVuuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویری از سرباز آمریکایی که در حمله ایران به اردن به هلاکت رسید
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/673500" target="_blank">📅 19:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673499">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aG5PowRikdohLQxsbw-MZvyy94axTSMHfjKwdwAT6AMKXxmV5r03iH_gbCzD06DeKJPvXq7GRFNVahpOLS6cs90fEBX27HKo_lIRMc4TS9Hv6qGPW-v44EaXU0nXhhHSHnLg6D6sOOh3lxl6nbR-HgYVeCZTIeCqMDAZhismQZIquINYe_dwP6XMy02TpznsHRrg8NbWG0MzY_APfxPV1RvGU0Gsus3KjewzZV9ybHGI77GxXxHdtWtFTq5J7f0EUhnImdV_x_x9RdzQ5KsQ7txEKtdIchLi7h1k3h1WdXgWn2ZQNOZy0GGJ9_i76XbUCjUyXpfglEE_jubif1N-8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سگ‌زرد: بر اساس یک نظرسنجی، اکثریت مردم آمریکا از توافق با ایران حمایت می‌کنند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/673499" target="_blank">📅 19:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673497">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
توانیر: بین ۷۰۰ تا ۸۰۰ هزار ماینر غیرمجاز کشف نشده وجود دارد
هادی سفیدمو، مجری نظارت و ساماندهی استخراج رمزدارایی توانیر در
#گفتگو
با خبرفوری:
🔹
از ابتدای سال تاکنون بیش از ۸۵۰۰ دستگاه ماینر غیرمجاز کشف شده که مصرف آن‌ها حدود ۳۰ مگاوات می‌باشد و این میزان مصرف معادل با ۸۵۰۰۰ واحد مسکونی می‌باشد.
🔹
بر اساس اطلاعات به‌دست آمده، میزان ماینرهای غیرمجاز موجود بیش از ۲۰۰۰ مگاوات برآورد می‌شود که معادل با ۷۰۰ تا ۸۰۰ هزار ماینر غیر مجاز کشف نشده است.
@TV_Fori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/673497" target="_blank">📅 19:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673496">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
جنگ دریایی با چوب و پارو؛ تقابل عجیب نیروهای چین و فیلیپین
🔹
تنش در دریای فیلیپین به درگیری فیزیکی نیروهای نظامی دو کشور با استفاده از چوب و پارو کشیده شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/673496" target="_blank">📅 19:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673495">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
شنیده شدن صداهای انفجار در شهرستان سیریک
🔹
عصر دوشنبه برخی منابع خبری و ساکنان محلی از شنیده شدن صدای انفجارهایی در شهرستان سیریک خبر دادند.
🔹
هنوز ماهیت صداهای شنیده شده توسط مردم مشخص نیست./ مهر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/673495" target="_blank">📅 19:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673494">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
♦️
آمریکا طرح ضدمقاومت خود در جنوب لبنان را کلید زد
🔹
وزارت خارجۀ آمریکا از آغاز طرح «مناطق آزمایشی» برای خلع سلاح و تخریب زیرساخت‌های مقاومت در ۳ روستای جنوبی با همکاری دولت سازشکار و ارتش لبنان خبر داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/673494" target="_blank">📅 19:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673492">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCghr1_PoFr3-IwKqFKyTKBlZ9IJg_8PoVY_5LiZfpDNgYd0ZOVJt4ugk4FsqRGwUNvawa9HQ7LbPWmn3OYGQ1n2Ln7F54_WRN8vhnMq4tNf032ZM9Ut5bRbvgQXwgebTsc6QGy42mCqxedzMgUHqLfVVafQ4p6CVTK9at7xCAnQsbwRQOEs5_mT4Jz4hsSsfAUlVcr9FyKjRLQ28_FAugKn7yFLOpxbe1J56HnvsomWEPZgGmFPT97rE6oFKuI9Xb_IEdJAepj4B9umYG7VStLbG5xrmZOdH_FCvQQ7vTTp0_VgwDxY-N6WRX-u6CmNE80-s4Yzzp1NLzFbpeBM8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c107e145b.mp4?token=r9miLp4cUYDidqhwWaED02t3DjDjasYK3_8PJIo4vyXiLZq9IA3d9G1qTgj882951nHn3WK6GvGdPQuKI2KWP8nyzV1xqo48Zdp0Y018EztNjCuTBnJlbI6UWIVVTCE4OnLLLAXzTtkkjH92mrnwsDxbMf5DyoIzSwW-kX0_O3bFoKmcqGuhKquD8Zcwxh5GcucZ0dH3FKnf6NB6p_x73HnhTYU6bwz9DaoSQ7BgvapBlZT6DjHA7fAuiuVaJxSulsCABnGQn7abyoB0Q2Ch8Tv0aURXOL_8Jp_XIkEWrvNCLg-QORjvVlEc5XzLJ71Di2BljOiaQhu7x6yzeECfrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c107e145b.mp4?token=r9miLp4cUYDidqhwWaED02t3DjDjasYK3_8PJIo4vyXiLZq9IA3d9G1qTgj882951nHn3WK6GvGdPQuKI2KWP8nyzV1xqo48Zdp0Y018EztNjCuTBnJlbI6UWIVVTCE4OnLLLAXzTtkkjH92mrnwsDxbMf5DyoIzSwW-kX0_O3bFoKmcqGuhKquD8Zcwxh5GcucZ0dH3FKnf6NB6p_x73HnhTYU6bwz9DaoSQ7BgvapBlZT6DjHA7fAuiuVaJxSulsCABnGQn7abyoB0Q2Ch8Tv0aURXOL_8Jp_XIkEWrvNCLg-QORjvVlEc5XzLJ71Di2BljOiaQhu7x6yzeECfrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آژیرهای خطر در بحرین برای پنجمین بار به صدا درآمدند
🔹
منابع محلی در بحرین از فعال شدن مجدد آژیرهای خطر در سراسر این کشور خبر دادند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/673492" target="_blank">📅 19:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673491">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkwUCyXnrdCndBIjvxa985kFaT5psOGopeN40KR0G28FMepb9IPP6kA0Xr_nFpAryz5No952EkEaqlMie3YK-Rx9XElbOjFW3YndJRtfTH4Yx4Kz2TPLvujMM4lj0dXGOsClwhlNpTufHNKzRNAzkvIy3EAJVDpyzKbQUYMBZGXjPpMO1gdcqK4EoLO5PxXYBv_-bP7ws-rM4vm6726-47p2tvYC_jCRX5sWKcnYs8rQ9XRY2YMTgpULCgBxE9X94DroM__cutfk0cB5_7_4HsT3MwIf8W6ouPGzO56Js7ipvQ1Z4bf2Dg3_uKAvffmyy93v0zcfSMYmEWyCtQR6yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتشی که از شترمرغ‌ها شکست خورد!
🔹
در سال ۱۹۳۲، دولت استرالیا رسماً به ارتش دستور داد تا علیه «شترمرغ‌های استرالیایی» (Emu) که مزارع گندم کشاورزان را نابود می‌کردند، وارد جنگ شوند!
🔹
ارتش با مسلسل‌های «لوئیس» و هزاران فشنگ راهی مزارع شد. اما شترمرغ‌ها تاکتیک‌های…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/673491" target="_blank">📅 19:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673490">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
آژیرهای خطر در بحرین برای پنجمین بار به صدا درآمدند
🔹
منابع محلی در بحرین از فعال شدن مجدد آژیرهای خطر در سراسر این کشور خبر دادند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/673490" target="_blank">📅 19:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673489">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6fe82fa2.mp4?token=TOoPU03i2HP3tj7crPzHxgaf8DHF2QjtFIm3GKbAts4KSgXLPvykRpRxjVTmNA42B7BWUQO6jyIqWlc8j4Tr_2bYBj33KMY75SHnaj3Uu2k1HoNTj1YqbuD4qdzrfrjqVYgH875I4Vv_4ptPHdTNUOWx0oc0x4ILtJIHWnV-LHusFfUFec-iuDP7IPK7yT8Nzvw7X0t2R2XhToMVYAtd1wKa3quFhPkPHarVEVSXQZu1jlFdVVD-CXI21d-KOgV5UcsvODsDv6h-E7FKKxfBo4CBTXB1zXg-KcHfQtzRsNd1FMF2Q9IY7kw2NjsuHx5LOtRcEuNeLiuynySK8WDenw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6fe82fa2.mp4?token=TOoPU03i2HP3tj7crPzHxgaf8DHF2QjtFIm3GKbAts4KSgXLPvykRpRxjVTmNA42B7BWUQO6jyIqWlc8j4Tr_2bYBj33KMY75SHnaj3Uu2k1HoNTj1YqbuD4qdzrfrjqVYgH875I4Vv_4ptPHdTNUOWx0oc0x4ILtJIHWnV-LHusFfUFec-iuDP7IPK7yT8Nzvw7X0t2R2XhToMVYAtd1wKa3quFhPkPHarVEVSXQZu1jlFdVVD-CXI21d-KOgV5UcsvODsDv6h-E7FKKxfBo4CBTXB1zXg-KcHfQtzRsNd1FMF2Q9IY7kw2NjsuHx5LOtRcEuNeLiuynySK8WDenw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محاصره دریایی یمن علیه عربستان؛ صنعا معادله «محاصره در برابر محاصره» را اجرایی کرد
🔹
نیروهای مسلح یمن با صدور بیانیه‌ای رسمی در پاسخ به محاصره ۱۲ ساله این کشور، از آغاز تحریم و محاصره کامل ناوبری دریایی علیه عربستان سعودی خبر دادند.
🔹
صنعا با تأکید بر آمادگی…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/673489" target="_blank">📅 19:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673488">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a228a0d421.mp4?token=Zpsq4aDDj-RUlwY_oMPVd-nmieyAHbFwbHwhBBO3V2Hjy29zB3gN9eGtIaBXMMZTxmy5DPNZT4eLNtHejXPaOtmA_sAm-quLOB5lzUepdYyrBgpENToSL6FN0pp3qA5WM9gd3PalEymrN1oAJvZYjhmbCksDHJEvQ7IrWQDP6Z3scTgOW6yTfNuTSskMyjG-LaerVNrFsV1kuAIHvD0nniNGITBbtJ_xv03oFBjZALovQt8r9MXHwNRgHDecy9KzpuPgNXOkJ0d1n2uHQqndc2jXMMpbjcYHhogJoYkIp760mXJ0hvhpCJnxcWX-N-t_Ah2lqkxUeSAHcm9iJkrNpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a228a0d421.mp4?token=Zpsq4aDDj-RUlwY_oMPVd-nmieyAHbFwbHwhBBO3V2Hjy29zB3gN9eGtIaBXMMZTxmy5DPNZT4eLNtHejXPaOtmA_sAm-quLOB5lzUepdYyrBgpENToSL6FN0pp3qA5WM9gd3PalEymrN1oAJvZYjhmbCksDHJEvQ7IrWQDP6Z3scTgOW6yTfNuTSskMyjG-LaerVNrFsV1kuAIHvD0nniNGITBbtJ_xv03oFBjZALovQt8r9MXHwNRgHDecy9KzpuPgNXOkJ0d1n2uHQqndc2jXMMpbjcYHhogJoYkIp760mXJ0hvhpCJnxcWX-N-t_Ah2lqkxUeSAHcm9iJkrNpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخریب در آشیانه هواپیماهای بدون سرنشین MQ-9 در پایگاه موفق سالتی در اردن؛ حضور پهپادها در باند فرودگاه مورد توجه قرار گرفته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/673488" target="_blank">📅 19:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673487">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k103cYVPYhFQAJRh5HZ9VeNzBodDsEGHLuai85JrgIgTrwkJ4w0e3unEOmszDrKbyq_pe_x_8nf4rEYwF4GhWSyp3p1NcFMDoe9bwwg8nCMu3GGQLsdIH4pkeBtdpO7ZKc0MxmQxbD7SGiJ0P3R7DV-0Pzp_rBWu1n9zKoysXZd0WQq94HvsbXKXvEuL5T2hvZFGLrGMg93NqrAnwqzf--I5uJFkMdki0ENRoR1Omn1E4eCSzpSL9uaydpeGtbvO1YXm0OGIR4P1cWiJkHsH_aCI79t2biXYMo4FBycg_-4m4PK6TZNXe2JPcKj_wCFz4zbimCGEQP8OAA3nsq2ATg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر کشور ایران وارد اسلام آباد پاکستان شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/673487" target="_blank">📅 19:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673486">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
انهدام یک پرتابه دشمن آمریکایی در آسمان اقلید
معاون امنیتی استانداری فارس:
🔹
بامداد امروز(دوشنبه)، حافظان امنیت در نیروهای مسلح مستقر در استان فارس، با هوشیاری و دقت عملیاتی مثال‌زدنی، موفق به شناسایی و منهدم کردن یک فروند پرتابه متعلق به دشمن آمریکایی در حوالی شهر دژکرد شدند.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/673486" target="_blank">📅 18:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673485">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 توصیه شما برای جوانانی که ابتدای مسیر شغلی هستند چیست؟</h4>
<ul>
<li>✓ یادگیری فناوری‌های جدید و به‌روز</li>
<li>✓ یادگیری یک مهارت‌‌ تخصصی</li>
<li>✓ کارآفرینی یا کسب‌وکار شخصی</li>
<li>✓ استخدام در سازمان‌های دولتی</li>
</ul>
</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/673485" target="_blank">📅 18:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673481">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALpWQ04F2MzUe-o0MDz18AY4HD6UwOUUymMT2Uuo57ELKK0_K4_J5PaDVWifP-t1U3CGn4Oxq8upWv9xpoyMBfYHeUqbgf-1RaNE1JiSBfyM66g0oyASoOD4whFhpYmY9uPn1L39Qo53UnlbiovpymJxk8T06FjpfbUjbSJZT8BRC8oQn6e3IFyR7Mol8nadBr1WCaj1b2UQSvZdVg45A7UYUFWzDOFlWNAeuwz_Z9gYfA4z38I_xGX2x9kvfJ91cHjGhd-IwldCAPXAsYFTF_XOsiATFVTjXJgkcuE7Vn1hAsvSbjg_pAozV6W9W7cvDYsR0c18Idkapz6a2vm7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله آمریکا به منطقه نظامی جنوب غرب تبریز/ چند مجروح و یک شهید  گزارش شده
🔹
بامداد امروز دوشنبه، یک منطقه نظامی در جنوب غربی شهر تبریز هدف حمله آمریکا قرار گرفت که وقوع یک انفجار مهیب را در پی داشت. این حمله حوالی ساعت ۲ و ۳۵ دقیقه بامداد رخ داده. نیروهای…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/673481" target="_blank">📅 18:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673480">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92cbfeb8e6.mp4?token=v-FK8gHsrV5ITv1PG8vnE89DiNNvnKE_k5iIfvfAODJsawtyTFrKlHweyVBTRffAlaEGq31bj8Ewmq2bd2JkSmb8LBMb82XDJs-q0SjC8ZE601GdjpvQr6a-sUXJoBSm_z731JYxQW5L4OlcFq_fCIH9J-HeaBaG7aVxm1pz17CXHc6IVXgv2amcHqZ-3tomaZEGXuf8lJ_S20R1IW_FMBPYg0pEt36Vu29b-yI0kWX7CrbAH7T6IweERp7g5DOGdmj3S8hk1xC1uZJKCgP9QMD-nEUPtL-opewGf1XVmoTDmlv2gpma2Yl0wQHp3ER7SSmmqsGbvl32Oaszy3tgaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92cbfeb8e6.mp4?token=v-FK8gHsrV5ITv1PG8vnE89DiNNvnKE_k5iIfvfAODJsawtyTFrKlHweyVBTRffAlaEGq31bj8Ewmq2bd2JkSmb8LBMb82XDJs-q0SjC8ZE601GdjpvQr6a-sUXJoBSm_z731JYxQW5L4OlcFq_fCIH9J-HeaBaG7aVxm1pz17CXHc6IVXgv2amcHqZ-3tomaZEGXuf8lJ_S20R1IW_FMBPYg0pEt36Vu29b-yI0kWX7CrbAH7T6IweERp7g5DOGdmj3S8hk1xC1uZJKCgP9QMD-nEUPtL-opewGf1XVmoTDmlv2gpma2Yl0wQHp3ER7SSmmqsGbvl32Oaszy3tgaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش عجیب خانواده چینی به خطای فرزندشان کاربران را تحت تأثیر قرار داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/673480" target="_blank">📅 18:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673477">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57970598c8.mp4?token=HR606MQjeYhCdZ9nnQSpv2KnpKTt1yfgBbSkg83nwsTR9WHKVsJzNux8KixPb9vwFr5uNcewRicgBRv0Gnc27hk_72wu0a4N17scBiSRMoxq8lh7Q0pkfxxyaa1CRSizV1UA_3vui2B9SUWjDWYXP_PLZFl_BJL7zlympRkXNEBxDThOlwgdYLkTE2dd8MErPSAzlJ-SOFBjs1bL0jDZbNq65Snww2Rmwke-wGwQPxu4HO1CRP1o80QtQs-u6UDwP0yFI_R6BgUbtJc1gUHB_K5yOaxIOJnX-aWY44YO9MA0kV35naClz9ZADp-83OTnkqH7-IYV5P0crE7lWlcdMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57970598c8.mp4?token=HR606MQjeYhCdZ9nnQSpv2KnpKTt1yfgBbSkg83nwsTR9WHKVsJzNux8KixPb9vwFr5uNcewRicgBRv0Gnc27hk_72wu0a4N17scBiSRMoxq8lh7Q0pkfxxyaa1CRSizV1UA_3vui2B9SUWjDWYXP_PLZFl_BJL7zlympRkXNEBxDThOlwgdYLkTE2dd8MErPSAzlJ-SOFBjs1bL0jDZbNq65Snww2Rmwke-wGwQPxu4HO1CRP1o80QtQs-u6UDwP0yFI_R6BgUbtJc1gUHB_K5yOaxIOJnX-aWY44YO9MA0kV35naClz9ZADp-83OTnkqH7-IYV5P0crE7lWlcdMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری دیگر از لحظه وقوع حادثه و بازداشت مظنون در شهر نیویورک آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/673477" target="_blank">📅 18:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673476">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szGQi5PkPWMOCSXCf7D5gBvPB8RKeWz0eTHFKi1CYxrXBehcrrZcSn_VmVFqhvyZJLk9VrZyBSRaagMnwY8Z4VpFUa5BK9qXbfxlUSCeCABpmW8DkflM-Cvoa6hsiXQdu13SY7diqLkyHQA2F0V5_xosL5RRBXYhfPJPjAmY3W2qPZhGHB1xyNOca34b8bQHtyS7szQshaGW27h43eolp78fMXFqPXT-uKWdlwXT7q7qNWawV7BW8zaOrCILMIyNDSMzf55NV6MJH1jgj1xxlU6rZPlMX5VZBx1xC9K-W2AKJSFF41bBXqM0TnjA7o-nHnunZZ-U3NfYzczIjOLDtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مردی که هنوز معمای خاورمیانه است؛ امام موسی صدر را بشناسید
🔹
امام موسی صدر، روحانی، متفکر و مصلح برجسته شیعه بود که با گفت‌وگوی ادیان، دفاع از محرومان و بنیان‌گذاری جنبش اَمَل، نقشی ماندگار در لبنان ایفا کرد. او در سال ۱۳۵۷ طی سفری به لیبی به شکلی مرموز…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/673476" target="_blank">📅 18:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673474">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کارشناس اصولگرا: به‌جای ترامپ، باید نتانیاهو در صدر فهرست انتقام قرار گیرد
حسین کنعانی‌مقدم، کارشناس و تحلیلگر مسائل سیاسی در
#گفتگو
با خبرفوری:
🔹
در صدر فهرست انتقام باید به‌جای ترامپ، نتانیاهو قرار بگیرد. کوشنر داماد ترامپ یک صهیونیست و جاسوس موساد است و ممکن است نتانیاهو با نفوذی که در کاخ سفید دارد، ترامپ را ترور کند و بعد خودش تبدیل به یک فتنه برای ادامه جنگ علیه جمهوری اسلامی شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/673474" target="_blank">📅 18:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673472">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsDVEwNYjz3ANl0gCLjSpX3IUdCrGhqCdCBdZhNDCfsfATBojPoWiBN29Pg1AdE4h1GPnCIMOr-RDqy9QS0ZDveT428gBSimJ5cyiaZGQPVEbma7TjZ5s9yzzeYYsB2xP33zMVkDLDPjZDOxi3TTw0t1A-Y8j-Mo9GeWA1crk0X_IvnxPJe609SYyojjt1wYIvN-zKLzw-RdaButfkQBiTd6ag_smqGc7hIsTDrVgwYamP6ISRzWbtyNxYRcoqbOjy_IiORPfYbPYMx7pyrGYETGcnetDA1HFECg74_mku5_pFpLcSOu_y0RFNI92bI4a1FnjXKKzhY2AbfcTRmfxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ارائه ارز اربعین توسط بانک کشاورزی
🔻
بانک کشاورزی در راستای ارائه خدمات هرچه مطلوب‌تر به زائران اربعین حسینی(ع)، امکان ثبت درخواست از طریق اپلیکیشن «آپ» را فراهم کرده است.
🔻
متقاضیان حقیقی دریافت ارز اربعین می توانند از طریق اپلیکیشن «آپ» نسبت به ثبت درخواست، احراز هویت و واریز معادل ریالی ارز اقدام کرده و پس از ۲۴ ساعت ارز خود را از شعبه تعیین‌شده بانک کشاورزی دریافت کنند.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/673472" target="_blank">📅 18:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673471">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313105da7e.mp4?token=LD-Wyb8q2y5yEZJpNwnFHq9Sy2MYmD-1g2gbFBVHm8Nb6ulmHnDYeDSTzHZfe6Z2y9qwWaVDEzNcdexMgmPcrDS-sN9P_nygSXubjH_6jlrgzKRNurbhiQcm69XXoOScT7cb4ufBGCc0qJf0s68RWcj1XuomA1iJP-EXeTt6wH2G9w1mCubr-geTLSt9zFv_heGBUWvweY4KiXRGjkDuDx50dQyOlK-LAN4OC7NZ0y2U5cGIWSCZ1l6DCtCu56NBNE8Sp7MSFKMDr4_F5Fg9WXEsQw1F4CVauatOCmuyyL0Mf8IsO97x2TsdpdqLIZ3uyZ2imFpM-STo910evN7fAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313105da7e.mp4?token=LD-Wyb8q2y5yEZJpNwnFHq9Sy2MYmD-1g2gbFBVHm8Nb6ulmHnDYeDSTzHZfe6Z2y9qwWaVDEzNcdexMgmPcrDS-sN9P_nygSXubjH_6jlrgzKRNurbhiQcm69XXoOScT7cb4ufBGCc0qJf0s68RWcj1XuomA1iJP-EXeTt6wH2G9w1mCubr-geTLSt9zFv_heGBUWvweY4KiXRGjkDuDx50dQyOlK-LAN4OC7NZ0y2U5cGIWSCZ1l6DCtCu56NBNE8Sp7MSFKMDr4_F5Fg9WXEsQw1F4CVauatOCmuyyL0Mf8IsO97x2TsdpdqLIZ3uyZ2imFpM-STo910evN7fAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«چرا ایلان ماسک و جف بزوس باید شاگرد کوروش کبیر باشند؟»
/ مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/673471" target="_blank">📅 17:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673468">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در شیراز
🔹
دقایقی پیش اهالی بخش‌هایی از شهر شیراز صدای انفجار از محدوده شمال غرب این شهر شنیدند.
🔹
خبرهای اولیه از مورد اصابت قرار گرفتن یک نقطه از شهر در جریان این حمله هوایی دشمن حکایت دارد.
🔹
اخبار و جزئیات تکمیلی متعاقبا اعلام می‌شود./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/673468" target="_blank">📅 17:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673467">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی دولت: برنامه‌ای برای افزایش قیمت بنزین وجود ندارد
🔹
ادعای سنتکام: از زمان از سرگیری محاصره دریایی ایران، ۷ کشتی تجاری را منحرف و یکی را از کار انداخته‌ایم
🔹
حمله هوایی اسرائیل به بیمارستان «یمن السعید» در جبالیا غزه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/673467" target="_blank">📅 17:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673466">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVeMuTL0xvczXKiFBV8NrMKjJWdRScPCimP9p6IdNQKy-lXzTCwbZBNMwaNwMdbw54FcJlainXUVcEQR_Abumi68SUN6R-jq4jD__-KXBSA-uO9JW_tuCmP946jeyNJ48wNaawUw_cqpyOqIzq44heLVRC4bU8AM3oGEw74vi2p5B7FwqaMcIwBUcvmEz5sj2h6FKUp-k936wIQ3PsExMn_Sw8bO2UZjb_lHxaBR6YuLJtVv9FRvhGxdgh24zIPYny9PPeCZosfEv_hO0MimBimtl2cuvKc4qR7EcTCpUiMZQmbbf5BQaFvu1SThdfbwDXUmD6vo50u9lGCDG3CtRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در جمع تولیدکنندگان دو داروی مهم هموفیلی
🔹
ایران در میان کشورهایی قرار دارد که توان تولید دو داروی مهم مورد استفاده در درمان بیماران هموفیلی را دارد.
🔹
کشورهایی مانند فرانسه، روسیه و ایران از جمله تولیدکنندگان این داروها هستند؛ در حالی که برخی کشورها برای تأمین یکی از این داروهای حیاتی، به واردات وابسته‌اند.
🔹
یکی از این داروها برای درمان بیماران مبتلا به هموفیلی A استفاده می‌شود و داروی دیگر برای کمک به کنترل خونریزی‌های شدید در بیماران هموفیلی کاربرد دارد.
@amarfact</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/673466" target="_blank">📅 17:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673465">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26fd8e9175.mp4?token=R0owytw8Y9iXf_ICQat67NPvWaOnFMoEQ_o8xjwF0X-qf7RlvGph7XROW4ELusSwBptOzr9RQ7885hJSzSl1DRdQONZIB3OsEoZv8cOKXiENYR3ms293ZQpbgRt9auWE_zgOpYGq9iIHJXbVM0zEGSPobzwcQX8m2YhoM1pdBvD1LiYbARf_wOCDLjNMvlkJmgl38otDs7L8cn7fT5aV0y1Tt3ju23LxzU4sttzM5qoxMhyxIWnDoA51ewfAnGVoRiJsAe2DGCzg3wUuK6_tXoS_4HHM4RCQfoB3tBYH1LRg5AwUZs8U3B5lnmD4K4BV6O1E6eAnEw6WIZHEDixwIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26fd8e9175.mp4?token=R0owytw8Y9iXf_ICQat67NPvWaOnFMoEQ_o8xjwF0X-qf7RlvGph7XROW4ELusSwBptOzr9RQ7885hJSzSl1DRdQONZIB3OsEoZv8cOKXiENYR3ms293ZQpbgRt9auWE_zgOpYGq9iIHJXbVM0zEGSPobzwcQX8m2YhoM1pdBvD1LiYbARf_wOCDLjNMvlkJmgl38otDs7L8cn7fT5aV0y1Tt3ju23LxzU4sttzM5qoxMhyxIWnDoA51ewfAnGVoRiJsAe2DGCzg3wUuK6_tXoS_4HHM4RCQfoB3tBYH1LRg5AwUZs8U3B5lnmD4K4BV6O1E6eAnEw6WIZHEDixwIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب‌ترین آسانسور دنیا در ژاپن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/673465" target="_blank">📅 17:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673462">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2c91f294.mp4?token=soXIcCjHUyWBphzTHcdpuhG3WBvK7IOVipBFSfdBeMzotSGD9aGZN75YGM5BgWSzFqtj-z46zdU_YobyoDXydIB2bVIKFTeWhjxq-46p4Ed3D0EzrVnzo7ME3PEilA_GPsIMPDM1ZO4TluMattjeuyiigpG0KywqQk2brO48lMgeuwIO2kePIKYj_o-6REMh4ElTWPWa_xJEfiYoHpYo9zsDjssfvo-pud3ryXUns1TczwwD5djLhELbjX6-Akg6DTNH2kMMgo3cGM0UvncTuBdAYH7AmBnMmU7ywx2s_1-R6a3oOLiDXK3iYn33VBFhc7t5AewX0QikCvQcxOPpx4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2c91f294.mp4?token=soXIcCjHUyWBphzTHcdpuhG3WBvK7IOVipBFSfdBeMzotSGD9aGZN75YGM5BgWSzFqtj-z46zdU_YobyoDXydIB2bVIKFTeWhjxq-46p4Ed3D0EzrVnzo7ME3PEilA_GPsIMPDM1ZO4TluMattjeuyiigpG0KywqQk2brO48lMgeuwIO2kePIKYj_o-6REMh4ElTWPWa_xJEfiYoHpYo9zsDjssfvo-pud3ryXUns1TczwwD5djLhELbjX6-Akg6DTNH2kMMgo3cGM0UvncTuBdAYH7AmBnMmU7ywx2s_1-R6a3oOLiDXK3iYn33VBFhc7t5AewX0QikCvQcxOPpx4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محاصره کامل منطقه حادثه در نیویورک
پلیس نیویورک:
🔹
عامل حمله مسلحانه و انفجار مقابل «فدرال پلازا» را بازداشت کردیم.
🔹
پلیس نیویورک انفجار یک شیء آتش‌زا مقابل ساختمان نهادهای امنیتی (از جمله اف‌بی‌آی) در منهتن را تأیید و شایعات تیراندازی را رد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/673462" target="_blank">📅 17:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673461">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
نیویورک امنیتی شد؛ فدرال پلازا پس از انفجار و درگیری تخلیه شد
🔹
در پی شنیده‌شدن صدای انفجار و وقوع درگیری در نزدیکی «فدرال پلازا» نیویورک، ساختمان به‌طور کامل تخلیه و نیروهای امنیتی به محل اعزام شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/673461" target="_blank">📅 17:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673460">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYMW9PQJGGiyeLAuFIuSa_qKmrX4jxL7TuMUEXKbKCGk1WqivRoF8XhEyWEPVkLf4pcXlvmvR9fSiD8ZbwQrpTK4tC-OUepPdnKqv5tEFQWa2R7urqWes685P-xeOXMNl1q_9LWGZRQfp3evdo4Z_VDJvPIjP3uHn4skLgJ0ILcfahzBWAL_X8dgQncSrgTg9hF7hmOIePmcFq6S5V0u4w_z33vsXNyBhtMVW9UuiJ9w7boAbmAdt1g2TL2OHxQVV627jqDLm6ksVL5nYGKLBxDcEx_a-zqa8Vl236vuD-iJfmO9JmGIxvbeORk2L2JnrgRanBA8dFmWbA9o4qMSfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا اردن به مرکز فرماندهی آمریکا تبدیل شده است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/673460" target="_blank">📅 17:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673456">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HNB1yx1_F-8jIS5fVVNuwswhl52XfGzN6ViHD-A6ptOy5Du2ysLQ0gkDTa1iN-RPAm6Kz-ahBcUgNY2I19hvI1MKJ-kgWQ97ji4MFEeplhKpo5b1sxaJnl54yHfd7mFucKEaSlr2vFV9SBT7miqS5tqAx4e_qdAdbH4wKOmNBDkl4QDuDminbPxu7iyqXetF125Akq8OXvWsOuP67UHey94znG0DCimZdMQ_jyXowqJokG1a7d6Nat8IvMlb9BH4zkLHtq58OFxp_EN2sPbgN-OOqIORbDSBYbSwTz31Sf5iT89nfv38HVIysPr1KhTHo72szVyQd6Gk8jnYxXfM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OY9aod3eIGUhF5OpYedWarn0fWaQ_YlMn2z7zCJfwUa2IRItmbY9sEjPJuu39oUHE69Jj8eUzf_JJFR5fuUdXQM7dBVUpCsk2hrlx5oRouIK0WUwSDeI8uwivqpLvzibiYgtcjno43AVXRvDohbnOm3H7DgBpxkHvPXS36ELslfZOwXpOHg4o4BZMmwrW9G1MIZUywIAYjFGhpYf-_U5AmXDXhrHmb_ClGc_J0HSxMdSvVU_QYSoHC1m1EXDZ7LXY-TQIm2hcCSTUOo-6UW6_fCCf6cCKQItpqfqbbZ7kt-GzitHro0GdNOzm5jpPUoSJT152skWkB7tnCUQ6njk2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af6db08f50.mp4?token=TCJqrplRII8WeyVXBo5Xq96m1rJL3beCRiOWCyc6kO22s8G6aaNWauELdi5NUcm19CcRKqbJBN9DzLXa1-880xdr5SwfEGmqcZZs_AS_bBM5V9AONjv14l_H1R-Ru2icghq6YLE5SA14T2PqTj-L-6Dr_GD9n2QaL_CKAFdJ2wTGgNEBnYmVpzBXoUhkTWKquG0p-5jDW0gF2JZbG_BhnYBucbM3CtibbthIJ40toLQxNeHMUf2iiyFwtC8EFi5gl8HIYeS3bsJ8MnFNc-T2V-fq7xgUYx6TLIvcjtYLxCRH_0l8pEoPxyTKJFbXu5QzPtwDXfDO3Z66ED9t1_HfpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af6db08f50.mp4?token=TCJqrplRII8WeyVXBo5Xq96m1rJL3beCRiOWCyc6kO22s8G6aaNWauELdi5NUcm19CcRKqbJBN9DzLXa1-880xdr5SwfEGmqcZZs_AS_bBM5V9AONjv14l_H1R-Ru2icghq6YLE5SA14T2PqTj-L-6Dr_GD9n2QaL_CKAFdJ2wTGgNEBnYmVpzBXoUhkTWKquG0p-5jDW0gF2JZbG_BhnYBucbM3CtibbthIJ40toLQxNeHMUf2iiyFwtC8EFi5gl8HIYeS3bsJ8MnFNc-T2V-fq7xgUYx6TLIvcjtYLxCRH_0l8pEoPxyTKJFbXu5QzPtwDXfDO3Z66ED9t1_HfpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از کشتی‌های متخلفی که اواخر شب گذشته به تحریک و اجبار ارتش کودک کش آمریکا قصد ورود و خروج از مسیر ناایمن و حادثه‌ساز جنوب تنگه هرمز را داشتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/673456" target="_blank">📅 17:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673451">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gznx9gfEudLqtN8YVSu1FGXi6JTHs9M7ZXdaMNsIXdrkP6k34i9wxkuhip50_wSUBh-ASmWtbi_nJQ9U2kGIASIOA4LA0QKUHXE5AnK7YenvWIxuQ-T7LU3VyCjN6RUiG4cq2bDEyHJk_C-C_ZgpWZqnK9mVA5H2i5atwVYTyWznLElnk8R5OdrZQTQTIsVWADdnEt9vx_g8di2x7cFqnNasvD_o60t-j4f1uNb1ulbYFbwMMlyGsEQM2Kd-vsrb7IfspEDzwfw6_8hMrXZginilcve9EVFZmmXxQ5VJwChmlZCWDYUCbU67IBSVu65gSxS0GsCA0zB-BkqqbwWz-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iA1MQZ1HeF_RLIaySCbLS3U6V1ep6JIzmdjDJsXUFsx9EHfcf7TG5y15fEA8lu0A5jJvLML4sfw57l25U33IMDwxBso-kbazjPhG1MrQ8gx9lVyNBcyHWd2IMuCd7kT6nX0mUcxJrslyO2vYCen05tlOZq2LdQuMxyYf4wLMFL1lXHNv1rCVWP6UKzOVbjU_d33mYxiqf31NxPrasvPER_APqSMIOGaw-6SOZy_ZNs2_aiU1j7ANTx6yfQ53D0QOFfVLLHJAI_CHilYsn9AEvtQD_6G59r0qf9AfQEbfUp799LUDShWXuRqHY_1sLPV0lNtfZsh8UGfPS0dIZzpd3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a7EwfSxCcjvRa_e3urf0tLjp42r24zQHTOK5rMRKt0p4FIQKQVSBcG2QnV929R4qd5QC0BOgPmnYjAmJnNETkHGw37L8TWj3m4fyCW2_INopKRBZfL36KaJTABVGOpnYESoa3ToZwerYPnMnu5-L0xdNFeHeWvYBOM8v7KYDVgPX-MtzHZAV5s4wIugtmRho0c2BhctjJOmJ_4koEPtklxicxh3hnz05jdynpP1-Ar2eEw7fA5japrZ8_kqBcJep1TFtMsoHRl7nIqF-FbB65LSszNUPyRvE0MX5sP4Dw_qIa6IZNqb2fBWnaXcFUU5HqEYMC2BVAq8L3IpteDwXiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-PtI0yWJmFGB-XzJ0XRhkWKm7g3tH8mZ25GP9Pjf86SQyjzCkycx-cadu6AD0CpbZ26Yg3-eMXIPFiIzGB_iMMDbSXMOTf7ibggk9nDcW3cs1Y1a-kFbsdsg3szZiXsq8rrMwpXNuVV9Yb8JzP1PLsPRbXKYVuJ8-tS_Q8_CAnlVn0KxAEe5pABubX5lIPV4wxmtTbiNAz9ckrmKDcebqkpDSjsD-u2CV-yQz4cNvjR6d9_oIzzZfD7Rcgp8y3R5Vav-m_ByRd9YzZvUfc9QFDP3jsw1thDsG0kScRY-GmL2uEHcIbrAjPvhlmptvJeEG_HqGBH08lXahkchKDa_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzbZhMtqRD4BT1QlaKoAeMgiCVxOwF6lT92EL-AZYdmbU4ZIaRj74oTkGsyncPkQFQuK5Gm0lJYVQYqH3E2iTZHibEUaQbX9HSMzf4YCzvAPh7RG1-OcRTeE01J8uXeeIEpxxoKwOSr8YK0NjouZr6MNPcezEe6X-mazL7YKC_NMVhV-SkRuxK_izpyw_C_NKWEvzBbXaNG8dm1yDeeh_EB1pxgwHNUGYredaaMv6_uupt7PyR9xTec2wzjgZO8xYzQVEipHXF2InDU9C7dBuAzvJt0oscmrWWpDFZ2FUWOXiVGlpj7CcH7wlt8AlNMBIa6XJ3miRez3Le3GfriX4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵ نوع پاستیل خونگی و خوشمزه
🍰
🥛
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/673451" target="_blank">📅 17:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673450">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c35230c72d.mp4?token=Yeplu_QWQiuaAAAq-nmXWv0eoKeQfztE9D-fDGPuB63_egap0vtFOKmhL1rj583OoWa1eAhkKCUs75h9aeIgCscc5UM7kx8xI1uaxKmXxF6z-0BftDknPkrlDILzS-fInOCC5vAN9KZPPJQClpJObU31QPzIj4X7BlgTZGmQ8j1uZSrtsyuYe1uVLd2bcjlLy6UIrYPjDagX5q6B5_7aDthdXVi6-ol4-f6IuA0uDhbWkhc5dlKFGFIo3OEheOrVR44Dgun97qP4AOcnRm6lA7JMnaTT_KMocYdLHAl4X4C4TqAvRXKlK0JISnnX-911WEM05gFPrC8zcRQ8F8YGAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c35230c72d.mp4?token=Yeplu_QWQiuaAAAq-nmXWv0eoKeQfztE9D-fDGPuB63_egap0vtFOKmhL1rj583OoWa1eAhkKCUs75h9aeIgCscc5UM7kx8xI1uaxKmXxF6z-0BftDknPkrlDILzS-fInOCC5vAN9KZPPJQClpJObU31QPzIj4X7BlgTZGmQ8j1uZSrtsyuYe1uVLd2bcjlLy6UIrYPjDagX5q6B5_7aDthdXVi6-ol4-f6IuA0uDhbWkhc5dlKFGFIo3OEheOrVR44Dgun97qP4AOcnRm6lA7JMnaTT_KMocYdLHAl4X4C4TqAvRXKlK0JISnnX-911WEM05gFPrC8zcRQ8F8YGAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
یک تیر و سه نشان!!
🎁
با شرکت در
جشنواره حساب های قرض الحسنه بانک کشاورزی
با یک تیر، سه نشان بزنید.
🎯
مشارکت در کار خیر
🎯
شرکت در قرعه کشی و بهره‌مندی از جوایز ارزنده
🎯
دریافت اعتبار خرید تا سقف یک میلیارد ریال
🔻
افتتاح‌ حساب قرض‌ الحسنه از طریق
اپلیکیشن‌باران
و شعب بانک کشاورزی
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/673450" target="_blank">📅 17:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673448">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fq43cVdlYpL_aYf5DpQS790jlOXawjGkLUL61L1uEFm8j0iBHs7NQa43tj_4hvZYx4pA0lzvRrEUt7mGgFKZdOuxFUtzwZuUfOsg7gWrxXw68QFpJ1GEY9O7QazC5d-9Rs_rUarK3H0TNZnuJOXehvctIbJGsDaHXsvVxqPdYRbTpf7Dn6Qlos50T2_ocPNEh3LJq8F-vhUoM7eOaxU_r8IB1JWszLk1M0uIGSr5ztH1o971d3rEBO-jkEB9sUdhFsMQ5DCnAxSV4h55fq7NAlhfh4IHxr1fw-NIE5ZypFfNZY0dBKnN8dQraPF1YQUVNWwRzBsOQmRhIE-AsH7_2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به مناسبت روز جهانی ماه؛ نزدیک‌ترین همسایه زمین و شگفتی بی‌پایان فضا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/673448" target="_blank">📅 16:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673446">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ضربات سنگین دریادلان نیروی دریایی سپاه به ارتش کودک‌کش آمریکا با حمله همزمان در سه محور
🔹
ملت به پا خاسته و حماسه آفرین ایران اسلامی، با توکل به خدای متعال و دلگرم از حضور هوشمندانه شما مردم بصیر در صحنه، دریادلان نیروی دریایی سپاه با حمله همزمان در موج ۲۳ عملیات نصر۲ در سه مرحله با رمز مبارک یارقیه (س) ضربات سنگینی به نیروهای تروریستی آمریکا در منطقه وارد کردند.
🔹
مرحله یکم: حمله به سوله‌های نگهداری و تعمیرات پهپادی واحدهای آمریکایی مستقر در فرودگاه اَلصَّخیر بحرین که منجر به انهدام آنها شد.
🔹
مرحله دوم: حمله به سوله‌های آماده سازی شناورهای تی‌اف۵۹ در بندر سلمان بحرین که منجر به تخریب آن گردید و خسارات سنگینی به شناورها وارد آمد.
🔹
مرحله سوم: به آتش کشیده شدن سوله‌های محل استقرار و پشتیبانی و تجهیز نیروهای تکاور ویژه دریایی در پایگاه عریفجان کویت و منهدم شدن آن به صورت کامل.
🔹
حملات کوبنده رزمندگان اسلام با انبوه موشک‌ها و پهپادها در مقابله به مثل و پاسخ به تجاوزات ارتش کودکش آمریکا ادامه دارد.
🔹
رئیس جمهور بی‌خرد آمریکا که بارها به ناآگاهی و بی‌خردی خود از اوضاع عالم، اعتراف کرده و می‌گوید بدون اطلاع از عمق نفوذ امام شهید ما در مردم جهان و عشق و علاقه عمیق مردم ایران و سایر کشورها، ایشان را به شهادت رسانده و اینکه می‌گوید بی‌خبر از اهمیت تنگه هرمز در اقتصاد جهان در این منطقه، جنگ به راه انداخته است، شب گذشته باز هم بی‌خردی و ناآگاهی خود را آشکار کرد و اظهار داشت تعداد موشک ها و پهپادهای کمی برای ایران باقی مانده و رو به پایان است.
🔹
رئیس جمهور قاتل آمریکا بداند اگر این جنگ چند سال طول بکشد به اذن الله تعالی تا آخرین روز آن موشک ها و پهپادهایمان بر سر جنایتکاران آمریکایی خواهد بارید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/673446" target="_blank">📅 16:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673445">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac7897cd4.mp4?token=DVYjYs_aoGC4KrsPvuawQ04KVEJCAwxEkVnRZrsWd9wWYeeEe8lmaNIZTsLZbRpc2c0jvwR5DIa5FNjctfChTstoirfIOiE_9vNyRo8NC6vQzzK_PohhreP-nQZ7mpDDq3TZwX3jgbmD-MeDJTJVU8uNh5ZVyiLyhXuD6vB9bqiI8KawPjKlAZ51yQU8rezxillMs5dId57nOL90S9VWzwtlWtj-xmId0Ucn_dEAISKSyj-vqCAa_Psljuvz2U4db2mEBT3_NC5Aii4ZnYgGqgSHRckJNj46jZ9W-TcmlGZNSuoDlaKo0O4EBoZ7CULI81MO4mY0sAm0WypAJqBGEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac7897cd4.mp4?token=DVYjYs_aoGC4KrsPvuawQ04KVEJCAwxEkVnRZrsWd9wWYeeEe8lmaNIZTsLZbRpc2c0jvwR5DIa5FNjctfChTstoirfIOiE_9vNyRo8NC6vQzzK_PohhreP-nQZ7mpDDq3TZwX3jgbmD-MeDJTJVU8uNh5ZVyiLyhXuD6vB9bqiI8KawPjKlAZ51yQU8rezxillMs5dId57nOL90S9VWzwtlWtj-xmId0Ucn_dEAISKSyj-vqCAa_Psljuvz2U4db2mEBT3_NC5Aii4ZnYgGqgSHRckJNj46jZ9W-TcmlGZNSuoDlaKo0O4EBoZ7CULI81MO4mY0sAm0WypAJqBGEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی رباتیک Honor با بازوی رباتیک برای دوربین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/673445" target="_blank">📅 16:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673444">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl0_HBMPqPHgGgAK7GGfsIlHED7JRA97O9qLfBpdXmw1JFcmsXR-OzGvh4LEzdwGhh7vb1S5gng918ryO0JUH_X8lBjWRl25e6NrzmqSM4aQwR73SZDsTlk5sIv1bNX9G5fKvD0uuIVVklZp2BjjO9QJ1pqey3lL1ggyLfCw3lnxMnbRgRcGEsMhama8f4rwg1ooRLSoTJHQY-WVLHrUVjg5REN1_Ust96NBuaObkZGe9WariAa1RU04IbCfz0yk-WYw5AbeRSe4ZpcPKhSoIcMjIN16CgoIRWyGSNuAj587ZIlS8lTptf6if4H_121Y4vyJWydk0db9cPwyNfNk5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا هویت دو کشته خود در اردن را اعلام کرد
🔹
ارتش تروریستی آمریکا اعلام کرد دو نظامی‌اش، «تایلر جیمز فیهان» ۲۵ ساله و «ایزابیلا گونزالس» ۱۹ ساله، در حمله ۱۷ ژوئیه ۲۰۲۶ به پایگاه «موفق سلطی» اردن کشته شده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/673444" target="_blank">📅 16:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673442">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5597d61522.mp4?token=s14Iw2yPtjOiYCOtxlTLlMNMvC7Z21dNN7VE_-rjBpiBvIfOgIrpGqLovZpTSSFBgbUIsK317o2ILcu5Wx_c3u6hcfBKt1W8zJCMw6mbcZplN44mmGaZ3Lh-Yq_sX54n1swCrpj2YpXbCW4KTvQcUsQWFjackQNPlPJXjliy94JEkjuiARZ9jaDTLGemiIIC0yo6mrgSELtT4p9nmMxhd-Fj94BCAta5gEkhOmRMsB13NgzE4KDJwvsLWWX6FgKdgZ0VBE9X14WkfONqhbARmYnlFWgv1QjoyI3QyRa14wdUJjmzLLt0djpo2pWDVnfdwBqd8dcGl0qHyauDU9u3DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5597d61522.mp4?token=s14Iw2yPtjOiYCOtxlTLlMNMvC7Z21dNN7VE_-rjBpiBvIfOgIrpGqLovZpTSSFBgbUIsK317o2ILcu5Wx_c3u6hcfBKt1W8zJCMw6mbcZplN44mmGaZ3Lh-Yq_sX54n1swCrpj2YpXbCW4KTvQcUsQWFjackQNPlPJXjliy94JEkjuiARZ9jaDTLGemiIIC0yo6mrgSELtT4p9nmMxhd-Fj94BCAta5gEkhOmRMsB13NgzE4KDJwvsLWWX6FgKdgZ0VBE9X14WkfONqhbARmYnlFWgv1QjoyI3QyRa14wdUJjmzLLt0djpo2pWDVnfdwBqd8dcGl0qHyauDU9u3DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران وطنم
🔹
پیام‌های صوتی ارسال‌شده به پویش «ایران وطنم»، بازتابی از مهر و غیرت هم‌وطنان است که با گویش‌های مختلف، کلامی از جنس امید برای مردم صبور جنوب ایران به یادگار گذاشته‌اند.
🔹
این هم‌صدایی زیبا ثابت کرد که خانواده بزرگ ایران با تمام اقوام و تفاوت‌ها، در شرایط دشوار شانه‌به‌شانه یکدیگر می‌ایستند.
🔸
شما هم صدای گرم خود را ارسال کنید تا پیام‌آور همدلی دیارتان با مردم غیور جنوب ایران باشید.
👇
#همه_باهم_برای_ایران
#ایران_وطنم
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/673442" target="_blank">📅 16:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673440">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e7297ee97.mp4?token=rvDQnVzva6JQIHUnGRmOjQEP9XJFpYkg4cGAA-48Em6cMJjESHZ-G4sUpJQQ3Id5UHvtBWaMPcx5F85_2qeMv0h48uPhWrh-KFjS39G3qSLv0YaSC7q897uiLQ-rUJv0ja5C-gr2ZaPi0LkFOgH9-59PNnyWii5txV_yjogM4co2bAA484Pli8dsBSHqt4XP7Xkt364bNDZocepmvqfqCJUlDRfnQ-SzzFa_GL5edAb9chyHR8C8VrteyCI9_Bfz6EQPdnMwpaZoj-ww31RxMi6nUrac75gaUvA_SRtiHWCusHgrTKwou4hUjYUrT1R7c4dw8_GjZkEgN2YqNI09QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e7297ee97.mp4?token=rvDQnVzva6JQIHUnGRmOjQEP9XJFpYkg4cGAA-48Em6cMJjESHZ-G4sUpJQQ3Id5UHvtBWaMPcx5F85_2qeMv0h48uPhWrh-KFjS39G3qSLv0YaSC7q897uiLQ-rUJv0ja5C-gr2ZaPi0LkFOgH9-59PNnyWii5txV_yjogM4co2bAA484Pli8dsBSHqt4XP7Xkt364bNDZocepmvqfqCJUlDRfnQ-SzzFa_GL5edAb9chyHR8C8VrteyCI9_Bfz6EQPdnMwpaZoj-ww31RxMi6nUrac75gaUvA_SRtiHWCusHgrTKwou4hUjYUrT1R7c4dw8_GjZkEgN2YqNI09QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما جنوب را نه فقط برای دریا و نخل‌ها یا نفتش که برای مردمی دوست داریم که همیشه کنار ایران ایستاده‌اند... #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/673440" target="_blank">📅 16:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673438">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2cd50499.mp4?token=bbCXNEhG2TkRUaAH0_QUFw6Mv95Nak4KsaFcm-WpDibtG1BETKs4A4rr6F9cn_J4-15cUBtdZgSsUlPjKpSkH1JYvN5DKkB3eBghtV_815CXqonrWAqhh_HNMJnNq99Zq5FuAz932xKHw88hMwgZfCyebd4TvZxlhekGRTZePfXGWQpTOjSEKbSy3-HTIB-74JjXe7bBcruYO7dnysIKyOwS5smHNdYGJ74rg6uwCCCbjjt2EslLfwqp3eDXfV8fRUilj-Op3eUN2tK-zP_DfdOHTLYJvb9NVlj4I9S7i4Low6ty1OvUeM1JWjiVKcSUXnRY1rwqiuRmKvEVXD6tbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2cd50499.mp4?token=bbCXNEhG2TkRUaAH0_QUFw6Mv95Nak4KsaFcm-WpDibtG1BETKs4A4rr6F9cn_J4-15cUBtdZgSsUlPjKpSkH1JYvN5DKkB3eBghtV_815CXqonrWAqhh_HNMJnNq99Zq5FuAz932xKHw88hMwgZfCyebd4TvZxlhekGRTZePfXGWQpTOjSEKbSy3-HTIB-74JjXe7bBcruYO7dnysIKyOwS5smHNdYGJ74rg6uwCCCbjjt2EslLfwqp3eDXfV8fRUilj-Op3eUN2tK-zP_DfdOHTLYJvb9NVlj4I9S7i4Low6ty1OvUeM1JWjiVKcSUXnRY1rwqiuRmKvEVXD6tbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر ۳۰ روز قند رو حذف کنید ، چه اتفاقی برای مغزتون می‌افته؟
🧠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/673438" target="_blank">📅 16:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673435">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/673435" target="_blank">📅 16:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673433">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3047709d8a.mp4?token=KqPqiuVI0JIcby-Pkhnd7JGf55-2f6pfk0vBRzgoGzNDl8054lezP109vIFrvqzmGzOtEapYanXQ8W6nnzdAcip99D8G9ka2CBOKtbk78D7A7njk-t932UA_ti_Fpc45kIMIePJ-fQYKGRT8o2LhuLj0NNoXjLduwKhZ9wrvgSykOTL-ifS8-8k4TPpw5h6skdTtRIE1f0MVI1zcTrO4l7E3CQr-NORHqvyql79FlrQoSXSb79_1qQo75okxKpwQ1ClkexaIfhlE-j0HdegNIEH8-w0u0VpXXqyvrUjb_39vtvRal47bBqQVfXUaYNLHPU1snaf_KvvKYn2pl8CqKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3047709d8a.mp4?token=KqPqiuVI0JIcby-Pkhnd7JGf55-2f6pfk0vBRzgoGzNDl8054lezP109vIFrvqzmGzOtEapYanXQ8W6nnzdAcip99D8G9ka2CBOKtbk78D7A7njk-t932UA_ti_Fpc45kIMIePJ-fQYKGRT8o2LhuLj0NNoXjLduwKhZ9wrvgSykOTL-ifS8-8k4TPpw5h6skdTtRIE1f0MVI1zcTrO4l7E3CQr-NORHqvyql79FlrQoSXSb79_1qQo75okxKpwQ1ClkexaIfhlE-j0HdegNIEH8-w0u0VpXXqyvrUjb_39vtvRal47bBqQVfXUaYNLHPU1snaf_KvvKYn2pl8CqKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معادله حسابداری رو با این زبان ساده و مثال کاربردی یاد بگیرین #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/673433" target="_blank">📅 15:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673431">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d40c47dcf5.mp4?token=lop4D_pD_8h1lmvhSs0ldWb6DFKqNcXQhvmZJAVCqqhxAe-11E5Lr1ZWA3rI7IwJ_WmATO44q_31Pz1a_KlsEEumQEm7QzQdarRbYTHTL1eEyhY5ayBv1wGqtnRoiJdR1Qe3dlhjWK8lcBtoxtnOIb3vbLqebVcZICu3nGuJdcjaX9GIzHQ82nML0c85cHwy7zKp7CqF3znogAlg2wCvsqGMiFpBtFeKy3JQ7yW_lyZl8aQdeOJnGQL58gZql_AtaMJ6Nxzo4k_pSAxidyutiiZfUSsgRlVh2kQ9d0DG0JRRNtHYf0LRbsZMBZyX8EDor1l6Puc0vjiieLvGv-V4JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d40c47dcf5.mp4?token=lop4D_pD_8h1lmvhSs0ldWb6DFKqNcXQhvmZJAVCqqhxAe-11E5Lr1ZWA3rI7IwJ_WmATO44q_31Pz1a_KlsEEumQEm7QzQdarRbYTHTL1eEyhY5ayBv1wGqtnRoiJdR1Qe3dlhjWK8lcBtoxtnOIb3vbLqebVcZICu3nGuJdcjaX9GIzHQ82nML0c85cHwy7zKp7CqF3znogAlg2wCvsqGMiFpBtFeKy3JQ7yW_lyZl8aQdeOJnGQL58gZql_AtaMJ6Nxzo4k_pSAxidyutiiZfUSsgRlVh2kQ9d0DG0JRRNtHYf0LRbsZMBZyX8EDor1l6Puc0vjiieLvGv-V4JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
سرم سفیدکننده دندان LANBENA
🦷
کمک به کاهش زردی و لکه‌های سطحی دندان (چای، قهوه، سیگار و مواد غذایی رنگ‌دار) و روشن‌تر شدن لبخند
😁
✅
روش استفاده:
بعد از مسواک، دندان‌ها رو خشک کن؛ ۱–۲ قطره روی گوش‌پاک‌کن/برس بزن و فقط روی سطح دندان بمال (با لثه تماس نداشته باشه).
⏱️
۱۰–۱۵ دقیقه بمونه، بعد با آب ولرم آبکشی کن.
🗓
روزی ۱ بار (ترجیحاً شب‌ها) | دوره ۷ تا ۱۴ روز
برای دندان حساس: یک روز در میان
⚠️
روی دندان آسیب‌دیده یا لثه ملتهب استفاده نشه.
🍵
تا ۱ ساعت بعد، مواد رنگی نخورید.
📦
حجم: ۱۰ میل
🟢
قیمت تخفیفی: 898 هزار تومان
🔴
قیمت قبل: 1̶1̶6̶7̶ هزار تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/56228/180124/</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/673431" target="_blank">📅 15:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673429">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49ff2d4703.mp4?token=JeJK2gUpTVdrew0Q7YfOjn8f8CCLKw2J-PpyuaPA3louPfwl3LWfsr0Q5QkrCFGIbfk9BmR3Blsz5ml0GYtH-2GjBaH_C6fUG0Xjxd7MMawIBHxTFBgZleJGh2fj97o225jAg16wIs-pGGg9lgXtzVgLzxJ-B_2hKlGqGFjDIwGPy9CaIhdPMwwJ_dUZ9KE0miiTHcdoCu9NG8IthPFps0XHM6QhVh8nKYweAQEjP1VEe3GjvTuva1BaILu2wS5nC1E9Y8LQ83ryzx3eqiUneaNMfdUoDYuR_ycIRl1PKRN9jfjhDOMywfwfvu8VNlN8U30Z7dbwyOs0IUH2b620WYzB4Vr1hnoUdGaBXSRM92YIQ3uVbBdJixeZPfLqpZGqR6mFAXGhLnqBqpa3Faysl9dsn3nnR5oUT99E8Se07BJCOcT-AgAeLXcvaFnYU9jeTxwiX74MUIwbqnHWqPWcJndRGfFFMNhpJYInBkfg7BInHAX38nQU6xckphWGOGWQuRQS_UMVCp_98B1qJ4Tg99rceFZmDmvSXxZC4ZsH8SkIp6vnKOtJaNioLXTRm78q6N0imFZGknvzgeS2YJb7KNXtk2x3b8Qh6mVhGhKvvKyLarSmkzWMbZeo3JNTBBmqtmBduDw2DYLfmGH_fb2H5lv2oQQa0hlr8IOFa3R85UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49ff2d4703.mp4?token=JeJK2gUpTVdrew0Q7YfOjn8f8CCLKw2J-PpyuaPA3louPfwl3LWfsr0Q5QkrCFGIbfk9BmR3Blsz5ml0GYtH-2GjBaH_C6fUG0Xjxd7MMawIBHxTFBgZleJGh2fj97o225jAg16wIs-pGGg9lgXtzVgLzxJ-B_2hKlGqGFjDIwGPy9CaIhdPMwwJ_dUZ9KE0miiTHcdoCu9NG8IthPFps0XHM6QhVh8nKYweAQEjP1VEe3GjvTuva1BaILu2wS5nC1E9Y8LQ83ryzx3eqiUneaNMfdUoDYuR_ycIRl1PKRN9jfjhDOMywfwfvu8VNlN8U30Z7dbwyOs0IUH2b620WYzB4Vr1hnoUdGaBXSRM92YIQ3uVbBdJixeZPfLqpZGqR6mFAXGhLnqBqpa3Faysl9dsn3nnR5oUT99E8Se07BJCOcT-AgAeLXcvaFnYU9jeTxwiX74MUIwbqnHWqPWcJndRGfFFMNhpJYInBkfg7BInHAX38nQU6xckphWGOGWQuRQS_UMVCp_98B1qJ4Tg99rceFZmDmvSXxZC4ZsH8SkIp6vnKOtJaNioLXTRm78q6N0imFZGknvzgeS2YJb7KNXtk2x3b8Qh6mVhGhKvvKyLarSmkzWMbZeo3JNTBBmqtmBduDw2DYLfmGH_fb2H5lv2oQQa0hlr8IOFa3R85UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همه‌ ما یه ریشه داریم... ریشه‌ای که اسمش ایرانه هرچقدر شاخه‌هامون دور بشه، ریشه‌مون همونه #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/673429" target="_blank">📅 15:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673427">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
محاصره دریایی یمن علیه عربستان؛ صنعا معادله «محاصره در برابر محاصره» را اجرایی کرد
🔹
نیروهای مسلح یمن با صدور بیانیه‌ای رسمی در پاسخ به محاصره ۱۲ ساله این کشور، از آغاز تحریم و محاصره کامل ناوبری دریایی علیه عربستان سعودی خبر دادند.
🔹
صنعا با تأکید بر آمادگی کامل برای رویارویی با هرگونه حماقت ریاض، اعلام کرد هرگونه تصعید نظامی را با تصعید متقابل و همه‌جانبه پاسخ خواهد داد و از ملت یمن خواست بسیج عمومی را تقویت کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/673427" target="_blank">📅 15:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673426">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec3e9b7c6.mp4?token=W27zGnfIqqe-6hC-kE2SKrszFwN9fxJ9RlT9GYmqQYmwbojUsRJmo5MhYTZB3iA7P-qC63K9wRBnpmiCjBBzbpty-PUlq_w9Y8WDpKt78_sBzHSPE_XcIxM9zScGrsSdj_SFmtaRjiFabfuPoICL76JeF-dHeVRz8IyOU6rLu5WA4kd0NHQn7zybkNUmD2HsyOmvTxIaRnPJTqdWmR4fxPdnykfoJBY0yCwOQ0a68rvSRAcoQIoRswDbx7NMUPaS-uOhywCf_1yaD4NMY_J6SVj8NbKjr2vc0TRQi2P5CxwfnpHgXGcQT_HTbm_BAg9Qpt49X7bQjHrZCRD5I9NjeWtJm73uh-E9y_gaFLEg-DeYO9DgJP5dfK1FD-gQYDbO3Eg70yBA8bnCLo02QCayTeWDICN03wtq6Bt9dW85MZe_-R3XWwiSyBC-ChkcJfxy1ZJ933vn12TRPt6D2eN6HW5donUjPAOldHM3bktC6Aem3o5c33l-AKwSNIknNoWiDBOygCZiFc-rYkxKqJysti0V19hObMwkOZo2I2uQsjAsW58TORwwVTw1VWWG5LZNrH54ywzwALKtBstbdhLr6FyBuJN2E1tLVsf7Cy-YGfK5RN5J8CHBaV98g9CHWKlhBR86924P_mLl_lJlg3dnSb0334YsB7NrBJ0L0gFTFXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec3e9b7c6.mp4?token=W27zGnfIqqe-6hC-kE2SKrszFwN9fxJ9RlT9GYmqQYmwbojUsRJmo5MhYTZB3iA7P-qC63K9wRBnpmiCjBBzbpty-PUlq_w9Y8WDpKt78_sBzHSPE_XcIxM9zScGrsSdj_SFmtaRjiFabfuPoICL76JeF-dHeVRz8IyOU6rLu5WA4kd0NHQn7zybkNUmD2HsyOmvTxIaRnPJTqdWmR4fxPdnykfoJBY0yCwOQ0a68rvSRAcoQIoRswDbx7NMUPaS-uOhywCf_1yaD4NMY_J6SVj8NbKjr2vc0TRQi2P5CxwfnpHgXGcQT_HTbm_BAg9Qpt49X7bQjHrZCRD5I9NjeWtJm73uh-E9y_gaFLEg-DeYO9DgJP5dfK1FD-gQYDbO3Eg70yBA8bnCLo02QCayTeWDICN03wtq6Bt9dW85MZe_-R3XWwiSyBC-ChkcJfxy1ZJ933vn12TRPt6D2eN6HW5donUjPAOldHM3bktC6Aem3o5c33l-AKwSNIknNoWiDBOygCZiFc-rYkxKqJysti0V19hObMwkOZo2I2uQsjAsW58TORwwVTw1VWWG5LZNrH54ywzwALKtBstbdhLr6FyBuJN2E1tLVsf7Cy-YGfK5RN5J8CHBaV98g9CHWKlhBR86924P_mLl_lJlg3dnSb0334YsB7NrBJ0L0gFTFXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیامی چهارصد ساله...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/673426" target="_blank">📅 15:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673425">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEeSOvEUjU6UebBg8c_MyMrUB34ga8fYvIFoglEqTPuDaW37wBOWf8SJcf77smxdz-zib8d8v22ZQ111BR658rTD-JQqXAuH2rIkrCMy-0Pmg9yG6bMNtjRfchQ-qRAzsla8rcXvuQcHthnrCCOQ8XiBb7GrUjYe6dSgxm7WYpp5chUWYtkbA1VnUTDjHCvNm5iob3qdYYVsAkT9MRDIzCN7ncpmglOTQCATs33_kVtSSjZqzxq7U3fLzZm6jwt1XDoa4SsWc4Rw47v53v0vh31QdPNMGeocStJn1yLh1QITI5CTddGCgsSz0ZfN51dxHLk8psuA7zXV51hNiVVJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش قیمت نفت در‌پی بعضی ادعاها درباره آینده جنگ
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/673425" target="_blank">📅 15:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673424">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ادعای رویترز درباره پیشنهاد آتش‌بس ۱۰ روزه
رویترز به نقل از یک مقام ایرانی:
🔹
میانجی‌ها پیشنهاد آتش‌بس ۱۰ روزه را برای گفت‌وگو درباره راه‌های احیای تفاهم‌نامه اسلام‌آباد ارائه کرده‌اند./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/673424" target="_blank">📅 15:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673421">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-p3Tbof02MAx38b7csGb9_NzAUKVbvP0sJBe5Aw8dhf3qk13RBn18gLTnWBdtDQNm50Kae7rL4W25U8qbycAPaSw8SzMQoAH-QaJr5OZ39JfJHHVXmygHGjkpoCtjl_zgdNniPq5lhWldZV4ZtnCBvSmA0IqL0nUZnj12Hon24OVHLRs5D_eo8lNeSTu5J5pNHHu8jNbfoWwRCT5hHAPKhlhoCaoYuJJJ3X1g6PG5xra9GHp0235mEo7lJk3Kp14PXV4LlY-zYTPFya17YEzEGsQpa7TbFMGpIRvDj1vNHc0FhEv4p7C6n64HwOhOgZpTpIboSvwIXU7lTzdjay4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اژه‌ای: من شهادت می‌دهم که رئیس‌جمهور مخلصانه در حال خدمت به مردم و نظام است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/673421" target="_blank">📅 15:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673420">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlKz_q8Te5tU-i_uyHf-bOFTl_cd4j88as1hXXYrlzkavvJuqRZPwdOqgjVxp-AXY5Z2Msf9UFObnrhDuvIGeuPcoaHhYaPmoDwz3bBmrDb8cSPwTxm_3wRzLmPUabhDYIWx6uqoWgcBd00iz42EKjHGlVQ_doF5NWmK-mnuPk4m7w7zEh6UiMOMAKRXA23gj5Y-1UuPiQDJcwpBjHBAR0rrbvShgOGYKOcwMl7_hRHUZaC22At38y7VYVRkUPOZgE8U3tWf5svPM1aYE2zKB1m_f_MNAreR5fD6z5Nw_35rnf3u1xi5jWMIgVySnAAjizKec-YfppUs89Uxxck6rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اندی برنهام به عنوان نخست‌وزیر بریتانیا منصوب شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/673420" target="_blank">📅 15:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673419">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C71EPojgB2PQEYMAOsu1T1E6h_HWwJ7dklix9EOtOyAEigkhIVtxybe3aYcZ8ePRp2MbaDSrJEdIbKzalURjCgywFCGaISGXPknBVMFbraM0_zdgevAn65hOQucyCp-joZBrPJ_fsa5lVbpexXT_ZXprm82vJyKhaLBR8OjlBd7T4QCD02iORjXOdFeZL4vGcJrUI5xmMKl0o0a0I_Ih4Tq_GBbGO1Efo_AVuKE_iSJX79vmN_3J688uMmorq8MomYWXIed3UOuqNhkusi7HCwMRpagzVvSWMVlIgPlkEQEsL0_PNepaCJmVwVSzEFZhnNFKZ4-ND2E_h7tHa0DOhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سگ‌زرد: بر اساس یک نظرسنجی، اکثریت مردم آمریکا از توافق با ایران حمایت می‌کنند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/673419" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673415">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixxFuUynPgtYjgIuhZFbVsnWeGEexQ0zFKbz-PfXgDiIn92MSY7YD8BevlgtBwvr8tAMSSUsfRmt9uKRn-671wIPKQMxIfFFyoKDBG6CKs1T1VPZ6ku62Oujmlw4cR_DFGKvXNrjFbrqFzlbUK6Jzmt0Y6pNd4BjTJOrjUnkAzyn0bhDTWNC65lQKlU_zlK765D0El0ikZi-cdmD2Hj5jFEFxNPvzaByKDjb64_pZZE9sCdSYHJDBgxiwzSPhvCKEHGqHHcip21TJVD5dpDAHSjkrETXhH7CH_LnlcT-xJkj0MaKENbsU8TdQ_eYp8d3588JTwLLmAf1Leq0BZ7KSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگ‌اند
🔹
آمریکایی‌ها روی هوش ما اندازهٔ آی‌کیوی مختصر خودشان حساب کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/673415" target="_blank">📅 14:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673414">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEGbqkQX6IkaSZkUaN_D_RRhoVpkBqWJ1tmhtJlYbmHRwZ7MSsBEFY5YufuvF4Wmc6ceGTpf-t-bePyepemZgl-N-scxTyPFcJ6MhgR2cjEBv5Qdlkw0Y2RfaqufwLlFZETiKpC_sRLnKI7W09sNB0EQ0YMdYfWlp12Qhbd5T6pO9U90QndcJ6BSOwEWMrL7ONm_Fzi7i7FYFkBaxAI2uKcfGyQlPHNOCQD6QMkY3T6ScoEfYmuWinv47PV6BmCCzSy2ObY35OBiGyScs1pIw6bYbI3DNXC4vmyusKGX32NPoxL7hTwhqazJMnJ9fF7AjPSINj1zeoEw41LQdqEHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خلیل الحیه رئیس دفتر سیاسی حماس شد
جنبش مقاومت اسلامی حماس:
🔹
پس از یحیی سنوار، خلیل الحیه به عنوان رئیس جدید دفتر سیاسی این جنبش انتخاب کرده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/673414" target="_blank">📅 14:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673412">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99db1856dc.mp4?token=j6KDxdk0xpsuIWMv262xHVS52Y4TsYaYKwP6bAchVbdH8eCpyjsnZ6_4TBL3wAynxBFv3NMr9gR8uR90FyovgpXfPd8--LNN_y5jK2DEnW08Va5lSYPW46WfBnwtTqd_nMP_uzGGwUYR1eHV8wCEg2X6KVdfpH-_iSXULdYyhIOnVkXn1I0K5aS6Yu84Em0sLQCtH0LC4ZQw3G4z02c39F5wisGwruBCoaGUWOnqIBwnYhP-hOr3YcMScTnQh5QV4j51aACi-ADOPmrpTPB7QnI8cjhVZcAl-pTGRdl1uuiLzrwbhtkxNxjdrz1hktk4XmtVS1S2jpBgyxnbrfrqlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99db1856dc.mp4?token=j6KDxdk0xpsuIWMv262xHVS52Y4TsYaYKwP6bAchVbdH8eCpyjsnZ6_4TBL3wAynxBFv3NMr9gR8uR90FyovgpXfPd8--LNN_y5jK2DEnW08Va5lSYPW46WfBnwtTqd_nMP_uzGGwUYR1eHV8wCEg2X6KVdfpH-_iSXULdYyhIOnVkXn1I0K5aS6Yu84Em0sLQCtH0LC4ZQw3G4z02c39F5wisGwruBCoaGUWOnqIBwnYhP-hOr3YcMScTnQh5QV4j51aACi-ADOPmrpTPB7QnI8cjhVZcAl-pTGRdl1uuiLzrwbhtkxNxjdrz1hktk4XmtVS1S2jpBgyxnbrfrqlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشف پهپاد انتحاری حامل مواد منفجره در سواحل استانبول
🔹
بقایای یک پهپاد انتحاری در منطقه قره‌برون استانبول کشف و پس از خنثی‌سازی، برای بررسی فنی به آنکارا منتقل شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/673412" target="_blank">📅 14:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673411">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
آمریکا هویت دو کشته خود در اردن را اعلام کرد
🔹
ارتش تروریستی آمریکا اعلام کرد دو نظامی‌اش، «تایلر جیمز فیهان» ۲۵ ساله و «ایزابیلا گونزالس» ۱۹ ساله، در حمله ۱۷ ژوئیه ۲۰۲۶ به پایگاه «موفق سلطی» اردن کشته شده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/673411" target="_blank">📅 14:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673406">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfmGoM7FHDzmo5H0NyumL6xLomANLlp17V9GfSGZXAYEQjc-5ENtRbk2Pn7Ol_xSSxCmqkDBzYS1-lKC7JtfEFUt7_VjkkU0oh-p9px7d6wysSg42HeTc3bP9vSqN-Toy-Q9vlp9O8qG68PUsno5mWAmID9pRkY3oGgHdG6Y3m71N0D1gqQ0CWjBAw05Mg5wz495VADs4fE46imlWyhYbVfseJKhI5fTMCHvuIRUupXWtGxdE7ys5NcrkCvb1y8-XF-kshEGcEESA7ACHmaRg70tpEY_XUEvVsRh3a_cy0qEM4uIDs6mPA48NjLXz2sbRYV5BDxeWlsju-uFOx-mmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدیدترین مدل‌های آستین که استایل شما را متحول می‌کنند
😍
#فوری_استایل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/673406" target="_blank">📅 14:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673405">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CapjIHIqsL8icdIPSZWu5n7Y6PF5LZBxcgMkJahe30AQFSYwERecuJ7Q0FKegBCIpD3Ex37ol44fGdwd0ssJktVLYwV08M8g9coMv8gRfg3M-2mWMaxlScI1fmbJK2Bp1Gb12U_fnDikjssa1q94TLprGN8iw5C0V071FXa0W9MfixwmhfG7plvMfNZXr0CMRgrQDfCWpJbM5zW1Q0ZxwJaPB59Ff4SvSoMo797gVE2Z6gdZ-pZ7niuVLMJ1q1zl8hFrxImfR-E3zag62pNdsZE2oil3zhHYImlAgxYNi3ryryYXtE0tpVuiGVsEjKlEXSzV8HcvJaoHoHP61YurSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر نیرو: پایداری برق جنوب، ثمره حماسه «قرار همدلی» مردم بود/ همدلی؛ تنها رمز عبور از روزهای داغ تابستان
🔹
وزیر نیرو با تأکید بر اینکه پایداری کنونی شبکه برق در مناطق جنوبی کشور، بیش از آنکه مرهون عملیات فنی باشد، مدیون مشارکت فعال مردم در «پویش قرار همدلی» است، اعلام کرد: آنچه این بار توطئه دشمن را در ناامن‌سازی شریان‌های انرژی ناکام گذاشت، نه صرفاً بازسازی تأسیسات، که همراهی آگاهانه و همدلی مثال‌زدنی مردم شریف بود.
🔹
عباس علی آبادی امروز در بازگشت از سفر به استان هرمزگان، ضمن تشریح شرایط مناطق جنوبی کشور اظهار داشت: دشمن در یک حمله ناجوانمردانه سعی داشت با هدف قرار دادن زیرساخت‌های انرژی، آرامش خانواده‌های هموطنانمان را هدف بگیرد. اما آنچه محاسبات دشمن را برهم زد، قدرتِ شبکه برق نبود؛ قدرتِ "قرار همدلی" مردم بود که با درک شرایط خطیر، الگوی مصرف خود را با مدیریت شبکه برق تطبیق دادند و اجازه ندادند خللی در پایداری شبکه ایجاد شود.</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/673405" target="_blank">📅 14:04 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

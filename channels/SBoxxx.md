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
<img src="https://cdn4.telesco.pe/file/Kg87VKarncqgkm8QpXvt91sKZ1ANKTgg08HI9G3zF4Kmr8UGxQmJwUxUGThgygdY-CbphDf8UWngmdklL25Tf23xfbTazrYM7aU8adMLSlPYm42BRWNuGOkHxXDMOKnaiy0bZ79NlEwk-G2akS_-IpoCKS6muwGrfiisTUlKxjo8H2FNeX7UOtEBLYyLhqEn9z6jN_nwNdOIlj70eMenVJdeMDq2ffu3xUM3UEALJl54foCUYHx-VIRm_fjTDQQRirxSBbjLTl3A5o5FYyYCpW1xvXL1MejOosPd1ijBWi6BsP1WWNDnvMWn50PZd1c4c9hH7ARHU8gn6crMZtilIw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 13:28:27</div>
<hr>

<div class="tg-post" id="msg-19478">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwGbeCxKraa7e6UQHIKbMxCVdjY4zzq78jptdzcBlwsAvb3GlmpQVT4CDTJYBO6vu_F6ut_5DLjiOWTq3cTK6qAA-bidDzB7I7FJVg_Q4BfACPRWnfyrAEo8pKT70avytZIaByVvWd6CPd85aQqS5yuqiFLA4hAJUdwS_kCk4tSxQtqqCIFycwMXjICBoSw-GjhHh4kDBAB2JvkxswDTJpLK0NMR-uy4SkM-eYcnMjXELtGPO1KtIrhhDiniP9SXTmUidiP-Jj1ItfMUmKhHcbe4QBloaB1XUSJDHZv1cFlJEyz4RfNY-51uZZ2Y8OY6P-JesNe71dSnO5F5EkGbaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لینک نشست دیروز با نیما</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/SBoxxx/19478" target="_blank">📅 12:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19477">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8eacd406a.mp4?token=Nbtts1XfrD729VJ5ywGwa-b4j_5GKPfDyr1ZzXzlna7y6M16T_54G1pwbmmGkQuYRfsaSG759yk_SmfpFlOF2eBaG9pnrKzKVpXUWLQ3-GgsOYpoWqaUnKzeLNueg6ZsZOVHljZN5K-ZexZWIWdb2stQhmV6Mmc0jOxQk8clVmQYR7lyVB4USODYoxfSHkrHxiwFp-ZTAQhFAThkAwFgnzdy5uif8LC9TD74mdPl4y_GhFmC_1beIXW15bYJg_Ff-0zz4zJZdFgjFlwkzw38ZSStrjVBz8GJEkMy0WjgVNJ8EiJIHZ5O0nwaXTrmed-Ne6i4geCSfFFl93-Ea0rtRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8eacd406a.mp4?token=Nbtts1XfrD729VJ5ywGwa-b4j_5GKPfDyr1ZzXzlna7y6M16T_54G1pwbmmGkQuYRfsaSG759yk_SmfpFlOF2eBaG9pnrKzKVpXUWLQ3-GgsOYpoWqaUnKzeLNueg6ZsZOVHljZN5K-ZexZWIWdb2stQhmV6Mmc0jOxQk8clVmQYR7lyVB4USODYoxfSHkrHxiwFp-ZTAQhFAThkAwFgnzdy5uif8LC9TD74mdPl4y_GhFmC_1beIXW15bYJg_Ff-0zz4zJZdFgjFlwkzw38ZSStrjVBz8GJEkMy0WjgVNJ8EiJIHZ5O0nwaXTrmed-Ne6i4geCSfFFl93-Ea0rtRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبور موشک های زمین به زمین اتکمز آمریکایی بر فراز شهروندان کویتی به سمت شهرهای خوزستان</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SBoxxx/19477" target="_blank">📅 11:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19476">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0Z0PbuiMZnDtwcurh6V-gJZ_jwItul-H4CWMmTmuMnIGSum8UGJd9bBVVlq-putJC7km0XsuI3c4ttQCBe8iYSiQuYXOdnkVM7_TJLcDayQ36UC39zumkYYMUBi2ALxdsl6EcaIAa4PJJjqs_YRp2HbD0bBT2FBPvjr7jIhQT96I1IqcS7iVwKGHNRKYJsoc20zWGanLJwiO6l0uowrFrU9QGZ0cE34kr6c1XLzqnvdZKoCf8nevvoV6hOFiRVSNYiTfqCBWhv_WycDRrGKP2AOBlL_CahYhIDrG1YFUgOUPHcLDIkjkJVYsk9l8yx-6xrADSDsbdvYSIa9l2hgNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این همان حرامزاده ای است که دختران را در لایوهای خودش کتک می زد و به آنها اهانت می کرد که خوشبختانه به این روز افتاده و تا مدتها نخواهدتوانست شرارت کند.</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SBoxxx/19476" target="_blank">📅 11:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19475">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhDcbGfmKpzF181DV2f6gZXhpDpVIOk9vkIuzoI-VxqqYiAAIA_pmo5xjFpkoBHfXBT29eb_17FkWIFFh1FiLjG08RjBXHPJAvvknTBfoJkwUcVVlsadxzgQl3z20eiEjqR8T7C7g18PgW_4AyOL_qzWckjXNoE-ta_s4TF-Y-8yr0n8bSwAuyeLjJZQVZuXqOF439fsSz-JsZphKCV9qQv5X6-a3PQKNQNV3i4uqLE6Qlw67B1vGv3iXCOa16AUduXn9UFfBZDHsHtKzZ3T7DVPMPy6DXDLd__iMOKOhBIV25vY-hsj55xKMKnfGjGvJI4NshIOvc42Ctr1VUKQuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدها چهره سیاسی، حقوقی و عمومی اردنی، نامه‌ای سرگشاده امضا کرده‌اند و خواستار خروج نیروهای آمریکایی از اردن شده‌اند.
آن‌ها حضور آمریکا را یک خطر امنیتی، سیاسی و اقتصادی می‌دانند که این کشور را به جنگی می‌کشد که تمایلی به آن ندارد.
این یک اقدام نادر و علنی است در کشوری که به شدت سرکوب‌گرانه با مخالفان برخورد می‌کند.
اکثر رسانه‌های اردنی از انتشار این نامه خودداری می‌کنند، و برگزارکنندگان هشدار می‌دهند که امضاکنندگان ممکن است به زندان محکوم شوند.
خشم عمومی در حال افزایش است، زیرا ایران همچنان به هدف قرار دادن حدود ۴۰۰۰ سرباز آمریکایی مستقر در اردن ادامه می‌دهد.
آژیرها در سراسر کشور به صدا در می‌آیند، و بقایای موشک‌های رهگیری شده در مناطق مسکونی سقوط می‌کنند.
این هفته، در پارلمان، یکی از نمایندگان به دلیل پیشنهاد تسلیت برای سربازان آمریکایی که در خاک اردن کشته شده‌اند، مورد انتقاد شدید قرار گرفت.
یکی دیگر از اعضا، ارتش آمریکا را به کشتن "کودکان، زنان و سالمندان" متهم کرد.
دولت همچنان به این ائتلاف متعهد است، عمدتاً به این دلیل که واشنگتن سال گذشته ۱.۶۵ میلیارد دلار کمک اقتصادی و نظامی به اردن ارائه کرده است.
اما جنگ بخش گردشگری اردن را نابود کرده است که تا ۱۸ درصد از درآمد سالانه دولت اردن را تشکیل می دهد
منبع: نیویورک تایمز</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SBoxxx/19475" target="_blank">📅 11:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19474">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-xVlZ6l2gic-d18GpJzLZeMUUWNZMhW53sft70QSRi65iFDH-VM8gc-H9a6ZkBsGDI8p51yUuKjoiTx0hJNNrHyiumNXbb7cSkAP92rFNShBlfNZuVxfef-c0IEVQya5TrA_WLe3ffLjkwhgqQwawtiQrN0PMTww18e2mnico_7KeODsusBPDeIe2DHWj1ZtUXBfI55rL7d64aiVcUbDQmmFJV6w9pn4mRAsjzjLo2Cr_rVXkwKoPUd-Ms-fk-b8QWfW_g46KBwGyvtFzAmAefVsHK52giVvch1JY5raCBZOgD-Uh3xUGsH9gOJPVyMO76y4D4xNBsfLNZq-lvj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهداف حمله پریشب حمله مشترک سعودی و آمریکا به پایگاه های حشدالشعبی در عراق</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/19474" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19473">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سپاه پاسداران:
با استعانت از خدای متعال، متجاوز همین امروز تنبیه خواهد شد.</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/19473" target="_blank">📅 11:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19472">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlfMYU26OzEbA52DTw3pz7wOXh6Z2Ao48livi20psETVy7SbgelcGL6QRNJOpiaHn0CDPOIKSJCDPLYG9MoHCkPme7fTtL_1jyY2hQ3nXItNZzB3cFSPcrzCEqzNpv20MAmZebzyn-3N82p4QHlBd2kNXOhsvOq7wvsdeF7nQaxbwYBL8ijrLDLt_LKW623aTX758yag3AsbP-BNKxoLSVQHGmQVhXptX71Z3CvsiEhidQ2CIb004QqpMZ0ffmeOWVVpRM6xuMfQ35bfm0U7Jc9eiaeL89tAXI0OQn8vS8T29sj01lQoWbhQeQeLLU4-dkZlFh8JALGgC7cTnFtMHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح میانه پایین است و حالت رنج برای طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/19472" target="_blank">📅 11:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19471">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">این تحلیل درست 4 روز پس از پایان جنگ 40-روزه ارائه شد و همچنان بر اعتبار آن افزوده می شود و خواهیم دید روزی می رسد که تنگه هرمز را فقط خودمان استفاده خواهیم کرد.  از همه کریدورها که محروم ماندیم و سهممان .... های باقر شد این هم از تنگه هرمز!</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/19471" target="_blank">📅 10:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19470">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پرسش: اوایل این ماه، رئیس‌جمهور ترامپ در مصاحبه‌ای با یک خبرنگار گفت که در رابطه با شما، همه می‌دانند که چه کسی رئیس است، یعنی خودش. او کسی است که تصمیم‌گیری‌ها را انجام می‌دهد. آیا شما هم این‌طور فکر می‌کنید؟
نتانیاهو: خب، شما می‌دانید که در آمریکا اغلب می‌گویند ترامپ هر کاری را که من می‌گویم انجام می‌دهد. و در اسرائیل، اغلب می‌گویند من هر کاری را که او می‌گوید انجام می‌دهم.
و گاهی اوقات، این مسائل توسط هر کسی، از جمله رئیس‌جمهور، در بحث‌های عمومی مطرح می‌شوند. اما حقیقت این است که ما شرکا هستیم. ما متحد هستیم.
او شریک ارشد است. این کشور ایالات متحده آمریکا است. بیایید این را فراموش نکنیم. و من شریک فرعی هستم، اما من نخست‌وزیر اسرائیل هستم.
و وقتی لازم باشد، من برای دفاع از منافع کشورم و امنیت کشورم، این کار را انجام می‌دهم.
منبع: خبرگزاری ABC News</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/19470" target="_blank">📅 10:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19469">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نتانیاهو:
ترامپ اساساً سه گزینه پیش رو دارد: اول، دستیابی به یک توافق؛ دوم، ادامه محاصره؛ سوم، اقدام نظامی.
هر چیزی که منجر به پایان برنامه هسته‌ای ایران شود، چیزی است که ما می‌خواهیم. این هدف مشترک ماست.
س: وقتی با ترامپ در کاخ سفید ملاقات کردید، آیا تلاش کردید او را متقاعد کنید تا حملات به ایران را از سر بگیرد؟
نتانیاهو: در واقع نه. این یک تصویر کاریکاتوری یا تصویری اغراق‌آمیز است. این درست نیست.
ما در واقع تمام سه احتمال را بررسی کردیم، و من فکر می‌کنم که این کار را به صورت شفاف و در بین دوستان و متحدان انجام دادیم.
و این تصمیم اوست. این تصمیم اوست.
منبع: خبرگزاری ABC News</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SBoxxx/19469" target="_blank">📅 10:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19468">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شب گذشته یک منزل مسکونی در قشم مورد اصابت پرتابه آمریکایی ها قرار گرفت  احمد نفیسی معاون استانداری هرمزگان از حمله دشمن به یک منزل مسکونی در محله چاه‌تنگو شهر قشم خبر داد و گفت: تیم‌های امدادی در حال جست‌وجو برای یافتن دو یا سه فرد محبوس‌ در زیر آوار هستند.…</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/19468" target="_blank">📅 09:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19467">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فیلم سنتکام از هدف قرار دادن اهداف در حمله بامداد
چند پرتابگر متحرک نیز دیده می شوند</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/19467" target="_blank">📅 09:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19466">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حمله موشکی ایران به اردن</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/19466" target="_blank">📅 09:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19465">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شب گذشته یک منزل مسکونی در قشم مورد اصابت پرتابه آمریکایی ها قرار گرفت
احمد نفیسی معاون استانداری هرمزگان از حمله دشمن به یک منزل مسکونی در محله چاه‌تنگو شهر قشم خبر داد و گفت: تیم‌های امدادی در حال جست‌وجو برای یافتن دو یا سه فرد محبوس‌ در زیر آوار هستند.
احمد نفیسی خاطرنشان کرد: جزئیات تکمیلی این حادثه و وضعیت افراد گرفتار، پس از پایان عملیات امدادی و ارزیابی‌های میدانی اطلاع‌رسانی خواهد شد./ایرنا</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SBoxxx/19465" target="_blank">📅 09:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19464">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">شهرهای مورد حمله قرار گرفته از ساعت 3.5 بامداد
🔹
قشم
🔹
اهواز
🔹
بندرعباس
🔹
آبادان
🔹
اروندکنار
🔹
شادگان</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/19464" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19463">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شهرهای مورد حمله قرار گرفته از ساعت 3.5 بامداد
🔹
قشم
🔹
اهواز
🔹
بندرعباس
🔹
آبادان
🔹
اروندکنار
🔹
شادگان</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/19463" target="_blank">📅 09:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19462">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حمله به آبادان</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19462" target="_blank">📅 03:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19461">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQnxFSEhoojf9W0WjOeeBauDzWtb6aUSjNPTWY-LKA3LIw8ODpJuvXOA2BvyfOVJbh2uLEGJYqIn6dJXLOIwmn7k_wCZ8qaZKIAode3oO0gJ_aP_ech-Id3YV13G5JvlSBczit2Juk-0L7IG53qeNMR6BE_Pp7naOW0GwZeuJf1LIRESuqvIQ1p_drfYSUn77QjJlpcQ8J5x5tYDSm0Gd9YWNCk11_wWuEtU5Xypp9HdALPG7JICVFtpgk-0XYiwnfe-8UXeNQLizm1fEaPlohYvnk50BjOf7YVLLiYSho6tinxHqwMi-s8jFVQi78j-Whuoek3cGBwpxb2rFvj6ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات آمریکا تایید شد</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19461" target="_blank">📅 02:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19460">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">چندین انفجار در ریاض، عربستان سعودی، و بسته‌شدن باند فرودگاه پادشاه خالد در ریاض.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19460" target="_blank">📅 01:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19459">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انفجار در اردبیل و ارومیه (تایید نشده)</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19459" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19458">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QE-JcU9OW8lzJXOS-g0zhr3yQMa-ICEIDt9i_B-jqB_VT8VfbLjdPH-1Q6cW_4Lall8dQqMOAjTQ1fr2MCcyAz21KiLvoK4X_kWLGrunhL7S9TQdRWGehaF464IJeCJbU61-IVDA1uXMYQ2sdKVRDngr_u53XaTomP5P2sDU-hbLbHBXYoT4c4EzxzCF4EDbVD4RmQ2ijVAveILVayOW71fS3U8H-mR2GWwgBpoMkT9FNe-aua-SrEs-vDZqxN9xrtmtftLcxTgENLD60dXkGC8jkMfTD7C0dKw5F5Dg27NPN7jixL_WuBxc6yQN80aSeeURj1GSuHCYne0Ol8dIHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا که اخیراً محبوب حضرات شده بود و چهره یامال را روی موشک ها میزدند، اعدام های اخیر در ایران را محکوم کرده و خواستار تعویق اعدام های برنامه ریزی شده شد.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19458" target="_blank">📅 00:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19457">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpJU-QxSNjGTxyWSovHvHDrszuLYBrmPJeD5_7UnQGC7WPHcK5DfAHfQbMGJWae39hQHdMAdiTvm1xbMJj0sFQO0mkJv8ER3UTy2MpDjzzCcp4hJJ6zosAkXckZ6x-z_BoOkVtQy76nJzgwBPMLo0nWtyTu3NDVv-nBjUTnH_gf773UBUX4XBkZhuonVwFlUGmX-NlVqIo0sbSP9ca4NyjrjDTmsCG8ower5WaOxOdSlI-FCogonaIu3S99oWfbiBwiJbQYE76CcZmYkrjKd9BZPcWbSUMl3SQl_K6ieaT0eZFTlz38YQ_tHnjRfMJo-moguhE24CYT-RI0PulpHRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا که اخیراً محبوب حضرات شده بود و چهره یامال را روی موشک ها میزدند، اعدام های اخیر در ایران را محکوم کرده و خواستار تعویق اعدام های برنامه ریزی شده شد.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19457" target="_blank">📅 00:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19456">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdQYnGCuCDJpbf8p52NaqjhkHXdPsmXeMppghyypYm54eUt-kMgOQuZFRQxql80-W7iJyd28v1iRenK7ePKIdLkfDunZDcqma9_RY4FMOTpYJcvhQ5IAszSGS9oX8t7DG6SW3AO2ZTx4J7v7tS49J27L_yKU811DyeUbyKHJpDsn3KcGnHF6V8VkQKk6rjVFEFz2H6I-UlBnDrHfG3BRd8OSeF28zGfYGU_iZ4iFmiiIhKtUL_ZaWSGjFXBRT470_N9U8K3z7MVnffOd4HIRr_9WdHKiXkwmv0vOmxAppR1JnxJzc9i2JM4LuHaKNHQNVJo-9gR83hMKivVKi4fYZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیدوارم آن یک هواپیمایی که نزدیک تهران است جنگنده نیروی هوایی ما باشد.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19456" target="_blank">📅 00:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19455">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر
به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19455" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19454">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXr_mOgtAH7AN-36SobnQ446QghXDxcDkkwEPMQ8dYfPizehly8HK48vj0jKWq7A5J-Sw7sg4ygYJXtVKWBUuOYt_MnJ3vykQxEImyzzHHKUlDi-fUsBXeEREwfzwQGh8EvxF5gQd1jBEBMeq2jlrEMQWJIG1OUFSbL5rLGXH2A8Lx2f2dVzKj-Xnf_BXqJfE9g3uHxBGO-w_-3DjUTXWwAJgfqVKzEhAGvy9P7ij6X0RbJboyktBzR1lFKZdlBAbHu6DRwACa6rNYiDD9FbqDcjA3Cia453xim8o-VrDhB1ZrN2X08eUcS_5gc-_0MhmMfz_sLJn_xm-_va_tCo3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز هم در وضعیت مناسبی قرار دارد و انتظار رشد طلا می رود.  دقت کنید که امشب نشست سرنوشت ساز FOMC را هم داریم که سناریوهای موجود در این یادداشت بررسی شده است.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19454" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19453">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3185a6e49f.mp4?token=raH1CYze9pHeiNS3Kb3hlwnxhRddueXxPG9PlUUo2x7uyDgq7COa0RxpCswVYS8DfnYG0iVUs8qAacOMpTJ8vED3yhpjORN9cGr_HgmoaIheZWHqq44qeelu415DAHGm6kAHna8r5oNiug7S00iD13JK18UZa-cEPc0iZcJsYhxvVVazrba45jSWYC9yEUVy8R5kIlxNWaDUNWA1U-IhHKeGUoGNL_7FwzPLRHePG3C4iXCsjEGiQhan9XGfezqloNtqTdMV0OVtT-iwfUwD1UuFX8O5VFWG20oHizZ89ze59wTTnUDOd6GAGnpFREDGSjN0IO8gXXw9I-YJXu1D-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3185a6e49f.mp4?token=raH1CYze9pHeiNS3Kb3hlwnxhRddueXxPG9PlUUo2x7uyDgq7COa0RxpCswVYS8DfnYG0iVUs8qAacOMpTJ8vED3yhpjORN9cGr_HgmoaIheZWHqq44qeelu415DAHGm6kAHna8r5oNiug7S00iD13JK18UZa-cEPc0iZcJsYhxvVVazrba45jSWYC9yEUVy8R5kIlxNWaDUNWA1U-IhHKeGUoGNL_7FwzPLRHePG3C4iXCsjEGiQhan9XGfezqloNtqTdMV0OVtT-iwfUwD1UuFX8O5VFWG20oHizZ89ze59wTTnUDOd6GAGnpFREDGSjN0IO8gXXw9I-YJXu1D-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک غیرنظامی اردنی به طور تصادفی، فیوز انفجاری یک پهپاد انتحاری ایرانی مدل "شاهد" که سقوط کرده بود را هنگام بررسی آن، منفجر کرد.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19453" target="_blank">📅 00:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19452">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
ارتش اسرائیل آماده حمله سراسری و بزرگ به ایران است</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19452" target="_blank">📅 00:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19451">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارش‌هایی از پرتاب موشک بالستیک از اطراف یزد در مرکز ایران</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19451" target="_blank">📅 00:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19450">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ درباره ایران:  آن‌ها می‌دانند که این اتفاق (حمله) در راه است. از ما می‌خواهند که این کار را نکنیم.  دیشب سعی کردند با ۵ موشک به ما شلیک کنند. ما همه آن‌ها را رهگیری کردیم.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19450" target="_blank">📅 23:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19449">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ:
آندی برنهام باید به مهاجرت اشاره کند زیرا این موضوع بریتانیا را نابود می‌کند.
آن‌ها از آفریقا، آمریکای جنوبی و بخش‌های مختلف آسیا می‌آیند و در حال حمله به اروپا هستند.
این یک حمله است و بریتانیا مظنون اصلی است.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19449" target="_blank">📅 23:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19448">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWwndm3KckF_6697jA9PSnmY73tPECn2oBpsIBCE6HHvj1MpljVdSb5ysgqy_U9k1xQrQke4broq--h49KjYd-0cCjahHJwID81pApJiw8M9CRp-SVae22O9SlgFN79dhQNpfLzlV1oQmkJ0xf4cGatr4UyhFyjdNcIWwKMKwzy1yuzqr6X6hT8zBZ2DWw13GK3_Zjy-pKK8oRyZRm_s97JAcSn7DGkQ5GiyDSvxYCUcObum8TZ4rayDoKYCizMCddeJbeqgTQwxLQwB8frqkirUD2Y9EB-WtzcUl8rFUN-KRbYOYd3uxTIln7IqeJvC1qbuGadvo-Y5qC4obE6vZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19448" target="_blank">📅 22:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19447">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها می‌دانند که این اتفاق (حمله) در راه است. از ما می‌خواهند که این کار را نکنیم.
دیشب سعی کردند با ۵ موشک به ما شلیک کنند. ما همه آن‌ها را رهگیری کردیم.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19447" target="_blank">📅 22:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19446">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ درباره ایران: آن‌ها را به شدت ضربه خواهیم زد، نوبت ماست.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19446" target="_blank">📅 22:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19445">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">علت رشد طلا در چند دقیقه اخیر:
مقامات امنیتی مصر به شبکه خبری "الحدث" اعلام کردند که هیچگونه حمله‌ای در بندر دمیاط رخ نداده است. آن‌ها مدعی هستند که این حادثه یک آتش‌سوزی بوده که در بخش موتور یک کشتی از رده خارج شده رخ داده است. - خبرگزاری "کان" اسرائیل.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19445" target="_blank">📅 20:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19444">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یک مقام ارشد از یکی از کشورهایی که در این میانجی‌گری نقش دارند: کسی که تصمیم‌گیری‌ها را انجام می‌دهد، فرمانده سپاه پاسداران انقلاب اسلامی است. - خبرگزاری کانال ۱۲ اسرائیل،</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19444" target="_blank">📅 20:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19443">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">انفجارات در اردن!</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19443" target="_blank">📅 20:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19442">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رئیس‌جمهور ترکیه، اردوغان:
دولت فعلی اسرائیل که تحت تاثیر جنگ قرار دارد، با تحریکات و اقدامات سازمان‌یافته خود، همچنان منطقه ما را به سمت بی‌ثباتی سوق می‌دهد.
اسرائیل با نادیده گرفتن حقوق اساسی بشر و زیر پا گذاشتن قوانین بین‌المللی، به تدریج و گام به گام، سرزمین‌های فلسطینی را اشغال می‌کند.
اشغالگری اسرائیل، سکونتگاه‌های غیرقانونی آن، و سیاست‌های آوارگی، ارعاب و سرکوب علیه فلسطینیان در کرانه باختری – همانطور که در غزه انجام داده است – منبع اصلی مشکلات در منطقه ما هستند.
هزینه این تجاوز نه تنها توسط برادران و خواهران فلسطینی ما، و نه تنها توسط مردم لبنان، بلکه توسط مردم با ادیان مختلف و کل منطقه پرداخت می‌شود.
به عنوان مثال، به دلیل درگیری‌ها در منطقه ما، عرضه جهانی نفت، یکی از بزرگترین شوک‌های تاریخ را تجربه می‌کند.
متاسفانه، این فقط نفت نیست. قیمت بسیاری از مواد اولیه کلیدی در بازارهای جهانی، از جمله گاز طبیعی، کودها، سوخت دیزل و محصولات پتروشیمی، نیز به سرعت افزایش یافته است.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19442" target="_blank">📅 20:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19441">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نتانیاهو:  من همین الان یک گفتگوی تلفنی با آقای پیتر هگست، وزیر دفاع، به پایان رساندم.  او نکته جالبی را با من در میان گذاشت. ایشان به من گفتند:   «ما به جهان نگاه می‌کنیم و کشورهایی وجود دارند که اراده مبارزه در کنار ایالات متحده را دارند، اما از توانایی…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19441" target="_blank">📅 20:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19440">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ec0VrVtBLP63PlIgrIwIjb_Ax6huyWRTYZSHFi2ySM4NP4U5qg7wMaXBZyUC-ACg-5WdEB_la8wWPTN4jK1czbJcbQBschTOgzIaouD2H60hTFi0a_ScUA2EfBI_yuMa5XQtg14Pfz6BIDVW-FJTQ5WzMAv7cVgef8yuPxZz5cvyiBCiJrFLui3gxtuz4MVTV_Kga4OR55rRpIzNy4cUNbpyv2lZAVejW-BBXcuTAzTih1GoeyX2zgHuvn5til39hgp8Z6-DnhRb8DZdGCC0Z86wHYPWuanCpnCKUXd90isuxIm15pBJuiWpeXwywAhjo4obxK8bqMwJU_9V4v5jmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:
من همین الان یک گفتگوی تلفنی با آقای پیتر هگست، وزیر دفاع، به پایان رساندم.
او نکته جالبی را با من در میان گذاشت. ایشان به من گفتند:
«ما به جهان نگاه می‌کنیم و کشورهایی وجود دارند که اراده مبارزه در کنار ایالات متحده را دارند، اما از توانایی لازم برخوردار نیستند. و کشورهایی وجود دارند که توانایی لازم را دارند، اما اراده لازم را ندارند اما فقط در اسرائیل است که ما هم اراده و هم توانایی را مشاهده می‌کنیم.»</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19440" target="_blank">📅 20:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19439">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مقامات اسرائیلی می‌گویند نتانیاهو در جلسه روز سه‌شنبه با ترامپ در کاخ سفید، نقشه‌هایی را ارائه کرد که میزان نفوذ اسرائیل و ترکیه را در سوریه مقایسه می‌کرد.
بر اساس اطلاعات ارائه شده، اسرائیل حدود 0.1 درصد از خاک سوریه را تحت کنترل دارد، در حالی که ترکیه حدود 5 درصد را کنترل می‌کند.
نتانیاهو از این تصاویر برای مقابله با فشارهای قبلی آمریکا استفاده کرد، از جمله تماس تلفنی ترامپ در اواسط ماه جولای که از اسرائیل خواست نیروهای خود را از سوریه و لبنان خارج کند.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19439" target="_blank">📅 19:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19438">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19438" target="_blank">📅 19:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19437">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یک مجتمع شناور ذخیره‌سازی گاز طبیعی مایع (LNG) متعلق به یک شرکت آمریکایی و دارای پرچم جزایر مارشال، در شهر دمیاط، مصر، مورد حمله حداقل یک پهپاد قرار گرفت.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19437" target="_blank">📅 19:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19436">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یک مجتمع شناور ذخیره‌سازی گاز طبیعی مایع (LNG) متعلق به یک شرکت آمریکایی و دارای پرچم جزایر مارشال، در شهر دمیاط، مصر، مورد حمله حداقل یک پهپاد قرار گرفت.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19436" target="_blank">📅 19:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19435">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به خبرنگاران گفت:
«ایران در حال حاضر تقریباً ۱۵۰۰ موشک بالستیک در اختیار دارد.»</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19435" target="_blank">📅 19:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19434">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مقاومت اسلامی عراق با محکوم‌کردن حمله آمریکا به حشدالشعبی در کربلا، به دولت عراق تا ۲۳ صفر مهلت داد تا توانایی خود را در دفاع از کشور نشان دهد.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19434" target="_blank">📅 18:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19433">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مقاومت اسلامی عراق اعلام کرد که انتقام خود را از حملات اخیر ایالات متحده تا پس از مراسم اربعین به تأخیر می‌اندازد تا امنیت میلیون‌ها زائر مختل نشود.   این گروه هشدار داد که حملات علیه نیروهای ایالات متحده اجتناب‌ناپذیر است و گفت که در صورت لزوم عربستان سعودی…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19433" target="_blank">📅 18:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19432">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مقاومت اسلامی عراق اعلام کرد که انتقام خود را از حملات اخیر ایالات متحده تا پس از مراسم اربعین به تأخیر می‌اندازد تا امنیت میلیون‌ها زائر مختل نشود.
این گروه هشدار داد که حملات علیه نیروهای ایالات متحده اجتناب‌ناپذیر است و گفت که در صورت لزوم عربستان سعودی نیز می‌تواند هدف قرار گیرد.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19432" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19431">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رسانه‌های ایرانی گزارش دادند که 4 عضو سپاه پاسداران از کاشان در حملات مشترک آمریکا و عربستان سعودی که در طول شب به سایت‌های حشد الشعبی در عراق اصابت کرد، کشته شدند.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19431" target="_blank">📅 17:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19430">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نتنياهو امروز با پیت هگست، وزیر دفاع ایالات متحده، دیدار خواهد کرد.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19430" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19429">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حمله موشکی ایران به اردن</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19429" target="_blank">📅 17:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19428">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmEzLhbey_uYAcBDm7kV_mW4fnTu2px0pO7YFin23wNkQCxABsb0MrjYZMMSFjR7QqO265mMp7mULvBrv06hbu5Sl6IVj-rUIJlUhbHQEdNvHazbgvHAOkGqD9VZikRl4VA4eV4Fw8QMbQpMaFzjfaU7Z18h9-WiZxDx-wdIH8tff5RDOvig9TlVxspVJIepEewMeJFC52SOFLuVt9VfqEnmLgXzyFcyMEZ1aejNqAUVxp7iB8vTelBigHaHN5PxtDkDbd3xyiNIEbxqu5FJwUaw0tJMpa0zRy-sM9muQ5nqArcd7ygiwZfJ2VFIcwDTymGmZhVjLXQ2CKNcCjcQqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای وزارت خارجه در هدف قرار گرفتن مواکب زائران حسینی در حملات دیشب سعودی و آمریکا!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19428" target="_blank">📅 16:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19427">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19427" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19426">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19426" target="_blank">📅 16:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19425">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انتظار می‌رود که اسرائیل امروز به حزب‌الله پاسخ دهد، اما این پاسخ احتمالاً مناطق جنوبی بیروت را هدف قرار نخواهد داد.
— کانال 14 اسرائیل</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19425" target="_blank">📅 16:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19424">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده:  «حمله دیروز ایران یک غافلگیری بود و نیروهای ما تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.»</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19424" target="_blank">📅 16:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19423">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده:
«حمله دیروز ایران یک غافلگیری بود و نیروهای ما تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.»</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19423" target="_blank">📅 16:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19422">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وزیر دفاع اسرائیل:  در دور آخر درگیری‌ ها جنگنده‌ها و سوخت‌رسان‌های آمریکایی از اسرائیل پرواز می کردند اما ایران همه را زد جز ما</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19422" target="_blank">📅 14:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19421">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پرتابه دشمن به استان آذربایجان غربی برخورد کرد - فارس</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19421" target="_blank">📅 14:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19420">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مطمئنم امین سهامداره  @Piknikanalyst</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19420" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19419">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RZ3MnI6hYpYT_iWLvAza1UCVMkN2fuVmMQnAE9c9UzDskLLrBsehTnxs6ZUSu95hKY-AgZm0EKPiJvdIcDwC2uPZUOBzOh7Qmpafl282RBwevF0z63PJB1LkpBlaG4Csb-qRtnINsMUrd30lDturWqpslq7KT5iCasSDanRTClRZD2vxftvkF4ETe1qXrWZti1FGQhiNIp1faRwyRELZqPdU_Q9yAs5KSsNtmLffAc4y7IPH_s5vqCZDCQNbGFkcpgCMGJWbuX0FgvvFPI2TeS-eONg7HXkEwVPOPXsrc_srX0XisEUulzu29a58hWvUcUijiQqHUMa7N5hSWURSJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطمئنم امین سهامداره
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19419" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19418">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نیروی هوایی ایران اعلام کرد که جسد سرتیپ مجید کاظمی، خلبان جنگنده بمب‌افکن سوخو-24MK که در تاریخ 2 مارس توسط جنگنده‌های F-15QA نیروی هوایی قطر سرنگون شد، پیدا شده است و طی چند ساعت به کشور بازگردانده خواهد شد.  نیروی هوایی ایران همچنین افزود که مقامات همچنان…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19418" target="_blank">📅 11:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19417">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFxtlwKqwDAQQox0qJ5vMHTPr1FH3WiP-CjMeLjgpVI7VZWEUEaCppA7NgG5rivSCSJA-rd3uJpF_mBWxAAHwP10djuEFQyrOEbq4se5SIFrg-e9frmduxudWohLQB5wkmsq6LzGdmz-yEfquaJ88jnPHm43Fzb6jZdkBdTslwj4aMFDJ_Okff6HXFFOjhlU44f42YICUKLTdqs8TBaDv79jlmlGo56LJOLVBpOKXLirbEr2SXMsu4Ff6ioDCaMVIx2vJVoVjSH_-bdsHI9dbkcV03CFrocUpCKJMxb4rgSm39Z3BQ2zCKmbletam-_V7RKjwvBkBhHYnE9OQEIxBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران تأیید کرد که تعدادی از ناوگان بمب افکن‌های سوخو-۲۴MK اش سرنگون شده‌اند.  این هواپیماها در حملاتی در عراق و سپس قطر شرکت کرده بودند اما سرنگون شدند.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19417" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19416">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a40b3b45d.mp4?token=FHYWyVmPDItkxNLDBp-gYtUtDE1iQfuHXQwQKyB4qdBS3AfwQLu6paxIqVX5uqtreN3TKuMb6OqZBFD3JrEeK4SUr44lPpjGZauDwRq6fmZwP6sxtyovApFQouRlnqcVJkh0eBR1aMRwHFLmf--D6fN-PN2lMy3IX9tSeqDSCUCnh__4-3FNhnPs2WULaUufu-Abh1xnYSsJkvLxlZ75tvdhFYR8aSZfMP2wzSjr7vNVwJplIhnbDnW0qNkp7xD5Guu1nn_DdF9cnv09yjqIdUpXfl-6_894zoP3im2xUEemPM2NBw2CAIT4rZONop_odrhQt2lKR2weoE9VwBmJMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a40b3b45d.mp4?token=FHYWyVmPDItkxNLDBp-gYtUtDE1iQfuHXQwQKyB4qdBS3AfwQLu6paxIqVX5uqtreN3TKuMb6OqZBFD3JrEeK4SUr44lPpjGZauDwRq6fmZwP6sxtyovApFQouRlnqcVJkh0eBR1aMRwHFLmf--D6fN-PN2lMy3IX9tSeqDSCUCnh__4-3FNhnPs2WULaUufu-Abh1xnYSsJkvLxlZ75tvdhFYR8aSZfMP2wzSjr7vNVwJplIhnbDnW0qNkp7xD5Guu1nn_DdF9cnv09yjqIdUpXfl-6_894zoP3im2xUEemPM2NBw2CAIT4rZONop_odrhQt2lKR2weoE9VwBmJMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمار تلفات حمله عربستان به حشدالشعبی  ۱۰ کشته از تیپ ۳۰ شَبک ۲ کشته از تیپ ۲۴ حشد الشعبی</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19416" target="_blank">📅 11:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19415">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQgG0ahaD1EeNUgE4D4fqlqqnOt6iIrtjNvLSabtVAL-gk9bIZBkZZPKgVX9HzEClREEVBgIFss-0Af7aHGIzq3pnGGbL6S758_q9lyUR9SR7gu4Vknk0aorwHQutxtK0tPOx3x9H_SfiZcKfdrl1yXF-8rwoUMzjq3TW05kwFumBEEobfePKDznM-ZIklXqI6d_qDX4S8ydz5c49mkciJb17LGYc6i0gYFd64tmqNPm3UPTQnlr7WyAO_131VubB3T5591xj3XenCXol2dTapB7L0VKFK5JMcjf5j5WXEhKVe72yp3D3JNmfSQYoHVYzhL65dDsgZoPQOovNPdROQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز هم در وضعیت مناسبی قرار دارد و انتظار رشد طلا می رود.
دقت کنید که امشب نشست سرنوشت ساز FOMC را هم داریم که سناریوهای موجود
در این یادداشت
بررسی شده است.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/19415" target="_blank">📅 11:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19414">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خب مثل اینکه «درنظر داشته» حمله کند  ایران، پس از حمله اوکراین به یک کشتی ایرانی در دریای خزر، یک حمله نمادین با موشک‌های بالستیک به یک بندر اوکراینی در دریای سیاه را مد نظر قرار داد.  اما گفتگوی تلفنی بین وزرای امور خارجه ایران که در آن این حمله به عنوان…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19414" target="_blank">📅 10:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19413">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خب مثل اینکه «درنظر داشته» حمله کند  ایران، پس از حمله اوکراین به یک کشتی ایرانی در دریای خزر، یک حمله نمادین با موشک‌های بالستیک به یک بندر اوکراینی در دریای سیاه را مد نظر قرار داد.  اما گفتگوی تلفنی بین وزرای امور خارجه ایران که در آن این حمله به عنوان…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/19413" target="_blank">📅 10:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19412">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPi8JQzaPV3LbK4swPnn7YG1XMub0odw0ss9IdawNa5EmmIJZUKNtBbt-7zCdzLxlwI9qop3CqiR2Zqpg80JJorAAQdJwDZtDMGzChcwpqyZb7Ne8LYLwecTBmrOFqJeeIRiBnk15uN3s_qIpuFVCM11qZfPIfhqYjJknp_UFc7pU6eZlh8i97B46VCXtt33VSDvu84bnpWCVmtTyhC7bd-Cjc1froKRqxnDw4txYNIlMHwshcbQRT7GsxQizmoIaYA7K1ptmnorVyz73Ny5HtDr_oJUMAknL7sec4FIGW4nfQhvktq4UoaAU0KcAUaLfY0aFglyzHGDp0v-RWQkGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: ایران، یک حمله تلافی‌جویانه به یک بندر اوکراینی انجام داد.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/19412" target="_blank">📅 10:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19411">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-ANNaM4FzrMqI3MsAjnqHQtvXBMte3FaK_TKA9PB_uegkoYigo3LYMFM5mXN16TA-lr3soGcqDPPHGj3ZlmW0hvSA8oTfYGY0XojIRRYRMjTIkNL-ZSrO3N7l6r9MpaIfFv9THlxVkzwxjHibOVr6rfK_LawkD55Jrg065zDPylQ4P0PSPXX1zi9PzjyX4ZrAzYW0S5XJd2d-xeP_VmqhSjOur-4cIu2JCtMIyGf4WFI2V668BBSbAqGwdgPzaoUbvRqu1AD2s6XYarLK8BakQfL6xPr_fhotvA7hlSR256x6UVut5WHpBp0Kxlh5hHRketZiKGX6qcHuOVFMaJlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش‌ها، ایران قرار است در یک قرارداد به ارزش 60 تا 70 میلیون دلار، 300 تا 400 دستگاه موشک دوش‌پرتاب چینی (مدل‌های QW-12 و FN-16) دریافت کند. اولین محموله‌ها طی چند هفته آینده از طریق شهر اورومچی و از طریق پاکستان به ایران ارسال خواهند شد.
این قرارداد از طریق یک واسطه مستقر در هنگ‌کنگ به نام "Zhongqing Baoshang" انجام می‌شود.
چین و پاکستان این گزارش را رد کرده‌اند.
منبع: رویترز</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19411" target="_blank">📅 10:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19410">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDK56ci4iYuXnWlp553rhy3sVZOJHAYRw6MlFoP7tP9R1bJ1HdMoecy0SX5hGqnvu7NC1ix9NCbSncRnNcCb_M5dFvyYeFZ-PrtirkiFHf2bJa1rNwjK1aY7gYpHg8pIwuuxKamIMTdLoxLs7p7Bfiebkj3Fg1ALm__Shy0rdoKVIJHxwVQPhyMGY4Y9DswzZKwylcP-ocNnDMyuSwckmXFUMC-msb2yJgExwqJDAJSu5XQ5lG7qi3ePtj-7Vrg9PRNq6reROwe1kvZS5PQBR7m54PdT4BvngSmPWeHHzfZHKwgXCN7TnN_A9EEduSdbZf24AP33yFc36lFox-DQGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: ایران، یک حمله تلافی‌جویانه به یک بندر اوکراینی انجام داد.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/19410" target="_blank">📅 10:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19409">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نیویورک تایمز: ایران، یک حمله تلافی‌جویانه به یک بندر اوکراینی انجام داد.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/19409" target="_blank">📅 10:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19408">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حملات عربستان به عراق !  گویا نیروهای حشدالشعبی هدف قرار گرفته اند.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19408" target="_blank">📅 09:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19407">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTroDn3XIKa7IC9TdGcmyT3BhMQcH-BeNb3DO02FPy2CWg9yNKQlWE8PCFJgeTG1QwsACQVbsDvEtJrIOmXwVqakECsBpEhY9SPlx2B-xhGZ8WEDCmAtoeaxgeo78dvu2rM2d-pOWETUpixzap1mKZSwGdnjDS5ich3wwaUrHdtsbFm-FJPIxZlYkGMWvD1T9sCyC5narQKymfWDdYviEbGi2TIMCoZWSs9QsJyFdtpV6_8gVcb0aeMbe6_w6r5IVimHr8mjvDU2i2l2ASwTx3groRzVz9rn5bIwbBcRaoIwYKu-eRxl1EIMmdDcF_t9EbQcKUJu_OCU0zDLY61_Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
فدرال رزرو در دوراهی حساس؛ تثبیت نرخ بهره یا افزایشی که پیام انقباضی ندارد؟
محتمل‌ترین سناریو برای نشست فدرال رزرو، تثبیت نرخ بهره است؛ هرچند افزایش ۲۵ واحد پایه‌ای با لحنی داویش نیز همچنان یکی از گزینه‌های جدی بازار محسوب می‌شود.
واکنش بازارها به تصمیم فدرال رزرو بیش از خود نرخ بهره، به پیام کوین وارش بستگی دارد و مسیر دلار، طلا، اوراق و سهام را تعیین خواهد کرد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19407" target="_blank">📅 09:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19406">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حملات عربستان به عراق !
گویا نیروهای حشدالشعبی هدف قرار گرفته اند.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19406" target="_blank">📅 03:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19405">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCpsB0m4P5OipQ7Je7yo4fVqBGCp5Iv7wEhPzGxFXzdqZCC9j3eBO1XWrX6GX4eLcGdmH-QCZpuVwN7k0HrcRjlhwwKzGOI3yFgfkx0HiRwjHBC1vLS1DZmrJ_oYN5oKVFRy758ejeunusII0mZhbu8gZU6SSg59xyROX0FsZXBUqUNcZS8fRpxGkeGFsQcSV32KSyuNNwJ3WYI3Yu8JNltgAastKLZD8q42sqkZzbd8ZtD8CiOIYe2WcqRLtCqXZ2uvwIo5cvDwLkFGGV9VSKFp3EDleQsL9I4ezsnkiKp9cvCTGJd5ejJAy7-vMXfDnEjJDgITRc-tkM5yGd_hXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/19405" target="_blank">📅 02:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19404">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGQSfU7mTJwMHnTCY61v-48DevWPfl6Gww-ZNjxQejRhHeyss_pdeinQ07ONlE_0uGSt39-jmCTBegSgAZHJXerhdF3DbWcBKJQclgCJnV_tCDDkYl5Gq-VMKJbrYfJsT41A5dHcVP5kRGQKVTgrNca8k7t46DUuPC8Epf0xoFW0ELVTUS08g8N0LpwwnL4SGxdqoAjZojwEqICzCs99Q3R696j2Fl-zXsuupKKTEmXBBR0q5VyU57M9RpfWHsf13MBd7ztOhYqAYgeNSvO4rEP1YhIMYuiRKnFVgWqCICqjkU85O2EfOHDZCfPyHVslmGF7e5Xfsu5TsINCXz7C4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه جنگنده های ما پرواز نمی کنند و این یعنی احتمال حمله هوایی بالاست.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19404" target="_blank">📅 02:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19403">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfXbWWYxAeGgCfaYRCtsyb_ClzGj_bTJuJkEC2nbmHms_w0hirXsgRn7NZniIWD4SZwAXNdhW6AHQQS14LkuGOlpuJt2oFZlhpON93A8wn4CMBH7vYNhAav0HLerlzo-zt7rJpRoMnZe42nPDKFNR6i8xZaH7sMRk10xLYTNsp0DcONRrEUGeZ_6m-fEAW-TB2CxeACaLBp9d_SkrblI6AHbZwv5CCSdS8ZbVugXyi8WdiKkVouN7jW-rPFKH7OVILc4Ts7pfjRnxLayPZ_8VnhGpy96Dow2M-aM1b4UfrP3FnA7FqYY9nx5BnzVpo3FNY4ChHZy5oOVyyscwLs-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلاً قیمت نفت بیش از 5% پرواز کرده</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19403" target="_blank">📅 02:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19402">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دیدید؟ همه گویا رهگیری شدند!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19402" target="_blank">📅 01:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19401">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQ93gmsW5oAKLu5-URqQrJwof8HMR3tsiADtGJCqf6f-lAffOJKY8JjdVa6NltkqVwqNF1gpL-1Aq9nQT8rH56qCgycWioNR7ksXl43HxCclS23umlTPS3TTrpxznZqibbxaYC_Kln4DhLmv0L_0RIzh6IJ0uM3L7anhJc2RP7udblANMdspVv6MAeuRFDhPt69oXBGR_l9cDUvb0o5c1CnDjzXs1H18K392dVpR6SbT5Aw1js8WskSa8_jS9KWXvL5jePYUANcPiG-r0JfAdJNoZ8mrD1RHoxcWv7lbrYSEa1pRT_kNITop8jn7Sy-bjxm6PzvDF_gGisudfQ_NjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدید؟ همه گویا رهگیری شدند!</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19401" target="_blank">📅 01:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19400">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اگر هدف پایگاه الازرق باشد هیچ اتفاقی نمی افتد.  مگر اینکه یک پایگاه الاحمر نامی را بزنند تا در هم کوبیده شود.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19400" target="_blank">📅 01:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19399">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">صبح ها اعدام داریم، ظهرها قطع برق، شب ها جنگ!
بعد برخی آمده اند تولدم را به من تبریک گفته اند!
وا بدهید لطفاً.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19399" target="_blank">📅 01:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19398">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMmop9sgWsInY3F1D0UX1wTJ8f-QkZBQMjj6OHvY6SSNGkqnI4Xubdph1NgS9Iwlr5oM7FeD7pOB9lccAc7vXbjsf9hjSkU_coW2QecZJa7u-jY4SdXuhxDX8FJFvO3PqbXqSJWHuEwR9CfIyoBUPnSz_KM7Cbqmefy_g5bjzIkk21utchmvNvmxQnePlxMAI2im0YV33Ju4tfRHUDvqPFvBCSevPU-DyNdJBFyfVSOl-jNVmpg9M3hsNvjVre5X1fqfHoJeTD77HqQvGS6ZQfz2I-YeR0CViiBt3LVmUHOiA4LWJgSWTNEuG8uQ7PoHXiw6OB-O_FL7RkclE1NFGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جا دارد دوباره گوش جان بسپاریم به آوای روح بخش بانو لورا برانیگن که زینت بخش این شبهای پرکت خواهرمیانه است.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19398" target="_blank">📅 01:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19397">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">جا دارد دوباره گوش جان بسپاریم به آوای روح بخش بانو لورا برانیگن که زینت بخش این شبهای پرکت خواهرمیانه است.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19397" target="_blank">📅 01:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19396">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مقصد گویا اردن است.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19396" target="_blank">📅 01:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19395">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">به نظر داریم وارد موج 2 از 5 می شویم و موج 1 از 5 تمام شده است.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19395" target="_blank">📅 01:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19394">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گیِرْت وِلدِرْس، چهره راست‌گرای هلندی:
من آرزو می‌کنم که در اروپا افراد بیشتری مانند بنیامین نتانیاهو وجود می داشتند!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19394" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19393">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">موج جدید پرتاب موشک ها از ایران</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19393" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19392">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شلیک موشک از ایران به سمت اهداف نامشخص!  (اوکراین؟!)</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19392" target="_blank">📅 01:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19391">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شلیک موشک از ایران به سمت اهداف نامشخص!
(اوکراین؟!)</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19391" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19390">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خبرگزاری نایا : موشکای ایرانی همسر دوم یه مرد اردنی را لو دادند!
یک خانم اردنی در جریان حمله موشکی به پایگاه موفق السلطی اردن، بعد از دیدن آلارم هشدار روی تلفن دومی که شوهرش در کمد پنهان کرده بود متوجه شد که  شوهرش از این گوشی برای ارتباط با همسر دومش استفاده می‌کرده است!
به این ترتیب، ماجرای زن دوم شوهر این خانم  کشف شده و اکنون وی درخواست طلاق داده است!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19390" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19389">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOfaSM_vDouN6JHRLsOhrjYvymTvyKXrTUkVpujaqmsrTmtIktQRc8vFxZHvdf_t204gBRYJu-bUIFzLy7cGblEA6MPqD854hE4pi_TXRDFuPpHqjOdPIy9zgvprVt_w0Q3PIdLVLsbQsiL2TJes1vCGFND81ywH-BLsHhNJoSNXAyYFCoNHhKYZXjg7G-M4ONsu3mg8PiRbml9mtKzp4hJxWUObDbumsr3FGrb88z-PK23q2C9O3a_ajp0kMwG1VlR8H4_lT-WIgsbb3yBtDk1UnTYex0tciz-AK932QJbsrIOPJSoKJSez5HiIKyP6iDtlDbPZr-Gb4aas0HIwAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست:  برخی از حاکمان خلیج فارس به صورت پنهانی به ایران پول می‌دهند تا در آرامش زندگی کنند. برخی دیگر در حال عمیق‌تر کردن پیوندهای دفاعی با کشورهایی مانند ترکیه و پیوندهای اقتصادی با چین هستند.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19389" target="_blank">📅 22:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19388">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxV92xr7K6wPcuqXIgwOSsoQGR28YrY5-6qLZaQZBG_uoehjX1Mp1SF_gqYQanq69sJmVuRArskDTtspthYe3MNf3dusPJTe8JQmHfwQtVrPwhTUh0VF14gta8Xrleds5m1QIQLzN2nqCMVca4AQx0y1KH832tg8LS4PWP_KHIlhq_Lg4z6CHajhCtTqtH7Tv2ArfG63FNvjHC0MLyLhtW_XjypRo3fW4ufWAWIjEzNFM80xbldAKaQtr55DHGEeqIQ53FzQhZAFwUT9v1Eusn5ocS7D5Y1bbxF9doBR6qqoxHhDMZLwf7M4SAMUUO8wwbup5gTVGpvEC0TXhkaPYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقت کنید که وزیرخارجه اوکراین هیچ عذرخواهی نکرده و یا وعده ای برای جبران خسارت نداده است.  تاکید کرده که هدف ما زدن روسهاست و هر کسی با روسها باشد خب هدف قرار می گیرد و جنگ روسها ضد ما غیرقانونی است و ...</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19388" target="_blank">📅 22:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19387">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وزیر امور خارجه اوکراین:  من با وزیر امور خارجه ایران برای یک گفتگوی صریح تماس گرفتم. دیپلماسی به معنای گفتگوی مستقیم است، حتی زمانی که این گفتگو دشوار باشد. من تاکید کردم که هدف ما اجتناب از تشدید غیرضروری است.  من بار دیگر تاکید کردم که تمام اقدامات اوکراین…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19387" target="_blank">📅 22:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19386">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وزیر امور خارجه اوکراین:  تهدیدهای ایران بی‌دلیل و بی‌اساس است. رژیم تهران یک همدست مستقیم در تهاجم روسیه به اوکراین است که با سلاح‌هایی که از سال ۲۰۲۲ جان اوکراینی‌ها را گرفته‌اند، جنگ جنایتکارانه مسکو را دامن می‌زند.  ایران هیچ جایگاهی برای ادعای قربانی…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19386" target="_blank">📅 22:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19385">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/19385" target="_blank">📅 22:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19384">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">غریب‌آبادی، معاون حقوقی وزارت خارجه:   هر کس فکر می‌کند که می‌تواند، بالای ۵۰ میلیارد دلار از تنگه هرمز درآمد داشته باشد، کنترات می‌دهیم برود کسب درآمد کند و نصفش برای خودش و نصفش برای جمهوری اسلامی ایران</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/19384" target="_blank">📅 22:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19383">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">غریب‌آبادی:   پیشنهاد شده با عمان در مورد یک مسیر موقت در تنگۀ هرمز مذاکره شود و اگر تفاهم شد، جایگزین مسیر شمال و جنوب در تنگه شود    عمانی‌ها گفتند مسیری را طراحی کنیم که ۵۰ درصد آن در اختیار ایران باشد و ۵۰ درصد آن در اختیار عمان. ما گفتیم این موضوع رفع‌کنندۀ…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19383" target="_blank">📅 22:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19382">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH6DYdafiDwWQ2f2mmNzQr3uyFTvTdLWQEEyDhS-kwsX6vF9rVznEKF1LtuKrwFuTvuV6C2btCp3o0DP9HB17Y80MlSFd5KCabeq9S1d-M_OmQCwyjkyEuQMlegtnwupuxWVdXbZIPbY7HahWQmrY0R0W8gH_vhSoSZ8tZFtNdoIaNhipbO7mt9OYEb4fxRroQKbj-LKm4FcMWEfbcD8mIVsf8Q4MvhKoIqEk5Vz6eA3_mq-Qw1a40RYHjAwAVV63ybVS7u1153bjteBU0jTv3s8nwlojZRH15DM4SDzKKZAGb61Vak7OGHG1XOF4YvNakKipS_5Rwy4N_51_rZJRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/19382" target="_blank">📅 22:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19381">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c8b5e1cc.mp4?token=gfvX-MWLTFTrfnvUfZL8xbpbnZ51lbJ-as9XMfC1tMD3SwETUBCip22mT6oOD32OFkTpz4C8QcLt_5cZlV6uI0s8nYa0j_RDBoP15cn6qspuBQ5cRgAYwVLOV4yBRd8OMdVnQSHCoHMDhGdbiOQBD20sTUPreMVnWwwTHnEFoFqbcbB18bHag58v7fwaRNV47hJT8OQtw8wriVwq5S0H5lpcR_8K2K24H66pmWrSMDK-2--UZhW_BOUwjMfbw7hPN6lj6805bw3HdbC7PpfGYilgd6CnWLn_Oi6peXObpEw6LvPtNQPE7zDL-7bgIcgCPt_aaYskvFMbh1ws4FAuoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c8b5e1cc.mp4?token=gfvX-MWLTFTrfnvUfZL8xbpbnZ51lbJ-as9XMfC1tMD3SwETUBCip22mT6oOD32OFkTpz4C8QcLt_5cZlV6uI0s8nYa0j_RDBoP15cn6qspuBQ5cRgAYwVLOV4yBRd8OMdVnQSHCoHMDhGdbiOQBD20sTUPreMVnWwwTHnEFoFqbcbB18bHag58v7fwaRNV47hJT8OQtw8wriVwq5S0H5lpcR_8K2K24H66pmWrSMDK-2--UZhW_BOUwjMfbw7hPN6lj6805bw3HdbC7PpfGYilgd6CnWLn_Oi6peXObpEw6LvPtNQPE7zDL-7bgIcgCPt_aaYskvFMbh1ws4FAuoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره لیندسی گراهام:
به نظر من، من می‌دانم او کجا قرار دارد، و فکر می‌کنم او آن بالاست و به نظر من، او ما را زیر نظر دارد. من تقریباً از این موضوع مطمئنم.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/19381" target="_blank">📅 22:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19380">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8c4c6d69b.mp4?token=F5CgNr14HR0mUg8Bx7vcZ5tyoYEpZEdRC9wpZeAUdT4-mJEKxmC3pNXwFLb_QGoqzc9ixoYk0Xi9iFduoQ61OkPZJz8oTKSF9by0fZgD3WEjEtZTdwHC9AvFTh9aLcE0uIcvB4bWcIEZkwH0NumPhybzgLrLDFgWIq1TyAGm3DevD9lXI4nbGn-ZtbKY-uMgeXSAppUJIrcBSAm40lijCz32D5u_AuJ1_MIyvmKRIf-J2PcGx4UhtJn_e3gM022NtXjOkymF1fRUCMSu-urwH946XUrM66bVmO_DTu6iPPP-4q2BRHwFm76HA13MrMatUchMgUCIL7ON5pQWlwZtvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8c4c6d69b.mp4?token=F5CgNr14HR0mUg8Bx7vcZ5tyoYEpZEdRC9wpZeAUdT4-mJEKxmC3pNXwFLb_QGoqzc9ixoYk0Xi9iFduoQ61OkPZJz8oTKSF9by0fZgD3WEjEtZTdwHC9AvFTh9aLcE0uIcvB4bWcIEZkwH0NumPhybzgLrLDFgWIq1TyAGm3DevD9lXI4nbGn-ZtbKY-uMgeXSAppUJIrcBSAm40lijCz32D5u_AuJ1_MIyvmKRIf-J2PcGx4UhtJn_e3gM022NtXjOkymF1fRUCMSu-urwH946XUrM66bVmO_DTu6iPPP-4q2BRHwFm76HA13MrMatUchMgUCIL7ON5pQWlwZtvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینیم مصاحبه این 3 چه نکات تازه ای در بردارد.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/19380" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19379">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1_94JdJD5-b81C-f2nQCEEw-Oe6XA_RPbnteVuh3oxCb2ZT81GofO8NgOJMTshkGZF9jHwnbN6X5H3ZR7T5mlPNXruc_dUeOOJVI778sO_bKNp4SmelLTFLbM6sxQnW1jTe3LEqpr1WbmbhS7TRw6KRuCedpc-PWXlX3UcQE-Uc7cTPIHbiBLRskjmf0S_vbD141f1BwRLsBTMwu0qGIdmUPxTc8V-vSOUA-lYLK8rW-PmCFzE_ZDcZkuqpbU-zXGOOCkt1ecqjL9kD0mGPtlZNh8A8ldbKeOz1AVUhMSGEFH-T9rFO98keisj3c9jXbshDlA-kRV37w6FwHbm6VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز سطح شاخص ریسک ژئوپولیتیک افت محسوسی داشته و پیش بینی می شود که رشد خوبی در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/19379" target="_blank">📅 22:03 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

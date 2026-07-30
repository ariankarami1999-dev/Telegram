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
<p>@SBoxxx • 👥 10.5K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 16:59:30</div>
<hr>

<div class="tg-post" id="msg-19481">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سپاه پاسداران: ایران پایگاه هوایی الازرق را در پاسخ به حمله آمریکا به قشم، با نابودی سه فروند اف-۳۵ حمله کرد
سپاه پاسداران انقلاب اسلامی حمله موشکی انتقام‌جویانه به پایگاه هوایی العزرق در اردن را پس از حمله آمریکا به خانه‌های مسکونی در جزیره قشم اعلام کرد.
طبق بیانیه سپاه، این حمله به منطقه استقرار و محل نگهداری اف-۳۵ هدف قرار گرفت و سه فروند از هواپیماهای اف-۳۵ را نابود کرد و سه فروند دیگر را به شدت آسیب رساند. چندین افسر آمریکایی و پرسنل فنی نیز کشته شدند.
سپاه گفت که این عملیات در پاسخ به حمله آمریکا به قشم انجام شد که منجر به زخمی شدن اعضای یک خانواده محلی، از جمله کودکان، شد.
در این بیانیه همچنین از اردنی‌هایی که با حضور نظامی آمریکا در کشورشان مخالف هستند، تشکر شد و گفته شد که موضع آن‌ها فشار بر نیروهای آمریکایی را افزایش داده است.
سپاه در پایان با تأکید بر ادامه عملیات علیه حضور نظامی آمریکا در منطقه، بیانیه خود را به پایان رساند.</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SBoxxx/19481" target="_blank">📅 14:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19480">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کشته شدن ۳ عضو سپاه پاسداران در حمله آمریکا به زنجان</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/19480" target="_blank">📅 14:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19479">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 15</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19479" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 15
پنجشنبه 30 جولای 2026</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SBoxxx/19479" target="_blank">📅 13:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19478">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwGbeCxKraa7e6UQHIKbMxCVdjY4zzq78jptdzcBlwsAvb3GlmpQVT4CDTJYBO6vu_F6ut_5DLjiOWTq3cTK6qAA-bidDzB7I7FJVg_Q4BfACPRWnfyrAEo8pKT70avytZIaByVvWd6CPd85aQqS5yuqiFLA4hAJUdwS_kCk4tSxQtqqCIFycwMXjICBoSw-GjhHh4kDBAB2JvkxswDTJpLK0NMR-uy4SkM-eYcnMjXELtGPO1KtIrhhDiniP9SXTmUidiP-Jj1ItfMUmKhHcbe4QBloaB1XUSJDHZv1cFlJEyz4RfNY-51uZZ2Y8OY6P-JesNe71dSnO5F5EkGbaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لینک نشست دیروز با نیما</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/19478" target="_blank">📅 12:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19477">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8eacd406a.mp4?token=Nbtts1XfrD729VJ5ywGwa-b4j_5GKPfDyr1ZzXzlna7y6M16T_54G1pwbmmGkQuYRfsaSG759yk_SmfpFlOF2eBaG9pnrKzKVpXUWLQ3-GgsOYpoWqaUnKzeLNueg6ZsZOVHljZN5K-ZexZWIWdb2stQhmV6Mmc0jOxQk8clVmQYR7lyVB4USODYoxfSHkrHxiwFp-ZTAQhFAThkAwFgnzdy5uif8LC9TD74mdPl4y_GhFmC_1beIXW15bYJg_Ff-0zz4zJZdFgjFlwkzw38ZSStrjVBz8GJEkMy0WjgVNJ8EiJIHZ5O0nwaXTrmed-Ne6i4geCSfFFl93-Ea0rtRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8eacd406a.mp4?token=Nbtts1XfrD729VJ5ywGwa-b4j_5GKPfDyr1ZzXzlna7y6M16T_54G1pwbmmGkQuYRfsaSG759yk_SmfpFlOF2eBaG9pnrKzKVpXUWLQ3-GgsOYpoWqaUnKzeLNueg6ZsZOVHljZN5K-ZexZWIWdb2stQhmV6Mmc0jOxQk8clVmQYR7lyVB4USODYoxfSHkrHxiwFp-ZTAQhFAThkAwFgnzdy5uif8LC9TD74mdPl4y_GhFmC_1beIXW15bYJg_Ff-0zz4zJZdFgjFlwkzw38ZSStrjVBz8GJEkMy0WjgVNJ8EiJIHZ5O0nwaXTrmed-Ne6i4geCSfFFl93-Ea0rtRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبور موشک های زمین به زمین اتکمز آمریکایی بر فراز شهروندان کویتی به سمت شهرهای خوزستان</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/19477" target="_blank">📅 11:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19476">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0Z0PbuiMZnDtwcurh6V-gJZ_jwItul-H4CWMmTmuMnIGSum8UGJd9bBVVlq-putJC7km0XsuI3c4ttQCBe8iYSiQuYXOdnkVM7_TJLcDayQ36UC39zumkYYMUBi2ALxdsl6EcaIAa4PJJjqs_YRp2HbD0bBT2FBPvjr7jIhQT96I1IqcS7iVwKGHNRKYJsoc20zWGanLJwiO6l0uowrFrU9QGZ0cE34kr6c1XLzqnvdZKoCf8nevvoV6hOFiRVSNYiTfqCBWhv_WycDRrGKP2AOBlL_CahYhIDrG1YFUgOUPHcLDIkjkJVYsk9l8yx-6xrADSDsbdvYSIa9l2hgNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این همان حرامزاده ای است که دختران را در لایوهای خودش کتک می زد و به آنها اهانت می کرد که خوشبختانه به این روز افتاده و تا مدتها نخواهدتوانست شرارت کند.</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/19476" target="_blank">📅 11:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19475">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/19475" target="_blank">📅 11:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19474">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-xVlZ6l2gic-d18GpJzLZeMUUWNZMhW53sft70QSRi65iFDH-VM8gc-H9a6ZkBsGDI8p51yUuKjoiTx0hJNNrHyiumNXbb7cSkAP92rFNShBlfNZuVxfef-c0IEVQya5TrA_WLe3ffLjkwhgqQwawtiQrN0PMTww18e2mnico_7KeODsusBPDeIe2DHWj1ZtUXBfI55rL7d64aiVcUbDQmmFJV6w9pn4mRAsjzjLo2Cr_rVXkwKoPUd-Ms-fk-b8QWfW_g46KBwGyvtFzAmAefVsHK52giVvch1JY5raCBZOgD-Uh3xUGsH9gOJPVyMO76y4D4xNBsfLNZq-lvj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهداف حمله پریشب حمله مشترک سعودی و آمریکا به پایگاه های حشدالشعبی در عراق</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/19474" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19473">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سپاه پاسداران:
با استعانت از خدای متعال، متجاوز همین امروز تنبیه خواهد شد.</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/19473" target="_blank">📅 11:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19472">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlfMYU26OzEbA52DTw3pz7wOXh6Z2Ao48livi20psETVy7SbgelcGL6QRNJOpiaHn0CDPOIKSJCDPLYG9MoHCkPme7fTtL_1jyY2hQ3nXItNZzB3cFSPcrzCEqzNpv20MAmZebzyn-3N82p4QHlBd2kNXOhsvOq7wvsdeF7nQaxbwYBL8ijrLDLt_LKW623aTX758yag3AsbP-BNKxoLSVQHGmQVhXptX71Z3CvsiEhidQ2CIb004QqpMZ0ffmeOWVVpRM6xuMfQ35bfm0U7Jc9eiaeL89tAXI0OQn8vS8T29sj01lQoWbhQeQeLLU4-dkZlFh8JALGgC7cTnFtMHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح میانه پایین است و حالت رنج برای طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/19472" target="_blank">📅 11:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19471">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">این تحلیل درست 4 روز پس از پایان جنگ 40-روزه ارائه شد و همچنان بر اعتبار آن افزوده می شود و خواهیم دید روزی می رسد که تنگه هرمز را فقط خودمان استفاده خواهیم کرد.  از همه کریدورها که محروم ماندیم و سهممان .... های باقر شد این هم از تنگه هرمز!</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/19471" target="_blank">📅 10:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19470">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پرسش: اوایل این ماه، رئیس‌جمهور ترامپ در مصاحبه‌ای با یک خبرنگار گفت که در رابطه با شما، همه می‌دانند که چه کسی رئیس است، یعنی خودش. او کسی است که تصمیم‌گیری‌ها را انجام می‌دهد. آیا شما هم این‌طور فکر می‌کنید؟
نتانیاهو: خب، شما می‌دانید که در آمریکا اغلب می‌گویند ترامپ هر کاری را که من می‌گویم انجام می‌دهد. و در اسرائیل، اغلب می‌گویند من هر کاری را که او می‌گوید انجام می‌دهم.
و گاهی اوقات، این مسائل توسط هر کسی، از جمله رئیس‌جمهور، در بحث‌های عمومی مطرح می‌شوند. اما حقیقت این است که ما شرکا هستیم. ما متحد هستیم.
او شریک ارشد است. این کشور ایالات متحده آمریکا است. بیایید این را فراموش نکنیم. و من شریک فرعی هستم، اما من نخست‌وزیر اسرائیل هستم.
و وقتی لازم باشد، من برای دفاع از منافع کشورم و امنیت کشورم، این کار را انجام می‌دهم.
منبع: خبرگزاری ABC News</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/19470" target="_blank">📅 10:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19469">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نتانیاهو:
ترامپ اساساً سه گزینه پیش رو دارد: اول، دستیابی به یک توافق؛ دوم، ادامه محاصره؛ سوم، اقدام نظامی.
هر چیزی که منجر به پایان برنامه هسته‌ای ایران شود، چیزی است که ما می‌خواهیم. این هدف مشترک ماست.
س: وقتی با ترامپ در کاخ سفید ملاقات کردید، آیا تلاش کردید او را متقاعد کنید تا حملات به ایران را از سر بگیرد؟
نتانیاهو: در واقع نه. این یک تصویر کاریکاتوری یا تصویری اغراق‌آمیز است. این درست نیست.
ما در واقع تمام سه احتمال را بررسی کردیم، و من فکر می‌کنم که این کار را به صورت شفاف و در بین دوستان و متحدان انجام دادیم.
و این تصمیم اوست. این تصمیم اوست.
منبع: خبرگزاری ABC News</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/19469" target="_blank">📅 10:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19468">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شب گذشته یک منزل مسکونی در قشم مورد اصابت پرتابه آمریکایی ها قرار گرفت  احمد نفیسی معاون استانداری هرمزگان از حمله دشمن به یک منزل مسکونی در محله چاه‌تنگو شهر قشم خبر داد و گفت: تیم‌های امدادی در حال جست‌وجو برای یافتن دو یا سه فرد محبوس‌ در زیر آوار هستند.…</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/19468" target="_blank">📅 09:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19467">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فیلم سنتکام از هدف قرار دادن اهداف در حمله بامداد
چند پرتابگر متحرک نیز دیده می شوند</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/19467" target="_blank">📅 09:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19466">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حمله موشکی ایران به اردن</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/19466" target="_blank">📅 09:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19465">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شب گذشته یک منزل مسکونی در قشم مورد اصابت پرتابه آمریکایی ها قرار گرفت
احمد نفیسی معاون استانداری هرمزگان از حمله دشمن به یک منزل مسکونی در محله چاه‌تنگو شهر قشم خبر داد و گفت: تیم‌های امدادی در حال جست‌وجو برای یافتن دو یا سه فرد محبوس‌ در زیر آوار هستند.
احمد نفیسی خاطرنشان کرد: جزئیات تکمیلی این حادثه و وضعیت افراد گرفتار، پس از پایان عملیات امدادی و ارزیابی‌های میدانی اطلاع‌رسانی خواهد شد./ایرنا</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/19465" target="_blank">📅 09:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19464">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/19464" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19463">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19463" target="_blank">📅 09:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19462">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حمله به آبادان</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19462" target="_blank">📅 03:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19461">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAgh_vtRdM5dWQCZ_1LghWdFzJIYqdzLC-3LxN0E9nhEt2CcsbGp4nmoZIVP4T0jUFUS0hld0mt6qcuC1J7UQdjjattuoCtz56pUD3s7uCRo29vT8Bk5PmsHVIJM3mp41sss0PWOrG7E-gmt9E4emlPao_rPnvRRYI3V9mtfiOO8XhdcAsXhAoFBFQnYzCFZrJUNb5O5Adk5FFTOJo-bosiyEz5IWkn3mdycN2vBRtAOVx-e5elZEfHf5u1sUMtev7Iq4DiE7DuXl0JfHNEY_J_FqF_dCSZGwu5Qy1BSFjC4zWOH2ZhyV9xuJJ_uutpnlhbE67Re1BA6K9Og12tRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات آمریکا تایید شد</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19461" target="_blank">📅 02:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19460">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">چندین انفجار در ریاض، عربستان سعودی، و بسته‌شدن باند فرودگاه پادشاه خالد در ریاض.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19460" target="_blank">📅 01:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19459">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجار در اردبیل و ارومیه (تایید نشده)</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19459" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19458">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AW6o4j3r_muLvi80oWoAXtRXCRyJggZYqkfrGpdZPRIhZ9aR459xtH2aP0cuSDwicGFQmwgDLyHuvApNtW525SjH2U_DdBv43KudAAxvAPkeNAQqstQa-V8hqme9_Oz1I6laY2u5A-m66J1c_tZVh5Z0qZpPnmleeIqMSPFL3WuLm05OCJZ6600WY1KhpaGGJOek527jXokdqWtKh9dCXcEfElHtomH5VADz8tEmRHzFLG5H_QBtyNhI-q1I1vLdcddF-ZS_XrwuZNI6KTKfPY1l56ZSynElbhYG6OWkEouoT9C2BH7s-g4sdBCjyUDeA00OXx3bqKEb1OczvVN_rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا که اخیراً محبوب حضرات شده بود و چهره یامال را روی موشک ها میزدند، اعدام های اخیر در ایران را محکوم کرده و خواستار تعویق اعدام های برنامه ریزی شده شد.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19458" target="_blank">📅 00:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19457">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-RlHsjJWfyhvhhmVN9a2u7l8SNN0W6G8njJPTqrokEerdgKUmGTr8vWbGiffpWn17hBUYq7N_yh_uIFF2_haEh9jSJv0_GBIFpGBr5JaZH-3uxO28MjqsCiPYaAqIseyUP1t8UROU29Og2MMWnT99J3Dk3F8rbX_ZlZ_7pJaiYxLvnCHW3TImHlwlu6j1IVzxXPJ5S7zQ74qoww_KGdxRAoJgG9FFdgJNhXh-BXiCBDg4M6Pnkl8PmAaTpSmClhQijGuiRsXajUajcRP-51scJ_p6MuSPQzYiSr8vCieKKCbjjCqo7ayIfSP0NiUUVfO9hBUSvN8HsLT7Mt3k2oZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا که اخیراً محبوب حضرات شده بود و چهره یامال را روی موشک ها میزدند، اعدام های اخیر در ایران را محکوم کرده و خواستار تعویق اعدام های برنامه ریزی شده شد.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19457" target="_blank">📅 00:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19456">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0kqDnNtSHu_NzS5IbhuSs0BeKMAr3Xv7IyMR7gjvztC_TZwTIgEUIB3t21JIwIeUl1nYFHp1CdGw042zW7N6-sVqLuesriDOAJxVulwLYbicc4f0I2-fW5Qjh1wokQSwqC33lNu2MF8EYI05zVPwZHf8D_yBCJK0NXqPbBHDnM0mhS7M-lrapP_spSgC8b-ycASfQbWmEUReLWVnyepqXTT2YScUgrVL0TOzVFHK_WHUUG6HierW8RsUpDYUF19FWw_fdWlujgfuoyoxf6_i_h8RQ-dYelxYCWF0mmcPzZXrugi_KjmFHA7PTTu7bIw8DYccsaGGk2XMrnLgDTuYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیدوارم آن یک هواپیمایی که نزدیک تهران است جنگنده نیروی هوایی ما باشد.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19456" target="_blank">📅 00:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19455">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر
به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19455" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19454">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBrstxn-eElGvWzzVZJB7gAG-dppWmoaBcleH9vMsWdsNf4L37W8HriPcOQIg2T03m4YXXlKt8B3K5l8tLfPhNUMwPY0_HYwrKIx_EV-fRZvQmHdFOYe6IaSTlF6eyumFKAPMHf_2GMd2EkRtE01DZrnaoVcBf9k_6KdbFUzFuY_ms0o7GbYGc2yOjkivgmijvuP4pReht2tdyzqkoA5uHEnI7A0L1ASeUqz9dUR61V2dZT77RX1w2Em7hqCKRCEscO94bHncQXbHsVwSDgIPR-ldTYxrKDwGpGqa8oGClzXK-KFLF8VCKOkiaIVf2wLvtK4sU3DBawm8WY3zbZNCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز هم در وضعیت مناسبی قرار دارد و انتظار رشد طلا می رود.  دقت کنید که امشب نشست سرنوشت ساز FOMC را هم داریم که سناریوهای موجود در این یادداشت بررسی شده است.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19454" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19453">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3185a6e49f.mp4?token=inGxCzjA4obejWYgiOqUOGn0I3yczaf9nTzENA-6qqTJ4i8yLuw6O8LPRytPpQektCM8RWz1brMU-P_MFLDpOQGjHfuy0VL-X1NT09BLitDR-vo4PUzB7DHl8qYSSNvjtDtutj4mEv1OQzB0e0TzNaw243AZIv_vtvX0mpvzxhOwOGXUCGe4bdY5RkXSNUjlphIpUv6JS8vxhFdK5EOfzrxqPfhH-Pk8fGJ6-gOaDR-gYJ3oFbR0kwdi2c8Arm97wxq_foFsVRXrfuoBVjvfSE2JTlgtesO2plregaGjc2mTK8tI4EPcwgEeoa53EfWrsvFdAqFq7UvvudWJI6x2Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3185a6e49f.mp4?token=inGxCzjA4obejWYgiOqUOGn0I3yczaf9nTzENA-6qqTJ4i8yLuw6O8LPRytPpQektCM8RWz1brMU-P_MFLDpOQGjHfuy0VL-X1NT09BLitDR-vo4PUzB7DHl8qYSSNvjtDtutj4mEv1OQzB0e0TzNaw243AZIv_vtvX0mpvzxhOwOGXUCGe4bdY5RkXSNUjlphIpUv6JS8vxhFdK5EOfzrxqPfhH-Pk8fGJ6-gOaDR-gYJ3oFbR0kwdi2c8Arm97wxq_foFsVRXrfuoBVjvfSE2JTlgtesO2plregaGjc2mTK8tI4EPcwgEeoa53EfWrsvFdAqFq7UvvudWJI6x2Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک غیرنظامی اردنی به طور تصادفی، فیوز انفجاری یک پهپاد انتحاری ایرانی مدل "شاهد" که سقوط کرده بود را هنگام بررسی آن، منفجر کرد.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19453" target="_blank">📅 00:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19452">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
ارتش اسرائیل آماده حمله سراسری و بزرگ به ایران است</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19452" target="_blank">📅 00:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19451">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش‌هایی از پرتاب موشک بالستیک از اطراف یزد در مرکز ایران</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19451" target="_blank">📅 00:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19450">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ درباره ایران:  آن‌ها می‌دانند که این اتفاق (حمله) در راه است. از ما می‌خواهند که این کار را نکنیم.  دیشب سعی کردند با ۵ موشک به ما شلیک کنند. ما همه آن‌ها را رهگیری کردیم.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19450" target="_blank">📅 23:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19449">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ:
آندی برنهام باید به مهاجرت اشاره کند زیرا این موضوع بریتانیا را نابود می‌کند.
آن‌ها از آفریقا، آمریکای جنوبی و بخش‌های مختلف آسیا می‌آیند و در حال حمله به اروپا هستند.
این یک حمله است و بریتانیا مظنون اصلی است.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19449" target="_blank">📅 23:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19448">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3zS9nr1NS4ecTEdph75CiQctYrdLH0DXlaK_wjMJwzpcaEBr28OJ0X1bus6cdOb0W8KeoYr8Jb5OapQ9aXbeN69lZwmx_H_NrSqgtIuNQ_MkltCDlGQC-C-onemzyiPT2GzjqvKDaAhG_G6YKzyqCCQlkSUYJqzdcAdvyy33scseTL_ChwOLqlzhnSk-95MlaBcacjkNj6-GLjAkt0eEUALJd76N74rBVPHP0dsdxXw3j9Ety673I52HX18TNDJWDj_idQs1dj5T45JV39pEJ4OwOHYaDo7ljXEdxujL7p2wJar94or6FZJNQDNZ9ByaPJ2k-l1XVUdL5MZ3ItD9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19448" target="_blank">📅 22:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19447">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها می‌دانند که این اتفاق (حمله) در راه است. از ما می‌خواهند که این کار را نکنیم.
دیشب سعی کردند با ۵ موشک به ما شلیک کنند. ما همه آن‌ها را رهگیری کردیم.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19447" target="_blank">📅 22:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19446">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ درباره ایران: آن‌ها را به شدت ضربه خواهیم زد، نوبت ماست.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19446" target="_blank">📅 22:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19445">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">علت رشد طلا در چند دقیقه اخیر:
مقامات امنیتی مصر به شبکه خبری "الحدث" اعلام کردند که هیچگونه حمله‌ای در بندر دمیاط رخ نداده است. آن‌ها مدعی هستند که این حادثه یک آتش‌سوزی بوده که در بخش موتور یک کشتی از رده خارج شده رخ داده است. - خبرگزاری "کان" اسرائیل.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19445" target="_blank">📅 20:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19444">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یک مقام ارشد از یکی از کشورهایی که در این میانجی‌گری نقش دارند: کسی که تصمیم‌گیری‌ها را انجام می‌دهد، فرمانده سپاه پاسداران انقلاب اسلامی است. - خبرگزاری کانال ۱۲ اسرائیل،</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19444" target="_blank">📅 20:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19443">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انفجارات در اردن!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19443" target="_blank">📅 20:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19442">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رئیس‌جمهور ترکیه، اردوغان:
دولت فعلی اسرائیل که تحت تاثیر جنگ قرار دارد، با تحریکات و اقدامات سازمان‌یافته خود، همچنان منطقه ما را به سمت بی‌ثباتی سوق می‌دهد.
اسرائیل با نادیده گرفتن حقوق اساسی بشر و زیر پا گذاشتن قوانین بین‌المللی، به تدریج و گام به گام، سرزمین‌های فلسطینی را اشغال می‌کند.
اشغالگری اسرائیل، سکونتگاه‌های غیرقانونی آن، و سیاست‌های آوارگی، ارعاب و سرکوب علیه فلسطینیان در کرانه باختری – همانطور که در غزه انجام داده است – منبع اصلی مشکلات در منطقه ما هستند.
هزینه این تجاوز نه تنها توسط برادران و خواهران فلسطینی ما، و نه تنها توسط مردم لبنان، بلکه توسط مردم با ادیان مختلف و کل منطقه پرداخت می‌شود.
به عنوان مثال، به دلیل درگیری‌ها در منطقه ما، عرضه جهانی نفت، یکی از بزرگترین شوک‌های تاریخ را تجربه می‌کند.
متاسفانه، این فقط نفت نیست. قیمت بسیاری از مواد اولیه کلیدی در بازارهای جهانی، از جمله گاز طبیعی، کودها، سوخت دیزل و محصولات پتروشیمی، نیز به سرعت افزایش یافته است.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19442" target="_blank">📅 20:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19441">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نتانیاهو:  من همین الان یک گفتگوی تلفنی با آقای پیتر هگست، وزیر دفاع، به پایان رساندم.  او نکته جالبی را با من در میان گذاشت. ایشان به من گفتند:   «ما به جهان نگاه می‌کنیم و کشورهایی وجود دارند که اراده مبارزه در کنار ایالات متحده را دارند، اما از توانایی…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19441" target="_blank">📅 20:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19440">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dfa1gNsUhKSUvHtHTKkTtMJC98DFgNlXu8mU5GTHZrses3qcdUlw0kQNMNI48bk97L7XBVi-GwHp64PSy2zw_Tuc0C8-7fwhPA_uKadcCxZzKWByIJ9BiAOiXUZEilHtsUylrd589tUwOI2vpSPxOXrvwmCo0RV-3HUrXWwR9FOVwW1ez2Ay2z2h5Sy857tYiDKb9x-bBr9dReMJw8puWmSgq2ETvov1vKzmmmJlv7ivOjHVgc2qq9JRSZ-UD4VcdnyAf7yS75eTZc6UHI55-owI5MKKACSUnfkxeDvf3OuSWZfuSKWm5QQMVcYAqiWIYNbywHdz-eKbtPpZX4v2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:
من همین الان یک گفتگوی تلفنی با آقای پیتر هگست، وزیر دفاع، به پایان رساندم.
او نکته جالبی را با من در میان گذاشت. ایشان به من گفتند:
«ما به جهان نگاه می‌کنیم و کشورهایی وجود دارند که اراده مبارزه در کنار ایالات متحده را دارند، اما از توانایی لازم برخوردار نیستند. و کشورهایی وجود دارند که توانایی لازم را دارند، اما اراده لازم را ندارند اما فقط در اسرائیل است که ما هم اراده و هم توانایی را مشاهده می‌کنیم.»</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19440" target="_blank">📅 20:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19439">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مقامات اسرائیلی می‌گویند نتانیاهو در جلسه روز سه‌شنبه با ترامپ در کاخ سفید، نقشه‌هایی را ارائه کرد که میزان نفوذ اسرائیل و ترکیه را در سوریه مقایسه می‌کرد.
بر اساس اطلاعات ارائه شده، اسرائیل حدود 0.1 درصد از خاک سوریه را تحت کنترل دارد، در حالی که ترکیه حدود 5 درصد را کنترل می‌کند.
نتانیاهو از این تصاویر برای مقابله با فشارهای قبلی آمریکا استفاده کرد، از جمله تماس تلفنی ترامپ در اواسط ماه جولای که از اسرائیل خواست نیروهای خود را از سوریه و لبنان خارج کند.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19439" target="_blank">📅 19:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19438">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19438" target="_blank">📅 19:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19437">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یک مجتمع شناور ذخیره‌سازی گاز طبیعی مایع (LNG) متعلق به یک شرکت آمریکایی و دارای پرچم جزایر مارشال، در شهر دمیاط، مصر، مورد حمله حداقل یک پهپاد قرار گرفت.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19437" target="_blank">📅 19:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19436">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یک مجتمع شناور ذخیره‌سازی گاز طبیعی مایع (LNG) متعلق به یک شرکت آمریکایی و دارای پرچم جزایر مارشال، در شهر دمیاط، مصر، مورد حمله حداقل یک پهپاد قرار گرفت.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19436" target="_blank">📅 19:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19435">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به خبرنگاران گفت:
«ایران در حال حاضر تقریباً ۱۵۰۰ موشک بالستیک در اختیار دارد.»</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19435" target="_blank">📅 19:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19434">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مقاومت اسلامی عراق با محکوم‌کردن حمله آمریکا به حشدالشعبی در کربلا، به دولت عراق تا ۲۳ صفر مهلت داد تا توانایی خود را در دفاع از کشور نشان دهد.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19434" target="_blank">📅 18:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19433">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مقاومت اسلامی عراق اعلام کرد که انتقام خود را از حملات اخیر ایالات متحده تا پس از مراسم اربعین به تأخیر می‌اندازد تا امنیت میلیون‌ها زائر مختل نشود.   این گروه هشدار داد که حملات علیه نیروهای ایالات متحده اجتناب‌ناپذیر است و گفت که در صورت لزوم عربستان سعودی…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19433" target="_blank">📅 18:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19432">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مقاومت اسلامی عراق اعلام کرد که انتقام خود را از حملات اخیر ایالات متحده تا پس از مراسم اربعین به تأخیر می‌اندازد تا امنیت میلیون‌ها زائر مختل نشود.
این گروه هشدار داد که حملات علیه نیروهای ایالات متحده اجتناب‌ناپذیر است و گفت که در صورت لزوم عربستان سعودی نیز می‌تواند هدف قرار گیرد.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19432" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19431">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رسانه‌های ایرانی گزارش دادند که 4 عضو سپاه پاسداران از کاشان در حملات مشترک آمریکا و عربستان سعودی که در طول شب به سایت‌های حشد الشعبی در عراق اصابت کرد، کشته شدند.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19431" target="_blank">📅 17:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19430">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نتنياهو امروز با پیت هگست، وزیر دفاع ایالات متحده، دیدار خواهد کرد.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19430" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19429">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حمله موشکی ایران به اردن</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19429" target="_blank">📅 17:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19428">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erxAYqcfPaj_hCd7omDQ_gpLLJH_FDlArxQCz0YlS8fatSn9Oo3rAIRB2XTnB8nbzmgVekBPoLfTEJfMO14FvHjSk4DP8tSkVbQSKjPDtMP7fH5fXboMmsdtfOT3mnKbxGTNom8g0Vk_q5nV5hDO_-17GxI7XErtteRYzpFjrNEHWNKtsY_vmqmqI--niPlufPuIntqzxEnSxrKCTfgxBcl-9exjckqVAlUboJsGnwtZKFug6CtCrhR2aA5jXUaV86FCfHTmsK3tBgpSpLcG5Xk5Qq3AxkPo_J697fPVF3qO1i8nbeeKvCuFBcqaJjEvx7919EsSMvRIHUGsSh-_fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای وزارت خارجه در هدف قرار گرفتن مواکب زائران حسینی در حملات دیشب سعودی و آمریکا!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19428" target="_blank">📅 16:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19427">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19427" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19426">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19426" target="_blank">📅 16:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19425">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انتظار می‌رود که اسرائیل امروز به حزب‌الله پاسخ دهد، اما این پاسخ احتمالاً مناطق جنوبی بیروت را هدف قرار نخواهد داد.
— کانال 14 اسرائیل</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/19425" target="_blank">📅 16:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19424">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده:  «حمله دیروز ایران یک غافلگیری بود و نیروهای ما تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.»</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19424" target="_blank">📅 16:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19423">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده:
«حمله دیروز ایران یک غافلگیری بود و نیروهای ما تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.»</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19423" target="_blank">📅 16:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19422">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وزیر دفاع اسرائیل:  در دور آخر درگیری‌ ها جنگنده‌ها و سوخت‌رسان‌های آمریکایی از اسرائیل پرواز می کردند اما ایران همه را زد جز ما</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19422" target="_blank">📅 14:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19421">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پرتابه دشمن به استان آذربایجان غربی برخورد کرد - فارس</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19421" target="_blank">📅 14:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19420">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مطمئنم امین سهامداره  @Piknikanalyst</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19420" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19419">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pSG7tY9cWPSzHjM_puoC3BqYmzXP6UotDI9BhL18EK2XNfruRilNfTILUyIjeFkpwQ-YObSfzrijztJBmGsq0Lph5YZRIuMsFiDn2OhQmsn8amKe-srkLxEzJlwMF2vxfHH_RG41IQxfFrGsCWPe1IAEt30qPmDL5tnyvb6mBZJD7k-LxDWKUUoiAqIH62vTjwGQhQ0PG5upMM7OtXF0Y8fSmUYTRVs28nlY_oqlZm_oR9iuByswz9xR8PPNOBFuTdJmvJSZjVJXfctBHmCcDPlZnwaleXhz3hqcueonngd3m9ElBtugtwxq3J-Ib5l_FHR05uatDuTVZTM7VLK3vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطمئنم امین سهامداره
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/19419" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19418">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نیروی هوایی ایران اعلام کرد که جسد سرتیپ مجید کاظمی، خلبان جنگنده بمب‌افکن سوخو-24MK که در تاریخ 2 مارس توسط جنگنده‌های F-15QA نیروی هوایی قطر سرنگون شد، پیدا شده است و طی چند ساعت به کشور بازگردانده خواهد شد.  نیروی هوایی ایران همچنین افزود که مقامات همچنان…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19418" target="_blank">📅 11:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19417">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqtS0mX7shv7AEA8hkqGRz2n-xGnuUr0NdzxR4lXODJR3bVp9lfvVYSE2YoqHP5jbyx-HP89Lfll-Y2CP-YgtC4n8Qguk46jcaeqCjaMHCWz00e9BYlTbdRROw9JnpX97kEFY306PZMkkot3RTyRhjEPRQ0FhR4JencfdYWNwC6mcAUpcJ11xGInXlWgaWJGJYGRgTgi22b8CIFe0U2Yj7gFq7swBuv9NEQ7_UiyB0cz1F-_P0oYR8BDJTPhXJ-WLEZfTqHSqwvTGcHx-SdFfYlNtrkc7StCzt9f3vELjnnF2S5IoYP0JXBFwEP4ht16IOgKiuCrsOJQNbU9kpxAlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران تأیید کرد که تعدادی از ناوگان بمب افکن‌های سوخو-۲۴MK اش سرنگون شده‌اند.  این هواپیماها در حملاتی در عراق و سپس قطر شرکت کرده بودند اما سرنگون شدند.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19417" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19416">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a40b3b45d.mp4?token=LqOa6iBSiWN1rx75Nuw0xuOfL-LsJCWxOIPyJCaf9Hd-ikmUBUolrpenuKG8Ypre0VIl4MtLHxCijNSI4FSzkF9nXwGxIUJ0zvP92pMnBQNIQhpFN5rK5yaBQechLpjoUcvnq-fQCQPw6PMl0dBk8OpAlFbutslW82qdMyS0rcvZ1k06UpiRSKyn196wvzoaXBm9tfh5b0XostKaqF1i7OpeM-0XKT5ot7W7pVCF0OIc8h22E9UUTEftCJN6rEBapCZxPVJvo2Tgw9UkNj2eUJ-HeF1v1qMsn6NiU3uuo0_0b9UbnNLfqbT8Z45NU8dSPfgRpE1oUI-C6pTTCQlMDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a40b3b45d.mp4?token=LqOa6iBSiWN1rx75Nuw0xuOfL-LsJCWxOIPyJCaf9Hd-ikmUBUolrpenuKG8Ypre0VIl4MtLHxCijNSI4FSzkF9nXwGxIUJ0zvP92pMnBQNIQhpFN5rK5yaBQechLpjoUcvnq-fQCQPw6PMl0dBk8OpAlFbutslW82qdMyS0rcvZ1k06UpiRSKyn196wvzoaXBm9tfh5b0XostKaqF1i7OpeM-0XKT5ot7W7pVCF0OIc8h22E9UUTEftCJN6rEBapCZxPVJvo2Tgw9UkNj2eUJ-HeF1v1qMsn6NiU3uuo0_0b9UbnNLfqbT8Z45NU8dSPfgRpE1oUI-C6pTTCQlMDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمار تلفات حمله عربستان به حشدالشعبی  ۱۰ کشته از تیپ ۳۰ شَبک ۲ کشته از تیپ ۲۴ حشد الشعبی</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19416" target="_blank">📅 11:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19415">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBz4QYMtddYctPGKi1UdjoQGZSoUUMSCF9BRVIDgyYcl9qzBH9hjLaoNiSao1IP-0HyPFreGmRwhtYdW8B-mCAR5t4xllROF039-FEUgJqPjewxEyEAN1nQDaTULfJ8u3-zZHiFpJbDBqu0URCppq9bSK02tT2ODSwTgJhcuSsbzIbysV9Eu6UMtSDRRwhhqvzK1RaNDaIalZR_dn3LK_0QFAlx4x5mde7v8ugRinqmahmoOoEVEdSbwLKTIMfIcWCUrDlEQjApO9JCYHXoUYuLRtLbBpQiqibEVxxM5GYyt032kjqzkY2JWAMYGMn-tl5E7KkQe_XpAv0wCcNQz1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز هم در وضعیت مناسبی قرار دارد و انتظار رشد طلا می رود.
دقت کنید که امشب نشست سرنوشت ساز FOMC را هم داریم که سناریوهای موجود
در این یادداشت
بررسی شده است.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19415" target="_blank">📅 11:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19414">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خب مثل اینکه «درنظر داشته» حمله کند  ایران، پس از حمله اوکراین به یک کشتی ایرانی در دریای خزر، یک حمله نمادین با موشک‌های بالستیک به یک بندر اوکراینی در دریای سیاه را مد نظر قرار داد.  اما گفتگوی تلفنی بین وزرای امور خارجه ایران که در آن این حمله به عنوان…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19414" target="_blank">📅 10:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19413">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خب مثل اینکه «درنظر داشته» حمله کند  ایران، پس از حمله اوکراین به یک کشتی ایرانی در دریای خزر، یک حمله نمادین با موشک‌های بالستیک به یک بندر اوکراینی در دریای سیاه را مد نظر قرار داد.  اما گفتگوی تلفنی بین وزرای امور خارجه ایران که در آن این حمله به عنوان…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/19413" target="_blank">📅 10:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19412">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQ5v87afiWXbuDwYk2lxiCksHdmgtNBiFO9ORciPmiyvIjKioy-NbXKgM1jocqwts88yZzhtE4nFu6dICTOz1zdkj550H1VR9hc4j_7rJ9iPDQZr-pxoj5Yulciu3Q17SlN4idKgo__xRMb5P1hwfZgwaBWzlpIs6xYvXqH1NbYchE-S_m-Bu7y8UW0yIMwJqUgfS5CRV0r5jzk3ff-OksjqlXny8FF22IRqIewmCkhu-XKKXGd71pBiKXyuIPLerFr1svyszpNz-FF7bYkhDjMCcZ8kz_MqQe9r5SylfHHTs_GAsrj7iRFZAuvdU8--PBoeeTh8Oj1n8wEBolf08w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: ایران، یک حمله تلافی‌جویانه به یک بندر اوکراینی انجام داد.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19412" target="_blank">📅 10:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19411">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLzfR9FjWTKyUaCJ0EpJM-KhZYo9OtzIcJ1oFTFjqkkm7sBTYnMBT9m76_Rn4UCtmtyb3vTytkarTdzNLwpbY_Hbjnx_ghS5rbR0osufNN-6nng7XDYwa-GQ0mXSuPTJoSvjDIUnuYoK_mUWzcZ36pHpFY_pHUMJ8J-5iQJgFTxcb40poOsQzaRttEOEX-NffxIKSY_Bpv5Ueca1Twc5pQ7y-dH9SEEtRjwBH-HXxhy587X9C4FB9_if44MgcufHkFC1Nj8FVrEHj9CPivFc4utrgTPx_-xplEYsUb8r0t7g3VK5od3QBAmsgh7t2y6otLIsAxFFlb-A4fdIYdcfuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش‌ها، ایران قرار است در یک قرارداد به ارزش 60 تا 70 میلیون دلار، 300 تا 400 دستگاه موشک دوش‌پرتاب چینی (مدل‌های QW-12 و FN-16) دریافت کند. اولین محموله‌ها طی چند هفته آینده از طریق شهر اورومچی و از طریق پاکستان به ایران ارسال خواهند شد.
این قرارداد از طریق یک واسطه مستقر در هنگ‌کنگ به نام "Zhongqing Baoshang" انجام می‌شود.
چین و پاکستان این گزارش را رد کرده‌اند.
منبع: رویترز</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19411" target="_blank">📅 10:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19410">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4Ts8dFrlkbqumAVhl2rU_uN8oOg8uH6AU25vQ7yS9C2Qxwn2vUB0RGrRGSmIffFLSsuXQ-1WVQNcPo1g2Ii5Py_7Herg_uWFQFggHc7zveNcsPmM3TdSA_WKYFn-3HM3YwZsAQEYkviltYAACrm7vPcYMKR-dnM7dp2JcUabgKa-sk_0rI4KCqQvKpg1cWwjb1RgeoN-TdN6rIE-Q4I0PaHX9m6lVxbpicvTsTOMssyvApHd9vBRGpD6NSjLsWD6Op0_c70a_gTAZqX79VFD6DVHIOHJBDEUfn45E2ixNmT1oqfUdbokSPDnJvd4bGX12xXLC_qy80nztC2NWQBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: ایران، یک حمله تلافی‌جویانه به یک بندر اوکراینی انجام داد.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/19410" target="_blank">📅 10:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19409">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نیویورک تایمز: ایران، یک حمله تلافی‌جویانه به یک بندر اوکراینی انجام داد.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19409" target="_blank">📅 10:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19408">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حملات عربستان به عراق !  گویا نیروهای حشدالشعبی هدف قرار گرفته اند.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19408" target="_blank">📅 09:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19407">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oj_Yb6MEjihq8B4BFTh4gTUsHYmXG2V75ddfv055QD4Z62QPV_nLgSfKDwTitTzs5ZJQOOSnVbOajP1q7jyMYcebMfadrufrFQMzkSjA6HcfQ7UaZFY_eO20NeygOu9dTZ6cWmONNKGocCa-Qvh9KdVOyqoIG7DF45bBCqJcPIlognF8--SVUrOZs7bHqGvWkiKSAwUvgPZvYWDaYrjAoDDThMV5p-XZ0Spu3wiCodwti4ae2PD-oFSehDp-f6pWUHXFOoDElkMjliAL5wk7GLb8Z-FV6NL4DzGSeoAceh4Kq1Pu6jwFWc1-FlB24TKiGILLYSZR354JqzZbd4ELBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19407" target="_blank">📅 09:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19406">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">حملات عربستان به عراق !
گویا نیروهای حشدالشعبی هدف قرار گرفته اند.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19406" target="_blank">📅 03:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19405">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozfmGAtf6IqRcCge9rH4swUvQt89Pk3PaUGavNVLHhE7dJ6aa0k97ss0vtkHiIweO55gAY34HHohLLKt38Os7l4wiBmNI3wMsDbaIY_8C3Grm2DhzKxPRNdvV-hPBo75RoB_Cgqjp-gnmO6I3Be24tMk4Hsd0LQ8v9U_eY0g6af5nkDCrzTEt_Pky_8sP8yj4jApW0QdA_WzEIk-yPQoXp1Kaxuem_8iiJbSDhYuOWpBjraXpTlTUFpiQU_KZ3Yrcppe78T8yUnNObK87Gae5QUSiYXS_p6SXA7nG5oAzesskxyjED0CVFZoFuVfbtTex-jOHY980LNko-rFS_xfeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19405" target="_blank">📅 02:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19404">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhSavyeuJUpKlEghFT872ftdD4I7ZSLYKqaiZKZ8DlaUbbWK77X7YHHj3cyrOC-dTKkG7Ax5EWl_iIosRLjyh9wZpmmdC6OmmEhh8HmtuAJp7N97uJaamGPbq8CN8Ak9BI5HU0eI1fKGmczHTd1SCeD1Uy8goVZlxMBsMjptTVHnpTw86yt2WqOxqDCSSL1fQG2hutVfmATi2_0EWxg4up0SkDEoG1XG4gtLCE7Q7Anq8aHK5RN0egOAUhLiOlWX3Miz7nGmOkO1m-sTCIttvcte-Wivr4ib_D7Hp0QjOgKrqtCG2Obg1oK3XvU47VM9HO2qFtyySIbQ17exLQVkmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه جنگنده های ما پرواز نمی کنند و این یعنی احتمال حمله هوایی بالاست.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19404" target="_blank">📅 02:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19403">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzD_qAEGG4AuURouhOvKL8OQ0EeqRSepwIRtkMozjqjfnG-3kS2nomSmvHZgePZyKbs6jlormFyb_PZcjTg5y5pkQWVkmm2nFvH0XGGRoZo_LHUseLATzzGaXnHrmktSQgyLexo0lDqwytYe6jqKYhzmbn7Y54xMXNNcC9DZzg56xrdGsUM4TXAuhCYYVVN-eqL3bH8spFAjvPpU7mhxGxqtIoXSCdJLjTYReo8PvTCEmSKR7F12neUAYz0wxLlbmaDRKPIjsOVB4UgRt7nRsc8_hYdNExTXwawa9baKOTrnxc2Us7cKm19jZh9N5U_SMr0us4m2hmrVUdDlsxejvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلاً قیمت نفت بیش از 5% پرواز کرده</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19403" target="_blank">📅 02:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19402">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دیدید؟ همه گویا رهگیری شدند!</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19402" target="_blank">📅 01:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19401">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J51mTg48Ig0DY0hB06pSWaRwicpCzSVu0dX53XhBq7icbufKf9PrVEm9SjolpBDT_XRJgrMEod78ePmXsaCkLJkxVwa41W0UoA_T1VLjqp8_f1vCzmbgLv5hc7Atc4UP3uNGH4cB_BWRm_3AJEm4A4C4gizkSwDB3FpR97gKI_TbZxt5zFOHmcPB9mDIm-5-bXwfGZ7nKOn_2t-pl1OPlwW10UEEOAlz_1gYjb00N9LgNmkXQ2tdRZi9VG4xeRKAc9IDbqy4pew6jFO572NBC7g62y917dpWX38rxVtjj7M_E3H8-mrJrKo2XZSuuOQvt8o4fp_AQNJIfWw57L3Z-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدید؟ همه گویا رهگیری شدند!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19401" target="_blank">📅 01:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19400">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اگر هدف پایگاه الازرق باشد هیچ اتفاقی نمی افتد.  مگر اینکه یک پایگاه الاحمر نامی را بزنند تا در هم کوبیده شود.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19400" target="_blank">📅 01:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19399">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">صبح ها اعدام داریم، ظهرها قطع برق، شب ها جنگ!
بعد برخی آمده اند تولدم را به من تبریک گفته اند!
وا بدهید لطفاً.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19399" target="_blank">📅 01:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19398">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuXwJ3eBp8_2Sj-aM5zPcNIekPwCA9jaefheFcjJ2eNiYF6GbyQYkiEZsydy4XId0H5q7bzQDb0E-wQPwMZEbiBSRTnAioiJlYW-f_--qHKUvEvVzarqeKeWIGqMEg5OxVOQn3aQ0Dc5463xfUsz9Lx_fmFOJp0yE1zPYY0mJM-1ctncR5YRM33DiR2igLFZDH4rUnL1E40UhdBqyshQ25TrB7-8F9VBxNiV_uCjB57vXClkaSZM-5_Uk9cFgs5uwtXyCoykr54Wp8x1aHY11Os7Ot6592T0JcRqmAedKHNbNIy5I5ZuqHDj27F5VpQCHB22nRz9CXbOhP7BqgBzZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جا دارد دوباره گوش جان بسپاریم به آوای روح بخش بانو لورا برانیگن که زینت بخش این شبهای پرکت خواهرمیانه است.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19398" target="_blank">📅 01:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19397">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">جا دارد دوباره گوش جان بسپاریم به آوای روح بخش بانو لورا برانیگن که زینت بخش این شبهای پرکت خواهرمیانه است.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19397" target="_blank">📅 01:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19396">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مقصد گویا اردن است.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19396" target="_blank">📅 01:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19395">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">به نظر داریم وارد موج 2 از 5 می شویم و موج 1 از 5 تمام شده است.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19395" target="_blank">📅 01:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19394">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گیِرْت وِلدِرْس، چهره راست‌گرای هلندی:
من آرزو می‌کنم که در اروپا افراد بیشتری مانند بنیامین نتانیاهو وجود می داشتند!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19394" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19393">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">موج جدید پرتاب موشک ها از ایران</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19393" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19392">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شلیک موشک از ایران به سمت اهداف نامشخص!  (اوکراین؟!)</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19392" target="_blank">📅 01:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19391">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شلیک موشک از ایران به سمت اهداف نامشخص!
(اوکراین؟!)</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19391" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19390">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خبرگزاری نایا : موشکای ایرانی همسر دوم یه مرد اردنی را لو دادند!
یک خانم اردنی در جریان حمله موشکی به پایگاه موفق السلطی اردن، بعد از دیدن آلارم هشدار روی تلفن دومی که شوهرش در کمد پنهان کرده بود متوجه شد که  شوهرش از این گوشی برای ارتباط با همسر دومش استفاده می‌کرده است!
به این ترتیب، ماجرای زن دوم شوهر این خانم  کشف شده و اکنون وی درخواست طلاق داده است!</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19390" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19389">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBbSDVkXz8WEMr2chw6rfzu-yIUQedk1ZpYvTq7yjl6ASCeOjIwm6ucz-AIz_BC6vC8Rw4lOa6cDRq2VoQcHTPdUntbSTTuj_r5Hd7_mdFTq-3F-EU3ZPKRDndG0v6naX8JVe6PWVKXXIgiU8FeafUqmr_4kars3HszEwGytUGbVbRUjWWB7G6NHaMbpL8UUuzNBQHWXkJdvP2DJDxEkSrobblKnaCmhxc6rAS1I-EjDCPYQ5RYUdF28l4Gc7wpqpAaeu0nfFwJU6YywHuH8FJHRPenYAWyeYZwpfXgFCeGoKW3oXQyClGwXxQzRuZXu-1xZk62qNf7yytNPQUB7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست:  برخی از حاکمان خلیج فارس به صورت پنهانی به ایران پول می‌دهند تا در آرامش زندگی کنند. برخی دیگر در حال عمیق‌تر کردن پیوندهای دفاعی با کشورهایی مانند ترکیه و پیوندهای اقتصادی با چین هستند.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19389" target="_blank">📅 22:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19388">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGoUl4AmSwh_FP1zMnk9bGUdcg0WMEQC2rI6I3O71VdsaxU5qQE22v5R8DG0CWy9bKPF7cyNC2lQjE_5ZRq9Hf4lvVOyqpShpKbIcfAnO06vIIUKt1_2Bmwrf6lLY5_pNbL-zSyliid5f1U28ldqo9bte3ty9vw55lQWMxhXLEl4HzfgVx7jxOYBl9API42vmPXcQmPbdEAq_oZ1rxk5Q4cr7qunVBVJ3HdMgVhenhPqFJX-Ztaw8gHEaYKp7AaOwgmezjBJVuBldwu_zqOuf4mQhXjGzDA2ZvS9sLryesgpjjyV3dPu05cFF2jxn43FirhpcMYJVGQ1VTL8BeuSGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقت کنید که وزیرخارجه اوکراین هیچ عذرخواهی نکرده و یا وعده ای برای جبران خسارت نداده است.  تاکید کرده که هدف ما زدن روسهاست و هر کسی با روسها باشد خب هدف قرار می گیرد و جنگ روسها ضد ما غیرقانونی است و ...</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19388" target="_blank">📅 22:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19387">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزیر امور خارجه اوکراین:  من با وزیر امور خارجه ایران برای یک گفتگوی صریح تماس گرفتم. دیپلماسی به معنای گفتگوی مستقیم است، حتی زمانی که این گفتگو دشوار باشد. من تاکید کردم که هدف ما اجتناب از تشدید غیرضروری است.  من بار دیگر تاکید کردم که تمام اقدامات اوکراین…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19387" target="_blank">📅 22:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19386">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وزیر امور خارجه اوکراین:  تهدیدهای ایران بی‌دلیل و بی‌اساس است. رژیم تهران یک همدست مستقیم در تهاجم روسیه به اوکراین است که با سلاح‌هایی که از سال ۲۰۲۲ جان اوکراینی‌ها را گرفته‌اند، جنگ جنایتکارانه مسکو را دامن می‌زند.  ایران هیچ جایگاهی برای ادعای قربانی…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19386" target="_blank">📅 22:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19385">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/19385" target="_blank">📅 22:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19384">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">غریب‌آبادی، معاون حقوقی وزارت خارجه:   هر کس فکر می‌کند که می‌تواند، بالای ۵۰ میلیارد دلار از تنگه هرمز درآمد داشته باشد، کنترات می‌دهیم برود کسب درآمد کند و نصفش برای خودش و نصفش برای جمهوری اسلامی ایران</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/19384" target="_blank">📅 22:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19383">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">غریب‌آبادی:   پیشنهاد شده با عمان در مورد یک مسیر موقت در تنگۀ هرمز مذاکره شود و اگر تفاهم شد، جایگزین مسیر شمال و جنوب در تنگه شود    عمانی‌ها گفتند مسیری را طراحی کنیم که ۵۰ درصد آن در اختیار ایران باشد و ۵۰ درصد آن در اختیار عمان. ما گفتیم این موضوع رفع‌کنندۀ…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19383" target="_blank">📅 22:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19382">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuIVDgg73vNKZTWULUfci4sbQkqVw7becxFCtFkdyZEcJDFpz7F8_SobytwBSuJdJPhX3j26dnWR6YUlD17Xlta1C-K7sCKtIiWIzyh8KheYmfrwdqy6FIrJyc04dCPw1T8svO40b4FQOBliDQsWMT9_oreLjtfDTlu6PaqQy7WDGbrjI6Ju6pNB2g9h66d6txXHYxALRsh3h8fewFPciKE_Q-z3XB81Br6-QELU8gY3cyfD_ybgXGIOYmGKKvWQp0a5fgAf5Bh_SN8oN5H5oaww7fG6-_okFGvTnWEYpQ9RLuySiDt93D9rnnS4tQFhofOwn0_Nzy-MYjI2aXLRYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/19382" target="_blank">📅 22:21 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

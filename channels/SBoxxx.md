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
<img src="https://cdn4.telesco.pe/file/VFtAQNZxCWHwtEAB0y_Od_SsLai_eDxrCWliynsDtsVmALptUQXuXeDYPsMhKCHsWRRHv6uF1kMsjPSaonlFnKDIFkdfdsk0RgqtaCyfkiFOx4lztrGt7WmQ9HyekE5x_tRQYioZ58owg0aMThRNPe4YBt3u41f0a8XIil6bnYPI3g7HeB8lz7ssgUtlwaLKw3eFKVPtO9bt3_IB_Ru2QrXJ1-9UV4UfjmxHmuZxncTPwh3L704-o_68pE0sejXn6gfd-H1o3D8eJb74XJ2hKaT3jgO4r3fzKEnnOzBr11Teh2R6qbL5uzwArCCj_HZIbaSkaf8ADhwAxBEhPN4FIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.3K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 01:24:32</div>
<hr>

<div class="tg-post" id="msg-18912">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">از کرامات شیخ ما یکی این است
شیره را خورد و گفت شیرین است</div>
<div class="tg-footer">👁️ 64 · <a href="https://t.me/SBoxxx/18912" target="_blank">📅 01:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18911">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سرلشکر رضایی:
هم اسمی و هم عملی دیگر چیزی به‌نام تفاهم‌نامهٔ اسلام‌آباد وجود ندارد</div>
<div class="tg-footer">👁️ 156 · <a href="https://t.me/SBoxxx/18911" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18910">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اینفانتینو: فیفا تأمین‌کننده رسمی شادی برای بشریت است.  ترامپ: مگر اینکه تیم شما ببازد.</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/SBoxxx/18910" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18909">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اینفانتینو: فیفا تأمین‌کننده رسمی شادی برای بشریت است.
ترامپ: مگر اینکه تیم شما ببازد.</div>
<div class="tg-footer">👁️ 579 · <a href="https://t.me/SBoxxx/18909" target="_blank">📅 01:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18908">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تسنیم حمله به یزد و لار را که فرمانداران شان تکذیب کرده بودند تایید کرد!</div>
<div class="tg-footer">👁️ 859 · <a href="https://t.me/SBoxxx/18908" target="_blank">📅 01:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18907">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الجزیره : وقوع ۵ انفجار در شهر یزد، در مرکز کشور.</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/SBoxxx/18907" target="_blank">📅 00:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18906">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">این توافق اساساً نوع مهندسی و طراحی اش به گونه ای است که هیچ وقت به صورت آشکار منجر به حل کامل و قاطع اختلافات نشود. عمداً بخش های زیادی به صورت خاکستری و ابرآلود باقی نگاه داشته شده تا همیشه بهانه ای بر زدن زیر میز وجود داشته باشد.  عین بلایی که سر ما تریدرها…</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/SBoxxx/18906" target="_blank">📅 00:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18905">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مهر:
موشک‌های آمریکا به مناطق شهر اهواز برخورد کردند</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/SBoxxx/18905" target="_blank">📅 00:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18904">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">چی بود امضا کردند اینها؟!</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/SBoxxx/18904" target="_blank">📅 00:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18903">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">Memorandum of Misunderstanding!</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/SBoxxx/18903" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18902">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اخبار تاییدنشده از حمله موشکی به یزد!</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/SBoxxx/18902" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18901">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شایعاتی تاییدنشده دال بر پیوستن اسراییل به آمریکا در حملات چند روز آینده منتشر شده.</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/SBoxxx/18901" target="_blank">📅 00:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18900">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شایعاتی تاییدنشده دال بر پیوستن اسراییل به آمریکا در حملات چند روز آینده منتشر شده.</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SBoxxx/18900" target="_blank">📅 00:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18899">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سپاه پاسداران:
اگر آمریکا به پل‌ها و زیرساخت‌ها حمله کند، ما دارایی‌های صنعتی و فناوری اطلاعات شرکت‌های آمریکایی را که در منطقه حضور دارند، نابود خواهیم کرد.</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/18899" target="_blank">📅 00:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18898">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حملات ایالات متحده به لار، استان فارس، ایران.
گزارش‌ها حاکی از آن است که این حملات با انفجارهای ثانویه همراه بوده‌اند.</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/18898" target="_blank">📅 00:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18897">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رونن کوهن، رئیس هیئت مشورتی کمیته وزارتی اسرائیل در امور شین بت:
«پس از ترور رهبر ایران، یک سوء قصد علیه یکی از اعضای خانواده نخست وزیر نتانیاهو انجام شد که در آخرین لحظه  خنثی شد.»</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/18897" target="_blank">📅 00:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18896">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">همین مانده بود که یک راس دوزاری  دستمال کش  بیاید گه خوری علی دایی را بکند!
ای مگس عرصه سیمرغ نه جولانگه توست...</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/18896" target="_blank">📅 23:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18895">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">محسن رضایی: اگر حملات آمریکا تا دو سه روز دیگر ادامه پیدا کند وارد مرحله تهاجمی کامل خواهیم شد
ایران در مرحله تهاجمی کامل دیگر به مقابله به مثل اکتفا نخواهد کرد و هیچ مرز سیاسی در مقابل تهاجم ایران امنیت نخواهد داشت.</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/18895" target="_blank">📅 22:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18894">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2mU6TzezN2n9gKG0u0u1ranmp16UiXO6Hgij9zTTejbVetZndfWSl96q43zmqxcCTeqT3esuoKTyPgf_dEdNjLuGDjGkZ1tB0algoMej4rsbZweBHlQCO211m3oMn29ofuhQXI_NIjLWTs5yRGyTS6axMzAvL5ItObJGK1HRgLhehbJJAxl_ak-Zt8a7QJufS0FDnsbdjayrxGY0NzKzg6Vwb8mBEHRJzsO7KVnNpwV3qR112REhRSm7fqrmEYJ5I8I9gA6YAd5wjygUI_ohwcA8NrS3nEjd2ajbvF0irL5kEa8G8aIZZaqDE1gZJ8n-ZxAIWOjHpgBGVLjs2IvXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشتی خواندنی از یورونیوز درباره ایزنکوت و حزب ش.  لینک</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/18894" target="_blank">📅 22:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18893">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">داده فروشی به سبک ترامپ!  شرکت رسانه‌ای خانواده ترامپ، Trump Media & Technology Group (TMTG)، قصد دارد سرویس جدیدی با نام Truth API راه‌اندازی کند که به مؤسسات مالی، صندوق‌های سرمایه‌گذاری و شرکت‌های معاملاتی امکان می‌دهد پست‌های منتشرشده در شبکه اجتماعی Truth…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18893" target="_blank">📅 21:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18892">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تحقیقات CFTC درباره اپراتور تله‌پرامپتر ترامپ به اتهام استفاده از اطلاعات محرمانه  گابریل پرز (Gabriel Perez)، اپراتور تله‌پرامپتر که مسئول کنترل متن سخنرانی‌ها و هماهنگی نمایش آن برای دونالد ترامپ است، تحت تحقیق کمیسیون معاملات آتی کالاهای آمریکا (CFTC) قرار…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18892" target="_blank">📅 21:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18890">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vt4-D4jW3W8kYBtm4kNyv4wpEuUWAdKHYeutnfQO5v09h5bEcBZBYQvQL-dioiJ2dxmhOELWjHoMnYeTMbUf2DJeHfIDz36GKjtUxY8jTXD9uf7TfJLeMaWsEhIq-AIfUv6QT0ySah2b36Np-LcLKCOE7O2NYbaceFlaUru4SbCjmdz_-VD9hlYgwGpCTo5xGvasMi6pT_Januv9jz4vO9u8pYhberIs_XQPtSmAFCAFlBBdMkHTE47OsMYUyy599zTkgaKkVR0ZCByq3pwWyb-ayJaNwF65qsM0XC-OW87wkWUn1xK7GAU1FzqXfqu2jkRFQQFAU6QXXGMmBoSqiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQjiFruwH98_UwVz4lBhZHvWpiFpsrp4fsA_DyThm0C6NvTpI9vSfwYeaTYuK2W0J-JPShjRxEtSfDnFOM-bnNjDjEpJES_orXrfz3byGBKAmPpfXY-Lei4bwowZFFCPhmJQoJselFrs6ZwMhsSW5pgfPOjI_hKuxaQgu-gr3dnrrFFzIDnfv7OBYBj23IUcXBb3COVOoq5qoBTmwJgWuh698mI4XKpdlJtYc4JwDjvXYZgrNV7kM52mXMjSvCqwVBEDyeYBxKwmdfpTZyoduXPA0Vuzh_Mk1MQJwQCYQuOTedyNPaUiTXd_GN-IUfpSETr-no7PMOpievoDIu6Tyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همبستگی عجیبی میان شمار اعضای کانال با قیمت دلار به ریال وجود دارد!
شاید چون اینجا هیچ گاه خوش بینی متوهمانه برای مذاکرات به خواننده تزریق نشده است.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/18890" target="_blank">📅 20:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18889">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دولت ترامپ به اسرائیل اطلاع داده است که قصد دارد ده‌ها فروند هواپیمای تانکر سوخت‌رسان آمریکایی دیگر را به این منطقه اعزام کند، در حالی که  ترامپ در حال بررسی گسترش عملیات نظامی علیه ایران است.
اگرچه ترامپ هنوز تصمیم نهایی را نگرفته است، مقامات می‌گویند که احتمال افزایش تنش‌ها در روزهای آینده وجود دارد.
— Axios</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18889" target="_blank">📅 20:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18888">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nC-d6jTebb1mDjCScEJ6x5e7YQX353Py4CPQCBf1T-qmHtyv8gbyeSe7apjfQUHr__SSiaCV6bwzIzG9ereVbuFrBhvB1V5RbO6KtSVCNm8jxTjQKufcjsmncecGphifXOoo6b6rtXum6f-OhoImYcIqoErHSAAV7GAFgwycoQLESatrifm8R5M-Rz-MFvSn8v6soJyNyQQNPC7YRk9SioA1gOizH_Ln8Y99bND__mXkpQRnODfPGwaICBwpdOckYAYUBPQFHp9Xb-9IXZr72LDqYK6oaHBAMKBpBb6UGfR9w06FKLIfEPzGGnxqVSjXADR_aGrxPrzJJLP8HgdSIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز هم شاخص #GRI به درستی پویه های ژئوپولیتیک را تشخیص داد.  #GRI</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18888" target="_blank">📅 19:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18887">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCHyHT0p4Xh9eCaQzfX9_V5mMplWuyqtKZ0vN3cdrMwGrcnvxJr01TJxhRd0OI8VOvvAKrIP4Zi0KbbLW04atcs_okjPWXvH-wETr1QmFr9_c7BqM1eAtc4sRB4-WfcS4cKZQBCWO0Hgn5Vj82mH1L4TUr7sFzbH7hCQ0mrACEuUZEt_v5AlhXSaz0sczeAUAqnAU25vnI2-6j9CdhyhfH8igLdyPk4LmiuDEa4OUIV8Ob24ODXTwPjD6tVjkNsICkvSr6CEEmEH5gNsJ5mO3X6Av1pdG7C4z6PNy9R_2Wjd0zt33onLbIwJiGpuIg48fn5VkxH4jOGQtekq0OggFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه به بالا قرار دارد و از دیروز کاهش یافته است.  پیش بینی می شود بعد از یک افت دیگر در دارایی های ریسکی و طلا، از سشن نیویورک شاهد تقویت میل به ریسک پذیری باشیم.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/18887" target="_blank">📅 19:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18886">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0GZaCGtPZ2FguTJ1IcQLnEbFt1NNCLj72oOGJbgvBNwXjRUKpWfdnxb1Nt8FdLglLd0ocCBv32vd476Z74cjScvFrm5O8NKUe5SZ7EKj9pH9Beb9-vb5aE0WOB_M58lIO-P21cjwuwQlDuph_FGP-fHq_p_CnI_fV239KQKh4kKSPnqbgux65mYBrehgPtbnsRw6PhRiJl1_pNA5MtsNIUcqTXGkP3YyzyTe1GqJ-DlptHRPGhh3H-0aBfBvltF6tVuyw3Wr-ez-51XeoH4i_IVPe_klbdzMRzi6HYl4iXAE5teg90O3-cXlljj5iFMDasHtTF-gxc1zeOaeHn7SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقامات سوریه اعلام کردند که یک محموله سلاح پیشرفته را در نزدیکی مرز عراق کشف کرده‌اند که قرار بود به حزب‌الله در لبنان برسد.  وزارت کشور جولانی اعلام کرد که نیروهای امنیتی، موشک‌های دوربرد، موشک‌های هدایت‌شونده ضدتانک و پهپادها را از یک خودرو مشکوک قبل از…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18886" target="_blank">📅 17:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18885">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پاکستان و کویت در مراحل اولیه گفتگوهایی برای گسترش همکاری‌های دفاعی خود هستند
به گزارش‌ها، کویت به دنبال یک توافق امنیتی به سبک عربستان سعودی است که می‌تواند شامل حضور نیروهای پاکستانی، هواپیماهای جنگنده، پهپادها، سامانه‌های پدافند هوایی و سایر حمایت‌های نظامی باشد و در مقابل افزایش همکاری و سرمایه‌گذاری در حوزه انرژی را به پاکستان پیشنهاد می دهد.
با این حال، مقامات پاکستانی اعلام کرده‌اند که استقرار نیروهای رزمی در حال حاضر مورد بررسی قرار نمی‌گیرد و تأکید می‌کنند که این گفتگوها هنوز در مراحل اولیه خود قرار دارند.
منبع: رویترز
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18885" target="_blank">📅 17:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18884">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruyian3MTXTNBXUrdQhIoF3KKd6NTI0SqwYxriGZJF0QI_tGiTq_JjwFZb2BE8iVVudtHbE-lMhbkXYIvz6JmNifjskV6Al-9xfuNj_q8leD9TCT7yvtL0bbMLTV2-pG-rug-9LsLAekCNQYkATCT-KZ7U2dmLWPvnyrtHMG-KNGFFizEMfCSVFrv4LJUH7fS-uus2P5jVrPwWlfehfgny_WZK23WapNqhGpoJyiR70z3TdWEE2XAR4VRgsncmg0YEAieH_2xUtyWchL64aVvSXJV4bupT0ESQQtRSJuLD1d2X53LBRDgnX-DuJzFZfpRTkDfcOOZDQtl3uB0pIaQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی همسرت رو میخوای طلاق بدی اما مهریه ش هم سنگینه!</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/18884" target="_blank">📅 17:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18883">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نایب رئیس آرژانتین انگلیس را «دزدان دریایی غاصب» و «تجاوز‌گران» نامید و پیش از نیمه‌نهایی جام جهانی به مناقشه جزایر فالکلند اشاره کرد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18883" target="_blank">📅 16:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18882">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ در مورد نخست‌وزیر جدید عراق:  او جوان و خوش‌تیپ است.  من این را دوست ندارم. من از این خوشحال نیستم.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18882" target="_blank">📅 15:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18881">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">علی مطهری:   یک مقام قضایی سطح پایین دستور فیلترینگ تلگرام را داد</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18881" target="_blank">📅 15:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18880">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">علی مطهری:
یک مقام قضایی سطح پایین دستور فیلترینگ تلگرام را داد</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18880" target="_blank">📅 15:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18879">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUaHdaZ6EgRsse3v5PE6mtSefWFmQM4Img_1lUqBLJVtqp1zn-GxJXDeQBoN2FlaMi7GuprxSTrRPFwCx2I5f7U1bJ3h-pwVAO-MxhXLmw37T3dWS7eu9W5hZyTb8Z_bUe9FGmI0ydwdg-2z3EUoDeEuGVPAhK7gdc_KXrqq6v8NN7XLdLAHptyueUMGNKFLMOfF6COULNf7p48Eosm5j0tQ5EEhaAf_viwV9u6M8X8vcZsLwcVbH3Mnrl2MWVoxPfsoknAO1pv0tzjIbCGb6js_ab_Zfhdzf9uzVpm7gWDoxfI8oiaGdXHZRwNHJLFZbhFvJYvFQlqdW8W0-Z7BNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقامات سوریه اعلام کردند که یک محموله سلاح پیشرفته را در نزدیکی مرز عراق کشف کرده‌اند که قرار بود به حزب‌الله در لبنان برسد.  وزارت کشور جولانی اعلام کرد که نیروهای امنیتی، موشک‌های دوربرد، موشک‌های هدایت‌شونده ضدتانک و پهپادها را از یک خودرو مشکوک قبل از…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18879" target="_blank">📅 14:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18878">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بعید نیست ترور گراهام کار روسها باشد که در هفته های اخیر به معنی واقعی کلمه تحقیر شدند و در گوشه رینگ افتاده بودند. گراهام هم یکی از شدیدترین دیدگاه های مقابله جویانه را با روسیه را داشت.  روسها خدای شیمی هستند و هر مدل عوامل شیمیایی برای ترور را که فکرش را…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18878" target="_blank">📅 14:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18877">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMNLn48Qh7F1Dx74O3WqRqW24FRxPxQ4QxPbKmYS2PkB_UZ0MCFoii8sApgE6K296lomE7GhCaA6CJWhv3wl7gV5VPGVO2QD6UjDEgrNf1Fy45rPPJz7fvbMsXbi9cgOGpO65b1ovr6E5EhGjSjMC4s-eA7IWCIllfYblE99ae-GAT1kXHudV0RVMn-Jc1zEHD_-rXVxk_qCFUYlNVZ095cLUsFPOYIiEQ9l93Dq7Dbpkw5NJRA8fDlaUloqk1kPc1t8nKbja-PUjpCIIQtW2hkTOhLZTk0Z4mmGiaO9y0JacjmLcvNbuSgZhJ4Le9ltL9k63yf6pD_mLBOPW_ejIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گراهام همین چند روز پیش در اوکراین بوده؛ جایی که اصلاً بعید نیست هنوز عوامل اطلاعاتی روسها در آن حضور داشته باشند.   مسمومیت با پولونیوم-۲۱۰ (در موارد شدید) معمولاً طی روزها تا هفته‌ها پیشرفت می‌کند. ممکن است فرد دچار ضعف شدید، تهوع و استفراغ، اسهال، آسیب…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18877" target="_blank">📅 13:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18876">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXcIGgBk5-jpjcDa2jjybD2XlUR2nVZxKGnVEMRGoeuEMYBLEPjMRb0BqdfX5rJXiNWDx4uLC5fZRFWy9Jel0y5d9d5ATcWORumo9ZNJny8XeZ2BLsvWwm8dtlozerQr6pjAhNCdr51yUWYoBTnCeuR_iI7DIQ4_RpnvgvcFT6szTspq7S_wVm65M95N3uM1xV8sX0vl-1X3r90AzZK1CfoQeNLuQmLpzRfpfrr98zrWMEcaS8mO2PoCGqPeX6MipcJeMXyzpNJXUQ0PSfIrQNv2Ihr6bPgmV6PonC4DaGOW_tDkjamo0Gy63pSYVgXfSa8S7OA6WnJRbNQQbbtwVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توفان احضاریه‌ دموکرات‌ها؛ تلاش نمایندگان کنگره آمریکا برای واکاوی معاملات ترامپ و حلقه نزدیکانش  لینک  #بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18876" target="_blank">📅 13:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18875">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الازرق</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18875" target="_blank">📅 13:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18874">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
انهدام چند فروند سوخت‌رسان و جنگندۀ آمریکایی با موشک بالستیک و پهپادهای متعدد
در موج۱۴ عملیات نصر۲
🔹
سپاه پاسداران: مردم شریف اردن؛ مردمان نجیب سرزمین قدمگاه انبیا الهی، ای مردمی که بیش از همه‌ی مردم جهان با فلسطین قرابت دارید و با دردهای مظلومان غزه و کرانه از همه آشناترید، بعد از حمله سال گذشته ما به پایگاه العدید قطر، ارتش کودک‌کش آمریکا برای دور کردن مرکز فرماندهی خود از حجم بالای آتش رزمندگان اسلام، مرکز فرماندهی نیروهای آمریکا در منطقه (سنتکام) را از قطر به الازرق در خاک شما منتقل کرد و از آن موقع تاکنون مرکز فرماندهی شرارت علیه مردم فلسطین و سایر کشورهای اسلامی در خاک شما و دردسترس شماست.
🔹
علاوه بر سنتکام پایگاه هوایی و دهها فروند سوخت‌رسان، اف۳۵، اف۱۵، و اف۱۶ آمریکایی در خاک شما مستقر هستند و از آنجا به مردم مظلوم فلسطین، ایران و لبنان حمله هوایی می‌کنند.
🔹
شب گذشته ارتش کودک‌کش آمریکا بازهم شرارت کرد و از پایگاه‌های خود در اردن برای ارتکاب جنایت جنگی بزرگ و زدن اهداف غیر نظامی از جمله چند پل، محلات مسکونی و یک مرکز پمپاژ آب در بندرعباس در جنوب ایران استفاده کرد.
🔹
در پاسخ به این شرارت، رزمندگان اسلام در موج ۱۴ عملیات نصر ۲ با رمز مبارک یا صاحب‌الزمان(عج) ادرکنی جنگنده‌ها و سوخت‌رسان‌های آمریکایی مستقر در اردن را در دو مرحله حمله با چندین فروند موشک بالستیک و پهپادهای متعدد مورد هدف قرار دادند که منجر به انهدام چند فروند سوخت‌رسان و جنگنده آمریکایی و آسیب جدی به تعداد بیشتری از آنها شد.
🔹
اینک نوبت شما مردم شریف و ارتش غیور و با شرف اردن است که به تکلیف الهی خود عمل کنند و با ضربه به منافع آمریکایی متجاوز و ضداسلام، لکۀ ننگ آمریکاییهای اشغالگر را از دامان اردن عزیز پاک کنید.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18874" target="_blank">📅 13:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18873">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تیم ملی والیبال نشسته ایران با شکست ۳ بر ۱ بوسنی، نهمین بار قهرمان جهان شد</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18873" target="_blank">📅 13:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18872">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تیم ملی والیبال نشسته ایران با شکست ۳ بر ۱ بوسنی، نهمین بار قهرمان جهان شد</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18872" target="_blank">📅 13:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18871">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دولت بریتانیا سپاه پاسداران انقلاب اسلامی را در فهرست سازمان‌های تروریستی قرار داد که بر اساس آن، عضویت در این نهاد، شرکت در نشست‌های آن و حمل نماد آن در انظار عمومی جرم کیفری خواهد بود.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18871" target="_blank">📅 12:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18870">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">📌
تایید مواضع هاوکیش وارش از سوی همکارانش در فدرال رزرو  لوگان و اشمید تأکید کردند که تورم هنوز مهار نشده و فدرال رزرو نباید برای کاهش سریع نرخ بهره عجله کند.  این رویکرد هاوکیش می‌تواند از رشد دلار حمایت کند و در کوتاه‌مدت فشار بیشتری بر طلا وارد سازد.
🔗
…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18870" target="_blank">📅 12:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18869">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phwGCYM8goQoiDRJrA8gJXTSeu261Tu8mBgIbq3h9ArZ2Or7HrEOfiggD4WJu3rklk3ZfQ6FsXKpbI-doowu4cRRlZHzevJbRTIpkXtk4xP9mhTIEeDUaMjXBvntmagEeFm6bquLnz85TqTcB7wmRQdqU5J5Uh8-ewsHR01UBJnLJwuMOPJpFb6oAyfZxyn2qWt1PSA_nz2569VlmVSNRbkl8QM4Lg8U74aaj9iyOzXB8OiC9ZVOwk2E8PfV6g3foqSfgB4_XbLm-ISP1FMWSGU5laBuFkPwxrd3tPArQZ8k4a3-NL1iG6JS6HoztfeGbqK3UxRJFvnjkBRYksQyig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تایید مواضع هاوکیش وارش از سوی همکارانش در فدرال رزرو
لوگان و اشمید تأکید کردند که تورم هنوز مهار نشده و فدرال رزرو نباید برای کاهش سریع نرخ بهره عجله کند.
این رویکرد هاوکیش می‌تواند از رشد دلار حمایت کند و در کوتاه‌مدت فشار بیشتری بر طلا وارد سازد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18869" target="_blank">📅 11:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18868">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KiwKisj063Smwc5a1-4At5pMadWBLF_Na5AlbqmDO5wg1benhLUHkc96d8qmvVOXM_wZfLsAGpuWeWkBg7mNZewkLnZxnkLXmH6MYofSmszO_TxA9Vgvfm7_w5-yerLPlkjnKvfrft4EZY6VuI4msufdH7vWDPzeDIplDao8_VXdFwNl14Hi7MD4mgsG19NFc_L3eRw68nF4uwFPSAsDgx8UJA43PceByci3IvQAT-kARDxYUI1MhTy_pj1-Zt2vBi80uUT3pHsIoHnT6b42PoiWuzva3232tZLsokHZqW2ZDGVMXPER2zPu8hykEyDFohicbB6rOcQrWl5acRCeTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ـ
😄
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/18868" target="_blank">📅 11:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18867">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mthcaWE9G8NKhGWNoxqUo4VnQrmzfQN-i7gjNLVo0Vu0ITapphzAmkUfzomIny_3shFYMX0OKzxYxWtycEr5-z8Gl88cHTCPQGfQg0WcMInbHxeUwlqsACe22n2kAxNFfdsbVrM18-_kuUP28C7xMZx7gVzMQvT_kNJgNXugIjghvoSyc0FNUPsmcfM9_XTnh6W_WMNzVZR53qc_hiYisP6TpLAaTssj-2OCx0y_eL4DQ9zvg6QZ0LZfpiVKRR3BxIdvDnHhG7HnkT7X_RErkGgC9HblirjXDMssOedNpEORh62vzN2myHvxdUm13skCRfiowQef15L428y3A4_1kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این نمودار نسبت بورس به سکه که دست به دست می شود و از آن عملکرد بهتر بورس نسبت به طلا در سالهای آتی نتیجه گرفته می شود تنها در صورتی محقق خواهدشد که :
— سازش اساسی — چندین بار بهتر و فراتر از برجام — داشته باشیم
— تغییر حاکمیت سیاسی در ایران روی بدهد و آن هم بدون جنگ داخلی و تجزیه
به جز این دو صورت هیچ تضمینی نیست که این بار هم محدوده حمایتی مشخص شده حتماً جواب بدهد.
تحلیل تکنیکال روی Ratio Charts هیچ تفاوتی با تحلیل تکنیکال روی نمودارهای سنتی ندارد و ممکن است همین رنج اساساً به پایین بشکند.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18867" target="_blank">📅 11:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18866">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPVNV58ubUiBfbmYrsun0ME0tQcWTct3ybum9gMRm5sv19q-gGTRV2EELf0LYwE7KHabl5jhzrRllnEY5dLwe4E6euFR4_q3g58SyR6dTdOphtVNb2xQhN7UC22W8oHX7MfzGNhBgpLiPoxW2P0N6hEi4mcXk55Tv2DVAcW6gV2-kgBO09NxnEM8F-0p60dV4j5z70MkOUX6E_C0-JWZCER9KczddqbrlSUZQPtzNENROaE0XwPNn0CsmT8mLXl3gXr6jadPGLGaG_E1F2D3ioQaRNP5Zp47yLtcsEHdzmcixJUDgiVMPzSqP7wc4ckrAakuM_yhvU6q5msQJftX_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ را در زمین ونس ترنس انداخت تا خودش را مبرا نشان دهد.  ونس 1405 = مرفاوی 1385</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18866" target="_blank">📅 11:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18865">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sV_bnFDXglTTUyuoulmUq7T-miummimzZFCFjQNeN9TnpgqjDJZCjar4eyHohwq74FX03-t9_Y5zBjD_HLWKOkT_rVRYytSEzyvzSMQOIyAdZuG4V5HfP2GFjszVLCVd36fq8i5jRsd_9B0V2N8cl0JgoCYkkd58FvbvCYJC2bYsZD2pDQ6lRHJrOiNYEbTL1ynOGWO9-UDR3bKQrkqvwmFxoYnUiwePlkin7OuMR3RRPWVErfywswYJrZ3wigL4y24pMWpNgg875g9p0FRLVMC3QsEzIo4kQaCSTz6sY7joG2bDf2MVxSUBHZbdLRC0ckoholJBeCj5w8KZXapSLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه به بالا قرار دارد و از دیروز کاهش یافته است.
پیش بینی می شود بعد از یک افت دیگر در دارایی های ریسکی و طلا، از سشن نیویورک شاهد تقویت میل به ریسک پذیری باشیم.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18865" target="_blank">📅 10:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18864">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18864" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 8
جمعه 17 جولای 2026</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18864" target="_blank">📅 10:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18863">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مرکز UKMTO:
گزارش دریافت شده حاکی از برخورد یک تانکر با یک پرتابه نامشخص در روز پنجشنبه، در فاصله ۱۹ نریلی (حدود ۳۵ کیلومتر) شرق شهر خصب کشور عمان است. گزارش‌ها حاکی از آسیب جزئی به ساختار تانکر در نزدیکی عمان است.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18863" target="_blank">📅 10:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18862">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سپاه پاسداران: رادار کنترل دریایی در صخره‌های سلامه و رادار کنترل هوایی آمریکا مستقر در منطقه غنم عمان منهدم شد
در ادامه عملیات مقابله به مثل رزمندگان اسلام، سحرگاه امروز نیروی دریایی سپاه در موج ۱۳ عملیات نصر ۲ با رمز مبارک یا اباعبدالله الحسین (ع) و تقدیم به تمامی مردم‌خونگرم استان‌های خوزستان، بوشهر، هرمزگان و سیستان و بلوچستان، رادار کنترل دریایی در صخره‌های سلامه و رادار کنترل هوایی آمریکا مستقر در منطقه غنم عمان را هدف قرار داده و منهدم کردند.
عملیات مقابله به مثل با قاطعیت ادامه دارد، همان‌گونه که بعثت جانانه شما مردم؛ و تنگه هرمز هم به فضل الهی کماکان در قبضه قدرت دریادلان نیروی دریایی سپاه است</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18862" target="_blank">📅 10:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18861">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dr4gzJYPK9wwyAMIKB0e0WG24mqGVMyqvyrTLsunnj1wVMgXMo1Z2a5MdR1xsZCQjiARe0q6BQoqt0ZWm40Pm2-auYw7fiTuoRfyqle9Ufy2wODFapp3v2ggDKMlG5qUJnwEKeN8SrDgqWKcLUrhqrUgQ_WDijGh1rxYZk57xYqziSyKmRO0OdsqID46Xrc3mahrTu-ocf8nMjOvEMDwJvmldQrj_fC5Svz6SqYNKzU5UUD2zloPo3sdmPXhYGpGSk7eKHMGCKYqB9TqDHUyFe_l0QpCgj7ybpg53ti98faqbrUsbu-X3sD_o-nlrSD50YvufFlXTSRxFOpcYiARGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برج کنترل دریایی چابهار</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/18861" target="_blank">📅 07:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18860">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">به‌روزرسانی ۱۶ جولای  سنتکام: یک کشتی «از کار انداخته شد» و کشتی دیگری «برای اطمینان از رعایت کامل محاصره دریایی مداوم علیه ایران» توقیف شد.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18860" target="_blank">📅 01:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18859">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تلویزیون ایران:
قطع برق در فرودگاه ایرانشهر واقع در استان سیستان و بلوچستان، در پی حمله آمریکا، اما هیچ تلفات جانی گزارش نشده است.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/18859" target="_blank">📅 01:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18858">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXKYE3s6TRBwt15r2OHieLbldFPSpEWc856vGdzLbyRSt0lK2rSHmijVAQ6hl95h2e0v-pO5ZDcPeCwpv_evg0m7ZwGiMJlsUn8vNG_qeIF1aItJaroMk4qdJ-ZyvzdV4F6XjPA2pdGtgqDUdtLfOT3nbwx0_Ln2yXk66aOGXFX2zF40iAlmIdKY_ywBzX_bbKoiAB4eY2lQDEIJIIDbZRDURdeZiBEyDNz9nZeUQ-39R7NXfumQaPQJRAzRyiQj_j_i7HAeZ01KASy3Jx4bRqBkMlb3ZTgRQxOnj9LS8l_9P0Dss9sfkVVaMEffZwjgcqMmrTPQ0ZSdimFr1wiyUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا ایران مستقیماً یک سامانه موشکی زمین به زمین آمریکایی را در کویت هدف قرار داده است.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/18858" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18857">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">به‌روزرسانی ۱۶ جولای  سنتکام: یک کشتی «از کار انداخته شد» و کشتی دیگری «برای اطمینان از رعایت کامل محاصره دریایی مداوم علیه ایران» توقیف شد.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18857" target="_blank">📅 01:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18856">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گزارش حمله به کویت، که احتمالاً توسط گروه‌های عراقی وابسته به ایران انجام شده است.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18856" target="_blank">📅 01:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18855">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آقایان این همه می گفتند پایگاه های آمریکا در منطقه را در هم کوبیدیم!  هیچ تاثیری در کاهش توان آفندی آمریکایی ها نداشته. هر شب دارند بدتر می زنند و اینها هر شب برای سر ترامپ جایزه می گذارند!</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18855" target="_blank">📅 01:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18854">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">رسانه های اسرائیلی:
پرواز جنگنده‌های اسرائیلی به سمت مقصدی نامعلوم.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/18854" target="_blank">📅 01:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18853">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گزارش حمله به کویت، که احتمالاً توسط گروه‌های عراقی وابسته به ایران انجام شده است.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18853" target="_blank">📅 01:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18852">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">Business Insider:
اسرائیل از حملات موشکی ایران آموخت که به رهگیرهای بسیار بیشتری نیاز دارد؛ رئیس برنامه دفاع موشکی: «این یک مسابقه است»
حملات موشکی ایران، اسرائیل را به این نتیجه رسانده است که برای جنگ‌های آینده به تعداد بسیار بیشتری موشک رهگیر نسبت به برآوردهای قبلی نیاز دارد.
«موشه پاتل» (Moshe Patel)، رئیس سازمان دفاع موشکی اسرائیل، در گفت‌وگو با
Business Insider
گفت که تجربه نبردهای اخیر نشان داده است تولید رهگیرها باید با سرعت بسیار بیشتری انجام شود، زیرا «این یک مسابقه است»؛ مسابقه‌ای میان توان تولید رهگیرهای دفاعی و توان دشمن برای تولید و انباشت موشک‌های تهاجمی.
به گفته او، سامانه دفاع موشکی
Arrow
(پیکان)، که لایه اصلی دفاع اسرائیل در برابر موشک‌های بالستیک است، در جریان حملات ایران عملکرد موفقی داشته و طی عملیات‌های سال‌های ۲۰۲۴، ۲۰۲۵ و همچنین جنگ طولانی‌تر سال ۲۰۲۶، صدها موشک بالستیک را رهگیری کرده است.
پاتل گفت نرخ موفقیت این سامانه همچنان بیش از ۹۰ درصد بوده، اما حجم حملات و تغییر تاکتیک‌های دشمن نشان داده است که موجودی رهگیرها باید بسیار بیشتر از برآوردهای گذشته باشد. به گفته او، حتی اگر سامانه عملکرد بسیار خوبی داشته باشد، در یک جنگ طولانی، مصرف رهگیرها به سرعت افزایش می‌یابد.
وی افزود که اسرائیل اکنون علاوه بر افزایش تولید رهگیرهای فعلی، توسعه نسل‌های جدید این سامانه را نیز با سرعت بیشتری دنبال می‌کند. رهگیر
Arrow 4
به مراحل پایانی توسعه نزدیک شده و
Arrow 5
نیز در دست طراحی است. هر دو سامانه قرار است با بهره‌گیری از فناوری‌های جدید، از جمله هوش مصنوعی، توان مقابله با تهدیدات آینده را افزایش دهند.
پاتل تأکید کرد که اسرائیل تمامی داده‌های به‌دست‌آمده از رهگیری‌های واقعی را به دقت تحلیل می‌کند تا سامانه‌های دفاع موشکی خود را بهبود دهد. او گفت هر درگیری واقعی، اطلاعات ارزشمندی در اختیار مهندسان قرار می‌دهد که در آزمایش‌های عادی قابل دستیابی نیست.
این مقام اسرائیلی همچنین به فشار فزاینده بر زنجیره تأمین جهانی سامانه‌های دفاع هوایی اشاره کرد و گفت افزایش تقاضا برای موشک‌های رهگیر، از جمله سامانه آمریکایی
Patriot
، نشان می‌دهد بسیاری از کشورها به دنبال تقویت دفاع موشکی خود هستند و تولیدکنندگان باید ظرفیت تولید را افزایش دهند.
او در پایان گفت درس اصلی جنگ‌های اخیر این است که داشتن یک سامانه دفاعی پیشرفته به تنهایی کافی نیست؛ کشورها باید ذخایر بسیار بزرگی از موشک‌های رهگیر نیز در اختیار داشته باشند تا بتوانند در صورت وقوع یک نبرد طولانی، به دفاع مؤثر ادامه دهند.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18852" target="_blank">📅 00:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18851">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انفجارهای شدید در سیریک</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18851" target="_blank">📅 00:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18850">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آقایان این همه می گفتند پایگاه های آمریکا در منطقه را در هم کوبیدیم!
هیچ تاثیری در کاهش توان آفندی آمریکایی ها نداشته. هر شب دارند بدتر می زنند و اینها هر شب برای سر ترامپ جایزه می گذارند!</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/18850" target="_blank">📅 00:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18849">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نماینده کنگره آمریکا از «تغییر رژیم» در ایران گفت
نماینده کنگره آمریکا تیم بورچت خواستار روی کار آمدن فردی در ایران شد که به گفته او با آمریکا تعامل کند.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/18849" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18848">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حمله آمریکا به تانکرهای سوخت در بندر عباس</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/18848" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18847">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حمله آمریکا به تانکرهای سوخت در بندر عباس</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/18847" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18846">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">لطفاً از مراکز نظامی فاصله بگیرید. ویدیوی وحشتناکی از اصابت موشک های آمریکایی به جایی در بوشهر دیدم.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18846" target="_blank">📅 23:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18845">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجارهای بزرگ در بندرعباس، قشم و اهواز</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18845" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18844">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">به نظر می رسد تنها یک معجزه می تواند از بروز حمله زمینی آمریکا جلوگیری کند.
تصور می کردم در اوج گرما این کار را نکنند اما روند حوادث چیز دیگری را می گوید فعلاً.</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/18844" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18842">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآرش رئیسی‌نژاد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/545819aa84.mp4?token=Bgr21jUuhw5uFeF2d6h444um_8QiX1YsvVLvOcken2HoPCRLYwkKgfVlw0eCzXIYWas9zVlzUcADE3QmjjX6lo567l_vD98KYOO7FhFsJgl2jj9Y78sWt4sSQfSQ009_5XkKnHTYfYD58Z1tucGCoTDxzBbeIWJUj4GHaX_xCBdAOGFalZMrWBW5b5JEV9791Sl4wdM-C8GxAzpdRPNQATAgT2gzklfxx4WeqAPQD4h6bqc_-1j3ogYxau2rNdljBDCLtp_XGGuv_aMixU87BGHucTRuC6pOSvF8D06H6TdN-pPXnOStyeFwyxCBqyxXmpq04630q9wszz_4vbS5bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/545819aa84.mp4?token=Bgr21jUuhw5uFeF2d6h444um_8QiX1YsvVLvOcken2HoPCRLYwkKgfVlw0eCzXIYWas9zVlzUcADE3QmjjX6lo567l_vD98KYOO7FhFsJgl2jj9Y78sWt4sSQfSQ009_5XkKnHTYfYD58Z1tucGCoTDxzBbeIWJUj4GHaX_xCBdAOGFalZMrWBW5b5JEV9791Sl4wdM-C8GxAzpdRPNQATAgT2gzklfxx4WeqAPQD4h6bqc_-1j3ogYxau2rNdljBDCLtp_XGGuv_aMixU87BGHucTRuC6pOSvF8D06H6TdN-pPXnOStyeFwyxCBqyxXmpq04630q9wszz_4vbS5bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهار ماه پیش، در مقاله‌ام در Foreign Policy، استدلال کردم که پنج نقطه استراتژیک در جنوب ایران، محتمل‌ترین اهداف هرگونه کارزار نظامی گسترده آمریکا خواهند بود. امروز، الگوی در حال شکل‌گیری حملات بیش از هر زمان دیگری با آن ارزیابی همخوانی دارد.
توالی حملات نشان از استراتژی کلان‌تر محتملی دارد. عملیات از جزایر آغاز شد، سپس به سواحل رسید و اکنون در حال نفوذ به عمق بیشتری از جنوب ایران است؛ حتی به مناطقی که دیگر در نوار ساحلی قرار ندارند. این‌ها صرفاً مجموعه‌ای از حملات تاکتیکی و پراکنده نیستند. آنچه دیده می‌شود، به نظرمی‌رسد بخشی از تلاشی گسترده‌تر برای تضعیف تدریجی معماری دفاعی ایران در کنترل تنگه هرمز و دیگر گره‌های استراتژیک، از جمله جزیره خارک، باشد.
اینکه این روند در همین نقطه متوقف شود یا نه، هنوز پرسشی باز است. اما الگوی کنونی این احتمال را مطرح می‌کند که این حملات تنها بخش آشکار یک طرح عملیاتی بزرگ‌تر باشند؛ طرحی که هدف آن خنثی کردن، یا حتی فراهم کردن زمینه برای کنترل آینده برخی از مهم‌ترین نقاط استراتژیک جنوب ایران است.
@Iran_Simorq</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18842" target="_blank">📅 22:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18841">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فرماندهی مرکزی ارتش آمریکا (سنتکام): ارتش ایالات متحده حملات جدیدی را علیه ایران انجام می‌دهد.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18841" target="_blank">📅 22:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18840">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سخنگوی کاخ سفید، لیویت:   ایران همچنان با ایالات متحده در گفتگو است و خواهان رسیدن به توافقی است؛ حملات اخیر به دلیل نقض توافق‌نامه توسط ایران صورت گرفته است.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18840" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18839">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سخنگوی کاخ سفید، لیویت:   ایران همچنان با ایالات متحده در گفتگو است و خواهان رسیدن به توافقی است؛ حملات اخیر به دلیل نقض توافق‌نامه توسط ایران صورت گرفته است.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18839" target="_blank">📅 21:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18838">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سخنگوی کاخ سفید، لیویت:
ایران همچنان با ایالات متحده در گفتگو است و خواهان رسیدن به توافقی است؛ حملات اخیر به دلیل نقض توافق‌نامه توسط ایران صورت گرفته است.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18838" target="_blank">📅 21:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18837">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Au6D1QdCd5WD7IPeDpzYGHSnA1IaaMVVuKxFaPUQ_nhnbrtUYS_GCd4Nr0YTP0hV0aZjVaMMYSVzhq4aK6j0hRv29epuOpJfLDAfnl3iAMOz1ulJJFCb1GjS9p98JrIRf1BVdgZiTrtPEiZBdIdMq1oIsfTDm1EUbhpyLSKXe_jZT0wRyQkpKiBzaC11AJMWWMn8_KlDhpQG-RTFckYrmAa-QOlkTboa9i9s9MujiK4x-q8DgSJf9_bqe1Bt6ytdQ6KZZzU9QUGmILo7gDM9DkTV9vsgRwNBcTfzWMLMLGefHj31NohjZZBsjhj2MPoQ8GamIAyi4PZVmTUn6OD-kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به حملات علیه املاک ترامپ در خاورمیانه تهدید کرد
باشگاه‌های گلف و برج‌های بلند در امارات متحده عربی، عربستان سعودی، قطر و عمان می توانند هدف قرار بگیرند:
- باشگاه گلف بین‌المللی ترامپ دبی - منطقه داماچ هیلز، دبی، امارات متحده عربی؛
- هتل و برج مسکونی بین‌المللی ترامپ دبی - مرکز شهر دبی، امارات متحده عربی؛
- برج ترامپ پلازا جدّه - ساحل جدّه، عربستان سعودی؛
- برج ترامپ ریاض - ریاض، عربستان سعودی؛
- باشگاه گلف بین‌المللی ترامپ وادی صَفار - وادی صَفار، دیریاه، عربستان سعودی؛
- باشگاه گلف و ویلاهای بین‌المللی ترامپ سمایسما - سمایسما، قطر؛
- هتل بین‌المللی ترامپ عمان - مسقط، عمان.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18837" target="_blank">📅 21:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18836">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وزیر امور خارجه اردن، ایمن صفیادی: ایالات متحده هیچ پایگاهی در اردن ندارد، اما سربازان آمریکایی به عنوان بخشی از همکاری نظامی بین اردن و واشنگتن، در کشور ما حضور دارند. - خبرگزاری فارس</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18836" target="_blank">📅 21:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18835">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وزیر امور خارجه اردن، ایمن صفیادی: ایالات متحده هیچ پایگاهی در اردن ندارد، اما سربازان آمریکایی به عنوان بخشی از همکاری نظامی بین اردن و واشنگتن، در کشور ما حضور دارند. - خبرگزاری فارس</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18835" target="_blank">📅 21:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18834">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_r7_3HdajPB94qMdADOxf_b7KFdIMBP4FwjugxxJ66NhhclmxgJ1uuRZEo-U-yV7iY8mGj_EpW21rrEh1gW39IoTeuA3D2tcppruLCLdEy5Km9iGfNmjC5gJL8XSd352imlqDGhhuIlJ2C72iqtnEB7Y9dZTaUwaaN8zQBXpIP60LKxMJJAAU7ZWNY7mvr_RxfBaQ8J7WnMehj3IXXXnsfovtHDapIkLhzITeYBfLc2uw6QlNSNvRA_3AFnNZ1_Y_5lxi-ypGcovB0nrATjGDsjX2Tr1Ip83TBuYS7vfxUhyFQ0ddkuDoZ0vQz6fmTYHMPQjxSl4NpFjZc7WgU9PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ را در زمین ونس ترنس انداخت تا خودش را مبرا نشان دهد.  ونس 1405 = مرفاوی 1385</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/18834" target="_blank">📅 20:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18833">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEk4a9EAcibgsNwaBm_UVQhqJ9acQqPKGk7kK62EdRU4yeRmw2rNea8gtWxBgQ2Q91SaO877t9ZLtXRsOdr7ZXuUe8_iIRb325k7yMHEsIGLCKHpL7KyWBD8n_GHpWOeDuFNjBYfH_Qc086FrCMM_bdcFiTNVlxfbYB1kyXRYbegE098OhKixh9F4VH1HYfY8rMVrJIoFtDZUw8CUyHOFAJAOZRU0-6dXb9KreRs8Z-TCW5kTys6hdqx9DieoTNORiW3vNx3PZTnVfuxvbZKVHQZ_tQtrBQ4UsXbujgkKmRpU35CV576Jrj6Pcoct-NC8Ly0Uh2hjaMPNecgJc_izA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سل طلا بسته شود.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18833" target="_blank">📅 18:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18832">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">موشک‌های آمریکایی به اهدافی در جزیره قشم در جنوب ایران اصابت کرده‌اند.
— خبرگزاری مهر</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18832" target="_blank">📅 18:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18831">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رهبر یمن سخرانی مهمی را آغاز کرده است</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18831" target="_blank">📅 18:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18830">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">این دیگر حماقت محض است. شما شاید بتوانید با موشک و پهپاد اهدافی را در یک کشور مرفه ثروتمند مانند قطر یا کویت بزنید و آنها را وادار به دادن امتیازاتی بکنید؛ اما زدن اهداف مربوط به کشوری که مانند صوریه جولانی 15 سال است اساساً در گه فرورفته و مردمش نمی دانند…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18830" target="_blank">📅 17:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18829">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مشاور محسن رضایی:   تصمیم مهمی در تهران اتخاذ شده است؛ اگر حکومت جولانی بنا به درخواست ترامپ و فشار آمریکا دست به اقدام علیه حزب‌الله بزند، با حملات موشکی و پهپادی مستقیم ایران مواجه خواهد شد. این هشدار به جولانی داده شده است.  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18829" target="_blank">📅 17:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18828">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1LNdg8TF147w5hxTwCbMDN915E14V9Ag9sO7tI6_UJTyjPv0Z8MIf0ZeCeyFboVUlyazCqbmE5huDf07oTx2kYK7v5qlAkNIl5Fq88nLGJZgACEDspGTPmvHZeVmKycfGdhd7mb3WDm08jHq8uI2JcWEX9uz75PwgyTR_gfcZwbNjTwO8CGEZbiL0fGekiEFLQJxM-Kg4NZ6YOk8k-Tq0nt7OJ4xF4ZERcLGlIsJX8n2KYX24q7ROdqMzeLxiu-zD6xpmsWr_0LBYtuCr6Tv4OEoLLlPT7bALJ95dgVpNjPOIoIcjJ4kT21EbpGulvXYix-_q4dqnWAWZsund9O0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر شما ترامپ با این سه سگ (اردوغان، فیدان، کالین) چه صحبتی می تواند داشته باشد آن هم وقتی که جولانی هم دارد به اینها می پیوندد؟!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18828" target="_blank">📅 17:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18827">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rS0Yr2Yglxcn9KukveA10eq7PmszsNg0TdlCBzy4Ih1vN1_aNF38WRWZbS_TY0rkKYppqdg85U9PiFZVt41bRmqRpzxslFYOE_faFBB0aLBhRI5E1WIIariMlljEsqxHrCqFDGlMU42JjEKQG29VGB443CKkfY_d2rGLHF1EO44cHhmlbsxnVmUFE3Kw_vAAdNvzjGYgXyWBpsfrX3DwQvv5qDpvqHDuVoPmsh5-4nEh8WOzXIRhiRQqLTlGFgH5dG2r_AZ_d3gHiUlaDlMnI35XN1x9W30O2-m-Xcl_5w8eetuxGnp5Hw6P7Yp_WC5m3dPyCk8_lWW_wvGdul3eYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار: آیا رئیس‌جمهور الشرع (جولانی) برای شما تعهداتی در مورد کمک به حزب‌الله در لبنان داد؟  ترامپ: بله، او این کار را کرد.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18827" target="_blank">📅 17:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18826">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رهبر
یمن سخرانی مهمی را آغاز کرده است</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18826" target="_blank">📅 17:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18825">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18825" target="_blank">📅 17:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18824">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بالایی است و پیش بینی می شود شاهد جو ریسک گریزی باشیم.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18824" target="_blank">📅 16:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18823">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نایا به نقل از یک منبع مطلع:
امارات در حمله شب گذشته به بندرعباس مشارکت داشته و در این عملیات، به‌طور مشخص از پهپادهای اماراتی علیه این شهر ایران استفاده شده است.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18823" target="_blank">📅 16:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18822">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9aF0AZ3naiEeGWf68OjrUKubCzDIK4c9z6NMWS4wdF6QKIcP42K1spopi1z1rvndmEeb_DjPt7_h7Q2Chkcw9ehiJQhvMfNYGyHQfgP5wQKr8kANiaZU4hYhEzQ-0YOlcDKF6T3QjHa4bThafwPNxaSwL1EDE-QviN1-Kc7o1JtC7w7sih9SEvhvuuKByGLAAyL-rKe6j4bdI6RVrpXD0e6esHCvG-Bc2e-VJ3wmXWWYfPPod5tupuW8CUyIvH8yKXY5BYEfjTf_qaYXu3MDvMyPSuAL-OjgXNOFvzZ96kBIYuyzliPkHZFt-_2AD7XebPHZpXAWBvY7zGe5Qa0UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این قیمت های گوشت، همه مان باید بزودی به هیات مذاکره کننده پیوسته و گوشت الاغ مرده بخوریم.
آبش را هم بدهیم میساکی بخورد.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18822" target="_blank">📅 15:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18821">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سخنگوی قرارگاه مرکزی خاتم‌الانبیا:   زیرساخت بزنید، هرچه زیرساخت در منطقه باقی‌مانده را می‌زنیم</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18821" target="_blank">📅 15:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18820">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یک تانکر نفتی در بندر بصره در عراق مورد اصابت یک پهپاد قرار گرفت و تمامی عملیات بارگیری نفت در این بندر به حالت تعلیق درآمد.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/18820" target="_blank">📅 13:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18819">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmF3UUJQAJlv3aB0gwFej0K_K5bSixxz0I9O-pz1hFLOnVF40PfFatRMGv9N96z6Oj5EqCAotL68-8fCreMdQk8HnsHa-77kIzIE4GonS47mG1Nu_3iwvOhpkEfzlRvGcdqD8yz3666PCAsTJhcFIDOcsDW9-3AOWp9wZPt_y2Drk66uJKw5X5QtkFvFUFyWD4QauJbcqG43_y1K9FdOCH-OXm6OO3xlVbicP9b_J2obzsdrdykL6Iw5erpBDAGezipgeeXWwcaRxJOIAAS2vkUbSXPIUggbmmzlCRz57fJdbqSeXJqWtzf-utmOb63Q1FHR7LCNw4JVf_xq4tgYaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بالایی است و پیش بینی می شود شاهد جو ریسک گریزی باشیم.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18819" target="_blank">📅 13:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18818">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اداره کل کشتیرانی هند شامگاه چهارشنبه ۲۴ تیر با صدور دستوری اعلام کرد تا اطلاع ثانوی هیچ دریانورد هندی نباید به کشتی‌هایی اعزام شود که مسیر سفر آن‌ها شامل عبور از تنگه هرمز است.    در این دستور آمده است: «با توجه به تشدید وضعیت امنیتی در منطقه خلیج فارس، اداره…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18818" target="_blank">📅 13:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18817">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یعنی وسط کویر لوت هم یک قایق کاغذی کاردستی پنج سانت و ده سانت چپه بشود چند هندی گم می شوند!</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/18817" target="_blank">📅 13:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18816">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">این امر روی بدهد، سپاه گزینه آخرالزمانی نابود کردن تاسیسات نفتی منطقه را فعال خواهدکرد.  البته همزمان ترامپ گفته که ایران خواهان توافق است و این ور هم سیگنالهای سازش می فرستند. روزهای آینده مشخص خواهدشد.</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SBoxxx/18816" target="_blank">📅 11:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18815">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سنتکام:
موج جدید حملات ایالات متحده علیه ایران به پایان رسید
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (CENTCOM) در ساعت ۹ بعد از ظهر به وقت شرقی در ۱۵ ژوئیه، موجی از حملات علیه ایران را به پایان رساند.
نیروهای ایالات متحده به مراکز فرماندهی ایران، سایت‌های پدافند هوایی، توان موشکی و پهپادی و تأسیسات نظارتی ساحلی حمله کردند تا توانایی ایران در تهدید دریانوردان بی‌گناه خدمه‌رانی در کشتی‌های تجاری در حال عبور از تنگه هرمز را بیشتر تضعیف کنند. سنتکام از مهمات دقیق برای هدف قرار دادن اهداف در چندین مکان از جمله بندرعباس استفاده کرد.
اوایل امروز، نیروهای آمریکایی در یک موج ۹۰ دقیقه‌ای به سایت‌های دفاع ساحلی و موشک‌های کروز در جزیره بزرگ تنب حمله کردند.
ارتش ایالات متحده در جهت فرمانده کل قوا، ایران را مسئول می‌داند.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18815" target="_blank">📅 10:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18814">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آمریکا برای احیای خط لوله نفت عراق-سوریه جهت دور زدن تنگه هرمز فشار می‌آورد  واشنگتن در حال هماهنگی مذاکراتی برای احیای خط لوله نفت متروک عراق-سوریه است تا مسیر صادراتی امنی به سمت مدیترانه ایجاد کند که نفوذ استراتژیک تهران را تضعیف نماید.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18814" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18813">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پیشتر گفته بودم که یکی از انگیزه های اسراییل از تعقیب پروژه تغییر رژیم در ایران ایجاد یک کریدور داوود بزرگ است که او را از امتداد آویزان بودن به آمریکا برای تامین امنیت ملی اش بی نیاز کند.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18813" target="_blank">📅 10:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18812">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">چرا درگیری بعدی ایران و آمریکا احتمالاً جهش تاریخی نفت را تکرار نمی‌کند؟   درگیری نظامی میان ایران و آمریکا همواره یکی از بزرگ‌ترین ریسک‌های ژئوپلیتیکی بازار انرژی بوده است. هرگونه تهدید علیه تنگه هرمز، مسیر عبور بخش قابل توجهی از صادرات نفت خلیج فارس، در…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18812" target="_blank">📅 10:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18811">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">منوچهر متکی:  باید برویم پایگاه های آمریکایی ها در منطقه را تصرف کنیم و بعدش صد نفر از سربازان شان را اسیر کنیم بیاوریم ایران!</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/18811" target="_blank">📅 03:16 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

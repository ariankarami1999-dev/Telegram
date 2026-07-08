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
<img src="https://cdn4.telesco.pe/file/Q5bQerLrruWcGnfcM4v_BY8UMdOi70z9JWx__wsBi80nM3yiHVvOT3lgG9jgki6p7RCn5vznReU25PHUM_lvD-rMvj4Y7EaiLb1afDicLOc0dD3RYE6hKA4GsJqP8hC1Sm1UeScdswNAhsHFsPtp-S-x6R15YiMKz-CVnBna9QqwnLxySnb_0KHxDWjNUHmk4MRx14HMylMIxH36qE7S7sXQIfMknenwz5qMTAYuUPmaFMOfOobYb7uuD3aG3HafYwibTiG5p26N9KZrhrX0olPQiNwqG-iPC50-vESL9zm6ep3CrxDtrDgXnveMhtr5hELgfawoNxeiw7h0_KvVIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 13:38:29</div>
<hr>

<div class="tg-post" id="msg-18347">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">عراقچی را در ایران فحش می دادند در عراق بشدت بزرگ داشتند!
فکر کنم عراقی ها چون دیده اند فامیلش عراقچی است فکر کرده اند ولی خب.</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SBoxxx/18347" target="_blank">📅 13:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18346">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ:
«ایران سعی کرده من را بکشد، اما من تا حالا خوش‌شانس بوده‌ام... فعلاً. من در تک‌تک فهرست‌های آن‌ها هستم. و تا اینجا، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد.</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SBoxxx/18346" target="_blank">📅 13:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18345">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دوستان درباره تن ماهی پرسیده بودند؛
به نظرم زود است و می توانید از مرداد هر هفته پله ای بخرید.
تصور می کنم هنوز ذخایر نفتی آمریکا پر نشده و انبارهای مهماتشان هم.</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/SBoxxx/18345" target="_blank">📅 13:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18344">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فوری | اردوغان: موضع قاطع ترامپ در مورد تلاش‌ها برای دستیابی به توافق با ایران قابل تحسین است.</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/SBoxxx/18344" target="_blank">📅 12:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18343">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ :   تفاهم تمام شد، نمیخواهم تعاملی کنم</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/SBoxxx/18343" target="_blank">📅 12:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18342">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUOzMitXl2VKMkD9JV82oItzzDL1M8Hg3KZoQPw_j4HOHIpdUO9PYrqUY94h3gLPB7-J92I8md4aIEWWsTd5J14l9j1B1hDgYEGZ3Lm38KmQNt9X2azle94Z-fnyMUt-APcBFwv2YPC4URg5kT9mB4ShYUlBe00GxMbB7IT9wNaysneojQ221xGIgsdu1Wa0v06ueWThv8DfufI__k9rMlyLlWKxsYIGuTGRdaRjUFBoCAX0uUSR81ZNdrPx3V11hsc-D6YAb4LwqFG8ImSNP4DrAPpixSb32Vy-P7uPD9BxrAWke5ZJHPX-U0O44NZit_4UuYJBWUaYV2teugzYpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جولانی به آنکارا، ترکیه، سفر کرد تا در اجلاس 36ام ناتو شرکت کند.  قرار است او با ترامپ دیدار کند.</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/SBoxxx/18342" target="_blank">📅 12:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18341">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دلار خرید دارد همینجا با تارگت ۲۴۰ الی ۲۶۰ هزار تومان</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SBoxxx/18341" target="_blank">📅 12:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18340">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMNajRxu-8ScL8rUOhjOU1SfVwYBu68IBBsijMnzHRrK8XTK4EZoTJA10K1F_JyXczNbeDxHgz5DlX98qwwRpdgjUI9x5pv20uCqSqBonC681RD3OUkCFsHbmykbL1z7VO1o-0U-7LYTrVhzRmoSu9U0Qvf1g-gw9G7_y4FwboWrL1WaXeFV-lFl705E8fUM64_Hho5HkogMAzsm_bEYZLciBBwGRbTKP_eDuRoeKyvzXpzk3j1trIQU6aCssrdhYAJyqs_NXfD9neFRXyv7EeEVA1fD9b-mDkoRRSs8t63ZmObdbfco7RUAzRIZ0cNMGx7q3v3VptuGqCZRGT0qHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پهپاد آمریکایی توسط پدافند ایران سرنگون شد.</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SBoxxx/18340" target="_blank">📅 12:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18339">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وقتی در اجلاس ناتو در ترکیه این چنین صحبت می‌کند یعنی یا به من کمک میکنید یا گور پدر همه تان !</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/18339" target="_blank">📅 12:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18338">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ:   با اسپانیا حتی صحبت نکنید. آنها کاملاً ناامیدکننده هستند.  آنها آدم‌های بدی هستند.</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/18338" target="_blank">📅 12:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18337">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">همکاری نظامی اسرائیل-مراکش و پیام راهبردی به مادرید  همکاری نظامی اسرائیل و مراکش دیگر صرفاً یک رابطه تجاری در حوزه صنایع دفاعی نیست؛ این همکاری به تدریج به یکی از مهم‌ترین مؤلفه‌های معادلات ژئوپلیتیکی غرب مدیترانه تبدیل شده است. از انتقال فناوری پهپادهای…</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/18337" target="_blank">📅 12:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18336">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این خبر از دید من مهم است و می‌تواند منجر به ورود باند جولانی به لبنان بشود</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/18336" target="_blank">📅 12:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18335">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اظهارات کامل ترامپ درباره رهبران ایران:  آنها دروغگو هستند، فریبکار هستند و آدم‌های بیمارند. آنها به مردم خود آسیب رسانده‌اند. تا به امروز، ۵۴۰۰۰ نفر را که در حال اعتراض بودند، کشته‌اند.  شما می‌دانید که وقتی مردم می‌پرسند چرا هنوز قدرت را به دست نگرفته‌اند؟…</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/18335" target="_blank">📅 12:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18334">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUgNaC3l-zaJwDFR9mBSuMglIvsSQ2lGMPWTAlIRYbFM1EdKpuEf2Tq_IghBxUYeo6q03GVzAAbu4Iq3zgMquz3lMM-TmEvL3M7o1a0xMBK5If7d7ZYjQBkJrGK1tLiksC1H7DUDRQvesD02puWnFyouRhmbjVlJUMWdcR5BmqHYJEeVbmzj_JfTDXs97NpKkSkxaH6F5QO3f2GAbpOMjMNa4KMUs-XbvfHQI1cvn5oKLE2Dyo470yWid_zgRE-0J7Z37TEKgyRRgJDozbirhI7nj1xO_aVLSaUWuUIpxsN5pwsgV-wjJe3ytCK4fpueaFfRXuVtiOiYBnSZOUFzCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک در سطح بسیار بالا قرار دارد و ریسک گریزی آشکاری در بازارهای مالی جریان دارد.</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/18334" target="_blank">📅 12:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18333">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ درباره اردوغان:
به نظر من، اردوغان هم از ایران خوشش نمی‌آید.
اردوغان شخصاً فردی عاقل است، و به نظر می‌رسد که ایرانی‌ها رفتارهای غیرمنطقی از خود نشان می‌دهند.</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/18333" target="_blank">📅 11:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18332">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اظهارات کامل ترامپ درباره رهبران ایران:  آنها دروغگو هستند، فریبکار هستند و آدم‌های بیمارند. آنها به مردم خود آسیب رسانده‌اند. تا به امروز، ۵۴۰۰۰ نفر را که در حال اعتراض بودند، کشته‌اند.  شما می‌دانید که وقتی مردم می‌پرسند چرا هنوز قدرت را به دست نگرفته‌اند؟…</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/18332" target="_blank">📅 11:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18331">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اظهارات کامل ترامپ درباره رهبران ایران:
آنها دروغگو هستند، فریبکار هستند و آدم‌های بیمارند. آنها به مردم خود آسیب رسانده‌اند. تا به امروز، ۵۴۰۰۰ نفر را که در حال اعتراض بودند، کشته‌اند.
شما می‌دانید که وقتی مردم می‌پرسند چرا هنوز قدرت را به دست نگرفته‌اند؟ چون آنها نمی‌توانند قدرت را به دست بگیرند، زیرا کشته شده‌اند.
آنها آنها را کشتند. هیچ‌کس نمی‌تواند قدرت را به دست بگیرد، زیرا آنها سلاحی ندارند، در حالی که طرف مقابل مسلسل دارد. و سپس آنها به کشتار ادامه می‌دهند. رسانه‌ها این موضوع را پوشش نمی‌دهند.
من به مذاکره‌کنندگان عالی‌رتبه‌مان اجازه خواهم داد که در صورت تمایل به صحبت ادامه دهند، اما من این موضوع را بعید می‌دانم.</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/18331" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18330">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ :
تفاهم تمام شد، نمیخواهم تعاملی کنم</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/18330" target="_blank">📅 11:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18329">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مواضع جدید ترامپ درباره ایران:  «آنها یک مشت آشغال هستند. من اصلاً از آنها خوشم نمی‌آید. ما وقت زیادی را با آنها تلف کرده‌ایم. آنها بی‌کفایت هستند. ما فقط باید کار خودمان را بکنیم. آنها می‌خواهند رهبر ایالات متحده - من - را از بین ببرند. من سال‌هاست که نفر…</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/18329" target="_blank">📅 11:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18328">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مواضع جدید ترامپ درباره ایران:
«آنها یک مشت آشغال هستند. من اصلاً از آنها خوشم نمی‌آید. ما وقت زیادی را با آنها تلف کرده‌ایم. آنها بی‌کفایت هستند. ما فقط باید کار خودمان را بکنیم. آنها می‌خواهند رهبر ایالات متحده - من - را از بین ببرند. من سال‌هاست که نفر اول فهرست آنها هستم. ما باید سرطان را زود از بین ببریم. من اینطور احساس می‌کنم.»</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SBoxxx/18328" target="_blank">📅 11:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18327">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">️خبرنگار:واکنش شما به حملات اخیر آمریکا به ایران چیست؟
مارک روت، رییس ناتو:به نظر من، این اقدام کاملا ضروری بود. ایران، آتش‌بس را نقض می‌کند</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/18327" target="_blank">📅 11:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18326">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">صدای انفجارات در بوشهر</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SBoxxx/18326" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18325">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سپاه پاسداران در پاسخ به حمله آمریکا، یک حمله هماهنگ موشکی و پهپادی به ۸۵ هدف نظامی ایالات متحده از جمله ناوگان پنجم، پایگاه هوایی علی الصالح در کویت و بندر سلمان انجام داد.</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/18325" target="_blank">📅 10:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18324">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">به نظرم این منجر به جنگ نمی‌شود.  فقط از کنار دکل های سیریک و اربیل فاصله بگیرید.  سپاس</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SBoxxx/18324" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18323">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhMaCJchD1BX2sbbs9BzzXxdJCNFuLbcBHIg0TlB3mS6T3C7Ak0KO4Xho1fW_njHgjwp4RCGnD5BMiMzYHCHHOZcZQUflnaHYewsvsVndsxAyIaRO9R5W8yi_p0FSHkzPFupeXf7uv3fBPyqFwymGqB0w6xLUXmRp58qKufsv58oIzFr5XYZJlgRh1BolKCVKTs4ZQcYuTtP-HF0vLR0PCHyW65B3xDcR-41sItvRLY2DZVFPouToRt2Oeq8g1EpRg2rhT0CxInjF2dLiVlNIeGyrQ3a8TQ4c7cxvH8dS4eng8JT4XpUjNXbQpDFwTuozrKYcXBVNmA11es1nwoPIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/18323" target="_blank">📅 10:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18322">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">CNN:
وزیر دفاع ایالات متحده پیتر هگستت‌ در روز سه شنبه سفر اول خود را به اسرائیل انجام خواهدداد.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/18322" target="_blank">📅 02:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18321">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8HcbpOBs3gN2wHfCyWP-u48dnGb-avIqd1nAuMtD0bUvEBzPuwhkN4QihHq86BmB17sX7aOM2kLIn6XEskp0POTd3rJbU0v9ZHDetK2eROQj5P4WL4OvS0ehhisishXTtr3hkAZ1byrHGToPaeTx6QY4UC1raKyAwCYNY1i5rqILBq0c3IgHUR7AWCbDxnYfgOcJ-bqqOKT-36SY017ZZpldT-0z9JnKJRWlXHJPHGi9IkFVbL9rdTPugrBmp8_HsECyhq9uVWzRW1YXJQR42kRXju3CndMUJded-3_T7C7l0O54HT4r_RMLzLIYJsDehXJIr6c_C3hrS_0lMrJPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی گفته بود حالا که ترامپ در ترکیه است او را ترور کنیم! ترامپ هم از همان ترکیه دستور حملات را صادر کرد!  ایشان را بیدار کنید خودش برود دکل سیریک را نگه دارد.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/18321" target="_blank">📅 01:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18320">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حملات ناوهای جنگی آمریکا در ایران، اهدافی مانند سامانه‌های پدافند هوایی، سیستم‌های نظارتی ساحلی، موشک‌های زمین به هوا، موشک‌های کروز ضدکشتی و محل‌های پرتاب پهپادها را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18320" target="_blank">📅 01:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18319">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مقام آمریکایی به CNN :
حملات به ایران برای تنبیه‌ست!
نه مقابله‌به‌مثل؛ و این حملات فعلاً ادامه خواهد داشت.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/18319" target="_blank">📅 01:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18318">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awrE11cXWU2Llr2xtKy-Oxa1DzXV5szuwJzYXC22oUTC3tM6x_HxnNTTSw_7EXrm8DTurdEBn3BsqyqnJVOzAdRlTOY9CJVltVpt-72expzrCgFoIhsf9t-mvkwCVpIM8bMIXbu3uaAWoDHnwfGiGUuKkPr2oGdU22U2PXtluXn4aao50CIECeNVXD315tI3yHmhPs1i8miJPJkpM2p9XSiQs5v_4veztdQZ-aQsU24d2QZHJZkerqyxqSomk27e4H0zj2Gpi1aM3M4PoAYE5TpiaG5x9UsdBsslOyARWY9vLXM_osNDT_xqsFxwbbQeJPX_ZCul3UbE0xTcanu8ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدماتمان اینطوری است که کشتی هندی با ملوانان بنگلادشی متعلق به میلیاردر یونانی دارد راهش را می رود، بچه های ما به کاپیتان آن زنگ می زنند که یا بیا از نزدیکی سواحل ما رد شو یا ما ترتیبت را می دهیم بعد کشتی وارد آب های ما می شود و ما اسکورتش می کنیم تا بچه های…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/18318" target="_blank">📅 01:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18317">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/782b3ef401.mp4?token=ElZja5AFZ2cgPPflnu0BO_cq427ShI4S9-74srxdyS2Wkp93-b2zPeRl6cuPsV4FjSCUYhUP0hWZvrhugY6s4SnXkHjroXvfIMgbefGnpXrDfPESrWZ0Ts6cirhmYzs4qGOGpy9shaHfFPymEL5UzOyc9_HGv1WqdfCR_Orljsc_ibHYGcKWx-18OrywexT50yk66QF1rnnzc0eew1eR9Wa9RzOfq5FlBH0dT7T5tAunSaUUMFYq8RGipWooM7dEzlf2YXTygpwD_GRsc82ml92M1vheUKT8I9_k198wewQR2vmxDD8obCvbjqUrpUvE67kFLogeV1UTm4m0DJDHpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/782b3ef401.mp4?token=ElZja5AFZ2cgPPflnu0BO_cq427ShI4S9-74srxdyS2Wkp93-b2zPeRl6cuPsV4FjSCUYhUP0hWZvrhugY6s4SnXkHjroXvfIMgbefGnpXrDfPESrWZ0Ts6cirhmYzs4qGOGpy9shaHfFPymEL5UzOyc9_HGv1WqdfCR_Orljsc_ibHYGcKWx-18OrywexT50yk66QF1rnnzc0eew1eR9Wa9RzOfq5FlBH0dT7T5tAunSaUUMFYq8RGipWooM7dEzlf2YXTygpwD_GRsc82ml92M1vheUKT8I9_k198wewQR2vmxDD8obCvbjqUrpUvE67kFLogeV1UTm4m0DJDHpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی انفجارات پیاپی در بندرعباس!</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18317" target="_blank">📅 01:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18316">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نفت را بای داریم پدرسگ ها</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/18316" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18315">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مقام آمریکایی به PBS: «ایران به‌وضوح نشان داده که به هشدارها توجهی نمی‌کند. ما در حال افزایش شدت واکنش و فشار خود هستیم.»</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/18315" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18314">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مقام آمریکایی به PBS: «ایران به‌وضوح نشان داده که به هشدارها توجهی نمی‌کند. ما در حال افزایش شدت واکنش و فشار خود هستیم.»</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/18314" target="_blank">📅 01:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18311">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رسایی گفته بود حالا که ترامپ در ترکیه است او را ترور کنیم! ترامپ هم از همان ترکیه دستور حملات را صادر کرد!
ایشان را بیدار کنید خودش برود دکل سیریک را نگه دارد.</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/18311" target="_blank">📅 01:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18310">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFR9DiNOVLVZmaikZD7bdBTU-uBANzGwtJpF_uWjc24Zq2Xbrhz4nXoVmqK8Wgdn28KAQUD00KYLf8DZFOSDFn51qAy92QtpwKs6FQNDGc0WaKcCWN47u1xS64sU82k-JSrRii2-rZSFjYyfbu3fIOVdZha6JNtuMp2dw_EIkn0Vhty9Lkv3ES09xjIj3CVMv0n732CQ17C-AFLIiiDKaRnewgGvx9-zY1C3TykgId5WmX8wEuwG_bPEWUYkYPLWFQULgk-PeEXIwXmJMDuapSgx7c7j5IabKXNV4hZQX02VWVc8YedpEl3ReHdAhodYAVK4S6wQoTFZRRLQcsBeBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چه دکل سگ جانی است خدا میداند</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/18310" target="_blank">📅 01:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18309">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L47QwaDvTjL-Lj8dZdjDEOG-Q0e2WMm7BAHxG7eORI79NWctj0k8kFnzsi_y7rqW0N5t1SL9Qs46olFoIJOzKR0SuXPexBEPQHc25RRk0Zdd4YiQ6D6ijEOwNjE5AnY7fnfTKpzRQRrw7Cyd6pG5Qu0u0IekPprBr1WwL7vvB-p9jhUJYpKSVO5lywYiGv2h_zyDedy-wPV89b5pLmigBv4kEGfP839XZY7ndCa5_dLawnoBPz605c8b8lMdRW6KYhMvpqiIm54RX03MwNBJIuQj9mCZ_5ps3PAKcHe_ENSoK6FxDOoY1PXWly1iLphlu4h3fO90p-9AqIm5gIvfPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویری از انفجار در پایگاه دریایی سپاه</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/18309" target="_blank">📅 01:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18308">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">باز  هم اشتباه محاسباتی منتهی باز هم از طرف ما!  بارها دیده اند ترامپ اساساً اهل محاسبات نرمال و عرف پذیرفته شده و اجماع-محور نیست باز خریت او را تست می کنند.</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/18308" target="_blank">📅 01:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18307">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">باز  هم اشتباه محاسباتی منتهی باز هم از طرف ما!
بارها دیده اند ترامپ اساساً اهل محاسبات نرمال و عرف پذیرفته شده و اجماع-محور نیست باز خریت او را تست می کنند.</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/18307" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18306">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اژدهای بندر را بیاورید ببینیم منشا صدا کجاست</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/18306" target="_blank">📅 00:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18305">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گویا ارتش آمریکا اشتباهی یک هواپیمای پاکستان را زده و سقوط کرده است</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/18305" target="_blank">📅 00:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18304">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سنتکام می‌گوید ایالات متحده پس از حمله ایران به سه کشتی تجاری در تنگه هرمز، حملات گسترده‌ای را علیه ایران انجام داد.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/18304" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18303">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">منابع محلی گزارش دادند که آمریکا به یک دکل مخابراتی در محدوده سیریک حمله کرده است</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/18303" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18302">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">به نظرم این منجر به جنگ نمی‌شود.  فقط از کنار دکل های سیریک و اربیل فاصله بگیرید.  سپاس</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/18302" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18301">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اسراییل هم شرایط را مناسب دیده و شروع به پیشروی با زرهی در جنوب لبنان زیر پوشش آتش هوایی کرده</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/18301" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18300">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">به نظرم این منجر به جنگ نمی‌شود.  فقط از کنار دکل های سیریک و اربیل فاصله بگیرید.  سپاس</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/18300" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18299">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">به نظرم این منجر به جنگ نمی‌شود.
فقط از کنار دکل های سیریک و اربیل فاصله بگیرید.
سپاس</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18299" target="_blank">📅 00:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18298">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آن 2 بند اول هم که از هنوز از تنبان توافق گشوده نشده صرفاً در برابر بازگشایی تنگه هرمز بوده.   به زبان ساده تر، یعنی ایران تنگه هرمز را بست که از کله زرد امتیاز بگیرد، اما او یک محاصره دریایی در پاسخ اجرا کرد. حالا ایران امتیازاتی را که می خواست نگرفته اما…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18298" target="_blank">📅 23:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18297">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دکتر محسن رضایی:   کاملا مشخص است که آمریکا مذاکرات را با شکست مواجه خواهد کرد</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18297" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18296">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دکتر محسن رضایی:
کاملا مشخص است که آمریکا مذاکرات را با شکست مواجه خواهد کرد</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18296" target="_blank">📅 23:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18295">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وزیر خارجه ایران:   کشتی‌های تجاری که مسیرهای هماهنگ‌نشده‌ای با ایران دارند یا دستکاری ردیابی کشتی را انجام می‌دهند، با خطرات مواجه شده و تلاش‌های ایران برای تسهیل عبور ایمن از تنگه هرمز را مختل می‌کنند.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18295" target="_blank">📅 23:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18294">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یکی از این تعهدات  این است که کشتی هایی را که از مسیر عمان میگذرند میزنیم تا بفهمند مسیر جنوبی ناامن است و از سمت ما رد شوند</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/18294" target="_blank">📅 23:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18293">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وزیر خارجه ایران: ایران در حال انجام تعهدات خود بر اساس تفاهم‌نامه در مورد اقدامات لازم برای مدیریت تنگه هرمز است.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18293" target="_blank">📅 22:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18292">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سپاه کشتی بعدی را هم در هرمز زد و نفت صعودی شد</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18292" target="_blank">📅 22:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18291">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سپاه کشتی بعدی را هم در هرمز زد و نفت صعودی شد</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18291" target="_blank">📅 22:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18290">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ایالات متحده مجوز فروش نفت ایران را لغو کرد</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18290" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18289">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRed Lion Corps(M)</strong></div>
<div class="tg-text">بازی فوتبال تیم مصر و آرژانتین، چیزی تو مایه های جنگ یوم کیپور برای مصری ها شد. کمی اولش داشت خوش می‌گذشت بهشان که زمین و زمان بهم ریخت</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18289" target="_blank">📅 21:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18288">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بح بح!
موشهای نیل به دامان طبیعت برگشتند</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/18288" target="_blank">📅 21:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18287">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خبرنگار سی‌ان‌ان:
«ترامپ در حال بررسی دادن اف-۳۵ به ترکیه است».
نتانیاهو
:
«این تعادل قدرت در خاورمیانه را نابود می‌کند. من این کار را نمی‌کردم».</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/18287" target="_blank">📅 21:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18286">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/18286" target="_blank">📅 20:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18285">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">امروز پوتین با لباس نظامی با رسانه ها گفتگو کرده و عملاً می خواهد از اعتبار و جایگاه خود دفاع کند.  حس خوبی ندارم....</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18285" target="_blank">📅 20:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18284">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdb88acd05.mp4?token=a73AFqCjiiSNpNWtpuFIT4lux6WWw7saBKtzDd7ZYzOW5JUnEQgHeZXgZrJZqohDYdBHfgTK_QT9_5T1qA8r8i7zryoX-bokCPe665131MIe_RyMFyAu6wgT68Xam0vH_zZJwp5OyW_D-pJ-iW5qjY-jOB7Eat11W2ptSOFIJeOjiE4M5U4VbAYuyKziAzFOSlWJLDhBG1fBoyqLoc1m33HHdy6V0QwKzzLgU9ajjLrp9Bhk4WMIaWOglrGgAWwDk7XWIYLdS9JPqHUvME7C6cbKGM6xlFVTtnZnalt8hQ9AEBNOLV4hUyRnlYQpr3jyGIIM75dWxO1gwPO-KZFG4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdb88acd05.mp4?token=a73AFqCjiiSNpNWtpuFIT4lux6WWw7saBKtzDd7ZYzOW5JUnEQgHeZXgZrJZqohDYdBHfgTK_QT9_5T1qA8r8i7zryoX-bokCPe665131MIe_RyMFyAu6wgT68Xam0vH_zZJwp5OyW_D-pJ-iW5qjY-jOB7Eat11W2ptSOFIJeOjiE4M5U4VbAYuyKziAzFOSlWJLDhBG1fBoyqLoc1m33HHdy6V0QwKzzLgU9ajjLrp9Bhk4WMIaWOglrGgAWwDk7XWIYLdS9JPqHUvME7C6cbKGM6xlFVTtnZnalt8hQ9AEBNOLV4hUyRnlYQpr3jyGIIM75dWxO1gwPO-KZFG4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک تروریست و یک شیفته تروریست در حال امردبازی</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18284" target="_blank">📅 20:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18283">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دبیرکل ناتو در مورد ترامپ:  من از این مرد خوشم می‌آید.  به نظرم کاری که او برای ناتو انجام می‌دهد خبری عالی است زیرا، بله، یک تهدید روسی وجود دارد، اوکراین وجود دارد، بنابراین ما در هر صورت مجبور بودیم در اروپا گامی برداریم.  اما او چیزی بود که برای ایجاد…</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/18283" target="_blank">📅 18:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18282">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">روته، نماینده ناتو در آنکارا:  ما روز سه‌شنبه در مجمع صنایع دفاعی، ده‌ها میلیارد دلار قرارداد جدید را اعلام خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/18282" target="_blank">📅 18:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18281">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR_cl9UBAnFiVTCL9PG9eqq5g4DVEw_vSNhg1girVkj2aeUzzZYqDFu9Cir0VlS_NoBWnVDOfc3gd9g5aZ1FHrynHZ_zDpEgxR3atZVYm9VEnXh5Em8sMvHZ5W865e9NokwxgPDdV8q4DuNvEZ4TYYIFFOhR5As1e4p9JgK_wjzi3704qtbb3ep9ZF2Tqyup43USofGcRRjOqQ47hqKfX5kOcXmqDKiPcnAdBYGb_wm3sdolUZXo32MveeGjRqHf4i4bVd1E3ePt3XRXQR451bF4rK0ydb9oPQQEw55UklqD5PhUVvB3LzuhGarjYNFn7yOamDYfG7gl424H3Ug7qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه کشتی بعدی را هم در هرمز زد و نفت صعودی شد</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/18281" target="_blank">📅 18:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18280">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lW5piiOrtAOHf1W9GVWcJ7ZSQBrIeUI0Q4Um7LFpQxBouQcp7AoP4UOwMGBai5i2e6VNBhV4a_xZ1bPno14F9vOyJOoEMthjSUw9Ghfj3I95qDbRrIgg24xdim55XtUT9o2RbwuX1mejXGG_YaRevzDVdBrPXfQ6prt8bIT80nFC8f0xBthfftFaIVXPmc3B-Iu7X9TkKi0u1KXQ1j8Jf00sreTxVLDVsl35Zc4F6iJHKhHravPPCIcqnlbSc-r88G6dtzY2hmsvzMnOBcdqrW59mAiXGa0zIvCnKUvtcKLl4xmaGlSualymqjQ-7J9jHd_VhZV31RsL5396tLBNpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">90 درصد این دولت ها را زردپوست هایی تشکیل دادند که از دید چهره و ریختار هیچ شباهتی به این دلقک های اردوغان نداشته اند.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/18280" target="_blank">📅 18:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18279">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سیرک جدید اردوغان!  لباس‌های تشریفاتی که نمادی از ۱۶ دولت بزرگ ترک در طول تاریخ هستند، در محوطه ریاست جمهوری مشاهده شدند و در صف ایستاده بودند تا از رئیس‌جمهور ایالات متحده، ترامپ، استقبال کنند.</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/18279" target="_blank">📅 15:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18277">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DSxrD3zf_TYxQFFJFdJsK4vp0MAvzcJ7onLrJ1DKrxg6ag-a2GbqWALCqT5JXWqvF93J_PqpTKtwP7ngkX-PHiP-yfc6NqZb0f383BK4ss2RMVhzCSgfClxGInZ0l0i0UcAHeyHFJETje4s1NEKI3QGP1rQm4lQk5fnI0kXX8kLW3DFzBurG1NwAz9Wa7CUUU1xkq0_6CNYqBRxoUVECj92GGhkbZnYjYhwocLWTk-_kfU27oLRN-A9SOm7pS0692GIZFG8TGIwooYK13OS9VXCGgJqY_4eWFnby1fmOVDRW4xVehMZ9DD89VZaLpE8EPK56fVqLEmkk--1Knp_zyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXnIKZ9x7noWcnwrIbPqo_6xUfs6r_gI9_6CQhmcj6x-Q3om4FjSqM3ahl9CxPftozl7aMAza83PpnN2-sIKspd8Gkc1HL4mU37qChnGY9HfdNcwz6wflsBnhlheYl-NREVlcaOeoiG4BA1R0zJDCi8K9dZoBwf4zRu-YwCTrGj1edrG3F6XTNCjXQpZabWPpwEXkiRx3OJJMSoAIYKzXzoE-Avl371YRHEgkly0LGSI-RrMGD0QA81pU75_00-VvVhkrLcSxLEc6AFPJg8fzn4ZtfahiyzxhPhfuOakiK7nnZzGA7CvVZCptvzfQBecuEubwGcbHIQqwJdq_B7omg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سیرک جدید اردوغان!
لباس‌های تشریفاتی که نمادی از ۱۶ دولت بزرگ ترک در طول تاریخ هستند، در محوطه ریاست جمهوری مشاهده شدند و در صف ایستاده بودند تا از رئیس‌جمهور ایالات متحده، ترامپ، استقبال کنند.</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/18277" target="_blank">📅 15:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18276">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حماس رسما انحلال دولت خود را اعلام کرد.</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/18276" target="_blank">📅 14:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18275">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حماس رسما انحلال دولت خود را اعلام کرد.</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/18275" target="_blank">📅 14:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18274">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حماس رسما انحلال دولت خود را اعلام کرد.</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/18274" target="_blank">📅 14:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18273">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWxoWru0l2mVI5lS4hq0IByS3rhWrCSBoUnVFMof_2e8bZBK4Nn9a8U_RItT7p4szdjo0_6OpOxEkJyBmNRbTULaWiiRLFvUEG3NGaAc96xyQXbyKZZpn1Jwj0mplS9psBfyzNsTSEXcjbnjQIfrPHU2d8hU-DDXjmMzHPWeUca3pZgql_k7xHhTpIZJBlViy20yKnChk178jR6-djpf5YZR3Sf2g-gk-s9lYHh083tRQVCmO4AQljvkCLIevtVsfKSmzjsF2mj9QCOZHCNihfu4TwjtZ6qPH9djf4Ba1A5e0srV3FrRCmYlsIlRU_scwpn0LtB0bwHaCLk3yHO2_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایه کشتارهای قومی بر اتحادهای ضدروسی
تنش‌های اخیر میان لهستان و اوکراین نشان می‌دهد که حتی نزدیک‌ترین متحدان نیز نمی‌توانند از سایه تاریخ بگریزند. در حالی که دو کشور از زمان آغاز تهاجم گسترده روسیه به اوکراین در سال ۲۰۲۲ همکاری‌های نظامی، امنیتی و سیاسی بی‌سابقه‌ای را تجربه کرده‌اند، اختلافات مربوط به حافظه تاریخی بار دیگر به سطح روابط دوجانبه بازگشته است. مصاحبه اخیر کیریلو بودانوف، رئیس اطلاعات نظامی اوکراین، با شبکه RBC-Ukraine نیز بازتاب همین واقعیت بود. بودانوف در واکنش به آنچه «اقدامات نابالغانه» لهستان خواند، تأکید کرد که کی‌یف نباید با واکنش‌های شتاب‌زده تنش را تشدید کند و امیدوار است پس از دوره‌ای از افزایش تنش، دو کشور به سمت کاهش تنش حرکت کنند.
زمینه این اظهارات به مجموعه‌ای از تحولات اخیر بازمی‌گردد. در آستانه یازدهم ژوئیه، سالگرد
کشتار ولین
، فضای سیاسی لهستان بار دیگر تحت تأثیر مطالبات مربوط به بازخوانی گذشته قرار گرفته است. هم‌زمان، اقدام اوکراین در نام‌گذاری یکی از یگان‌های نظامی خود به نام ارتش شورشی اوکراین (UPA)  واکنش‌های تندی را در ورشو برانگیخت. برای بخش بزرگی از جامعه لهستان، UPA  نه نماد استقلال‌خواهی، بلکه مسئول یکی از خونبارترین فجایع تاریخ معاصر این کشور است. در مقابل، بخش قابل توجهی از جامعه اوکراین این سازمان را نماد مبارزه برای استقلال در برابر سلطه شوروی می‌داند. همین تفاوت بنیادین در برداشت از تاریخ، بار دیگر شکافی عمیق میان دو متحد ایجاد کرده است.
ریشه این اختلاف به سال‌های جنگ جهانی دوم بازمی‌گردد. ارتش شورشی اوکراین (UPA) در سال ۱۹۴۲ به عنوان شاخه نظامی سازمان ملی‌گرایان اوکراین شکل گرفت. هدف اصلی این نیرو ایجاد یک دولت مستقل اوکراینی بود؛ دولتی که نه تحت سلطه آلمان نازی باشد و نه اتحاد جماهیر شوروی. اما در کنار مبارزه با این قدرت‌ها، UPA  وارد درگیری خونینی با جمعیت لهستانی ساکن مناطق ولین و گالیسیا نیز شد.
در سال‌های ۱۹۴۳ و ۱۹۴۴، نیروهای UPA مجموعه‌ای از حملات گسترده را علیه روستاهای لهستانی آغاز کردند. بسیاری از مورخان معتقدند هدف این عملیات‌ها حذف جمعیت لهستانی از مناطقی بود که ملی‌گرایان اوکراینی آن‌ها را بخشی از سرزمین آینده اوکراین می‌دانستند. اوج این خشونت‌ها در ۱۱ ژوئیه ۱۹۴۳، موسوم به «یکشنبه خونین»، رخ داد؛ روزی که ده‌ها روستای لهستانی به طور هم‌زمان هدف حمله قرار گرفتند. برآوردها نشان می‌دهد بین ۵۰ تا ۶۰ هزار لهستانی در منطقه ولین و در مجموع تا حدود ۱۰۰ هزار نفر در ولین و گالیسیا شرقی جان خود را از دست دادند. در مقابل، عملیات‌های تلافی‌جویانه نیروهای لهستانی نیز به کشته شدن چند هزار غیرنظامی اوکراینی انجامید، هرچند از نظر ابعاد و سازمان‌یافتگی، بیشتر پژوهشگران معتقدند خشونت علیه غیرنظامیان لهستانی بسیار گسترده‌تر بوده است.
همین گذشته، امروز نیز منشأ اختلاف است. پارلمان لهستان این کشتار را رسماً «نسل‌کشی» توصیف کرده و خواهان پذیرش کامل مسئولیت تاریخی از سوی اوکراین است. اما در اوکراین، اگرچه بسیاری از پژوهشگران وقوع جنایات گسترده علیه غیرنظامیان را می‌پذیرند، بخش مهمی از جامعه سیاسی همچنان UPA را نماد مقاومت ملی در برابر سلطه خارجی می‌داند و با اطلاق عنوان «نسل‌کشی» به این رویداد موافق نیست. این دو روایت متفاوت از گذشته، امکان دستیابی به یک حافظه تاریخی مشترک را بسیار دشوار کرده است.
با وجود این اختلافات، بعید است تنش‌های کنونی به فروپاشی همکاری راهبردی دو کشور منجر شود. لهستان همچنان یکی از مهم‌ترین مسیرهای انتقال کمک‌های نظامی غرب به اوکراین است و امنیت دو کشور به طور مستقیم با نتیجه جنگ روسیه و اوکراین گره خورده است. از سوی دیگر، ورشو نیز به خوبی می‌داند که تضعیف اوکراین، فشار امنیتی روسیه بر جناح شرقی ناتو را افزایش خواهد داد.
با این حال، تداوم این اختلافات می‌تواند پیامدهای ژئوپولیتیکی قابل توجهی داشته باشد. نخست، شکاف‌های تاریخی میان دو کشور می‌تواند انسجام سیاسی جبهه حامی اوکراین را تضعیف کند و روند تصمیم‌گیری در اتحادیه اروپا و ناتو را پیچیده‌تر سازد. دوم، روسیه همواره تلاش کرده است از اختلافات تاریخی میان کشورهای اروپای شرقی برای ایجاد بی‌اعتمادی و کاهش هماهنگی میان آن‌ها بهره‌برداری کند و چنین تنش‌هایی فرصت مناسبی برای عملیات اطلاعاتی و تبلیغاتی مسکو فراهم می‌آورد. در نهایت، اگر ورشو و کی‌یف نتوانند میان ضرورت‌های امنیتی امروز و اختلافات تاریخی دیروز تعادل برقرار کنند، یکی از مهم‌ترین شراکت‌های راهبردی اروپا ممکن است با چالش‌های فزاینده‌ای روبه‌رو شود؛ شراکتی که حفظ آن نه تنها برای دو کشور، بلکه برای معماری امنیتی کل قاره اروپا اهمیت اساسی دارد.</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/18273" target="_blank">📅 13:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18272">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انقلاب هوش مصنوعی و گلوگاه جدید آن؛ آیا آینده رایانش به مغز انسان وابسته خواهد شد؟   هوش مصنوعی در سال‌های اخیر، رایانش را از یک فناوری پشتیبان به یکی از مهم‌ترین منابع راهبردی جهان تبدیل کرده است. هر نسل جدید از مدل‌های هوش مصنوعی به توان پردازشی بیشتری نیاز…</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/18272" target="_blank">📅 12:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18271">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انقلاب هوش مصنوعی و گلوگاه جدید آن؛ آیا آینده رایانش به مغز انسان وابسته خواهد شد؟   هوش مصنوعی در سال‌های اخیر، رایانش را از یک فناوری پشتیبان به یکی از مهم‌ترین منابع راهبردی جهان تبدیل کرده است. هر نسل جدید از مدل‌های هوش مصنوعی به توان پردازشی بیشتری نیاز…</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/18271" target="_blank">📅 12:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18270">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kw6DKe2SZ3TAZGOvKGA_xoyprf09QU_6qDddm40tFA_KByBrbzfEWdMJyI1uGMV-BzdbibMivL502QRYIK9v4zLMQXIqJprGRApsOtTSwnK0SOlxXg_QXUz0S4j0qgoW5-vnKtgbGKqER6ZkzXQTu2dPISCNGeAoAlEvM8OArUUd59JI99SaQiVlpmePxUaW5VD0eQdF8wtoUnige-y5MNuPC4hcPH9CXMbMnkoCiauTQ_S4mYXBrwQeRAz5oJ4qywmSkjPiSUL2r_ItfkqAb4RY2T7Z3cV3k8a26vbEzjDbYHNbAYfhrxV_YFdHrfPrSBKBJk-AgutA2XXrRob9nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقلاب هوش مصنوعی و گلوگاه جدید آن؛ آیا آینده رایانش به مغز انسان وابسته خواهد شد؟
هوش مصنوعی در سال‌های اخیر، رایانش را از یک فناوری پشتیبان به یکی از مهم‌ترین منابع راهبردی جهان تبدیل کرده است. هر نسل جدید از مدل‌های هوش مصنوعی به توان پردازشی بیشتری نیاز دارد و میلیون‌ها درخواست روزانه کاربران، فشار بی‌سابقه‌ای بر مراکز داده وارد می‌کند. نتیجه این روند، رشد سریع مراکز داده و افزایش چشمگیر مصرف برق آن‌ها در سراسر جهان است.
این تحول باعث شده است که انرژی از یک عامل جانبی به یکی از مهم‌ترین چالش‌های توسعه هوش مصنوعی تبدیل شود. در بسیاری از کشورها، شبکه‌های برق برای تأمین نیاز مراکز داده جدید با محدودیت مواجه هستند و شرکت‌های بزرگ فناوری سرمایه‌گذاری‌های گسترده‌ای در نیروگاه‌های هسته‌ای، انرژی‌های تجدیدپذیر، سامانه‌های خنک‌سازی پیشرفته و طراحی پردازنده‌های کم‌مصرف انجام داده‌اند. امروزه دیگر تنها پرسش این نیست که چگونه پردازنده‌های سریع‌تر ساخته شوند، بلکه این است که چگونه می‌توان انرژی لازم برای به‌کارگیری آن‌ها را فراهم کرد.
در چنین شرایطی، توان محاسباتی به یکی از مهم‌ترین منابع راهبردی جهان تبدیل شده است؛ منبعی که می‌تواند بر رشد اقتصادی، پیشرفت علمی، توان نظامی و رقابت میان قدرت‌های بزرگ تأثیر تعیین‌کننده‌ای داشته باشد. از این منظر، رقابت آینده تنها بر سر منابع انرژی نخواهد بود، بلکه بر سر تولید توان پردازشی نیز خواهد بود.
همین مسئله موجب شده است که پژوهشگران به دنبال الگوهای کاملاً جدیدی برای رایانش باشند؛ الگوهایی که بتوانند با مصرف انرژی بسیار کمتر، توان پردازشی بالایی ارائه دهند. یکی از جذاب‌ترین این مسیرها، رایانش زیستی یا Biological Computing است.
مغز انسان نمونه‌ای شگفت‌انگیز از یک سامانه پردازشی بسیار کارآمد محسوب می‌شود. این اندام تنها با مصرف حدود ۲۰ وات انرژی، وظایفی بسیار پیچیده مانند یادگیری، تشخیص الگو، تصمیم‌گیری و پردازش هم‌زمان حجم عظیمی از اطلاعات را انجام می‌دهد. در مقابل، آموزش یک مدل پیشرفته هوش مصنوعی ممکن است به هزاران پردازنده گرافیکی نیاز داشته باشد که هفته‌ها یا حتی ماه‌ها به‌صورت مداوم کار می‌کنند و انرژی بسیار زیادی مصرف می‌کنند.
همین تفاوت چشمگیر باعث شده است که برخی مراکز تحقیقاتی، امکان استفاده از نورون‌های زنده، بافت‌های عصبی و اندام‌واره‌های مغزی را برای انجام برخی وظایف محاسباتی بررسی کنند. هدف این تحقیقات، ساخت سامانه‌هایی است که بتوانند از ویژگی‌هایی مانند پردازش موازی، یادگیری تطبیقی و بهره‌وری فوق‌العاده انرژی در سامانه‌های زیستی بهره ببرند.
البته این فناوری هنوز در مراحل ابتدایی قرار دارد و فاصله زیادی تا کاربرد عملی و جایگزینی رایانه‌های مبتنی بر سیلیکون دارد. افزون بر این، مسیرهای دیگری مانند رایانش فوتونی، تراشه‌های نورومورفیک، شتاب‌دهنده‌های اختصاصی هوش مصنوعی و رایانش کوانتومی نیز با سرعت در حال توسعه هستند و هر یک می‌توانند بخشی از نیازهای آینده را برطرف کنند.
با این حال، یک واقعیت بیش از پیش آشکار می‌شود: در عصر هوش مصنوعی، توان محاسباتی در حال تبدیل شدن به یکی از ارزشمندترین منابع راهبردی جهان است؛ همان‌گونه که نفت در قرن بیستم نقشی تعیین‌کننده در اقتصاد و سیاست جهانی داشت، ظرفیت پردازش اطلاعات نیز می‌تواند به یکی از عوامل اصلی قدرت در قرن بیست‌ویکم تبدیل شود.
اگر روند رشد هوش مصنوعی با همین شتاب ادامه یابد و محدودیت‌های انرژی به یکی از موانع اصلی توسعه تبدیل شود، احتمال دارد پژوهش درباره معماری‌های نوین، از جمله رایانش زیستی، از یک حوزه صرفاً دانشگاهی به یکی از مهم‌ترین عرصه‌های رقابت فناوری تبدیل شود. هنوز مشخص نیست که آینده رایانش بر پایه سیلیکون، فوتون، سامانه‌های کوانتومی، نورون‌های زنده یا ترکیبی از آن‌ها خواهد بود؛ اما آنچه روشن به نظر می‌رسد، این است که رقابت برای دستیابی به توان پردازشی بیشتر با مصرف انرژی کمتر، یکی از مهم‌ترین رقابت‌های علمی و فناورانه دهه‌های آینده خواهد بود.</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/18270" target="_blank">📅 12:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18269">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPPvflE-Z3s697RW_nlGHlZnYksslCHwipNBYfrJxnnmeubRv1EohhKteneyoPL3ToFGk3JFBLUb00Ee_72VM_xIQzSDOqR-r3k_vJ3fRSTNqScLk1vzbgUAb6GjOm2oM-rEp50e_2XzkPNdDNQHDMIbW-g7ISPW9Dm-aXyF6hJ1SF_KzCVK6V7aopUDDosW5eQg639IBEyB3CHPljHHUujZxKiZ4Da19X3NRQoF1ymEn4ELCzYuO2KZguu3ENyQy_sY4hikfs8uMg5zm3YxCQebbqLj1YQWQRymMQcTbmwsGKiAjOKD41nCDWO2C_bd2pHSV0bSuBqO62bkEI43Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارهای پرشمار در دمشق نزدیک محل اقامت شیفته صبیه رفیق بهزاد.</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/18269" target="_blank">📅 12:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18268">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXqQ7BqQQYXX29_in3hoZkrd0Yr282itjzpXAD_uLmsD1HzPhFnytTlIOPvuj8ywKxVTUWnCmvCx48VHR4vhczT9QP3ZfSzKdHKpcwV-9WIgjSPt9l8QeMXaNezVb1hjYLN-ZFgFVWfU6w-HMsbSYbx7Z1htbEmKqolUxE6Ieg6BL-x_JA1shnLsEugOq7ELehdoZV1HLZCGhLBJ7L8LC8oMV3jK_bfVMakqWxLT7KlPRehInoMd7Huz5chmMXEFlDSZ0UFfuul_8eSNKSMyzRG4qVtJ0jK0p7AD4AI2DfEcWq6P7NtWMugde_d6xW1D367md3ISJL2CwmNkmXDnlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهید لاریجانی اصرار داشت با مال دیگران داماد نشوید ولی خب.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/18268" target="_blank">📅 11:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18267">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">راه‌حل شاید ملانیا باشد!   تهدیدهای تکراری ترامپ در مورد تخریب ساختارهای اقتصادی و زیربنایی ایران در صورت شکست مذاکرات، تنها کارکردش این است که جمعیت اصطلاحاً خاموش کشور را به حمایت از جمهوری‌اسلامی و بیزاری و نگرانی از آمریکا و اپوزیسیون وابسته به آن، ترغیب…</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/18267" target="_blank">📅 11:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18266">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">این زیدآبادی دستکم ۲ تخته اش کم است!</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/18266" target="_blank">📅 11:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18265">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">در سوریه، ایران و اسراییل مشترکا از گروه های ضدجولانی حمایت کرده و او را یک قاتل داعشی کت شلواری میدانند!</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/18265" target="_blank">📅 11:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18264">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGH6iG3ku8Ny_9Sf3bkaK2GLka8lf3iFyL-igqgVBpPG4d35sIPUSwomQqeTouvLkTamg0Fl-wGiI4yKNI50fJGM_eCf4IkZZ8oS6ZeUfcoYpM7I5fff8bA2rGYv9y1EUeo_4AHjRHziMdMEE1EH7TB-LJ49_9DKlHBJm56nPYfLbs7xtUM4wTDtoXZqXmDhduDBqLSMm-UcXiKEMntZ5Qr_plS971vOKNe-Z9dJQHQeI7iHgDzfhGaTdlIBWz2J0Awcw4m64v56GSic2ysKFSo2oTOT8X5hvXz-UN9cOBGPTvXXW2JnuG3W3jhwhttj7hwch_1RsAH3NS0vHmn-yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه پایین قرار دارد و ادامه شرایط نرمال پیش بینی می شود.</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/18264" target="_blank">📅 11:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18263">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18263" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 2  دوشنبه 6 جولای 2026</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/18263" target="_blank">📅 10:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18262">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">◆ روزگاری وقتی اف 14 فول تراتل روی دریاچه ارومیه پرواز میکرد ،نعره موتور تی اف 30 تا اتاق خواب مادر الهام علی‌ اف میرفت . اما امروز تاندر تحویل گرفتند و با وضعیت فعلی آسمان ایران،می‌توانند تا تهران بیایند سلفی در کابین بگیرند برگردند . این حجم از اختلافی که…</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/18262" target="_blank">📅 10:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18261">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromParvaz dar oj</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTUD-xuPmR5tcbWWmma9MCzqk0oPkh1XqH3yNNOHe_QOtsJP9BCbYCp8dyFyNnuxWGjxIf0l-AI4Jbpj60_8KbhlqCvpK6xuV9UfSPp9P6WJNdAtJB8K2TK4HC7V2OCfZcU5aCMOoemQXdLTciwO8i1oVb3QFDOlRZRK-GRR97Mt_F3w5yphID1uroWLS2Ri1BfW5arkbzKpg7N_vrtFiQZQZL5MGZa5aIGizRtYsb7SOjVwfE2c4ChwaLMXzQ8XvH08PDAq38-OhwpC6tDYsDTA7oanrrqfUXOCjROpekFtdSQhifEDQTythKdeaeqozil-OaXBpc7i7yi7gY4u9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◆ روزگاری وقتی اف 14 فول تراتل روی دریاچه ارومیه پرواز میکرد ،نعره موتور تی اف 30 تا اتاق خواب مادر الهام علی‌ اف میرفت .
اما امروز تاندر تحویل گرفتند و با وضعیت فعلی آسمان ایران،می‌توانند تا تهران بیایند سلفی در کابین بگیرند برگردند .
این حجم از اختلافی که افتاد واقعا خرابکاری نیست،شاهکار است!!!
@PARVAZDAROJ
| 𝐀.𝐑.𝐀</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/18261" target="_blank">📅 10:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18260">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">جمهوری باکو به برنامه اوکراین در زمینه پهپادها پیوست     معاون دبیر شورای امنیت ملی و دفاعی اوکراین، دیوید آلوویان، در مصاحبه با گاردین اعلام کرد که در ماه‌های اخیر، کی‌اف توافق‌نامه‌هایی در چارچوب برنامه Drone Deal با شش کشور امضا کرده است و به گفته او جمهوری…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/18260" target="_blank">📅 10:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18259">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جمهوری باکو به برنامه اوکراین در زمینه پهپادها پیوست
معاون دبیر شورای امنیت ملی و دفاعی اوکراین، دیوید آلوویان، در مصاحبه با گاردین اعلام کرد که در ماه‌های اخیر، کی‌اف توافق‌نامه‌هایی در چارچوب برنامه Drone Deal با شش کشور امضا کرده است و به گفته او جمهوری باکو نیز در میان این کشورها قرار دارد.  این برنامه شامل توسعه مشترک، تولید و صادرات پهپادهای اوکراینی و همچنین تبادل تجربه جنگی بین کشورهای شرکت‌کننده است.</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/18259" target="_blank">📅 10:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18258">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پاسخ دبیر شورای عالی امنیت ملی به ترامپ</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/18258" target="_blank">📅 09:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18257">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STiDMw3qlIR9zkrnxmYt8WnrJEnCU5tWBKOb0Rxg4BukGWHSVvyOGjPONOZp3WZtSsqNv2aCYqHoloFSBISxVP-7SktJ2UwXLRpIWSPdZ33MVyIWMme9nVS23hKFbSPJ8IWd9u8FacfTidxS0QOK3M5dP28yoUTIl1j9iLgjy5sAbi3kbsD2ItewkD3kZ3csNGtv16sz89Cb7TowrTAycSy9CQB6vNHCi1kxgwfAf61vQEfEs0zhHwkc4kD3Rb6Tx5BKRhrkO5J1qIDHxuEeXtt9mAvR_Y29FiL9rJ0XZxuG599RmqsluoDhqEQywJmUkRupW5Oqf5F-Ai0WX5F-9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ دبیر شورای عالی امنیت ملی به ترامپ</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18257" target="_blank">📅 09:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18256">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یک نفتکش در تنگه هرمز هدف حمله قرار گرفته است
مرکز عملیات تجاری دریایی بریتانیا: یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18256" target="_blank">📅 09:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18255">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مسئول آمریکایی به اکسیوس:
بیبی وعده‌های زیادی درباره جنگ با ایران داد که محقق نشدند.
اما چه کاری از دستمان برمی‌آید؟ او خواهد آمد. او وعده‌هایش را می‌دهد و سپس ما مجبور خواهیم شد همه چیز را بررسی کنیم.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18255" target="_blank">📅 00:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18254">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خیلی جالب است؛  از 6 کشوری که شدیدترین بحران های انرژی را تجربه می کنند، 4 کشور در منطقه ددخیز خواهرمیانه هستند و 3 تایشان (سودان، سوریه و یمن) در ژنده پارچه ای که به عنوان پرچم رسمی معرفی کرده اند، رنگ های نجس و نحس پان عربیسم (سیاه، سفید و سرخ) دارند</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18254" target="_blank">📅 20:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18253">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZoVqK61YpqjSLQ41k7OoskyzxHfyL7PQ4u7ItX5PT8G50KO7Jg9HC4Ph5N6rSEXlnqBMV89ztigKLIi9CoPRx8DihIRBk-S_QRHN02et_vgPxCLgAvx2vr8P_ks1nVrjJumlqQJXmY8rgAyH6q80yXPDS6CuXM8WgChW9I2GmgNmdYdkbZVlsTIDPNG4UYccRNn6cT6BzXUQLFDESQN6CL-40c9Gdog8ZgI2Fi66AgI1Suf1lkOi7UfnaCE3PxtnvKzwh0HNINxcv_s5oNl6bkXl6ngmmKGXJvaIYjz4PpN00dRtjnIk-qkxKkPcWLeXy6o_cvKo61kSHYcbKqpSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما در کل این سیاره خاکی بگردید هر جا کمبود برق و انرژی باشد احتمالاً یا کمونیست هستند یا دوست دارند شبیه کمونیست ها باشند و با شکم گرسنه و خشتکی پاره مرگ بر آمریکا و مرگ بر سرمایه داری سر بدهند.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18253" target="_blank">📅 20:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18252">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شبکه ملی برق کوبا روز دوشنبه دچار قطعی شد و حدود 10 میلیون نفر را بدون برق گذاشت.  مقامات اعلام کردند که علت این قطعی همچنان در حال بررسی است.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18252" target="_blank">📅 20:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18251">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گویا آمریکا می خواهد در این مدت آتش بس موقت با ایران، تکلیف کوبا را یکسره کند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18251" target="_blank">📅 20:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18250">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نشست ناتو و 3 پویه اقتصاد دفاعی روز  افزایش هزینه‌های دفاعی در کشورهای عضو ناتو در حال تبدیل شدن به یک روند ساختاری و نه صرفاً واکنشی به تنش‌های مقطعی است. هرچند در ظاهر، این افزایش می‌تواند به‌عنوان یک محرک کوتاه‌مدت برای رشد اقتصادی تعبیر شود، اما واقعیت…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18250" target="_blank">📅 19:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18249">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ در مورد جنگ اوکراین:
به نظرم ما بسیار نزدیک‌تر از آنچه مردم تصور می‌کنند (به آتش بس) نزدیک هستیم.
پوتین می‌خواهد که این جنگ پایان یابد. من این را به شما به شدت می‌گویم. ما یک تماس خوب داشتیم.
زلنسکی در واقع می‌خواهد که این جنگ همین حالا پایان یابد.
ما می‌خواهیم به ناتو برویم و می‌خواهیم در مورد آن صحبت کنیم. و من فکر می‌کنیم که می‌خواهیم آن را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18249" target="_blank">📅 18:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18247">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
بمب خبری ... اولین حضور رهبر معظم انقلاب آقای مجتبی خامنه‌ای در تشییع و نماز برای پدرشان در مصلای تهران  https://t.me/+SV6YYFA0zX1kOGZk</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18247" target="_blank">📅 15:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18246">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEhsan Movahedian Channel</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a018aa532.mp4?token=Tj_iasSOTIk2odkTDJpDoLOSpKJy4Ip_CtTZzULGiGbaJOSzLlhWpYH-pYTBCe_JHcJkhB3U6aFSQF0LCgqo2UOlfx1XDCmqVlvYg8J6K_rzzscFxafD8128hGis60DgTs4N3ARQeayWKhVskFBwqxAns78x3KkD2PPnuC0rpuV8tjzjR6mTU2h6FeWyW-5OQURxccDbqreMYHxIGEtuoYS355hy-wl6KE5IU0lg0cL7bpihEl0KEaTGdjqT3Upy6RZeVnEB-BohTFpJvdZCLbfRuGp577ETG0nzE5GqqFb1eu-35DSVrwsTvAN2_KvO0a6b7NhKW3Xy6nhI-I6oEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a018aa532.mp4?token=Tj_iasSOTIk2odkTDJpDoLOSpKJy4Ip_CtTZzULGiGbaJOSzLlhWpYH-pYTBCe_JHcJkhB3U6aFSQF0LCgqo2UOlfx1XDCmqVlvYg8J6K_rzzscFxafD8128hGis60DgTs4N3ARQeayWKhVskFBwqxAns78x3KkD2PPnuC0rpuV8tjzjR6mTU2h6FeWyW-5OQURxccDbqreMYHxIGEtuoYS355hy-wl6KE5IU0lg0cL7bpihEl0KEaTGdjqT3Upy6RZeVnEB-BohTFpJvdZCLbfRuGp577ETG0nzE5GqqFb1eu-35DSVrwsTvAN2_KvO0a6b7NhKW3Xy6nhI-I6oEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بمب خبری ...
اولین حضور رهبر معظم انقلاب آقای مجتبی خامنه‌ای در تشییع و نماز برای پدرشان در مصلای تهران
https://t.me/+SV6YYFA0zX1kOGZk</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18246" target="_blank">📅 15:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18245">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ونس: ظرفیت تهاجمی روسیه نزدیک به صفر رسیده است   در مصاحبه‌ای با تایمز بریتانیا، جی‌دی ونس، معاون رئیس‌جمهور ایالات متحده، وضعیت نظامی روسیه را ناپایدار ارزیابی کرد.   ارزیابی او: توانایی روسیه برای عملیات‌های تهاجمی بیشتر «ناچیز و تقریباً صفر» است. این می‌تواند…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18245" target="_blank">📅 15:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18244">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 2  دوشنبه 6 جولای 2026</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18244" target="_blank">📅 15:15 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

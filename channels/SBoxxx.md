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
<img src="https://cdn4.telesco.pe/file/e2L1ioh-hRmnLmc2dtYjrplSE-FFbnybasFqvIoBVJxpMY8RanbJY8OunvxGNPqxayCBXqVgvj5BATiQnjsI0Vux64VGrlE8QS8GaOWu65uQVLGx5ItRR1BBuljRnaLnAFsssNqyPmiIn3S7HXaukgze9XBMGe8hKrtuHR8IoBa2gLCvfpvzY82K3oG_RQNH_2H-jJ7VywTaHwfJE2cPNKXGpPe88BDLmptKa4osLycPqkCzN8-ImBG71HNV-ozSX2WV8aYb0OLuttVvVEp0FLslB3MsZN0RgNFPQmfVnSDf4aQnHIkUCsor8CFjodm0iHuWs_jwtVHCN_OP-XXIpw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.85K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 13:12:49</div>
<hr>

<div class="tg-post" id="msg-16415">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">احتمالاً زمان بازگشایی بازار بورص هفته آینده اعلام شود</div>
<div class="tg-footer">👁️ 153 · <a href="https://t.me/SBoxxx/16415" target="_blank">📅 13:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16414">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ارسال پیشنهاد اصلاح شده ایران به آمریکا از سوی پاکستان</div>
<div class="tg-footer">👁️ 178 · <a href="https://t.me/SBoxxx/16414" target="_blank">📅 13:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16413">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ارسال پیشنهاد اصلاح شده ایران به آمریکا از سوی پاکستان</div>
<div class="tg-footer">👁️ 822 · <a href="https://t.me/SBoxxx/16413" target="_blank">📅 12:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16412">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uyhh15YPtqheFzm3HajxBFBscVMrA95XDRQvj3pb0XgX4ivzODArJjeFhpg4RLIMr_eyRdsPQU7SdCTou7tIr_gmjwQ5uilMnc4MTUl7cJgsqWOuXU_u7P2G1lj-Xqm9BbveIbDy1P1fwGnE18l-JOszoqAXLjptI5UaGIpXvi52g7Mac2ZhmX8nec1tZQPQyEpOtJm2AB8OHovjbwtdnV-yPilb3PWjzm8ky5TS09Wi_wxFtXySk57ktj3VVFQJJUMkIUScmr-GWsHC4TsX0aNPQXI1-fUy3XahIcNXduNvDN6NTnNjE6FvbLtyBYn2BWDxaRD5mEgvdHnqm_tyhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/SBoxxx/16412" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16411">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🟣
خبرگزاری CNN :  کابل های اینترنتی تنگه هرمز ، توجه ایران را به خود جلب کرده است</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/SBoxxx/16411" target="_blank">📅 10:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16410">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COBI7cfIzy99UZMOCpxi9BaF1zbNkRv4h6ZZa_ogMu6evL-53OyYumx5aL100pww5AFmrrKaq0tLmG278olalPxqGnf7c0JAbAYynJfnG1v18rm0MmkU9AR3ud8uSvtsME-WDd8Hg0yqhevjVyWdQ4Oqiu1K0QiPqF3AkxeoX41SjVX_0AptXMLyBQPdD9f-IFeG7QdESdh13LLC7MLUREJhsduiwWduSvfwD7iUaOSPoLkcIqhJN5DDGR0YfyP7S7NjYf4yfWLCc49RpIs3YvBVRTYU_gCnuX9WJ89OaPchEGZGI8i0J7JQC3BckdMVo06yDBOWD6dZs7yUQYw-uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL -- H4
💬
ارتباط با پشتیبانی : @cyclicalwavessupport
📌
کانال ما : @cyclicalwaves</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/SBoxxx/16410" target="_blank">📅 09:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16409">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcT_S1u17jS2lwruxbIYbUEWa6x220j0tTIh8NsytgbRHfZxAVyxxZ8jrE65MkhezFN1XV95MxvfATeiIFytx9NrRqHsa6FP3bpyuXAa-wrgnwBuZKF767U5FwDMkUEIzCGezuEBPZIB2uzTXAfRT9CxW9qJ1iAwBY1rvPfvdpwnC2Y7busE7OIvALndXjZHJmW4_or8pqJku4YiIjsYkJ-7bRfLrWoUvxfZt4l0fUwgd8bI_7wX_hfTVRVV-bRL1L1Oc1bWQUi964A2b1xeeKqbCN51Kgk3DBtQgfWJiWpr-w7hQTZ7YdSUVvpcXjwhCAzkjyvIeadCot8PrPgYSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین که ترامپ مردد است بین کوین هست یا کوین وارش کدام را انتخاب کند نشان می‌دهد یا دنبال دستکاری بازارها است یا اساسا نمیداند این دو در دو سوی طیف سیاست پولی هستند؛ یکی بشدت هوادار تسهیل پولی (هست) و دیگر طرفدار متعصب محافظه کاری و انضباط مالی (وارش)</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/SBoxxx/16409" target="_blank">📅 09:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16408">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">#URA — D  #سهام_خارجی  این یک فرصت ویژه ایرانیان خارج کشور است. صندوق ETF اورانیوم می تواند در قالب موج 5 خود دستکم 70 درصد رشد داشته باشد که در چارت می بینید.  نظر به مسخره بازی ما در تنگه هرمز، احتمال هجوم سرمایه ها به انرژی های جایگزین بالاست و انرژی هسته…</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SBoxxx/16408" target="_blank">📅 09:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16407">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تأثیر جنگ ایران بر بحران انرژی اروپا
جنگ ۲۰۲۶ ایران با بستن تنگه هرمز و حمله به زیرساخت‌های انرژی، شوک شدیدی به بازار جهانی انرژی وارد کرد. اروپا، که به شدت به واردات گاز طبیعی مایع (LNG) و نفت از طریق این تنگه وابسته است، اکنون با چالشی بزرگ روبرو است. بر اساس گزارش‌های اخیر،
آلمان و ایتالیا
آسیب‌پذیرترین کشورها هستند. بانک مرکزی اروپا هشدار داده که این اقتصادهای وابسته به انرژی ممکن است تا پایان ۲۰۲۶ وارد رکود شوند. افزایش شدید قیمت‌ها، تورم را در بریتانیا به بیش از ۵ درصد رسانده و تولید صنعتی در بخش‌های شیمیایی و فولاد را با چالش‌های جدی مواجه کرده است.
کشورهای بالکان مانند
یونان، قبرس و ترکیه
نیز به دلیل میزبانی از پایگاه‌های حیاتی ناتو و آمریکا، نه تنها با بحران انرژی، بلکه با تهدیدات امنیتی روبرو هستند. حملات پهپادی به اکروتیری و دکلیا در مارس ۲۰۲۶، منطقه مدیترانه شرقی را به منطقه‌ای ناپایدار تبدیل کرده و صنعت گردشگری این کشورها را نیز تحت تأثیر قرار داده است.
در مقابل،
فرانسه
به دلیل داشتن سیستم انرژی کم‌کربن و مازاد برق، کمترین آسیب‌پذیری را دارد. این کشور با تکیه بر انرژی هسته‌ای و منابع داخلی، توانسته است از شوک‌های خارجی در امان بماند و حتی بر افزایش تقاضا متمرکز شود.
به طور خلاصه، کشورهایی مانند آلمان، ایتالیا، بریتانیا، یونان، قبرس و ترکیه بیشترین آسیب را متحمل می‌شوند، در حالی که فرانسه به دلیل استراتژی انرژی مستقل خود، در موقعیت بهتری قرار دارد. این بحران بار دیگر اهمیت تنوع‌بخشی به منابع انرژی و کاهش وابستگی به واردات را برای اروپا برجسته می‌کند.</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/SBoxxx/16407" target="_blank">📅 09:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16406">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجنگاوران</strong></div>
<div class="tg-text">تلویزیون دولتی آموزش زنده‌ای درباره نحوه استفاده از
مسلسل پی‌کا
پخش کرد.</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/SBoxxx/16406" target="_blank">📅 07:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16405">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFPZTrQ104_0vZaFgwrbkL04mB02sOw0nTE0QAXk5HTuiJR0KDg482J5oEZdCAQOtOrI7-jt514twqyQ0YyPB421b8fE6OhDHFXAjJvF3O5jaL4PxtC3YUYEwGfILv9pkorW2fFIrE_Ja3uVAVKElnEYR9cXWbgJNdh7Tdrb6ZaPLnsMpS-4-s_XmqjjqLx74zbAPHqmJzORwFX-HAIPjbb3S8OaJSpPyU3V1czRong43QjFx-fQg9pWSNXoO0eFasI4rC4LDhfXwfQZyZZXJeEcAsMxkkaPKbUpMFnR4-_uvH9Xa8Z-umbxxplTneaVcDvNz2EREeX-mke7PwgQyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gold/UKOIL — W  افت 45 درصدی نسبت طلا به نفت پس از ارائه تحلیل.</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/SBoxxx/16405" target="_blank">📅 06:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16404">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvGpOiOBNH3d7sAFonaYt1Z7Fb6S5Ha4fr63TqURdBav-LDou_nSqLbyBM7Q7LZHM77zNztvPYzbXXIq_4SQB7gQ_AJbTw3hpwKB8IMxmeQJVZLUptls1Byw2DN0k2nbzMZ9ntma2KPNjZkltVC5yjlGidttp28iBLcaB-OG0kiCepM-qsJ_HCkaU4qZuEjsFXpKGjm2fcFAaQ5IL6CmqHojjNlXfluxN2tVtuOTuV56DtDqhNGjgoouQeYofIUumGYbjdYdtMNNgWZr8bfghh2RlRyEQ2jc0HHG6QrJvynPm5E6zoTIVQC90rbSZlDKP8bbRRCJc4K3Z55MKjM9DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشخص است کله زرد خسیس رفته نسخه رایگان هوش مصنوعی کذایی را که با آن کار می کند خریده و گرنه این همه اسم شهرهای ما را اشتباه نمی نوشت.  رشت = Majd? تبریز = Toha?</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SBoxxx/16404" target="_blank">📅 06:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16403">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پست جدید ترامپ که به نظرم به نوعی تاییدی بر حمله زمینی است.</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SBoxxx/16403" target="_blank">📅 06:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16402">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ارتش عراق:   اجازه نمی‌دهیم عراق سکوی پرتابی برای تعرض به سایر کشورها باشد</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/SBoxxx/16402" target="_blank">📅 05:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16401">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حقیقتا «الکسیس میانرودان» لقب شایسته ای برای عراق نیست؟!  تل آویو - اسرائیل برای پشتیبانی از عملیات هوایی خود علیه ایران، یک پایگاه نظامی مخفی در صحرای عراق ایجاد کرد و حملات هوایی علیه نیروهای عراقی انجام داد که تقریباً در اوایل جنگ آن را کشف کردند.  به گفته…</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/SBoxxx/16401" target="_blank">📅 05:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16400">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKo44nkd-Sqr0hcZqcU15aLeD_SQnR3ne4Ejz0tOE2eqPQqKM2kw3YwxipNxfBww46VBqPPi4lkZ3bqkHpowcGk6AQTFzhLbrOKDYWnb0FDrjbdAgZqJpp3yPP8In-62gAL9TCRgK40J2nqlwh8UdU_B3qG9wRAnoJ_8ct9_4fsRAeRsqV1FgVxbj-GwK07cOnJ5MWtwTZsA7QcsJ4jPFOk5D2GQvUd1xV2qosVVmzstfidqN-aUA5L-s0gRtfSGESr_ZHG8XM9Lq10eccSlvFmjTq0RJjFKqFDAeMF470pIdEqNscjAk-YhVu_Mke0Q1vecdCESQn9L7AQPGWvMWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج ۵ نبرد ایران و آمریکا همراه با هلی برن گسترده با حمایت هوایی سنگین خواهدبود و تسلیح یگانهای ویژه نظامی در ایران به تفنگ‌های دورزن و موشکهای پدافندی دوش پرتاب و نیز موج آموزش عمومی کار با اسلحه در صداوسیما و مساجد و … در راستای مقابله با این تهاجم است.</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SBoxxx/16400" target="_blank">📅 05:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16399">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBzAdEmKqZMlqK7w0kRMyxRHZurHcC1i__b-kM9rj4I7bgHOS79jUrmvbFf1AFFGXxcsq4sETLrlJ0tucA6w3-n2Y2GvhgTBwP5VF6U6fc8jLmo0bzC4FPEXehrXWW0ykZWu6ULEcMX9w2RfjdzCx2SAfEfONS_IF0X7EQmirXCu_cSrWeiBZzKS3b_cB95MWNUdskBwfewcOpZNvmO3UAct2_petMfGbMdTDzHr399j5qnbJrvNH-DO9IoQ5itGQWLz_fetw-nxZgNg2vQPww2csB7s-2EK_O3rMledtOccmBIprGTei8nVr8r2fDi1mG0tEu1O52vfd4jWYJN9OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SBoxxx/16399" target="_blank">📅 05:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16398">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b124790efc.mp4?token=FlhHAmtyCK5tDhFnuTtziL8FpDmS4HgGvk5i4nK5sMCTyVbRhXmR8Mcm5AzoNkluetsWYHkWkEQ0UgPl0g-EP8dwZkEhXvDXcslE9WbBUlquVJ-4TpJyLxvCV1kLq0VrvnBvB8wqa4wVWgtF4z0z4zYk7inIiEnBtE55m6JGh772SrMU86DnqOSOFlv8UYhMvnW9COvvt_29jK4JNga_JJAKlgMIYiVsVqgIhqm7DeJ3yO41rApQopsG8ZqHYAKrFGrQkTrim9obPD8P7ewYDIVE_z6ZCDdNSEcO0kAc6d64mAstfyX1SWuwc2ZpbSxehL3WrjYTDgjL9MvZSSSs7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b124790efc.mp4?token=FlhHAmtyCK5tDhFnuTtziL8FpDmS4HgGvk5i4nK5sMCTyVbRhXmR8Mcm5AzoNkluetsWYHkWkEQ0UgPl0g-EP8dwZkEhXvDXcslE9WbBUlquVJ-4TpJyLxvCV1kLq0VrvnBvB8wqa4wVWgtF4z0z4zYk7inIiEnBtE55m6JGh772SrMU86DnqOSOFlv8UYhMvnW9COvvt_29jK4JNga_JJAKlgMIYiVsVqgIhqm7DeJ3yO41rApQopsG8ZqHYAKrFGrQkTrim9obPD8P7ewYDIVE_z6ZCDdNSEcO0kAc6d64mAstfyX1SWuwc2ZpbSxehL3WrjYTDgjL9MvZSSSs7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
در ادامه تمرینات آمادگی دفاعی شبکه افق ، پس از شلیک های موفق به پرچم امارات در روز گذشته ، امشب ، نتانیاهو و دونالد ترامپ بدون استفاده از گلوله ،  بصورت نمادین هدشات شدند</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/16398" target="_blank">📅 00:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16397">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">برای ایران، ساعت در حال تیک‌تاک است و بهتر است سریع حرکت کنند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است! رئیس‌جمهور DJT</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/16397" target="_blank">📅 20:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16396">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqqIIUw4qmqvimfhhhoChHeR2DZ2wsW-1xHGpC2a3vFzut9cbVuUCXJUgA4c-mONzFNDSCKH62QW8HMjDQGJRyBxnHN5yg7mv4o5mS0XUUoL6O81rk8srkSa6Zew2bNH56ItAqvw6shSoA9zq06O4Zfny5xTv7A7x1QVG2sbu3wNSBAzcFBz95i7h24W4w-rY0aGKf-HdXYmCaOFIgKW_xkWp2veK_0HR2iYkO4W0WNHgYsoXrTwqZITn_5o9r9aAGIUpfoUC9cb_d2WALngiZzJsHy6MqhiXHNS90yFX3rhjDHvom1ZxXZDj-lf5-yH7btYSElJChYIFGS_by9WOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یووال اشتاینیتز، رئیس شرکت دفاعی دولتی رافائل اسرائیل، اعلام کرد که اسرائیل با کمبود رهگیرهای موشکی مواجه نیست.
این اظهارات در حالی مطرح می‌شود که گزارش‌هایی درباره فشار بر ذخایر دفاع هوایی (به‌ویژه رهگیرهای Arrow) به دلیل درگیری با ایران وجود دارد. اسرائیل همواره این ادعاهای کمبود را رد کرده است.
رافائل تولیدکننده اصلی سیستم گنبد آهنین است و برخی اجزای Arrow را می‌سازد.
اشتاینیتز در یک کنفرانس گفت که گنبد آهنین حدود ۹۸-۹۹٪ موفقیت در رهگیری راکت‌های حماس و حزب‌الله داشته و از ۷ اکتبر ۲۰۲۳ تاکنون، این دو گروه حدود ۴۰٬۰۰۰ راکت به سمت اسرائیل شلیک کرده‌اند.
همچنین ایران از سال ۲۰۲۴ حدود ۱٬۵۰۰ موشک بالستیک شلیک کرده که به گفته او تنها چند ده تای آن رهگیری نشده‌اند.</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16396" target="_blank">📅 19:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16395">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزارت اطلاعات کوبا تایید کرد که رییس سازمان CIA به این کشور سفر خواهدکرد.  به نظر می رسد اینها هم بزودی پرچم سپید را بالا ببرند.</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/16395" target="_blank">📅 19:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16394">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔘
پافشاری ترکیه برای تغییر نام «آسیای مرکزی» به «ترکستان»در کتب درسی
یوسف تکین، وزیر آموزش ملی ترکیه، در مراسم «رمضان در قلب آموزش» در استانبول، از تغییرات در برنامه درسی مدارس به عنوان بخشی از «الگوی آموزشی قرن ترکیه» خبر داد. به نقل از رسانه‌های ترکیه، طبق این برنامه درسی به‌روز شده، اصطلاح «آسیای مرکزی» با «ترکستان» جایگزین خواهد شد.
🔹
همچنین این مقام توضیح داد که مفهوم «آسیای مرکزی» محصول اوضاع سیاسی پس از جنگ جهانی دوم است، در حالی که «ترکستان» (ترکستان) با ادبیات علمی مطابقت دارد.
🔹
این تغییرات بخشی از مدل آموزشی جدید وزارت آموزش ملی ترکیه است. جایگزینی برنامه‌ریزی‌شده اصطلاح «آسیای مرکزی» با «ترکستان» در برنامه‌های درسی تاریخ مدارس در اکتبر ۲۰۲۴ اعلام شد.
آمو | مطالعات تخصصی آسیای مرکزی</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SBoxxx/16394" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16393">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/16393" target="_blank">📅 15:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16392">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDcycn1YVNBUiZKE2QjQ_9pf4y1IIB0GW5GPP0EtjbyXE-F8McjY-GseJuMPby1zz1Z09w3Ggxmv5W0x8v7RlXV4G38lXvF7av48ncLjLm5CEjY6FhJRHJF-iWVIPclv5yHMs6L-7XCXpRkAkOn6ge3VpzMcaL5h6vTxJEdrG8vvIcbsWXH9RMbscCR2wSlgxPjS-Ur1P8Qm7xn3LAvedcNUhZO_OBPw61vCUjngLoKJZuqdYaWsZYUeN3thbQYjmXOt56H1NV8pcniM_Vfyo5UiS-_n2sFP3p7VJDJIR9jvA3Rd2HME4vxfem2h_QehE6fZkDADgyNbr-7KSkzFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان بدون اینکه خنده اش بگیرد روز جهانی «ارتباطات» را تبریک گفت!</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/16392" target="_blank">📅 15:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16391">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✈️
پاول دوروف ، مالک تلگرام: دبی دوباره شلوغ و پر از ترافیک شده است. از همین حالا دلم برای آتش‌بازی‌های ایران تنگ شده؛ آن‌ها کمک کردند تا شهر از افراد زودباور (وحشت‌زده) خالی شود .   پدافند هوایی امارات زیر آتش (حملات) عالی عمل کرد. ما با پرداخت ۰٪ مالیات،…</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SBoxxx/16391" target="_blank">📅 15:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16390">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kq9rsANfOCd8Qcj_Cj8hzxGSDzSQPFYcHCYstgRGj6p9IT_W_5t6TV9n2ua-1oGGFwii8-gJExC6T2v017GVsCvDo-RfKfBrsIlJIRVS8BKWfgxb3sc5RADIiz-jpJnK0dEL9mm6M6pZv7sk5QxmphOJwT9NjMnbI04GeX9NeUuSx4SmDcvw3XM_8dJT5VjxZPGD3ob9TQzrdjiZSArDk4zStLvRmWPVdJIvvDGASUgBasmT5oF_np3QY0BLrxB-44iP3kg-6m-S8O5WENcO730ORv0wH2bN7LrO1HgRXmEHcDeavwF--FLqO12p2BvEWExw-cSP_BJ5rRQAeb4juQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔑
حضرتی، رئیس‌شورای اطلاع‌ رسانی دولت
:
حرف‌های پزشکیان در مورد اینترنت «وعده» نبوده، شائبه وعده بوده</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SBoxxx/16390" target="_blank">📅 14:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16389">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsDNWK9JuerQIr6A4yDULgzyU-pKZJYiS9fcFq4eKqrKqNheX5RJR90LWRP_ai4bkFhfw1LDaVzLWDiZgjy3CZI65Mf4P6uu5RZefL7XOzphrlWwCozGmLz3Q0zbiGNSlA2KeZWdog3zRVPFMY3yLkAoVQNmObvhCIm_JB0Z-F9_4wlXf1n7kuPO0agPM9PeEf8BK5gJuXV0MX0An2qASNXTjEUKP9PtEJx0xdBkW67pdt8DBvOihI0oKjIcd2TBrELPNS53s6yQinXIXgliG8EzdlhKwNdKIftpNRZyaRLf5P564SVMXX7OnTKUudgOKoqA-QAxMJGuaEYU8t3suA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#EURNZD
-- H4
کانال نزولی در حال شکسته شدن است و انتظار رشد مناسب داریم.
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SBoxxx/16389" target="_blank">📅 13:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16388">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
رسول جلیلی ؛ عضو حقیقی شورای عالی فضای مجازی: اینستاگرام مثل F35، F22 و A10 آمریکا است، مثل آن اژدری است که به ناو دنا شلیک شد</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/16388" target="_blank">📅 13:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16387">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🟣
خبرگزاری CNN :
کابل های اینترنتی تنگه هرمز ، توجه ایران را به خود جلب کرده است</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16387" target="_blank">📅 12:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16385">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
رسول جلیلی ؛ عضو حقیقی شورای عالی فضای مجازی
:
اینستاگرام مثل F35، F22 و A10 آمریکا است، مثل آن اژدری است که به ناو دنا شلیک شد</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/16385" target="_blank">📅 10:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16384">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بحران انرژی در حال تبدیل به بحران ارزی در بازارهای نوظهور آسیا است
نگاهی به لیست بدترین عملکرد ارزها از آغاز جنگ آمریکا و اسرائیل با ایران بیندازید: الگوی جالب ولی غیرمنتظره‌ای آشکار می‌شود. تقریباً تمام آن‌ها واردکنندگان انرژی هستند. بزرگ‌ترین بازندگان شامل پوند مصر، پزو فیلیپین، وون کره جنوبی و بات تایلند می‌شوند. در میان ارزهای اندکی که صعود کرده‌اند، ریال برزیل، تنگ قزاقستان و نایرا نیجریه دیده می‌شوند — همه آن‌ها
صادرات‌کنندگان عمده نفت
هستند.
آسیا با چالشی فراتر از یک بحران انرژی روبرو است. اقتصادهای نوظهور این منطقه نه‌تنها با افزایش هزینه‌های سوخت و برق دست‌و‌پنجه نرم می‌کنند، بلکه با
فشارهای تراز پرداخت‌ها
نیز مواجه هستند که به نوبه خود بر ارزهای ملی آن‌ها تأثیر می‌گذارند. در کشورهای آسیایی که به سوخت‌های فسیلی وابستگی بالایی دارند، افزایش قیمت‌ها باعث بالا رفتن هزینه‌های تولید و کاهش قدرت خرید مردم شده است. این وضعیت، در برخی موارد، منجر به تضعیف ارزهای ملی و افزایش کسری تراز تجاری شده است.
در حال حاضر، کشورهایی که قادر به تامین انرژی خود نیستند، بیش از همه آسیب می‌بینند. برای مثال، اندونزی به دلیل بازار داخلی کوچک و وابستگی شدید به واردات انرژی، با چالش‌های مالی فزاینده‌ای روبرو است. افزایش یارانه‌ها ممکن است باعث تاخیر در تثبیت مالی شود و کسری بودجه اندونزی در سال ۲۰۲۶ می‌تواند از آستانه ۳ درصدی تولید ناخالص داخلی فراتر رود — موضوعی که نگرانی سرمایه‌گذاران خارجی را برانگیخته است.
در این میان، کشورهایی که صادرکننده نفت هستند، مانند برزیل، قزاقستان و نیجریه، از افزایش قیمت‌ها سود می‌برند و ارزهای آن‌ها تقویت می‌شود. این تضاد روشن نشان می‌دهد که
بحران انرژی اکنون به بحران ارزی تبدیل شده است
— پدیده‌ای که اقتصادهای نوظهور آسیا را در موقعیت دشواری قرار داده است.
بلومبرگ</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/16384" target="_blank">📅 10:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16382">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eadhRb5fhl18OUMRJHdUQRcg3sVczrhCz5p9UKW8v046Q8PNjTJer73AR8ZxkHtPYay6bSABX6xo_X7a9AcRuWcm9p-0DMBzCzfix8Fn-yTO2HPvkZXA54RXoVZNq547zKkgY_YMVHE4oiLSpeJnRz06j7rGtHsL53guRi5S1asAiBetdqt5Yx8tYIdJgT53YxzAGvc2rn9KJBwyF7mTSHd6pSigaZ636pBPzlVJ8jYsFIciKr4LTxC1sjSFHPQ7G0gzpWa2XoDnYNNkWVANa09DqdrJRG79hspfVMJxsYAtlQtBqLGXSyDJHYC-nJj9HqG6e8LfZ65cVOyN3KBB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCLh-iQbKBw7x0mFWv_64j4X8F6VZyQccvYjZelCXKICZqd-USkxOIqNnYk1jw6-46S9KQMJ-vxwQ7r6Zsc6lBDqoN5Jna2vGId1Rqc-kF4JMUhq_6IRpWDU7HyLeA4bnETVQ8qVwyxkc7bw9fuKv038KWBoWQfibsv5xZez8ake4lrxvp7ivch5gJ5_0YJburWQh_nLWq77JEv6_7Il_0LxH6mh8YFsjfWcj-md9TmkN8IJJswTQHA4y-mIJ2lQ6tNQa0HY7jn_XOuqC0Wak3EPGWKX4BeO5UcHLaBIcthLdwyjMnQpBcVX-xoEgrYAMdw_g-CebE88rQFCLLdG0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیروهای نظامی جمهوری اسلامی اواخر سال ۲۰۲۵ قراردادی برای خرید ۵۰۰ دستگاه پرتابگر موشکهای دوش پرتاب زمین به هوای  Verba (تصویر پایین) به همراه ۲۵۰۰ موشک مربوطه امضا کرده بودند که بخشی تحویل شد و بخشی در جریان حملات اسراییل به تاسیسات نیروی دریایی در انزلی از میان رفت.
همچنین سامانه مشابه میثاق ساخت داخل نیز در اختیار نیروهای مسلح ایران است.(تصویر بالا)</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/16382" target="_blank">📅 09:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16381">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">موج ۵ نبرد ایران و آمریکا همراه با هلی برن گسترده با حمایت هوایی سنگین خواهدبود و تسلیح یگانهای ویژه نظامی در ایران به تفنگ‌های دورزن و موشکهای پدافندی دوش پرتاب و نیز موج آموزش عمومی کار با اسلحه در صداوسیما و مساجد و … در راستای مقابله با این تهاجم است.</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/16381" target="_blank">📅 09:16 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16380">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ehk4JRYzF0RvAr5B5ht23nwJ5Lqa98ilzPx6sdnOSFa0bdfTchSWwbvAVdSIfmQBzLVijEGjtOe_jHQMlG3i-0j8Geo_ImpA0Sebm0LkwQFB4CcTF6YCSPI9cytiNMIdaV7OgBETkgKlraH00Ae7IYvBb_Hx_eQJEXxdEfGP6dTDQqqwfL8tHE4BHaO-uLxnJ3QmrGAnCMdRqEBmAOYxU3piL-o569H20CfYSjCl8eKfD5zHtZqSHpC4Usnvwkk3SPYCoAECX3EYccrp0164ZzqS_UKOR7hZwRC3gMGoe4WPdxcu26SI232AQqIscKeCfntQqrusZSDykWPTy6Jejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج ۵ نبرد ایران و آمریکا همراه با هلی برن گسترده با حمایت هوایی سنگین خواهدبود و تسلیح یگانهای ویژه نظامی در ایران به تفنگ‌های دورزن و موشکهای پدافندی دوش پرتاب و نیز موج آموزش عمومی کار با اسلحه در صداوسیما و مساجد و … در راستای مقابله با این تهاجم است.</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/16380" target="_blank">📅 09:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16379">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzL0_Pl0iBTPno-lBOcpBh5cTE0uUhGTiKEv5mXQtXbWUswjsltdyrQH52UrghRI8KqYJc0I6vtM7P8fp9KBAa1oQMFBPRvoAzZj1e054XSeGfh49jhXlF0RG5aT0JlKMe1CNnBZiIhP5FGeyEKTJ8dev0SDMGOrleHo-nfo8DFjDyFbisPZAvCvibW-5r8TE9iO0fRLvmuop91TR0Eunl9vAbW-IteusIlq7f1AIhd2mP7VHGppVnqqkUplj8HcXMBEyDqcaOktUI1dyKVPZ240n9YUSt4xUhbNFY_0WqJ_B8hSV1xfpdaCNahNZVylZZc9GwQddTaC_IA57ZS3hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16379" target="_blank">📅 08:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16378">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/617dc4e3f8.mp4?token=BVeI_sWUIrecQcPdmSr46GNqybj7RMIN6Wo6E0Vt8OTfAC-ZzAk4Rf6HspCRkAYWY7V98KS7_Dg4tkV9NCJZR94XjEm_YZnQLmmBL58GfrVkuSzx84xcYR4vWGyavOzBAyaxFxrnPl8zFI79DGWTJMsL3enIAdpbAiQF2meGFz2Qfs3EFwHhG8xX7imixXL1ykwkSeQdptlg7007qvlpsOyq38WBwZ7xpcMiqR-y2ipFxnt5MfM_1p-xh3MzD1rBneLNwHOpYdR5Ad4hJTpVXpH1kNu9p-6_c8UCBSSx4in0KtCuMkSLaSPQgyqwhANDn4tj94HuidHOmtSSHGODsFKij1S8TeFF-UuGp1KXhWxZdnh69VHbmAcZnEwIY2jGDuo19SidhvkzUT6VsYfNe234fMI9H9FXUrwppWJ3HDjE39JeJmhNB1mFMibgLjwao3AkgAuaoadrvC1Ee0c24zMcTz4f1pCKzyg-7c8XYRrgnzFDc_AHyriuHU04ZAnaXSJstmNcJayd6JZapO8GRhd4-OLk5rxI_-A07v6EQKdhJjFapx_VkariPgDgYS75MLVn6UVRc2QXYtGeZQKOPUb7NB7iHhvaj4GCQfHAWLS9rS6hlY4gM_kNgIyKctXFno63GU6jcEGqOvnh1fOlX-E7ALtoxcVQI9U1btjhEYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/617dc4e3f8.mp4?token=BVeI_sWUIrecQcPdmSr46GNqybj7RMIN6Wo6E0Vt8OTfAC-ZzAk4Rf6HspCRkAYWY7V98KS7_Dg4tkV9NCJZR94XjEm_YZnQLmmBL58GfrVkuSzx84xcYR4vWGyavOzBAyaxFxrnPl8zFI79DGWTJMsL3enIAdpbAiQF2meGFz2Qfs3EFwHhG8xX7imixXL1ykwkSeQdptlg7007qvlpsOyq38WBwZ7xpcMiqR-y2ipFxnt5MfM_1p-xh3MzD1rBneLNwHOpYdR5Ad4hJTpVXpH1kNu9p-6_c8UCBSSx4in0KtCuMkSLaSPQgyqwhANDn4tj94HuidHOmtSSHGODsFKij1S8TeFF-UuGp1KXhWxZdnh69VHbmAcZnEwIY2jGDuo19SidhvkzUT6VsYfNe234fMI9H9FXUrwppWJ3HDjE39JeJmhNB1mFMibgLjwao3AkgAuaoadrvC1Ee0c24zMcTz4f1pCKzyg-7c8XYRrgnzFDc_AHyriuHU04ZAnaXSJstmNcJayd6JZapO8GRhd4-OLk5rxI_-A07v6EQKdhJjFapx_VkariPgDgYS75MLVn6UVRc2QXYtGeZQKOPUb7NB7iHhvaj4GCQfHAWLS9rS6hlY4gM_kNgIyKctXFno63GU6jcEGqOvnh1fOlX-E7ALtoxcVQI9U1btjhEYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این هندی ها همه چیزشان کمدی درام است؛  مقامات هندی در حال بررسی طرحی برای رهاسازی مارهای سمی و تمساح‌ها در نواحی رودخانه‌ای مرز با بنگلادش به منظور جلوگیری از نفوذ و فعالیت‌های مجرمانه هستند</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/16378" target="_blank">📅 08:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16377">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">معاون وزیر خارجه روسیه دقایقی پیش از قریب‌الوقوع بودن حمله آمریکا و اسرائیل به ایران خبر داد.</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/16377" target="_blank">📅 02:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16376">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔹
رسانه های اسرائیلی از وقوع انفجاری عظیم در بیت شمش خبر دادند
🔴
گفته می شود ، انفجار مربوط به کارخانه بزرگ " تومر " که فعال در حوزه تولید و توسعه موتورهای موشکی و موتورهای پیشران است ، بوده است
🔹
هنوز اطلاعات دقیقی از خسارات و تلفات این حادثه منتشر نشده…</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/16376" target="_blank">📅 00:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16375">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔹
رسانه های اسرائیلی از وقوع انفجاری عظیم در بیت شمش خبر دادند
🔴
گفته می شود ، انفجار مربوط به کارخانه بزرگ " تومر " که فعال در حوزه تولید و توسعه موتورهای موشکی و موتورهای پیشران است ، بوده است
🔹
هنوز اطلاعات دقیقی از خسارات و تلفات این حادثه منتشر نشده است</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/16375" target="_blank">📅 00:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16374">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bzc35S_KfIG6zdaMn3V7DMDBNYNeTX8u4JLyprNpllCLxeDp17iZDDLxuTGx3nmou_1ZZW5Y_x_afaTQ8ykWqY8x42fgDccoRs5JklZn399pkc0fP6cYKZvxnOIiZo1p_zMiRMgMQf9FrGWLkekSFldHqHDasRhoBYPAWMYqXx2fhVrsBJyRv6T6NN2CwxwUWa2Ijbx0nWXgeYAe9EcOcWCwSZ0Uy-AIlg2TFttYErh54IW6JrQosZSho5hdNrsHj5OuwW-ArdaJr-aisgvoEpcBKKagC68GHH5ijOVxC6kb9V1gaFdjLYEwDgkLBmyd9cQiGw0T_AZXYSB94eoXxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مرغ طوفانم نیندیشم ز طوفان | موجم نه آن موجی که از دریا گریزد</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/16374" target="_blank">📅 00:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16373">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/16373" target="_blank">📅 00:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16372">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16372" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16371">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwmBNAnsE_eKkSJtBTrHoyAc1TtJWEpBkq3Y-MDTcrjYkZAoS2URZWH4hS5hnOrrgFMmKBicR441UGFOsQ-zEiDmGXCmxs6uPnpL45AxJ8vMTiCaGMdUipV5Pi4GbYHWipQNumjB4pfWN5-9Sgczzir128BxZNwl3zrPIv_2LMXqx5KlBSiKA1J5aOPtCLVAUXmT_jO1glfKe8NIcbMOwFRLyPy5accbpfBeWne4sGURHNWAcZZ8uHYep7lOC2sOmBLcH8F_VmLxTQI2LZDPz0dIjNqFZ6nWC5uDpp5aOPyGp2PHbq23n6FOYviUrOhcCWHffgekIb1_M7lKF-35iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کله زرد ول کن این هوش مصنوعی کذایی نیست.  چه گناهی کرده ایم که این ور با هوش مصنوعی هر شب فرعون و ناوهای آنها را غرق می کنند و آن ور هم آنها قایقهای کوچک مان را اینطوری پرپر می کنند.</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/16371" target="_blank">📅 23:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16370">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⭕️
تاثیرات اختلال سوپراپلیکیشن "شاد" و اخلال در بستر دیجیتال آموزش کشور</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/16370" target="_blank">📅 22:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16369">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iodMTwQzAmn4GdWqVGjWoJxmT8w2_KwrPXbPCrq8QXCaIOL-KlNhQUZo3LJFG5kBLLKTQh7X6ikq1l2axujtK-B7IE1XMl-fTf1IiPFEbREZDGqVEd-P-h580cmUf9WON4yuXu-9rM8fZ5OHNZ64dKY2OsHJUT1bcS8RId-8LsE_FhTdKuUxdvC5374kq0fXtkK_m0jrsyHvTzCuCOKbGKEZ_wd8kdnEvA_8Ag23J4JkvQ0TARo6eiIhRSwodzMyNleTEgXL1ldfUm2Cm1Gc668ZJlvOXBRRVumWmjTF4F1LiaUY-2AuE3CszbgTE-xXlnZEcxmzkrmOKMASGtRJKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر داگلاس مک گرگور از میلیتاری نویس های برجسته X دال بر نزدیک بودن دور بعدی جنگ</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16369" target="_blank">📅 22:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16368">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بازگشایی بازار سهام از روز سه‌شنبه
‌
معاون نظارت بر بورس‌ها و ناشران سازمان بورس و اوراق بهادار:
برنامه‌ریزی لازم برای آغاز معاملات سهام و ابزارهای مربوط به آن از روز سه‌شنبه ۲۹ اردیبهشت ۱۴۰۵ انجام شده است.
‌
بر اساس هماهنگی‌های صورت‌گرفته و پس از اخذ مجوزهای لازم، مقرر شد بازگشایی بازار سهام، انواع صندوق‌های سرمایه‌گذاری در سهام و مشتقات آن‌ها از روز سه‌شنبه هفته جاری صورت پذیرد.</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16368" target="_blank">📅 22:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16367">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">عارف، معاون اول رئیس‌جمهور:
دیگر اجازهٔ عبور تجهیزات نظامی دشمن از تنگهٔ هرمز را نخواهیم داد.</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/16367" target="_blank">📅 21:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16366">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✈️
پاول دوروف ، مالک تلگرام
:
دبی دوباره شلوغ و پر از ترافیک شده است. از همین حالا دلم برای آتش‌بازی‌های ایران تنگ شده؛ آن‌ها کمک کردند تا شهر از افراد زودباور (وحشت‌زده) خالی شود .
پدافند هوایی امارات زیر آتش (حملات) عالی عمل کرد. ما با پرداخت ۰٪ مالیات، حفاظت بهتری نسبت به اروپایی‌هایی دریافت می‌کنیم که ۵۰٪ مالیات می‌دهند.</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/16366" target="_blank">📅 21:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16365">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حالا امارات را مسخره کنید اما اساسا یکی از مشوق های اسراییل برای پیوستن کشورها به یک پیمان راهبردی با تل آویو «تصرف خاک» است.  نمونه اش پیمان با باکو که منجر به تصرف قراباغ شد و از دید اماراتی ها، وضعیت جزایر سه گانه برای آنها معادل وضعیت قراباغ برای باکویی…</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16365" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16364">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">در حالی که ‌وزیر کشور پاکستان در ایران است تا معامله تمدید آتش بس میان ایران و آمریکا را جوش بدهد، شهر دالبندین در این کشور بدست جدایی خواهان بلوچ سقوط کرد!</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16364" target="_blank">📅 19:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16363">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oamMJ7XWHgpqvOPSKqsESEYNzaNXBbltEfOADWhjJiGsWWfcxGGl5GgBUQGpY4O1hz_c-xGBbWMKml7Ouqaet9hBvSJ6Rw2xObEZzW7KKsrvVv17Gwq-pkXjRp5btZotSLHES97drVmuNI0Z35kMzV3vaxG9Ye-C-wWKANylubCBs40K6woO0FKFxq-_v-TsXk0HmI4ZDNLLWnof19EEnbRvnoFs6afB2E-corFFGxVx-FtZ7D_z4BJkJtMhDXPMS_sZMbbhasv9oZpg2vQluK9n2Q6l2whHJzKs18SYKKhwadZc4eQg8YQKFV8pEHBzk36_ZHhUgdV9qCvef9BfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بعد از تعمیر سوپراپلیکیشن "بله" ، سوپراپلیکیشن "شاد" دچار اختلال شدید شده است</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/16363" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16362">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♥️
سوپر اپلیکیشن "بله" دقایقی قبل از دسترس خارج شد</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/16362" target="_blank">📅 17:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16361">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♥️
سوپر اپلیکیشن "بله" دقایقی قبل از دسترس خارج شد</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16361" target="_blank">📅 15:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16360">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6ibW5dKoFANUqotH10jycBLPHPBKaT2PF6f4UMoxHQf1wFq8wPVZ6K3sxU-YmiUNM-Kkj0LCql_Fmkcajs7zHHMFvWcuK04CElHbPs473WazCKjwTdGpZSaHX0VBmMM7DkgdPDQeENAAMs3BA3HRtflNpAREcL6O3vuehNPukqhbcIcdRje4ClNFRs0wkSMhVnC45ClZY4eZqTGUTjrJaY2WKYOX4YVzgpyTV4JLtz-yLNLlGuXaF7mvynaBNVxOQAWnD-oz1UlnSIq3gZ91K_yXUVpMKu0UhqtkW9CnnnBmHGHHmGZ0yBVqylBwvTx7U-Ej0DpHztswc6JPwZPTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تحولات رفتار بانک‌های مرکزی درباره طلا
بانک‌های مرکزی در سال ۲۰۲۶ رویکردهای متفاوتی نسبت به طلا اتخاذ کرده‌اند؛ برخی مانند ترکیه فروش را افزایش داده و برخی دیگر همچنان خریدار هستند.
ادامه خرید طلا توسط کشورهایی مانند چین و لهستان نشان می‌دهد طلا همچنان جایگاه مهمی در تنوع‌بخشی ذخایر و مدیریت ریسک بانک‌های مرکزی دارد.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/16360" target="_blank">📅 15:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16359">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">◆ در صبحگاه دهم اسفندماه، چهار فروند جنگنده فانتوم نیروی هوایی ایران مأموریتی علیه مواضع کردهای مسلحی که قصد نفوذ به خاک ایران را داشتند، و همچنین علیه نیروهای آمریکایی مستقر در فرودگاه اربیل، انجام دادند. در این عملیات، دو فروند فانتوم وظیفه اسکورت به عنوان…</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16359" target="_blank">📅 13:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16358">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromParvaz dar oj</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYcL9imUh9GiyZxv1FU9joEYizi-quLdpkXLvr_qlR8NCYRjMT6Y6hQ-6qiWwGf6HErgZO2TPV9USul94qf6IqPdDEoxhHG9Gu6kS03vQLubzyX-Lvy6Ior_NnfHbMILZWhoLsXFcu5HUA6IG4J7ozf2B4N_9zXR4eUBBWaalq5gNKdzTr9IQ8iQWCuUDhxBFVhXIdTscQWdZJdlVrCVR8Fy-91INVhWxpwvHORaawBrP64UKvD8Qiuei4Vim_UE-B6otAg5mV6o4lG-O0nsEr_pjUvTsoMxJPxcfJFWRmt2JOub7Texlu6Q06e1hBOmbDlFuV_AE5QiT99WYDQN1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◆ در صبحگاه دهم اسفندماه، چهار فروند جنگنده فانتوم نیروی هوایی ایران مأموریتی علیه مواضع کردهای مسلحی که قصد نفوذ به خاک ایران را داشتند، و همچنین علیه نیروهای آمریکایی مستقر در فرودگاه اربیل، انجام دادند. در این عملیات، دو فروند فانتوم وظیفه اسکورت به عنوان تاپ کاور  یا تأمین امنیت هوایی را بر عهده داشتند و دو فروند دیگر مأمور اجرای عملیات بمباران بودند. جنگنده‌های بمب‌افکن موفق شدند مأموریت خود را به‌طور کامل انجام داده و اهداف تعیین‌شده را مورد اصابت قرار دهند.
◆ در جریان بازگشت، در منطقه مرزی ایران و عراق، جنگنده‌های اف 16 و سوپر هورنت  با هواپیماهای ایرانی درگیر شدند. هویت دقیق جنگنده‌های فالکون مشخص نشد و احتمال تعلق آن‌ها به نیروهای آمریکایی یا اسرائیلی مطرح بود. در این درگیری، دو فروند از جنگنده‌های ایرانی مورد اصابت قرار گرفتند، اما هیچ‌یک سرنگون نشدند و هر چهار فروند موفق شدند به پایگاه خود بازگردند.
◆ همزمان،تامکت های نیروی هوایی ایران نیز به حالت اسکرامبل درآمدند و برای پشتیبانی و مقابله احتمالی به پرواز درآمدند، اما در ادامه درگیری هوایی مستقیمی رخ نداد. با این حال، پایگاه مادر این عملیات بعداً هدف حمله قرار گرفت و از آن زمان تاکنون از وضعیت عملیاتی خارج شده است.
◆ با وجود خسارات واردشده، این عملیات از نظر نظامی و تحقق اهداف تعیین‌شده، عملیاتی موفق ارزیابی شد . خلبانان اعزامی با توجه به گشت دائمی هواپیما های آواکس و جنگنده ها بر فراز آسمان عراق،کار بسیار بزرگی انجام دادند .
به خلبانان اطلاع داده شده بود که به احتمال 70 درصد ،هواپیمای انها مورد اصابت قرار خواهد گرفت،اما همگی با شجاعت مثال زدنی راهی آسمان اربیل شدند .
@PARVAZDAROJ
| 𝐀.𝐑.𝐀</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/16358" target="_blank">📅 13:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16357">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6d3c48e2.mp4?token=M3N4g7MHaRqAEnpoCAytqWr0XKgmSeRdzA9viyfz5y7MPzqvvunCo6HLsWCZi_eFHfE057A3hzuftm3nvqo8c6_yrd4tIfBithn5KRebQPLCpGGhzZUYdhkc2jVvLZWRdVpLfrao5Y_BjsXTtTz6RVyC9L_XgDw3Xdw_kvgOfyNiLgwII4w8rKqwKhWro8GCayMXKZdJfYbAbX6pbiHftn9fjaHKbL3EP3vHdUaa0rkHVP0mINcfe3ibod9Ct_O_WKpOEfESeKyTrS3rzhwE75Q-hpnwpY6HvikT-51DP5VzxZweNOZTsWK5jVIQNMnaDdbJl25nZMkRuatbXikBVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6d3c48e2.mp4?token=M3N4g7MHaRqAEnpoCAytqWr0XKgmSeRdzA9viyfz5y7MPzqvvunCo6HLsWCZi_eFHfE057A3hzuftm3nvqo8c6_yrd4tIfBithn5KRebQPLCpGGhzZUYdhkc2jVvLZWRdVpLfrao5Y_BjsXTtTz6RVyC9L_XgDw3Xdw_kvgOfyNiLgwII4w8rKqwKhWro8GCayMXKZdJfYbAbX6pbiHftn9fjaHKbL3EP3vHdUaa0rkHVP0mINcfe3ibod9Ct_O_WKpOEfESeKyTrS3rzhwE75Q-hpnwpY6HvikT-51DP5VzxZweNOZTsWK5jVIQNMnaDdbJl25nZMkRuatbXikBVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اعلام_وضعیت
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/16357" target="_blank">📅 12:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16356">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9JBFXkEWa3mrwlVaJ2LLfyfCHOsMANXsfWk7EsYuQXw4T0s1dPb0NQ0knI33DtenaikTT7pQ6PjuulOe_a_GGXIfRdUkUlbQimf9MnNJ3ZYtAbYS8a59TDnfrnJvlu6D8WTeV72S0Q8O7oQRPp1-qHkowxhxTypveS41uevybuMQhoLkRFPLa6M6m6D8tGuT_bTBsue9fRBOsB8L33Lg0mHDB8ksN_DPaZIJb0EDQiJFlb817In7rlqIV9ShYuE6xdTsRPKZuEfGcER_mS4kITwBocUa-ga0nLMk1UskqM2Ravuj2L0JZDVuePp6R-mgp3oYExp_hEX0Nic1QWyAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب گویا شماری از مجریان صداوسیما فاز امام جمعه بودن برداشته و با سلاح در برنامه شان حاضر شدند!
سبحان الله !</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/16356" target="_blank">📅 12:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16355">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نتانیاهو.pdf</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/16355" target="_blank">📅 12:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16354">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">به نظر می‌رسد ایشان از خوانندگان Secret Box باشند.</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/16354" target="_blank">📅 12:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16353">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4117d0b4d4.mp4?token=oZrchDIX2cmrsp90Vcwh4Eyw63BcRWsLUCVylRz2fT5mCHDoP3ghpJv-zI_a-eCIp3oYjU0gBXGhNaTKJlGOJxPGg6bhMixUDKSwO_hlYOnq1dDEmjKsDEYkiroc8ThX6lffDPXrghlN6zL_c2kWjdk1FpjVB-xEbFY_zWsI3iwkj-_lTpDp8f7gcEGdWIvfDDfunURhefDGwdgmfqZQE2buga2dJX_zIQXa1OSQPWEH4v3ntIqB9NPTjKWENe0Z58GNnV7rJqDJLR2EQjkW-afhIyQbg5-ZxZh9LqFNlaxqqNriX7pvkDHbRCAEZpTNjQXChf3AWCiZCCsGE9S0-ZUChJe3AYJpvKaRaWUYJuk8FsF-9z7wRN5UXWkB_Msir206KzdGMAFye4ThWJxvsEL4lIuGf9BAxUgTymhOBEGWtoKcHzxjP5a_8oEvJclncIhZLRobm8ALmTffLntk49ae_DXEPqdl2Yxrz-uxRDPu6UVhiZZOmeDjp0rozy1y_ARIGoYHl7jKZusghJPNNn5Wu-i8Y3SNcRDFGydLdtnt3iGpPj6vxZf994SQoVGbQbxJVWadkvOP9ZVUdWOxhZNsAvD-7QHHxgF62-d_h8_OrI0ohxDlFlz1hXBhhGojJhBh48RdjW-Bn2Hd3j8kku1Bl2vKM1C2I2X1nMdio4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4117d0b4d4.mp4?token=oZrchDIX2cmrsp90Vcwh4Eyw63BcRWsLUCVylRz2fT5mCHDoP3ghpJv-zI_a-eCIp3oYjU0gBXGhNaTKJlGOJxPGg6bhMixUDKSwO_hlYOnq1dDEmjKsDEYkiroc8ThX6lffDPXrghlN6zL_c2kWjdk1FpjVB-xEbFY_zWsI3iwkj-_lTpDp8f7gcEGdWIvfDDfunURhefDGwdgmfqZQE2buga2dJX_zIQXa1OSQPWEH4v3ntIqB9NPTjKWENe0Z58GNnV7rJqDJLR2EQjkW-afhIyQbg5-ZxZh9LqFNlaxqqNriX7pvkDHbRCAEZpTNjQXChf3AWCiZCCsGE9S0-ZUChJe3AYJpvKaRaWUYJuk8FsF-9z7wRN5UXWkB_Msir206KzdGMAFye4ThWJxvsEL4lIuGf9BAxUgTymhOBEGWtoKcHzxjP5a_8oEvJclncIhZLRobm8ALmTffLntk49ae_DXEPqdl2Yxrz-uxRDPu6UVhiZZOmeDjp0rozy1y_ARIGoYHl7jKZusghJPNNn5Wu-i8Y3SNcRDFGydLdtnt3iGpPj6vxZf994SQoVGbQbxJVWadkvOP9ZVUdWOxhZNsAvD-7QHHxgF62-d_h8_OrI0ohxDlFlz1hXBhhGojJhBh48RdjW-Bn2Hd3j8kku1Bl2vKM1C2I2X1nMdio4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها مواردی است که اسراییل را به سمت یک راهکار نهایی پایدار منطقه ای بوم پایه  — بجای آویزان شدن از غرب (و خصوصا آمریکا) — می برد و کریدور داوود و پیمان موسوم به کوروش و … در چنین بستری معنا می یابد.</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/16353" target="_blank">📅 12:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16352">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">۸ سال پیش …</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/16352" target="_blank">📅 10:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16351">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">استوری مشاور محمدباقر قالیباف</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SBoxxx/16351" target="_blank">📅 10:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16350">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR6k0LKaoUiK4uKNFUNv35WhB8wQms9DGTa4WND53fTnuS_lgyedDhiRu2idr4s795JJOU_ze7-FFBgRov1lBZAx9x-8wyGezJ91QE1n5QAFDxAbCxeUOK5S1hNCLnnXFjWc26DOVAcledCkBhFN-hRmZFv1x_-9ibUReEI8vqScDq0SuDIxasSdZxaBQsgTmjyvzTxmJSgG23Zc_QQitho53bG9BdlcboouS7gME9UKWw5ZcRxY0hS_kc-1NiNwmLSWl8j-o3lSH8PUFIhI3gKcQ8MpwJr8HBPVQhe9_vXaC4Tt9xKhv2gMhcd1lIEemCyfe6-1vZsAYw4M6-w4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ خیلی صریح محمدباقر قالیباف رئیس مجلس ایران را به ترور و حذف فیزیکی تهدید کرده و او را "محمد یه چیزی..." (Muhammad Something) می نامد و با تمسخر می گوید اسم نصف ایرانی ها محمد یه چیزی است و ما می توانیم آنها را از فضا شناسایی کنیم و اگر نزدیک منطقه ذخیره…</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/16350" target="_blank">📅 10:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16349">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpGpz5FcTjVlXx7bsaC4pOZcRWuAHjnDJjpXtq8lWRHHLpGkZqEfUkH6QzNw8-TlCh4iRYEH3umJVqrZj9gzsU_ieNnLFtQOqZwI-VS64bijZ35Aji-nEQhz0rrlZpsEbp07lJY0Pjc8q-Vd-6iE_V5v2Du4yJ-_dNq3VLIREm9bRM3oK6vwcVy8mWJMZfDacU1ydjNaEdGPj2iy--p6nOf4tPQ_gUNUiaOFzYWCj-Vp-GS67EltXOIGSK5c9GpRkA3tMnNgwRDvLd1oQqO8rFls9KLZaY9lLA0K6u8bgprN_kkh6-tjNOmKEvn6vRiFthjJErnXBfhOL3l8R-SjDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ خیلی صریح محمدباقر قالیباف رئیس مجلس ایران را به ترور و حذف فیزیکی تهدید کرده و او را "محمد یه چیزی..." (Muhammad Something) می نامد و با تمسخر می گوید اسم نصف ایرانی ها محمد یه چیزی است و ما می توانیم آنها را از فضا شناسایی کنیم و اگر نزدیک منطقه ذخیره…</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/16349" target="_blank">📅 09:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16348">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ خیلی صریح محمدباقر قالیباف رئیس مجلس ایران را به ترور و حذف فیزیکی تهدید کرده و او را "محمد یه چیزی..." (Muhammad Something) می نامد و با تمسخر می گوید اسم نصف ایرانی ها محمد یه چیزی است و ما می توانیم آنها را از فضا شناسایی کنیم و اگر نزدیک منطقه ذخیره…</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/16348" target="_blank">📅 08:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16347">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37f23855f2.mp4?token=CMrciAQPmXR1iv6oOBwAYKE96XJwetUXileY2QZSSYwPrXZYr1WV8c1huyLQTHDpSkbq3skGMBVhaEk6gxDTHVDUuQvx5XyRiyDGXIzJ4lLfTvaT2_n96bFR0XKU7Lh070kEO7BP8pLYxzrFuPD9V8U4M6fDoTKurhtg9Ujt9__8lHQmaip4mxh80ZwIGNShF5bkh-uQmCNpeOC7dzxifrIbFi0vNlMd1v3CderlFaOW4ZQzNtBWHMtRVkbl1b92YBREIv1i46RL8-ILTF1pZGYZRM11dGOEhp6YLHjK4EncA3b8SnK_LaF3fUKeWjKJSvEbUSUb6inTA-66Szjw9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37f23855f2.mp4?token=CMrciAQPmXR1iv6oOBwAYKE96XJwetUXileY2QZSSYwPrXZYr1WV8c1huyLQTHDpSkbq3skGMBVhaEk6gxDTHVDUuQvx5XyRiyDGXIzJ4lLfTvaT2_n96bFR0XKU7Lh070kEO7BP8pLYxzrFuPD9V8U4M6fDoTKurhtg9Ujt9__8lHQmaip4mxh80ZwIGNShF5bkh-uQmCNpeOC7dzxifrIbFi0vNlMd1v3CderlFaOW4ZQzNtBWHMtRVkbl1b92YBREIv1i46RL8-ILTF1pZGYZRM11dGOEhp6YLHjK4EncA3b8SnK_LaF3fUKeWjKJSvEbUSUb6inTA-66Szjw9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ خیلی صریح محمدباقر قالیباف رئیس مجلس ایران را به ترور و حذف فیزیکی تهدید کرده و او را "محمد یه چیزی..." (Muhammad Something) می نامد و با تمسخر می گوید اسم نصف ایرانی ها محمد یه چیزی است و ما می توانیم آنها را از فضا شناسایی کنیم و اگر نزدیک منطقه ذخیره سازی اورانیوم غنی سازی شده بشوند، شدیداً به آنها ضربه خواهیم زد.</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/16347" target="_blank">📅 08:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16346">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ: ما به پیروزی کامل نظامی بر ایران دست یافته‌ایم</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/16346" target="_blank">📅 07:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16345">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J23auPlQM6rn1IG1NbUJUZxjExyvpdQQ3aHi2cc2DYYOXYqdrZcRXaH9qVY7hmGWfXF9BpL8Yra5QyY1R3Jwod6zq6SSmfgyrOPpCmk3FEIPYk6IUAWal_yAycu4OAHXmP3ympHhHeaOan1WgPwZRfJzRKX_7Ix7QLOsOh_w71h1K-l0ZDLTf_ZcV2N8dglBy9oAsNQaoPf9WTjGGiwaxtFqDl2WPQGHs8F0-PmHOjP4hel2rufTkSEYoXmli0ZZ7diS82QrmgPYI7wqkb1zTthfFVa_GaRWcbOpCeyGo72JQPcK-o6HID_2Zxr8basjmjT49QqsqnoQ5gWZDWKDwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستوفر نولان این خانم را برای نقش «هلن» در فیلمش درباره افسانه اودیسه برگزیده و ایلان ماسک هم با گفتن اینکه «نولان با این فیلمش دارد به قبر هومر می شاشد» از خجالت او درآمده است!</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16345" target="_blank">📅 02:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16344">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">به نظر معامله بزرگی در راه است.</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/16344" target="_blank">📅 02:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16343">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVjVJxT-H4tU5oVQYH5k2J-QmWhAC_rSMzyp29rMPziNrGkuCPWz5gRROnXbcgDA6_7Y8puAV-MLcPh9xb_M3RnPgXyW1suWuJmfgGTAMcImbdFnF2AY4kfetc652wWQiOBni5P6s1ZVWlBrt-f9GbLKtU244kxBxO1bs-HcE4Szc2PX7vi8YdriD9onivDJj2sdB7WbjI5rHqO3gD_yF_pp0vDPQNwzSWM0GkXKBRzhtUEP-hLyzPHmZyVoLj5uJJAZ3tJAMiqBcSfIoTFH845g13GXimE5WW9GtEfkgQhd5ra5dQLICNfh3pnDwR3lZtg5OIVjtNDnyIZlr4vQWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تأثیر منفی بسته شدن تنگه هرمز بر سیاست‌های پولی غربی: اهرمی برای ایران   بسته شدن تنگه هرمز می‌تواند با افزایش قیمت انرژی، بانک‌های مرکزی غربی را به سمت سیاست‌های پولی انقباضی و نرخ بهره بالاتر سوق دهد.  افزایش فشار اقتصادی و تورمی بر کشورهای غربی، ممکن…</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16343" target="_blank">📅 00:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16342">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حس میکنم دوباره سوی شیر گرسنه دارد گاو می آید که ولی خب.</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/16342" target="_blank">📅 23:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16341">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فرانسه حضور ناو هواپیمابر شارل دوگل در تنگه هرمز را تکذیب کرد</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16341" target="_blank">📅 22:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16340">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فرانسه حضور ناو هواپیمابر شارل دوگل در تنگه هرمز را تکذیب کرد</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16340" target="_blank">📅 22:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16339">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ مخالفت خود را با اعلام رسمی استقلال تایوان ابراز کرد
من دنبال این نیستم که کسی مستقل شود می‌خواهم آنها آرام شوند. می‌خواهم چین آرام شود.</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/16339" target="_blank">📅 22:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16336">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5m355BbWMNnCDOY3mITOvBjwysx8kS28EFadlYERat2mLmXbnmDKHa0qDYhHiqaC1TtD5yOxSqfR_1IuIBO_uJ502aTqtV46ClIwAt-TvkAJTC0BjXNSutj3b2YoV7MEGGsej6hN9VGry1CA-HQoTVaUNdQKwQvvi_aEtHGgAqxsG_wJvGzrpLTaimSY5qs9fDDY9VaS8vDEHLJlEXBkL1J6j1mCIqys8RhWPg3I03MQtIKLW0Jlv0t94DLAdVnQFO9Uo4QbO5n-nBVI3X01XFTr2u8xEcqHFp4BSY99wcbK0INrBlcbncze6Zbg-6ATX8knAjb2ow-ug-LeY1bHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:  عزالدین الحدّاد، رهبر حماس در غزه را ترور کردیم.</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16336" target="_blank">📅 21:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16335">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نتانیاهو:
عزالدین الحدّاد، رهبر حماس در غزه را ترور کردیم.</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16335" target="_blank">📅 20:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16334">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ولی خداوکیلی راست می‌گوید ، هر چه آدم توخالی بیسواد عقده ای که با قر و فر جلوی دوربین توانسته نقابی فریبنده برای خودش بسازد، در اینستا لانه کرده.</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/16334" target="_blank">📅 20:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16333">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">میرزا ایلان ماسک السلطنه:  اینستاگرام برای دخترهاست!</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16333" target="_blank">📅 20:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16332">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ای ایلان، ای مرد پرگهر !
ای ایکس ت سرچشمه هنر!</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16332" target="_blank">📅 20:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16331">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">میرزا ایلان ماسک السلطنه:
اینستاگرام برای دخترهاست!</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/16331" target="_blank">📅 20:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16330">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شاید ما برخی کشتی ها را با پهپاد زده باشیم، برخی ها را با موشک بالستیک، برخی ها را هم با موشک کروز.  خب اینها می‌شود تفاوت‌های حملات ما.  اما یک شباهت بزرگ هم میان همه حملات ما وجود دارد و آن اینکه کشتی مورد تهاجم مال هر کشوری که باشد، دستکم ۲ ملوان هندی در…</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16330" target="_blank">📅 19:34 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16329">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/16329" target="_blank">📅 19:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16328">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8TvbbygymOqNbwXShdxODkNykebAM8wZdhxC8SizRyj7yBpmgxNRAo9kT_zLgsjywPWwUx_XLqSkirf60wHUiKvU7pDS6d2obKOqVholOMRq_4yGlGvZXfzFgD5RMkiiIJkBsiU2CDhig0pEgSoGlzS_w1APIZhOGCwlX2Xdxxl6X7nH03QgS5y_OX5B6M5URZNISkWiXjfJzvpxg--EfbAfmIoFTm3kPAvP8ptiDjsgz2D36vxfNmNAHM0BrjKn_AxB1H7SqYS6EP7U3LaAacgE4EEIvMdLkD4VYwz-E8y2ZTE0O2gbDfwvPfD19tEiR4BfUu00j93U8Bx1sw36Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تأثیر منفی بسته شدن تنگه هرمز بر سیاست‌های پولی غربی: اهرمی برای ایران
بسته شدن تنگه هرمز می‌تواند با افزایش قیمت انرژی، بانک‌های مرکزی غربی را به سمت سیاست‌های پولی انقباضی و نرخ بهره بالاتر سوق دهد.
افزایش فشار اقتصادی و تورمی بر کشورهای غربی، ممکن است به اهرم سیاسی مهمی برای ایران در مذاکرات و معادلات ژئوپلیتیکی تبدیل شود.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16328" target="_blank">📅 18:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16327">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODNxUuIp0YY79X2gzux6QHWWl-kUivMU8R_1hw7Li5DefYxT3-_5FtL1S6MEk5aHbH5VkvIF9RdXrLVO73XHjkmcAyo08WgGBPORDIIGfS089NWqo8MBh8hK0zCNuCtXn3iG4XRvLWtdM6A_aPbb62sUuhd9xK_V1Bp2QuUcTgWOW_MHm7R8GIA7e5W3Jw-GRts2bfz1fKipbGzU3tHiRGYdLp0dedgQJeWPR3ca69HzhfPQxsjH6yKC_jKq03TXhApl-QLeLS_9FG7f3bfmvIM3aveColNLD8tqZu0-2zqZ8i0ofrwDdVg_xbxTg1-JSOqPq7o8ZPJfTZipYWn-DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی ؛ وزیر امور خارجه دولت :  پس از تجاوز آمریکا به ایران ، کشورهای بریکس به چشم دیگری به ما می نگرند</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/16327" target="_blank">📅 15:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16326">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qq84FtlkZ8C_-V4tpQ2CkrcjEYEucDmwL8Yt1pt-LqkqfQqAH0xLIfrYqqhgiyb7sT4yQhsL_6yT2gHLeqXEOFSEPk1odNQJBtzzmWF8Bdufg6_qn58cegg1hGucOMWftLL-5tVaa4c5JusNog6e71XKFo2w2x23itNdD0XVfgeApDLQ-OzM32NWb4I4hvdkSxYzEx25hT5nkJ6-yc1hoZB6-LVboYKGCrpInK6uKeGfbG2I2uRmb6v9xv9er06WQeJj94FwwgxI13-rtfY15qC3PZTM3yc11JtiwRgr9NtiGFbjq5KiPjJ4eSVzWdriwKc9mnCuklId4aCj3qeepQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بحران نیرو در اسرائیل عمیق‌تر می‌شود: ارتش اسرائیل به هزاران سرباز جدید نیاز دارد
۱۵ مه ۲۰۲۶ | پیترو باتاچی
در سخنرانی خود در برابر کنست در ۱۰ مه، رئیس ستاد کل ارتش اسرائیل، ایال زامیر، بار دیگر بر لزوم جذب سربازان جدید تأکید کرد.
وضعیت ارتش اسرائیل:
ارتش اسرائیل طی سه سال گذشته در سه جبهه درگیر بوده و اکنون نشانه‌های خستگی را نشان می‌دهد: نیروی فعال عالی آن فرسوده شده، در حالی که عملکرد نیروی ذخیره در سطحی نیست که انتظار می‌رود. به‌ویژه، بسیج مداوم نیروهای ذخیره، منابع انسانی را از اقتصادی پیچیده و کوچک اسرائیل — که فاقد عمق استراتژیک است و در چرخه‌های جنگ طولانی مدت آسیب‌پذیر است — تخلیه می‌کند. بر اساس اعلام ارتش اسرائیل، ۱۲٬۰۰۰ سرباز جدید به‌صورت فوری مورد نیاز هستند، به‌ویژه برای نقش‌های رزمی عملیاتی.
یکی از راه‌حل‌های پیش‌رو:
اجباری کردن خدمت سربازی برای یهودیان فوق‌ارتدکس (حریدی‌ها) است که همواره از خدمت نظامی معاف بوده‌اند و در حال حاضر حدود ۱۴ درصد از جمعیت اسرائیل را تشکیل می‌دهند — سهمی که با نرخ زاد و ولد بالاتر از سایر جمعیت یهودی، در حال افزایش است. در ژوئن ۲۰۲۴، دیوان عالی اسرائیل حکم به لغو معافیت آن‌ها داد، اما از آن زمان، حریدی ها به‌صورت سیستماتیک به خیابان‌ها آمده‌اند و عملیاتی شدن این تصمیم را به تعویق انداخته‌اند. برآوردهای اسرائیل نشان می‌دهد که حداقل ۸۰٬۰۰۰ مرد فوق‌ارتدکس بین ۱۸ تا ۲۴ سال سن دارند که واجد شرایط خدمت سربازی هستند.
کمبود نیرو برای ارتش اسرائیل:
واضح است که ارتش اسرائیل با کمبود نیرو مواجه است و تحولات اخیر در جبهه لبنان نیز اوضاع را بدتر می‌کند. حزب‌الله، علی‌رغم ضربات سنگینی که متحمل شده، مقاومت شگفت‌انگیزی از خود نشان داده و اکنون با موفقیت از تاکتیک پهپادهای FPV استفاده می‌کند — توانایی‌ای که در مدت کوتاهی (با کمک چه کسی؟ وفاداران سابق اسد؟ روسی‌ها؟) به دست آورده و برای ارتش اسرائیل مشکل‌ساز شده است.</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16326" target="_blank">📅 15:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16325">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ: ما به پیروزی کامل نظامی بر
ایران
دست یافته‌ایم</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/16325" target="_blank">📅 15:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16324">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وزیر امور خارجه ایران: همه کشتی‌ها می‌توانند از تنگه هرمز عبور کنند به جز آن‌هایی که با ما در جنگ هستند.</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SBoxxx/16324" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16323">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وزیر امور خارجه ایران: همه کشتی‌ها می‌توانند از تنگه هرمز عبور کنند به جز آن‌هایی که با ما در جنگ هستند.</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/16323" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16322">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ: آخرین چیزی که الان نیاز داریم جنگ است.</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/16322" target="_blank">📅 14:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16320">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">از دیروز که رفته چین 2 عقب نشینی داشته ترامپ:  — اینکه به قول خودش گردوغبار هسته ای لازم نیست حتماً خارج بشود و همین که ایران دنبال کرم ریختن اطراف محل دفن آن نباشد کافی است.  — اینکه اصل غنی سازی در خاک ایران از دید او مشکلی ندارد.</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SBoxxx/16320" target="_blank">📅 14:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16319">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نرخ بازدهی و نفت به جاهایی رسیده بودند که فشار می آورد و شاخص های سهام هم نزولی شده بودند. از این رو لازم بود که کله زرد یک آرامش مصنوعی تزریق کند</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SBoxxx/16319" target="_blank">📅 14:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16318">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فوری | ترامپ: من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم، به شرطی که این یک تعهد واقعی باشد.</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SBoxxx/16318" target="_blank">📅 14:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16317">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فوری | ترامپ: من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم، به شرطی که این یک تعهد واقعی باشد.</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SBoxxx/16317" target="_blank">📅 14:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16315">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ژاپن معاملات تسلیحات مرگبار را در جنوب شرق آسیا پیش می‌برد  وزیر دفاع ژاپن، شینجیرو کویزومی، روز دوشنبه در جاکارتا با همتای اندونزیایی خود، شمس الدین، یک پیمان همکاری دفاعی امضا کرد، و پس از به مانیل خواهدرفت؛ جایی که نیروهای ژاپنی در کنار نیروهای آمریکایی…</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SBoxxx/16315" target="_blank">📅 13:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16314">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVjPc5pMvkmjQruhy2PtBJHiIIXnKZFLqGRnhHkBpGfaPqBM9jqvqjE6Ermmu7DFCte5T1Ex3vZ91NA7l-WONbWCxMIc4ROD5JgtmVAtT4wSfhj-tyyOSpOTSwpKotbAWkxR942vUFoZgVUPwluocvU6t9zj2eGfGjH_Idaw49DT0omHPj6Fq6vPWjNqRDG3nsbJPpkzuVO4M3AlIL8FkD_mfot8MFu74kcXis01RmnQTSJKeCcveKijFf5dGBQhNzCkhwfl1trIoYmF2HBUE-6gUamolRb1YADFDIYFQGxq3qW_-bmiSsk96CSfOaer4hHUGn8NkLRTolq3o3OsWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی ؛ وزیر امور خارجه دولت
:
پس از تجاوز آمریکا به ایران ، کشورهای بریکس به چشم دیگری به ما می نگرند</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/16314" target="_blank">📅 12:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16313">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/16313" target="_blank">📅 10:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16312">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTXpU-wCKFuuOLjNZszyBa1pcvAN0sx4f3tWDvaT96mnAy55PjX4RUX3THOq2iezx76D7y-Pa6F1QlobQYzCe2SOZjkwbV4CyyYkEUcQR3I4051vx-gBcsP64YEkfR05o8-ISya3YmMSl9Q7tTo3ajx8gz9ysTa1Zk-pja8ieJ5mXqA9hoBmmq2g1Jc9EH6NjmEcAWMC4W5-tDdb554jk_PrO6VaVV95S90N8eyuh21iiX2SB3cROUgqB_YLpP-We7ib2Sololr8YUlalkYGvGMFizP51ykDclRrYq1IEmAqy-PQNV1xdZGpebZBSt4kMfwMHqMzSLa31ju1TJOm0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستوفر نولان این خانم را برای نقش «هلن» در فیلمش درباره افسانه اودیسه برگزیده و ایلان ماسک هم با گفتن اینکه «نولان با این فیلمش دارد به قبر هومر می شاشد» از خجالت او درآمده است!</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16312" target="_blank">📅 10:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16311">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇸
🇻🇪
وزارت امور خارجه ایالات متحده اعلام کرد که «اورانیوم بسیار غنی‌شده» با موفقیت از تنها «راکتور هسته‌ای» ونزوئلا خارج شده است.</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/16311" target="_blank">📅 10:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16310">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Zaraban</div>
  <div class="tg-doc-extra">Shahab Tiam</div>
</div>
<a href="https://t.me/SBoxxx/16310" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SBoxxx/16310" target="_blank">📅 10:14 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

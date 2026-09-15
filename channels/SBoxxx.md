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
<img src="https://cdn4.telesco.pe/file/BjfPj7KX6zdKf3NV02GZLNjyl85NU2VQy8SSg67vDyI0_atc39munF3QTz39tLVW6V8nUnpw4j_MPRRIUhnuIS3nT445-c287SlJUH-O-TfiSSl5e_aCcwoxbus3sNrD-HWQtM6jAvQZ_jrGeFQbye5GRCaImdKOVaPlXIQ46kSf0nGwergajPSwcWq5DJEYbbOnfY3mYKSqL2b2fqmaMfIZvGv3kyURUZ20IZCJbLIwHhd4m9QDjfUKwzKdmEdqJQiWZrhpT5ozdrcPDdYbsRVZ9iAbyt2SjHt8uNVqVtaEf0MrtUvbcm7DnFT_0BYpCYPiVaCs8yCQV6Gtu2D8OQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.8K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 19:33:43</div>
<hr>

<div class="tg-post" id="msg-20918">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">عراقچی فردا به چین سفر می‌کند</div>
<div class="tg-footer">👁️ 800 · <a href="https://t.me/SBoxxx/20918" target="_blank">📅 19:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20917">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آکسیوس:
یک پهپاد آمریکایی پس از تلاش سپاه پاسداران برای توقیف یک پهپاد نیروی دریایی آمریکا، دو قایق کوچک ایرانی را در تنگه هرمز منهدم کرد و اکثر سرنشینان آن را کشت</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/SBoxxx/20917" target="_blank">📅 18:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20916">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بارگیری نفت در ینبع، مهم‌ترین بندر عربستان سعودی در دریای سرخ، به دلیل حمله قبلی به خط لوله شرقی-غربی، متوقف شده است. (به نقل از خبرگزاری رویترز)</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/SBoxxx/20916" target="_blank">📅 18:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20915">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بارگیری نفت در ینبع، مهم‌ترین بندر عربستان سعودی در دریای سرخ، به دلیل حمله قبلی به خط لوله شرقی-غربی، متوقف شده است. (به نقل از خبرگزاری رویترز)</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/SBoxxx/20915" target="_blank">📅 18:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20914">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.  بهترین محدوده خرید از 4280 تا 4250 می باشد.  نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم…</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/20914" target="_blank">📅 16:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20913">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.   از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SBoxxx/20913" target="_blank">📅 16:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20912">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jb7ZovA08FjrZON8WUL9rlWmpSmX74FSHvCcBpzoJEv4PSxsrAJPGILZp9yNBolM8m2sh9K66FfI_nrhuTv6B8T295Vh0UgwX0iXyEAs9uj_LizIPkoUeF9h_i-sDfWH1m_2OQCVJjmDeFL3Dm0sCennlqdDO1bpSQ8E8WdeTb4ZCPqFmJJ4rOquklfP6jjuynBkoehPvYOdEKs8ijtnqmqyRPvyyb9g8XG_LFFUDqGOypYUGVcbwTWAEqizqeBwXqv74Q5uopliInAP5iSdlL1IHly7Y558h12jvXHVxwcWhoKmdoqMDAMXoTKXJQo8WARmG95oN1HD7DFa6HJipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سخنگوی پویش جانفدا :  جان فدایان غیور صرفا برای اهداف نظامی به کارگیری نخواهند شد ، به زودی پیام های جدیدی را به این عزیزان تقدیم خواهیم کرد</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/20912" target="_blank">📅 16:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20911">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.   از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SBoxxx/20911" target="_blank">📅 16:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20910">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SBoxxx/20910" target="_blank">📅 16:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20909">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">به نظرم بین اسراییل و ترکیه و پاکستان یک تورنمنت سه جانبه بگذارند ببینند کی می‌تواند برنده شده و بیشتر گاو شیرده حجاز و نجد را بدوشد!</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/20909" target="_blank">📅 16:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20908">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رسانه عبری والا به نقل از منابع:   تماس‌هایی میان عربستان و اسرائیل با میانجی‌گری فرمانده سنتکام انجام شده تا از طریق ارائه اطلاعات، به سعودی‌ها در دفاع از خود در برابر انصارالله کمک کنند</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/20908" target="_blank">📅 16:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20907">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SBoxxx/20907" target="_blank">📅 16:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20906">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در سوریه با گران شدن سوخت، اعتراضات مردمی آغاز شده و آشوب ایجاد شده</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/20906" target="_blank">📅 15:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20905">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 27</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 27
سه شنبه 15 سپتامبر  2026</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/20905" target="_blank">📅 13:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20904">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گویا امروز برای ادارات و نهادهای دولتی ابتدا کد 100 (تخلیه فوری) صادر شده و باعث ایجاد اخلال در کار ادارات شده و بعد از چند دقیقه وضعیت سفید اعلام شده و با اعلام کد 69 همه به سر کار همیشگی خود برگشته اند.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/20904" target="_blank">📅 12:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20903">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/20903" target="_blank">📅 12:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20902">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1_6u1xqm-Q2HlH-4hBnIUS49B1WRsT5nvf4V5xB0TaD0hMSwJi1064VBa3i8Kq26SuyerBwhurDW8BTAdWaTcK1fvqmS8wvReg9CMAnJNPyQWgs8NnHQWjUQpv2RKLbvhymLLi_C7nclj8nL3yZTgYk3ClZl6FfiUX3xVGs0Fhd345K234Mhfe2Lxx0G-TBew1Jd_mno5oGvDDoNiqWaJRJbcu--F2T_6pfbAArdXnG5ymtRAJu-ty9m7HsxibgGKKGTcEINPLMoos00YTjIOPN75acKsANQF_zvZCOan9dOPR4ezjFyxyJ3SXzo_jvlN8f025JGVYlB1H6tUHvcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20902" target="_blank">📅 12:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20901">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPDzmA_hnu5d7jaLH6Rp88R74kTaku1dWp8D92VpeL9Lh4eHmrnh0lf8AcWR6yZBk110EvYs2AwYIzqsJChuKrCmYwJP4CmQZu8iHJCJcyA05gXWS0b75wL2c7G3-Yi_oF19YVkFNyLb-VNWu0WqMrk9h4mXXQWneIpeDc4XXiRAoknyvfEEllS7pHzbdm7vvUU8Rm9_K8BBV-DITvsyAtpJMVCj-7I_pz29rlcD2Zkw8XZl-TnSiVRH_RvDANlkAvK5E2EekRLNe89S9H6SsT2YInUGmJmqzrc3Y6341Isxa8JKdqKKt7ylXIT8cVO2m36vqVSXiHRtMHrYpsCTKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال: کمک ماهواره‌ای چین به ایران  به گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی می‌گویند ایران پیش و پس از حمله موشکی ۱۷ ژوئیه به پایگاه «موافق‌السلطی» در اردن، از تصاویر ماهواره‌ای با وضوح بالا از منابع چینی استفاده کرده است.  در این حمله…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20901" target="_blank">📅 11:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20900">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHp1FGEld3iXbUs433VVLtpCl3sMJVtsZ_zm_NqNf_qMhHm7dljSKY56T947SEroZsxU0ZnbxeRu9qz4XXfFtZS20H9lb5tXI6jE0R8pDb4ywcppacpmeu0B2N6hMTyU6wFT6Ckz_IUEqUf9th6AekIRkyvuBxbyizjONo8Vu5xmwjNf85NfCYS8u1XnvuqCxSDrgK8F3bvavFqmOgHDX1wGnLeB21_zPgJ1zfKuO5zqyF-rdjrW3Hxj_OuE4X0fB5ltplKV0N72CWdbxl71zd2N7s_9C073FdX_kVgdC6kT0dO620VP0vor7_fYJbS6jldzY66e-e7tVcu8oZZ3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/20900" target="_blank">📅 11:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20899">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDSWMCoCr6vFgeKJmN9HAg60sxoni_i6vz7hxtnIGKs5K77Cr5BrF8Jte9wrJOuESxCBGC0HVjVKKsu0ZxUHf-5O5qCP7_AEa5au4KW7y4xbI-IEuuz_YEIwIDj0--8W-AnfkfE-MRAMycOdw09BxOJ1UVc39gFR35qMHjhumDlDhFZrl4l8-ANgNMX7XnD9YTqFrkwemKMXRKdlxEyuKr8dHkfzKbMSAyu-TP3JVvV1-ohTQ6SlusgacLw2AUnFbuTh1zccWgbeZGEdEDwvn8ma_LyKEoaRVTQLtqHMWVBayhHa5i1SZ0zvsQ3m_N-EwKACBrrvoKkIH6vLhG4MPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.
بهترین محدوده خرید از 4280 تا 4250 می باشد.
نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم و پیش بینی میکنم این هفته طلا سطح 4400 دلار را پس بگیرد.</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/20899" target="_blank">📅 11:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20898">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZwVE6Gj8bw_KmPylRpTSaaGsoZl3AhLZOKwX3k7LLrysMFmmHjj2YtuZJXIE2f3fgFxb0WeRNjWTDvSam-LbgjiUyzc7rHEJlqeHVhDYMlQgCDsXi_CPdvVTWnS1XN1bFKlZjOCtI4Y2UGVOZF10agAOf7yMJrVwmehE90-1aNS6zFjWAeHI5o0Cyoi-4irC0hCW9pPMDU1xpM5-awSXXPFs8cpLLj9-zfiPYVUdxjsfbWu6MxZ0CwvYHg60v7y6aof2i4yHS0b0kzTINmAl2RKG846FBuIGxp-u_e8YhkL4Uo_b6wrhSo29LAkQxISeWid1XC_7jJApj0U4QiOfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح نسبتاً بالایی است و احتمال فراوان هر بالایی فراتر از 4300 فروخته خواهدشد.</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/20898" target="_blank">📅 11:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20897">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoyffGNg-bna42I8pDn_AJLBfwd-XoNnNPdof_FT3Kz6w8ij2V97DUZ6qmXTX0P2OxaLS_cUmfgIWkXUVMm7AyeXq3Zz1ffHGQ9KPm-FBAZt7Uww2nCXUalLU3S9i1R4Cbf2-2Z7FeYZFw0a8My7ofVIBZ09TaV3aN2X1GdA1HXBpvcDz7ZlQKH0sIwE4gjbRf5wQqg_CAOXRp_WKSqUqYioWCNeNBbfZOqs9gMdlW_iM_mCA6-Nquf4OXvtbl9KKZ7-0UfoGy0xUC64sbS2RA1Z3nfx6j_7fwKNHyZdnBEnb1IptgAngibYE1wLFg-FrbWBc35Jn94SZd2ebXKkzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله حوثی ها به عمق خاک عربستان در ۱۱۸۰ کیلومتری مرزهای یمن!
و کماکان از متحدین پیمان مکه (عثمانی و فاکستان) خبری نیست!</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/20897" target="_blank">📅 09:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20896">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">جمعی از نمایندگان مجلس در بیانیه‌ای خواستار تجدید نظر عضویت ایران در NPT شدند</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/20896" target="_blank">📅 09:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20895">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">درخواست کمک عربستان از انگلیس برای حمله به یمن
بعد از مخالفت آمریکا با حملۀ به یمن،‌ عربستان سعودی این‌بار از انگلیس خواست که در این کشور مداخله نظامی انجام دهد.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/20895" target="_blank">📅 09:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20894">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یک بار از یکی پرسیدند تا حالا اتوبوس هل داده ای؟
گفت نه ولی یک بار تو اتوبوس هل شدیم دادیم!</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20894" target="_blank">📅 01:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20892">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آن‌قدر به ما گفتند ترامپ تاجر است که قبل از جنگ به آمریکا پیشنهاد همکاری ۵۰۰ میلیارد دلاری دادیم!
- حسن قشقاوی، سخنگوی کمیسیون امنیت ملی مجلس</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20892" target="_blank">📅 01:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20891">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXR3z13PTmMJPkVEFpkWLx62P7X0ILsFyb5Hu8DaVEv30yJeMj3AiQ5c6Sceu4p6S2DEl-wuFMf3DwTq9M7y0c9PjCe6r5Zz-Ypj3uvm2iQwtySMeeZdVYm4YZpf29viMeVtQqjiUPBOnnjtz_YoOdmqRpv9JHHIr3BSXJ8n7aWKCRlYXLhmPwTaiNU9hdyWXijC_apAqx9YQeaSKP7ui6s92QblAyqsdnLURXWv477un8tHJi1egOJcltefJ-d4dpv9mYDIeI9QaqwOGutb9PGlsvTdkcsW0zGb2Nq9Al_jxdkRxj99uhjkgnBlsorJDIZY35crzQ7PxR6lplD9Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
💙
😀
💙
😀</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20891" target="_blank">📅 00:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20890">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">برنامه ریزی آمریکا و عربستان برای حمله به مواضع تازه تصرف شده ارتش یمن در ساحل غربی
یک منبع یمنی وابسته به مزدوران سعودی اعلام کرد آمریکایی‌ها به عربستان سعودی در مورد مناطقی که مزدوران عربستان آن‌ها را از دست دادند و مشرف به باب‌المندب هستند، فشار می‌آورد تا این مناطق را پس بگیرند
در پی این فشارها عربستان سعودی با کمک نظامیان آمریکایی در حال طرح ریزی حمله ای به مناطق تازه آزاد شده ساحل غربی با نیروهای سلفی و سایر مزدوران است
این منبع اشاره کرد طبق دستور آمریکایی ها به بن سلمان این حمله بزودی آغاز می‌شود.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20890" target="_blank">📅 23:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20889">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پزشکیان:
برخی کشورها در خفا به ما می‌گویند ما با شما هستیم اما در عمل از آمریکا حساب می‌برند و جرئت همراهی با ما را ندارند</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20889" target="_blank">📅 22:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20888">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پزشکیان:
آمریکا چون نمی‌تواند رهبر ما را پیدا کند درباره سلامتی ایشان شایعه می‌سازد</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20888" target="_blank">📅 22:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20887">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران ایران اعلام کرد که نفتکش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در بخش جنوبی تنگه هرمز، با یک مین دریایی برخورد کرده است.  سپاه پاسداران می‌گوید تلاش‌ها برای مهار آتش‌سوزی ناشی از این حادثه بی‌نتیجه…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20887" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20886">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران ایران اعلام کرد که نفتکش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در بخش جنوبی تنگه هرمز، با یک مین دریایی برخورد کرده است.
سپاه پاسداران می‌گوید تلاش‌ها برای مهار آتش‌سوزی ناشی از این حادثه بی‌نتیجه مانده و این نفتکش اکنون کاملاً در آتش می‌سوزد.
آن‌ها تأکید کردند که تنگه هرمز همچنان بسته و «تحت کنترل هوشمند» آن‌ها قرار دارد.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20886" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20885">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گاردین: طبق گزارش ها نخست وزیر بریتانیا در حال بررسی اعزام ناو های جنگی برای حمله به حوثی ها در کمک به عربستان سعودی می‌باشد</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20885" target="_blank">📅 22:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20884">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">روسیه و اوکراین دارند با پیشنهاد ترامپ برای تعهد به نزدن تاسیسات انرژی یکدیگر موافقت می‌کنند</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20884" target="_blank">📅 19:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20883">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20883" target="_blank">📅 19:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20882">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ادعای ترامپ:   ایران به شدت می‌خواهد در سریع‌ترین زمان ممکن توافق کند.  من تعیین خواهیم کرد که آیا وارد مذاکره خواهیم شد یا خیر، و این گزینه‌ای است که نسبت به آن پذیرا هستیم.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20882" target="_blank">📅 19:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20881">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ادعای ترامپ:
ایران به شدت می‌خواهد در سریع‌ترین زمان ممکن توافق کند.
من تعیین خواهیم کرد که آیا وارد مذاکره خواهیم شد یا خیر، و این گزینه‌ای است که نسبت به آن پذیرا هستیم.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20881" target="_blank">📅 19:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20880">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">محاصره اقتصادی | فعال شدن گروه های جدایی خواه</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20880" target="_blank">📅 19:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20879">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اینها تغییرات بسیار بزرگی هستند اگر خوب دقت کنید.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20879" target="_blank">📅 17:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20878">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!  محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20878" target="_blank">📅 17:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20877">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akIxd9ujqXo0B1CjLn7vmfJP4AzXB7JpCKiZvz03Ij9NF2Y_mkTRtU1fYvysaP0NrTwBe0gzooYAYUNCT0jo2R0w-SOHrHb4mc6-17mpRR73_w3wFXhYEhVfooZEvR9fjdBQ-1E_QQI-XD9J5V773kLtOWi8rBrHNCkBXnzjq8iw_yP0mWwvFaStkXP-hMXRUPQhedpfWgwGs775USWjwPUeIbb93aCWmbRc48fLpmGUdvtl2C-sVdC9og24NIfzYnrdEQrMZYtf6PJov_DaWXtDRxJn0mN7Yg5AvFs1LiV-aVEmFaXOZswIWcJOT7iaBu3WL4rKkosVP996ar9RfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی احتمالی دموکرات ها در انتخابات میان دوره ای نوامبر عملا مبتنی بر یک سنت تاریخی است که در دهه های گذشته بارها و بارها تکرار شده است</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20877" target="_blank">📅 17:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20876">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXwX1B8QUX3YTdCVkSpOFeDMo5mHHMAUlSnRLxr2pHtFjgG8r5uw1RtxNA5wvH78mJuJd75_oFyQK8R5KhgjCHfQKcdOsWqYT2TjOQJPKmm0Ei5FME4HKV99_rhbj9eNL6btc3FUiD_pMg2XtIBEA50_xQ_TBYWRvP6dmqPOKjPAB7GhLVhK5JIi0m3XbVjn8N5McMw60XyGKDwh2TqIrl8pXsoMZtRlZjEawCC21oj1GJGFtaMikpno3VmjqkyW3Aq__C-AIRrsGRvrYK4XihyHTo4t6aPR8ubraN9xCbqY25p2SL1hQc8pdu8e_WOCDTxVu_XuKip1hT8TvEuKQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20876" target="_blank">📅 13:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20875">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20875" target="_blank">📅 13:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20874">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Td0hj3zoUmVTxJZknLmDrpIKRpbWhZB7C7ZsGeQ0eGzZ_DA59os5PzYvtG323VQLVeemh6wD3jG9stYOV3c41zThhN5Wzg030V3IGcsYNsLWZKdjdS8RA4iNCMAkHR6_B76Tsae5os1sCv4_BogSsQ90Znz4Q2vOwREhc3uuQTLOMeJuU3iBgw9uFGqtpnD9ZVB7YBTG4wbMhLK-N3gRBaRbk5i14CjqG4anNZOMW9z3gRaxrU7JlKfe7vcBbkKjiM7d6jXpWc6dy_22y3FYPReFSoO7sc9lT_A5eoE3YqQFBgUgOofiMwvka0kDbuZJ4Y4r0J7cqX_qSSKd4TUq1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20874" target="_blank">📅 13:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20873">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یک آوانس برای براکصه در آستانه سفر رهبر چین به آمریکا</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20873" target="_blank">📅 11:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20872">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bqo95vuUafx4ug7gG85y7xJpZ7tN4nWh68Yk58ANQQB5XkXAoizPm40gLVYz4qEBw4IpGts1LLetLzR91hgOz7wqkvX8tQO2A1KeJA97-XqavH4Z5vqHBU-ImiMyV3UITD0hytW5v4I9tX-ZmVlHuUOV4mpD50zNfnS2u-36ad47FL54ETImPIi1he5yblVDHANeCTlp2kT_b8erd6VqxInFYNOefTypMPSgVJgM4P3TvN33cjgXG0lHK7BNVK6mq2EGkb20pBPNNg6W77sEml4Bxx2LquK7tKpW4s8Z62T21fAtzEeJcadDSMEVZI2N4Kpr-B6J9ObPfqq7GLm7zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20872" target="_blank">📅 11:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20871">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-_sP4lZALUxPwyPgFItcdaLopD8w275ojKRXQWwg3l_xkCAnlwD3xRSjAKoKf_TSWUUxKc5OWPhRHx-36pksp3omk293vNmwKQkSLuNF9KJJCTlntXAE-vC154lwbjCbYiBIzqloY8Zit9knIfM7I_jmc3djL7nOyl08584vaIXieWqW-68DnG9GLhNOauCmPbgwDaROo_dlEcfSgzE88i_QOK8O1WJQ2MA9G7rVbzKOgEfyov0WkZQehmd6-bHiMXb7wG-vlRne6Ft0M45tk6vFUcpay8Sb4kmRMO9PecN5-xDzhOivWln7Cn5nIDHK6vn0jQeX3hZx5HrNN8HOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای است و نظر به ریزش طلا تا الان، انتظار یک اصلاح صعودی می رود.
دقت کنید که رشد طلا «اصلاحی» قید شده.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20871" target="_blank">📅 11:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20870">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20870" target="_blank">📅 11:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20869">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!  محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20869" target="_blank">📅 11:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20868">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!
محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20868" target="_blank">📅 11:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20867">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAn-r4tkug4DFRxp8oRTnP9NkQiQ95nS7NP6L6WooFAvFEVZeFhyU0ly9ocSM2GbRAgkxppUqcr9aN-h-hvhscc_48JMFJZn0TtYgFELr5Qz0V64e6Kbyw1rn69R2xobwHFyL7OB6362BGyBsCxnzxZzioG_bokmearq7EJSpgaArxr97JISGSEvOf-TQ9CSW0EO0B80O1RNw9Py5cerhMxz_Zya6UTUYQprpHqlgfg3qXwewlhkwcIq4FsP1soyBfrFO9YH1LZ5MQkZBolefZ7irefoJOZdgRroIMz5yuhueOgQPwj2qRaGj2OsV0R2bPkGqBxgOqBg4H-vCheqbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشت تحلیلی | سناریوی اختلال کامل در مسیرهای صادرات نفت عربستان
یک سناریوی حداکثری برای بازار نفت، تخریب خط لوله شرق–غرب عربستان، بسته‌شدن تنگه هرمز و هم‌زمان بسته‌شدن باب‌المندب را در نظر می‌گیرد. اگر هر سه اتفاق به‌طور هم‌زمان و برای مدت معناداری رخ دهد، بازار جهانی نفت با یکی از شدیدترین شوک‌های عرضه در دهه‌های اخیر مواجه خواهد شد.
اهمیت خط لوله شرق–غرب در این است که به عربستان اجازه می‌دهد بخشی از نفت تولیدشده در شرق کشور را بدون عبور از هرمز به بندر ینبع در دریای سرخ منتقل کند. ظرفیت این خط حدود ۷ میلیون بشکه در روز است. در شرایط عادی، صادرات نفت عربستان حدود ۶ تا ۷ میلیون بشکه در روز است؛ بنابراین از کار افتادن این مسیر، وابستگی عربستان به مسیرهای دریایی خلیج فارس را به‌شدت افزایش می‌دهد.
اما اگر هرمز نیز بسته شود و خروجی دریای سرخ از طریق باب‌المندب هم امکان‌پذیر نباشد، تقریباً تمام مسیرهای اصلی صادرات نفت عربستان مسدود خواهند شد. در چنین شرایطی، ظرفیت قابل استفاده برای صادرات نفت خام جدید می‌تواند به حدود صفر تا ۱۰ درصد ظرفیت عادی سقوط کند. البته این رقم یک برآورد سناریویی است، نه پیش‌بینی قطعی.
اثر اولیه چنین اتفاقی احتمالاً در بازار نفت بسیار شدید خواهد بود. بازار نه‌تنها کاهش فیزیکی عرضه را قیمت‌گذاری می‌کند، بلکه «ریسک عرضه» و احتمال تداوم اختلال را نیز در قیمت لحاظ خواهد کرد. بنابراین افزایش قیمت می‌تواند بسیار سریع‌تر از کاهش واقعی تولید رخ دهد. ساختار بازار نیز احتمالاً به سمت backwardation شدید حرکت می‌کند و پریمیوم نفت فیزیکی افزایش می‌یابد.
برندگان مستقیم این سناریو، تولیدکنندگان خارج از منطقه خلیج فارس هستند؛ به‌خصوص تولیدکنندگان آمریکای شمالی، کانادا و برخی تولیدکنندگان آمریکای لاتین. شرکت‌هایی مانند ExxonMobil، Chevron، ConocoPhillips، Canadian Natural Resources، Suncor، Cenovus، Petrobras و Occidental می‌توانند از افزایش قیمت جهانی نفت و کاهش وابستگی بازار به نفت خلیج فارس منتفع شوند.
در طرف مقابل، خود عربستان با یک تناقض استراتژیک مواجه می‌شود. افزایش شدید قیمت نفت از یک سو ارزش هر بشکه صادراتی را بالا می‌برد، اما اگر نفت فیزیکی امکان خروج از کشور نداشته باشد، افزایش قیمت نمی‌تواند به‌طور کامل زیان ناشی از کاهش حجم صادرات را جبران کند. فشار بر درآمدهای دولت، پروژه‌های Vision 2030، پیمانکاران و بانک‌های داخلی نیز در چنین شرایطی افزایش خواهد یافت.
اهمیت ناوگان نفتکش‌ها و مسیر SUMED نیز در چنین وضعیتی افزایش می‌یابد. در صورت بسته‌شدن مسیرهای سنتی، دسترسی به مسیرهای جایگزین و ظرفیت حمل‌ونقل دریایی می‌تواند به یک عامل استراتژیک تبدیل شود و نرخ حمل نفتکش‌های بزرگ، به‌ویژه VLCC و Suezmax، را به‌شدت تحت تأثیر قرار دهد.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20867" target="_blank">📅 10:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20866">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رقابت عظیمی میان ترکیه با اسرائیل برای ایجاد هژمونی در غرب آسیا شکل گرفته که بجز جنگ با ابزار دیگری حل نخواهدشد.  بزودی در قفقاز هم شاهد تحولاتی خواهیم بود که نقش و جایگاه کشورها را عوض خواهدکرد.   اسرائیل به شکل هوشمندانه ای از دهه ها سرکوب اقلیت های قومی…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20866" target="_blank">📅 10:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20865">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rp9fY3ZFZKyIT0_dXhdF9VGnRCj8Vgxbh56IhPEu_2bQDjzE5n09sJaGwMpFOigRFWsLv0_QdPnOl8_YtekXP7BuO0xvu7Aw11LGb7anZ6isvqpHMP3BcdtFChttOUmxmwbWVXYCFsYDvf0z7NcnVDotyshtNENLZICYil5-fIPe29c3pFVVjzQHMR7M1L5DdHeubeSLTd2HHP6zIkqs7q5-CS-fEbVeG-qgA_p5Tk3WLfImDwrc4lchMgmSReEDL4if_1K2VKMLulxeIGDcN5lGsHo4TzOQ_E2tMAnrNqfKNs5nGH5p3Quqh4NEv1ALgJsSFMq0xfHN7SCubDEHdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ نفتکش‌های VLCC به شدت افزایش یافته و در تمام مسیرهای اصلی به بالاترین حد خود رسیده است، زیرا جنگ ایران ترافیک تنگه هرمز را مسدود کرده و جریان جهانی نفت خام را مختل کرده است.
هزینه انتقال از خاورمیانه و خلیج فارس به چین به حدود ۱ میلیون دلار در روز رسیده است، در حالی که نرخ خلیج عمان و چین در یک ماه ۳۰۰ درصد افزایش یافته و به ۵۷۱۰۰۰ دلار در روز رسیده است.
این محدودیت فراتر از خلیج فارس در حال گسترش است. نرخ نفتکش‌های غرب آفریقا به ۴۱۱۰۰۰ دلار در روز رسیده است که در یک ماه ۲۸۰ درصد افزایش یافته است، زیرا سفرهای طولانی‌تر اقیانوس اطلس به آسیا کشتی‌ها را متوقف می‌کند.
موسسه لویدز می‌گوید که خرید مجدد نفت خام چین، ترانزیت‌های خطرناک تنگه هرمز و راهکارهای ناکارآمد فزاینده - که اکنون با تعطیلی خط لوله شرق-غرب عربستان سعودی بدتر شده است - عرضه نفتکش‌های موجود را بیشتر محدود می‌کند.
با توجه به اینکه حاشیه سود پالایش هنوز به طور غیرمعمولی بالاست، اجاره‌کنندگان تاکنون می‌توانند شوک حمل و نقل را تحمل کنند. دلالان می‌گویند هنوز "سقف مشخصی" وجود ندارد.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20865" target="_blank">📅 09:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20864">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_4XRaR3cfyhEJc0duABZs0rbs8O2KuPTYt_ns8nKvJqp7BvH8qE2zZBVM9_6GQZpiiSt8F4EQVDMzXr8EjqSXmAHvjXTnp8Tb_xASMb37cU6mmYTB9LwR0TAucJmBd57yrInrdlgZP-NKJtlEk0nO_sSgVhtAXuJOkhF2Yb4Rr-QOiZG9ae59R0Zu6FlvX2Tl_FufFp-OiKh__7rqQLmSovgmkiAjv0h_OrgYG_N2FTvkdSr-UQ4zTOlByk25TPvzx3Y0JsPQSfSL2FTcta4ZeFn20_gtHCn2Xe5_vu3vHEGWL-JVP83B_4RYvKFQCVfXg4S3Pv9U937sJk9W7Gcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان سعودی ممکن است تا ۴ درصد از عرضه جهانی نفت را از دست بدهد اگر خط لوله شرق-غرب آن به سمت دریای سرخ در عرض چند روز
راه اندازی نشود
این خط لوله پیش از حمله پهپادها که منجر به توقف آن شد، حدود ۴ میلیون بشکه در روز به ینبع منتقل می‌کرد.
منابع صنعتی می‌گویند ینبع در حال حاضر فقط مقدار کافی نفت در انبار برای حفظ صادرات به مدت پنج تا هفت روز دارد.
این منبع زمان مورد نیاز برای تعمیرات را فاش نکرده است؛ برآوردهایی که رویترز به آن‌ها استناد کرده، از راه‌اندازی مجدد جزئی در زمان زودتر تا ۵ یا ۶ هفته طول می‌کشد.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/20864" target="_blank">📅 09:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20863">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHstWTsLElXHG8SsQFBqPQtUcEFgevvutHTNmUjxqRvRlkuDoddx5tg2-tiqXdaG5S34Gj6sorA8dMW5Zl4Z3pG9_RS-2uIdn3FG_LeuJ8A-BrvN-bHoUXMzt_AfIwyxn1x6d_RZE7jBKPyHstK4IailkkeOIsrV46Jr_C70kHuHGd5ASpfyWOM82MfRyAmnKe38TfG7KqNuY6kpySymKnJBiU_OsqZWRKJtVPwvX7HVTGK8Lj9yjse9E1jGIz9C6mIGBaDmt-NloH7Hpnp67RbsaKzRpqe4lYnpVWvCd_EAFLErk2ntzPLMOH_ymcqp49Gjxum35qu01pCH-fTU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور خارجه عمان پرچم  شیر خورشید ایران رو گذاشت
😁
@Piknikanalyst</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20863" target="_blank">📅 00:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20862">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نشست فردای ایران، عمان و کشورهای عربی سر تنگه هرمز فعلا لغو شد</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/20862" target="_blank">📅 23:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20861">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شلیک موشک از ایران به سمت تنگه هرمز</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20861" target="_blank">📅 23:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20860">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qh8ARNsq8Bi4syGizSeJI1o7QRe8zNx2pQtGQRw8bMvHkysTGc764iVCSTlJoSgHcRDE64FUNCFPLOO67BqSS7-YRi_RBA_5gLIDALlIDkbC-tFySlMYeZaWW2bpUt4ynzEpx8sC8GapR4g_w4WYjYbmKTjX5-dgttrSh0fKzyyYymIK2JcFnGcjZoKzieBBAKCXZ2F90NgmTduOzL7_G5IjJhNuFkCizTRj_tWSj4hkcaqe2lEa9FWr65KZ9ORvr0E8RTaldb3Fr3276eQTlgIJPN4YXNnexR1gb_JNgqnuaAF_0BIDM-CQ6B0BuoJ8lzkZ5O1n96NsCNVTYOOazw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور خارجه عمان
پرچم  شیر خورشید ایران رو گذاشت
😁
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20860" target="_blank">📅 23:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20859">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">توافق ایران و عمان برای تنگه هرمز به معنای باز شدن خودکار تنگه نخواهد بود   منبعی نزدیک به تیم مذاکره‌کننده ایرانی به تسنیم گفت: درک چارچوبی در مورد مسیرهای کشتیرانی «به زودی اعلام خواهد شد»، اما «فقط» بین این دو کشور است و مسیر جنوبی هرمز را بسته نگه می‌دارد.…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SBoxxx/20859" target="_blank">📅 22:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20858">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP8KE_vxzkRjboE1DchfefA6iDeIsynGbRgfFn-D1EaLx4pPXlEn8buYohQkl-p28s5oAYgJGHZEufKgkZDBXTny0bCnvaTy2lftWnQjHsmgXOvllEsFT5BIDDkwtDSpMBB8yG1kA2o4A8mL1hFctsKfGhihNOqzYdwcDVyahMnIp-IODo_B3IhBajdsFoBVBnfHXCppPbvxp-6JtSc4a7AqUKhxooTCMspygvGCQRoyvKux2UuzHVj1FmYNki-6XUNH1lUGs81n9mYhlOh1-Hw4NU3i-MzBgymY4s-lpBz6sEp3u5r5CsbdLHWLZ0q2eQfX0Wb-PH9Dc-5XSqg_tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگنده J-10C چین: نیرویی جدید در آسمان جنوب آسیا  جنگنده J-10C چین اولین پرواز رزمی خود را انجام داده و نقطه عطفی بزرگ برای صنعت هوافضای چین محسوب می‌شود. پروژه J-10 که در ابتدا در اوایل دهه ۱۹۸۰ تحت رهبری دنگ شیائوپینگ آغاز شد، با هدف توسعه یک جنگنده بومی…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/20858" target="_blank">📅 22:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20857">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فیدان: سوریه می‌تواند جایگزین مسیر هرمز شود
وزیر خارجه ترکیه گفت:
سوریه می‌تواند با اتصال به اردن، عربستان، عراق و ترکیه، نقش مهمی در ایجاد مسیرهای جایگزین تنگه هرمز ایفا کند؛ مسیری که قرار است از طریق راه‌آهن، بزرگراه و خطوط لوله عملیاتی شود.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20857" target="_blank">📅 20:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20856">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODEXagP3uxgnM7iHfPZnvT87Btw6Cb0I3GLVaMROOtIw3sBtijjfYGl12hAZ4xrQ64tPGo63TQY__C7KmOrs-A1RvYSJYKEPYBaa7R8v2_riww9hEZbDOcAD92uoi2VNRhIEIc5u1wlqqGLysGnytwY6QAzTjBAH_Le_kpgk7aC0ly3Z5zqIWIKBkJthhlwyp9ZdXNxvasGUEwnnJZFMPPThF0lTpmpeLe14l6xSOtWI2uIGZjkHrruOnnG8-VURldDxwqgu8H99FA8-htxz4BdT8Hz5xrtNaSjyUdDsxaG6gudKAYr0_3SvrkAThzSfRRtVhc04Z53S555qBrsbig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشیال تایمز:
ایران از روسیه درخواست پهپادهای اصلاح‌شده «گران» را کرده است
بر اساس گزارش FT با استناد به منابع امنیتی غربی و یک فرد نزدیک به کرملین، تهران به مسکو برای پهپادهای مدرن‌شده خانواده «گران» روی آورده است.
باور بر این است که ایران قصد دارد از آن‌ها در درگیری جاری با اسرائیل و ایالات متحده استفاده کند.
این نشریه علاقه تهران را به توسعه سریع اصلاحات جت‌ساز روسی و افزایش قابلیت‌های این پهپادها از نظر برد، سرعت و هدایت مرتبط می‌داند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20856" target="_blank">📅 20:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20855">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4zbcgNN_MjkHqrOmQrnhf7E0EWGmtmJnM92FYCeVfUPnsmg4UWXkNTgno2GjA4qsuJBuILTYRllKVPU6sscRTWwNb68-BxbV_8ClseYKh_2zrYtLc4mbbBvZbHIR14sGLVR06E356fy-hfKFhN0FLwi6U_9eyKVu1zQrbu9klyGy2ZtQCW6KtNzq5mPCyCuxlmr94s_C6m4ab30SSK1HzJRW41tK0E3NSUfJ0T6LVkXJstt-EULO-eqaZiDC3vTh6BDvU2ydbZIlJt_SmWLKyyXoC2nEjZfs4J6uF61bD8x6VBP8noqQzJF-8gzv9aBzAakrKJBSD0qh65rDfZD1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
نشریه شماره چهاردهم منتشر شد
📌
در این شماره می‌خوانیم:
✔️
طلا؛ دارایی‌ با بازدهی پایدار بالاتر از تورم
✔️
واگرایی میان فدرال رزرو با خزانه داری
✔️
وضعیت رشد تورمی در اقتصاد آمریکا
✔️
چرا طلا یک دارایی راهبردی محسوب می‌شود؟
✔️
و...
🔗
نسخه PDF ویژه دسکتاپ
🔗
نسخه PDF ویژه موبایل</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20855" target="_blank">📅 18:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20854">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">انفجار در بندر ینبع عربستان</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20854" target="_blank">📅 14:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20853">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هم میهن:  ترکیه به جای دلار گاز، غذا و دارو می‌دهد همتی به استانبول رفت  منصور بیطرف/ روزنامه‌نگار و تحلیلگر اقتصاد  دو روز پس از آنکه مهمت شیمشک ، وزیر دارایی ترکیه اعلام کرد که آن کشور - منظور ترکیه - پول گاز وارداتی از ایران را مستقیم پرداخت نکرده و بر…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20853" target="_blank">📅 14:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20852">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">هم میهن:
ترکیه به جای دلار گاز، غذا و دارو می‌دهد
همتی به استانبول رفت
منصور بیطرف/ روزنامه‌نگار و تحلیلگر اقتصاد
دو روز پس از آنکه مهمت شیمشک ، وزیر دارایی ترکیه اعلام کرد که آن کشور - منظور ترکیه - پول گاز وارداتی از ایران را مستقیم پرداخت نکرده و بر اساس سازوکار توافق‌شده با آمریکا عمل می‌کند ، عبدالناصر همتی ، رییس کل بانک مرکزی ایران وارد استانبول شد
به گفته شیمشک، مبالغ مربوط به خرید گاز ایران در یک حساب به‌شدت تحت نظارت و تنظیم‌شده نگهداری می‌شود و ایران فقط می‌تواند از این منابع برای خرید اقلام مجاز در چارچوب رژیم تحریم‌ها، از جمله مواد غذایی، دارو و کالاهای مشابه استفاده کند.
سخنان شیمشک فقط درباره پول گاز نیست. این اظهارات نشان می‌دهد که ترکیه در دوره فشار حداکثری جدید آمریکا فعلا حاضر نیست برای حفظ تجارت با ایران، ریسک قرار گرفتن نظام بانکی خود در معرض تحریم‌های ثانویه را بپذیرد</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20852" target="_blank">📅 14:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20851">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxwpxrZjl7f2yPI_CYYECKygrGKHS5dFSN8ZLajXOOEl0OOn8kVuCLInLx5_9RLLlZ62xdA1XhnUlnbPqaJtkDurE9VplQVnnFCMv-_Flz7n1OW63NCF973TqeFNDRAmB9ltCNgfRCtPc9eZgFPVY9kZC2rSllPZFlTlegKlbwJCjm-bIUrr5Wev9fURiKCF23xwkGysG6k2aCwNyTjQ0pIyCn1p8j4evdaQuJ1CzKxwCXF7CEqvYb1wUd4rwMx6egTa-LIgYY-KpWcq0mPci00WnbXkXYKK9j6QOb4IbMSnJ0v8ZaKJ3JEMH31yVeuOrqr9qcVl1_5sG-5fdznpwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشیال تایمز:
حوثی ها با هوش مصنوعی آنتروپیک موشک بالستیک ساخته اند!</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/20851" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20850">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پزشکیان:   نمی‌دانم مشکل آنچه در پاکستان نوشتیم چیست که آمریکا می‌خواهد از نو گفت‌و‌گو کنیم</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/20850" target="_blank">📅 12:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20849">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پزشکیان:
نمی‌دانم مشکل آنچه در پاکستان نوشتیم چیست که آمریکا می‌خواهد از نو گفت‌و‌گو کنیم</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/20849" target="_blank">📅 12:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20848">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خب امروز و بعد از ۹ ماه تارگت ۲۴۰ هزار تومانی دلار محقق شد.  بعید نیست مدتی رنج بشود.</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/20848" target="_blank">📅 11:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20847">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">— یک کشتی تجاری ایرانی در نزدیکی جزایر هنگام و قشم مورد حمله قرار گرفت که در نتیجه یک نفر کشته و سه نفر دیگر زخمی شدند.</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/20847" target="_blank">📅 10:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20846">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">احمد اروزان کارشناس ترک:
خلبانان اسراییل برای حمله به ایران در قونیه ترکیه تمرین میکردند!</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SBoxxx/20846" target="_blank">📅 02:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20845">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">معاون وزیر خارجه یونان:
ترکیه و همه در منطقه می‌دانند که یونان کشوری بسیار قوی است که جایگاه بسیار بزرگی ژئوپلیتیکی، دیپلماتیک و نظامی کسب کرده است.
و من مطمئنم که هیچ‌کس هرگز این قدرت‌های یونان را آزمایش نخواهد کرد.</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/20845" target="_blank">📅 00:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20844">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaNQRYCE6DQAuGib814g8CvWSsMWObZ74ilDBU2NdPz4Ow8jEra98J_Aq1bOaiE5Zf0OJUZlNSQaBIFJvHUNq9RaFC8LkCp8H_bBhqTsB312ik6__BrkttF-VKgCpiE_C6fTZiYZrtUDFKiIQWVUKk0ZxUfuyjtw4uWR1xsgkh37o515U-bShXyhK7pHnukZr0m0dc9H898GMFZ5BQFVTSz3a_uo6BqX-QY5_N7yeQa47JWSsQf6fRPNyedAp_VWRJKHC_yb1yfB4pZ0wAC-JQ0Iul274eCHZKwpynzUT4hXJeFO5HmFYHMl5AZTLs1hT05ix13DGOK8A_3BRu40_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت پیمان مکه!</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/20844" target="_blank">📅 00:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20843">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پرتاب موشک از ایران به سمت هرمز</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20843" target="_blank">📅 00:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20842">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کانال ۱۴ اسرائیل:
ایران در حال آماده سازی برای تست سلاح هسته‌ای است</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/20842" target="_blank">📅 23:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20841">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dfyt6lTRfA1el-zqqzWRwFBinLnneUZrG08xFks5AtDJqSgYugjybhdiAkluNU62k1GoAxtDJAoZzGyKDgJnTEQ5WmbjRzWwXa-d3Gw29uG2LcGzs75j4UWHlbrkYNO6mC4v9Kxt58NlDdN14JRMzEV6-_lmK8iPvbqQgPIvUj4mQ7idN-Ql9ti9bFjqU5icVtlp_QIV4f10u8VwbcgjqZbmbNcY8bAaNgkm0Vy7cISlmocPNQYj6N6emFkrxTwFX-yWxyn_WGMoPr5bZcLQYIlgvq8Y2D7s6q-s_ogQCTL9C-Mk05B28OlP5YF_wGHZV71rUOkvu0pkWz_UyozLeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/20841" target="_blank">📅 23:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20840">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">توافق ایران و عمان برای تنگه هرمز به معنای باز شدن خودکار تنگه نخواهد بود   منبعی نزدیک به تیم مذاکره‌کننده ایرانی به تسنیم گفت: درک چارچوبی در مورد مسیرهای کشتیرانی «به زودی اعلام خواهد شد»، اما «فقط» بین این دو کشور است و مسیر جنوبی هرمز را بسته نگه می‌دارد.…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20840" target="_blank">📅 23:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20839">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پزشکیان مدعی امضای توافق هرمز با عمان در حضور کشورهای عربی شد  رئیس جمهوری مدعی شد مقام‌های ایران و کشورهای عربی خلیج فارس روز دوشنبه در مسقط توافقی برای ایجاد مسیر کشتیرانی مشترک میان ایران و عمان در تنگه هرمز امضا می‌کنند.  مسعود پزشکیان گفت: «کشورهایی که…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20839" target="_blank">📅 23:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20838">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترور یکی از بسیجیان عشایر منگور
سپاه پاسداران انقلاب اسلامی شهرستان پیرانشهر با انتشار بیانیه‌ای، شهادت حاج اسلام کاک درویشی را تسلیت گفت.  پاسدار پیشکسوت و دلاور عشایر منگور، حاج اسلام کاک درویشی توسط عوامل پلید ضدانقلاب در مقابل منزل خود در روستای کوپر به شهادت رسید.
شهید اسلام کاک‌درویشی از جانبازان سرآمد و از نیروهای مخلص و وفادار به ارزش‌های انقلاب اسلامی بود که سال‌ها در مناطق کردستان و آذربایجان‌غربی مجاهدت کرد.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20838" target="_blank">📅 23:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20837">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">معاون رسانه‌ای انصارالله یمن: با هدف‌گیری خطوط‌لوله و پالایشگاه‌های عربستان کار به نفتکش‌های سعودی نمی‌رسد
درصورت تشدید تنش میتوانیم زیرساخت‌های نفتی را هدف قرار دهیم تا اندک صادرات نفت عربستان از کانال سوئز هم قطع شود.
همه چیز ممکن است؛ مگر این‌که محاصره علیه یمن برداشته شود؛ عربستان فعلا درحال لجبازی است.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20837" target="_blank">📅 23:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20836">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تهدید فاکستان به حمله موشکی در صورت دخالت نظامی در یمن</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20836" target="_blank">📅 20:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20835">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پزشکیان مدعی امضای توافق هرمز با عمان در حضور کشورهای عربی شد
رئیس جمهوری مدعی شد مقام‌های ایران و کشورهای عربی خلیج فارس روز دوشنبه در مسقط توافقی برای ایجاد مسیر کشتیرانی مشترک میان ایران و عمان در تنگه هرمز امضا می‌کنند.
مسعود پزشکیان گفت: «کشورهایی که خاکشان از سوی آمریکا برای حمله به ما استفاده شد نیز در این نشست حاضر خواهند بود.»</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20835" target="_blank">📅 20:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20834">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_jyUddwO2Pp8YwmwHQdW7WfsDtLi753VVMZn3-kz2CWQU5ZDFUcCLRrIQiFsLudqEtgEy8qZvMtf5krxb6CUZ0aBBvpd3RsPWYHmuzdBCY2M1oenmTeqIbv9me3ZWQ8eLJeo2ZvdAzqzq_DscjfCWnv1q-5ofqIloLQMz3jzvcR238fk3aTx8UphEyjXcWM2rNBSjSINTwRGJ1qFPkt0idCNBg62uoDmsm-ArE8-rcyF6bvquUFqQjLykVU26Z1pO5Mznez9wlv9wTqbpwdHjqZGHTcIEL3dJvoWCnT0nYFKqbkVeU4_Pp5Dhm_T1Eit6a_yS6M2dHRBFEdPKm9ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی ان ان:
اوکراین در نبرد با روسیه، فراتر از اروپا، تیم‌های کوچک متخصص پهپاد را به آفریقا و خاورمیانه اعزام می‌کند تا نیروهای محلی را آموزش دهند، از گروه‌های ضد روس حمایت کنند و به منافع روسیه حمله کنند
حدود ۱۵ متخصص اوکراینی در شمال مالی در کنار جبهه آزادی‌بخش آزاواد (FLA) که توسط توآرگ‌ها رهبری می‌شود، فعالیت می‌کنند و به جای درگیری مستقیم در خط مقدم، آموزش پهپاد، اطلاعات و پشتیبانی عملیاتی از راه دور ارائه می‌دهند.
نیروهای اوکراینی همچنین نیروهای چاد، نیجر و بورکینافاسو را آموزش داده‌اند، در حالی که چندین متخصص در سودان نیز عملیات کرده‌اند.
سازمان اطلاعات اوکراین می‌گوید این اعزام‌ها با هدف فشار آوردن به روسیه در خارج از کشور و تبدیل تخصص اوکراین در پهپادها به یک «ابزار سیاست خارجی» انجام شده است.
نیروهای اوکراینی در سال جاری میلادی، هنگام تصرف کیدال توسط شورشیان توآرگ، به آن‌ها کمک کردند؛ جایی که نیروهای شورشی و وابسته به القاعده، نیروهای سپاه آفریقای روسیه را به عقب‌نشینی واداشتند.
نیروهای اوکراینی همکاری خود با توآرگ‌ها را عملیاتی و نه ایدئولوژیک توصیف کردند و یک منبع اطلاعاتی گفت: «وقتی توسط همان احمق‌ها مورد حمله قرار می‌گیرید، تفاوت‌های ایدئولوژیک در پس‌زمینه محو می‌شوند.»
اوکراین همچنین از اواخر سال ۲۰۲۵، اپراتورهای پهپادهای دریایی را در شمال غربی لیبی مستقر نگه داشته است. یک اپراتور گفت که یگان او از پایگاه نظامی بین‌المللی در مصراته برای انجام حملات علیه «ناوگان سایه» روسیه که از تحریم‌ها فرار می‌کند استفاده می‌کند و در عین حال نیروهای محلی را آموزش می‌دهد. یک پهپاد دریایی انفجاری اوکراینی از دست اپراتورهایش خارج شد و در سال جاری میلادی به سمت یونان هدایت شد که باعث اعتراض آتن و عذرخواهی کییف شد.
اوکراین همچنین تیم‌هایی را به حداقل ۵ کشور خاورمیانه اعزام کرد تا در طول جنگ، آموزش سرنگون کردن پهپادهای شاهد ایرانی را ارائه دهند.
مسئولان اوکراین مأموریت‌های خارجی را هم به عنوان راهی برای تضعیف روسیه در هر جایی که فعالیت می‌کند و هم به عنوان فرصتی برای آزمایش فناوری پهپاد اوکراین در شرایط میدان نبرد مختلف، از گرمای شدید و گرد و غبار ساحل در آفریقا تا عملیات دریایی در مدیترانه، معرفی می‌کنند.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20834" target="_blank">📅 20:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20833">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9fpJ7mxBckIXbOjI6wQUUt8DUz0bwvJaTzAp-3bHMuZ2FWjfuxMpydVjUg7SXwsyMeAE5zA2N4oR2yj8UxlMtC89UvGzaQqRxlSljzTcI3pqnlgnF_SiS0w8QVDAYWK77Ckqde_UdFCn48xixHjBPrcRydPMP6hpNtj_F9bnQz-ftaQAh0RGZqu-1lvYMYN0-_VQfYUFhwmwp02qqQLIH1NnB0beE_Esyre7eLBfrFo0knbVxEOZdUu6IfeB1lRgyhDh8YDJ4aGyk3fnfiswBJhulvmiL_6ooeBp8NM5AsKAp_MnS0O5nDVss3HIqxAglVIryxQMiMfqB1CL_YFLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید فاکستان به حمله موشکی در صورت دخالت نظامی در یمن</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20833" target="_blank">📅 19:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20832">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">احتمال اینکه کل داستان جنگ یمن در روزهای اخیر یک تله برای حوثی ها باشد وجود دارد…  توضیح خواهم داد.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/20832" target="_blank">📅 17:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20831">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مدتی است به صورت آشکار و بی پرده، صحبت از لزوم ساخت سلاح هسته ای ایران از سوی مقامات کلان جمهوری اسلامی مطرح می‌شود</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/20831" target="_blank">📅 15:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20830">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ:   حوثی ها با ما تماس گرفتند و به ما اطمینان دادند که به دنبال درگیری با ما نیستند.   ما با حوثی ها صحبت داشتیم، آن ها تماس گرفتند و به ما گفتند که دنبال درگیری با ما نیستند و نمی خواهند ما به سراغشان برویم. آن ها اجازه می دهند اکثر کشتی ها عبور بکنند…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20830" target="_blank">📅 13:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20829">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ:
حوثی ها با ما تماس گرفتند و به ما اطمینان دادند که به دنبال درگیری با ما نیستند.
ما با حوثی ها صحبت داشتیم، آن ها تماس گرفتند و به ما گفتند که دنبال درگیری با ما نیستند و نمی خواهند ما به سراغشان برویم. آن ها اجازه می دهند اکثر کشتی ها عبور بکنند و فقط با یک کشور (عربستان سعودی) مشکل دارند.</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/20829" target="_blank">📅 13:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20828">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">درگیری های سنگین میان نیروی انتظامی با جیش العدل در سراوان</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20828" target="_blank">📅 13:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20827">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a939b42fc.mp4?token=gm3B5YIvt232GdUquiqiYNgQlr8CjsnM3bbhabQPP_pR34cLyGggxsZ8BStlVlYvliJ2Tm2PRsiv2LkmKbF-RTg98MWdFKR5Up3UwuyhlFI2n_2XgCuB2cf3UMfVyd89pufeC3s69w6IwaXph1xwvOoSF_SNgKoH5NTn7SWu_KaJklRT3cI5jOtiRtHvpGZgWMilcvDMwAt9YR5W2LF0gCHeYKV3VMJ8noX_1QT_leHvJeZY9he8QQ6IyIc_oxf6pB2UJkhQQA5cAciJ_JuEoRt4SzUg8A6sWbGQ2CJ38UMjI9dLy4cWG3h5gtq7dsudRz8g9lIWoZZbtkRAPZ68aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a939b42fc.mp4?token=gm3B5YIvt232GdUquiqiYNgQlr8CjsnM3bbhabQPP_pR34cLyGggxsZ8BStlVlYvliJ2Tm2PRsiv2LkmKbF-RTg98MWdFKR5Up3UwuyhlFI2n_2XgCuB2cf3UMfVyd89pufeC3s69w6IwaXph1xwvOoSF_SNgKoH5NTn7SWu_KaJklRT3cI5jOtiRtHvpGZgWMilcvDMwAt9YR5W2LF0gCHeYKV3VMJ8noX_1QT_leHvJeZY9he8QQ6IyIc_oxf6pB2UJkhQQA5cAciJ_JuEoRt4SzUg8A6sWbGQ2CJ38UMjI9dLy4cWG3h5gtq7dsudRz8g9lIWoZZbtkRAPZ68aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیلی دیدنی از پتانسیل صعودی شدید ریال</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20827" target="_blank">📅 13:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20826">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ درباره ایران:   قیمت‌های نفت پس از پایان درگیری سقوط خواهند کرد</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20826" target="_blank">📅 13:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20825">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ درباره ایران:   همه چیز به‌خوبی حل خواهد شد</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20825" target="_blank">📅 13:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20824">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ درباره ایران:
همه چیز به‌خوبی حل خواهد شد</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20824" target="_blank">📅 13:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20823">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده در آستانه گسترش تحریم‌های ثانویه علیه ایران
بر اساس اطلاعاتی که یک منبع آگاه از برنامه‌ها به
رویترز
گفت، انتظار می‌رود وزارت خزانه‌داری ایالات متحده دامنه تحریم‌های ثانویه‌ای که می‌تواند بر شرکت‌ها و کشورهایی که همچنان با ایران تجارت می‌کنند، اعمال کند را گسترش دهد
این منبع گفت که این اقدام به عنوان یک هشدار نهایی به کشورها برای قطع روابط تجاری با ایران انجام می‌شود
انتظار می‌رود اسکات بسنت، وزیر خزانه‌داری ایالات متحده، جزئیات بیشتری از این تدابیر را در یک نشست خبری در ساعت ۱۳:۰۰ به وقت شرقی ایالات متحده (۱۷:۰۰ به وقت گرینویچ) روز دوشنبه اعلام کند.
طبق گفته منبع، بسنت همچنین یک کمپین فشار اقتصادی گسترده‌تر علیه ایران را ترسیم خواهد کرد که او و دونالد ترامپ، رئیس‌جمهور ایالات متحده، آن را «روز D اقتصادی» نامیده‌اند.
این منبع گفت که انتظار می‌رود بسنت روشن کند که کشورها باید بین همسویی با ایالات متحده یا ریسک قطع دسترسی شرکت‌ها و نهادهای بزرگ از سیستم مالی مبتنی بر دلار، انتخاب کنند.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20823" target="_blank">📅 12:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20822">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">درگیری های سنگین میان نیروی انتظامی با جیش العدل در سراوان</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20822" target="_blank">📅 11:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20821">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مرزهای بازرگان و بصره بسته شدند.
مرز بصره جوری بسته شده که تیم تاج برای سفر به بصره جهت میزبانی بازی های آسیایی (سبحان الله چرا بازی پرافتخارترین تیم ابرقدرت چهارم جهان باید در بصره باشد اصلا؟!) به مشکل خورده!</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20821" target="_blank">📅 10:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20820">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLfHqEHSoAiYB1ZcvYC3xUNJ0nUm5BnB-2W8EhAg3ydYtZiBFnbfFI3bRxQjb6n_8f2g-6C1Wqrwxze2agE-zX96njnkaN2ZsJySEWnA5DFi0cr6yij4T75263ZmC3gFQbAY74C-apconacwmsy5NnXyuLBtJgAmuXa4EuFWGd9qe1Wl2JN_qfDfwDtXZX8nEwvDJtZ8ATDqPH5SyxYPJsh2Y7gl-QEPIWF4frHL9GQU_cFJIK_JHz2JJ-FykS251DI5lBUvRtYJH6ABj7p7s3qo9OZRH3RDWb6f20faZIAQakv16Gc6-Ul8JQXUDfOJ5lsBLmayiRl2lo0PZoTJmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال اینکه کل داستان جنگ یمن در روزهای اخیر یک تله برای حوثی ها باشد وجود دارد…
توضیح خواهم داد.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/20820" target="_blank">📅 08:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20819">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">— یک مقام اسرائیلی به کانال ۱۲ گفت که کنترل حوثی‌ها بر تنگه باب‌المندب «خطرناک‌تر» از وضعیت فعلی در تنگه هرمز است و به جغرافیای این آبراه اشاره کرد.
کانال شرقی حمل‌ونقل دریایی در نزدیکی جزیره پریم تنها حدود ۳ کیلومتر عرض دارد، به این معنی که کشتی‌ها در محدوده دید مستقیم از مواضع حوثی‌ها عبور خواهند کرد.
«آن‌ها قادر خواهند بود با موشک‌های ضدتانک به هر چیزی که بخواهند شلیک کنند. آن‌ها می‌توانند کشتی‌ها را با چشم خود ببینند. این همان تفاوت است.
در هرمز، ایران به رادار، سیستم‌های نظارتی و موشک‌های ضدکشتی نیاز دارد تا ترافیک دریایی را تهدید کند. اما در باب‌المندب، یک جنگجو با یک موشک ضدتانک ساده در جزیره میون می‌تواند به یک کشتی تانکر شلیک کند که می‌تواند آن را به صورت فیزیکی ببیند،»</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/20819" target="_blank">📅 07:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20818">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">— دادستان‌های فدرال آلمان هفت مظنون عضو حماس را متهم کرده‌اند.
به گزارش‌ها، اینها در حال برنامه‌ریزی برای انجام یک حمله مرگبار علیه اهداف اسرائیلی یا یهودی در آلمان یا اتریش بودند.
این توطئه تا ژوئیه ۲۰۲۵ به مرحله عملی رسید و قرار بود در دومین سالگرد حملات حماس به اسرائیل در ۷ اکتبر ۲۰۲۳ انجام شود.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20818" target="_blank">📅 07:19 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

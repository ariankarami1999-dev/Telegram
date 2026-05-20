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
<img src="https://cdn4.telesco.pe/file/CiITELu_Jw9s8qTQTXTeGOivX6A4Mpz_pi65GE2iG7rRL3RboyRd2QzwuoSaihUKhArmsUM1Gz0xAtDIdRrnokJm7S9gdQqBnSQuEINm1MVf-MmIn_3pRH17JvTp-63xsxnCCNGVmEUhS0g8DNjDk5whS11FYaIJh2sk0jbq4SMiFIS0P5gn9QF9br8Si4onlOLcFK68Lw7f0iwBPfvBGQdeDT7MgelSXAm7DAdc_3SEnk7zpZRZnLpQS4TQUlu-NjOLCiqN7Ri7qCAscNLCqKehK4WRZ5X6c0a01qdO4n2UqixqE7QYGwtepU5dasRMddjhQXIR-DksM9tD5_yKVg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.86K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 21:07:19</div>
<hr>

<div class="tg-post" id="msg-16482">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ:   نتانیاهو هر کاری من بخواهم انجام می‌دهد</div>
<div class="tg-footer">👁️ 981 · <a href="https://t.me/SBoxxx/16482" target="_blank">📅 20:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16481">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇺🇸
🇮🇱
ترامپ می‌گوید پس از پایان ریاست جمهوری‌اش به اسرائیل خواهد رفت تا برای نخست‌وزیری کاندیدا شود.</div>
<div class="tg-footer">👁️ 991 · <a href="https://t.me/SBoxxx/16481" target="_blank">📅 20:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16480">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ: درگیری‌های بیشتری در راه است مگر اینکه ایران عاقلانه عمل کند.</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SBoxxx/16480" target="_blank">📅 20:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16479">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">#US10Y — H4  فعلاً موفق شده با این سیرک امروزش مقداری نرخ بازده و نفت را همزمان سرکوب کند.   خواهیم دید چه خواهدشد.</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/SBoxxx/16479" target="_blank">📅 19:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16478">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wna92lO4UJYaSwWABzBYM93MNX2g6byTdiNDhjrsKB392sYDgiyRrVyDwhbvVl-T2FXbbQZUORK7cN-a241qoy33J69zT0xGfT82N87_ogCsQQUaUXDqrVXrUbc_5wy_Trmpkx1HrWhKZ9blSPkn6Zsw4oqJLRmvbTQbse7PcYQlrpwZEG6RRcbxSu4xMqHkDZ1Ay0eMYnTKdR3OIeX3_M0ID6VHfDahuAHihlm_RcZ2Bai5CHP3kuIhvIBgrzCivi9yyHiy42aopTWKGrKj9vceBnY4e-xJ6bSZEQirP6BfbZlh4w18q4AxQjgu6O_QlKXobv135YMjK06qPLBBAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#URA — D  #سهام_خارجی  این یک فرصت ویژه ایرانیان خارج کشور است. صندوق ETF اورانیوم می تواند در قالب موج 5 خود دستکم 70 درصد رشد داشته باشد که در چارت می بینید.  نظر به مسخره بازی ما در تنگه هرمز، احتمال هجوم سرمایه ها به انرژی های جایگزین بالاست و انرژی هسته…</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/SBoxxx/16478" target="_blank">📅 19:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16477">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3XKSucqj8Pm28Z8U8ZbFOl98FTJyG5SvOU31mZ0Xb748MKc_xj04UaPdLJdQi08MU24RQFW9qUHvlMNEI1b1eWalIqPy6_3tUgL6XrgqRg_UOk-826MoRmw1RWZovvvbpGreaSlsyp3yEsbdzogeEBjRA4Rf0cipaay80rFC2JrYhC7uvPEUFVgZAUzh72BHBZVKuam4dc1vdanRiSfkLckN0aYajHUownG4cHxlA60sLh0T6BjCpi7pZOyxAoze0bnP0PmHAcuIJ0k5b2_XZ294nlYONIM_72l_4gia1bMLx_-4TKwU3RPveXzhFj3PabWcyWh3_O-NtTrRDbj9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ بازده اوراق قرضه 10-ساله خزانه داری آمریکا سقف مثلث را شکسته و عازم سطوح بالاتر است که فشار سنگینی روی دولت فدرال برای تامین مالی اش وارد می کند.  ترامپ اگر تنگه را باز نکند، بازی اش با نفت میتواند از کنترلش خارج بشود.</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/SBoxxx/16477" target="_blank">📅 18:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16476">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❗
⚠️
ترامپ: آمریکا در «مراحل نهایی» مذاکرات با ایران است</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/SBoxxx/16476" target="_blank">📅 18:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16475">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇺🇸
🇮🇱
ترامپ می‌گوید پس از پایان ریاست جمهوری‌اش به اسرائیل خواهد رفت تا برای نخست‌وزیری کاندیدا شود.</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/SBoxxx/16475" target="_blank">📅 18:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16474">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔻
ریاست مجلس
:
دشمن از تجاوز مجدد به ما ، پشیمان خواهد شد</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/SBoxxx/16474" target="_blank">📅 18:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16473">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⛔️
اخطار قوه قضائیه بابت برخورد با کشت خشخاش</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/16473" target="_blank">📅 12:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16472">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">به خدا قسم این مردک روانی است</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/16472" target="_blank">📅 08:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16471">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCxYTTFA4J_A4w0Q48Mtn0hBoB-xncheUIyw9yZTuy9Jl0Cjhny6EacKsaMHx9SJgoxZSGgEjjSYhfg2QAq-Bhqs_KxgCo81VCcqBhRhulNdYC5CyU0ap-EzppjXbphrKJJA_CRcLXwkW5TkFo_-fj0i9niuc_hTxk2KS4r5E74m10yeVrBZ2owfmReoAKHbwuh3IjWqjV9ZEb3Ttp-1O6fuE0IUz4EGFoo26UQyeAGLlcTnisL-hN9BEsW67TX20jwmb1WKJLx9G4RJUVn5TrMl7Uxhoy49M-aHQvnk_ivOR7ixwLfrbfs5--A3DQC5fS9EGTXNO-IqsdAB8-cysQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگرانی هند از ادامه تسلیح پاکستان توسط چین  پویایی در حال تحول قدرت هوایی بین هند و پاکستان وارد مرحله‌ای بحرانی می‌شود که عمدتاً ناشی از ادغام فناوری پیشرفته موشکی چین توسط پاکستان است.   نگرانی ویژه کنونی هند ، استفاده گسترده از موشک هوا به هوای برد فراتر…</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/16471" target="_blank">📅 07:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16470">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">متن کامل گزارش کنگره آمریکا درباره هواگردهای سرنگون شده ارتش این کشور در جنگ با ایران:  بررسی کلی  در ۲۸ فوریه ۲۰۲۶، ایالات متحده آمریکا با هماهنگی اسرائیل، عملیات‌های نظامی علیه ایران را تحت عنوان عملیات خشم حماسی (OEF) آغاز کرد. این درگیری شامل نبردهای هوایی،…</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/16470" target="_blank">📅 01:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16469">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">متن کامل گزارش کنگره آمریکا درباره هواگردهای سرنگون شده ارتش این کشور در جنگ با ایران:
بررسی کلی
در ۲۸ فوریه ۲۰۲۶، ایالات متحده آمریکا با هماهنگی اسرائیل، عملیات‌های نظامی علیه ایران را تحت عنوان عملیات خشم حماسی (OEF) آغاز کرد. این درگیری شامل نبردهای هوایی، دریایی و موشکی در سراسر خاورمیانه بوده است. سرعت فعالیت‌های رزمی در جریان آتش‌بس در آوریل کاهش یافت. در عرض چند هفته، برخی حملات از سر گرفته شدند و شرایط همچنان متغیر است.
وزارت دفاع (DOD، که «از یک نام ثانویه وزارت جنگ» استفاده می‌کند، طبق دستور اجرایی ۱۴۳۴۷ مورخ ۵ سپتامبر ۲۰۲۵) ارزیابی جامعی از تلفات رزمی در عملیات خشم حماسی منتشر نکرده است. در جریان جلسه استماع ۱۲ مه ۲۰۲۶، حسابرس موقت پنتاگون جولز دبلیو. هورست سوم شهادت داد که برآورد هزینه‌های وزارت دفاع برای عملیات نظامی در ایران به ۲۹ میلیارد دلار افزایش یافته است. او گفت: «بخش زیادی از این افزایش ناشی از برآورد دقیق‌تر هزینه‌های تعمیر یا جایگزینی تجهیزات است.»
در اینجا ۴۲ فروند هواپیمای بال ثابت یا بال گرد، از جمله هواپیماهای بدون سرنشین (پهپادها)، که طبق گزارش‌های خبری و بیانیه‌های وزارت دفاع و فرماندهی مرکزی آمریکا (CENTCOM) در عملیات خشم حماسی از دست رفته یا آسیب دیده‌اند، فهرست شده است. تعداد هواپیماهای آسیب دیده یا نابود شده ممکن است به دلیل عوامل متعدد، از جمله طبقه‌بندی، فعالیت رزمی جاری و نسبت‌دهی، قابل بازنگری باشد.
گزارش‌های تلفات و آسیب‌های هواپیماهای عملیات خشم حماسی
چهار فروند جنگنده F-15E استرایک ایگل
در ۲ مارس ۲۰۲۶، فرماندهی مرکزی گزارش داد که سه فروند F-15E بر اثر آتش دوستانه بر فراز کویت سرنگون و نابود شدند؛ هر 6 خدمه هوایی به سلامت بیرون پریدند و نجات یافتند.
در ۵ آوریل ۲۰۲۶، فرماندهی مرکزی گزارش داد که یک فروند F-15E در جریان عملیات رزمی بر فراز ایران سرنگون و نابود شد؛ هر دو خدمه هوایی در عملیات‌های جداگانه جستجو و نجات به سلامت بازیابی شدند.
یک فروند جنگنده F-35A لایتنینگ II
در ۱۹ مارس ۲۰۲۶، یک مقاله خبری گزارش داد که آتش زمینی ایران یک فروند F-35A را در جریان عملیات رزمی بر فراز ایران آسیب زد.
یک فروند هواپیمای تهاجمی زمینی A-10 تاندر بولت II
در کنفرانس خبری ۶ آوریل ۲۰۲۶، ژنرال دن کین، رئیس ستاد مشترک نیروهای هوایی، اعلام کرد که در ۳ آوریل، آتش دشمن به یک فروند A-10 اصابت کرد که پس از آن سقوط کرد و در عملیات جستجو و نجات نابود شد؛ خلبان بیرون پرید و به سلامت نجات یافت.
هفت فروند هواپیمای سوخت‌رسان هوایی KC-135 استراتوتانکر
در ۱۲ مارس ۲۰۲۶، فرماندهی مرکزی گزارش داد که دو فروند KC-135 در حادثه‌ای بر فراز فضای هوایی دوستانه درگیر شدند؛ یک هواپیما در عراق سقوط کرد که منجر به کشته شدن هر شش خدمه هوایی شد. فروند دوم KC-135 در منطقه‌ای نامعلوم که نیروهای آمریکایی مستقر هستند، به صورت اضطراری فرود آمد.
در ۱۴ مارس ۲۰۲۶، یک مقاله خبری گزارش داد که پنج فروند KC-135 در پایگاه هوایی پرنس سلطان در عربستان سعودی در جریان حمله موشکی و پهپادی ایران آسیب دیدند.
یک فروند هواپیمای هشدار و کنترل هوابرد E-3 سنتری (AWACS)
در ۲۸ مارس ۲۰۲۶، یک مقاله خبری گزارش داد که یک فروند E-3 در پایگاه هوایی پرنس سلطان در عربستان سعودی در جریان حمله موشکی و پهپادی ایران مورد اصابت قرار گرفت و آسیب دید. در ۷ مه ۲۰۲۶، یک مقاله خبری گزارش داد که E-3 در یک مسیر تاکسی بدون حفاظت پارک شده بود.
دو فروند هواپیمای عملیات ویژه MC-130J کماندو II
در ۵ آوریل ۲۰۲۶، یک مقاله خبری گزارش داد که دو فروند MC-130J که از عملیات جستجو و نجات برای یک F-15E سرنگون شده حمایت می‌کردند، پس از اینکه قادر به ترک محل نبودند، عمداً در ایران روی زمین نابود شدند؛ همه خدمه هوایی به سلامت تخلیه شدند.
یک فروند بالگرد جستجو و نجات رزمی HH-60W جولی گرین II
در ۶ آوریل ۲۰۲۶، ژنرال کین در یک کنفرانس خبری گفت که در ۵ آوریل، یک فروند HH-60W در جریان حمایت از عملیات جستجو و نجات برای یک F-15E سرنگون شده در ایران، از آتش سلاح‌های سبک آسیب دید.
بیست و چهار فروند هواپیمای بدون سرنشین MQ-9 ریپر با ارتفاع متوسط و مداومت طولانی
در ۹ آوریل ۲۰۲۶، یک مقاله خبری گزارش داد که ارتش آمریکا از آغاز عملیات نظامی علیه ایران، ۲۴ فروند MQ-9 ریپر را از دست داده است.
یک فروند هواپیمای بدون سرنشین MQ-4C تریتون با ارتفاع بالا و مداومت طولانی
در ۱۴ آوریل ۲۰۲۶، یک مقاله خبری با استناد به یک سند نیروی دریایی آمریکا گزارش داد که یک فروند MQ-4C در یک حادثه سقوط کرده است.</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/16469" target="_blank">📅 01:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16468">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbcWsByvm-c6w-RsxhREYvsNUP37VvtyeT3qo612BYG63n7smDjQkPUfZ5q6Gctrl_y7CaYhvWs60yoSgzsESLI2nVeI7G30sAYvg3ykJugvJJ4E0KxY1onpNexcrNbTWkNboWwwNj2Ymb9Ji3D9LHUElp3fimGeKMFEb69Zflfk22hReJahX5yr_L7PpkA_sdrpdqcp8eU6N5A5a2dySnsbNdzNGgdydaG_7Riw85FCCOUeMXxLj6Ssi_QcjhOV5KEs9D0TPOBFNXtAeAI8TYdBa5_XpMrT005iS4AxWnwiqwOTDhjgN5ko3rAwxieYx-IH2ijiqPCoRQxMJBtP6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم با توجه به اینکه این بار نه نفت افت کرد و نه نرخ های بازده خزانه داری و عملاً توییت مثلاً صلح طلبانه ترامپ بی اثر بود، هر لحظه احتمال تهاجم نظامی آمریکا و اسرائیل می رود.</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SBoxxx/16468" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16467">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خداوکیلی مملکت عجیبی داریم!
انفجار روی می‌دهد دلیلش نامشخص !
گردوغبار همه جا را می‌گیرد دلیلش نامشخص!
وزیرخارجه مملکت به نیویورک می‌رود نماینده مجلس خبر ندارد!
سبحان الله !</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16467" target="_blank">📅 00:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16466">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خبرگزاری مهر ایران: صدای انفجار در جزیره قشم شنیده شد، علت نامشخص است.</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/16466" target="_blank">📅 00:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16465">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس:
امیدوارم خبر سفر عراقچی به نیویورک برای مذاکره در خصوص تنگه هرمز دروغ باشد
چرا ما در خصوص موضوع تنگه هرمز باید در خاک دشمن مذاکره کنیم؟</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SBoxxx/16465" target="_blank">📅 23:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16464">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ در حال ساخت یک پناهگاه زیر سالن باله است
او می‌گوید بیمارستان، تأسیسات تحقیقاتی و اتاق‌های جلسه برای ارتش، در حال ساخت زیر سالن باله کاخ سفید هستند.</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16464" target="_blank">📅 22:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16463">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نیروی دریایی آمریکا یک نفتکش متعلق به شرکت ملی نفت ایران با بیش از یک میلیون بشکه نفت خام  را در اقیانوس هند توقیف کرد.</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16463" target="_blank">📅 22:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16462">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نیروی دریایی آمریکا یک نفتکش متعلق به شرکت ملی نفت ایران با بیش از یک میلیون بشکه نفت خام  را در اقیانوس هند توقیف کرد.</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/16462" target="_blank">📅 22:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16461">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔺
پزشکیان: بیایید اروپایی باشیم
🔹
رئیس‌جمهور: بیایید در مصرف انرژی مثل اروپایی‌ها باشیم. ما الان ۳ برابر اروپا گاز و برق مصرف می‌کنیم.
🔹
اگر بد مصرف کنیم، در تابستان و زمستان مشکل خواهیم داشت و این بدمصرفی به گرانی و بیکاری تبدیل می‌شود.</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/16461" target="_blank">📅 22:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16460">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔺
پزشکیان: بیایید اروپایی باشیم
🔹
رئیس‌جمهور: بیایید در مصرف انرژی مثل اروپایی‌ها باشیم. ما الان ۳ برابر اروپا گاز و برق مصرف می‌کنیم.
🔹
اگر بد مصرف کنیم، در تابستان و زمستان مشکل خواهیم داشت و این بدمصرفی به گرانی و بیکاری تبدیل می‌شود.</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SBoxxx/16460" target="_blank">📅 22:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16459">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ونس به جای ترامپ!   ای کاش ترامپ صفر تا صدِ پروندهٔ مربوط به مذاکره با ایران را به جی.دی ونس معاون خود می‌سپرد و خودش بخصوص از اظهارنظر در این زمینه خودداری می‌کرد! ونس حداقل گویا و آرام و قابل فهم سخن می‌گوید، اما ترامپ با زبان تحریک‌آمیز و شلخته‌اش فقط شرایط…</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SBoxxx/16459" target="_blank">📅 21:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16458">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">معاون رئیس‌جمهور جِی‌دی ونس درباره ایران: من فکر می‌کنم اینجا فرصتی داریم تا رابطه‌ای که بین ایران و ایالات متحده طی ۴۷ سال گذشته وجود داشته را بازتنظیم کنیم.  رئیس‌جمهور از ما خواسته این کار را انجام دهیم و ما هم به تلاش ادامه خواهیم داد، اما این کار دوطرفه…</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SBoxxx/16458" target="_blank">📅 21:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16457">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
ترامپ می‌گوید جدول زمانی برای ایران ۲-۳ روز است، شاید تا اوایل هفته آینده.</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SBoxxx/16457" target="_blank">📅 21:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16456">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">معاون رئیس‌جمهور جِی‌دی ونس درباره ایران: من فکر می‌کنم اینجا فرصتی داریم تا رابطه‌ای که بین ایران و ایالات متحده طی ۴۷ سال گذشته وجود داشته را بازتنظیم کنیم.  رئیس‌جمهور از ما خواسته این کار را انجام دهیم و ما هم به تلاش ادامه خواهیم داد، اما این کار دوطرفه…</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SBoxxx/16456" target="_blank">📅 21:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16455">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">معاون رئیس‌جمهور جِی‌دی ونس درباره ایران:
من فکر می‌کنم اینجا فرصتی داریم تا رابطه‌ای که بین ایران و ایالات متحده طی ۴۷ سال گذشته وجود داشته را بازتنظیم کنیم.
رئیس‌جمهور از ما خواسته این کار را انجام دهیم و ما هم به تلاش ادامه خواهیم داد، اما این کار دوطرفه است. ما توافقی نخواهیم داشت که به ایرانی‌ها اجازه دهد سلاح هسته‌ای داشته باشند.
پس، همانطور که رئیس‌جمهور همین الان به من گفت، ما آماده و مسلح هستیم. ما نمی‌خواهیم به آن مسیر برویم، اما رئیس‌جمهور آماده و قادر است اگر لازم باشد به آن مسیر برود.</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/16455" target="_blank">📅 21:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16454">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/16454" target="_blank">📅 20:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16453">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمو | مطالعات تخصصی آسیای مرکزی</strong></div>
<div class="tg-text">🔘
اقدام نمادین دولت تاجیکستان در انتقال خاک مزار «قهرمانان تاجیک»
⬅️
با پیگیری
دولت تاجیکستان
بخشی خاک از مزار «قهرمانان تاجیک» که عموما چهره های نخبه و بنیانگذاران تاجیکستان مدرن در دوره شوروی بودند در اقدامی نمادین به این کشور منتقل شد. از جمله این افراد شیرین شاه شاه تیمور، نصرت‌الله مخصوم و نثار محمد از بنیانگذاران تاجیکستان بودند.
🔹
صبح روز ۱۹ مه، امامعلی رحمان، رئیس جمهور تاجیکستان، با ادای احترام به یاد و خاطره آنها، جعبه‌های حاوی خاک مزار این چهره‌های برجسته تاریخ معاصر تاجیکستان را دریافت کرد.
🔹
نماز میت این چهره‌ها در مسجد جامع مرکزی دوشنبه به نام امام اعظم برگزار شد که در آن رستم امامعلی، شهردار دوشنبه، شرکت کرد. پس از آن، خاک نمادین در گورستان لوچوب به خاک سپرده شد.
🔹
شیرین شاه تیمور، نصرت‌الله مخسوم و نثار محمد در سال ۱۹۳۷ در جریان سرکوب‌های استالینیستی به اتهامات سیاسی در مسکو اعدام شدند. آنها در گورهای دسته جمعی در نزدیکی مسکو دفن شدند. پس از مرگ استالین، در دهه‌های ۱۹۵۰ و ۱۹۶۰ پرونده‌های این چهره‌ها بررسی و از آنها اعاده حیثیت کامل شد.
آمو | مطالعات تخصصی آسیای مرکزی
@C5_Amu</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SBoxxx/16453" target="_blank">📅 20:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16452">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">به نظرم با توجه به اینکه این بار نه نفت افت کرد و نه نرخ های بازده خزانه داری و عملاً توییت مثلاً صلح طلبانه ترامپ بی اثر بود، هر لحظه احتمال تهاجم نظامی آمریکا و اسرائیل می رود.</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/16452" target="_blank">📅 20:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16451">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔻
غریب آبادی ؛ معاون حقوقی وزارت امور خارجه دولت :  برای ما تسلیم شدن معنایی ندارد ، یا پیروز میشویم یا شهید</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/16451" target="_blank">📅 20:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16450">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dr4AhivuKz0SiZeri1mfBRjKZklFhE9wpMmagjgckYN5vcBngpaOlrdTCCzhbPDppXOT63HX_DxH9eZbLTMSeGD6KOg4LTnhiuvyaDc7uW3jvfohy8xfbAN1rEQk2iIM88okLybUnRuaQIiKWj_KlojZVqzs1Ws8k1Yf0YbpYCRXAzfmHh5_NmcZpugbCT6oCWEYN87ymAbqNtNj0IqY7bhbsyWhyB7AWWmK8bB4N2j-fycQ2IM-v72yk02yOQ0fwCQ75SAk3rwBXmSxp0ah5oHEG6qa_lYTHXAY3m-692_PbI0vibdRrMA4oLsfxfa6hm4jHiiJMQa3qIl6gMyc0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
غریب آبادی ؛ معاون حقوقی وزارت امور خارجه دولت
:
برای ما تسلیم شدن معنایی ندارد ، یا پیروز میشویم یا شهید</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SBoxxx/16450" target="_blank">📅 19:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16449">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjtm9R6uw2D8u3Opxy9jZiRIPOX6CvNjqRT05ajcmvFMkTgSFUSJimVGH27sijlySf96Khiq-6oZkw3t-D5KTIpxKYy0rXFeMeluk_TdFgnVEbwtObFM7hjTTN-CID1c-UTGykaF2oYuW2haj_AtaQ86XKDDqV_GFpOJ3VFxjGBJTUXySxQyz8ic3j545-UNKG_iYxZATsxO9FXgEhmSk0ZC_rwYKKLBrtM4K4ZIPyc2BOlUmz4QkDwmYwR964mzKTqo7Qh_tmumB-8gFGkKsUIqLOiJGLSQ-vga4N6HzjoJ7IuAANnb4npRU2ywjb6FxI2dVVbrx5IthCx_QQMJZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه اسراییل بزرگ روی بازوی برخی نیروهای نظامی این کشور  با این تیمی که ترامپ چیده بعید نیست به این سمت حرکت کنند. بیخود نیست وزیر دفاع ترکیه هم نگران شده است.  برخی اطرافیان ترامپ رسما باور ایدئولوژیک به اسراییل بزرگ دارند.</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SBoxxx/16449" target="_blank">📅 15:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16448">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اینقدر که ما نگران خطای محاسباتی آنها هستیم خودشان نیستند.</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/16448" target="_blank">📅 15:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16447">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اینقدر که ما نگران خطای محاسباتی آنها هستیم خودشان نیستند.</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/16447" target="_blank">📅 15:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16446">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پدرسگ های کافر هر 5 ماه یک بار دچار خطای محاسباتی می شوند حرامزاده ها</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SBoxxx/16446" target="_blank">📅 15:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16445">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فوری | فرمانده نیروی زمینی ارتش ایران: دشمنان نباید در محاسبات خود در مورد توانایی‌های نیروهای ما اشتباه کنند.</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SBoxxx/16445" target="_blank">📅 15:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16444">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⭕️
معاون امنیتی خوزستان
:
امروز  براثر تست پدافند و برخورد پرتابه های آن به یک منزل مسکونی ، متاسفانه ۴ نفر از شهروندان عزیزمان مجروح شدند</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/16444" target="_blank">📅 15:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16443">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هاکان فیدان:   اورانیوم غنی شده ایران باید خارج شود یا به صورت سه‌ونیم درصدی تغییر داده شود</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/16443" target="_blank">📅 14:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16441">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هاکان فیدان:
اورانیوم غنی شده ایران باید خارج شود یا به صورت سه‌ونیم درصدی تغییر داده شود</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/16441" target="_blank">📅 14:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16440">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خبرگزاری تسنیم:   فعال شدن توپهای ضدهوایی در جزیره قشم به دلیل پرواز پهپادهای کوچک در حریم هوایی این جزیره بوده است.</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/16440" target="_blank">📅 14:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16439">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">در بازگشایی باشکوه بورص، این نمادها کماکان بسته خواهندماند:  #مبین • #نوری • #پارس • #آریا • #جم • #جم‌پیلن • #شپدیس • #زاگرس • #بفجر • #مارون • #شکبیر • #شگویا • #اروند • #بوعلی • #شفن • #شغدیر • #شجم • #شفارا • #شیراز • #شاوان • #فخوز • #فاهواز • #فولاد…</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16439" target="_blank">📅 14:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16438">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiONyegx1tF6c-dSTeuKgFKlVfAN7C4EE9xcJNuk5SoxIosqQ2aB505VZFKM-zBvCkccHSLdM9tGhBwaFltL2rDF4yBj-WOAebIeBh4VJMrLBc9EZ6qC-ZjuLko1fGo7xJqOL-3PatyTV1ZNE_j1ocCA3PU4QIfGxjWttILMkMDj2pluVqPX7D2vhXoRXIwbPsfNlAuC5XmrjNZDR6PqnSurVfU7gacYTjBAT8Vibs7pPaO0Asi4ZP-fFagYQRjAFCF40H8a6HzvNYjvxQ9rxxFNen57_I3J4xfHhE2wKUii68kDlTZaUsVE_npeP1DWRymN07OOd2iJ1gAP2i4epg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشورهای دارای بیشترین نرخ زادورود!
هند زیبا در صدر!</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/16438" target="_blank">📅 10:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16437">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">چرا میخند؟!</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/16437" target="_blank">📅 10:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16436">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکاخ رسانه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe204bf88.mp4?token=mQPsvwoQvrydtlQeY1_Qv2ct6P51EP8Sxe6_D1GMFNI9PTDgVphFFPR7oGisHVdA84WKqPuPA7TFMg11NJHY3q6hCmWiJYrbe8d9Gnf80B2L5kVlqmh1UwqpXTM3fJGFlw-tzLfolmrKOkm8QTwihBWdsTnUm6tR4ft_xXgpJ7NCUX59RJJLSJVL3bzNq9ckV8ZEf5hZpE1pJueeIhN0HseLpW02ucjU137niVmpMstXKZ8BtWnAYdd9fJ17seZdWfwkYzckyl_J8XdNHpieKGkRh5pOdVGxRJ31XN8rZgzHZwHCI30Vmbml85XywJJGuGHDhhmiTJESeeWtfpwsaqZoBLSrLQRUfiBe-2WzLZ4eQ3Fwu6AgTU7NTyPTBIuqlP3jvWTX5ywkL08SzTcQEAh92Hq2jHmpiwsISKCYKihpz6rwgPTusOTvt2h-MZggBJi8ttTedsmfygF58pQmhUB3I_6kEFtPKg6teav3iBktcGKlomU3YwqKYkA1oxn2tzI_kx8tUT0N5yjgBppkPDDSBIavHdwuIcdSaXBv0Jx61jbi7B9cdLJ1raE8AWIshcI1d3Zo8bRrcaL4MaA0c2ICMWvmcStogyKVD88W6zyvYvBTB9hwYjdjJ38DPJ0fDU69LjjrsakKQbmeHGmj6dMVQDEHwG9vXM27KGbA7-E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe204bf88.mp4?token=mQPsvwoQvrydtlQeY1_Qv2ct6P51EP8Sxe6_D1GMFNI9PTDgVphFFPR7oGisHVdA84WKqPuPA7TFMg11NJHY3q6hCmWiJYrbe8d9Gnf80B2L5kVlqmh1UwqpXTM3fJGFlw-tzLfolmrKOkm8QTwihBWdsTnUm6tR4ft_xXgpJ7NCUX59RJJLSJVL3bzNq9ckV8ZEf5hZpE1pJueeIhN0HseLpW02ucjU137niVmpMstXKZ8BtWnAYdd9fJ17seZdWfwkYzckyl_J8XdNHpieKGkRh5pOdVGxRJ31XN8rZgzHZwHCI30Vmbml85XywJJGuGHDhhmiTJESeeWtfpwsaqZoBLSrLQRUfiBe-2WzLZ4eQ3Fwu6AgTU7NTyPTBIuqlP3jvWTX5ywkL08SzTcQEAh92Hq2jHmpiwsISKCYKihpz6rwgPTusOTvt2h-MZggBJi8ttTedsmfygF58pQmhUB3I_6kEFtPKg6teav3iBktcGKlomU3YwqKYkA1oxn2tzI_kx8tUT0N5yjgBppkPDDSBIavHdwuIcdSaXBv0Jx61jbi7B9cdLJ1raE8AWIshcI1d3Zo8bRrcaL4MaA0c2ICMWvmcStogyKVD88W6zyvYvBTB9hwYjdjJ38DPJ0fDU69LjjrsakKQbmeHGmj6dMVQDEHwG9vXM27KGbA7-E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داماد شهید رئیسی: شهید رئیسی اثبات کارآمدی نظام ولایی را رسالت خود می‌دانست
صادق توسلی، داماد شهید رئیسی:
🔹
جوهر اصلی شخصیت شهید آیت‌الله رئیسی را می‌توان در دو واژه «تعبد» و «ولایت‌مداری» خلاصه کرد.
🔹
آنچه در سلوک ایشان به وضوح لمس می‌شد، احساس رسالت عمیق برای اثبات کارآمدی و موفقیت «الگوی نظام ولایی» در هر جایگاه و مسئولیتی بود.
🔹
تمام اهتمام و مجاهدت ایشان بر این اصل استوار بود که مردم برکاتِ ملموس این نسخه یگانه و نجات‌بخش را در زندگی خود احساس کنند.
🔹
رابطه عمیق، عاطفی و سرشار از محبت میان ایشان و امام شهید، صرفاً یک دلبستگی فردی یا عاطفه شخصی نبود؛ بلکه ریشه در یک پیوند تشکیلاتی و ولایی داشت.
🔹
این ارتباط ساختاری با ولی‌فقیه به عنوان عمود خیمه نظام، با این هدف تعریف شده بود که خروجی کارآمدیِ حاکمیت دینی را در عرصه اجرایی به ثمر بنشاند و حقانیت این الگو را در عمل پایدار سازد.
@kakhresaneh</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16436" target="_blank">📅 10:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16435">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">معاون وزیر امور خارجه ایران:   رفع تحریم‌ها، آزادسازی منابع مسدود شده و پایان دادن به محاصره در پیشنهاد اخیر ایران به آمریکا گنجانده شده است   پایان جنگ در همه جبهه‌ها، از جمله لبنان، و خروج نیروها از مناطق نزدیک به ایران نیز در این پیشنهاد گنجانده شده است</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16435" target="_blank">📅 09:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16434">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">معاون وزیر امور خارجه ایران:
رفع تحریم‌ها، آزادسازی منابع مسدود شده و پایان دادن به محاصره در پیشنهاد اخیر ایران به آمریکا گنجانده شده است
پایان جنگ در همه جبهه‌ها، از جمله لبنان، و خروج نیروها از مناطق نزدیک به ایران نیز در این پیشنهاد گنجانده شده است</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SBoxxx/16434" target="_blank">📅 09:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16433">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6nd-6Ygxh-2f3cWpNoYrCxFB-aTMc3-EVTpXnjzCvr4uUClpl5gNWrJjCZK1I0ix9N9cfXzQhAGei5DAiRBY9Hr9DMUcC8nPJU0QQ36CppQuHKTuwy79xK5nXXFpCPvHbY73QbmGaTqJbnO5A1sVIPyOCzbRDL9pqg_Iw1dN0CBvqfB8k--61Cmtz866BMWpHqUHl6nifp3cQvpR4Dlnj9qI-ZZmx-zdWSzZDUnCTneotlBlyAhKnPwgXZm99fyMKN-J2W0HwpqctIh23fWd3OvKQKLsStnEacvTg7Li5_lMWPgByW1O5u5OjXEiW6FfGWPpLPjh5fCKfJcsPPKWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ نیابتی آمریکا با بلوک چین در شاخ آفریقا هم نمود پیدا کرده و دیشب نتانیاهو اعلام کرد که اسراییل، استقلال سومالیلند را از سومالی به رسمیت میشناسد.  جالب است بدانید که سومالیلند از ۱۹۹۱ دارای دولت و ساختارهای حکومتی خودش است و اتفاقا از دید قوام نهادهای مدنی…</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16433" target="_blank">📅 05:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16432">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خبرنگار:
«آیا گزارش‌هایی را شنیده‌اید که می‌گوید ایران دیگر درباره تعهدات هسته‌ای صحبت نمی‌کند؟»
ترامپ:
«چه سوال احمقانه‌ای. من چیزی نمی‌شنوم، ما در حال حاضر در حال مذاکره هستیم، تو چه آدم احمقی هستی. من در این مورد با تو صحبت نخواهم کرد.»</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16432" target="_blank">📅 05:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16431">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioNosWHOJgbY6qqaq-N-v5QskeQbycV0dSdAcf-XnimTSAk8OBTOT4WMEuyBA566MipUHypgWnVCDswLiXG21ZUS-lV0gHCCF1BSKCDtvvF0LhpWyv_CFFw8LpP1GSaWPxMum9YIpTuvMWxaojcicvZyu2rD9UAOPXTZlfDICdB4bBwjmSiQDdLMWoHG0m5wR1ni5npWZfjYWc3F1TVlNfEKhvLGcmqrNzWgWZEsnTWxDJUYpJGXenqplsg1Cb1W8J68bypyE_pFmS4xGGPmgCujx4x-zddsQr38tAo4Ub-a9dtPwpufz_QaKb6wRpg4jbHIhQhtFlHsHiA5VXjWug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب گویا شماری از مجریان صداوسیما فاز امام جمعه بودن برداشته و با سلاح در برنامه شان حاضر شدند!  سبحان الله !</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/16431" target="_blank">📅 00:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16430">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تقریباً ۹۰٪ از کشورها اکنون شاهد روند افزایش بازده‌ها هستند و نرخ جهانی ۱۰ ساله به بالاترین حد پس از سال ۲۰۰۸ رسیده است.</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/16430" target="_blank">📅 23:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16429">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">زیرنویس شبکه خبر!</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/16429" target="_blank">📅 23:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16428">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhfZOWNlyxpb5Z8VDfX83THo7v_YqOf4MTFGxy0oUloPF54o-2jrZ3xO_W57EoJeGgDtPTqDreIyi_P0Qq6C4BDWhvnRPX2uYBHgd6GzpRxxQBOIw0egakb4P-4PXiVrQH_pLeD4ThMFLRKocfUSS8JMJJ_JsZDk8Abwb4A59LHZKDuJ1GbvKvAs9xaQIcBIR7xiZr74TcMorHCcq55mBz14OyQ3amELw6QArNKLaT-Jez_ndYdidRMekAooZV6-v4DkjsmmjKBcRqJbbIW67VQftJxCBsUj7K8AAfhRhdlzZMVikSGxOo4GdBQc5hjNlIrsSfNJx_6wE3g1yj2cbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر!</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/16428" target="_blank">📅 23:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16427">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خبرگزاری تسنیم:
فعال شدن توپهای ضدهوایی در جزیره قشم به دلیل پرواز پهپادهای کوچک در حریم هوایی این جزیره بوده است.</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16427" target="_blank">📅 23:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16426">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">به خدا قسم این مردک روانی است</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16426" target="_blank">📅 22:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16425">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">I have been asked by the Emir of Qatar, Tamim bin Hamad Al Thani, the Crown Prince of Saudi Arabia, Mohammed bin Salman Al Saud, and the President of the United Arab Emirates, Mohamed bin Zayed Al Nahyan, to hold off on our planned Military attack of the Islamic…</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16425" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16424">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDonald J. Trump</strong></div>
<div class="tg-text">I have been asked by the Emir of Qatar, Tamim bin Hamad Al Thani, the Crown Prince of Saudi Arabia, Mohammed bin Salman Al Saud, and the President of the United Arab Emirates, Mohamed bin Zayed Al Nahyan, to hold off on our planned Military attack of the Islamic Republic of Iran, which was scheduled for tomorrow, in that serious negotiations are now taking place, and that, in their opinion, as Great Leaders and Allies, a Deal will be made, which will be very acceptable to the United States of America, as well as all Countries in the Middle East, and beyond. This Deal will include, importantly, NO NUCLEAR WEAPONS FOR IRAN! Based on my respect for the above mentioned Leaders, I have instructed Secretary of War, Pete Hegseth, The Chairman of The Joint Chiefs of Staff, General Daniel Caine, and The United States Military, that we will NOT be doing the scheduled attack of Iran tomorrow, but have further instructed them to be prepared to go forward with a full, large scale assault of Iran, on a moment’s notice, in the event that an acceptable Deal is not reached. Thank you for your attention to this matter! President DONALD J. TRUMP</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/16424" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16423">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voMepy8bMec7MeM_K7aLWhdNTcbcYSROR8fSF78SndOyKFTprnv6uS48ToBOJX4krL7-Z9NEV7dik3BgEi8aVeYlbj9_DFEpydRnts2nga6bYztthjNZH6YdIkLBi0y28Esw3Hoh8zps8n0j9rTXmfa23HlbXQmyPD0FyHjColrNqeUv-c0JILojISwG-ExNTQjg-28PhEAImYdwKJrG6aCNK1AKx9XPTJ3IKk1r86GAXNkQSx0xY4xrSEIH8Hbjzy0apKxjdnAsVxYDh_LY1UkidacwiR-YOs__zDKe9dGWS0_9XlRr9YL3fJpGsoZLcLCdTzC41UpuTkem1HfIdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/16423" target="_blank">📅 21:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16422">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ:
«رژیم ایران می‌داند بزودی چه اتفاق وحشتناکی برایش می‌افتد»</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16422" target="_blank">📅 21:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16421">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♨️
پس از رد پیشنهاد جمهوری اسلامی ایران توسط کاخ سفید ، وزیر پاکستان ، خاک کشور را ترک کرد</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/16421" target="_blank">📅 20:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16420">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_IJbFN9ArNd_J6RIqhSwptk9-oScQ7fCGrhWZLqa960L_VExcaMJ7eOKrwQcpVh702XTQzjzbDkxHKHvTIilhDrrigKebGsu97vd3Dc7RmeZfcJjs3KVKw0-fWDC6GuzAfjhp8gVGCbDUfTarFjfhGnuu3l3DFhmpEffGNex8EUinhs7FTPQVkfipzTNodnWYe8e4_VIK42SoJzs3uMCWGa2raRTmUl8h7sC7gAHdDPUF4esc7Wl0kecsKx1Hd7Qk2_YK_Bn1QHqmzLmsADlbEG2TX3VpaMXPk4R7qNJUxTGZfXSC90SchQ_dbQ_U6aVgpCEv8yXbSVUvnsTUkrlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صلاح مملکت خویش خسروان دانند اما چیزی که من حس میکنم این است که یک «اجماع» بزرگی دارد شکل می گیرد که آخرش شاید به جماع عظیمی ختم بشود ولی خب.</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/16420" target="_blank">📅 19:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16419">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">قلعه‌نویی، سرمربی تیم ملی:   40 درصد عقب‌ماندگی بدنی و فنی داشتیم که 25 درصد آن را جبران کردیم، شرایط سخت است ولی نباید بهانه بیاوریم.</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16419" target="_blank">📅 18:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16418">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">همه تیم ها دارند تدارکات عالی برای جام جهانی میبینند ما هم داریم اینطوری با خودمان ور می رویم!</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16418" target="_blank">📅 18:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16417">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ارسال پیشنهاد اصلاح شده ایران به آمریکا از سوی پاکستان</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16417" target="_blank">📅 18:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16416">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">📌
تأثیر منفی بسته شدن تنگه هرمز بر سیاست‌های پولی غربی: اهرمی برای ایران   بسته شدن تنگه هرمز می‌تواند با افزایش قیمت انرژی، بانک‌های مرکزی غربی را به سمت سیاست‌های پولی انقباضی و نرخ بهره بالاتر سوق دهد.  افزایش فشار اقتصادی و تورمی بر کشورهای غربی، ممکن…</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/16416" target="_blank">📅 14:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16415">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">احتمالاً زمان بازگشایی بازار بورص هفته آینده اعلام شود</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/16415" target="_blank">📅 13:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16414">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ارسال پیشنهاد اصلاح شده ایران به آمریکا از سوی پاکستان</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/16414" target="_blank">📅 13:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16413">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ارسال پیشنهاد اصلاح شده ایران به آمریکا از سوی پاکستان</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/16413" target="_blank">📅 12:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16412">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ji_43IWVQ4lbIRiOH1JR_WVRgbVOW19ih3A9rfum_zWQl8wzVvEj9paal6UymBrhZ1_b3nC9XrqdtT4dTKiDiQKllEKZaHZTWl1VMsLZanWwjixX0Mofauma5R7pzeeZZxtryhviLIhqSWqROtR3l4jOnmq4NzVYUT7tbp40EHcvD8v9FZdxYctSYJ3GKWF0lMXq59I32XI8tjCN88N6mr8KVwPwLSalJTPvfnGyWwLdQc35B_Xd-vLKIoGXbO-i-kykmQQXqyFuEdw8KlRXrfYWySXSG-G1XhER_SpNIgocLd0GHBIcRIiPp8j0m-AxyCiifpBwMgO-PxXnfq8WSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/16412" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16411">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🟣
خبرگزاری CNN :  کابل های اینترنتی تنگه هرمز ، توجه ایران را به خود جلب کرده است</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16411" target="_blank">📅 10:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16410">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Id32Bz9FlU-psGc_dlpxWFXENqIVoGKtgbg9UDAzVmXPAz-Or7VCiwyLw87uSXk2W0kwfmwYes3xFRYhBX2M5oXvduiNkuA92qpZS2Fo9RIRke5pmuauKh2ImSntv9PFYcYeFYeFWj03rqdkmFziBbs51ehypWH6c7aDDYczHlmmwbw1Lp1mQamryoKb77hAXBeWaJf19qCV2XRaUIp98MVuuDemR_zfR7z4n_cQVk2PZqtSw-o27FeMAv0jxQTU5lsv_kWIKRLpKeEmz7rU7XArGyiVeZBIJTtW1ag7HT-rViO46TQ8lR9A06Bm3oJHTVFQi_WchWKESA2hJTzkgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL -- H4
💬
ارتباط با پشتیبانی : @cyclicalwavessupport
📌
کانال ما : @cyclicalwaves</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/16410" target="_blank">📅 09:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16409">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWQH4_G1KpMOhiKiqXUFTsnyhekoBPNDKkze2fBnDAONtpxIzuVk3ICrKTuWsXcqevwsyN9CjZrdOy0AGjgH952wxVsyIB4Ucc4J4UAoqN7LgnEWtiJWcYjIERdzmWiCyRBD_RbVx5sz1P5xNQlk_s1-6BOBOJw7oG0o9M8mJ53jXfQ6BOlSwfAtRorVNWQaJhYiiCk9qpjRfbm5Ml7ShmvXx4gloHCaCUc9X3LHLta9MwO_FS_OVlioOLBrcZOY98Ba2Vf82Okd6cAx_nGVVvsL-1GEVmH6GtwUtDltRLf-4wjC5r8eJ767-kp1zg_qCtOY2lnY51t_H5jOE1iYXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین که ترامپ مردد است بین کوین هست یا کوین وارش کدام را انتخاب کند نشان می‌دهد یا دنبال دستکاری بازارها است یا اساسا نمیداند این دو در دو سوی طیف سیاست پولی هستند؛ یکی بشدت هوادار تسهیل پولی (هست) و دیگر طرفدار متعصب محافظه کاری و انضباط مالی (وارش)</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SBoxxx/16409" target="_blank">📅 09:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16408">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">#URA — D  #سهام_خارجی  این یک فرصت ویژه ایرانیان خارج کشور است. صندوق ETF اورانیوم می تواند در قالب موج 5 خود دستکم 70 درصد رشد داشته باشد که در چارت می بینید.  نظر به مسخره بازی ما در تنگه هرمز، احتمال هجوم سرمایه ها به انرژی های جایگزین بالاست و انرژی هسته…</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/16408" target="_blank">📅 09:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16407">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SBoxxx/16407" target="_blank">📅 09:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16406">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجنگاوران</strong></div>
<div class="tg-text">تلویزیون دولتی آموزش زنده‌ای درباره نحوه استفاده از
مسلسل پی‌کا
پخش کرد.</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/16406" target="_blank">📅 07:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16405">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKtf6NpRHhsNcGiGyAmQOpyBD9I-Cv_5ZiLf8Gr4JJ027vG0jfVxW3nHj9SjeVHR4rXhSvGeSNcFD1IiVEDP9RtT6oOEyn_mWID318uoNVh1qxF_KdHCi2gk-XehjB5B_zC-sLVmCwmNNR5MO5CC0hvWKnjCJpkMEr8X-tdQ8ItHMiuq2FEHh1cyAzaguaTQymPrORgHSDO0hwnQ25annfSAXfobwwbZXtlEiRKmq60I74f5c2yEwQCbZ6eycwj-tKVBEgSF9qTqSE9VpxWVwi8HWkMIGbRlVjMWqSyh0IZ_HCB0Ihpy1CVwyGblx1u4VJU49AyKjTnQ87vL3HdFSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gold/UKOIL — W  افت 45 درصدی نسبت طلا به نفت پس از ارائه تحلیل.</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/16405" target="_blank">📅 06:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16404">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvN4wXsbvPRxJHMGx6smljgXTkDuxQxMdPzx5SFGc3xUyuFhv_7PR_u18GbdgaXDglM2ilJrKi1mT7PEutrIKSMOkdT3d1lBs_dyP3-qJmu6bG4f1DeFEG376zNOdsB7RcfE6ghVYF6k_YC61uloog8kwaOxbn2x9WFG30_zvOA1RGTqFBDLJvOyUtuYubYBUhn2xQePNr1xe2f27wiUB8KabW6P9y3CT0CrRb0wrtIA0WRTr_1I1FaDN4l5Bx5CLFR6AAN5MVDLIAVicsq_d5NJfBsMINJOjmuqku3mHSLk0YVwIR4BWzOnp60rjY13LuD-IzZNyQfrrCZL32MFjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشخص است کله زرد خسیس رفته نسخه رایگان هوش مصنوعی کذایی را که با آن کار می کند خریده و گرنه این همه اسم شهرهای ما را اشتباه نمی نوشت.  رشت = Majd? تبریز = Toha?</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SBoxxx/16404" target="_blank">📅 06:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16403">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پست جدید ترامپ که به نظرم به نوعی تاییدی بر حمله زمینی است.</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/16403" target="_blank">📅 06:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16402">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ارتش عراق:   اجازه نمی‌دهیم عراق سکوی پرتابی برای تعرض به سایر کشورها باشد</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SBoxxx/16402" target="_blank">📅 05:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16401">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حقیقتا «الکسیس میانرودان» لقب شایسته ای برای عراق نیست؟!  تل آویو - اسرائیل برای پشتیبانی از عملیات هوایی خود علیه ایران، یک پایگاه نظامی مخفی در صحرای عراق ایجاد کرد و حملات هوایی علیه نیروهای عراقی انجام داد که تقریباً در اوایل جنگ آن را کشف کردند.  به گفته…</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SBoxxx/16401" target="_blank">📅 05:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16400">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkznMW95Y8uK4bAQQbUqHfFZCmP6SQm7ucbI3ZJXVARi48LQ8ryI3_b9SCmxL5IsaOOJPBaIDDCpwCYfA_BThL0WAP7wrCZgXBB5Nc0CLh5R4YwYrAEt6dSAbGW5C5Org7RFZXq0HU1Lg9DxVXvoUvsIv3seGCpySHJOa3GnqIRpZoZnIlgdP_nNo1HaPDMCzvQOn91NL8N3o1R4C5JRt0ESfg3gKNZ_kL9liiklGcc3yt8Dk-ARdGVQZU-VpxXxtfUgepLmc69b1SD28QkwDQTtTxl6n5rcymZFfvJnZqtDl5TkoAQPMRcPunu3S-i4oidcLpoCPYJWQQEs5B5LMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج ۵ نبرد ایران و آمریکا همراه با هلی برن گسترده با حمایت هوایی سنگین خواهدبود و تسلیح یگانهای ویژه نظامی در ایران به تفنگ‌های دورزن و موشکهای پدافندی دوش پرتاب و نیز موج آموزش عمومی کار با اسلحه در صداوسیما و مساجد و … در راستای مقابله با این تهاجم است.</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/16400" target="_blank">📅 05:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16399">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uszjj9qm-1GJqqjjZPRLQyvBSK1ulBzkGmyAKWK06SpIBejW8d15WLUwVQMv3QdXjn_9bUqf1Jqt1NRNDKePdqS-InS7yCkPe3VQqIZ-DNVtdkIXUc6HfSyb-MRK-fCEH-ocC34NHqngBsYqa54VmyVv2nm6QbZUF1rgdKcMbrcWr1iODgrQRsv7Hb21mkCtSCPFJ0_bG66AEd95RKwE4fysGMvOdydibp8zIPJXH7J7RCh2F0tOHPX1pRelsPORc_bQrrJPUsz2ETZtPXbE2O8aD4zlahxyisxL7CWFWmJbZMrswj7WdXjSlutp1tw3ChuMGy3beGW8B8lgA1IUtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/16399" target="_blank">📅 05:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16398">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b124790efc.mp4?token=JT2_zf6RQ4rD-fO4jravcLmqsGVC6Dv95hkv5KeJO6TqVbgsTNPUVpgT9ur9SUehhot5oEk94FNMORAfjhL5QANPpI03AzJEKXYpltH8wlWY56ckUxuds0T_o5u1O4awKSaG9BlIIreGk4v4vgNbyI_ZvaC7LuM_c_Z_n8hcg2_sOU_W33dg9t15jKn8v6eEKrg9YDsLEzQizf7vrFDkURaMmNCBVidjiwzUPqKy4b3ymIIYTNVVTBQlcTEprwqF0PgukiO40nkIIhvPcIeknDVrIkGE7b4tmHBUpfJG4axkuFqDmeBYzxLSZeM0902jZ3PJIvBpp4sNqbepIV3BQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b124790efc.mp4?token=JT2_zf6RQ4rD-fO4jravcLmqsGVC6Dv95hkv5KeJO6TqVbgsTNPUVpgT9ur9SUehhot5oEk94FNMORAfjhL5QANPpI03AzJEKXYpltH8wlWY56ckUxuds0T_o5u1O4awKSaG9BlIIreGk4v4vgNbyI_ZvaC7LuM_c_Z_n8hcg2_sOU_W33dg9t15jKn8v6eEKrg9YDsLEzQizf7vrFDkURaMmNCBVidjiwzUPqKy4b3ymIIYTNVVTBQlcTEprwqF0PgukiO40nkIIhvPcIeknDVrIkGE7b4tmHBUpfJG4axkuFqDmeBYzxLSZeM0902jZ3PJIvBpp4sNqbepIV3BQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
در ادامه تمرینات آمادگی دفاعی شبکه افق ، پس از شلیک های موفق به پرچم امارات در روز گذشته ، امشب ، نتانیاهو و دونالد ترامپ بدون استفاده از گلوله ،  بصورت نمادین هدشات شدند</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16398" target="_blank">📅 00:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16397">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">برای ایران، ساعت در حال تیک‌تاک است و بهتر است سریع حرکت کنند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است! رئیس‌جمهور DJT</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16397" target="_blank">📅 20:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16396">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EF1nhHRPc2l0MoU4_PkcZbFhNjgrxUdo19gRLs_PjqafSZDyYDLYNxYLwU2HI3bEColwBq0rdG9hTXg8VzbpCr18FwORYacecQma4F59e5OwQanw-7a0N12w-pXTTapojCY5JsDRYGvPIjkJncJ9f0YLl9aHiz6MHrsm6rYdlubXeaW1AHA3lSPOnmIU2ehV2oaRCjva3Fw1np5IF434YXRJ2SqjGZx3yLp2050rbgyvQdW23d6ywrhHwT0_PXSATv4Z_9dUpHH7sGXzMM-VhjWfSJ-8Xjqi98Arg3kW7gZOCV83IwL6qAE8YzBPgssniD7EQ7SMsrgc5Kj9-sddyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یووال اشتاینیتز، رئیس شرکت دفاعی دولتی رافائل اسرائیل، اعلام کرد که اسرائیل با کمبود رهگیرهای موشکی مواجه نیست.
این اظهارات در حالی مطرح می‌شود که گزارش‌هایی درباره فشار بر ذخایر دفاع هوایی (به‌ویژه رهگیرهای Arrow) به دلیل درگیری با ایران وجود دارد. اسرائیل همواره این ادعاهای کمبود را رد کرده است.
رافائل تولیدکننده اصلی سیستم گنبد آهنین است و برخی اجزای Arrow را می‌سازد.
اشتاینیتز در یک کنفرانس گفت که گنبد آهنین حدود ۹۸-۹۹٪ موفقیت در رهگیری راکت‌های حماس و حزب‌الله داشته و از ۷ اکتبر ۲۰۲۳ تاکنون، این دو گروه حدود ۴۰٬۰۰۰ راکت به سمت اسرائیل شلیک کرده‌اند.
همچنین ایران از سال ۲۰۲۴ حدود ۱٬۵۰۰ موشک بالستیک شلیک کرده که به گفته او تنها چند ده تای آن رهگیری نشده‌اند.</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16396" target="_blank">📅 19:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16395">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وزارت اطلاعات کوبا تایید کرد که رییس سازمان CIA به این کشور سفر خواهدکرد.  به نظر می رسد اینها هم بزودی پرچم سپید را بالا ببرند.</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/16395" target="_blank">📅 19:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16394">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔘
پافشاری ترکیه برای تغییر نام «آسیای مرکزی» به «ترکستان»در کتب درسی
یوسف تکین، وزیر آموزش ملی ترکیه، در مراسم «رمضان در قلب آموزش» در استانبول، از تغییرات در برنامه درسی مدارس به عنوان بخشی از «الگوی آموزشی قرن ترکیه» خبر داد. به نقل از رسانه‌های ترکیه، طبق این برنامه درسی به‌روز شده، اصطلاح «آسیای مرکزی» با «ترکستان» جایگزین خواهد شد.
🔹
همچنین این مقام توضیح داد که مفهوم «آسیای مرکزی» محصول اوضاع سیاسی پس از جنگ جهانی دوم است، در حالی که «ترکستان» (ترکستان) با ادبیات علمی مطابقت دارد.
🔹
این تغییرات بخشی از مدل آموزشی جدید وزارت آموزش ملی ترکیه است. جایگزینی برنامه‌ریزی‌شده اصطلاح «آسیای مرکزی» با «ترکستان» در برنامه‌های درسی تاریخ مدارس در اکتبر ۲۰۲۴ اعلام شد.
آمو | مطالعات تخصصی آسیای مرکزی</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16394" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16393">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/16393" target="_blank">📅 15:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16392">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1pjfgT4tnoICWpukWhQLZceUkqHE6Ic7ozpoVkX_rcXuhSWGoyIHtzp_-OTpPeZnKSLae-cffFACjO6IClGq-TrIOr0xvQ7U-VhPJxA33r7nvsxHkEbhUtC7BjEU2efbJrx8FUwUfdRWLZGR5RW6vC6Bp54nvcLMmFqSbT7YE7BXFh6zFx05uHf-PlF7UPpbaPecYyvxFcsqphREvitE-aOf4f3W6Y0muxXCkHQuDlzJQDiTNmZ6uFLBx2MaDZqpKc-ZmLYgPTOQKRN2iQRAVDuHqtw00RJKUvIu6hYopIR5BADxKwAUSFB3I2H1xF-hxg6t3I_vKkZhwQWnPvbQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان بدون اینکه خنده اش بگیرد روز جهانی «ارتباطات» را تبریک گفت!</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/16392" target="_blank">📅 15:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16391">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✈️
پاول دوروف ، مالک تلگرام: دبی دوباره شلوغ و پر از ترافیک شده است. از همین حالا دلم برای آتش‌بازی‌های ایران تنگ شده؛ آن‌ها کمک کردند تا شهر از افراد زودباور (وحشت‌زده) خالی شود .   پدافند هوایی امارات زیر آتش (حملات) عالی عمل کرد. ما با پرداخت ۰٪ مالیات،…</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16391" target="_blank">📅 15:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16390">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQ85bKL68yocCGZrqyAWgLB8_eL-RJ6xbmLt3x31IZ2QSSds-LT7sd7efkJF8xdAgSvlXk3zF0xt9C23EcaLDOWclmnLdTxLBs20nt4fMND0VJVhSrsmeEm4o3du99xNcqIjOKlFfl8ZSP_Ml5RdJn8pj5XDfaOYQ4E5DJb-eIFMnWLAx0t9nToyEoXtbY2rGJauG0WIxXusoNNlVOw1FlqW-FLp67RYCaH6fual-uDqhLnyBvuWsMTzohUHnEMlgHymhZ0ZUOpNw7HMhLFeF5nwpsGM3AQdNNX24sjKxgYBW2c42m46siPJJuXiCxrWKUdMF1YfO0jj12TUEE0oEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔑
حضرتی، رئیس‌شورای اطلاع‌ رسانی دولت
:
حرف‌های پزشکیان در مورد اینترنت «وعده» نبوده، شائبه وعده بوده</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/16390" target="_blank">📅 14:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16389">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teO0crtN5c4XR-IQrB38bsQPHW07yMGldALDjSMuT41XTe8qGJOcU0h7ts5YQ20D9UMMTol3ORilbYO8t1uQkCISWujOhiC7OCeNya71AxPVBJwBSWxRe5vDj3qCFoD_Vcsn0VNK8BF2Jei7ZUX0vKq50Mh7p6KnPvb0dXaXHXh-CdjOIgGLdU0V9Oali_ZRzRmWKHbY6OU4Qir7EIqYR6yLstP_Tfsgonv2cxCFAyPLU3gjjFi5UWOLAT5uz__fgYlWBVJKlSYNHojZxLI8Q5VhS8QBnBc_vWW5X0M-RQ1OvsKcgV3KzdrVc6UFQ7a9KprJ4N1TlXGx0v4jpkyNKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#EURNZD
-- H4
کانال نزولی در حال شکسته شدن است و انتظار رشد مناسب داریم.
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/16389" target="_blank">📅 13:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16388">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
رسول جلیلی ؛ عضو حقیقی شورای عالی فضای مجازی: اینستاگرام مثل F35، F22 و A10 آمریکا است، مثل آن اژدری است که به ناو دنا شلیک شد</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SBoxxx/16388" target="_blank">📅 13:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16387">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🟣
خبرگزاری CNN :
کابل های اینترنتی تنگه هرمز ، توجه ایران را به خود جلب کرده است</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16387" target="_blank">📅 12:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16385">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
رسول جلیلی ؛ عضو حقیقی شورای عالی فضای مجازی
:
اینستاگرام مثل F35، F22 و A10 آمریکا است، مثل آن اژدری است که به ناو دنا شلیک شد</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16385" target="_blank">📅 10:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16384">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/16384" target="_blank">📅 10:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16382">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQAEwtQO9OWa75JvOCDQwz7GYPZ8BtNZBi4apXK90hz3ZtIbGJh-SpPf_bthv-tWI_1XVfYCBCXnfXZFJGG_fWpMTrVBWefGDmtdFIfSGLTomyR_DyY5bElcXaNEiOW6SNgGjpOLVqSW5Lt1k0suN-DohoShWglE91YDc392kS8GKVnqEAfmLaiCZXFIpfMx2nhhQjml_kWbDkaLD6aQTqy2LpfdgKeC7emgbv8YIwg5uVhRpIAdHq9d-PoUsA_VJWeaGE3Pmm9Bo4U5JbFQ2gXqeCJ80fgUl9CXxlzQZLtGkOfw-9O7mhkQsIeczZnuTRM7dIrfsg0LGJtKr6V-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bdVhKZqlvwhCvdSzW44D1kfH0hsP-koNH2kxL4HmBK6X8RCkwDP2hKEzwQ0RxVpDG2S3HrlIlPAVNi-TJlcYSzLrvnkWLCm4pY5KkMU6e_fK0hg87q2vZc910rb8xeYMEkOOUvamgP5qUmH-YXrTBQa2e6DZRX80rr2S8FlBru6sUz-N0quq9_qpWiRZuiaulwS8w1nmsGSQJhGMChKgh9PVmP5vzNhIN4vXblKNueF9kGIczQU6I15oxBU6PlfkODd7ryjohS5-g-_gPpwZDiMX0BRGFUuaiQju0RESD5xvFYemPXhDfxlAnAckSysbYXo7EMA3_VVJIbsrNIS_Gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیروهای نظامی جمهوری اسلامی اواخر سال ۲۰۲۵ قراردادی برای خرید ۵۰۰ دستگاه پرتابگر موشکهای دوش پرتاب زمین به هوای  Verba (تصویر پایین) به همراه ۲۵۰۰ موشک مربوطه امضا کرده بودند که بخشی تحویل شد و بخشی در جریان حملات اسراییل به تاسیسات نیروی دریایی در انزلی از میان رفت.
همچنین سامانه مشابه میثاق ساخت داخل نیز در اختیار نیروهای مسلح ایران است.(تصویر بالا)</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/16382" target="_blank">📅 09:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16381">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">موج ۵ نبرد ایران و آمریکا همراه با هلی برن گسترده با حمایت هوایی سنگین خواهدبود و تسلیح یگانهای ویژه نظامی در ایران به تفنگ‌های دورزن و موشکهای پدافندی دوش پرتاب و نیز موج آموزش عمومی کار با اسلحه در صداوسیما و مساجد و … در راستای مقابله با این تهاجم است.</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/16381" target="_blank">📅 09:16 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16380">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUJhqtovK0eNvvXvYCzogVITFhB5c3N8nBjRyIhLkslyn_oNfHRcQ4O4PSlHlSlEGSw-60doWWIlfs30ghi8GFQeWbZQT0-pmlWD6bhl9H67zxK6ZL0Aqv9ccEn-wGvX3CVfGSUyuigVuTMmwg1EEoP5B8SmJmedA0boYaS5okTPUgdm0PeFSYH7QnrxOFspko4f_qpuClfcebUjEcN0p-UA4cBVTGsG32hfnoB4mB2zpbhv3wJTX3UXzFf654E4LTLWsYG4cGmueFlH7vt21L620InJGlLKvXe4OqFe8J39YmbiFUfp9HZuSSxNTbHGmYTFQZej5xtHEqcnh-3PfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج ۵ نبرد ایران و آمریکا همراه با هلی برن گسترده با حمایت هوایی سنگین خواهدبود و تسلیح یگانهای ویژه نظامی در ایران به تفنگ‌های دورزن و موشکهای پدافندی دوش پرتاب و نیز موج آموزش عمومی کار با اسلحه در صداوسیما و مساجد و … در راستای مقابله با این تهاجم است.</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16380" target="_blank">📅 09:14 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

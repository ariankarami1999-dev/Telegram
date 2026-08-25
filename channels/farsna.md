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
<img src="https://cdn4.telesco.pe/file/rfcOYpT6ocouIqyLw6dJISK-CDpc95h4xNbsAbm02uvxJIrSQ5L96sfovvKmt7EE91Y5rcur-DI7mUZAgzFk0DQWexgZzjwPhjbna3q4iB8lxqxuJueyCqLZ4STakKDGVF7lTosBREhw9cdgWX2C11G3A7HQ5s_sNjrsyP-revk8oomfhygAvsLWeofWutzdhaJP94_69c94irFtkmcTxznMmEd3FWJ1XmkoAWwj1d5JNB_R1lCl_l_EUI4M0VE7mey_SLSxYIy0RqHYS2O2Ng_pK3CHTTmIc2AM7XauQSuXs4qNf9ABygxP0gvX1mlDi13Z6F8Q_SoNSRGbWhEjMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 18:41:38</div>
<hr>

<div class="tg-post" id="msg-458195">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXBqrdPEtgbEML7wHLDx5QAznpimO0jTdoYSc2NL3DRwfmpMlF085rMVy1jZD8ZQ9ZZv0pE-Mph1yAG09altSevsC8mHJlzNC9NJ3owNDYYxnfkDygWozJfThcnuhzH6Dj5oc32OqdATVwrpD-dQSrMy29zQjPujAaBW46uZF87JdBNpFMJEt0EJmrBTOm1Ml4Uy0KChlHuH8NnPeI5alwTG7Uq2YONvK9p8KzELRzzB04vlvm3bioaVTrngKGzdsEHKSzdFnBFheevZdqhMdT9KaKBp8Gjl0BeGh6JDRbmCDuMDMPuDr92KjE6IROOCQOabFS1wkBzbqNTPAoP92A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IsykC9lRVkeSamvbKer2vWmmZH9pZOgfJkm3WPTWaCt2Yy3BB1B2DPp1b7bfHGE0CzNmKQZiCUa_FdJYvZf7bDa9UVQVjRzfzGW4lFaGKUJzdbAEvJzZ2-c3Uny7tfYniPjv0vmu4SOYsjnjhkvhaCtwXw_FpW51IpejtY3EyvgCq1u6T2T5zkMYaSQBfSS3rKqTeF-6DNdqLSB2V81X4q7n4-p2DXAeVm1AtIoIH6a6yXm1uwnOzmOUdzuNnrzdf5m0h22U5zOupb15rsvoXmcXKQn_ceXwJ77lwNtsr1BsaPYUvAFzr4_ZtoWjuS0IGFZ8DHWQGkKLlndJuqAYhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ، حریف بازار ارز تجاری نشد
🔹
طبق گفتهٔ رئیس کل بانک مرکزی در حال حاضر روزانه ۱۰۰ تا ۱۵۰ میلیون دلار ارز در مرکز مبادله تامین می‌شود.
🔹
بررسی آمارهای مردادماه سال گذشته نشان می‌دهد که این اعداد نه تنها در رنج ارقام سال گذشته، حتی بیشتر از آن است.
🔹
این در حالی است که امسال کشور هم درگیر جنگ و هم محاصره و محدودیت در تجارت از طریق بنادر جنوبی کشور بود.
🔹
رئیس بانک مرکزی می‌گوید تاکنون ۱۶ میلیارد دلار ارز تامین کرده‌ایم که ۹ میلیارد دلار آن مربوط به صنعت بوده است. این رقم مشابه میزان سال گذشته است.
🔹
ارز تامین شده در بازار ارز تجاری صرف واردات مواد اولیه تولید می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/farsna/458195" target="_blank">📅 18:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458194">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‌  عارف: جایگاه نخست ایران در فناوری‌های پیشرفته در منطقه را مدیون رهبر شهید هستیم
🔹
کشوری با شرایط ایران در حوزه‌هایی مانند فناوری نانو، بسیار سریع‌تر از پیش‌بینی‌ها حرکت کرد؛ به‌گونه‌ای که از ابتدا قرار بود در جمع ۱۵ کشور برتر این حوزه قرار بگیریم اما ایران…</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/farsna/458194" target="_blank">📅 18:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458193">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مسیر شمال به جنوب کندوان مسدود شد
🔹
رئیس پلیس راه مازندران با اشاره به انسداد مسیر شمال به جنوب مرزن‌آباد، گفت: حدود ساعت ۲۰ محدودیت یک‌طرفه کامل از مسیر جنوب به سمت شمال اجرا خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/farsna/458193" target="_blank">📅 18:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458192">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عارف: پیش از جنگ برای اقتصاد کشور برنامه‌ریزی کرده بودیم
🔹
معاون اول رئیس‌جمهور با اشاره به آمادگی دولت برای شرایط جنگی گفت: برنامه اقتصاد جنگ در آذرماه ۱۴۰۳ به تصویب رسیده بود و دولت بلافاصله پس از آغاز جنگ از این برنامه استفاده کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/farsna/458192" target="_blank">📅 18:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458191">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elRSz4tZs2MGn7ddiS1T1wI0iKcKrFH0mQPOk9b0iwqM4CS7o4JikevwOqBlbmvezmf9Rku4sE54ZAGW-CKTlmao1B8UDt3IRMvFfRGNChXRVdp_9L5a_QED0JzSXD_JGzqlNvsLM55SFJ2dOgbRs9kWnRKTq8pUFNJzs2ZTzpv8QM0wngc60BT8SpWk9W_QWzcs_ieD5XsTd8BRgAy8hvDnKzpMQz24SCF34S-zDMX9z9a4sDD4Dnm7pkQdyH56D1CUi4XC2dyQUDSKoFnq5cKcwzxCrNlww_SvmJooLUjYbMfmXjFlIphR5k6T5JK1TPi9sIfvRBYn3mPbETLUCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: پیش از جنگ برای اقتصاد کشور برنامه‌ریزی کرده بودیم
🔹
معاون اول رئیس‌جمهور با اشاره به آمادگی دولت برای شرایط جنگی گفت: برنامه اقتصاد جنگ در آذرماه ۱۴۰۳ به تصویب رسیده بود و دولت بلافاصله پس از آغاز جنگ از این برنامه استفاده کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/farsna/458191" target="_blank">📅 18:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458190">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87fe6b2685.mp4?token=A3snor0GNKoIMpcXW25IpRqRlR_43g8AQcntRTGmptfEs_Fv0gDYeWKcG9pFHnWHpi8rhoGSu2gCky_fNxjERd4qWnP47uYfz1Y6zSyRpDYcb_58hfegcSJ90wq9r-OXxfTU_icU2qG2qBM8omZuutcsJfanJR8Wmt7VuSp6p6cwG4OZkLmgiJhhvF3nL77t7geuyJsAoINWJkIZYOBr86ho3S4RH2PN2_aDvqfqWBm542CPEeT0RE7dclcKZ-os7Ey_2zT8JkP60vhLdmyPMwKB9oT2y6ZiyRHUOTH9yHMT1red9TfRJilC6dW0ks5itHd2ZsYDWbBmmgqbVrmQTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87fe6b2685.mp4?token=A3snor0GNKoIMpcXW25IpRqRlR_43g8AQcntRTGmptfEs_Fv0gDYeWKcG9pFHnWHpi8rhoGSu2gCky_fNxjERd4qWnP47uYfz1Y6zSyRpDYcb_58hfegcSJ90wq9r-OXxfTU_icU2qG2qBM8omZuutcsJfanJR8Wmt7VuSp6p6cwG4OZkLmgiJhhvF3nL77t7geuyJsAoINWJkIZYOBr86ho3S4RH2PN2_aDvqfqWBm542CPEeT0RE7dclcKZ-os7Ey_2zT8JkP60vhLdmyPMwKB9oT2y6ZiyRHUOTH9yHMT1red9TfRJilC6dW0ks5itHd2ZsYDWbBmmgqbVrmQTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رد شدن موشک از بالای سر نیروهای برق‌رسان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/farsna/458190" target="_blank">📅 17:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458189">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پزشکیان: دشمنان روی نارضایتی‌های اقتصادی هدف‌گذاری کردند تا ایران را به آشوب بکشانند
🔹
دشمنان متوجه شده‌اند که از راه نظامی نمی‌توانند ملت ایران را تسیلم کنند یا شکست دهند، از همین رو بر روی ایجاد مسائل اجتماعی و نارضایتی‌های اقتصادی هدف‌گذاری کردند، تا از…</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/farsna/458189" target="_blank">📅 17:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458184">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lva9H8FMBJlDpvu9qC15k8zskqthZYBMd5T7YG4-UDhf3Tm0Pd-Ma_5OR65wM1-edLIoMo1mpdF6ToU1W1Zh64BHdAfamz8q7fo_LrWbg3Fo5biZ_sUPUPTZhrf9tVO4_8NIadpp9_sHkqlsXgtQy6k8I3f3acPnL0yWvFg8c7ymAMVTs1h1HxqeB7F9Kbakg8L5QET3nz7RwBZ3HMq7Fzx9eXsEqfVZK-3t39hvZuSAc49TJZyVcYbxyh0ZT85LdDP3d9hO2DcOy_ffGGDJeMRfnUrhcsstM9WH3ir-NBC6I-puvZODlZK-Mz6NEdOfpwBaWy1B7pqDex4da-xVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fEYWr9v2FU7GbSqPLPVjGZbVaDIQtO-J5FKZ3tTwER8fb3P4aoBzvRbfxp7uPApcVh-8OF9Luee3BFNrniT1-gNife-9dwVlBL5fjqZDUqSJQrg-FrAWeQ_sW5wG8NnaYmb_-bEig5mPBkdflr0dtkqgzNKD-oQ9N4pP_v6Z-EqeQrycZ05KjtX_wZMVJ9_Rlak8uuglXmF6QK7-Eda-70I-K0JFHK8NTQghpuUFJuYzRE3G53xvlnYIMuHkJpoAD49NGN8E3UP0qbJCIIhqWKjF2CaZoMkHOtOD4OkhOiDvC0qbCyvktYOJQbo71Gd8UERNq0_DCplzT1Vmh63OQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Grc0qDFXD75Csg91-dMdYwAOJTLMcadt-QiYINMKLSYSTG86-ntAZPiDVcmqC_6rr9bf7Zz_tCYRfWPPsVxs1z2AbXSOhzi_YWNkRtnl3eQbgrwsnYQDfHBOJEMhemhGcPkIR8nW5H9-0HGiPgUhtIxwaeZxF0Da5y2fbplaAgAarGlwlMIdNdKqyRstATUUS1ck63bqbl0LrQtcoTiaHkB5__-mUbFVqCATwD_ztfBuVxST3SR_jPw9p3kgOT34NLZXdOVv_UiZoPW8JRDxklMmCoiIlkyQc9pB5F_p0Qhfvusynt3FMo4rE8PEgQBSBn7xtMq7Km2Tehn1twS4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MgQqNLkRevXiFnaKtEqtl2X2521w-FM1NnFmYzc4fDEu5L92Ys-D4fTiTLW8gUXTzl7ZF7_CDMI5LIHqdp5iyxZ-LAZjz7nzNiK4QfvvLv3uyehj01kuHxjTi8_h9s_1mB23RSFxK8BjYJW7C_qVu0OyNmQHet0JPQLwn0P6DMwFkOJ6UbWV-S-Qv5v6oHHrWPJ24owUyqpEaq8vA7-aDfr32VmnzKBIEXlEOyhO-Vi-6WfnZZiKTkba2Z96IIYVY4mn84-ziKsSnd4iDxl1AnP4xfqhLLCdH--2CmxDmi1BNl_M7DvQpwvM5J9KOMh7QH4_EQzR6W-TnTpOWLPBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3bGtz_bsPibc30AZrHO7B6UgGplbkKdIssS2hwrlbivDB1m9jwrumqJEuczN2PWEGHS-rdARGw-Df_aMOkmmmEWU5XvWdOOzht0e-fdtnd3ffFkgiQUZ3S3SuBNS_uf5pIF2q_nZmPKC7gLxBYwgcFxNPHt_W9QKo9zDvP0pdLlvPoFZe2ngZnjSbLw7Haq96MgVA2coM-4_HCH0S1wF6_F3fXfdd8W76O15XFYGpCVTW8HGswbJOaQ9Oam9GvmXYrAKwmxtB7JbGWPp3ZwBj6WCnhqLOSyXU_UCK6BbjBqN0hBMysZmfqhq47N7kGfdRL5-J0CFRnmoarQ9_s-aA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور رئیس سازمان بسیج در دورۀ معرفتی تشکیلاتی «آرمان»
@Farsna</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/farsna/458184" target="_blank">📅 17:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458183">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrnaG0Dg4FcoV2WEjMQVcSTl2x-wIbef2GB9BtFXm9gOlOY9C_rcnuXUHDltuVQ4LQKZ_RzztBXsVAI3nv9ZRTt76u4xXCp44DQnk1l37IHML48qUsO9-CkwIVFEG0JCHOEw8A0iqT98VihFGWjbUPgVCPeobVkePz-XD-2FTOn5BrvT_8psWBdGLNdVVrNpUZTz1hWakCPB4emtWbPNZJAHMKFJfTR-uS1Ozji-YrjhjoE_VTNoTPZeQle3XZO7G5SGvm0qXNxGbEHfdHgPtZWFdEtBunTakE4nJcG7zGBi2H11qhiGROQY9SkGbKEG7TDHD1IkNZgb6zk1SPXQDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: دشمنان روی نارضایتی‌های اقتصادی هدف‌گذاری کردند تا ایران را به آشوب بکشانند
🔹
دشمنان متوجه شده‌اند که از راه نظامی نمی‌توانند ملت ایران را تسیلم کنند یا شکست دهند، از همین رو بر روی ایجاد مسائل اجتماعی و نارضایتی‌های اقتصادی هدف‌گذاری کردند، تا از این طریق ایران را به آشوب بکشانند.
🔹
ایجاد فشار اقتصادی یکی از راهبردهای آمریکا و دشمنان برای این است که تسلیم شویم، اما آیا باید در برابر مشکلات کوتاه بیاییم و تسلیم شویم؟ قطعاً خیر.
🔹
تمام تلاش من و مسئولان نظام این است که وحدت و انسجام را حفظ کنیم. هر یک از ما راه را پیدا خواهیم کرد و با مشارکت تمام آحاد جامعه، منطقه و کشورمان را آباد خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/farsna/458183" target="_blank">📅 17:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458182">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3077fb76f3.mp4?token=H1UYjsA2tz3CGI3HuV3PgrlgVT4zfT3Ua00WDnKiuv_BBrGEcAOiEEUGsgWhha6_3jQD3AlEhtSzV84X1B4sye-RhbRve2eOxWTGExq9RVxls9e9W-64jVBNp2TojSPAGyBgqs422TVlZdFstCAWaA3s7BbfBgLPIG9OUXV3sdH8RIaVhpo_TZORjObTZjwJAZKfsqryTEJ_4oLGMRg2Q49lHqC5ptmjXVbmJtQC4HuMJkT73QYeKx5DiGICy8fMnyqQmS0fCYxWzVbqsO3v0V1iYpS-0nH7dYV-70qLE0WJz8CO2xjd2Dk6osIqMs1wIvunEx9fAETzkiDsQ3o5MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3077fb76f3.mp4?token=H1UYjsA2tz3CGI3HuV3PgrlgVT4zfT3Ua00WDnKiuv_BBrGEcAOiEEUGsgWhha6_3jQD3AlEhtSzV84X1B4sye-RhbRve2eOxWTGExq9RVxls9e9W-64jVBNp2TojSPAGyBgqs422TVlZdFstCAWaA3s7BbfBgLPIG9OUXV3sdH8RIaVhpo_TZORjObTZjwJAZKfsqryTEJ_4oLGMRg2Q49lHqC5ptmjXVbmJtQC4HuMJkT73QYeKx5DiGICy8fMnyqQmS0fCYxWzVbqsO3v0V1iYpS-0nH7dYV-70qLE0WJz8CO2xjd2Dk6osIqMs1wIvunEx9fAETzkiDsQ3o5MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادامۀ حملات رژیم صهیونیستی به جنوب لبنان
🔹
توپخانۀ اشغالگران، ارتفاعات علی‌الطاهر را برای چندمین بار در روزهای اخیر گلوله‌باران کرد.
🔹
همچنین شهرک المنصوری، حومۀ شهرک‌های میفدون و صربین، و منطقۀ دوحه كفررمان نیز هدف حملات توپخانه‌ای اسرائیل قرار گرفت.  @Farsna…</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/458182" target="_blank">📅 17:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458181">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ddeff49d8.mp4?token=uLat67h6oveR0c1bd54AHcuQipguGX1IvlR_3E_skUoRKOlvUV_EUWsiqZDxeqtTKv3NSVlRSeMyRVlC9ZPLt_MiL_efuuU4mSUub6VE-XydsFyAKhTrRv06anR7ImPzOEGiXSPJWbeouqC3CDSM-z4LVqztCzYt8V8o9K-GsfsUAxp_AYSOXYjB8lZD2BNmm-fsl6EdUsghYbOY4zlpxaMoN7Uz8YJi2iO7muvcPGRFTXH0MLEVSLAUxs6qkNxxKUqKhWLRtWWnEjNkjQUDdTCSNPLXeY--MYlkDtMHnCRu-lEWS5LOjqXGMOSWkmlm1cOD68RV1wmUsqzRf7LQmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ddeff49d8.mp4?token=uLat67h6oveR0c1bd54AHcuQipguGX1IvlR_3E_skUoRKOlvUV_EUWsiqZDxeqtTKv3NSVlRSeMyRVlC9ZPLt_MiL_efuuU4mSUub6VE-XydsFyAKhTrRv06anR7ImPzOEGiXSPJWbeouqC3CDSM-z4LVqztCzYt8V8o9K-GsfsUAxp_AYSOXYjB8lZD2BNmm-fsl6EdUsghYbOY4zlpxaMoN7Uz8YJi2iO7muvcPGRFTXH0MLEVSLAUxs6qkNxxKUqKhWLRtWWnEjNkjQUDdTCSNPLXeY--MYlkDtMHnCRu-lEWS5LOjqXGMOSWkmlm1cOD68RV1wmUsqzRf7LQmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«دی دِی» ترامپ «دی‌فیک» شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/458181" target="_blank">📅 17:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458180">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fnz8ZNb2-gEbiIREMrZrIQM7WW3DnSdDsViamgcmiaWjD76SX4aDHGC9DfjWbZqTWCw9jlG0Eq1Rm3SwUY0AfV5OBraG427iUulPGEO7KxRZqnPrhFL_IArizBRPRRZqr46WKwXmdu-3lXH1YBSspicWAi9eTaOsZFIiUVFfdeQNq-_yIwWH1WXFUA8Q9ZY-Io0FfM1IT0s8IHguBODHJtQzmyWSPgWJZ5yv9vb7tylyq9s9ogssKfsRgFoWmn9Ptmy2wtTmHbxeFIk_3Orn0a63PCyRJQAtDc5Yc9X4Ia-vqVfC8x_FMUnJi4MGulIJi1sDgSYpCOFBRxFO-FKBkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار چین به آمریکا به‌خاطر تحریم ایران: تلافی می‌کنیم
🔹
نشریه انگلیسی فایننشال تایمز: چین به آمریکا هشدار داد که ممکن است به دلیل تحریم‌های ایران تلافی کند.
🔹
پکن به آمریکا هشدار داده  اگر واشنگتن سرکوب تجارت با تهران را گسترش دهد، تمام اقدامات لازم را انجام خواهد داد؛ همچنین اگر شرکت‌های چینی در هرگونه گسترش قابل‌توجه تحریم‌های ثانویه جدید ترامپ در رابطه با ایران گنجانده شوند، تلافی خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/458180" target="_blank">📅 17:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458179">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌
🔴
رهبر انصارالله یمن: عربستان فرودگاه‌های ما را بر روی مردم‌مان بسته اما فضای مکه و مدینه را برروی صهیونیست‌ها باز کرده است. @Farsns</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/458179" target="_blank">📅 17:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458178">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌ رهبر انصارالله: از هیچ تلاشی برای پشتیبانی از مردم فلسطین و مبارزانش دریغ نمی‌کنیم تا وعدهٔ حتمی الهی برای نابودی رژیم صهیونیستی محقق شود
🔹
تأکید می‌کنیم که در کنار مردم مسلمان ایران هستیم و به تقویت اصل «همگرایی جبهه‌ها» و همکاری میان محور مقاومت ادامه…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/458178" target="_blank">📅 17:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458177">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رهبر انصارالله یمن: تمام امت اسلامی در خطر است؛ چراکه صهیونیسم زیاده‌خواهی می‌کند و دنبال «تغییر خاورمیانه» و تشکیل «اسرائیل بزرگ» است
🔹
پیروزی بزرگ ایران نتیجه استقامت در برابر تجاوزات آمریکایی اسرائیلی است. @Farsna</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/458177" target="_blank">📅 16:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458176">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRUZzUjcnGCX6Vmxmdz_2nNev9mxLiS_rwViM7zuoOIZavGv2-Dbouj6RFYJSU-Mkc5efONVnlln3K1UIfPt4QsBS14HVxroPHIo3Hho2mv6S1pgcuWwcj01ETY-m2klEUB0DHnWOOxbOWXLOSEkd4O5eXp_OopDAKfY7S9BNOjZDZNX0hlWTPUsS4CFiby9-pLI4K0dJLzx4sd4oQuXQRjjpjFyRs9mPt66Klf99DAPGoU7smYXu-hONMcq40AncPznEjQKX0Ig5TqF2PtGS66IyXGNHaFpQrfIPyW3okC2RurpJ2a2hGEHdmCQna1qpAYEkL4AcbqqAQg5M87h2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انصارالله یمن: تمام امت اسلامی در خطر است؛ چراکه صهیونیسم زیاده‌خواهی می‌کند و دنبال «تغییر خاورمیانه» و تشکیل «اسرائیل بزرگ» است
🔹
پیروزی بزرگ ایران نتیجه استقامت در برابر تجاوزات آمریکایی اسرائیلی است.
@Farsna</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/458176" target="_blank">📅 16:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458175">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48cf1095b3.mp4?token=Q1NpNURJldKOjVS6TJ203c-xk7foRFuNfIpHCXm6UbyacuJlB6kltOjMwkxog485T92LGbNV8zPZ1jfz99R4CVOoMcvmsXJwl414z1Of0b8_Z8wGotzd1FU3p2PkcOVdGZ18uaD8A6EdfYlFf80nIYl2yWwJHHmmXqxfg3ZLX96l66gdQOsCfVT5WoSjyBZ5FoRc3KDAhVf81De4wolv3gYzEScNDuWM_jd68y9nTDJkexEDw3Pbn1osLhqPIpaP_KeO96eYZlZiC569ZqS23a9-VksAI2cl9260NlKqH-lza38vnPgRdOE9nY_860UGQJBs7fDLAfTDs1eJxcFCooi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48cf1095b3.mp4?token=Q1NpNURJldKOjVS6TJ203c-xk7foRFuNfIpHCXm6UbyacuJlB6kltOjMwkxog485T92LGbNV8zPZ1jfz99R4CVOoMcvmsXJwl414z1Of0b8_Z8wGotzd1FU3p2PkcOVdGZ18uaD8A6EdfYlFf80nIYl2yWwJHHmmXqxfg3ZLX96l66gdQOsCfVT5WoSjyBZ5FoRc3KDAhVf81De4wolv3gYzEScNDuWM_jd68y9nTDJkexEDw3Pbn1osLhqPIpaP_KeO96eYZlZiC569ZqS23a9-VksAI2cl9260NlKqH-lza38vnPgRdOE9nY_860UGQJBs7fDLAfTDs1eJxcFCooi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش عجیب رضاخان بعد از شنیدن خبر اشغال ایران توسط متفقین
🔹
روایت مهم و دست‌اول وزیر دارایی و  نمایندگان مجلس در دوره رضاخان راجع به یکی از حساس‌ترین دوره‌های تاریخ معاصر ایران
@Fars_plus</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/458175" target="_blank">📅 16:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458174">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/icu46_V5JG9h76HM3XYbpbetTmYDunTN6thPd8skz5KH--yeyzWcV-VWb2zndVjs2oKKIy6gL91zFZQ8XNC4pKwagfu5DLEStRF0Q7HZsq8viKlOLZDD_LYc-aGd1R51m47qGCpNVPA-P2kClZuZbtR81jNRODRpD1UPFMw4Y5bXANH6Egn2WnIlW0_180oFNa9ACWWrkSIE_sgYhB0vaG0kcIHgwdXk1RvvtFTnKPZDJQo3H36zdnp68K9w1j0UqeTbp5N6pd121KZHEF8iTG5vyAkVaS5AOg7mltxc5aNQLq5IPJHL2zwVauP8uuJXdQPdYbCDq9Mn5MDtrQ9Vsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چادرملو کرسی‌نشین ارشد بورس کالا
🔹
شرکت معدنی و صنعتی چادرملو در صدر جدول عرضه کنندگان شمش فولاد بورس کالا قرار گرفت.
🔹
به گزارش روابط‌عمومی چادرملو،  نتایج معاملات بورس کالا نشان می‌دهد کچاد باعرضه ۲۰ هزار تن شمش، بیشترین حجم عرضه شمش در معاملات ۲ شهریور را به خود اختصاص داده است.
🔹
در معاملات ۲ شهریور بورس کالا، میانگین موزون قیمت شمش به ۶۴ هزار و ۶۱۴ تومان به‌ازای هر کیلو رسید که نسبت به میانگین قیمت معاملاتی هفته گذشته، معادل ۳.۳ درصد افزایش داشته است.
🔹
میانگین قیمت معاملاتی شمش در هفته گذشته ۶۲ هزار و ۵۷۵ تومان به ثبت رسیده بود.
🔹
یادآور می‌شود؛ در معاملات روز گذشته در مجموع ۶۱ هزار و ۲۲۵ تن شمش در بورس کالا عرضه شد که با احتساب معاملات مچینگ، ۱۰۰ درصد عرضه مورد معامله قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/458174" target="_blank">📅 16:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458173">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyGkoAbmFrjhyPERMlzXNbRp-2asmR57y7O6FhuP6IcuX5L-ZFN-FGRnlfq88BGYfUkns-E1sbWrmvVJAlXURays9qAKEiHvjY-fORYUynbrnBhoDm_HElPmU8bm1mRi4UmFwOsOEoksMX8kehxtbwqooe5h99LcatrmlyLxtqs2zA967TrpsCDycoc0MIVAWI6GjE7DNELakbYMdu8jUAfkAR_IT4bcM6aEF-k_fdWc2br91wYBgwGpZFkGy-O8Hrtf_UeyYfWWjz8jjbxaypwL6dQ3w6RgxgXUAA4Vu5L1kL-bYSlSFchOdHDgkM3TZV71fJqsP8q1vd3-hv-wCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
یکشنبه‌ها در پارک آبی اُپارک، بازی‌های گروهی منتظر شماست!
در سانس بانوان، در کنار آب‌بازی و تفریحات اُپارک، در بازی‌های گروهی شرکت کنید، با دوستانتان رقابت کنید و شانس برنده شدن هدیه‌های ویژه را داشته باشید.
🎁
🏆
🎟
برای خرید بلیت به سایت اُپارک مراجعه کنید</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/farsna/458173" target="_blank">📅 16:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458172">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/458172" target="_blank">📅 16:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458171">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTv9eDuBbEWPfYO86b3Y95mbmaSrNn6yzyTQs3frMmmFsG0Bczc-BDU-0Nq2BrH8fND_7NPLKF8NRAvYcysBDSA-xyPp92HnAFEnjlhCeTUo-XKWTOtSVAZ-uhtMctJeFHHpm8HuAq0DtdPfp8Y0hyrkOeV0lkPZAIlmUAa8vI_MIPTjNcz9zU10fy2SK4vBo0jDXvwiorTtYuzYiTk5L1yz_JT4XS1XuDiukkBQJxeTModbkT9V4e6be9bAhtP3WthLr9kJ4brZpMt0eWD6KQgBBs6s0UkvdocNG03kOm5rG52Zdq-V55IS8qZPPMz7AoCcKhPl40q19xRuC1cS7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس مبارزه با مواد مخدر داراب به‌شهادت رسید
🔹
پلیس مبارزه با مواد مخدر داراب فارس: سرتیپ دوم حسین حکیمی در درگیری با قاچاقچیان مواد مخدر به‌شهادت رسید.
🔹
در این عملیات ۲ نفر از قاچاقچیان مجروح و یک نفر دستگیر شد؛ همچنین ۱۳۳ کیلوگرم تریاک و ۲ سلاح کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/458171" target="_blank">📅 16:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458170">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/567b7b39b6.mp4?token=rmhNe-kfjebYrsVx5Qh4Vk7vJPX6a24G1GTSCxp89eiF4Zg47LwIhi5aZ16P4JADkrMzTyQ7oQqkssDNqPjA0Dc4o3Lbx3fSn4oVNlcYTy_b-ebv3KO3nX1J6-Xwd6JyfMzBqRIHcArsrAx_0wvyl4_DQvmovPGjizBXFtruHlkfj_Mjgop4X9z54Ln0Q4zqBtfisE3TRd9LHKEsS2yYq0s0M8ts_GovWbmvpothBCKfJvANGVhLdGpW6HkzqLDQ7NBgGdgUNE_J2TQQodQ5fJRnOvUSoJt_Tqu_DbzMBfgc5JIMmAJe5_V7rETb4M-MkK545EZPdcIeLdjVw2gj1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/567b7b39b6.mp4?token=rmhNe-kfjebYrsVx5Qh4Vk7vJPX6a24G1GTSCxp89eiF4Zg47LwIhi5aZ16P4JADkrMzTyQ7oQqkssDNqPjA0Dc4o3Lbx3fSn4oVNlcYTy_b-ebv3KO3nX1J6-Xwd6JyfMzBqRIHcArsrAx_0wvyl4_DQvmovPGjizBXFtruHlkfj_Mjgop4X9z54Ln0Q4zqBtfisE3TRd9LHKEsS2yYq0s0M8ts_GovWbmvpothBCKfJvANGVhLdGpW6HkzqLDQ7NBgGdgUNE_J2TQQodQ5fJRnOvUSoJt_Tqu_DbzMBfgc5JIMmAJe5_V7rETb4M-MkK545EZPdcIeLdjVw2gj1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیلاری کلینتون: نتانیاهو فردی مخرب است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/458170" target="_blank">📅 16:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458169">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N97E8W4l0SQpMO_0r5G6GGcRmnagqs4OSZmWvGJfDpd1TQp_xfotHsk3oahYfjP5c7Ict5rFRJNNrYgoXyjLsnAHn80ztoyFxSBS9UZcbBq2yMHJMuB6AnimXB_Z_xoURQqUL7Fx_iXyIkgluGBRbV3paljt7gZctEiRbjZBrbUhCnqahhPpuLgOvUvjQcwVzJnO8-uoL9OziIMxSOe8AE6UAf3ZRAaEXTnsH7gbCs1_MzT_kTlqamBgwtwVKbwL_kJ_3XrWnqIkqR6bBIFtGB-4ClIYC07BWGvOmSkYWf8T0bJ4E8vMKXRW3yomGRE9vngfPt84K6tMyqMk0FlFKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سرلشکر رضایی: همۀ جهان فهمیده‌اند ترامپ خالی‌بند است  @Farsna</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/458169" target="_blank">📅 16:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458168">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c291b758c0.mp4?token=EuImh8aOhAn5OBZTulzPc291r69vQT6b3t8JwFuFv1chS5XFQbxEDceSp7gFHXfiFy0HSxn9thgXGxSuUYgqXQljWC_lursxEeRqul43Su526E5SogkXyR-QMDdmtUnf6UUA3kIXFx1M7n6LdqUEI_0cf0PpDv1P5J5G4KvXtDYN7HS0_13kCd7OLrdkW52iBMsDee2Y2flzfDY10YKBnktfvf_gtkngTRmYcfVhgHPkKjFtuMo7wElyMLiSow8TAgGxm1jb_fLmxJ-WMed2XorakehFa09ZA152CEIfQz8--j_O83Ot0yuFmlY_t6qwbNqhTTzXfh5_1Q081PjPnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c291b758c0.mp4?token=EuImh8aOhAn5OBZTulzPc291r69vQT6b3t8JwFuFv1chS5XFQbxEDceSp7gFHXfiFy0HSxn9thgXGxSuUYgqXQljWC_lursxEeRqul43Su526E5SogkXyR-QMDdmtUnf6UUA3kIXFx1M7n6LdqUEI_0cf0PpDv1P5J5G4KvXtDYN7HS0_13kCd7OLrdkW52iBMsDee2Y2flzfDY10YKBnktfvf_gtkngTRmYcfVhgHPkKjFtuMo7wElyMLiSow8TAgGxm1jb_fLmxJ-WMed2XorakehFa09ZA152CEIfQz8--j_O83Ot0yuFmlY_t6qwbNqhTTzXfh5_1Q081PjPnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کربی: آمریکا در کارزار اقتصادی علیه ایران ائتلاف تک‌نفره است
🔹
مقام پیشین کاخ سفید و پنتاگون با تردید درباره اثربخشی کارزار اقتصادی آمریکا علیه ایران، گفت تحریم‌ها در میانه جنگ معمولاً کارایی ندارند و اجرای چنین راهبردی بدون همراهی متحدان دشوار است.
🔹
«جان کربی» در گفت‌وگویی تلویزیونی با شبکه ام‌اس‌نَو درباره وضعیت تصمیم‌گیری در کاخ سفید ترامپ نیز هشدار داد که قرار گرفتن رئیس‌جمهور در یک «حباب اطلاعاتی» و محروم شدن از دیدگاه‌های متنوع، به توانایی او برای اتخاذ تصمیم‌های بهتر آسیب می‌زند.
🔗
شرح کامل این گفت‌وگو را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/458168" target="_blank">📅 16:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458167">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4OCkcbWOq7AKwvd3S2MjdgfsdeXRPlvNHCJSuxWxMmtnPtWILHGnSjaP1aPokXsILFg9Noh4z7Lovb89Dd54zKrZTeuEUo5xVowBDLwd55oZFLQO_ZW3EAgOrKwJ5xfxTlYIOaDvjiWAOCQ6dZqLonvrefi4X-t85_b-gcxnouwTI-1DT5PtrsSi3h2e6oNMBTFdcFfPshh9jWq_rSdBxGqMhTPpIO098ZkYQpZwya-QmfubTRNejJh0lXRE1-Jfs7rR-edfnVwSLOmuc5RlWZF0C7A8B-W-Ygt8Ao2sFcz308ZvE08yQ7MU2Fn_-3Bfp5FV1V1ZqED5X94_3vy1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس‌جمهور در حکمی خداداد غریب‌پور را به‌مدت ۵ سال به‌سِمت عضو و رئیس هیئت عامل صندوق توسعۀ ملی منصوب کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/458167" target="_blank">📅 15:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458166">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfJPiZslAw5mGuaGKxHJwbEGCNa91ZL0rcpYgcWK0lccJXZWIQ22K3oxIv1g5R5DRbTDoouEAgHActM6fsdepEq9Ma9ppBp5C3jo3GRkv0yJvlD6Sp0vh88mfBibd16LAyPYtEN5IioZlQiMCqXYdwufbOGKYvukrzF35GmmDABuYW5Y1KrA84UMeA4Sx2XXnUCn5yCOhe3k56vNK-ciskN6WaQB-NQch7-fS3GEKIJWrQQsak1zJ8OwM9F4k-KdTTvZVHMscgCIjuQYA-_XIh6AqC6zF7pQQnP1DFkUhsEtlAPx1xtk5i-2ZnjZukwyCBAchqK5WJtRAcz1rsL3gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگیری ۸۴ متهم پرونده‌های کلاهبرداری کنکور
🔹
پلیس فتا: ۸۴ نفر از متخلفان و کلاهبرداران مرتبط با کنکور دستگیر شدند؛ در جریان برگزاری کنکور نیز ۲ نفر که پس از تصویربرداری قصد انتشار سوالات در فضای مجازی را داشتند بازداشت شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/458166" target="_blank">📅 15:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458165">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‌ تاریخ و محل شهرآورد مشخص شد
⚽️
دیدار رفت استقلال و پرسپولیس چهارشنبه ۱۱ شهریور از ساعت ۱۹:۳۰ در ورزشگاه نقش جهان برگزار خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/458165" target="_blank">📅 15:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458164">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">عرضهٔ ۵۰۰ میلیون دلار اسکناس به شبکهٔ بانکی
🔹
بانک مرکزی در نخستین مرحلهٔ عرضهٔ اسکناس، ۵۰۰ میلیون دلار اسکناس در اختیار بانک‌های متقاضی قرار داد.
🔹
بانک مرکزی اعلام کرده که در صورت افزایش سفارش‌های ثبت‌شده از سوی شبکهٔ بانکی، آمادگی دارد حجم عرضهٔ اسکناس…</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/458164" target="_blank">📅 15:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458157">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MLTN7tcx4zWdvppnrrI8KwF3CVnXwfHwe8SG--VfoSLMDOPklNcRmIDgxeyEH9tJ8dSHdTQoqz1a7voVT1lSdryLidSwRy-eLMq1HgsHNyOKuVHzQY0-xWBxDHGzGoIcTeDTsx_06qVxnYXoPOlD1AZYTl5n2MSRPOMQ50aCszpih_vFP4yo3nKhFd8kvFPqKNS-spV0FyXczrXrMf23lnAP6tjfAWXRcDk0xAyf7ANLb-us_yHhQ7tWDAerSzsRnb06Cb4xF7bE-WQrBKR2HjTFrzRZSTrXqPfaVohQ9DgK4VpIEUtQoQBJM7vwF9TzYGck-2q01lsWHNuXEXsZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5_KNYjuoRaSZMqblKvp40j7pTyurzQGzKbFPmNmrtkqRgO9ES4rUiREbKGbePnJSizroeGljJ22-dr7JIH6R47aSXYTILHuOHF0YfciYrsIL8aDbZyACbKSnFNVf7GjYhOXsP1F6zjhRVdrpLhN5ZTO68ib9xtWfN3DYh2Sql2d86MNX_9TPy8Kmq-laTF1okT1PHjOWS74zYOcThXB8pvfsVaSASkby5mrVgzcjH4uWfxuIiYZaQA7NUbIOTZel0ClILOXP5YUZVK2pC4hew-m7RVLyQup8SQK9j-_qc8NyhH12LwtMmoht0MX22smEsh0kDppTBjp249LCuA0yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LWspFoFZ1PobpVjPKmqYToCS8xlwqsyidulIuEfOsAFRQv-U1dA-AGMfdN1Fso-QB0BipKHcb-fz9cpyvgAeHGltj_o4ge2cAO48qyQFm-EdOnAeHQqTjVwO24xzY6zuQiMNtijrBxIyOM-hz3jp69fTSSRpM-9CPCKAzito3qcbedbJ3gbMf4IKkThSW38_eRTe3JB-VR1-bX3vx_63WAhCW9yqMHfH-QKvDk-NwQFCRkCOKj_MMiuHoIocX6y-Skx8twEF98VX-jJX2ffdY57nkXxj3-fYDPozc4Ewpkp6mAI3ZyWMI6STYHYf7irPB0mW6g5HYeT5JQQZEnnORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FemaJRdCZXxeXZH9r3TNtOv58ETh4Y-wNBDZZE5-PrWDghBau-rAVwzRC5y_yH5WHK1oWBw2VkHhZ4dU7LOfNtrWvNZX36iPEmQW25LoNRmIgXuSm7ubOJ2xuVcCCRfUOYrZbn6-QCmMtCrAQUwz77CbPSQqDxolQPIFWEb9O3AH847XbRxENrfnYEGz2303RH0GdEvjfSefirVF28zHp9arkPiy9fRWalC_dx5Hyrorc7lHeuGAIOrMbwYt9GlXGkCiixOvLykKQ7sERvV-eLusMxqp2PTH_OHKmK2oxdMdxDpH8K0Jd7W5x7PIeK8iZR6Ep46-VRgKdnLTi7SDsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hu967w8ftwAAYohuhnyvtS1sYnlABsBXkbUup_4TK18stYY-dQt14Ux3s2cImbIq765p_gj7fOjX4WsipNXO44_127B47VH_2sS07UVrws14TuQakOThsLC8mV9YSWd3nL5j4X0WoTdzhfGiUdt_xudotZut-tduCkmW-zU7t6E6lPGr7-LEMyhVF2RBu7TXoTJgsKS1ymanN2uDX8tTIZ0bEPAH4WGRasCuSbI0M7ZSVbTk-6D5LZupSN06V98UIcqwmaleflN4HPDWDdZEtGiIH5yp7wpWAB6PLon_YUwpFFPN6XT_h6VAsBwLowbVm4Le0ykJBTTncYZlSCnG4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K-WJsiUVII0AcidvJpyyK6IAfiYJbQwgoxBZCERb-aR9uNghjuJy7wd8qyxtBl9HrSHrmRAPLqsv4AgvNmpsz-mBV9_myvFZ0AOjtAx7JYmzNfiP9QEsQLLClm7xQhSngBfT0hwy5eEbMWf0iAt86Qkc1u_jOD5fW0RTGYom5wOC5cggW6uBMSmRupimrpAjYyQPphQERPEYTvJtcyk8Lv4Ez1x0sVF2k-7zJTm2C3UjCmSNCecvG_LnZyoJstbmfZep_xopv-qfg865cE9cEUWutqmN3jWZaOap-sX_wY6Uw5GKwkxI0oXA0Gk5dnpPL3UuO_J7wVCm9XS64aQSHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0iTTa4eAyyQrRDvzjR4_BcBSIliYBzVS3cyIbGib8YTuKvAg3LN8KE64mUeOcd1DIOPXjqknygzZrkoK4yYsTqBuuSFHxfqKm7275nXz7rKD8CXEbuLFf2rlvXv9EPxQ5-uTC0gDuPtZii7ZxlXnwRp2EPe01OFYqQXeQ95hnTT5QhnXY6Yg2ktOwJTSf2SDvZFyjmGIuMTBFozzpRZsEb7L7jLm5Xr2MTVYsVfl9HWYkxOgGDrCQttkcmDa2Nd_Kb8V8bynxeH68E-5YNyfK4JmI8qrdoPj715yOi2qZiCKlL-oOFlAEEsPyAJ41q8YkgZC-4QMeFNU1y9sDvGew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سارقان و خریداران اموال مسروقه در تهران دستگیر شدند
عکس:
‌محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/458157" target="_blank">📅 15:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458155">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0PJcPsmmmEQj8rTeKqVktcyzq7PyURJhAFtqJjygd1xfuqz5yVVeAlsjikuzMwwHsU_6my_1Ym3J4-2hvXngXDlmz8fY7Bp9lWFfC4K7Oh-lRD1BBaIAlX3ySQEZWxqLK6yU0TZ3lygn1cqOnVUVDLHqBuQym3dw2JZOPzjgZP5LjK_ht12gN6ATJ0bltdP-ILSHNqiS3655zagym4_PhMNiNP-VIw7Nguwr7TsrtFhBYPkgFkCtrpbjOnPRKojG425fUY1QHFHPkQI-SAVBBlJYoiSXWORuoH5_8dgyspQduVmurL7vkfYxaSPyuoZJHOXYN8Iwc35kSFjjockHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FLyOY8Y2434xtHLSBxNHua_Zr_euvSpT20MSgiYo7dBCACNXQU9JB5qux75vkXsPPIL8rh1G0J9UlILUFJgsh-APIB2L9CgftUnVAAJkMMgmkwPsiUAdQrBi1SMmcVRThztQWQBxml95DGyxJBBM8QF1A4kBGvzrzuxnRbCmL13fTw6xdFZTcFLkW3tsfrZOMrBwqIby2FvFVzgaatirSk-UZt5iWc5_M-NKtDNc937nZHsjv4Ar_frOC8HqwyhS5LnQAqtf4KM9e21Zoe_1NPdeKoLPMWzlMsnijyPc0t4uTOqe3_Ef5KF5Ngxb_QzDNlAN-LWd8YnfJp3NdcPh2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزیر خارجۀ عمان فردا به تهران سفر می‌کند
🔹
سخنگوی وزارت خارجه: این سفر در راستای تقویت همکاری‌های دوجانبه ایران و عمان و ادامۀ مشورت‌های مستمر سیاسی بین دو طرف، به‌عنوان دو کشور ساحلی تنگۀ هرمز، برای کمک به تقویت صلح و امنیت در منطقه انجام می‌شود. @Farsna…</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/458155" target="_blank">📅 15:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458154">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGFZMHoiB1w3UWL8koP36rGrdxpR2uFBu6_4Vs8HOeK8oNs96rhEhkCTBi3EX65POKnWoa4uX0FIFQ9SD7_VHXy3Ph4JPjF5eJB-buG9u-SPoxgnkL5n9VE-RmCXdGSipHsHafy2Ms8BBOk75Sxk-R6IUj5s7ND6_nvsKPD9lAlja0l67_9p3TGSory18Nfj1wsoTdnzaAIaKYz_U5U2X9vpr0nFzO0TjRDjWvNpqWMFZWMnasDvYK2QeyT4LKC8zpWoQojKNkfPnwlqJCPLMGeuY8-8XVc05l_UyKQaNXntqudQkLA9jPUL2e1UH4O_C9bNk7cGWKUo99HM_a1_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ از توهم هرمز به دریاچه کانادایی رسید
🔹
در حالی که توهم روزهای اخیر دونالد ترامپ درباره «آمریکایی» کردن تنگه هرمز خبرساز شده، حالا او در پیامی به سراغ تغییر نام یک دریاچه کانادایی رفته است.
🔹
پیام جدید ترامپ در شرایطی منتشر شده که پس از ناکامی مذاکرات چندین ماهه آمریکا و کانادا، جنگ تعرفه‌ای این دو کشور همسایه عضو ناتو بالا گرفته است.
🔹
او در پیام خود نوشت: «ایالات متحده در حال بررسی جدی تغییر دادن نام دریاچه انتاریو به دریاچه آمریکا است.»
🔹
رئیس‌جمهور آمریکا افزود: «ما انتظار نداریم که دیگر هیچ مراوده تجاری با انتاریو نداشته باشیم. از توجه شما به این موضوع سپاسگزارم.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/458154" target="_blank">📅 14:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458153">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pubhvdDuefs3DxIA9GWlZVrJHtlwAy1agzUaChBmbxh3EpMWlSKovY5LUOnd9OxZjE7zB8YQSuJxLi6FfaD5abUlVKkaiRZWokvnRu9WUi_XV7FdPnCeBYSKvxACx0YyF9XXadl4OaUbUlVHi6kR70-g9ta87z5QKCuIZQg9riUHwUA5zM-JLlLx7hwCwh8xPuoTIZxJlCY1rvmrMJGGIv2tsvP6gPMT_j6bfqNXfr7dQBkV3I8L9g5z87EnJoD7HpFYx2byjj_bwv8NFDrUg0nv4H1Y30FIaW5hcgCa7L5DVPjiEMCo3ucc-6vOSmz7u_pwb6luAePGHmC4a5Ts0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرپرست وزارت دفاع: هر فشاری که معیشت و امنيت مردم را هدف بگیرد، بخشی از جنگ است
🔹
کسانی که میدان فشار را گسترش می‌دهند بدانند، ما هم برای دفاع از مردم میدان را در چارچوب منافع ملی گسترش خواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/458153" target="_blank">📅 14:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458152">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZbBZqSPQETpoXQ7lgCHbq5h04PEhHJ_Xf9jOSC3AFdPCmpzip81jyXJ8u-6cRcJ19S0P-l92GTrfUvxOB32fyre-fr16eo_gOWP6sXiKFbv_3MWrxrmzPstw5GawdEu3w-Hl9pke8BfifVZ2OqWSjTrJWQkXYVp_YRu79bTRAv5qhujp0nkxuu83AbzG4IM5AeqPByw9KLK8mJ_x0hBay63vKODvXwYcD5PrC2ncs5RP9QB61x7BKr5-xYekligbaZ7bOhkhfoff3Q7BwvVtCI1V7F5RzT5Vu1Oovg8Mt8GpAwnefFEuxWk1pIlcv2dmSZjmspUGtEpfhtRpAxT3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۲۶ سلاح غیرمجاز در مرز سیستان‌وبلوچستان
🔹
مرزبانی فراجا: در یک عملیات از قاچاقچیانی که قصد انتقال سلا‌ح‌های غیرمجاز از مرز سیستان‌وبلوچستان به کشور داشتند، ۲۲ کلت کمری، ۴ سلاح شکاری، ۲ نارنجک دستی و ۱۳ خشاب کشف شد.
🔹
قاچاقیان با استفاده از شرایط سخت جغرافیایی فرار کردند، اما تلاش‌ها برای دستگیری آن‌ها ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/458152" target="_blank">📅 14:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458151">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a487029da7.mp4?token=OfVSej94AlqzjyHb7KwXrrMlziunZhvOyT8sm4nETqg9yAG8ZlW2t8BoDOUorwcNtk33WHD_iueGmdi1yD7zXx_szwAz27XqvFEl2nyq-l7y9j4l1cm7M9MceS2kHsU2_WZOXe_wrzRf-gWQvIpw4VsKLKXYUHINHu7iPOwU2TT4dR2Pl9_1Nrbn3o4nRfTyMFpWsvLSzDKOw38yCEMfSTbPXxWhD948R3SXcef9Lmiin4tjZViojRJ0e4EOPJ3SADRpm1Z48459XuVbQDFYqegkYgOIIyMLnZQ6Ugj6cWxW0YuxzV1N2guDb4OGSjzEqC9li9WQq56DaVxycSLpRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a487029da7.mp4?token=OfVSej94AlqzjyHb7KwXrrMlziunZhvOyT8sm4nETqg9yAG8ZlW2t8BoDOUorwcNtk33WHD_iueGmdi1yD7zXx_szwAz27XqvFEl2nyq-l7y9j4l1cm7M9MceS2kHsU2_WZOXe_wrzRf-gWQvIpw4VsKLKXYUHINHu7iPOwU2TT4dR2Pl9_1Nrbn3o4nRfTyMFpWsvLSzDKOw38yCEMfSTbPXxWhD948R3SXcef9Lmiin4tjZViojRJ0e4EOPJ3SADRpm1Z48459XuVbQDFYqegkYgOIIyMLnZQ6Ugj6cWxW0YuxzV1N2guDb4OGSjzEqC9li9WQq56DaVxycSLpRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اژه‌ای در دیدار با رئیس شورای‌عالی قضایی عراق: همکاری‌های ایران و عراق در همهٔ ابعاد عمیق شده
🔹
رئیس قوه‌قضائیه در دیدار با فائق زیدان گفت: روابط ایران و عراق در بُعد قضایی و حقوقی روابط با تفاهم‌نامه‌ها و موافقتنامه‌هایی که منعقد شده، توسعه پیدا کرده است.…</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/458151" target="_blank">📅 13:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458150">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6RGNUn5ziVwduB6H7UueOdIk2-VtKAm3CKSrzcw9oncEmxfKzgkyHqTHO42QwIU4k88T1UXCMYAta4MWvkJwkYpC_AshKpO1E0G_5KTfbcuSWxg_5Vqnj5PKrlDSZ7JrYuqasRapS-tJIvVuEojttwVsoZHDHTlDBMt-Yrow1HfcmFqUExVxDnMlMi2WMtN1k0gyiM8_-GcpfRu8BTl2PBOcN1aEC76vWf-EKotrpMXYS8j_kl4oz6DOlIrGjAs2gdq4YQNDBMkkqHzs8bhPsBuo4BMArbRag0Zal4BPSu-Qo3uH5hCq2UaNqe7s3AgT1iiyanEOQh9BcVXrFYVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قربانیان جنگ ترامپ با ایران در مزارع آمریکا
🔹
طبق گزارش فایننشال‌تایمز، کشاورزان آمریکا می‌گویند تبعات جنگ با ایران باعث جهش شدید هزینه‌های تولید شده و بحران مالی بی‌سابقه‌ای را برای آنها رقم زده است.
🔹
براساس برآورد فدراسیون مزارع آمریکا، تولیدکنندگان ۹ محصول عمده از جمله ذرت در صورت نبود حمایت‌های دولتی ممکن است امسال حدود ۳۱ میلیارد دلار و سال آینده ۳۲ میلیارد دلار زیان کنند.
🔹
این بحران در آستانهٔ انتخابات کنگره برای دولت ترامپ اهمیت سیاسی ویژه‌ای دارد؛ چراکه کشاورزان از پایگاه‌های مهم رأی‌دهندگان جمهوری‌خواه محسوب می‌شوند و نظرسنجی‌ها نیز از افزایش نارضایتی اقتصادی بخشی از جامعهٔ آمریکا حکایت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/458150" target="_blank">📅 13:39 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458149">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26d8c64f97.mp4?token=ut4_5BlVDuCz7bvXq5JvIBaLxIwRqaVB1jDvYuGJdqD-pEeLQKENh05jdSo9mijytPg-LbyNrkiYWYdQ3J3DlCLnYUvOawqOInENqOcSPhXxyRP7heqF8akqd-E-91fIHjDSdFBd-ElquuferIy3xer-SfnR2aglaFSv9fn9wAXQXW2Dd4f5QU142yU7YrUmyzfAcSerWmuBmdIhOOeayOxGtA3CbQzsgzR48Q4OElgr1LItkDzWqoKdPWcUoSH9WRe_az-UKUsGV_ym0VeppC7SKmqgYHZsejqrS5odkcZUtiPC2bZeAFvyZPWXqMWY4kQZHo0Tptm62RShZ7Tu51q3YjeKx7XcFB7QfK2yX7CNk3CZnE8tmTXmAbSlRmf5lNkP438zD4nTDNTdqtf6ZR3j4kpbPKnPNrf22WdEQV0iVsmwZ5lbNlaUsYWSU_Bl8YIAUSYBQ9hFzIX1-JhDS5DpP4xHdlaWskBbHirXYh1Vkp59MBkua4mBOFd20Y50hjmVcaBa-tKFc389Rap4f1wyMvdYh207Dk89aeS0hftA-7eEiKU-PmWCt9xg2jrKBvt2-DEEw4q9FMPtbAN9Ey6S_aa1L2W5ga69fGTpYN3X_PFirrVnXHNqxZVgGm4ilIub3NgMteuJ-7ylB0j6ZU1dsp3sDkPvWrf-uxbIYa0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26d8c64f97.mp4?token=ut4_5BlVDuCz7bvXq5JvIBaLxIwRqaVB1jDvYuGJdqD-pEeLQKENh05jdSo9mijytPg-LbyNrkiYWYdQ3J3DlCLnYUvOawqOInENqOcSPhXxyRP7heqF8akqd-E-91fIHjDSdFBd-ElquuferIy3xer-SfnR2aglaFSv9fn9wAXQXW2Dd4f5QU142yU7YrUmyzfAcSerWmuBmdIhOOeayOxGtA3CbQzsgzR48Q4OElgr1LItkDzWqoKdPWcUoSH9WRe_az-UKUsGV_ym0VeppC7SKmqgYHZsejqrS5odkcZUtiPC2bZeAFvyZPWXqMWY4kQZHo0Tptm62RShZ7Tu51q3YjeKx7XcFB7QfK2yX7CNk3CZnE8tmTXmAbSlRmf5lNkP438zD4nTDNTdqtf6ZR3j4kpbPKnPNrf22WdEQV0iVsmwZ5lbNlaUsYWSU_Bl8YIAUSYBQ9hFzIX1-JhDS5DpP4xHdlaWskBbHirXYh1Vkp59MBkua4mBOFd20Y50hjmVcaBa-tKFc389Rap4f1wyMvdYh207Dk89aeS0hftA-7eEiKU-PmWCt9xg2jrKBvt2-DEEw4q9FMPtbAN9Ey6S_aa1L2W5ga69fGTpYN3X_PFirrVnXHNqxZVgGm4ilIub3NgMteuJ-7ylB0j6ZU1dsp3sDkPvWrf-uxbIYa0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
ببینید
👇
✅
معیارهای پنج‌گانه انتخاب مدیران در شستا
🔹
محمدرضا سعیدی مدیرعامل شستا ضمن تاکید بر اینکه توسعه اقتصاد در گرو توسعه بنگاه‌های بزرگ است؛ معیارهای پنج‌گانه انتخاب مدیران در شستا را تشریح کرد.
@tappico1381</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/458149" target="_blank">📅 13:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458148">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0UoWdqBGkpvCSStCectjt9lYg04DcpqZzhqWhywWEDEZrHaB3DhaycLfekhTUvTJmA8aYCKP7dOEqndSiVZufnNKZW_yKYnHLD2-sT8MAm6sPwMmdvDcJ7PnbETHbrLqc1k5JDB2MGBOdeAcCaywohP9XwJXnntcZ5rkB9v0IhJAXd620F91z4kDVeiAs4Elwe4VtwjrvUhNNfHiAZC3tyEzIbbeaLLplWc6unurj_xjBdZt96ykst4V7ZZePTPKR2_Jct3B3VhqHIZrHm8asoIQCjuY9jiTnZL_VgHY58nCv_xjvcZGDQkrSR3O8OfPk7MuylSmcKtrHS-l0Ctew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
واگذاری سهام «سیمان تجارت مهریز» در فرابورس
⬅️
نشست خبری معرفی سهام شرکت «گروه صنعتی و معدنی سیمان تجارت مهریز» با نماد «سمهریز»، با حضور مدیران شرکت و خبرنگاران بازار سرمایه در فرابورس ایران برگزار شد. این شرکت در راستای سیاست‌های دولت در زمینه واگذاری بنگاه‌ها، توسعه نقش بازار سرمایه و مولدسازی دارایی‌ها، در فرابورس ایران عرضه خواهد شد.
⬅️
مدیرعامل شرکت با اشاره به ترکیب سهامداران، برنقش کلیدی بانک تجارت به‌عنوان سهامدار عمده تاکید کرد.
🔗
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/458148" target="_blank">📅 13:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458147">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/458147" target="_blank">📅 13:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458146">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boziJQG1YlMPVDT66C7Oaq4Zb-j-t6r9OdFv4a-EVl34W9IlcWZfnA_TgxseGkrBKeeaOsrKBWaXwoW3gEYbFxl9auxaOVOvdN9JbLXQwqNMgzlBkqIkFbsi8q-lEidBx7bKUZlQZWB9Vjn9ynSy1smAMUw4g-6woMRs5wW7eRWsMrJ-cLa1McehzFkls7MMhqvKALhR74VFVIh_uu531jdzWH6cVp8l59BbdYRU2Qszha0Ddch8RZ6czCMbL-mR0Yi5-v5FmfshlSCe5PtGoC6KK4YaSMz54C5m_PQZC8kkXmlLNIRWW3uOFNOoFMjsrO4xp2x9w_JKsGs0fp5pTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اژه‌ای در دیدار با رئیس شورای‌عالی قضایی عراق: همکاری‌های ایران و عراق در همهٔ ابعاد عمیق شده
🔹
رئیس قوه‌قضائیه در دیدار با فائق زیدان گفت: روابط ایران و عراق در بُعد قضایی و حقوقی روابط با تفاهم‌نامه‌ها و موافقتنامه‌هایی که منعقد شده، توسعه پیدا کرده است. ما بر تعمیق هر چه بیشتر این بُعد از روابط تأکید داریم و در این راستا آمادهٔ هرگونه همکاری با دستگاه قضایی عراق هستیم.
🔹
اژه‌ای با اشاره به تفاهم‌نامهٔ تبادل زندانیان بین ایران و عراق گفت: یادداشت‌های تفاهم و توافق قضایی و انتقال و تبادل زندانیان میان ایران و عراق منعقد شده و بر همین اساس، ما بر تقویت موضوع استرداد محکومان ایرانی و عراقی و ایجاد تسهیلات برای خانواده‌های آن‌ها تأکید داریم. پارسال بالغ بر ۱۳۱ محکوم ایرانی از زندان‌های عراق مسترد شدند.
🔹
رئیس شورای‌عالی قضایی عراق هم در‌ این دیدار گفت: حاکمیت و ملت عراق در موضوع تجاوز جنایتکارانهٔ آمریکا و اسرائیل به ایران، با دولت و ملت ایران همبستگی دارد. ما هیچ‌وقت حمایت‌های ایران از عراق چه در سال ۲۰۰۳ و چه در ایام بحران تروریسم را فراموش نمی‌کنیم.
🔹
خون شهدای ایرانی و عراقی در مبارزه با تروریسم در هم آمیخته است و ما اوج این قضیه را در زمان شهادت شهیدان حاج قاسم سلیمانی و ابومهدی المهندس شاهد بودیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/458146" target="_blank">📅 13:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458145">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YppLEocn6hwW1I23SDmhu8UGrVbxzTMPvUWTfPESrQmZL4a6-DFZknPuid5zXY51f-rPCCQdeph7dFw20y9Q6ZpLDTDJFz0Bjmy7AfC9Wpg2bO5VD6Rdsah_s22qAiEpukz7ssj5l6oetIrsl2FvVay72KFci_ZJ82D5opB5-CpdAz65t4RQ6Rw4uRXWDUkv8ZD7yFsrjdfp3lqGP5T_wHHNyRu9dFnhPS05f3-0UV87jYlluTdOiCHRV-iKOKZtD85bLs2QGXSV-MHkxbNNdp1TvBPbRWuOTB5Hw6icBbJeq7KwnqYM-ur_CKgw3Ga81C5MTaIMPEH6bvZDSE_sWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گران‌ترین بازیکن لیگ ایران مشخص شد
🔹
سایت ترانسفرمارکت در به‌روزرسانی جدیدش ارزش بازیکنان فصل جدید لیگ برتر ایران را اعلام کرد تا امیرحسین حسین‌زاده، مهاجم ملی‌پوش تراکتور با ۲.۲ میلیون یورو گران‌ترین بازیکن لیگ لقب بگیرد.
📊
پنج بازیکن گران قیمت لیگ برتر ایران:
⬅️
امیرحسین حسین‌زاده(تراکتور): ۲.۲ میلیون یورو
⬅️
اوستون اورونوف(پرسپولیس): ۲ میلیون یورو
⬅️
یاسر آسانی(استقلال): ۱.۸ میلیون یورو
⬅️
علی علیپور(پرسپولیس): ۱.۷ میلیون یورو
⬅️
حسین کنعانی‌زادگان(پرسپولیس): ۱.۶ میلیون یورو
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/458145" target="_blank">📅 13:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458144">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8OerPeIM3vECjmPmYeK0gA1lDk7nG2-G3gm8cC-ffxEuTHT5ZCkxeUybAq22xawnRIbPB8TSDG5rCvwuk18EYdJrvwoix7ewR_hO3NeFxv5fn96C5ejvLB2hZw0v-kBN6wq5yXbAaqt8uPa0YYtnxeTnXT9t5Nq7P33yTJ0AECqHaM-2_tzkB9c0RQW1zdk8u7EB7O7YT6gJjuel79-IW-r8jjjareeFQ8BgMsu0naFfcW1aLqxqyBuYs4OkLdPzm9qGcdV1zSY-T5WUodx8aR5be0zuU1MNc_VbkEan7jrJtvtyDViynbvah9N55CsDAmybMWyLBpuIo8i7CjG1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین: با تحریم‌های غیرقانونی آمریکا مخالفیم
🔹
چین ضمن مخالفت با تحریم‌های یکجانبه واشنگتن علیه ایران که افراد و نهادهای این کشور را هم هدف قرار می‌دهد، تأکید کرد که از حقوق و منافع شرکت‌های چینی حمایت خواهد کرد.
🔹
به گفته سخنگوی سفارت چین در واشنگتن لیو چانگ،…</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/458144" target="_blank">📅 13:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458143">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">طرح مقابله با نفوذ بیگانگان، در دستور کار صحن علنی امروز مجلس
🔹
سخنگوی هیئت رئیسۀ مجلس: ادامۀ رسیدگی به گزارش کمیسیون امنیت ملی مبنی بر مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در دستور کار جلسۀ سه‌شنبه صحن علنی مجلس قرار دارد.  @Farsna…</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/458143" target="_blank">📅 12:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458142">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXavLdFfbk5b52wUr9qQmBldLEJ2LxAZIv2Yrv6fHHlyEozDnrS7Xu0IU5KmaKVAM0MF4obAQbl7t7juSE6OsUwY43nttUS22X6BCZGT0RbvBcgvm0Pj7H5fweZLfWYl97-8SE2LOZA8jn55aWfU4VHn5tLr0F-trUoymaooAphx-Zj4MNewr-DPfpwXVjgyHrZd6tDv51SUTgG1uLnU-WR8whe9sytiH7c8Bp0hQgDUAp-rD5NeXyqo1aMPjuZnYvHCxLMwAmDRkYDMJpL7t9FjFuXlxepK79gqxIdChy1cM9eYqmpf5Jy_6X6FP2tNpzeVLskDc8Rn-2KfXRK81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد تاریخی جدید بورس با جهش ۲ درصدی
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۴ هزار واحدی به ۶ میلیون و ۲۲۴ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/458142" target="_blank">📅 12:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458141">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ab6957ba.mp4?token=EKGqPoaCulfwkqD12UzK5nncVgel1bkqbwU0HelLWA342THhz1TIjBi6369YJXZMTUA-q2-SnVuLEna9amDtGS_1vWw_5BMy6ZEcca_dmvA7km2JFnw6zO8aNeodIgCpdMRYQ1K0l0474QaZF_3ydOJdHc5N-eJ0EOv1JjatrYAjLmX410CVKeUfkS8cgY5_eNhcYftuGofH0VUH_pwltdBB81HfdBNhxaoW_TSoNLMdVB07H8ohPFOxnELHxVT19wohOxS5m4dewZMFneiOhkUGPUnRhH7I3LaaARHwg4M1RgBB11IFZzrqTGUK4pMyO-LGrq_YnHB1aylbIV8AUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ab6957ba.mp4?token=EKGqPoaCulfwkqD12UzK5nncVgel1bkqbwU0HelLWA342THhz1TIjBi6369YJXZMTUA-q2-SnVuLEna9amDtGS_1vWw_5BMy6ZEcca_dmvA7km2JFnw6zO8aNeodIgCpdMRYQ1K0l0474QaZF_3ydOJdHc5N-eJ0EOv1JjatrYAjLmX410CVKeUfkS8cgY5_eNhcYftuGofH0VUH_pwltdBB81HfdBNhxaoW_TSoNLMdVB07H8ohPFOxnELHxVT19wohOxS5m4dewZMFneiOhkUGPUnRhH7I3LaaARHwg4M1RgBB11IFZzrqTGUK4pMyO-LGrq_YnHB1aylbIV8AUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: تا ماه آینده از طرح جامع تقویت اقتصاد خانوار در تهران رونمایی می‌کنیم
🔹
این طرح در ۴ سرفصل مراکز آموزشی و پشتیبانی دارد تا کمک کند که اصطلاحاً به‌جای ماهی‌دادن به شهروندان، به آن‌ها ماهی‌گرفتن یاد بدهیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/458141" target="_blank">📅 12:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458140">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad6cf14bb.mp4?token=Tpw-qOqF8j1fEKcdYjsnFSZwjDJke5YOIi8e0G8Spp7_VLmaVOU5NKN9hlNvatxW8kpXGRoYzCp34EKn02mM8kc0dyq0Iv9BrbiAsXhnFkvD5Pr-0-kQNJ7aK7xEOBKvDb2Tr_R-lFvJ1BiDigEoi5uh9r1lMUsrbtx4wasby7Mq_mkrOD3Ldm39hYsnK2RrIpD1KwpYo230B15CXZO5y_4t57cG_nSq2XKs39z3BjBERZ8U4LzY6heXoRm88d0ZLvQr6HShXh8_Est2Nl7AjfvWIh5RNuYlLJcVJoYuYWndNWXjDdQHdVjqAM-z6CKai7PIJMMOGC5ckMl_N-ysRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad6cf14bb.mp4?token=Tpw-qOqF8j1fEKcdYjsnFSZwjDJke5YOIi8e0G8Spp7_VLmaVOU5NKN9hlNvatxW8kpXGRoYzCp34EKn02mM8kc0dyq0Iv9BrbiAsXhnFkvD5Pr-0-kQNJ7aK7xEOBKvDb2Tr_R-lFvJ1BiDigEoi5uh9r1lMUsrbtx4wasby7Mq_mkrOD3Ldm39hYsnK2RrIpD1KwpYo230B15CXZO5y_4t57cG_nSq2XKs39z3BjBERZ8U4LzY6heXoRm88d0ZLvQr6HShXh8_Est2Nl7AjfvWIh5RNuYlLJcVJoYuYWndNWXjDdQHdVjqAM-z6CKai7PIJMMOGC5ckMl_N-ysRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: شهرداری کنترل بازار اجارهٔ مسکن تهران را از چنگال سوداگران خارج می‌کند
🔹
۵۱ درصد تهرانی‌ها اجاره‌نشین هستند که بیش از ۶۰ تا ۷۰ درصد درآمدشان را خرج مسکن می‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/458140" target="_blank">📅 12:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458139">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a323b1e08.mp4?token=Fs9-VaoSlUXKZBfa4qg7jxU0XhbsL-59U0KcC1_iE5xwaFOFwHHMlUrqJopt_JIEIOy8FspmwNMLK0cizwAAdwTY9Z0VwCz8c_jqo4StWh67mOJr8Ex0gan6lZ0SzloRMxY75ZRhjrEudyS3_jXHY6dsbKchfXeZHX4EXhoYmIL-M4VKLB_A4momtA1_UoUad6qvl-ItSs1kKNY64lZ_soz9U2-K1j8d7Nrb8WNFiwSv9VMmFaUPQCTimj4o8adZCurBs62Ho6Wo5RoDqMYoLDenDvFL1ub9cPSjW4V7TpOMsV5Bh7SttEJjpfI6mIQeaCXdE-EOo2nvgILcRIyMlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a323b1e08.mp4?token=Fs9-VaoSlUXKZBfa4qg7jxU0XhbsL-59U0KcC1_iE5xwaFOFwHHMlUrqJopt_JIEIOy8FspmwNMLK0cizwAAdwTY9Z0VwCz8c_jqo4StWh67mOJr8Ex0gan6lZ0SzloRMxY75ZRhjrEudyS3_jXHY6dsbKchfXeZHX4EXhoYmIL-M4VKLB_A4momtA1_UoUad6qvl-ItSs1kKNY64lZ_soz9U2-K1j8d7Nrb8WNFiwSv9VMmFaUPQCTimj4o8adZCurBs62Ho6Wo5RoDqMYoLDenDvFL1ub9cPSjW4V7TpOMsV5Bh7SttEJjpfI6mIQeaCXdE-EOo2nvgILcRIyMlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ عرضهٔ مسکن متری تهران از فردا آغاز می‌شود
🔹
درحالی‌که بیش از ۷۰ درصد درآمد خانوارها صرف هزینهٔ مسکن می‌شود. شهرداری برای خانه‌دارکردن مردم، از فردا طرح «خانه‌ریز» را به‌صورت رسمی آغاز می‌کند.
🔹
قیمت خانه‌ریز معادل میانگین قیمت کل آن ملک است و افراد می‌توانند…</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/458139" target="_blank">📅 12:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458138">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2af26a6d5.mp4?token=qgvVTAVLdoHDtC_99nSNQ2aC3Tx7VEDutpjqBLUGfm8EV3SaILSWgnr0BPV7mgMFKD61Q7YYO7FiBa5w9OqwN7pst8S4PPDqH585xyjAl0xfhJ5-i7OqTxtwrM-sWxHo1nf8-2YGxPPTRYkqhipYXWH1wOU9CBFibB31rLKx7D2fB0gwcwXwbhsoiHKhmXStGwx2zmwOsfImF4aJN09gpiVw2kfMZSmMa_XqJhALrT04q6Fr4s2TsePOf2QmabVVrAC4RB59l05V5M0NWzrGs_ltGsRffB__zbOBLxavUM1UZ4Tc9BynwAu2Yh5Y-TkavR8MBX9LHEAhdUKqsTjEGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2af26a6d5.mp4?token=qgvVTAVLdoHDtC_99nSNQ2aC3Tx7VEDutpjqBLUGfm8EV3SaILSWgnr0BPV7mgMFKD61Q7YYO7FiBa5w9OqwN7pst8S4PPDqH585xyjAl0xfhJ5-i7OqTxtwrM-sWxHo1nf8-2YGxPPTRYkqhipYXWH1wOU9CBFibB31rLKx7D2fB0gwcwXwbhsoiHKhmXStGwx2zmwOsfImF4aJN09gpiVw2kfMZSmMa_XqJhALrT04q6Fr4s2TsePOf2QmabVVrAC4RB59l05V5M0NWzrGs_ltGsRffB__zbOBLxavUM1UZ4Tc9BynwAu2Yh5Y-TkavR8MBX9LHEAhdUKqsTjEGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی: کالاهای اساسی را برای دهک‌های پایین جامعه با تخفیف ۵۰ درصدی عرضه می‌کنیم
🔹
شهردار تهران: یکی از اقدامات مهمی که شهرداری تهران به‌دنبال عملیاتی‌کردن آن است، ارائهٔ تخفیف ۳۰ تا ۵۰ درصدی در کالاهای اساسی به دهک‌های پایین جامعه است.
🔹
در نخستین گام به‌دنبال…</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/458138" target="_blank">📅 12:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458137">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33c6340a4f.mp4?token=JMeYRhJixkQvas8vlSpVEP45mCFAaMcTUeerDTLpy5RdD16IVn08bY2vGL4uZuTqOxjQcpj2Euj-voWCf1qsO_gzUvAyocFatg9Bir28PJe4UUvqIwQRPKtsxtbvaStRGMjCayeMNMjnyNlAFsCIptf84Uz-6_sHSO1fP-keSyWzbOAArOUtCvmgRe2ERBTSJjtnVaBzTMl65v9TaUkwsF_95rQsa12CRyCXi7TJp2EUIi2TwsGqBixTUC1yv0Zb_VCnrSb6CWI4m4Nmy6hGiIMzWbMTof_xirqGTWNpZnSkijLwdrDpLF_Pi5SHXItGA31M4PBJtzfdLdK9LWRYVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33c6340a4f.mp4?token=JMeYRhJixkQvas8vlSpVEP45mCFAaMcTUeerDTLpy5RdD16IVn08bY2vGL4uZuTqOxjQcpj2Euj-voWCf1qsO_gzUvAyocFatg9Bir28PJe4UUvqIwQRPKtsxtbvaStRGMjCayeMNMjnyNlAFsCIptf84Uz-6_sHSO1fP-keSyWzbOAArOUtCvmgRe2ERBTSJjtnVaBzTMl65v9TaUkwsF_95rQsa12CRyCXi7TJp2EUIi2TwsGqBixTUC1yv0Zb_VCnrSb6CWI4m4Nmy6hGiIMzWbMTof_xirqGTWNpZnSkijLwdrDpLF_Pi5SHXItGA31M4PBJtzfdLdK9LWRYVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون پزشکیان: رئیس‌جمهور به من گفت «آقای زاکانی یک اتاق فرماندهی برای پایش وضعیت مصرف سوخت تهران درست کند و من حاضرم روزی یک ساعت در این اتاق وضعیت را بررسی کنم». آقای زاکانی صددرصد پای‌کار است.  @Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/458137" target="_blank">📅 12:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458136">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f85e9480.mp4?token=bd7IWFMls6Pi8igvDQ1mlSOXOOXFarQuhjhX5ujHKiea6lepgN-GeIFQMyIduNUZE04srdg4TZnhXtcSfgR7wUmLQpmhdQ73Y0h5-FBKA0kVUZ6YTM086lE18e4Egi0Q7rBnf7DZ_9Jw3whd9VIRD1vRK8UwvP0fi9LBBcuUYM_GbLTo14tuNsVTp-2_eablHx7dPwRahsaHo8-DuUWPzsYh-o82tNCx-0IezwLVsO1tL9dOX2kA45TX2hGjYMlvjllwTa3lthPfrvbnTiCk47pNcC6yZoDevJVxApLeA8gp_97nSo0VPAOASy05BLGVlFEHxr_aoHD8LpVnFn9mPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f85e9480.mp4?token=bd7IWFMls6Pi8igvDQ1mlSOXOOXFarQuhjhX5ujHKiea6lepgN-GeIFQMyIduNUZE04srdg4TZnhXtcSfgR7wUmLQpmhdQ73Y0h5-FBKA0kVUZ6YTM086lE18e4Egi0Q7rBnf7DZ_9Jw3whd9VIRD1vRK8UwvP0fi9LBBcuUYM_GbLTo14tuNsVTp-2_eablHx7dPwRahsaHo8-DuUWPzsYh-o82tNCx-0IezwLVsO1tL9dOX2kA45TX2hGjYMlvjllwTa3lthPfrvbnTiCk47pNcC6yZoDevJVxApLeA8gp_97nSo0VPAOASy05BLGVlFEHxr_aoHD8LpVnFn9mPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقاب اصفهانی: خودروهای غیراستاندارد بخش بزرگی از بنزین کشور را می‌بلعند
🔹
رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی: بررسی‌های انجام‌شده نشان می‌دهد یکی از عوامل اصلی افزایش مصرف بنزین، پایین‌بودن استاندارد خودروهاست و حدود ۴۰ تا ۵۰ درصد فاصله میان مصرف…</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/458136" target="_blank">📅 12:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458135">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d4cdc7c07.mp4?token=G_qiUXnRrBNCDiXnPv2h-S3CoXlLCgn1-upoNGDRF-D95yBfPGq7guvwMyQt6hil6JxSs-sqOUjMXiFHaTc9H9C0v_UlbDk8GUDniCJcuf4pRRoAs8A-3ForVdpN9trvYxbPH0pTp7q_NGxJeuTFIsQ2BIRf1wzalREpTjum89022VL24pzN2yRVkuFkQuLYTCqBksZhoC6Ltxyhzk6Zhsl06xE_Ae8xjvn0vhwOV927ijCot739dDym_jbHGRezNUO1-a85ymNcgS_3om47wrLUul8GTKuNIjxC9RPQeV8Oq5-qj8xRbGmg9y0cA-yEqy7q5N4xHvvCJVlyL9eqZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d4cdc7c07.mp4?token=G_qiUXnRrBNCDiXnPv2h-S3CoXlLCgn1-upoNGDRF-D95yBfPGq7guvwMyQt6hil6JxSs-sqOUjMXiFHaTc9H9C0v_UlbDk8GUDniCJcuf4pRRoAs8A-3ForVdpN9trvYxbPH0pTp7q_NGxJeuTFIsQ2BIRf1wzalREpTjum89022VL24pzN2yRVkuFkQuLYTCqBksZhoC6Ltxyhzk6Zhsl06xE_Ae8xjvn0vhwOV927ijCot739dDym_jbHGRezNUO1-a85ymNcgS_3om47wrLUul8GTKuNIjxC9RPQeV8Oq5-qj8xRbGmg9y0cA-yEqy7q5N4xHvvCJVlyL9eqZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار فرمانده نیروی زمینی ارتش به تکفیری‌ها و عناصر معاند مستقر در آن‌سوی مرزها
🔹
امیر جهانشاهی: هرگونه تحرک، شرارت و اقدام علیه ایران با پاسخی قاطع و کوبنده مواجه خواهد شد.
🔹
پایش و اشراف اطلاعاتی کامل، طرح‌های عملیات رزم زمینی دشمن را خنثی کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/458135" target="_blank">📅 12:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458134">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ee52107d.mp4?token=DP6tM-mXv65ltcbChyQT1MOSIpXqD1R_PTFQi_uYUegaHel0TPg_n6SVjjjOx_Njp27EfY5qfWVWZ-F7Uxzla9L8_K8aZaHgyRu7mPZgT7Q0xj9YXQGTEJRi8yDUjUKZ0WtBS4fWSJm1yF4-vRlV0ab5Ath3oPgjy0KkyHLXDXHznvrkGtOGVG6cBk4x0fmJvuFy-qyoXhzr2mbLalCHbLzlzPuSYih0p-gxjm2HsZZmmP4_5dyQwMVEyAE2Ttw2z0C09MsocMkU1Kk_RFuwcGj8i6iTbj2q1ywUxw-6Bjchr8w3lqh-cDioG0VmZeczzEk7ARO07pkyx4bfi71cPiXxJLm8EVOOdN2TMwTJLyb-48VNkUPl_QyV07TywNQ3jX_clQhphyObk2kiLm1SenfsZtZVNDUm5s87LIL-L5A-e6_3uSnRfRBZkanWjiSl_4b1CMMIzIqjXl3CHdPRq10RHbvzN2f1MfAypzRlnMgXCooN7Pf-mEN3W-qyDmqoqWGqYqP00wF3caq3rUUttgtWjPjmBysWesaUVYIRuQ_6mhdPru8gBbByV1h7EdC2YX0hraxbzsOn1r6gdrByBCNe-SfK288NI2GjR-q96o3HBYL7pMW-zD09eIkhsAD1yLqYc_S3bIUU6Q6uss1L3NzOC2quNuWp1vsWDeldy-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ee52107d.mp4?token=DP6tM-mXv65ltcbChyQT1MOSIpXqD1R_PTFQi_uYUegaHel0TPg_n6SVjjjOx_Njp27EfY5qfWVWZ-F7Uxzla9L8_K8aZaHgyRu7mPZgT7Q0xj9YXQGTEJRi8yDUjUKZ0WtBS4fWSJm1yF4-vRlV0ab5Ath3oPgjy0KkyHLXDXHznvrkGtOGVG6cBk4x0fmJvuFy-qyoXhzr2mbLalCHbLzlzPuSYih0p-gxjm2HsZZmmP4_5dyQwMVEyAE2Ttw2z0C09MsocMkU1Kk_RFuwcGj8i6iTbj2q1ywUxw-6Bjchr8w3lqh-cDioG0VmZeczzEk7ARO07pkyx4bfi71cPiXxJLm8EVOOdN2TMwTJLyb-48VNkUPl_QyV07TywNQ3jX_clQhphyObk2kiLm1SenfsZtZVNDUm5s87LIL-L5A-e6_3uSnRfRBZkanWjiSl_4b1CMMIzIqjXl3CHdPRq10RHbvzN2f1MfAypzRlnMgXCooN7Pf-mEN3W-qyDmqoqWGqYqP00wF3caq3rUUttgtWjPjmBysWesaUVYIRuQ_6mhdPru8gBbByV1h7EdC2YX0hraxbzsOn1r6gdrByBCNe-SfK288NI2GjR-q96o3HBYL7pMW-zD09eIkhsAD1yLqYc_S3bIUU6Q6uss1L3NzOC2quNuWp1vsWDeldy-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودروسازان چطور بنزین‌ را می‌بلعند  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/458134" target="_blank">📅 12:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458133">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌ دانشگاه شریف: حکم اخراج رضا دالمن، دانشجوی اخراجی برای اجرا به دانشگاه ابلاغ شد
🔹
شورای بدوی حکم اخراج و ۵ سال محرومیت از تحصیل را صادر کرده بود که شورای تجدیدنظر ضمن تأیید اخراج، مدت محرومیت را به ۴ سال کاهش داد.   @Farsna - Link</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/458133" target="_blank">📅 11:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458132">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMAuT07vSjuvN5STVKT9ABBtS93M6Lh_RzvstzZ9FbVI1RMw5iHy-TfUXz3ijpqfpaz8r8Wff-ymxwYxIyAj-WfrHLdP0LnPMoa0rLn2lLJnmXRy8WzubPt_nhRdoBWWTfDIh_eKQFJee2hQSbVDr7L0AfYmvw-Ft-pEvlYzR66QmMZEsIaGxCPrTlhsyrPVWNWm6X7xn3inbUtjcTVG5GY8BVrmRb3BZcj3S-xTRT-W_XlQgVaesMIH2wgZfGXJDW6DsCTY7q3YHXyTDQmCGZMqmcaIxWtXvhceVSD6awRnf-2nEd-VM00ZSn7iXqx7wPXUlfZ2GSCM0vU2pIPeXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی دسترسی به اسکناس ارز را افزایش می‌دهد
🔹
براساس تصمیم بانک مرکزی، از امروز کلیهٔ اشخاص حقوقی می‌توانند با مراجعه به شعب بانک‌های ملت، تجارت و صادرات، نسبت به خرید اسکناس ارز تا سقف ۵ هزار دلار و اشخاص حقیقی نیز با مراجعه به این بانک‌ها تا سقف ۱۰۰۰…</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/458132" target="_blank">📅 11:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458131">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gxg7dC4BTtDpluBO_tk3-mHtcGYkh8BwTbPpRmr4GlQVgOiXzFTFH4V0Ua0MMaedTHyrnJnZQGBVJcEOCaA4BXZ44kfLv88FdxdErZaJRkL9VmP6NANbQBvSvSanYpxH9WEWTyjKDf9kk6soA1byk3PTSV0xhA1tdNlEiWxOUjZtcssnuuOzYuMCCrrHc-JWa_4YAu5CQlKVKfUtCZd1J9TWsEpioKuwJ6OFpB-e6aqOkO-eCeoHGhKE0Q53J4v89r5hFYBfpWMaL_-oPg0590z_TS1VSdMQBMpTByWyMck-YJ_qMNUl3hijtxd8_FOaHRgmCPKOWyY-TRTFDrXvEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی دسترسی به اسکناس ارز را افزایش می‌دهد
🔹
براساس تصمیم بانک مرکزی، از امروز کلیهٔ اشخاص حقوقی می‌توانند با مراجعه به شعب بانک‌های ملت، تجارت و صادرات، نسبت به خرید اسکناس ارز تا سقف ۵ هزار دلار و اشخاص حقیقی نیز با مراجعه به این بانک‌ها تا سقف ۱۰۰۰ دلار با نرخ توافقی اقدام کنند.
عکس: مرضیه نورعلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/458131" target="_blank">📅 11:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458130">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a9dbd2ef.mp4?token=QuAMLM0dHgK4bycqY3sGg57v6LMduSXhIIkTwYTkxBgwX0DbDBZFGMPINcEGEX4Fc7wXy0FBM1tx8tW3Ar05OJ_ETTBZoukbhjSdAEbraCibSl0qvpzeIAxJ2dTwVfWLP8-AX-E0gdoP7L5F07A9rvbPiqnzayiOKFS4j0CWlAqndNbPzklNa8nB0mgtotA91EHiheKIM1YNAFV3UzaTc-1AcB0EEHA7FrLVFgNR6yADm6gGdi-ZB711XaIf04iiA1bdZcOfkfxL1fixXhMwZz3FYJZjR6s4NITmkLmyuLCjMTdbWlSmGVNQ3rqZgAnqs8bbiOWVWvaqlKLW3Q0vKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a9dbd2ef.mp4?token=QuAMLM0dHgK4bycqY3sGg57v6LMduSXhIIkTwYTkxBgwX0DbDBZFGMPINcEGEX4Fc7wXy0FBM1tx8tW3Ar05OJ_ETTBZoukbhjSdAEbraCibSl0qvpzeIAxJ2dTwVfWLP8-AX-E0gdoP7L5F07A9rvbPiqnzayiOKFS4j0CWlAqndNbPzklNa8nB0mgtotA91EHiheKIM1YNAFV3UzaTc-1AcB0EEHA7FrLVFgNR6yADm6gGdi-ZB711XaIf04iiA1bdZcOfkfxL1fixXhMwZz3FYJZjR6s4NITmkLmyuLCjMTdbWlSmGVNQ3rqZgAnqs8bbiOWVWvaqlKLW3Q0vKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد نامزد مسلمان سنای آمریکا علیه رسانهٔ نزدیک به ترامپ
🔹
السید: مردم درگیر گرانی بنزین، معیشت، درمان و جنگی که ارتش را نابود می‌کند هستند؛ نه ورزش زنان!
🔹
نامزد دموکرات سنای آمریکا خطاب به ترامپ: تو نمی‌خواهی دربارهٔ قیمت بنزین صحبت کنی؛ نمی‌خواهی دربارهٔ قیمت مواد غذایی صحبت کنی؛ نمی‌خواهی دربارهٔ‌ خدمات درمانی صحبت کنی؛ نمی‌خواهی دربارهٔ این جنگ تجاری احمقانه که اقتصاد را نابود می‌کند صحبت کنی؛ جنگی که در حال نابودکردن ارتش خودمان هم هست.
🔹
مسئلهٔ مردم در میشیگان این است که چطور از پس هزینه بنزین بربیایند؛ مسئله در میشیگان این است که «وقتی بیمار شدم چطور نزد پزشک بروم؟ چطور شغلم را حفظ کنم؟»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/458130" target="_blank">📅 11:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458129">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJEgTS4joszwm2PEHDu4RxKrpwtO6gQVxbfLep6_TG6x5AUC-SUKJi56dXn8CSFDTUf6hgoZRFC2VWgVaAuONWxWnDObBdE60_rzVISIPgsk8IQSd-dJjLadIaJEIdMptXBontO6GVjUh7c0WjP-9acj6Sdtqnbs_iyUgSJsp3h9Bnj7FK54de-PxDmDpnstW_EGMJDaWRLaRk6Rt1VuL4UNUUe4GKieyNe_LES3JeZdBps3Wo21iHQz8v51g-yI78wsj3gmm25md7jWCTe7KqNYj4sRVTW3nW3Z-fdVkHqYVWKnjlqT-THKarqt0Liq2ldjWyIV8EQd-hPFaNSw2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
وزیر خزانه‌داری آمریکا: امروز شاهد افزایش ناگهانی قیمت نفت بودیم که من واقعاً دلیلش را نمی‌فهمم.
🔸
رئیس‌جمهور آمریکا امروز از تشدید اقدامات اقتصادی علیه ایران سخن گفته بود. @Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/458129" target="_blank">📅 11:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458128">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayl7CF1tAA3qB3BixhGUzeodmYkAK4QJUlwR_J5vILhFBwXzWu6acnPvCu0UT1qj-RjIZBO_XdbWHBFf0M7LuNa5US4x5BxUJMq8ChGCegrdsx0OV7za5Q1BBI2S2N2w1qC_eOT4FYRDZB70cowDayMi_mWTupXHua0lGgLL4ohgjl_VBOrSmXOyxKkq8bOmxxRZbYOK2lcYcSHVS9qljRp_lgp_qfvGLYkCmq1ggDY_TwuSQ5c0UkLnvfraYOeZo8YqUdD8ehjmZrK7OaAuLiHw8zNSEYDMZDe_HmRHr_JH6-_CPWLcWHB_CH7kUkQz54A6owbUHVT8duZgMmnM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاه‌آبادی: تلاش کردم ادبیات ترسناک را ایرانی کنم
🔹
حمیدرضا شاه‌آبادی، نویسندۀ «تابوت سرگردان»: ادبیات گوتیک و ادبیات ترسناک گاهی این امکان را فراهم می‌کند که آدم‌ها با ترس‌های درونی خود مواجه شوند، آنها را کشف کنند و به شکل ناخودآگاه با آنها کنار بیایند یا آنها را پس بزنند.
🔹
می‌توانیم بپذیریم که اولین مواجهه‌های مخاطبان نوجوان ایرانی با ادبیات ترسناک از طریق کتاب‌های خارجی صورت گرفته و سایۀ آن را قطعاً می‌بینیم.
🔹
حتی خیلی از نویسندگان ایرانی که داستان ترسناک می‌نویسند، تحت تأثیر کارهای خارجی هستند و همان فضاها را گاهی اوقات تکرار می‌کنند.
🔹
من به سهم خودم تلاش کردم که این‌طور نباشد. سعی کردم جهان داستانی خودم را داشته باشم و فضاسازی‌هایی داشته باشم که یک‌خرده رنگ و بوی ایرانی داشته باشد.
🔹
مثلا در «تابوت سرگردان» ابتدا با مراجعه به «عجایب‌المخلوقات»، مدت‌ها آن را نگاه کردم و دنبال یک کاراکتر ترسناک ایرانی بودم. آخر سر این کاراکتر، «افریت»، را پیدا کردم و انتخاب کردم و آن را پرورش دادم؛ یعنی سعی کردم یک چیز ایرانی باشد و از دل ایران درآمده باشد.
🔹
خیلی معتقد نیستم که داستان ترسناک می‌نویسم؛ از عناصر داستان‌های ترسناک برای بیان قصه‌هایی استفاده می‌کنم که خودم دوست دارم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/458128" target="_blank">📅 11:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458127">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krA8VRA69QfG6PPQaIjNj2WPNgTHivK8c8oVAfxpcKuRTfpq8V3-41lGqHRyocIjkM874yLBh3i3CbWh5_yPJTpiuOknL_4WP02QotUXc9-rmvv7T5gEwDllrOKhPP_XhIVH9v9Gd0ziD5ByosWjZfJlk8mJKZUlxDENcMSeZrGVBnicjU9eZ_qV5Q3m7tyoniV5HZCIg9eHK7_Enx2FJ-q9zN09Rwl6O-3FWKD-ZzjZ7sdDcDBQaJoHwSnZHyxdk1MEBr9_rIWPiZWutQA17ffadgGbtY13qSLhSKoO7WquLMVizksq4Ht0u7rQ6mjhNjfunJspO6JrL3a2_pahjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوک بارشی پایان تابستان در راه ایران
🔹
بررسی داده‌های امروز هواشناسی نشان می‌دهد پایان تابستان در ایران با الگویی دوگانه همراه است.
🔹
شمال‌غرب و ارتفاعات البرز با افزایش ابر، رگبار پراکنده و احتمال رعدوبرق روبه‌رو هستند" درحالی‌که شرق، جنوب‌شرق و بخش‌هایی از مرکز کشور شاهد وزش باد شدید، گردوخاک و کاهش کیفیت هوا خواهند بود.
🔹
همچنین ارتفاعات سیستان‌وبلوچستان، کرمان، هرمزگان و جنوب فارس به‌دلیل رطوبت دریای عمان و خلیج فارس، مستعد رگبارهای محلی و رعدوبرق هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/458127" target="_blank">📅 10:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458126">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXq4J0B4G2AOvoIdARhW3Mfozoa82mFn_ZqY0iOBTIEyV0xbrR6Itoo6RJJ4FWXPOi0gQ1MD3ODzSzxpvF6aa8PTCcxD17gVqiLfympNKg7Y7fuSkwvFqoqU2bcNBSuL2M_QT6l5Cbs626AQaBVZbrMkyUoNCWYbnGh1TVGcBZ0js9ZAF14hElDXzIbe1tO3YvLts9_tJZOHmxJPOTyEx5Gu__feRVyP13Thu8SsOyyijQmumknqKPDkbhGuz-rRQq5jrMJK1hEN0S3-xhJr6AYg_qEy8K_DPqPwJXyJdhb4OwtGian-8krrxHLQU5mKGkUnt0Anjax9qJPD7SAxMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایش توان فناورانه کردستان در حضور معاون رئیس‌جمهور
🔹
معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور در جریان سفر به کردستان و همزمان با هفته دولت، از دستاوردها و توانمندی‌های شرکت‌های دانش‌بنیان، فناور و خلاق استان بازدید کرد.
🔹
در این نمایشگاه، محصولات و دستاوردهایی در حوزه‌های
کشاورزی، تجهیزات آزمایشگاهی، سلامت، خودرو و ماشین‌سازی، فناوری اطلاعات، نفت، نیرو، صنعت و معدن
عرضه شد.
🔹
از جمله محصولات ارائه‌شده می‌توان به
پودر ثعلب، فیکسچر دندانی، دستگاه کشت خون اتوماتیک، سامانه هوشمندسازی گلخانه، کربن فعال، بذر هیبرید توت‌فرنگی، تجهیزات هیدرولیک و آفت‌کش زیستی
اشاره کرد.
🔹
همچنین چند شرکت فناور استان، نیازهای فناورانه خود را در این نمایشگاه مطرح کردند.
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/458126" target="_blank">📅 10:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458125">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سوم شهریور روز ملی ارس گرامی باد
#منطقه_آزاد_ارس</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/458125" target="_blank">📅 10:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458124">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/458124" target="_blank">📅 10:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458123">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaBprAFs4X8ZUj1zZxypLZHR_Ps3L9QIHwdvCITmYAcJbSlwLmXNyE9MLCD20L8HRO4Vj16HWd8aR_ctrIwdkaHLaZV9v9vgbCDIEbxoWQ9iSqRcMZlpKLSuydUFzfpY8m_YW4HlSvt_b_6gDG8ZKsnW_8eSlSbsIlhJHmCoIAgNKJPxuLiheahUqYV7JXFVIiyREhLQTT4Scd3d46j-554jb1I_D4zu1cbvyeOq_IMVWIFsya0XKInVDR8-Z1gedE9n2zgUr7HvYfmvZ-g48JRsZTe92szaRN8ZyRguYoFaXThLsnnnjcC0hSp2FdjarqWNMag0B_eSS9wytWXq-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین: با تحریم‌های غیرقانونی آمریکا مخالفیم
🔹
چین ضمن مخالفت با تحریم‌های یکجانبه واشنگتن علیه ایران که افراد و نهادهای این کشور را هم هدف قرار می‌دهد، تأکید کرد که از حقوق و منافع شرکت‌های چینی حمایت خواهد کرد.
🔹
به گفته سخنگوی سفارت چین در واشنگتن لیو چانگ، «تحریم‌های یکجانبه غیرقانونی آمریکا هیچ مبنایی در حقوق بین‌الملل ندارد و از مجوز شورای امنیت سازمان ملل برخوردار نیست».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/458123" target="_blank">📅 10:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458122">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsT_i6dCJ6aF2TzCTELNHZ4GSGKxcbE0VBxp2m2Ptbe9wYQWd5AttEG1rEP6rBv9zOkOBYxOvMZ2C_-qCXaUYhozjv-3E3NldEOjCdfpCrmo2FADT41i3VkNUXzXBfieg5QteajNdzWMwdSujpjJYaUYN5a9G4nEnEAqBBuynAelmTEgtWuxH2zDAVojKSNIAUeGNI6Uawc3Zk3HUtXKixDFNT9oq-BP5NTF1jZnwIJxnMUIPGJQIfTacKS6Yi6rdMu-qcCLB4KccSTWVMCDmjZMTm6gjpgxeN7eBHifM4-yJTkDZMPZjjcypkOG3QgwP3JktcLbOA8J4Y8NEIZpwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
افتتاح نیروگاه‌ خورشیدی ۹۵ مگاواتی در استان تهران
🔹
پزشکیان: انتظار این است در دو سال آینده ۳۰ هزار مگاوات را از طریق انرژی‌های پاک و تجدیدپذیر تولید کنیم.
🔹
با دانشگاهیان و کارشناسان حوزۀ برای کشت گیاهان دارویی در کنار نیروگاه‌های خورشیدی و استفاده از…</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/458122" target="_blank">📅 10:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458116">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFWYNraFy7NG2JWEsj16sheZetmbchZsYfacAlGZLvNr8Zd3HJAKnfTh8n_TG2xhzlnsu_80flZWOFqQqN6TiLekxyXxGXrNmfGEAqAED2oKrABOTLYvgLYQ1j_SPVAHcbsTCO9k-DPbgk2oVHl7tGwArY292H97uDs567Fooz1fDTbTMCZwRjmzjbsDC2S4lEP9mZ1O8nQpVuUToRRXD0psnmELcGkJfe6c8ozqYnZi4ontUyWEtWHWRZi1gJ5KPQN-NVy2yenjJ8mWD4Mw5pCGkUuXEKBaXk8GmoWZppv3Ddil7eEvE142umS5TIvPGCM9z8_Ts0kNwCW45ySrRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RwxVn7uCy4-eKGWZ0DHuxL0pjG_gfPJls5THV33eAb51SFuU4yIfWymDQEtrhPp1vV4hD8f0nQCdRZuKgIWkXzGhJJx-STTaeSxkclv_8-rSHopMpIqr-c6WFTotEAl99p5B5BMLeI0a59pqfW7w58OhFcyGW6STR24MIKJynDxP3ekLou4KeAHxIzBKTGBoE2Mmh19MmE2QoD_AJpFXLTFqNCDx-wRogmOpU9bgKM-B8CGP3vi4T_o0uosVm_EwO-_z-L7B9MkcCCAbgYYTbsVj4WBhXfy5yZjzWYjNtRD1PO_CyV_G5z73_Z8dDhZBC7doKQX3_H7k2AJ3xabs-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iDZpltJynOYUHUMNrtTahXAy8I_gk_jz0h_swlJ1J3dP6G_3ClAU2QRcJAcYAcljkeJBuVyMziCpQ6lK8DQe6Un1njvx7_Vt71enj8jyLuJa4ZzObVfUwjLOcwm_Lwxkzsp8APXWg4D_BRYfqovBUZGXNkKV1yVXEUOpsG-VrPqLX9T80o-Na_YIuZC6ZV8Ba116zzyA8s6M8NNIClwfdQd_tX4WeI_DEUhOMm5gLt4IksfuSwHaEUj9DbMb7m_6AYAAUAZUue101VyKW78Z1ZevdSEYCcxhRiz1zdI7uFMXxK_vsBxD1DSM-DoFcPu5yOAA0Z2Lxjda0eCBcQkvXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s2vlFVFxNBvXHkPLPupr6uuuXZ1gcQjmT7qaHbxxLuA4cgJseL3JJnNtC0851HV_Y3zk7iA5wUNi0-J9epklA6LA7GnBcYVrqy5eGzbnScST7N9AKIga5yOhibq1GjWZGcQbYKhqYQqxQdAGoyPCEqum5-xdxESCTTbGrqx209cIr4zvxPzDESptuEKOmGL5S_eWnWoYab5MVSVhIRX4Pq4uZznmzRXMWbsK5QejcUsMR-Fh2njdcpssvcW_oF3yz4enm8W8iuOsjYo9SbLOGP8rZxTs_PDWsrIYo3y8TWNtOhoNhg1m5apGFBffMsnAbs8NgOzizRbs3XUAxLDE5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZBk-48wPrqlcFQs_S1HVfVOlzW_3OXRGY_ePmtSuGXYtS85yWTIAPI48r8CyOIGbk5P4LKOxEMVYd6cu-T2Oe9yxPhUpMsvrJP_Aq2QKhBDsXnQADVQG_HXVfk8nDbdsQnJkAl4ePM0Mpmi0MngLyQ_SDsWCh7S8starCxxwvucQPrlt7kCYg8F3U4u2mnt0hRW9PI_KAQgHHP0KYmw_4O4Zfn9S1kxRFurXrRjxafFcDsaD9-7ggBoCVYr6xMP2opj-1nTi8Ed78CEjWKT3PVkQWDKow4nB9KuK_0Gzz_jbJ5pn3nf9AgDNa7lxYJLfdDMw-i88IB8GopGJ3oty-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-63KSZXK0x6f5MdtBxHxW7sWHMTGqGo18Habsktc9ZVi2F3mLme2mZ1OZHzadyHqoh42jKLmH18O5nMR89r5ZN3Lu0C-Pt1L5217GKeGTY3WauDPsnR7O6u8fthJNPf-nZlJQ831nDK5fPD1b0M4A8jL750ecFV_O_P5poSUgSOZ8YYhxcd0BSLQkevgbmYTjNsA4uJyQyC9s8Gv8qZ0xB-_yCEQP1kzn0wCGGI17oH2LlgHXgBhdhZdg7QtJXDrvePnt6GfTc1IFnKcGpgr3zUzNE4N_zYi1jKMjN7s3jlwQ7yot62WrfYIh0QpJbIquiY-4fZTsZrFrrdg-naWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">افتتاح ۶۰۰ مگاوات نیروگاه تجدیدپذیر در کشور
🔹
سازمان انرژی‌های تجدیدپذیر: ۶۰۰ مگاوات نیروگاه تجدیدپذیر در قالب ۱۰۷ پروژه در ۳۱ استان کشور امروز افتتاح می‌شود و ظرفیت نیروگاه‌های تجدیدپذیر کشور تا اوج بار سال آینده به ۱۲ هزار مگاوات می‌رسد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/458116" target="_blank">📅 10:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458115">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bab7fd852.mp4?token=RAjPWkLDTz6VDZnbvAAMzz1dH7RcPkgn_W7jRrMZXViT2hlo5Pdrawoxg2f-8E9uONm7WWOjPypT6ThmavMTjVmrOTpLvdH1_36HLatTlcoHyAboObx2TaQfURkexCcq1AkWnq0re_d8FEDPZyR-ADPxUP86nxUxNC5WTSlYLEJRqLaLGgWrdeST3c0-GzBG9rsWzgKE7l2uTfyiZDnAbMHQ_BxkipJo1gV1dXGHpUFzqbdMhISqwP_jE5AoW89mplPFLj1yHBbr3B9MYjbHPq2v4dshZMlHZFiLxyUIr4pAbHJQGRqkjeKJAflZqH07UROAswRVY3gCxJf2mjkRmY5OdjNa6sJLQb3rU5ofadJDti2uWRiJwNs6dYbioyRjh9UfufFj5cIoTnKTnxI-dGPSnDFcQJNsyT4jzS15aO3gAlhGkeyrpZhm4HSgXMcWe-fDbmSOlQpM3TtCRcWAQDerWAM6jcXofpXLm4sIxqRcbYBZka-CTz6F1liF-4Q9emkzaLFtb8Dp_oswl_R5fY11UcquOBQTe_w74Iv_z6gOKlsNB7KmP0HPXvSB-RpGfDXxydJESe9mKOOIXV4bQ8pULSFLp9dB_GQOna0wJdH5ls5I1oMtidPbEdAz_PLqqK10-y7ua9L9zat86VsYVjyUo1Hi7NZvhlF-csrpce0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bab7fd852.mp4?token=RAjPWkLDTz6VDZnbvAAMzz1dH7RcPkgn_W7jRrMZXViT2hlo5Pdrawoxg2f-8E9uONm7WWOjPypT6ThmavMTjVmrOTpLvdH1_36HLatTlcoHyAboObx2TaQfURkexCcq1AkWnq0re_d8FEDPZyR-ADPxUP86nxUxNC5WTSlYLEJRqLaLGgWrdeST3c0-GzBG9rsWzgKE7l2uTfyiZDnAbMHQ_BxkipJo1gV1dXGHpUFzqbdMhISqwP_jE5AoW89mplPFLj1yHBbr3B9MYjbHPq2v4dshZMlHZFiLxyUIr4pAbHJQGRqkjeKJAflZqH07UROAswRVY3gCxJf2mjkRmY5OdjNa6sJLQb3rU5ofadJDti2uWRiJwNs6dYbioyRjh9UfufFj5cIoTnKTnxI-dGPSnDFcQJNsyT4jzS15aO3gAlhGkeyrpZhm4HSgXMcWe-fDbmSOlQpM3TtCRcWAQDerWAM6jcXofpXLm4sIxqRcbYBZka-CTz6F1liF-4Q9emkzaLFtb8Dp_oswl_R5fY11UcquOBQTe_w74Iv_z6gOKlsNB7KmP0HPXvSB-RpGfDXxydJESe9mKOOIXV4bQ8pULSFLp9dB_GQOna0wJdH5ls5I1oMtidPbEdAz_PLqqK10-y7ua9L9zat86VsYVjyUo1Hi7NZvhlF-csrpce0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیرعامل شرکت ملی نفت، جواب گزافه‌گویی وزیر ترامپ را داد
🔹
صبح امروز وزیر خزانه‌داری آمریکا ایران را به تحریم سنگین تهدید کرد، حالا مدیرعامل شرکت ملی نفت ایران می‌گوید، هر اقدامی که انجام شود، برای آن راهکار پیدا خواهیم کرد و نگرانی نداریم. @Farseconomy -…</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/458115" target="_blank">📅 09:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458114">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f78e8b1f.mp4?token=Es7fYUxfRtetZshWe3r_b6nLZgC1C2jcfuS2oCHuIVROydQ-32jp8AVIflug8itFyhp8RVhvukjY5VyyBULm3gJwJFZVhCvb09rU3to5Y3VSkS6HwL0lN7ZxNQXKK9dp-r0auO_dvOgg6hImX7orCWi9TDq8P8sas4vtUYqTXJJN2tx54mRMcxcQwLyj1_piPttnNIUxJhJBLGRkA6PQH-IVlxrr5iEXZ2GHVU0cw5Z-7T9kJcAm2KWhUmsBEljwcbhb_eGvCF4C5VbgEVJCbwmfEnwi19cSFuNVfsJpEuDR3-tFMiW7ixZ18obObC_DV3tFsiLu8GSmxpESLFaC7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f78e8b1f.mp4?token=Es7fYUxfRtetZshWe3r_b6nLZgC1C2jcfuS2oCHuIVROydQ-32jp8AVIflug8itFyhp8RVhvukjY5VyyBULm3gJwJFZVhCvb09rU3to5Y3VSkS6HwL0lN7ZxNQXKK9dp-r0auO_dvOgg6hImX7orCWi9TDq8P8sas4vtUYqTXJJN2tx54mRMcxcQwLyj1_piPttnNIUxJhJBLGRkA6PQH-IVlxrr5iEXZ2GHVU0cw5Z-7T9kJcAm2KWhUmsBEljwcbhb_eGvCF4C5VbgEVJCbwmfEnwi19cSFuNVfsJpEuDR3-tFMiW7ixZ18obObC_DV3tFsiLu8GSmxpESLFaC7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فداکاری یک خانوادهٔ آتش‌نشان آن‌ها را زائر امام رئوف کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/458114" target="_blank">📅 09:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458113">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vz3oXd0aCTjs5dsOWR3j9x3siH8L5Sm1q2xmrEUvdBLJPNLnwLJ0-4pe23NzdQgz9J1xko5w8EWDM42KHnx6lU33akH3Kfx14zFuoLzaOWlYUxUF4ZKlZMjCEF8kODmvfVL4aB-hMxhhU7OjTLkBufVzNdJs-XHLEfaFuxpZbRHHTOkGy2J1UvpsGbrS_wgKGtuukB2suh9j1mCrKfRWOGdLXz9odqca5-94DJpo29Ub_71U6sZ9QGk53t6MhNwCyf0HLBuih7NwuHxXspaLN0GACXLpmHzDGQMp8Rfvon7fnGMeiUvrL_7VSpxPAR5sdUrkIPaKOVvaewlnv-JHlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاح ۶۰۰ مگاوات نیروگاه تجدیدپذیر در کشور
🔹
سازمان انرژی‌های تجدیدپذیر: ۶۰۰ مگاوات نیروگاه تجدیدپذیر در قالب ۱۰۷ پروژه در ۳۱ استان کشور امروز افتتاح می‌شود و ظرفیت نیروگاه‌های تجدیدپذیر کشور تا اوج بار سال آینده به ۱۲ هزار مگاوات می‌رسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/458113" target="_blank">📅 09:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458112">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af37209889.mp4?token=jSmXCjPvv9xjQDK4Ir0nL_5quYalU4PMfd9jh_HjJ70MEbMH3sNVeM47yd7SEcZEJULKWPBFpgVsKESFFiip7RsuyMiZyw7zzEuGlHsHVmzG8aCVnKosrSMATd4KL5BDqHcmFzDFLn_RtyyJR-238Gkw5Z_HF-QEHaMPxnbVqDS3XOFozHX1tzu6qObmVIDjORnL7Qio85u3Ci_WfieOPp805PmWy-22S941PbfAwU6lX3LmNF2CLTcFqS-Ut_UkH568RlBnKYDmCJjD4D_NphGXomBJC5lfPpueS4txoMZYkZDv_vzo9XMFLiE9rEBiH9uoMBQ1VcBi5CKymCrwApqdsub6bHZhZ--aQqQLBFEJ2NRtjERzZW6v-yCq90u50Ja12LboIc7DNtKxyIf-B2vyfLAAARlM0Rb79U_cxqJ6SPICPKjp2oL9q4wgIbpWiCFcS40WjTHOgE3J6BMC9ZRF0mv_RVCvvy8VmlNCxQHYVl7Sf5Rz5bryPD9fceAx2Arwr-KTmvsQt7BWat5xY7-smERZG34xJJ-DcAOo47QPs028upplsIpWXAKpcS5tPPHLR54pXQ9IjUQejn6dFgEHOEm6hfIxXwSDjvawSyuw5Pm9VhUFiXF6QGg9nYi76zpT6eet5foA8ec-U5IoFZ7lragzLBftETZC_sqXcPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af37209889.mp4?token=jSmXCjPvv9xjQDK4Ir0nL_5quYalU4PMfd9jh_HjJ70MEbMH3sNVeM47yd7SEcZEJULKWPBFpgVsKESFFiip7RsuyMiZyw7zzEuGlHsHVmzG8aCVnKosrSMATd4KL5BDqHcmFzDFLn_RtyyJR-238Gkw5Z_HF-QEHaMPxnbVqDS3XOFozHX1tzu6qObmVIDjORnL7Qio85u3Ci_WfieOPp805PmWy-22S941PbfAwU6lX3LmNF2CLTcFqS-Ut_UkH568RlBnKYDmCJjD4D_NphGXomBJC5lfPpueS4txoMZYkZDv_vzo9XMFLiE9rEBiH9uoMBQ1VcBi5CKymCrwApqdsub6bHZhZ--aQqQLBFEJ2NRtjERzZW6v-yCq90u50Ja12LboIc7DNtKxyIf-B2vyfLAAARlM0Rb79U_cxqJ6SPICPKjp2oL9q4wgIbpWiCFcS40WjTHOgE3J6BMC9ZRF0mv_RVCvvy8VmlNCxQHYVl7Sf5Rz5bryPD9fceAx2Arwr-KTmvsQt7BWat5xY7-smERZG34xJJ-DcAOo47QPs028upplsIpWXAKpcS5tPPHLR54pXQ9IjUQejn6dFgEHOEm6hfIxXwSDjvawSyuw5Pm9VhUFiXF6QGg9nYi76zpT6eet5foA8ec-U5IoFZ7lragzLBftETZC_sqXcPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ فروش محمولهٔ نفت آمریکایی به نفع بیماران پروانه‌ای
🔹
رئیس شعبهٔ ۵۵ دادگاه حقوقی بین‌الملل تهران از اختصاص بخشی از اموال توقیف‌شدهٔ آمریکا به بیماران ایرانی خبر داد و گفت: براساس حکم صادرشده، ۷۷۱ بیمار که علیه دولت آمریکا دادخواهی کرده‌اند، در اولویت دریافت…</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/458112" target="_blank">📅 09:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458111">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">صدور حکم سارقان سوخت هواپیما در هرمزگان
🔹
رئیس دادگستری هرمزگان: حکم قطعی محکومیت افرادی که با سرقت از خطوط انتقال سوخت هواپیما، اقدام به قاچاق آن می‌کردند، صادر شد.
🔹
۲۲ دی ۱۴۰۳ یک انشعاب ۲ کیلومتری که از طریق آن سوخت هواپیما سرقت و پس از آن قاچاق می‌شد شناسایی و پس از دستگیری متهمین، فرآیند رسیدگی به اتهامات آنها در دستگاه قضایی استان هرمزگان آغاز شد.
🔹
متهم ردیف اول به‌نام یوسف زارعی فرزند محمد، بابت اتهام مباشرت در تخریب عمدی تأسیسات عمومی شبکه فرآورده‌های نفتی موسوم به خط لوله ۱۰ اینچ فرآورده‌های نفتی به ۱۰ سال حبس تعزیری و بابت اتهام مباشرت در قاچاق حرفه‌ای و سازمان‌یافته فرآورده‌های نفتی سوخت ATK به تحمل ۲ سال حبس تعزیری، ۷۴ ضربه شلاق تعزیری، منع اشتغال به حرفه مرتبط به‌مدت ۲ سال و پرداخت ۱۴.۴ میلیارد تومان جزای نقدی محکوم شده است.
🔹
متهم ردیف دوم پرونده مهدی برسم فرزند حسن نیز بابت اتهام معاونت در تخریب عمدی تأسیسات عمومی شبکه فرآورده‌های نفتی موسوم به خط لوله ۱۰ اینچ فرآورده‌های نفتی به پنج سال حبس تعزیری و بابت اتهام معاونت در قاچاق حرفه‌ای و سازمان یافته فرآورده‌های نفتی سوخت ATK، به تحمل ۶ ماه حبس تعزیری، ۷۴ ضربه شلاق تعزیری، منع اشتغال به حرفه مرتبط به‌مدت ۲ سال و پرداخت ۵.۷ میلیارد تومان جزای نقدی محکوم شده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/458111" target="_blank">📅 08:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458110">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تقلای ترامپ برای ازسرگیری مذاکرات با ایران
🔹
شبکه خبری الجزیره به نقل از یک منبع آگاه خبر داد رئیس‌جمهور آمریکا دونالد ترامپ هفته گذشته با فرمانده ارتش پاکستان، عاصم منیر، به صورت تلفنی گفتگو کرده است.
🔸
به گفته این منبع، ترامپ در این تماس، درباره پرونده…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/458110" target="_blank">📅 07:56 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458109">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzeliqmS2IJEUHoYP84lsBsSKXQhHZTr4qfAMhknEC4G1dBbmKwx9-17ajbWb6d4T31HfuHkIvl7eUBJXXlAswYMxv9TxVFcBAX__BrTDnIGR8e8wtqeduOS-in_K4puOSxFF2kLCi_Ad9PD4tD2r8agtlagxs8TUK7EAA-Zagor53SHDysxQ3yLZpYsnuggR8ubyGFGjpLWM31tMu1Ac9WiCDJo4PPmwzL8EzmU7oaOJo_kS_aT9J7m6gDv_fYfdMa-gXXaJ89aoIbvDBV0k0Qu7lTx_jbPQH6XZEUZSP7A0jmdFP-PyqiCXCALNQzO5_96U-O7UmDzkgJiAOLGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روشن را دیدید، تلویزیون را خاموش کنید
🔹
«آقا پخش می‌کنیما». «بکنید». این دیالوگی است که بین حسن روشن، فوتبالیست پیشین تیم ملی و استقلال و مجری یک برنامۀ یوتیوبی ردوبدل شد. درست بعد از آن که روشن تصویر کارلوس کی‌روش، سرمربی پیشین تیم ملی را دید و فحشی جنسی و کش‌دار داد. او لحظاتی بعد همین را برای ریکاردو ساپینتو، سرمربی استقلال نیز تکرار کرد.
🔹
روشن تنها بازیکن ایرانی است که در تمام تورنمنت‌های مهم فوتبالی برای ایران گلزنی کرده. جام جهانی (۱۹۷۸)، المپیک (۱۹۷۶)، جام ملت‌ها (۱۹۷۶) و بازی‌های آسیایی (۱۹۷۴). او به همراه ایران قهرمانی جام ملت‌ها را هم تجربه کرده و در استقلال هم به قهرمانی رسیده.
🔹
بااین‌حال چیزی که این روزها از روشن در اذهان دنبال‌کنندگان فوتبال مانده، اظهارنظرهای تند، عجیب و غریب و حالا توهین‌آمیزش است. او در این سال‌ها مخالف حضور بازیکنان و مربیان خارجی در ایران بوده. مخالفتی که البته فارغ از درست یا غلط بودنش ایرادی به آن وارد نیست اما روشن حالا پا را فراتر گذاشته و رو به الفاظ رکیک آورده است.
🔹
او با چنین سابقه‌ درخشانی در زمین چمن، بیرون از مستطیل سبز دارد تیشه به میراث خودش می‌زند. وی البته تنها کسی نیست که در این راه قدم می‌زند؛ پیش‌تر خداداد عزیزی، قلیچ و فنونی‌زاده نیز با دُزهای متفاوت با اظهارنظرهای غیرعادی در فضای مجازی خبرساز شده بودند. سؤالی که پیش می‌آید این است که چرا پیشکسوتان به‌جای ارتقای دانش فنی و حضور در پست‌های مدیریتی یا مشاوره‌ای، به کارشناسان حاشیه‌ساز و پرخاشگر تبدیل شده‌اند؟
🔹
سال‌ها ارکان فوتبال از لزوم فرهنگ‌سازی روی سکوهای ورزشگاه‌ها گفته‌اند. اما چه توقعی از نوجوان پرحرارت استادیوم می‌توان داشت وقتی پیشکسوتش چنین ناسزا می‌گوید؟
🔹
برنامه‌های یوتیوبی ثابت کرده‌اند که برای هنجارشکنی، بیشتر از یک تحلیل فنی ارزش قائل‌اند. برای همین است که پس از حرف‌های روشن گل از گل مجری می‌شکفد. او می‌داند همین تکه پربازدیدترین بخش برنامه‌اش خواهد بود.
🔹
حالا دیگر وقتی روشن روی صفحۀ تلویزیون یا برنامۀ اینترنتی ظاهر می‌شود، تنها توصیه‌ای که می‌شود کرد این است که کنترل را بردارید و خاموشش کنید. چون جایی که یک پیشکسوت گل‌زن، به یک فحاش تمام‌عیار تبدیل می‌شود، دیگر ارزش تماشا ندارد.
@Sportfars</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/458109" target="_blank">📅 07:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458108">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMIsdrsBc5tPqtSiHNZexVK8rIle_Bu7J3Cf3VEMI-0VGwyuRIg1DvjCAFB0svh38DZIW4nVphuZZEKoORNkpZpTfCxfaOhKLtT5WAXrH_vZoM9ZtaqoDrQQuP_HUAPOfB9N6D71AU-rZG8pWlzQwaqAhbPm3QgIltN0g1TF5_IKw8jr9YBg3UYhZS58L9nILJvEf9CFNBd8JMmAnjj9-Ynd3PKtnTPrQsvzU19ZTPbOZkz58Z8F_6AJwCNIZ6XnEUPE8ZXwMdL9gr2hFecFdfVt92-qdejKBzjVsJBYFz0upGNXfUmGgrIul-dyQPuHJNpbE_IDB3xyaBLtEyAN_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقاب اصفهانی امروز به شورای شهر می‌رود
🔹
سخنگوی شورای شهر تهران: در جلسۀ سه‌شنبه، معاون رئیس‌جمهور و رئیس سازمان بهینه‌سازی به ارائۀ گزارش درخصوص برنامه‌ها و اقدامات انجام‌شده در حوزۀ مدیریت مصرف بهینۀ سوخت در شهر تهران خواهد پرداخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/458108" target="_blank">📅 07:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458107">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">طرح مقابله با نفوذ بیگانگان، در دستور کار صحن علنی امروز مجلس
🔹
سخنگوی هیئت رئیسۀ مجلس: ادامۀ رسیدگی به گزارش کمیسیون امنیت ملی مبنی بر مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در دستور کار جلسۀ سه‌شنبه صحن علنی مجلس قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/458107" target="_blank">📅 07:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458106">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آمریکا روادید ۲۰۰ هزار نفر را لغو می‌کند
🔹
طبق اعلامیۀ وزارت خارجۀ آمریکا، واشنگتن قصد دارد ۲۰۰ هزار روادید تجاری و گردشگری که خواستار پناهندگی در این کشور شده‌اند را لغو کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/458106" target="_blank">📅 06:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458105">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca58c6482a.mp4?token=JJksclH5zLAlOu4Y--gjAuRIMbRAvfG4Oq1Yb29K6kBvcQDqXxRjEYg139BxbogyCAkdEECUgeQSdeOWQ6KF6V6DK7t1pomV6VD3ygW4d_8NyIq6bkbNNtFDftPh6kViawwoek9yLe4T77BRRklnEZCLn6feVlsmh_DaOYEss652hNE9cx1Eqg_erxC58mL9AL00nNeAMikiAGLorGImyPBO9v36qeg86CceGtfjlOm-j6AtuJhj3WmLWjNnIamPDVjKCDJchR03JH6X0BMoCzOsH1DBFwjaKvjQH1LRA771WJzRfZdZ6UyeuAloAxxG9VvfCzXumpcLg36UYRCsaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca58c6482a.mp4?token=JJksclH5zLAlOu4Y--gjAuRIMbRAvfG4Oq1Yb29K6kBvcQDqXxRjEYg139BxbogyCAkdEECUgeQSdeOWQ6KF6V6DK7t1pomV6VD3ygW4d_8NyIq6bkbNNtFDftPh6kViawwoek9yLe4T77BRRklnEZCLn6feVlsmh_DaOYEss652hNE9cx1Eqg_erxC58mL9AL00nNeAMikiAGLorGImyPBO9v36qeg86CceGtfjlOm-j6AtuJhj3WmLWjNnIamPDVjKCDJchR03JH6X0BMoCzOsH1DBFwjaKvjQH1LRA771WJzRfZdZ6UyeuAloAxxG9VvfCzXumpcLg36UYRCsaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملۀ مجدد اوکراین به یک پالایشگاه نفت در روسیه
🔹
هواپیماهای بدون سرنشین اوکراینی  پالایشگاه نفت شهر «آفیپسکی» در فاصلۀ حدود ۳۰۰ کیلومتری خاک روسیه را هدف قرار دادند.
🔹
این پالایشگاه در حملات قبلی اوکراین نیز هدف قرار گرفته بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/458105" target="_blank">📅 06:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458104">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iyloew-D0oIGxV8QWTaiswdMPXvD698WqqmVxtffqoqlGkW8dKuCMYV98dD8FT8uITA0eBfhLiy4C6vqYBcJnwrqcOH9nYNUFveKySdPWMSChlcMsm4T8Vz1dqPbswfuBWSUtroex_4cf9qq32t2qMxDOFsKXdUU1OHR7JRLOHhygu2tlac5wgubtmPeiprfGflL5Ohm_ujVQnXXW7ezY-nklnM6Ur3lcy3G-wcSFRUWW0wm2uCGhpHZfgjxLMaOf8UyfFgREzK7AfpvH9ALpbpUK7fxF9qAJIe1fICTLdzDevLV4BnRQsxFtgp-BkSY-d29hi0tY3OUidyc1HvLvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌رسانی با سرعت کبوتر
🔹
بعد از سال‌ها رقابت برای سریع‌تر شدن اینترنت و پیام‌رسان‌ها، حالا اپلیکیشن‌هایی ظهور کرده‌اند که دقیقاً خلاف این مسیر حرکت می‌کنند؛ پیام‌ها را عمداً با تأخیر به مقصد می‌رسانند.
🔹
در یکی از این اپ‌ها، پیام با یک کبوتر مجازی ارسال می‌شود و سرعت رسیدنش به فاصله واقعی میان فرستنده و گیرنده بستگی دارد. یعنی هرچه مقصد دورتر باشد، باید بیشتر منتظر بمانید.
🔹
اپلیکیشن دیگری هم از حیوانات مختلف برای ارسال پیام استفاده می‌کند؛ حتی حلزون! هدف، تبدیل انتظار از یک مشکل به بخشی از تجربه پیام‌رسانی است.
🔹
پشت این ایده عجیب، یک هدف جدی‌تر قرار دارد: کاهش فشار ارتباطات فوری، اعلان‌های دائمی و انتظار برای پاسخ سریع. این جریان بخشی از موج «پیام‌رسانی کُند» است؛ جایی که گاهی کندتر بودن، خودش یک قابلیت محسوب می‌شود.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/458104" target="_blank">📅 05:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458103">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86fa6d752a.mp4?token=YXKJamWPmqrCHPQMZ6HBtMGnm0TS-ZzjiFRnV_aF0NNzM2V5Y4G_yu5e99XT5Qoqf1n4syMaMLH5a4y7aTYr6cGWhqBv-lZbpZA6CirISiwAWae6w8vkD_dl_Y4UKc1qwJ1GWLRNgUxbJW89lLWeCF6Ex-Ihq1K7Kl7li6a_BBMo8tmw1xDc55Ekt67Q1pqWKI7ayaomNSXCRZQxXPYMJCYt_T98oEWQHCH7ensKvbom-5Gyr0Q0JUqk5ghyVWGKBTi93XkxqY7pNOqMtuZreVw7gq13rXc3lTD4k9G1C7CyTWlhXx4X8PlnN6t-UTMONmziF0a5LUZ2JC7-6Sqvxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86fa6d752a.mp4?token=YXKJamWPmqrCHPQMZ6HBtMGnm0TS-ZzjiFRnV_aF0NNzM2V5Y4G_yu5e99XT5Qoqf1n4syMaMLH5a4y7aTYr6cGWhqBv-lZbpZA6CirISiwAWae6w8vkD_dl_Y4UKc1qwJ1GWLRNgUxbJW89lLWeCF6Ex-Ihq1K7Kl7li6a_BBMo8tmw1xDc55Ekt67Q1pqWKI7ayaomNSXCRZQxXPYMJCYt_T98oEWQHCH7ensKvbom-5Gyr0Q0JUqk5ghyVWGKBTi93XkxqY7pNOqMtuZreVw7gq13rXc3lTD4k9G1C7CyTWlhXx4X8PlnN6t-UTMONmziF0a5LUZ2JC7-6Sqvxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیرالمومنین(ع): کمک کردن به نیازمند را به فردا نینداز
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/458103" target="_blank">📅 04:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458100">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qCPUqEyGooJ4ZxZULgOrdzRnUidbpO_VvxpG5DX8GdOJPbY_Rx-249Fu3HEpUwHI7gKbKR18CIX0OOWs3piFv9rxol-3lbs48hAMLz0qIKCiECVjhpiZZhuHUyeKQDkAqEZnxiFUyudGNyxFGu-aXOOYxJeVAG4Qq3p_yJjWRV1hi03aUalY3ZWWTHJOkiRsqJyTEpuYJk3yMKPdxOi6JwK0Zj6WxHcTJ_tqLpE8U9lLqUiHNae0i5v8Sy5GfqOvnUB2xuo3RScAP1JgnCvBydqPinisgZ8ghfribAJgTWqOkKgmWtFP1h107IpCvhEDmGLtlzVbKnUXu0l3m5N3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7oVcx6ynl0DDe7nZC0zid-9yb7iNIJuf47LkgGfEH6xEebEQJcKyA86Y-vPaHQywNV1ie1fKwDJZFq9KYmb41wa7q4oPSjECWUEvY7B1JXd2auZB-uoip3r5lssGOsAWZ2un-7wENF4yKZEeWT6J8zLGod5w1X0-WZ8LtGe46MjdyxXlxj5vJSFRWlALf2gMpu71v-i4zBVJwy12WLVF7EN8JwNudkDtSEnsZxepfRTaCvQMmNDFh5ByVOQZmrC4LlonHuIAfnSnvIyHmwUZ0bJWfA03XyfaM07cKPgdOvJcPy9cG11-qMXxCWrHryfj4zVo5pCWjzct9ruwFoddA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qg2MCQjIdxypLFLV1FFatD4jjDpFt6Dm9_cL4yqsltGM66BeqBBnVa1cSiyDbd1jXZw_GGgd4aT4dMx_2iJTeh8Or9vq7AkYgVBzNRbBHgnXGCMP1sAqPQPziCa6QSkmdfTIjVArYhCv4NOm7lItXNozGt7QvWlXhjeOqoIbKStH6PefEZLEk00s78iC1OCiBSsRj1DbffiyCPiU-B-YjtJy8gsiS738frP0MQ1c0CEVnl1FZmdXXapik7YLou9Y6MO4D3hNdkm4Tft7Xs7LkWgptunCjcVpa6ufeMDkV3dpzHOzfMRfGqngocIjydggi7Wkv8-DM5UDYgjBwrdKKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شب‌های پل خواجو
عکس: امین علیجانلو
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/458100" target="_blank">📅 03:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458099">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حملات صهیونیست‌ها به جنوب و مرکز نوار غزه
🔹
المیادین: خودروهای نظامی اسرائیل در شرق شهر خان یونس در جنوب نوار غزه آتش گشوده‌اند.
🔹
صهیونیست‌ها به‌سمت چادرهای آوارگان در شرق شهر حمد، واقع در شمال غربی خان یونس، تیراندازی کردند.
🔹
اردوگاه‌های «النصیرات» و «البریج» در مرکز نوار غزه نیز هدف آتش خودروهای زرهی اشغالگران قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/458099" target="_blank">📅 03:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458097">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jcvb-k-ozV9AyO0bS5-c8PxE_L3KNUWCgDysPW6JQH5wknRD6AP345I0Vcsu27j1ZU5DH3ULYXB7NSB48Pe_jOzZUaq3eg3I_pXuDRHUB2BrGam7CQ1o8LFtL0igyriJru2zZtNNzrxZHCsVhz3RZRQMoKHuHtpGWTM1H1Zf4EbbRVlVWeavaRb6nDQsdHM5AGPhjRbofpjoKitYTtAevrFsDWajhCoP4mAlcv02bMek8srb33gwZFFvx2DPjf3k8fsbsMUKdeZjgPFxxVYkrQxXbYtcrD9KLIgESAsY6j9aJUxLW0-P2Fe6r3mWsr2gvKm9-TbCTX_qQaVNpBETVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کلوچه‌ از بطری پلاستیکی ساخته می‌شود
🔹
پژوهشگران با کمک مخمرهای مهندسی‌شده، پلاستیک «پی‌ئی‌تی» را به ترکیباتی تبدیل کرده‌اند که می‌توان از آن‌ها برای تولید موادغذایی استفاده کرد.
🔹
این مواد در آزمایشگاه با ترکیباتی مثل فیبر و نشاسته ترکیب و با چاپگر سه‌بعدی به شکل کلوچه درآمده‌اند.
🔹
هدف فعلاً تولید غذای روزمره نیست؛ پژوهشگران به کاربرد این فناوری در محیط‌های کم‌منبع مثل مأموریت‌های طولانی فضایی، زیردریایی‌ها و مناطق بحران‌زده فکر می‌کنند.
🔹
البته هزینۀ فعلی تولید بالاست و این فناوری هنوز در مرحلۀ آزمایشی قرار دارد؛ اما ایدۀ اصلی عجیب است: تبدیل زبالۀ پلاستیکی به بخشی از زنجیرۀ تولید غذا!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/458097" target="_blank">📅 02:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458096">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B68u9o__k7hxoORU_HcMt2YmDlh3DJd5XgIMmTP_3QT_RRId6wVhfGKLupEeKbqmLOo630SHYNueHnVSS880LUGoImjFMm_xPhxChuenly7V1fKhO6j2uDAl7K9rD2KlWRqKPSMUFKlUWXBRFh7hbmKqkO4jcoe13KQcmHh3Tcv8-Yp5_pfCFPM4aDK98ofP84E7Xp_ZY2NY13VVUB1180pe7MvCJDoJjgA1O0QNxQ39hnjhmKsMBJeKXcsYQ_4yJlCF0LOaM2OW43Im8OvaIKVb8U91u9X_dpu6Lg6hmIkx5bdROQOmhlM2Rd3HdZt0zSrbPCm8GSkSg44HV1i14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هدف قرارگرفتن یک نفتکش در تنگۀ هرمز
🔹
سازمان عملیات دریایی انگلیس: یک نفتکش در آب‌های ۱۷ کیلومتری منطقۀ «الشیشه» در شمال عمان، مورد اصابت یک پرتابۀ نامشخص قرار گرفته و موتورخانۀ آن از کار افتاده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/458096" target="_blank">📅 01:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458095">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آمریکا تحریم‌هایی را علیه ایران اعمال کرد
🔹
وزارت خارجۀ آمریکا اعلام کرد که تحریم‌هایی علیه «مقامات نظامی و شبکه‌های ایرانی دخیل در تهیۀ سلاح و حملات سایبری» وضع شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/458095" target="_blank">📅 01:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458094">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ادامۀ حملات رژیم صهیونیستی به جنوب لبنان
🔹
توپخانۀ اشغالگران، ارتفاعات علی‌الطاهر را برای چندمین بار در روزهای اخیر گلوله‌باران کرد.
🔹
همچنین شهرک المنصوری، حومۀ شهرک‌های میفدون و صربین، و منطقۀ دوحه كفررمان نیز هدف حملات توپخانه‌ای اسرائیل قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/458094" target="_blank">📅 01:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458093">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b225fc7a.mp4?token=RWy_nLyOdqUeL1hz4KVTjvKM__50SFQVyFUoZeoawaNivqrVi6Q1TujjwsdAwTH60WN_Lpels0pkDpor1ls4eBIbeh1RAtbyOCdyv3pAWP_Tj67plzHbpnlQTPGgR5eW6kKMFXYortb51cfHp2BU5nqYDS-ULROVd4Dr4ildPo9ybeUQdJmvomKzr0okwI2hsp6zEWTJAZ1izxLDC1tNKCfIx20t1yK2N2CSMaBC8Z06NTN6t-fa0RxzP0qeLvGfLY9wJfsUK0ZfgIrnCsZ-BMlnPHa30Ikw4y-TlnUj_ZkJ8OIcj97FbrdrYwZAl_UIV-xxz3hnJZxhV-IyfxHJP5DLNA2G_L3UWI4zrYA9LywIq3TWU7Op-A7GDAQ6X0mkJuAquJu-7Prcwp8JplJpOjLLUonlqJEBgpKxVvNLlAR8aBbpdb3Wou3mBSaNvCrUq1_UZf2K8nIKVhTf5cXnuW6-5PipLpUh2CAfCdxHpqSeGxi2WQ-vEC8cpjjBHnI9wUjhv1scajtov_r3sYm9_xl6S_zcJ9eUPNZQZHG1KnxfcWANupbgLwqRc76M4ffZ3i43pW3zbctaekqyes-UJZYoBDfknBlXZg9E-rz5c42ubnTQ9BPiFgZD1CC9jcUCzbx24wU80j7GSogvpxjpaCZkE3d9kW5miMtqKKiMg-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b225fc7a.mp4?token=RWy_nLyOdqUeL1hz4KVTjvKM__50SFQVyFUoZeoawaNivqrVi6Q1TujjwsdAwTH60WN_Lpels0pkDpor1ls4eBIbeh1RAtbyOCdyv3pAWP_Tj67plzHbpnlQTPGgR5eW6kKMFXYortb51cfHp2BU5nqYDS-ULROVd4Dr4ildPo9ybeUQdJmvomKzr0okwI2hsp6zEWTJAZ1izxLDC1tNKCfIx20t1yK2N2CSMaBC8Z06NTN6t-fa0RxzP0qeLvGfLY9wJfsUK0ZfgIrnCsZ-BMlnPHa30Ikw4y-TlnUj_ZkJ8OIcj97FbrdrYwZAl_UIV-xxz3hnJZxhV-IyfxHJP5DLNA2G_L3UWI4zrYA9LywIq3TWU7Op-A7GDAQ6X0mkJuAquJu-7Prcwp8JplJpOjLLUonlqJEBgpKxVvNLlAR8aBbpdb3Wou3mBSaNvCrUq1_UZf2K8nIKVhTf5cXnuW6-5PipLpUh2CAfCdxHpqSeGxi2WQ-vEC8cpjjBHnI9wUjhv1scajtov_r3sYm9_xl6S_zcJ9eUPNZQZHG1KnxfcWANupbgLwqRc76M4ffZ3i43pW3zbctaekqyes-UJZYoBDfknBlXZg9E-rz5c42ubnTQ9BPiFgZD1CC9jcUCzbx24wU80j7GSogvpxjpaCZkE3d9kW5miMtqKKiMg-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سربازی بیرانوند باز هم به تعویق افتاد؟
🎙
سخنگوی فدراسیون فوتبال: نامه‌ای روز گذشته به سازمان لیگ رسید که در آن قید شده بیرانوند تا ۳۱ شهریور معافیت دارد اما کارت بازی او چنین بحثی را تفکیک می‌کند. آخرین کارتی که برای بیرانوند صادر شده تا این زمان را پوشش می‌دهد.
🎙
بااین‌وجود یک اما هم وجود دارد. اگر استعلام دیگری از مقامات ذی‌صلاح به سازمان لیگ بیاید، آن کارت به‌روزرسانی می‌شود و وی می‌تواند تا زمان جام ملت‌های عربستان و نیم‌فصل در باشگاهش بماند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/458093" target="_blank">📅 01:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458092">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcxSWKQHXGNtNbcbPNMsEEq8O2-aANsxuJnaXtrJgoBa35S5BS0oaEP9lE0g27fe0BtYPK6CF613B8bsbsFuw-LTrHCQIHjjOLoGF-eo1ydxenvcQa1jFOmLHFh4kgJnpfry_EdwFELVNAyi04edwTMR7bynZLWrhAQ9XhwKj8WlcuDL590j7zh-W3sD1XyK_CCN0d5zhitfRUrzLN4HiznktNsoWs4SS3e7_wSVEfLj5DO5Wst9YLEzSjXqjhOmbyMVXQ95wu0z-Zsd6VIrGsT6pPx0haIWPE50rCMDCMIETrAXBBh-2gzSL5EdinXAlD0E_SQJp_4DXYu1hs9c_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
زاکانی: تغییر چندبارۀ رویکرد جنگی آمریکا بهترین اعتراف عملی به شکست پروژه‌های قبلی در جنگ با ملت ایران است
🔹
در زمین نظامی شکست خوردید. در زمین محاصره به اهداف‌تان نرسیدید. در زمین اقتصاد هم بدتر از گذشته شکست خواهید خورد!
🔹
دست و پا نزنید. خروج از این باتلاق امروز کم‌هزینه‌تر از فرداست!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/458092" target="_blank">📅 01:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458091">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9287a378d3.mp4?token=v0Z7daxlVR3wC6y0CK1ik6rhN-zS1jX3blwM7Um8TbR8CH5gG6B5roU9p6E6NjZK-Qldv9Jk1xjzevb-GqAELvIf_XZ514sffWHz8-DjgIdSFGbtwsv0bwczdQpctbOUL01mABEqyQzl9ONkVvCZ3k5KkLT0HchkCoCyxRMgWwlBj2vlTwmAlP2Hk13JPWo0D-7_yRqE0rEUy_z00mta0x-Mgh4wt5Z_SsRRjr-GE9XG_l6uYdsJV7LSu-DVX_ftriVrKetjIlyNWzCALvn5VqZib3nLziefM7af5U-miqvLDgi9AwNmrA8YF390qKxITJYqNT30gbnsbpfc_o4RzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9287a378d3.mp4?token=v0Z7daxlVR3wC6y0CK1ik6rhN-zS1jX3blwM7Um8TbR8CH5gG6B5roU9p6E6NjZK-Qldv9Jk1xjzevb-GqAELvIf_XZ514sffWHz8-DjgIdSFGbtwsv0bwczdQpctbOUL01mABEqyQzl9ONkVvCZ3k5KkLT0HchkCoCyxRMgWwlBj2vlTwmAlP2Hk13JPWo0D-7_yRqE0rEUy_z00mta0x-Mgh4wt5Z_SsRRjr-GE9XG_l6uYdsJV7LSu-DVX_ftriVrKetjIlyNWzCALvn5VqZib3nLziefM7af5U-miqvLDgi9AwNmrA8YF390qKxITJYqNT30gbnsbpfc_o4RzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین مرگ‌بر آمریکا در رواق دارالذکر حرم رضوی، و مزار رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/458091" target="_blank">📅 00:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458090">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOnMkmdPqM2rJQI2piBviTYXL8VtfrVHQiZWMqGotaOFTA56wdMl9lNfeg_nTPvLlXdXI9AbFhlJYcSXq7FPVG3Cs6bUbJjbnKGcPNDhMUq6X5xamzSlaGx-12yEG1IYcCwWUTsXINihuWChTmlus89yPd5U7EELHqzbNHchTG53ESsZK6ySfJ_AYRcb5BSu0jE36Ow2D-E1VWImeV-QfIhUymcE64COVNjslnxer-eqqJktOhLSCsZQR6ru7Nzkyf93FOh4kIyySDBZZ7rQWGCc5puN95mz-2HxQRsWSysae-a5AkGRdHbBuduLTzimTLWGLWc491qX6gk3i382Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور: مشکل ما مصوبه نیست؛ مسئله اصلی اجرای مصوبات است
🔹
قائم‌پناه در سفر استانی به قم: مشکل ما در بسیاری از موارد قانون و مصوبه نیست، بلکه اجرای مصوبات است. مدیران باید برای تحقق وعده‌های دولت تا حصول نتیجۀ نهایی پیگیری کنند.
🔹
مردم باید ببینند وعده‌هایی که در سفرهای استانی داده شده، در حال تحقق است و پروژه‌ها از مرحلۀ مصوبه عبور کرده و وارد مرحلۀ اجرا شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/458090" target="_blank">📅 00:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458085">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4PNe2uBCHTzl9P4gEVC18c4o7sBfVXib7e4XLr3zzHRpjKGUQXN43MSoB9xr1mlQXFxBadov6XLQZUzXUkE9yKF_3jXKAeVrBEoYEF5X660UIkgO-nrPNrl7UslIzYWgOvzuwr_4kNodpLu5GhOpA-qn0CMcIB7zBXLeCd8cE_kg54t9Yt_LC6WMf-Win6pNnLfmaS8XqdC4Lg6Xw0UL78Z72OAm4wHwbz14PudqPlkCylD28lTblrSXhAbLGa3x90r8FWNUtynyEGh2Kny4TdgUhLVVbu3gZ2g9_u_bRvnRXdsm3ADNIbX8WYLdtS5vhoyOCMD-CNxa2W_rccB1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kSzeGLlO-KFXYjw_aCDi6zjCG3PWmOOlu9vW_8nZAmvFEwoCRQiS_MMosOy0JJezdfk02Cq-0KVFYktfKWIzUHEbP24bGyn19Oidh8mqsY6YYid0j8m8_7AHEJyB5xHmfrdzAh_s-wtFlfgBtji5lSP7_oUJJHNaX7xt04HtunBWK1AUGb_2swAoj-UOfD7mNpCm1Kphr8VCmFTD_eYeVf32A_43HD9pPoDYFDu3EI4aq7au3bhOd1RFDU0IIMVX3J4_BNMXKeOflXC8dIeDJrA1X2z0oTX2H8Qcba_Ioe_VLy3tJVyFNU7ECGtxwPYpun3OnHMauVyFtpsDYzDV5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/voItS6PHqpwPRf0nPU0Xtd-XOHbo18Nj_x9vRYsL4jsZjppYQMN0JVQwYJ_87oaMRJxiVDL7Dx1N3uhCXyhLbzfl8znnD2tH52tMum9bYd7cYfPRKuYQ84UC3U5AF4-DLi0CejUT9Y16dFzmLh1QHi5PK6z1DiKjgDYXog0yNmibmhiK3WJBWQmspDWwvNtWOkEssmi3KmaWYe4hD_-0grt35cy_SKuQ_V_dDTx_s-vt3JBVWvvQ44fsVqFuOIE7CHCylfAz46oDwbpAghDmdT2NnFz0YQk0_zEp9viyk73M5wEjjac0U1I_VFERw-2SmnGGFz-EkVaR06qrjR2i3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SKgtGAu8487HRLbOguF_UaPBN24KV-qbUpw6WnOL_YHuqhJg6CUyWeWcjWYXguBDpsK7cxl1PTrTL6lUSEHByWVnta45DEIVg7cCA4qAS89NuCXBAVQqwR5RjusZyT4gWqiY3mEeizCRKV_hhgjyHbOXRU5JFfSanOnek4R-NMkwQL5CVkjgRm3c8FeS7wGgXcKeCCzukkLHmoVB0IdZT0G2drKaYdsour8uf1Q2xK1u_0NWKmzp-bdK1LPpOa1cr0r7c3c3l98C4HR6jmiQmiYDLMKHJhU-59nSKbsA390pKXabfTfsZJtuTxtwgSHt12Xti4JCSGuuh0Gegem9Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ag78l1oBzv0Qey5zeQswjsPOE2N1O1JeMPZ4jcEHuoT95YgIWCBzg515v6wP_234m28s4G3jdmaOQyyfg8vTbRLCcyP8KqGkPoOZ0v-ypmva0LowkFBJU9aK3KYAKSPBRXKh4DJ6hY1dvxq_cS7wSAlwMH3JfU4ao5r48Ttp8WleIjT_XX5ZTGA5EB8uAmtGNbGPWcKnJjNO0lCgpydbzK_EvMhaMUDjrKz4z5Bm7RRYGd-Q_zTWISrw4dgO62uALfiSEsmqISRo6OMU9jL7s6oD5hHU7xtNtzM6WPFn-6FxJj4U28c9RejVXeHyAAjCFYWvhkUIQdqBVbhI56cOog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۳ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/458085" target="_blank">📅 00:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458075">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Et1_4ca4MLCcklpjky7xZjo7RkqfNSOZ-vXVefZ3XVhuX_a8Hv4Hh0_4Cq-eeyrAGgs2hE1XQ3YbbcxVrKIHlLXXgFQPDnYpyXJFjhQOVht2r6iCjwtUq0KGiAToBPQoC3t8Lb23LoDsFDZ2V79_I4ZvQz7oAXEHvuQOo6xcT0Xl76C_fpsjGSUz0lCaUNxV28oL4W_Yvf9N87HAOZ6P04bI9dlKJrrA5EgxWbizrvZuu_nMwaDsFAnDsS8JIJJhL-2L3r1_KkI6HWFicN2CbIMXmUShNvfrRNQL89KJM6MgZOL8FJOlbGeZFEnBOtSElv9SUGfn6OzDCg2HdFo0_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNyFpxzFEICJZ-ybEhWq1NQw4dWTB0E0lGKs-X74GLqXNNVD1D6NU1dzVeyGlR1SN4_BKjOO9GKTp6zk6AffAYgt78ovxsMMjwcgQIO65ophiVW4HLg_yn57jxcj8mz9Ra4lXC5-OjG-7FaSerLG8nj8vRiGNQ3UWT6EoUqTPf_ZcN9_8iKxmmTbXisFet0BePS4B1Ng7ZUmVj519QUpayfzjvA2O4NwvI5EpMaBopMx1ap-M6sRyuaRogMhiMvN_KgEvyiYjTDIhDyAUqrk6JL7zabJjw4AkOZSJsa94wsGXu_NG3MxghVS3RPul6zIBbs7LpHrfe0wEAXLeUvx8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k5-rem8VT58TVPwHeQBA7rdi1yvQDKC0OkzsWOIi_Yfg2t3zNrzavwlLr8vA4F5RUHyAzr7U6kgcCRfd7g82dvRCkHAXpcB7ZWSv1AeNWOhdVTW59HLWX5-GGTPQufxeGdsHDZHJuj1xvudlvVdMK6LlEOpQ4BA1fBVyfUazFqdjFl__LwN3G77OmzGbz7nTJ4Qjwco-F_kesG4fWzl1vORdRdl0UCfTVkiSzv3rfJ1c53BjO6zTfW4AldtEaMXTYk2kYtZJcVOwUGfty-Zy9WSrHnPyvH91P4Up6RWP-Cu9L10rrR9dkqv75G2qBi64NYOIPrDctMvIwyhl36TSyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I-EpRdEgjzN-0E9if0-2seHElSnmU3MwspbDfOZokCh_jeO2oFp2DxolHMCiiitIezYZDAX-unpA256n9nz8SNJMJGSf_Im9TxM73eFuIW391Hh5Wc6qrk8bN3APOPWJFtoDGJ9VoF7yagF0H6RXggdecmSbL65Ujz5IvAwIgK2KaumgcNFKPilajPbbZ9JpChb5IAZDFYlVkumbiEtpNds-nko9FepjULHsru0u6TAGgWP8FfHqUwLnGoPo9VfeH2qc2BcmTcFPHykYI24TCHFoU8CKwPHS-zOK5Zdb8uqLClM7SnR5gixWnVi1xkr8WEjX3uncbOQR31BK_o9ZSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cgNxvf2ZU2Srgg7m4PlFqvigJofWT9aItLIxagzLNFeAetAMdr2haln1hZaYpaz45i13k4S61aQR3b_JevGIy9fLvrArQxpqAJ0EQu8TsLAg_aYLD4wu2OdE0JIc0TNM_Eb27EvB21NmDHkXLOjC3WycCyWnS1Hi8G1897baqzLpwh0uz2tl4KQK60SRVPDDyLYhY-2q0B6Z86aNGMAQzwtDWBpCdKEmv-fQafte-rKibQsmumsmfiDfGcsbk2bn-z0BeK-VFUocaI0dodYpLBkUeA12pxWLlVAilr_XV9fhacqBdAYUncEyzqcjPJ6RfRTcMeLhLFDT-8nt5b-amw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMAaARXVQdzCKl72ByciSst-Q5xDXSk8d6OGMNMQ1AAV9uZinA1Aa-q1WgYsHv6lwhdc1y4jwOsMwTKOKvUU3O9_F65_6-vubMmSSmZPma6hOldVUx_ftIpWak__IOYLa71ah4mAKTn2dHax1Cp62kv-4_L7dPOWESvKdPfolWsot3f4zUHA7stoYdrXsApJMYlBjzTyMmyCboZimH8dOQGLIXu5WVSSC6g5gj2Z8ivS--YNTwl9neDQlJqVhkw-Le3ECUDWEGzDUd3fljHZow4eLvCeIeEpLd_Bt2f9iYetdVqAm5oHfvlzO9mSnKmbrGozpNwkDQKsDg8_opZRCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Co9L9BkfZF6ZxE0zgQ_t2RN_voZJSmysro3kQ3_M6kTUiMuDpjmdotxCzVtmypiFlczT_iioRdRHD_yzPwjST14oIManLbkDVmTDKRN28pB_c3ItJwSemKZXQWw6g4Ddw-WUdCrpMy4yF7tEkzaauCgNYyGN5nkeZRznQwpof_kHV587iXM-t7Nbs7YOMVlOD6AL-H1GPFyUsXo5vk71V3Y4C7vUtJa4Al34Pf0JoXoQOHuafh9kwAmLv4sVuwUdiGNJ1-YY8Tmq6eCRM11Bzaah9wKKXGudkl04TON3Oa8xgwfooWwpckIpnBaV3nqqHojtbKXrvBT4r2nOoCUkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mTqus2hLuwXPQLS-eZS81gAotpMdNx13HmJPOwSSaCbh5E_grWmwKM6uaGKbp3O3EBS5YsBkfiBOBbY6JlTDjj7s19yFNCH_SwBpMb4bAhk3BF4qDmFpnIt33JZ4Qfu5OoTsxxv8n15cVOWAvhmXmcwb7QdYJ9BGQnNBV0QkyOiRz-d6IZEMVOiyymkeXY3WH6ieOXX2adg_KCUX8DmzTAtfwg_CYO9oiaVDKQ1YO1qaN2_cU3Hr1D4qRCu471xWZTAWc77c4tRK7IyabPgRhEpfpX9MHf_qJX8zdUHAeFNh6WwGT9ZnUbZ3mH1Z7G6piiZ_YDWHRJQY80_OmtGk-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZhBnOQgAwvL85fQoXT6nrpIREpmfICnGYZbgPsUm3hrh--ed5NRc_FcAipRhPpHItyoQF-WIFL2Nnyb3miRouAw04fEmzHA1V3si5myqaWQweE0d7h2kzO-gF5Jy2f6IIEJQK-VWG7WJuGhyV2iqhamXN3KsE8zKQv8aSSR7yGK99eTHmEfgosCDCuXxHlJ0BGWxqnJOUeh0x03m9yThhG4mFk-4iZ5BqBijsOnzwi_F7RuqLjYQW4dPvKmc-i9DpJ6EoKxnFpwjd3CAR4UR3JOa_KQfd7o3KF2IRoZYH__BjcgLoxAwEvMBSHVAhAdQcuGoLDbWqzOE5aD0NG6HNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pE8RiDBoEzt2V94u8wFYPXqMCuKS9Io-4tDkZW4QNgtt69yyIf9e3fN4FF_BUfJB52eqbKX3OsfkKjGRaQg0QCMEwJ0RYam7yTT9q33uZFqLUYGBqlMIj_rThmuo4E8dhD9JslYI0spsksaM_Pd7OASxmXuCevAcnI6xxbTP0LYvmf2j5HVOZqb6cZvbxjPcHpsRgJCPvzmgtcK5ON3cg1kOniv6h6o0aObEEpDQF-Izy0Zrw00RmUqIkDc7M-ErXEnYLK5hklbXaNxiTVUgg3_YX7Qc-q-aFh-wVJpldQy6uB_uPj0Gx9Hb29PkZ0UB-8I3mXsz-kmMHBcGI1Bplg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/458075" target="_blank">📅 00:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458059">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b9f37d892.mp4?token=r0ygulF8TJgNvROsI4PmDIB5Mi_rLcnpQZJPshwDKlxkQMqu3oqs7-nbL9IqmqzKwgOEng_fVa4hiVUyBQxtdbKZdvnwqWZo8Lv83tmdBTtn98UXwCzUKCEnjJqEch4OV3ekv6mdJZnMNecdJ_6HeW4c12zset4TLdW7S-pWHNhWYOGVYfydRMppZMbSdff3848rCRSHrf2pHoKiOClRRfpiOMGXil20EFG__Xgt9h_mpWmse7eVywVTW8AVZGrLq-D3cSIurRl7GuH-LrEdXSFZcJUQxy-THhV1ukJe7s5hd2mkV1n5obRId9N6p4sh3pmWYxFfzcGZQ7zgmvfl-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b9f37d892.mp4?token=r0ygulF8TJgNvROsI4PmDIB5Mi_rLcnpQZJPshwDKlxkQMqu3oqs7-nbL9IqmqzKwgOEng_fVa4hiVUyBQxtdbKZdvnwqWZo8Lv83tmdBTtn98UXwCzUKCEnjJqEch4OV3ekv6mdJZnMNecdJ_6HeW4c12zset4TLdW7S-pWHNhWYOGVYfydRMppZMbSdff3848rCRSHrf2pHoKiOClRRfpiOMGXil20EFG__Xgt9h_mpWmse7eVywVTW8AVZGrLq-D3cSIurRl7GuH-LrEdXSFZcJUQxy-THhV1ukJe7s5hd2mkV1n5obRId9N6p4sh3pmWYxFfzcGZQ7zgmvfl-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دختری از تولد شیرین تا شهادت در کنار پدر  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/458059" target="_blank">📅 00:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458058">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0Ra2QYjf5cs7ZoWmID0Jy5QrtokBJ-fItFhVYk5Q5UnajP4tfG5IZGgrdSkuRmO-wgruYSAjtlfS68IE2ZC87rjREBfxTEEmQ4TWYvqIESEtRkiKReia4Wg_33yC7KoqkjcX-sSXVvbca77KnK_9KFq7tod33nlZtBJPnx_gD93bHHIhYiOcEaGVeAWLzE3TRB3E1O2b5WPjUZjJsiu7tTY0_nih8v5c0e-AUushNZbIKLbQEtd5Xb_uYsEFSQgf2wa0tIndAqHjvzOx4_EJ_B2sVhJOIu9L_X21GBOYUNvHSn2XHNfohIyq-iAjs_bL10s7LDyga7yHY7OKM9xeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقيف محمولۀ داروی قاچاق در بندرخمير
🔹
پلیس شهرستان خمیر: در جریان اجرای طرح مقابله با قاچاق کالا و ارز، مأموران انتظامی از یک خودروی سواری هزار قلم داروی غیرمجاز و فاقد مجوز به ارزش ۲ میلیارد ریال کشف کردند.
🔹
در اين رابطه يک نفر دستگير و با تشکیل پروندۀ قضایی جهت سير مراحل قانونی به مراجع قضایی معرفی شدند.
@Frasna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/458058" target="_blank">📅 00:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458057">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiX1oqupt7supy0DD1xF6_a4jZmDCMR0B0D7zTbwulwfUU8atxkTaSqCS2AKYsLFuHUTuRBOuwFDWE1U7NYXbjo179LiYdv7hFcYFQo9ekxEqXbPO53Bj-ECyNhnUe2Hcgqzi6vD7I7tR3vibeRjQIPY7JwDIPbqYjI9kEqtSb9cv_pEd6g6WFOMpl2u4tCeHLD2LCRGfTVmM0mn57PAcAKp0WjTqD-ObvYvr3oL57W6NVGmDyeVta5kU0BMbOBOkb9ts1f_OnJ3ilwJDFGY0LDurrtB6-zfzd_wnvgrSeoQGm4GNe0eonkXfUS7dttvqHrv3XZm7eDI8fmnWYReHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای شنیده‌شدن؛ خانم‌ها از این اشتباه دوری کنند
🔹
گاهی درد و خستگی واقعی است، اما نوع بیان آن باعث می‌شود به‌جای شنیده‌شدن، فقط احساس گناه ایجاد شود. مظلوم‌نمایی یکی از همین خطاهاست که فرد را در جایگاه قربانی قرار می‌دهد.
🔹
گاهی زن واقعاً خسته و دلخور است، اما به‌جای بیان مستقیم نیازش، جملاتی مثل «همیشه من باید بسوزم و بسازم» یا «هیچ‌کس قدر مرا نمی‌داند» را تکرار می‌کند.
🔹
این شیوه ممکن است در کوتاه‌مدت توجه ایجاد کند، اما در بلندمدت همسر را خسته و دفاعی می‌کند.
🔹
راه بهتر، بیان مستقیم و محترمانه نیازهاست. به‌جای اینکه بگوییم «من بدبختم که هیچ‌کس مرا نمی‌فهمد»، بگوییم: «من این روزها واقعاً تحت فشارم و به همراهی بیشتری از طرف تو نیاز دارم.»
🔹
پیش از گلایه از خودتان بپرسید: «می‌خواهم همسرم دلش برایم بسوزد یا واقعاً بفهمد چه نیازی دارم؟» این دو، نتیجه متفاوتی دارند.
🔹
جملاتی مثل «همیشه من»، «هیچ‌کس مرا» و «من بدبختم که» را به این شکل بیان کنید: «من اکنون احساس ... دارم و به ... نیاز دارم.» قرار نیست دردتان را کوچک کنید؛ قرار است آن را روشن، محترمانه و اثرگذار بیان کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/458057" target="_blank">📅 23:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458056">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcb52a1b4f.mp4?token=Zj4iUESzKW-nrZoFQ35vqabcv4LrsGWrSFzEfBorIIPfR0OmcUj5C_Dwf_giNAF_4h2JP2BrcqjJoCFRv2zR1oTx8OFjUEEVdBeRiFCHUwd1dKK9eX6rZIPBPTGXpcmbn2gLUm0hvCE7J7to3MWMw3dHVJqBoMSjWwdNei201MhSikVlpkekSpUUTwA7-AaeXKbOlDWqCZN1PUCvz63m3d6MvNlGVTB6bM67n4mhYTBV68q7bJEPAw8a22KovP3tr5mzfw1qj78KqACXbFQy48OtqFZMd8fOLvQmSaZYPYoOyZ6biMnGIkQQLNI_TNp8GdPv1g4KJnEzDF0SDdWLdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcb52a1b4f.mp4?token=Zj4iUESzKW-nrZoFQ35vqabcv4LrsGWrSFzEfBorIIPfR0OmcUj5C_Dwf_giNAF_4h2JP2BrcqjJoCFRv2zR1oTx8OFjUEEVdBeRiFCHUwd1dKK9eX6rZIPBPTGXpcmbn2gLUm0hvCE7J7to3MWMw3dHVJqBoMSjWwdNei201MhSikVlpkekSpUUTwA7-AaeXKbOlDWqCZN1PUCvz63m3d6MvNlGVTB6bM67n4mhYTBV68q7bJEPAw8a22KovP3tr5mzfw1qj78KqACXbFQy48OtqFZMd8fOLvQmSaZYPYoOyZ6biMnGIkQQLNI_TNp8GdPv1g4KJnEzDF0SDdWLdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: آمریکا از دوران دفاع مقدس هشت‌ساله در آرزوی تسلیم ایران است
@Farsna</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/458056" target="_blank">📅 23:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458055">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🎥
گناباد در شبی که با عشق و ایثار روشن شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/458055" target="_blank">📅 23:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458054">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7090408440.mp4?token=r68AVXZOAfvpmTMIplUOGkpb6-W5GZMKywx0wRGCEWwVxBWkvyVxEKfrzBoghLY1JFRdOrPdJcNrcM6MPRMdoKcgHQUeVmTg6Fa6ZM_wLGvi2uSAWp0Oag0Qn3AHfpmtG2FjwYrjQZuZ3V6yqXWKOSINVV0zTEp_P1sONwFh5rxB2DRBsJlX_dKLsQEfeAaP9Q1L4YDqexd52IfazxDnuzXmINfpMrojsOK6mc5v7dCLHpTR-TuF--E9FO43jXLl2Phdhs5l_ziQ3rPAiot5pptKkgGMcDcw8kQZJm9K9VOkrPTPBzH-24stzqwIpwZmJmtSAMcIELZjuCk4jATIJg6Z2ss82r_OFX1lkLVMTV8qisofmrzjw05KUxFBdVn74fzQHUesXqvkO8xlJjP2T_z52Aupzh9DDpmSFq7jssg1BqgTDuzA0ONZ0GmbYzHom1FOZp--ZSrEB8yRJPql-OJ7SdfgrKRMOWMiw8NCtHR0rIbxOR7JFy7plpnqPp5vpwAahWiY-uqglJ-W1TlPIsK83iuktyukSXG7qFz4UGXXddLU0z4iRNfgvVTkyGulh82w0CIlBLtbRCLzehQ7sYYRnVutyogRDctahJ71N_zZBFLOvQ4m07wAu03n_911l1560iPGZZ_ZPyTvckC08C5X_FJsuwz9qXVpK6JuSLU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7090408440.mp4?token=r68AVXZOAfvpmTMIplUOGkpb6-W5GZMKywx0wRGCEWwVxBWkvyVxEKfrzBoghLY1JFRdOrPdJcNrcM6MPRMdoKcgHQUeVmTg6Fa6ZM_wLGvi2uSAWp0Oag0Qn3AHfpmtG2FjwYrjQZuZ3V6yqXWKOSINVV0zTEp_P1sONwFh5rxB2DRBsJlX_dKLsQEfeAaP9Q1L4YDqexd52IfazxDnuzXmINfpMrojsOK6mc5v7dCLHpTR-TuF--E9FO43jXLl2Phdhs5l_ziQ3rPAiot5pptKkgGMcDcw8kQZJm9K9VOkrPTPBzH-24stzqwIpwZmJmtSAMcIELZjuCk4jATIJg6Z2ss82r_OFX1lkLVMTV8qisofmrzjw05KUxFBdVn74fzQHUesXqvkO8xlJjP2T_z52Aupzh9DDpmSFq7jssg1BqgTDuzA0ONZ0GmbYzHom1FOZp--ZSrEB8yRJPql-OJ7SdfgrKRMOWMiw8NCtHR0rIbxOR7JFy7plpnqPp5vpwAahWiY-uqglJ-W1TlPIsK83iuktyukSXG7qFz4UGXXddLU0z4iRNfgvVTkyGulh82w0CIlBLtbRCLzehQ7sYYRnVutyogRDctahJ71N_zZBFLOvQ4m07wAu03n_911l1560iPGZZ_ZPyTvckC08C5X_FJsuwz9qXVpK6JuSLU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماهنگ قایم موشک
🎙
باصدای: سعید باقری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/458054" target="_blank">📅 23:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458053">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90c246713.mp4?token=mcjPPEUL6rlhhdMCM3RyBnmL5S347GmCzp_Gq0WNEVSH_8Pt2qvx18tayKAgPU9vjRm6G7GPTgEsULn90jHbnueHWXZWiYGzrXtQ1Bh4kZ1dhoQZYl5YW1uePB0ksG5nCW9vABiUEYV8yVwVLYDrcHT6w54GomTzM4J2vtBJ0uj-6I_2AxE_95ABbuUAM_ux1vzDluGcLq46hWR2cI5g3Ky4ZKTXs5qhHWreFI8ClyD96gDjpQ11PKQK8__V2y8MKVxmDi4Lzip9gTYQBrXnUTuYpr-vj9mXjsyBrTA0Kx0zPn4pBWKCgQbGiILR2aXtK2SQtGzUwuyioZMgKoFoOb0scsKNhyvvppJekFN0rBTYZa-No41WZeyUfwNX63i0z6iAt2FiB5eW2xNyVqqmfauJ-tC8PKqedvRKH_aFD4CVL9Gh4rz8hvtsiD2zjkuM7GpKq-LJ2hIL7TVMcecndFO4ohx-zfdX5qabM3dREakW30V05TNeCGrAizl93sBNJf7O-8X1cXWTwVTldFXAxWsWmLX4wMmDfyYYh0SvH09t3-vznSITTbONZiUd30uR2caEP7UldaIDUi9G4KblS_pMW7XX1DmD6JhtwQDZz70ULiydkaU3MkURnSxpTOpa21aJPPD8p15YrbUC0-nZ6LBR7CQGQkf03j8XO93cDmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90c246713.mp4?token=mcjPPEUL6rlhhdMCM3RyBnmL5S347GmCzp_Gq0WNEVSH_8Pt2qvx18tayKAgPU9vjRm6G7GPTgEsULn90jHbnueHWXZWiYGzrXtQ1Bh4kZ1dhoQZYl5YW1uePB0ksG5nCW9vABiUEYV8yVwVLYDrcHT6w54GomTzM4J2vtBJ0uj-6I_2AxE_95ABbuUAM_ux1vzDluGcLq46hWR2cI5g3Ky4ZKTXs5qhHWreFI8ClyD96gDjpQ11PKQK8__V2y8MKVxmDi4Lzip9gTYQBrXnUTuYpr-vj9mXjsyBrTA0Kx0zPn4pBWKCgQbGiILR2aXtK2SQtGzUwuyioZMgKoFoOb0scsKNhyvvppJekFN0rBTYZa-No41WZeyUfwNX63i0z6iAt2FiB5eW2xNyVqqmfauJ-tC8PKqedvRKH_aFD4CVL9Gh4rz8hvtsiD2zjkuM7GpKq-LJ2hIL7TVMcecndFO4ohx-zfdX5qabM3dREakW30V05TNeCGrAizl93sBNJf7O-8X1cXWTwVTldFXAxWsWmLX4wMmDfyYYh0SvH09t3-vznSITTbONZiUd30uR2caEP7UldaIDUi9G4KblS_pMW7XX1DmD6JhtwQDZz70ULiydkaU3MkURnSxpTOpa21aJPPD8p15YrbUC0-nZ6LBR7CQGQkf03j8XO93cDmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«انتظارات مردم از مجلس انقلابی»؛ صدایی که در شب ۱۷۷ شنیده شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/458053" target="_blank">📅 23:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458052">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0811e8964d.mp4?token=OikkUuNPNjjnIfXEbFKQZfywzwHLHksybzRS_oYUhdycUEr9KkiE0R32u3r25zuCj_xiquuLYVUjrvC3SD4uWkN9O4xo-IelH_Jzn7BDmYqe0aqjr3BbNQSW17XvucP2qSwq9Y1jDsFeS5MgQsxwwUJozXtQad6VImVHSaJzTYgfZs-TzJ2EBg9Su4ecSGJxBblIPLny3mLERASQR7pY2imozb6a1BTZTMKMc3KbrBiqUfpWaURPJZKjBefoB0p8yEtY4mUJBmeBQepydWj1Rux1SK8CYgm1VsjsJT_IBdzsa_flTVZzGLjmwYtRthzKdruLki34wcr8UBRL73_AA36RIm3bcvO3M_GIo-QG_oxb470Hfr9PvY6ZzrTtcYkBPcf6r6lWKLmsSDueWoNE-LI0X3UHdzmsgS2SQmZseXateqIZ34qgu1CtlKm_BQACND-ID5iBN_8Zc2wns2FY8fHBK7TA6WlJLyyM8QCtFw9gbk8I8mWAwyD__z-VDoT5cPDS8c7rnsEVqzMxZnpRcbAQ6Xk6iESPgXs5iKr0rfTUnyyIgzuJpLQhs4hzxD_N2LktcsAljnwnkNDZGsbwvTLuc1de4v-1IIwBp06fx2hKtRE2HXJKsCqa0OQnhun6NQ_BS8kZQY4y1nrUDD8l9gr1LbSaBJb63dEKI_VM3FY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0811e8964d.mp4?token=OikkUuNPNjjnIfXEbFKQZfywzwHLHksybzRS_oYUhdycUEr9KkiE0R32u3r25zuCj_xiquuLYVUjrvC3SD4uWkN9O4xo-IelH_Jzn7BDmYqe0aqjr3BbNQSW17XvucP2qSwq9Y1jDsFeS5MgQsxwwUJozXtQad6VImVHSaJzTYgfZs-TzJ2EBg9Su4ecSGJxBblIPLny3mLERASQR7pY2imozb6a1BTZTMKMc3KbrBiqUfpWaURPJZKjBefoB0p8yEtY4mUJBmeBQepydWj1Rux1SK8CYgm1VsjsJT_IBdzsa_flTVZzGLjmwYtRthzKdruLki34wcr8UBRL73_AA36RIm3bcvO3M_GIo-QG_oxb470Hfr9PvY6ZzrTtcYkBPcf6r6lWKLmsSDueWoNE-LI0X3UHdzmsgS2SQmZseXateqIZ34qgu1CtlKm_BQACND-ID5iBN_8Zc2wns2FY8fHBK7TA6WlJLyyM8QCtFw9gbk8I8mWAwyD__z-VDoT5cPDS8c7rnsEVqzMxZnpRcbAQ6Xk6iESPgXs5iKr0rfTUnyyIgzuJpLQhs4hzxD_N2LktcsAljnwnkNDZGsbwvTLuc1de4v-1IIwBp06fx2hKtRE2HXJKsCqa0OQnhun6NQ_BS8kZQY4y1nrUDD8l9gr1LbSaBJb63dEKI_VM3FY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: برنامه‌هایی برای عملیات آفندی اقتصادی علیه دشمن داریم
🔹
دشمن می‌خواهد در اقتصاد علیه ما آفند کند و ما هم باید آفند کنیم.
🔹
امروز هرکسی حتی یک سنت از اوراق قرضۀ آمریکا خریداری می‌کند در خون کودکان شهید ما شریک است. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/458052" target="_blank">📅 23:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458051">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_6U14lj2fQFluTulCN0oRlpR29hR3v-XnK50WBqlsZ5momzcLUOGhtQD4apCweRo5onTmIHIZTdB8LZm8mtZ_j2qYiRXAikH6XgZNw1fxIZy9F5y1baDBlFocjDb0_8-b44cCBnWS1pL_p3krwCyn5zPJZSUVYT1PURhMNCthAXeez_pmwHWso7upmczX49a3mcp_Zn-rE9EXEUkX9YAkrUeacqoExKovjYi5AbJemMGOzp83uectJVqcepbHlHLcxogwNbu0oA6soV9UcxcwIi7I9dbC7FibFi-ey4FNdc5sYmKIcrxx2yYUN1JWOd7loVaCPWivlmCG0OGd4_mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فناوری موشکی این ناوچه را به سپر دریایی تبدیل می‌کند
🔹
اینترستینگ‌انجینیرینگ: چین یک فروند ناوچهٔ جدید از خانوادهٔ «۰۵۴A» را وارد خدمت نیروی دریایی خود کرده است.
🔹
شناوری حدود ۳۹۰۰ تا ۴۰۰۰ تنی که برای انجام مجموعه‌ای از مأموریت‌های رزمی، از دفاع هوایی و نبرد ضدکشتی گرفته تا مقابله با زیردریایی‌ها، طراحی شده است.
🔹
ورود این ناوچه، بخشی از روند مستمر توسعه و افزایش تعداد شناورهای عملیاتی نیروی دریایی چین محسوب می‌شود.
🔹
کلاس ۰۵۴A که در ردهٔ ناوچه‌های موشک‌انداز قرار می‌گیرد، یکی از پرتعدادترین خانواده‌های شناورهای رزمی چین است.
🔹
یکی از مهم‌ترین ویژگی‌های ۰۵۴A، سامانهٔ پرتاب عمودی موشک آن است؛ این ناوچه به ۳۲ سلول پرتاب عمودی برای موشک‌های پدافند هوایی مجهز شده و از موشک‌های میان‌برد «اچ‌کیو-۱۶» استفاده می‌کند.
🔹
این ترکیب به ناوچه اجازه می‌دهد در برابر تهدیدهای هوایی از خود و سایر شناورهای همراه دفاع کند و بخشی از چتر دفاعی یک گروه دریایی را تشکیل دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/458051" target="_blank">📅 23:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458048">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28636dee93.mp4?token=QVSv1dlhdTlm-k2oK0k75fFUpl-PD4N6Rrp6gaGjoCH5sH0TQ7-8T9TFKqWZUuG7rlpdsV_sBOE3BYDrexxdaczMffl4yYM5bvGTUoPPUe--tFgXDkTCTpKta63MZS3k0Iz8DpeFFdf-UxwtLy8_fGMiLmOXcJCpyIB6ZMn28UtWZ4fo6MzmVF5SBbm0fPv0Rx6hhmygmlanBJhKLtlipqFpz1N2yFOuU4VDA_AgOlaGP6qNm_v6iwzxMjN4bOkYQD-HENd9PWzb2Tt_r8F5hAagFZDJqbA3n5G8DO_KXmnbngegOlPiTlFgIFS121JhcBqJYJd7dcCjnapZ4Hb80w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28636dee93.mp4?token=QVSv1dlhdTlm-k2oK0k75fFUpl-PD4N6Rrp6gaGjoCH5sH0TQ7-8T9TFKqWZUuG7rlpdsV_sBOE3BYDrexxdaczMffl4yYM5bvGTUoPPUe--tFgXDkTCTpKta63MZS3k0Iz8DpeFFdf-UxwtLy8_fGMiLmOXcJCpyIB6ZMn28UtWZ4fo6MzmVF5SBbm0fPv0Rx6hhmygmlanBJhKLtlipqFpz1N2yFOuU4VDA_AgOlaGP6qNm_v6iwzxMjN4bOkYQD-HENd9PWzb2Tt_r8F5hAagFZDJqbA3n5G8DO_KXmnbngegOlPiTlFgIFS121JhcBqJYJd7dcCjnapZ4Hb80w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: با کمک مردم در جنگ اقتصادی هم مثل جنگ نظامی دشمن را شکست می‌دهیم
🔹
مردم همان‌گونه که در حوزۀ صرفه‌جویی پای‌کارآمدند در حوزۀ سرمایه‌گذاری برای بازسازی اقتصاد هم خواهند آمد. @Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/458048" target="_blank">📅 23:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458047">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ab451d35.mp4?token=A-pHrEByRiOcHGEf2LL_sNpKUBxwz6Hy4kK4OP5rnBSbxEGrNhxH8hf7j0GA7dImxRyF7RTQflBV2bqtpVIVnxjZq46NNm_Z4dOfM1ggdMdsd-xxY6tAJLMUb7jXMtPLppC0YUo0EDrF-80oCBsH8SHNzJfWgiLLAgiZf9_x9DzEOU6NbxKKJ89o_C9Oa-GNxbbbr-7YcjJUFcdgY9GhTuJo-qKVvs1ZTXzv0yIw9-mfJwigXM-gJ9evLToZNTPTElaM-C3qizopu7KJXdzFlk3vO76bRsT0zE5OHiPZjrNDtN9V1buZV_jnUnkyouFrbd7I5Goyc-jGwqj9gDutAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ab451d35.mp4?token=A-pHrEByRiOcHGEf2LL_sNpKUBxwz6Hy4kK4OP5rnBSbxEGrNhxH8hf7j0GA7dImxRyF7RTQflBV2bqtpVIVnxjZq46NNm_Z4dOfM1ggdMdsd-xxY6tAJLMUb7jXMtPLppC0YUo0EDrF-80oCBsH8SHNzJfWgiLLAgiZf9_x9DzEOU6NbxKKJ89o_C9Oa-GNxbbbr-7YcjJUFcdgY9GhTuJo-qKVvs1ZTXzv0yIw9-mfJwigXM-gJ9evLToZNTPTElaM-C3qizopu7KJXdzFlk3vO76bRsT0zE5OHiPZjrNDtN9V1buZV_jnUnkyouFrbd7I5Goyc-jGwqj9gDutAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: مردم صرفه‌جویی بزرگی را رقم زده‌اند
🔹
اتفاق بزرگی در حوزۀ صرفه‌جویی رخ داده که آمارهای آن به‌زودی منتشر می‌شود؛ باید در این زمینه واقعا قدردان مردم باشیم. @Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/458047" target="_blank">📅 23:08 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

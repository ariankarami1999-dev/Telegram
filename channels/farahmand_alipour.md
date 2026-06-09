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
<img src="https://cdn4.telesco.pe/file/LwVhhoeNiDAe7HKkaMgAjFJxme7TH6Ljr8xjrIAEfAxDv6mk0nIYUY02JxlpJwPjarQWsg_Wp07Pq1jRQM6R-fNe6npJlFcYlyBJfKa51QkWvplNOaRi6KZhy0coCntnIg0XQ7I4YNV_iP5s5EsmEMqKUxYOfleJisRqtYcOaGM0rkB5ZjoapxO-q71TFmQ1Ot-jpRuWft4zPkAVBHDE9HXu7eFc_9e-pUMsddskOWm0wmxXj6eZmwuXjv68VBHSb49DM2uGYt-JYF33k8s0DpwdOPmAQqq3AX_hOvRHw--i_snRzM-ognOtdAkzXBgEWY-Q7mhh2rEqz6J0kWwC1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 10:00:44</div>
<hr>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 823 · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOHMF10K4WDoLxoBUEJHMckd7TH6GX9PXf3N22nnZXOUf12BIwMzpla3GBmJN8pWd2mutB9e5Qun1GsXCm_Y6jRLP5EOD2tBWFa9EnfaDdsAutOsTLNOHMaZIzR4DNJRfpsxfoPuF4ic4YAirjl3J3u9WAl49Ke_zENxYDjXcJRhbJ4eWyftdmj6BEplrL7Qo1zTTQjG7kEEEVd4slCDM4uC-ptt3Iscso09dSJLF_aPVAHJFOpL3OSuoqKH8qtv6BFugUaBuXN7A5a9kWw2URD-fUaj0GReP2C6HAEEo8C6FTZL8-f1L00N6Kx23d08Nf0jd2YP7xNUcgKnLoMgmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IY9RV32qaTw0exm9-DK194NbTlE-4E9YEDTZBelmKhAtJ_j5kG90do-ougJdaa0GsfzcC-K65VVfBQ6uKfsVCEHlflMykONaJpyyjow85ZhkwhgNz6YTKFfLyU3Cpl2A1Zt4TNM5jH-c9TG9ZlOAnIO-7O1KL1w38Ll36o2db7YhBBk6dcjXQ0tstSpjIpQ-ePQToQ_dN4yBeGaWTaGIAMC-ZmweDk0Xe5yZcpTshtlokHywcnmkUfI_d10godRXovQRB9cSggFfSQmAMAMp9cQs0FXyc2RA3-vw0al1owD-guBFKfZQq1-uvb2uVGpNBMZTLCJ7pr99NGetd-Hr5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانبار خواهید شد!</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5OnaQD486OnHpeM6ME67lrGchiBntn4xr3QP02UhTz9_MjCEKaYVoXPWc2a279KgxLXZI3EXwDv70ix7Y7fDmLZ6PeTJ5mv-AzSGsTrk7bLT8mOeANGRt7RpEJRT2g7XtmjoSx4eb2M0FCPXjJVqw-CgQMwzZfm2tp2ftN5KMc05xzSMFxeau4I40msYKxveNcQgI7DaagBL5syIfpU1v01D3Av-68RWcOOsXu72R4bBZ_mSDjYK8CQl_BNrSHZ5oHDyl0bH8GwPu6dWZckDafiWKv1a5XAAojtUEysoesKxbT_DGgVut1fkO4XPc9LZz_CZjD0502m-q5opfTe1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZwzkcG2NF92qI08UivrDGCx-Fh3LmDmcqZy4m3i5G8uIkE368TU2o5E0w3rfEWO7DJilUjGjPzPg9crtUX12WTNT_fjJrn3fbOvO9AOM2x6iSc_-cHMTXhH9ojc1w2RxI_cylip9yF1TPmyB0vDQSSb9esf0ERkHtnZOgWQd-3-0r5cFS_dCbBZ5wtHN_PWl4LAHGUyHVcS4eOWYHJQnPzJAHWZwC5ZuB57Mv3hjYsENuUR_DRI8seA8KtoCwObF2wRxDr_B3asSVqHdK24KdNxLpi3x12hzAXrtljSPJZLP1mOlYPZARMW23lPSvMY0KmDclRJIEh-rlw_ATPMog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانبار خواهید شد!</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG5RMPS_pTLU1v55QAEFcOksdt2MfA7CYcCGEFpWS8Ac25UcYO0gKrxRZdSC2igAug2ZmexHtUlStFEntaJB4Y-Iz9oTJZKqDXmUDrQhC3upjVLXQZJIStqDmxO2pX5o-GZRX3Yt9aauVon8reczj-JZS5l-wYydKjBYrQOf8b3hV9097fs0EXp1A_n6P_ef68qWSUpO5f4vW4xfP3jWNUW9I6RIib9LFki_icXCDjecrqDUs-TvVnI0gvnVBGp0lUK2Vu0wnVPqKIy7Jl1QLB4Kl3xdbMoiQXAqYOAsJNOONxszM-ETxuNcxnbJiBi-j4uyEOZFxmE9VS93VG-x5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAT5Yo62vOWr3odIdejd4zKBzhTgEZ7K1oMlwMqls1VUENGPYGZSClaIkx156X5UFWNUh8sPY70XU8ootnu_9hDyFYTewwZgnzwC5sG64ijS6_j1bwpCveEdlZv1NYVJgcVqKLYTmhm_d_exTz9lCUH8Fs4bXGJitqNGqAb5HW_kmyt271r7Ub9qT-w9xs0U7PGWxIgLWr5eM-juAHq7STGuV4iK_ZsBdyk7JiJMzh-Kc9UQVrXrW7iJ00aVycRYBFBDLg0dljil83-G3Mex_TjU1XD2d80aStWT5pj3i770Y3MTJfIHov5eEi0b3BhjhPJNv1mo4dcpc5GLr4IUqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKLcjLtymkdAPjcMUa41LF_UH1rSbwYCEJAtHXbJuBEVZ7iioIqic9oa516HOBFJHgQBopzOEx8qqfuIN71VeCB_Y4ixJl1FZ8uSCa8epcFyK77ZPxppk9tTYGq6TZX76sHUqU_P80ezjeEZUtWfSGhrQvkcQJJbrMKpEOAi00p-Gt_tK51Ra7Yfap7vXkmdV2R9cSwNWpZwfK0itbFdjIi42Qu2gRU1kIwDyr3CirkcyJEeDHgB39A2-9WPQowhXSLtT3K0QWg8xOkjaEEPzHtgPbJkLrR05kImstWsQ-HZPNWRpEiIujVGw3out5F5jG0Iw3qF--Z2ImNgJNEPzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=etHA__5-FmUpF8kVamL_oL0FpVgls-DcdJRLqjGhIx-9pdZ_nb4XPmMIYXHNmzm0hx5Gj-ElPWJwFUayrGZmhnyj1qbZNSt9E7cWjFttr1JiVwkBsis4I5anWUctnVeyiegHClmxnfHw8aoU9KZo_0xUsSDYaS9A83wyBaXn13K81HYZW8sO7or3KFHpsZDPZ-UmssQpmLE8dw40uyNtoBLPrJ38Xny4FTwh0Vyu-vCpDkofgz20oqYw9ui3u0zo6FQkllh4oIJn6AA5XbpyE8M3Z8Zh7VISsYtOBJh_Ja6utQqRyo94UeZ6lLj-gNvuV1Aaes1klmDZQpj1AW_izQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=etHA__5-FmUpF8kVamL_oL0FpVgls-DcdJRLqjGhIx-9pdZ_nb4XPmMIYXHNmzm0hx5Gj-ElPWJwFUayrGZmhnyj1qbZNSt9E7cWjFttr1JiVwkBsis4I5anWUctnVeyiegHClmxnfHw8aoU9KZo_0xUsSDYaS9A83wyBaXn13K81HYZW8sO7or3KFHpsZDPZ-UmssQpmLE8dw40uyNtoBLPrJ38Xny4FTwh0Vyu-vCpDkofgz20oqYw9ui3u0zo6FQkllh4oIJn6AA5XbpyE8M3Z8Zh7VISsYtOBJh_Ja6utQqRyo94UeZ6lLj-gNvuV1Aaes1klmDZQpj1AW_izQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله سنگین دقایقی پیش اسرائیل
به جنوب لبنان،  بخشی از هدف این حملات
پیام اسرائیل به جمهوری اسلامی است
که قادر نیست با اسرائیل معادله‌ای تازه
در خصوص لبنان ایجاد کند.
جمهوری اسلامی با حملات دیشب و بیانیه پایانی امروز حملاتش، میخواست این معادله تازه را ایجاد کند که حمله به حز‌بالله لبنان مساوی است با حمله به اسرائیل.
اسرائیل این معادله را نمی‌پذیرد،
در برابر حمله به ج‌ا به اسرائیل به ج‌ا حمله می‌کند و در لبنان هم از ج‌ا حساب نمی‌برد.
گروه حزب‌الله چند روز پیش آتش‌بس حاصل شده میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5421" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSI6XhpcKhhyX-p4jUn3coWb6WKpydoMhMi7mOO16YKillKOdrHM-6XRWYluAVn4hMh5CRSV49uugBKzhEm9A8pAONk2iHxv8bGf0_W44BB6C7tTDjg5wQqUj1FoKJOor7iqXGIgXyV4gCd0v1KmTdTI29zhB_5QDooB_eCELZgD6YCE7ubjiKnefDgHTlDeeoLlYkFKvKDWRxkxcmgyyG_l-aJ9sQp-YTVtaAY2zJ2f8z_aN9kR6pTc3Qu0Y7K5I-FmthVkrF8p7qKAb_pj-ROWk00UAQsSCaiiXBFT2IE-kAk0WoWO1K1n66X1AyO9lf6xs5ZX7a2K7l3iM0r5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=BnbsKhzi1uiA3fFYbM5vHbN9SoHA2KZa85c430MOdIBFwKFZgibmk-5rJUdnhxgfUA1YGHrpxkt4y13S786SmoDPbd_gj0T4Fqv2j1o5Jf4uf95LTrIyRX1ArVoacB7eWbQs67HN4LwB9_8YlTdvRxcQ7FK0_aupNDYXgfxwj6fEPFzrnRpQB1I8-wGZzT0b0T-xMoC8bzOiHK8JLj02Uz9YTiwPb-csYvIvLOX0bxYSs_WuyPTGpzNZPUOAAU-y8hHtSeVe4g5djfoWnFwTqBArRnh4Gt8GOT-1Vc6ksZ3dpZ0B_Wvdn3-Wxx2Bvyl9VsnDji7q-syjshAiPZEQUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=BnbsKhzi1uiA3fFYbM5vHbN9SoHA2KZa85c430MOdIBFwKFZgibmk-5rJUdnhxgfUA1YGHrpxkt4y13S786SmoDPbd_gj0T4Fqv2j1o5Jf4uf95LTrIyRX1ArVoacB7eWbQs67HN4LwB9_8YlTdvRxcQ7FK0_aupNDYXgfxwj6fEPFzrnRpQB1I8-wGZzT0b0T-xMoC8bzOiHK8JLj02Uz9YTiwPb-csYvIvLOX0bxYSs_WuyPTGpzNZPUOAAU-y8hHtSeVe4g5djfoWnFwTqBArRnh4Gt8GOT-1Vc6ksZ3dpZ0B_Wvdn3-Wxx2Bvyl9VsnDji7q-syjshAiPZEQUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=nChgvLDRQG6hVrZjQid8Sho2Smxds428ZMx0CnzlEM3cQzG6WKWQEqadQWyIXUb0Upu7a_H2EtRA8rX4rjHEkV0Kpo2GrguudkfJss0LXWfkDgOodvDz9mOs7XDHSin7t-IthzAahVXJZVjML797RIvssLmc5hb9XMt6bO5NsCrrqrCi4aiZpcIR8TKzFPVMHKSqS0sqVqX-WfyQFI3BtrP8mIf-LSO70l-dpscbenMabzWvO7utE0r201AvFEQVEtH7P1mr89WXESwQu47xuvf7zhg5aOqaVm4fKrCJWtTXgaydetzrXDigPZ0zjFhOdZjk8yrYY5C3M5WeB03WdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=nChgvLDRQG6hVrZjQid8Sho2Smxds428ZMx0CnzlEM3cQzG6WKWQEqadQWyIXUb0Upu7a_H2EtRA8rX4rjHEkV0Kpo2GrguudkfJss0LXWfkDgOodvDz9mOs7XDHSin7t-IthzAahVXJZVjML797RIvssLmc5hb9XMt6bO5NsCrrqrCi4aiZpcIR8TKzFPVMHKSqS0sqVqX-WfyQFI3BtrP8mIf-LSO70l-dpscbenMabzWvO7utE0r201AvFEQVEtH7P1mr89WXESwQu47xuvf7zhg5aOqaVm4fKrCJWtTXgaydetzrXDigPZ0zjFhOdZjk8yrYY5C3M5WeB03WdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=Nsbk_2QDXA0ACkEs9ZyYceKGmg6vTehgVvWACIAp3EHSChHQo2ghXVu88O8_o76HGqqG8PFZ_MQHU7jpjTgaNBFTCXE-91p6DUmul1kC-_HWd8yp3_2b7RlKM3H_bK0fiT7R3imNBl1aUUv9CPO2PARrnV-7BHU8i9rCimUJem-nQs9xHDgtZ-my78txVRZp_FEXiCKpq2bDWh3EL6rjWjFEgd3B_29RlWUUqfrClmZ64tMgDyqOP7QIj3wm7f78vljj1q2jRIZX643yuSgQWW85OwXWX8H_mnCpgLEtTMYXsv4JDKcg9EXT8Cu96xd82hXICu8fU_Z0B5kNGnvnjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=Nsbk_2QDXA0ACkEs9ZyYceKGmg6vTehgVvWACIAp3EHSChHQo2ghXVu88O8_o76HGqqG8PFZ_MQHU7jpjTgaNBFTCXE-91p6DUmul1kC-_HWd8yp3_2b7RlKM3H_bK0fiT7R3imNBl1aUUv9CPO2PARrnV-7BHU8i9rCimUJem-nQs9xHDgtZ-my78txVRZp_FEXiCKpq2bDWh3EL6rjWjFEgd3B_29RlWUUqfrClmZ64tMgDyqOP7QIj3wm7f78vljj1q2jRIZX643yuSgQWW85OwXWX8H_mnCpgLEtTMYXsv4JDKcg9EXT8Cu96xd82hXICu8fU_Z0B5kNGnvnjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cf3PHh3LtMSh_zqSPUpUCbFpArE58y2EZBDd3XBrKfGl7acfotyUSb9BJIkQ7Xz8SZ-nHyWzRRDsP48UkH4KYpcgokq73jrbnJnuN-sHC-hADvwAOEZxPUNR1CAqeVvc0bzgL0JYyybxeFCQAk0wvOvNumPJhttHPbgQ9Kgh539E7MZW1B1yaRmJzZyAhEpXInQM2n3z2slnuB1tb-ETkY0AePZv18xGW70nWcSt32BPIVtgndQjaSJG5LSrS_gQPs_ZUbT-sHZxuyv-kNegwEs7yh_7kmKf-7m50pBK8vhki0dcem-QpIvUDtXoj6Z1NNRHNENnK208F8Bf9aGATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b-IdRHS2E1ilfJj-RAzHx3GTRIoC7AmweePIbohu2q-lhiuHCo0TPEjmomAv7rSvf7xP5U2ZP2SSdHGZxZfw_s_MP6NOvNQ0oJBLlhqMFHvflqZlensXogQPNJGD0VY-ax07bYrxUDGpvM5u0TZJrqTQXuPKj3aPC0KybNxIjWVfmVulZHuWZokT8fnnVsPfwHpE2HW8uYQhLFNzXgCqEyiRixp6oSuFM8zYwLgcZ394fxpKundMxunN8zzTyLDjuy8nACOjIWLX99idLCsbhA6YNGws7fUIa-2Rm_Xuy2oj24c5P6HoR6Ku6CJL7ULRuvf5OXgwL4ETUywZDXjPvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336071990a.mp4?token=LTUb9b5mqE0hl8kEKt3kILNwYvXrlo95PxWNDOp84XNG_IvZViwK6bCvucKxh_6CwcrtnurzOrbh9URrqx1PmZDcim4uIu5wsbjJz0VBugS5h9lYpKfKUX6m8PBX5i52x0B9rv0epik24RucTRON3wIM5iBqSostxJeJdA6bXft6ay2LMKuAGOyrpRQ86DDHPbq5m2ZUzvfvNnuAwukqDIxP5yKtPO4eXxwpLAOUHyjebwUPrwB0wihs4hO6S9IKPALqV7jKpwjuhZXyufF-NzcXGH_LZM5OzhVn1XN6niSRFfs9K1dLnzSSMuyYRzF9FkG1MGWEctNiKhGE56MB8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336071990a.mp4?token=LTUb9b5mqE0hl8kEKt3kILNwYvXrlo95PxWNDOp84XNG_IvZViwK6bCvucKxh_6CwcrtnurzOrbh9URrqx1PmZDcim4uIu5wsbjJz0VBugS5h9lYpKfKUX6m8PBX5i52x0B9rv0epik24RucTRON3wIM5iBqSostxJeJdA6bXft6ay2LMKuAGOyrpRQ86DDHPbq5m2ZUzvfvNnuAwukqDIxP5yKtPO4eXxwpLAOUHyjebwUPrwB0wihs4hO6S9IKPALqV7jKpwjuhZXyufF-NzcXGH_LZM5OzhVn1XN6niSRFfs9K1dLnzSSMuyYRzF9FkG1MGWEctNiKhGE56MB8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله به یکی از پدافندهای همایی غرب کشور توسط اسرائیل.
این انفجارهای پشت سر هم مربوط به موشک‌های این سامانه است که یکی پس از دیگری منفجر می‌شوند.
این سامانه پدافندی قرار بود از آسمان کشور دفاع کن (با شلیک موشک)
ولی اسرائیل بهش حمله کرد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سپاه یکطرفه این آتش‌بس و توقف جنگ رو اعلام کرد. نه به درخواست کشور ثالثی، نه با رسیدن به هدفی و…
این می‌تونه ضعیف جمهوری اسلامی تلقی بشه.
احتمالا برخی‌ها در حکومت ترمز سپاه رو کشیدن</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5410" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=LQWranoo6ndXSFHEh0-PwqCiChDeIbwSQdfbVH54-dWz0YjRPEIasiHGvtAO1pt8t6NllfMlupO29APp4k1Y9LflJnZBQpHQsVMgRTDOyOM-HusZ-Ix5hi6OC9a5S-dD32_UjZ13RUa88EW3tWHUDN7Cp4YYVh0o19Iy-M8Uk6iyVj90V3FDjz592rlhfJXqnZYuh-LMWOVoditb1-6c441rfCQyulbKLoeSfiXRzaarBq00XgVcX_EbNBfnJsAaKphQb4LMlt8CMxZcwcTpk7AiQADVxljspSgIgIGjk1srX_irIeasKFanHd2H7njuNebYCS7jOc0WucLOoz_E4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=LQWranoo6ndXSFHEh0-PwqCiChDeIbwSQdfbVH54-dWz0YjRPEIasiHGvtAO1pt8t6NllfMlupO29APp4k1Y9LflJnZBQpHQsVMgRTDOyOM-HusZ-Ix5hi6OC9a5S-dD32_UjZ13RUa88EW3tWHUDN7Cp4YYVh0o19Iy-M8Uk6iyVj90V3FDjz592rlhfJXqnZYuh-LMWOVoditb1-6c441rfCQyulbKLoeSfiXRzaarBq00XgVcX_EbNBfnJsAaKphQb4LMlt8CMxZcwcTpk7AiQADVxljspSgIgIGjk1srX_irIeasKFanHd2H7njuNebYCS7jOc0WucLOoz_E4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJaGWez2C-Wl9iChTSM-3l2p_NiuWSOCtaFsgshMGrgC1vHZ5bp6FyxyGI_8UWHNRJI8PfnEmd9SD0M4wvlBJTVSBZZXhdST26fOlptNwwWf8b8bfB8FW43wHNQTJhxAKdlfjn6uXS-UCpk0oIqXDXMntm4h7EegbhAcjRViYqRZ0Roq4jAI03pMIWmsyrzJ9F7uQXx5z-afLZDaqWQ5bvWyKVt5xQca0XELyr5O1ecUJMrh7rzO8mIyx6tasgoafpwwiWtCLXgDiZ7SZS3wECn5M6haQWGpEis3ftglnCCXkZd1LP12gvgUENekL3jm9wjGbNtPH6wXh8V9AXs-XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=HNJYReisziI2GX6upVd0pagCXxXd0DL6eDo7mFF4wSqUsYFtbcBiio6gUuSyUD3ZXt4-N2jHxLlgEHJo17s6lz34qpYHSOxDPAJWsrnyNcT6dhYidgy1CExVPUvrpO5IMVDLKH1CNssyFYV2FPvMrz4-2jiD0clQX75-wM_4pIt0vTQOWawMuUseddi-q54nzcKuaxzCOunwX6iV7mwigTtXb5d6Rj9ua3Hs6QW2a40kcttsIAFIrWSaGkHAu4cTTp9HVgxqn5He4VkYe9GcvB3ttFMa8DXVAx2Si2G_MFg1pgIIr52nxPFuGZZHtLcaEiAb_c1FZUotgLAk_Q_U5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=HNJYReisziI2GX6upVd0pagCXxXd0DL6eDo7mFF4wSqUsYFtbcBiio6gUuSyUD3ZXt4-N2jHxLlgEHJo17s6lz34qpYHSOxDPAJWsrnyNcT6dhYidgy1CExVPUvrpO5IMVDLKH1CNssyFYV2FPvMrz4-2jiD0clQX75-wM_4pIt0vTQOWawMuUseddi-q54nzcKuaxzCOunwX6iV7mwigTtXb5d6Rj9ua3Hs6QW2a40kcttsIAFIrWSaGkHAu4cTTp9HVgxqn5He4VkYe9GcvB3ttFMa8DXVAx2Si2G_MFg1pgIIr52nxPFuGZZHtLcaEiAb_c1FZUotgLAk_Q_U5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط یکی از موشک‌های جمهوری اسلامی حوالی شهر فلسطینی «اریحا»
دفعه قبل موشک به یک روستای فلسطینی  زدند و
۵ زن فلسطینی کشته شدند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5405" target="_blank">📅 13:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
در جریان حملات اسرائیل، حداقل به دو سایت پتروشیمی حمله شد که هر دو استراتژیک محسوب می‌شوند:
پتروشیمی کارون در ماهشهر و
پتروشیمی سلمان فارسی ماهشهر</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5404" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/af6q-aNp8BGnkUXhqrEl_BgU1v07BYJ-z-aPmrE63y40pYNT1LVTqYgF6GAoqqc-LBqVl1Ucp3Gx-yiIX5M53RZMjgPksRoPf2uizVfFFv_v1B9Xz_1pvsmd_XVOOkzhwTc5atQc-wo_asaIVFFllycQQpDncLg-3RqpcfR10OgKRH5JY1p1XImrCIsTzC-X-3hU-9yJbdXFkteACxKVHw02ESP7QWoI3BQMhZabPk4WyqrH3bEVNFglbx0Ncv2vzdJ79-gUlhQEJQRXw2o8jPcSc3H_JJ1OaccXym2mnTJIebEQzXTQXU4lXEMxgWCcrel5U2nAO46sUzidy6qgWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ : اسرائیل و ایران باید سریعا حملات خود را متوقف کنند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5403" target="_blank">📅 13:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.     دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5402" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGkWfkgfB6PcI9MNu5prwMoVW-pj3SuigqTM35cqN-TAKB07qz1NBla0rh1hWYoBQtiBDBlbbukhSdbOKqRjNpUQxnr7u0Br-u1gDSUE4qMw7z5FzkPPqR13DfWDPoWDi6hBPX_HBYbabo7zcOhNaU23R5po2xNydYLvhMwDx32dAAHgDWPp1ctGL3m9pWOenRGxzMP3u_8PXNuqc7LlzLAILIsWUE6RbQkk0sTYy4GjrfWq-K3N2VG66rwz74t4vCdMOuhRIvg0yyDrHFv5rN350SM7Qg8zWC0DNCbnz4GbZMxUGWt1KWltt6dlqcqAMx5j9e5-Z4HCHfNhSjoBaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.
دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین شاه ایران است،
امضا کنند
که :« جز تخم نیکی سپهد نکشت!»
متنی که در اون نوشته شده بود :
«نگوید سخن جز به داد و خطیر
نباشد به پیمان او بر، زحیر»
(هیچ فردی به خاطر فرمان‌ها و تصمیم‌های  او دچار آسیبی نمی‌شود!)
در واقع ضحاک به این بسنده نمیکنه که
خب زور دارم، پس سرکوب میکنم و حکومت،  بلکه احساس نیاز پیدا میکنه به فریب  افکار عمومی  و فریب ایرانیان!
برای همین دست به تهیه این «شهادت نامه» میزنه.
و از روی ترس، همه بزرگان ایرانی هم صف می‌کشند و گواهی میدن که او بهترینه! عادل‌ترینه!
که با این شهادت‌نامه، دشمنان ضحاک به عنوان دشمنان یک شاه ایران‌دوست و خیرخواه و عادل معرفی می‌شدند!
کاوه اما این بازی را بهم زد! یک تنه! تنها! طومار را پاره می‌کند و به ایرانیان نشان می‌دهد که رنج ایران از ضحاک است و آن دو ماری که بر دوش دارد!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5401" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
انفجار در غرب و جنوب تهران
🚨
انفجار در فرودگاه شیراز
🚨
انفجار در کرج</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5400" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cN3e4jVlF78gZ3480lilllQqJNNAjg50PEDMA574wN4HwtwnrO4MNiPvIDebiA_JrIuaCycdiNAWGe_F0FjDUwrx3GbTsuUNqv2BOavDrx2wpd-fjsFtCp7VEt8XX1qrmH9-0TQxHAQD11ryxzGlKqLSbiBX_HTpi_Df885ZnhJX8qu_h70oZwEQYi9q4Y9g07hDbPnkuUtSfkQaamg-UVU0QTFvRYF5LLU-_CrNbiQlU1950n_6t8iKmT9rhKf5jMhKg_7M-X_bTF_fLIT1XQm12tw_g8SeQpBHGWJ5jKbZokHsXbuncXvWFK7QGUBVFiOhSuJnxQ8XJw3XrFCd3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداهای انفجار در تهران و اصفهان
🚨
حمله به دانشگاه هوا - فضای سپاه پاسداران در تهران.
🚨
گزارش‌هایی از حمله به یک ایستگاه متعلق به بسیج در کبود آهنگ همدان
🚨
جمهوری اسلامی در پاسخ به حمله اسرائیل به پتروشیمی ماهشهر : صنایع انرژی کشورهای منطقه (کشورهای مسلمان عربی!) رو هدف قرار میدیم!
تصویر : حمله امروز اسرائیل به تهران</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5399" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5398">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEgLuGmWhQIjk_sk_ybC375ZuG-j-aqSI5xFLnX6LQ2xA-PtC6fdBR85WECzpo2afekyJd0w0ixb-l7zQgn--UoypN9v_q118FsdQwbKpHyNOcLt9Fx-nAV7vI_SfAkA_Kh6PVMaWm5Nunys2suoJclI2TqRlo5NahG505EMtwpcVNns3aTzy74Pt8oxuLZRL271UEYIvvPfS7UY7DOWJ8IdVuPguZU2D_nKrndJPcLJ0XGLkm1WcdW7pgmsp2VX8h3yiQ7pr9cNyOYcWUAgMzARGDg87xNBMA2glgACWVes0LD7e5LnRPgWu_ZQ8B2mGkQRJ-kMG7sHNKInMlriiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی برای عمیق کردن دشمنی بین مردم ایران و اسرائیل این بحث «پوریم» رو به شدت تقویت کرد.
۱- پوریم اساسا افسانه است و داستان!
هیچ واقعیتی نداره!
۲- حتی اگه واقعیت داشته باشه :
یک وزیر ایرانی به نام هامون تصمیم گرفت یهودیان ساکن ایران رو قتل عام کنه،
ملکه ایران متوجه داستان شد، قضیه رو به شاه ایران گفت، شاه ایران هم با عاملان این طرح و با هامون برخورد کرد و سرکوبشون کرد!
حامیان جمهوری اسلامی حالا اومدن میگن : ما میخواستیم یهودیان
رو قتل عام کنیم، چرا ملکه رفته لو داده و چرا شاه ایران دستور برخورد  با عوامل طرح و هامون داده! عقلشون هیمنقدره!!
خب شکر خوردید خواستید قتل عام کنید که شکست خوردید!
کی دستور برخورد با هامون داد؟ شاه ایران!
۳- این داستان اساسا افسانه است !</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5398" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">۴ موشک جمهوری اسلامی به سمت حیفا و ۲ موشک به سمت تل‌آویو شلیک شده‌اند.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5397" target="_blank">📅 10:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5396" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5395" target="_blank">📅 09:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جمهوری اسلامی از دیشب تبدیل به نیروی نیابتی حزب‌الله شد.
وقتی جمهوری اسلامی در خوزستان ، تهران و کرمانشاه جنگید تا ضاحیهِ بیروت بیروت آسیب نبیند.
مقامات ارشد جمهوری اسلامی بارها و به صراحت گفتند که نیروهای «نیابتی» را ساختند تا آنها سد دفاع از جمهوری اسلامی باشند،
مثلا خامنه‌ای سال ۹۴ گفت :« اگر اینها مبارزه نمی‌کردند، این دشمن می‌آمد داخل کشور... اگر جلویش گرفته نمی‌شد، ما باید اینجا در کرمانشاه و همدان و بقیه استان‌ها با اینها می‌جنگیدیم و جلوی اینها را می‌گرفتیم.»
یا قاسم سلیمانی گفت : جمهوری اسلامی امروز در سراسر منطقه دارای عمق راهبردی است. این عمق راهبردی نه برای کشورگشایی، بلکه برای ایجاد یک سد استوار در برابر استکبار است تا دست آن‌ها به مرزهای ما نرسد.»
یحیی رحیم صفوی : «خط دفاعی ما به جنوب لبنان و مرزهای رژیم صهیونیستی منتقل شده است. این توانمندی مانع از آن می‌شود که دشمنان به فکر تعرض به خاک ایران بیفتند.»
دیشب اما جمهوری اسلامی تبدیل به نیروی نیابتی حزب‌الله شد!
داستان بر عکس شد!
جمهوری اسلامی دیشب در خوزستان و تهران و کرمانشاه و تبریز درگیر شد، تا دست اسرائیل را از ضاحیه بیروت و حزب‌الله دور کند!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5394" target="_blank">📅 09:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=b0hY4OYLMl1msfWDUM5PX_9GKB0K4xXROIX5ZmUjxS5WABmDZdQ9CeEbTalPLAWoHgInDcqHSzo3mE4_qt4nTaI9tFowyD9VrAri_DW6eXwT5aKT2IYTmQC8YSLtpsrBHI1hEYa249iponWPvIPYugksIU4bQD8c2GDgOaZnwgRlfn5bqWXEE0-u7DMu0IsBywu37ldhXwVF00HTGvlBWes7Y3xDqOs59bQTDE_3NX4RqeP8pl-Ww6dYqchGkFfYV7c1L3CI6WEiNdiHPuxTqgxhMUHC9tVvq4hmwXe3sSfNJmFTXMT2yDuRAHMgaov69E_5hKpS8jPbJac-b0SVrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=b0hY4OYLMl1msfWDUM5PX_9GKB0K4xXROIX5ZmUjxS5WABmDZdQ9CeEbTalPLAWoHgInDcqHSzo3mE4_qt4nTaI9tFowyD9VrAri_DW6eXwT5aKT2IYTmQC8YSLtpsrBHI1hEYa249iponWPvIPYugksIU4bQD8c2GDgOaZnwgRlfn5bqWXEE0-u7DMu0IsBywu37ldhXwVF00HTGvlBWes7Y3xDqOs59bQTDE_3NX4RqeP8pl-Ww6dYqchGkFfYV7c1L3CI6WEiNdiHPuxTqgxhMUHC9tVvq4hmwXe3sSfNJmFTXMT2yDuRAHMgaov69E_5hKpS8jPbJac-b0SVrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی  جمهوری اسلامی به اسرائیل و  واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5393" target="_blank">📅 09:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔺
وزیر کشور پاکستان صبح امروز تهران را ترک کرد.
با پیامی که مهم توصیف شده بود، از سوی رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان، دو روز پیش وارد تهران شده بود.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5392" target="_blank">📅 09:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=FqihelGcuJFNbIOazYECAs2xFQgRL5cPf5vZ7oS0lwzVIxfEGYVXBSdg3faET6wJJt-l4TnBIR-TXN9syqT3KtnmsqG1sqBS7m7xLppsIM8-y8OwBANMc4R42el8qF4eLAK9kDCWdXYvglBJvyjFwyEcpzvlgU5ftSs_QuiTRFDipcEwHcY2qeGRHELSBYnS3CH9f6RGKL6KD4BXhU8Px3qFPfZy1ZnudnI_W2b06dm9D43lkcRx6twizb0p_5PLg5g4wUFDk5UjattSMBajOPIE203VX3kRTxTM9iLhkyVkP9xD1-7uWDRWd4pd2EwfX1D_QmV2YDzBi_6nr-LS4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=FqihelGcuJFNbIOazYECAs2xFQgRL5cPf5vZ7oS0lwzVIxfEGYVXBSdg3faET6wJJt-l4TnBIR-TXN9syqT3KtnmsqG1sqBS7m7xLppsIM8-y8OwBANMc4R42el8qF4eLAK9kDCWdXYvglBJvyjFwyEcpzvlgU5ftSs_QuiTRFDipcEwHcY2qeGRHELSBYnS3CH9f6RGKL6KD4BXhU8Px3qFPfZy1ZnudnI_W2b06dm9D43lkcRx6twizb0p_5PLg5g4wUFDk5UjattSMBajOPIE203VX3kRTxTM9iLhkyVkP9xD1-7uWDRWd4pd2EwfX1D_QmV2YDzBi_6nr-LS4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی
جمهوری اسلامی به اسرائیل و
واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها
میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5391" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SU8hE0L1KC5k-aiZnIORlGNefAaHk-0aVbx47Ke8jyDWBb3gCrh9dinLJURunKMbe7M23jFHu2axARsL0t4HMvat341_MH4rN1gqmxrcKZ3CGJXrjPOGkeWIRdQXJ17rK_FsaVbSHizj9jl-u8ZhcicA_a4mXYlwfeufO96JbBOZKEW1WvgVelG8RWFmedHDLN8ye9AgPNu6jCoPRCN5tAEyRwxyZ0lykJ36EcTv7cLsdTbDvLxx0SI1NwwEvTvx71KaaiGwLKGpIdXj1TK4F3u7R-Bv2U6R7rmm7ih0MTWw3pLRYzPsP_DKC0SWpC9OTlKwOGuhUxXKYg-DEiJo_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاریجانی هم صبح زود از اون دنیا توییت زد که غم ویرانی ایران رو نداریم!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5390" target="_blank">📅 08:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
سپاه : اسرائیل شب گذشته به چند سایت راداری در سه نقطه کشور حمله کرده است.
🚨
سپاه : دقایقی پیش حمله به مراکز مهم‌اسرائیلی چون پایگاه هوایی نواتیم را آغاز کردیم.
چند توضیح :
🔺
سایت‌های راداری که اسرائیل به آنها حمله کرده کار شناسایی و مقابله با جنگنده‌های اسرائیلی را انجام می‌دهند که اسرائیل به آنها حمله کرده
🔺
سطح ضربه‌های دیشب اسرائیل به نظر میرسد کنترل شده بود. با توجه به مخالفت ترامپ با پاسخ دهی اسرائیل.
اما به نظر میرسد سطح درگیری و ضربات امروز افزایش یابد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5389" target="_blank">📅 08:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSdNMqa7YvK2GUcb2fFgKumdkOhhDO3_p4jtkJ8QMUvbMR4kAXLdlJdO4kCfgCF0iK1MPOb8CHLe9ekQ9r0Tnp-DSEpNs091pZiof8ZVifVAoqQJR1SxsclR8nE98SrVFIMaEBDyE4MG8acZUYrzvU2YaxIGsOdI_rYiYuRKV5ZTqybrxfrBs_N8isAsoit0MoQoLz_457KgTpBpiTmqWuEjO5LPoP-Uu-V8GZ5Oda7UDyVmTbMP4bqtOE8rE3ZIndbt9sNpabS3j9TA5-Hbhbn-SHQy3RxHP57yoygNo3w8u03h-xhP2s2ysSHaSBlR-C5eACVbvrYpAUcLw_VsIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5388" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای موج جدید حملات است.
🔺
کابینه امنیتی اسراییل تا ساعاتی دیگر برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5387" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تاکنون : حمله به تهران، تبریز، ارومیه و کرمانشاه گزارش شده است.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5386" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل رسما حملات اسرائیل به مناطقی در غرب و مرکز ایران را تایید کرد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5385" target="_blank">📅 04:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجارهای مهیب در تهران ، کرج و اصفهان.
کانال ۱۴ اسرائیل؛ آغاز حملات اسرائیل در ایران</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5384" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اسرائیل ارسال هرگونه کمکی به غزه را قطع کرد.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5383" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یدیعوت آحارونوت:
🚨
🚨
در گفت‌وگویی که لحظاتی پیش پایان یافت، نتانیاهو به ترامپ از قصد خود برای حمله‌ای قدرتمند به ایران اطلاع داد.
رئیس‌جمهور آمریکا تصریح کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/5382" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5381" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یدیعوت آحارونت:
ایالات متحده به اسرائیل پیام داد که بهتر است چند روز صبر کنید تا ببینیم آیا می‌توان به توافقی دست یافت، و اگر نه، ما طبق برنامه به اقدام مشترک ادامه خواهیم داد، و ارزش ندارد که این را با درگیری‌های محدود تلافی‌جویانه هدر دهید.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/5380" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uev3eqIFNPpoeNZarXsxY1kuESBYOCnkU0trDrGnMjl1eXcBLkKwXF3bHOxjeVSYb9iMHnTTOOVMUBm0BlzbRXzUmKRQSLQjEdlpzF8_Jan5xEEnmYWbzSSKENOOwH6SD8jpoypvgsHDH-oUaTQMef4eEP8mjpRKFEO4ev5BUcxUu-wpmt5ltlEGyPfpg8Ns_QUQLaVOS2sicFGDn1xShfNA9iCpxgAcfH5unu-60TAi8Mn4Ide7ovtOO8yIJVbBFyLWW5vdEL3y1J175Qw3SZOsr48lh7Wy6aXALxqZggf7DvffedozXf77N3H-cYsHYnjaU1_F3oxTzkP--YIVxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.   گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.   ولی این بار رو بعید می‌بینم. عدم پاسخ اسرائیل، یک معادله…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5379" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رهبران اپوزسیون اسرائیل، نفتالی بنت و آویدگور لیبرمن، خواستار حملات قاطع به جمهوری اسلامی شدند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5378" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9lKcTcqm-d0HEnbrVQfONljkdlMMGOXO1wd1_OKoPpXL3OdJvVRECn_N9SimLHU__-pJ9UaC4HpsVzMqZmEmmzxUN9XvQn_v4zbFWADvLDPK9mihEe9q7YdYouEquDExzOThxRr0YJDcpgplNQ52cXwQdCPRZ1_oDCkOxLaQ6ehhHy9dWTIw_STbYSWDxHcCDuB5Sod1SRXs_f0YRiWaAa6h3XV2MlSPCb7WQDYFC5JwEYDJ0Ied6xVEDC5H8TXak-0kLBIrj-WjtY8TeNvxOGcxKYmuHoTTRcbRh87ziTs8d1nllfjfHOfScAKezygkW9xxzz0XQPoE0G_EKpPvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ وزیر خارجه اسرائیل به توییت عراقچی.
عراقچی پرچم جمهوری اسلامی و لبنان
رو کنار هم قرار داده بود.
وزیر خارجه اسرائیل ولی پرچم حزب‌الله و جمهوری اسلامی را کنار هم قرار داد و عراقچی را «شیاد» توصیف کرد.
اشاره به اینکه جمهوری اسلامی حامی لبنان نیست بلکه حامی حزب‌الله است.
🔺
یادآوری : دولت لبنان سفیر جمهوری اسلامی را اخراج و جمهوری اسلامی را عامل  جنگ در کشورش معرفی کرد.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5377" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5376" target="_blank">📅 00:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حوثی‌ها حملات موشکی جمهوری اسلامی را تبریک گفتند.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5375" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5374">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.
گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.
ولی این بار رو بعید می‌بینم.
عدم پاسخ اسرائیل، یک معادله تازه ایجاد خواهد کرد و ‌دست اسرائیل رو در لبنان خواهد بست.
چون در برابر هر حمله به حز‌ب‌الله، اسرائیل هدف قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5374" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5373">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/5373" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5372">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
ترامپ : از حمله امروز اسرائیل به بیروت ناخرسندم. اسرائیل با آمریکا هماهنگ نکرده بود!</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/5372" target="_blank">📅 23:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از مقامات اسرائیلی: پاسخی قدرتمند به حملات امشب موشکی جمهوری اسلامی خواهیم داد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5371" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏ترامپ در اولین اظهارات خود: به ایران می‌گویم؛ شما به اندازه کافی شلیک کردید، بس است. حالا برگردید پای میز مذاکره!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/5370" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5369">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned «
🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.
»</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5369" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5368">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5368" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
اسرائیل : تاکنون تمامی موشک‌های شلیک شده را رهگیری و ساقط کردیم.
🚨
گزارش‌هایی از موج ‌پنجم و‌ ششم شلیک موشک‌های ج‌ا به سمت اسرائیل.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5367" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
والا نیوز : اسرائیل در پی کسب چراغ سبز آمریکاست تا به زیرساخت‌های انرژی ایران حمله کند.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/5366" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
موج اول موشک‌ها از کرمانشاه
موج‌دوم از  تبریز و موج سوم از ارومیه شلیک شدند.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5365" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
اسرائیل : پاسخ حملات امشب جمهوری اسلامی را خواهیم داد!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5364" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCQ-JHepR0-FiyH4hn73gMn0tebijK6AOpJXnZPcVnlw2KEMNcpP8dh7HMGDvAM5yfYEH3okU0jkS8MWP2B6t1CQSLgwWDBQeqoVaasu8dnvZdnfI2WVgg6iYaQHBGjzrkjwEq68bxJMq98ZjYHG1pJJwSRBBmJdPCZDMfJDC9uX-BovPMpz-4MUViM5Co8QdxmlUKieAY_DGRJ-IFVHI1tFzudGWV-n-s0T8UnDx3Ugcn07BXqiA2zkbrDW-kIX3xZ93yM7lsnCmfCsl6AzCjliiyUJGYmB1_lEFtpcbBsNec2EuH8imFlwjrsLupGpIFedcI3EQ99oQzXHxLr2XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
موج دوم و موج سوم حملات موشکی ج‌ا به سمت اسرائیل
توییت عراقچی</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5363" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
منابع اسرائیلی : ۴ موشک بالستیک به سمت اسرائیل شلیک شد!
دیشب نامه مشترک رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان رو تحویل گرفتند، که آخرین فرصت توافق و گفتگو است.
امشب جنگی تازه را شروع کردند، این بار برای حزب‌الله لبنان!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5362" target="_blank">📅 22:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از حمله موشکی ج‌ا به اسرائیل.
🚨
هشدار حمله موشکی در شمال اسرائیل
🚨
قطر آسمان خود را بست.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5361" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ارتش اسرائیل در حال آمادگی برای مقابله با موشک‌های جمهوری اسلامی
فردا : تعطیلی کلاس‌های درس در اسرائیل.
اسرائیل : نشانه‌هایی از احتمال حمله موشکی ج‌ا به اسرائیل وجود دارد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5360" target="_blank">📅 22:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
آسمان‌های ایران و اسرائیل بسته شدند.
🔺
امروز ‌و در پی حمله موشکی حزب‌الله به شمال اسرائیل، ارتش اسرائیل  به مرکز فرماندهی حزب‌الله در بیروت حمله کرد.
جمهوری اسلامی چند روز پیش به اسرائیل هشدار داده بود که به بیرون حمله نکند و در غیر این صورت به اسرائیل حمله خواهد کرد.
مقامات جمهوری اسلامی امروز اسرائیل را تهدید به انجام حمله کرده‌اند.  اسرائیل نیز هشدار داده که هرگونه حمله ج‌ا به این کشور را شروع یک جنگ تمام عیار تلقی خواهد کرد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5359" target="_blank">📅 22:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byFZ3Lqvw0JynYA6k80t2dqR5hMjl2GTZlEHjyw3lueHgMBX_RJ8Y6Svx1xLc2bvUVt1y4Qz-dv5NpE9XZyAtOzKVBbXw_sz2jJd9sESdwIIlx_pS5jFz1-H71jptpv89x83kH7Na4cYyp1plOcCmKn_1KoTM5L-PiHaOWwMpPYa6PlYMX4hX4VWjxPJEDMH0a5vWhc2D22197dwngUVkVWd6OSJ-dL2DAYPtLdSF-PYtfLXKRAzmSo6WIGPPYjGx5EuhVIElwbCd61lumynpQJWydzJVIYrj7ZoltE1B-NSfUtOdUF6CFSEc9nDg5m5cqO7I3HEzHLud7XOuU_zJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز تهران - استانبول تغییر جهت داد و به تهران بازگشت.
گزارش‌ها : حداقل سه پرواز ایران مسیر خود را تغییر دادند.
گزارش‌هایی از بسته شدن آسمان ایران.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5358" target="_blank">📅 22:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ارزیابی برخی رسانه‌ها : جمهوری اسلامی به جای اسرائیل به کشورهای عربی حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5357" target="_blank">📅 21:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
هشدار اسرائیل به جمهوری اسلامی:
هر‌ حمله‌ای به اسرائیل به معنای آغاز یک جنگ تمام عیار خواهد بود.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5356" target="_blank">📅 21:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اگر فرضا جمهوری اسلامی برای کمک به حزب‌الله، وارد جنگ شد و در پاسخ اسرائیل زیرساخت‌های ایران رو زد، اینبار چطوری میخوان توجیه‌اش کنن؟</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5355" target="_blank">📅 20:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">جنگ خارجی نباید به اذن و دستور فرمانده کل قوا باشه؟
نباید قاعدتا مجتبی فرمان بده؟</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5354" target="_blank">📅 20:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
قرارگاه خاتم سپاه : به حمله اسرائیل به ضاحیه بیروت پاسخ میدهیم.
🚨
اژه‌ای : حزب‌الله جان ایران است !
🚨
قالیباف : فقط زبان زور می‌فهمند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5353" target="_blank">📅 20:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkW419vURLPa6rhjj1fc2DIuMnomiu8C4Z9kP4hgVA8VQlRj0ZRRleKxT20OPFGgyRBMffsluiVBg-oo9Cv_iC4sCjQ7DmsmzV2YWjxV8bYzOKXGm376-yyFiKLdmIBORj9Q-3mFR7q5bedAsnpaHNzPighv3Zmx2Ulf-_K9YNxfJVYUZLAlljH-rsjlmPm-9XZ_0b_Q8m98VbyxdyPGl1wNdNHysB2L4-PL2xnltpE4iwA23CVaIUGGSc01abEUSPssAnYXdt2S3ZrThwmqRKByuvQDYpYo1mNK3ujWuHY5TyfkcYoOZHIEahEUmGXUy09asoA94vu86_b0LSACuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!  در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5352" target="_blank">📅 19:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2dP1wHn62m4LhgwZsr1AURLykIlhH_WYIm91jLRHYM1GIEXTAruJ_MU8DPlEZNnRMYwp1Sftdl0uYVis5-s3PCxwV-3v3hm1zxalz-dSfatbaKdw4AmC4hZS1w1B4nNCSGuqc2rDduA0Dt8NfPTIDJBDBpzu8ZoZPBZ8bj_PH9rM7d_WQFd6CKl_S1lXTnwx5fhAMhbHv-wQidCy026QvHwvSKn4i-qtK6r2iHVuHmxlh2CSmBZFd0Zxr-HYm_V4J09PLpYBvUZ_amLP_E6BS2HxcexqeESMcbD5JQSZJvyZZpLvELc7aXAvHP-KQxJW1v7mU6pqM0VHcx7UWvc2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!
در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5351" target="_blank">📅 18:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQaXO29a_BztgtZz-UCQyFUSEQhQmPP9i9xzLllKk4ho_3gOGUSVQzZMipSejlEP9A7uHQvD9rmrLsEHsTTqmgtsqfeAnsXpLjot2RmcThE_KrSu8ZTUVz_lsd_ME-EtlEvAxWjSA29nD8UiXGPK5G5qFrirGp5CnGmWAZOy7sSl0usqlUHhE_UZ4C7kV2eRn2qMrXsqfVLs07XEkKyc1KhwRwK_shHwkfaKwH2Ewbu4WKhVX2N6Wxxb5qruGrxz3258KPI8DSuPej4gBlqmw5Mm8T6mStThtlxGjAzRgCrWZiodJRYQFdgYNmilmrEjxkEpj11cni-ho_vmCbRMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی حز‌ب‌الله،
اسرائیل به جنوب بیروت
(منطقه شیعه نشین ضاحیه) حمله کرد، چرا مهمه؟
چون جمهوری اسلامی هفته گذشته تهدید کرده بود  که اگر حمله‌ای به بیروت شود،
به اسرائیل حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5350" target="_blank">📅 18:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=pxqDGqGuWQ_KNWKKIy2aRGOJIGWmPmr-fYfId0oJy739yuWAYcePbQLg-oitKlLKyYQz-ZQ4RUO-XCf68cfFYcdCdIMp3vQcsvVxWtE3vofw4pWLYnIZXwjovU3UFMnkEV1DwB2KHxKRnR1Fd4u2ojVu2x9Z3zmCQLqrDp_7xjWLls5RX9KJd8e_5O91kO7prcZMN-F4BQ6Lr8gs_W2AIaOFC5typSZy2nCGrSsa5us9YFgpMTIujv-n1ucYYxoyBAk8hRhhHYE7Phy_yGS7ScAZefi6_7vMNZdYbBPj55TfknNpXCnvzCl1MQnBJ41sVDhDkQSu2kcK5K-ztUY_sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=pxqDGqGuWQ_KNWKKIy2aRGOJIGWmPmr-fYfId0oJy739yuWAYcePbQLg-oitKlLKyYQz-ZQ4RUO-XCf68cfFYcdCdIMp3vQcsvVxWtE3vofw4pWLYnIZXwjovU3UFMnkEV1DwB2KHxKRnR1Fd4u2ojVu2x9Z3zmCQLqrDp_7xjWLls5RX9KJd8e_5O91kO7prcZMN-F4BQ6Lr8gs_W2AIaOFC5typSZy2nCGrSsa5us9YFgpMTIujv-n1ucYYxoyBAk8hRhhHYE7Phy_yGS7ScAZefi6_7vMNZdYbBPj55TfknNpXCnvzCl1MQnBJ41sVDhDkQSu2kcK5K-ztUY_sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،  عراقچی ۴ روز پیش به شبکه المیادین  (شبکه لبنانی با پول ایران) :  اگر اسرائیل به بیروت حمله کند  اصلا تحمل نخواهیم کرد  و این یعنی شکست آتش بس (بین ایران و آمریکا)  و نیروهای مسلح ما پاسخ خواهند داد.  به کشورهای دیگه…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5349" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=usjsvQGndmHywWnGyIXIAEcSLNe9vCL6ILCjAmMNeCgKGdHNO_XSXr_GUoVq5fe68cGdkUb5CL0q0gh-2XfCHx1lh79Zv-vdCChVqwwjN6kqz5bYbJgOGEMxQrgZoVr_NL0vAHAc7PK0l-i_DNVrOD9iYxjheHoUTSM5VI205jqCum0Uz23DbfNLV2bw_C0MLDoLHyBtifDSsDCxxu5rawpGdCJQoCxkEm71U-v7D7U1okJWRdg2tCYxq_JpMGSmA5U7uzrXALyMpgkVAYmJhDkp1eRVvjTSun7Rvl1HyxbRy2Wkxx7Rtj2Z29aViE1poUfFEgKjzVeDgniVjr_4IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=usjsvQGndmHywWnGyIXIAEcSLNe9vCL6ILCjAmMNeCgKGdHNO_XSXr_GUoVq5fe68cGdkUb5CL0q0gh-2XfCHx1lh79Zv-vdCChVqwwjN6kqz5bYbJgOGEMxQrgZoVr_NL0vAHAc7PK0l-i_DNVrOD9iYxjheHoUTSM5VI205jqCum0Uz23DbfNLV2bw_C0MLDoLHyBtifDSsDCxxu5rawpGdCJQoCxkEm71U-v7D7U1okJWRdg2tCYxq_JpMGSmA5U7uzrXALyMpgkVAYmJhDkp1eRVvjTSun7Rvl1HyxbRy2Wkxx7Rtj2Z29aViE1poUfFEgKjzVeDgniVjr_4IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،
عراقچی ۴ روز پیش به شبکه المیادین
(شبکه لبنانی با پول ایران) :
اگر اسرائیل به بیروت حمله کند
اصلا تحمل نخواهیم کرد
و این یعنی شکست آتش بس
(بین ایران و آمریکا)
و نیروهای مسلح ما پاسخ خواهند داد.
به کشورهای دیگه هم‌ گفتیم که در اثر اقدام اسرائیل جنگ‌ دوباره آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5348" target="_blank">📅 18:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=uflpwvER6b3quIhblnukljhO1TZSQLx_hWRMSaGauiJo1Lbfg4LblZnEHI7embPoPyLUfczhiQO4Q97n5j0xIrTxxORy2Ezhva6MLTZUIynWnHvJ-FezzWorctoust5PK-TCf2YUg0RNFe8Q3ML8IyWCXWcDy7z1i-gTsmH047cca6Tmh0L2fhMmGHIUg7wdrLAMm76IXyyq2YlAp141ebEf-13jrr-QmVOwS7OPTqcJ3idATwuIZ6MXSJBnXQ1FOJ30DaWDX1YEKEIbpPJBL35c0oD_vJJDSnbNHdMP5fjPd1_jU3RiMnwEy-EFDl0EC_kSSrZPuFW-ZERgBuS2CDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=uflpwvER6b3quIhblnukljhO1TZSQLx_hWRMSaGauiJo1Lbfg4LblZnEHI7embPoPyLUfczhiQO4Q97n5j0xIrTxxORy2Ezhva6MLTZUIynWnHvJ-FezzWorctoust5PK-TCf2YUg0RNFe8Q3ML8IyWCXWcDy7z1i-gTsmH047cca6Tmh0L2fhMmGHIUg7wdrLAMm76IXyyq2YlAp141ebEf-13jrr-QmVOwS7OPTqcJ3idATwuIZ6MXSJBnXQ1FOJ30DaWDX1YEKEIbpPJBL35c0oD_vJJDSnbNHdMP5fjPd1_jU3RiMnwEy-EFDl0EC_kSSrZPuFW-ZERgBuS2CDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو‌ رستم تهمتنی،
«چرا دیگه نمیزنی»؟؟
بله جنگ طلبها دیاسپورای ایرانی بودن!
نه اینها که ۴۷ ساله سیاست‌های
خصمانه و جنگ طلبانه دارن!
در دیماه وقتی مردم ایران رو قتل عام میکردن «حیدر حیدر» میگفتن، یک ماه بعدش شد «رستم رستم» !</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5347" target="_blank">📅 11:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8jWnvr1a8dqRdD0pzrcyQ5pif4dW1Ej23QZxveVVZoA_070dRlolVNjAQ8FeND_zvEyTArw71dAljTYZ4-NEawH7jaA1Wd6eMRAX-yknihif2cPOigjzZGsrglyJCMIfhGoZlx-7dSPq716Z4XZ4Xc65JquS10Z3P7xv_qZLNspTMlHw5UEa3cFf7Z0fV4gErVKCGNvP5bQ7zH4D3iVMymAGhGVDLH2ymaZ554qEtOqAidqJ95yF5yQIuEB4pzNViUyxATv1_fBenHSrKceaD79FZlz8eBlI0R1FZ8V-6UH4tScvCH51bF-HVO1dw8Bmze5Rjiyz6z8uIkkrNnIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد. در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5346" target="_blank">📅 11:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UY0XtsuqmVEyrP1DSEI4LdC6NoMhuPv6FrX1UwyUwk6v7HTv3eNFzFoXymhE0v_eky3dYtlEfSKgRimumYY2vDEIfkkgdt0j4AWEcR2xfmVXfTxzNsK0TnTjHf51XWB_HviC5KEyTdtHFCGGi1dGHdCQXhlsPYEjU9EiXdJsE1Ji4oqXbhBYJ7SC3s8leLj3yHHFobx8AgMWdE8SZk7kjaVQXvgYTsw4eyZk16O1DmXwszkj3eBJkOlfjNrl2LOCLivGygL5vybm-0FcnXX2vr3ozwUbA3vtO9blAK9egiqPUexiCuGVSLGsnIZkXI3W4FbvpPb3frUeN7sPpkB7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت
و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد.
در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5345" target="_blank">📅 11:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کارشناس حکومتی : در اعتراضات دیماه ۱۴۰۴ حدود ۱۰۰ شهر سقوط کردند یا تا آستانه سقوط رفتند.
نهادهای امنیتی گزارش داده بودند که کار رژیم تمام است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5344" target="_blank">📅 10:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
رویترز - آمریکا قصد دارد از پولهای بلوکه شده ایران، خسارت کشورهای عربی مورد حمله جمهوری اسلامی را پرداخت کند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5343" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سفیر ج‌ا در مکزیک : ویزای اعضای تیم فوتبال برای آمریکا چند ساعته است، همان روز مسابقه وارد خاک آمریکا می‌شوند و در پایان بازی باید سریعا خاک آمریکا را ترک کنند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5342" target="_blank">📅 00:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgkuyMOjowXB3YpHhJAdv-LwmXlxpSo0SgD5M1gBylWs5G6n2Gj4Bc3kSDxbsDIoSg5cqXIrcMXidhOoIsyAGb-qTc87Ss7iFkQIDvWERCY21GPzAh4wMc3O6J1BwtZTBOpGqVfyxiKZxHWFyMlSBC39puVfllMVsKVxeX_0aqfHJ7siXW4ZACZAM8RSyMPNNtsdW1DtC5mHEx-v7AQhiX6Nu-aKagmwXrP_Xo7Ug7xEKnCbTyYug1balpLdGlGyBkrKEglkJEQkWad39sbwcAZ9vt4vOjbVdQNUATy9KwcLdtXawu81TkVBZMG0rTzqasiPntgn-64xZo-xLP86aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه ویژه و مشترک رئیس ستاد ارتش پاکستان (عاصم منیر که روابط ویژه‌ای با ترامپ داره) و نخست وزیر پاکستان
برای مجتبی خامنه‌ای</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5341" target="_blank">📅 23:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Li9q3r8qiPLJbM1Lj-cAxIvj418982GvdRZGOmJrjY7Wud35vesl65366PMKherkbToKSE1SilOw4rE6aec5D6bJcABk8pgx8pShlP1uG9u-t-BXfAb-M7F1NT7vgEIJ-Ww_LEwIWdRUCSzh1hYg50i09CEVFrnTpmV71b1QqRi6-cXB4AEyDMOgZtgjB75RnwNTM6ms-X5I7ixeahyStw1zuxj-y1yWWG8iewhZizJgEFIy88GuBB9GWIdNmnnjKr76cdOTEytjuiV3bxmE_h2lc46RTAQu9kVr7-N8NVjE_XCf2M8gzGjy7J6EhekHf7bl-NsgWDw845bn8mDdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونهایی که فرانسه و عربستان رو دارن
توی خونه‌هاشون نشستن،
ولی اونهایی که جمهوری اسلامی پشت و پناهشونه، رفتن توی گاراژ و انباری
و توالت اونها قایم شدن :)
با این توصیف، خوش به حال اونهایی که
جمهوری اسلامی پشت و پناهشون نیست!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5340" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_AYPk4pOlQD0cIF6IAqIIpo4DPgjjGD5H0iMtrFy3zPVi02U1o4lzzsUCXNL3fFbM-ZimjlGdmyKjBfnMmuyNky2YnOI4aYwAMIZ5UltWMGJngGLJLuplN2KeIOq0Xx-nctQRmbf7l-LwnkSAKA8ZFc2L4T44pKaQ5m-q-fYyUlpKX_FiwXDmIoyqpIkcJ_DzJcpuuwBXIiexugCUHgCDWroSzt03mMaFpUEBJNwsV1W1IhWacdBB1Hjf97WxTHKxsxDMdd2-x7Y9wTrt9fHH0M2Ff2gWd13IGrH4se1dZm8muZu_q-hWlqOZeczFzy9wcO7TljX68m9NVJeRtIMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.   ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5339" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDxG6JqPZ0xhDSb7JcEyZdJCkcLtP86tB1Iyk3c-77_ewh2bLAAyfLiD9EvvKCZ6UnKCxpbxATi_3lZ1_bTemZ32o-KMgft9N7k5ntxIZ8-5PgyUu7K1v4tF8rPauabpSJrg4Qkzlyw6z8zXUU0lPnnEkDK4zDWXAxuqYHl4i6sJYzHpB-1L85v2dFHhB-jvoCc7l1xzPE9Dhv7pIqQ8yqaMMMBlMuNmQtjW-x_XbRiiOu9LKEIx5TWe6F5lfX6pe5vDa1v4CyTYF6ASuJj1GOGyy6JKvCX5yTN3XttDIIy-MlZRhsZKteTmoEtHO38PikGkbYsT1FVZonuujjFd2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.
ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب الله از طرف دولت لبنان نیست! حزب‌الله برای شروع جنگ از دولت لبنان اجازه نمیگیره!
🔺
این جنگ رو حزب الله به لبنان کشاند و باعث شد یک چهارم جمعیت لبنان آواره بشن و یک پنجم خاکش اشغال بشه! به خاطر جمهوری اسلامی!
🔺
جنگ به خاطر لبنان و منافع ملی لبنان نبود! با اجازه دولت و مجلس و ارتش لبنان نبود! با سلاح لبنانی و پول لبنان نبود! به خاطر خامنه‌ای بود و با پول و سلاح جمهوری اسلامی!
🔺
تا الان هم برای خونخواهی خامنه‌ای بیش از ۳۵۰۰ لبنانی از جمله آنها ۶۰۰ کودک لبنانی!! به خاطر خونخواهی خامنه‌ای!  کشته شدند!
🔺
لبنان و اسرائیل ۲ روز پیش به توافق آتش‌بس رسیدند ، سپاه پاسداران اولین گروهی بود که بیانیه داد و آن را محکوم و رد کرد!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5338" target="_blank">📅 16:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGKesFx-6rcMiNTx5K0_I_cx3ehR87j-BeZl1yKlSIqEqDMivn9MFobb8P19OO3mKl3RgITSe-GhCbPAxqDCJgXTF0aqlLZoVfkG4u76WZ3SsMAfx8nS8hwnXPiZPpwPCMXKB6vgioqeobWxjcCH4bPTyj2FpeEQWImv2HPJ04EoYRXkjzrJVFyBf-1MD3CGnmpXTl9t1KaUSHz7yKn6P8NulSSPFcRYmH33-oTP9jyHWFzg12pagWa-l7UXlgevqKr5mgBtNj0WwSgLF4fM0oSF2suDjSbHgA6JgyV8umMQ0kvrPr_AjARTtonOWzJrgIa9X-EirUMhP2iq1DvkfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZiNaFTmWGYH6HFD7D8LWtGcUKLtDCYOCauyFGQ7cWssRdamb04xG9rvo6n8QffR-C5ZNW5kktbyo379OrMG0AYxOmePPlZH31pJncEDNAWxVrO6TZA8YojeZZnbiuinv_dEkTP7Mjo0bLjxy4QtG8S28_B2vQ3_6P2ZzQoLYY14uSzveZ_3S0gOWqk64Yv-z2SSOOoFc8qAMomn_nGavBHGnAalVLcdNK5z0DUHa4VuW1d9Hu_q0X7VIZf7F-AX2iePv3f1F2z-sNegzE3VdGnxe2SW4vQimi5C8GPH7n1hMfy5dsBq6XCrrna8CN-U2hkJFF8ukNVbuBY8VAZb0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QyIatW_AU4r5l0-8YWGanxl1st-5K54cDMjB34h77PMlcigpko3A_zSiwoA3yKl2g0ZxslIHz9TYlEI6cJTBghhdnaQFp96vBspix2khAz-Vounb9NQdf9szuPXqQsfC4mH3XYVxEsw7VMYjqSsGh-OcsO_BLV_wS-C_MKjZbPpGPmB_SBwQHLkTN_F86nNV3HUSkUswf62m9r31TE3nVHaLLDNdJ72uhGwVL1X90M6fyBJQECEtCc0MDHOxMNE8Ul0rXCAdSMahK-cqVu0A4tjKvJWzgVLKvSYCyIPyCSVUDxHlLVdSxpGrnnPYinerRca-bYEikZznabRPFRfATg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=ejIBHGWPqLiGpjJ5AeHoleucRPWCsfzL4UqexGfQOcdBCFj4eHGYmCwNQdZt1QbagTJSMnLBI1JefByHjEbus4RhuFyM-GHdRPpfYdhE-6lIiz5eciFDF_qi-XdoVsjDCfkUC_Gutj1fl5C_1aaQgw_T1GSFTYjElNSRZv-Wfm0HguJ5INPDvtO9V0W5FsnLzpIPQomOruiWtOhURMt6Ov0ZB3nsJJtG1xT_mJDF2X32y5qpt1RNkmyfFI2aLuMKBr_RPAYHDKX0bW_yA6IX65hjUYQdSLi32yyCnpJU-nukQK5eXsFdIZyCiO1EienBI3rHc1mCMhYX_RgCdQB9tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=ejIBHGWPqLiGpjJ5AeHoleucRPWCsfzL4UqexGfQOcdBCFj4eHGYmCwNQdZt1QbagTJSMnLBI1JefByHjEbus4RhuFyM-GHdRPpfYdhE-6lIiz5eciFDF_qi-XdoVsjDCfkUC_Gutj1fl5C_1aaQgw_T1GSFTYjElNSRZv-Wfm0HguJ5INPDvtO9V0W5FsnLzpIPQomOruiWtOhURMt6Ov0ZB3nsJJtG1xT_mJDF2X32y5qpt1RNkmyfFI2aLuMKBr_RPAYHDKX0bW_yA6IX65hjUYQdSLi32yyCnpJU-nukQK5eXsFdIZyCiO1EienBI3rHc1mCMhYX_RgCdQB9tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه خبر ، پخش مستقیم تجمع پیرمردها عشایری برنو به دست رو نشون میداد!  تشویق برای پیدا کردن خلبان!!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lBLk7wPIFiZKf4556KmQX4SN30dHuuj8EH9MSBV3mP0PXrPbh-KLSK3LH8g47UTwykxe20hv4ooendeNjFAfIHrTDsUAI9D3_0sjBwzQzL0W0F1Z_2qYew3V-iO9vdYBB1xVB8NUMtODuMy0i3w6imNhezpZ2qGqZxSnxQG5O6u0iWWV2t9VfDfDIunFObo6jeXSXEGh4E_W6pwxZdZ5oMd9z7OfdrA-p1Pdv28Y_wKM3dzwufK2GMe1YcI5FaxznGbVJNA0kZf7s5LJ2GJamj6ASfxWEvIkYiyd8uNCBW-iMXY0iU_dLEpdvYMP7JUCYfz96GMd1DK5Ha69x9lgrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7ER-NbiMh4NenIKAwGMgFUkxoehH6Tq_BoXkLMxJ9jQWqZabrMuzJsVw6NncyUrTl6oIiMNgOMxV9GdsVBPXZBogfBncfo0CfWuKRDcdaP3LECe5pgMpg2uGaaMz625nWBnDjng5a-kZIMFhTbZFSeqe5rf_2rTdc7NYbrqrKvz8HubItvyuLmYY1K3cDiFmkN6BTaRPgK2DT-k0ghiovdbj2j5uKon-UhZlOzR8EQqxcnCdVmDZvuJUt8sVv8zp-EmQ9ho1UlrC9vVpalyT7FXgcvGqe64tP-WchDxdkYaJwZ4N_n5KEQBHmYFpkmDL7SmyOd9PRwKfIsqRbfjuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pGAKs73-k49c6BxQnoANuvQWW4OJG0uM48Bz_LvsSM6NWRYGy8KhqZ94lcOrneq_Rl0ZaUKl3i-GQ8GBatNKcdoVldL9f12hTKWF9hTswy3rLS-4_6XNx90_EeaoHIH-ogobHMmgO9D3lQn-XdYTwPU_6szS5HzI4or4diE7x2sU_SBpWdUEc1oyZ1NzS3_oegyoLOcXgd3Vvw_-ZJowxuDKvpUhOA7DRJBYwUSQMEOKJWQXikOvV-4lqy9Ik1TaWvOJjFVduOTc7MlbZunTvEYK2hIuFqBkqiF_bDoPDRTK_1KtBU26C6UxzRxPcl7EkEfzGywpUPilSAnGqw4KMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gvkTOg9x_RSAw2Y2RjeQSRWcaIeLArb1-RMHJzkC1lgazQfjrv6sjFAuvqdhRmsZJAomUxL5WkE2idfraA0RlNyMETu6THi66dNjX1cRwu3nEmONd2vVaSLqcF5hbUg-9iX7sXhLwk3S7Nt7oH4wcDd9pb9KLSs3c_oY5sZFeyOD0gIuuKcxdkiFJtCRV1R6hY2sVVyafL-8pRVvI6OlZvNv83iuRIiRNpuRLbAumyT3yP9Zz-fkh7Xn5dOhrm4h0Hjf4QGQOx8xOOwN7pdzHSiIEiqlLJ_C19xgXgdX_aKNcXJEeSLjZCp29WTm6szo0dXCi2LxaBTAzUxq807VIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صدا و سیما مارش نظامی می‌زد!  مردم رو بسیج می‌کرد برید خلبان رو پیدا کنید و بهتون جایزه میدیم :)</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=SJZwx4p_JlTY6qxGoeB_dshJSy8RCV3z0FcDWvJtDO_5x3kIwJlAE2kBMsWO4d0SDuvefLVxiUKXOFX1RYRTktPPCumC34XGi1VNYU4V0YIP2me95yZyN9s4DuUztGjq_HkHQjyVp7M46j_qeGjIJRYDJ-EP30EpyCvxeeDE64D920iSPPEkR6Mf1SnvajMpQU49C25A_LuerGkjwsCrBgS6cI1w-0MH8yd3636lkTpj1M_G7hy0OthCnz-cP2A19wH2TcXjZrQ7-IBSfouBEmjUYitnc_iGfmeBdjYQEol9NfK0G8UxjH1ix0Xij60bTeMT7wtMv4Eq0NbKp8FQhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=SJZwx4p_JlTY6qxGoeB_dshJSy8RCV3z0FcDWvJtDO_5x3kIwJlAE2kBMsWO4d0SDuvefLVxiUKXOFX1RYRTktPPCumC34XGi1VNYU4V0YIP2me95yZyN9s4DuUztGjq_HkHQjyVp7M46j_qeGjIJRYDJ-EP30EpyCvxeeDE64D920iSPPEkR6Mf1SnvajMpQU49C25A_LuerGkjwsCrBgS6cI1w-0MH8yd3636lkTpj1M_G7hy0OthCnz-cP2A19wH2TcXjZrQ7-IBSfouBEmjUYitnc_iGfmeBdjYQEol9NfK0G8UxjH1ix0Xij60bTeMT7wtMv4Eq0NbKp8FQhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی هم این مدلی دنبال خلبان بود! در انتها هم نه ارتش، نه سپاه  نه عشایر نتونستن پیداش کنن و  سهمشون همون شورت شد که عطا مهاجرانی از لندن نوشت باید این دستاورد حفظ بشه!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

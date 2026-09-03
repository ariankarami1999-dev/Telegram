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
<img src="https://cdn4.telesco.pe/file/odMzl87i0JB-7YA73nt40ciO9Ig1DWW51iGAkIV43D_yAOf5r4bNUu2FjGKox8OCbmHHoqiZFqRoAjYCieXhE9zkgveTET9MlrUJLI8siylCmQkQkOkRRE_Q_E4jwgv4cDm9Na-fiXBootKlb7XuL8y-v9wnOevkTSFi_xLMDeV_0Y5AC0ueTDaWZptx8TWjEH01C9wI_jexQ7XwK2Mr7Oh6k2xZceEc7IUKU1SFahxfF_oRtGR5BJpZKRaBvAzSLnxcuVVvQWxtITho8bqVJZnWZLd5IMa9M8Gf5bOBpXKm9hF7lONBrS9NEh_bUmkuCK1AJGHkTyjpItX4Z3_9RA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 12:48:51</div>
<hr>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsto6SnBp_pi60gd21bENs2IPfIOgAbWrPCJxtlRTSApICc1zggjF2Y7MByxAXnkx-u3Ys4YWQDZJEii0f_W4GiD1gIShvgzQqrWwBi_ppkRxeXGbGQQP-jXFv5gWZHppGrmiYpimg2XruhykZrDYNvPAzZVBxd2W0z3nvJ0a-8jnGD8QabSlnP-HtHnCAO_pT6EvWbCFCvh-3NqcoPUSOa7jIXbGe1oKXInunZLwy8XLj4giZKn8hlNaYB19MARHMygRn0Dwwxf8xXBucL7kyGhFuNHgRvp4ATh-7zPqXJJAuRhPhWIT3UiKMHVTkzY3h6ZSh-4AO2LFZl74ZP4JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKpL8XcNjuSGgDo9_lu6V_4QskFWeO2xeOjdfxmlZ7AvsUIYfYrgIZn5EgiQSrnX-61crc0DH1W_2EpWnADkqjPatHdfTd0ilv6y7g0V4oLVrbZL5sGG5mQoLEqemhHTDOZtv5M8wvMcfFcLQdpBiY0DV0rxADtujt21oWItnQ21XV_53G1GoIfX_bKnzgNccChoj9-hriznKywmzdD2egGMoBAVAoyKV9jcI4um6iiBPjtp6C2Cxl6wK-smoeRQkEUANIUnTFKTcqPYqZirQK4ABXyAttHrhfJBO22h3z162Bg3yYaFOzqYaIDUYT7vhXl24TR1MX6mnLrv1ivvhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMIuzHJp8QYZ-tuQQyQLvdF4D6ZcQYZGKh5kUgNhm9XFYRA_mO6GU3df1qCyR8_kyZcbW0anC3Np_BSsRTxzMJlpES5wzqoHVy4RNJvHjJ4MEANUi0HocILgwr7f68jcEY3J06I8CRL_uaBVf8FeZhHDyDIeY0kwk6hhpeTdOKiLUeU4nf5kEiBRlbMFy5TS4KcE5_eDrjemdVi6gsoZTY0imyx2_4S6ZhnXngeGD07vH1h0U0aeeX_x76krlv6eAGg4j6Gt9f4ZIKFuG3Zs8EiPV0JuxmwTZeoIZx_-jPXA_-DRrKCEG3sQQTBBAbtKY2wBeLGuLWJ_QXyJKP30WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOXmMBzj1gtPL767RKTF92jto7e8cWxFLMPYeONe6lI3a-pCrmTnKv6xwd3pEhevMC2JuihD-WohScw13uRH7dUeNmWaNumzWTX7txVzRQwJEz2zpltW60D0soqLEdyGDXWhy1-ablGG6_-NBf3-SGSvf99KbId2ger4exy46K9K0S9lVfvyEwHVGRbenqpCEIchMhCMym4nfJZH488RaZJ7uzZ3YngmCs-laco3dyrDgC-W9zL1qjzA-x3h5jxzYVrkMry6XdUwmjVao5DlYuxLL3hZuU3BT0fb3U9IVsnp9fbbIUtZtxTCrEfX5eKvH3WYgvDpu53SN--vMjt9aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WdEsWjej7mEmokP6asnb70Lt2eFWtjPo6x3B0RDpKE3K8BG-b0l2gxTPg_69UilzAOcSJnlIdLe-RpPpiXx1FZ6vPYXpvD_9t85qIwAPJH-mkzZLrCkAUK50ab6J_XFDFb1ZA4yvGGwvUAP-OkjjMeVo_Qsjb3iaoOGyWpDpoGZFmJnZ9ZlH_yGs9wW-cZAckxJ4ZfkysTXzMXn3XVoD3DJmnguDyJLR-CJLwlY25ZcLQvePNkRkmie3-5va7GKsDCKlMmfe3l__k0wYkDLPvmdPVe4VusOdf6i3hdRs7wnq0jImOcY4jb-1jo-7YRSt3zED3k1pYz8lFrS59GFKmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nW4uDwOybgmv7CGxBKQqpLCroTddtpw9ofUDU3OIIqexjMWTH38Lou50yPLMTY-AbGpoVj2Lv96ZmVE5gabnRpL5MFe6jOrhvuV6U9HkNYTfu7Ug5WxdSBs5m2MLhUA51Y9Pv4WT99hVJ2TJejAiE7aRKfyCiDWuusRaV-symHoaX6UG-prgERh-Wqkmvr-6AQy2KA-YRDDkXUTWMcHdYo9yiiXjdmRdpTJ6A_sB-lRTuMz9Ze5EucSNx7estd3ZeOUr_l5WHzcSqLnXmJXsNY73AoQJZN39sU0voCzaWDk76dH46e7tXIbesUzyNQl2QNiu9qjCocB-HvKk6oiPBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVrth0LlkZyb1w3aJ56lbzqapAjdLBA85r80v6EUhFDMPuWHgXR3EwC20JdE6T1ZaaogkkyuN-673_fKsXkS6BTWN-teIeTI2C8HSSXNbAnBP_xXQ9XfEtmDOdMYc0inbys4SCLT5o4shAduGCsJgpFvzxX18U9i8vNF6ZjcPA0hk0kFyhlv4V2pFD7P--BNFh0Gg1P7bTVukuOHfs1ClIky79c41SkiD9a7KSO-IZJtqpiUYSGN_fAN6xhwnbkFOJO0qkylsHS2Ck_c5Q_J6ahwhksSQ9YCK6awiGPuLWMbFjDE7BQ_nBhQ9WS_-JGD0g16XJBsLjphiXKqnpaWQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=mGdwr7f3S_uxClEQQFEjIA_yViTWbcJeoTcajssyIBzKPX35kREVf9anxtoKaBKkL2eT6O8kwSeOCBOjiUWEk9B6y9cPGZ6_1N6tS9VwvK8K8oTZif1QCtmVYaf0ouy0l0WPkNNbprMHt7mBJmD1CY9u87nb4Y6poxh0mC1bfR99WdHZdSdZCi9LFmwdqoQEQc5JAINbMNh_QeM_cftQr0esVO4I31MkDz19IJaOtw9Qq6_ME0NLD1EXyemY_mLCcfIuDrjrK2FIIB5UYUzInOYGw0gcZQb0-Wh_7KiT9ZdAl_Z1eb7onzr-vi31HLwMVnIdWT3wz5DmaDQYZ3Nwaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=mGdwr7f3S_uxClEQQFEjIA_yViTWbcJeoTcajssyIBzKPX35kREVf9anxtoKaBKkL2eT6O8kwSeOCBOjiUWEk9B6y9cPGZ6_1N6tS9VwvK8K8oTZif1QCtmVYaf0ouy0l0WPkNNbprMHt7mBJmD1CY9u87nb4Y6poxh0mC1bfR99WdHZdSdZCi9LFmwdqoQEQc5JAINbMNh_QeM_cftQr0esVO4I31MkDz19IJaOtw9Qq6_ME0NLD1EXyemY_mLCcfIuDrjrK2FIIB5UYUzInOYGw0gcZQb0-Wh_7KiT9ZdAl_Z1eb7onzr-vi31HLwMVnIdWT3wz5DmaDQYZ3Nwaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMbTrJ1cxkKVtaWF1vAleUk00ZtLvk0Z9lLdesjnDJNCaO8OEkLzA2ZWybbgjgwQk02CFHooTqVVWsNewvci4b6GP0GfnFI8hYU6j_R9auI8oORe7-RZHcgGdaQcUhnEk-jHoH7w71CVjkCNOFQEWUmek5mnqykoiqD96Sl-JQ4UglR1p8CbX9CvhqY2_uOWrSiPCiV6g31M_-iOCwnWghCVFIbYDBYC9y3DIxDDwiXZE5oh1C1pDUspLmZCQiEFSSmiDRDOAWT-po5fcuqFGJn3sTqhZq7f-TZethkPVi7BoRS_zmpFeSetnHN5kla9o3OGQaWtTy0JqHuKUue6tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmDjRaWue63TouEG_h3VRkHeRToos_ao4DABkBaHU9JON3q8lT3ozcHWijzjJJ3l4Z5NtpAMFL0dwSJiEZvuZfbmd1KHHhiHQ-8Vb7KaOk--XbalXM09Mq7JMtb8TiC23kNoIyXodbqNmr2U-kd4L_NVlzQ3tOM4Y_yzfZgzSJtLpWk4e2xB2YapC4BXHwiV_pgEa7ns0jDWfXiWaf4SR_0ksO9r5O6bJJ-aOGv4mjBwjgVYQfWR4e_bpnJuFAGhtfzrDGsDQTTpc6J5cxArb4D0-C7oZT0UMeEWPgTCpzZNGlJqCTcDSHJz3Y-34lFMuGsAf9U8ffip5tthHPWPmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=QLn6_Ht8IVjvvydoi7XDItHkATyjvXOsAZsDlebgN2qB3OD7r3oma9nEHwvIMYV3EEtDETfNSVaP-xMNI4SAOxIoDccoEZdaQiSVbv8VWVFKb8LQ3PX2pHetKhV6GIWOQSQM7y-tAnLz7ovchFLVxkdZslr_PFCjRaKECtAP0Ubt-OOD6N9fFevI2biGEne1hpA15Uhq7dW71QKyTyAHWWl2w3UzrR1RnYrOAtZPiHGQTlvdfC5u2e0q7PZPYh-WmJ18N4sQVW6csDIfTT9QBAq8pwMa6fQ5bqwDzyGPMOwY9V9-7k9g72UlKhoG9CVNK6LTg9pOLzl45UDoGIk6UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=QLn6_Ht8IVjvvydoi7XDItHkATyjvXOsAZsDlebgN2qB3OD7r3oma9nEHwvIMYV3EEtDETfNSVaP-xMNI4SAOxIoDccoEZdaQiSVbv8VWVFKb8LQ3PX2pHetKhV6GIWOQSQM7y-tAnLz7ovchFLVxkdZslr_PFCjRaKECtAP0Ubt-OOD6N9fFevI2biGEne1hpA15Uhq7dW71QKyTyAHWWl2w3UzrR1RnYrOAtZPiHGQTlvdfC5u2e0q7PZPYh-WmJ18N4sQVW6csDIfTT9QBAq8pwMa6fQ5bqwDzyGPMOwY9V9-7k9g72UlKhoG9CVNK6LTg9pOLzl45UDoGIk6UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=KOzncjh94cMee9BQCHOzij5pY5jA6jYeqMIirvm1jKspjt7xrure2gobg3aBPPO4xhtlLN2_uLTdpjY0bktB1AdRGnclgGHJX7tQhy_XN3CWYt2ZY9QPNYLsgvYAQAZWU_0a6xff-GClxb8x9oAbG3HDznHmts7zUg881Ct0cOQuY4dOZXpt-dFJa8uztE1cUmWFuBsbbVoU9yRUjyCREW4XkjqsRatJr6GOqDRcSXp3h_1-onHb1Dr7JOIrOb62PSVGKOsz1JpWPNxExqNTA6i6Nka_VoUvDKRkFLpcR650YGOcTqpq_kTZNJpca9O1SeSV9WgZ8noxhFeQdYfQqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=KOzncjh94cMee9BQCHOzij5pY5jA6jYeqMIirvm1jKspjt7xrure2gobg3aBPPO4xhtlLN2_uLTdpjY0bktB1AdRGnclgGHJX7tQhy_XN3CWYt2ZY9QPNYLsgvYAQAZWU_0a6xff-GClxb8x9oAbG3HDznHmts7zUg881Ct0cOQuY4dOZXpt-dFJa8uztE1cUmWFuBsbbVoU9yRUjyCREW4XkjqsRatJr6GOqDRcSXp3h_1-onHb1Dr7JOIrOb62PSVGKOsz1JpWPNxExqNTA6i6Nka_VoUvDKRkFLpcR650YGOcTqpq_kTZNJpca9O1SeSV9WgZ8noxhFeQdYfQqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7JNHrYULz8G49rBnYQyiDZQXlsVm8brjUdWBcv66W5b8-1IFMz4m2R3PkXheeJlXZaUaMZQCLVwq1_2hDItap7QCw4DipRIMV4bnCBey5DPFp5dWHtI5mfU6mGYpvDff0dj7yspvcq4rl154Y-b-hjRumoLO2ReaTt9D-3HGTL0WGDgeSQ0L01AuiAb4Jj9plCMXw1TTdHar21jA-UfPyV4ZszeEfc57nizCwSzywAzCG5PwNke66VROI-ahGrpcK7UFY8xfqwEdLP4WKY4lgWd1kuwhkHBLllzDoJ4nP77QmpM-x3EXlalxOb7vDEGVbb0M2KSZsqdK2jTI6EsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHm4CvaoENjVNGT68RyfK0VBQNL2uTyRPhH48Xt_YnEtG_qjLFkjbt5LDOvlLZD11f-5hRnS04g9kvUYZDWDEQ90Wg-5me8GPDTzMOlwM6wIeLp3sWCajLXi7WGKiQUSEgTzR_B6E_nzPANNzeFs1kvuIyD7mlc5nMgXwlgMH58Znpcuj6sqMex-3Gy7Nnodx9cMb-ZJ2ELvWVAtagJImvl1PNv-xVxS8-5Ue7PYNER7wXwZy5JI-PsOWbJfzByInNKUrQz7_8pT0SsTkYOoKM7mfbyt9rSFWIPEMw2V_mD1f6LRQezs_tpw1FPIml5Ew1nLV4yGgbcOFnDoR0El_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8Y7IKVs5EAsb1VYeOwnqnkbOg2NHjpa6T9X5V0IIUlDmr1PepAAKU0V8bPTKx7MwlyU0B7znUt_IiQu9Ix0QjeYqP86OGb2TjG-qJorSjhl5InFdawc8eCnWPcykKfRTcLaiD-7xnQMBOxoHqMAnvWQCj3KAfFgZEqkD_pGHDtCf4V1B7a3cbftMTqpjYTLiSiRweS4w_fKwDITJt0u38MSjMIYaw4CX9kmK6ZoikydqSyTSj16xtOyHvaSvU81f_ZmFPZhrXSyo6k-z6Z024NlNrZb2BAAoUIuc8PYGxbOoRIWC0fgsWM4i7-sNvsrfix-dz8IGqmxAO1MMnQPbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pacbchZbjrNoozD1ChftuEAAc0V58IsMd6-ghGep4juDAp4PKU0dDmAK-N9km78yZ3Gvc47w6J76L1_tKVQq2a0_YZ5cC5X_c_aBmfIuzgFfJkGwr4CIUztx0YHrNMz852yQka4d4rVGz1uOi13f8YLAfK531E8fmSGLoIochlhmqM4Hdq6JUbpAcQ4S4QAm_eBqum0jb_3y1gXwqizRg-kwfCFKPhvEoMCLia026nqH9vyN3VLTUMvunyg8OWELdBkMcpQz-FVxk2JI6XnzAGIE3lqK0aFsJdawwsq_Ti-tDY25Sm2SToUFxilRwtwwknJfXOcSbFX7WBjLt8VBVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4_gQUzijbDkHCHFvlW-S6d9U_V7jKY5BaMfEuzW2GUabRiXOLAyMgxv4AFif9QtiR0hBWlqOzkkl1MAmiSwR9RRWgx77_PyO-g-GlJvRL0KcMTp_YsX2MKCVmtlKpmB3qS4J-PXZsVmRDqEc3FRWMoZ-M5aylWMbSE-tJlWauZID7sTrjWPeBe6tF86EsDEPWa_WdFL1GI-AslreVnvULz48Al4HNOlF-qpJYwhewauafnrV4TFOzbJGv1W6xIKAYqS1L9eRjNr2rDc1wkIU8k_diPxATKV8M55dZgLVVDqRaemQklzRtBROYNJIbxc_-EVixlGPd37vVkvyf3qbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdE8wJEGt5PYFjQ3KE1AH-0ki7p_Dkfo-S3tV2guPCgIbbFSDgVrsAEkdemIiaH6Sxv6p4FOPuebOUKEXcsQFDkhi4mgnYVxux7omaPv4D6xALUVUTdkw8l_QD2w2Y7qOtSKvrjOl3R3piYNaUZBAXghIX-L6YNmoHME7_AHChxGQ6EuXv-aSFsxcwfGTyGbEFPP99-WscRIcbBzzp5zQ1zC_px2ADV957kwXJL9Z-ntMPMHX81DP0ydS_Qhc9NsIdyUjYqCwyQwY5qKBM-84j47l2rztN1wX5UVUOTPL4E_asDK5LlpW8ChEfpUU7eDgkn1TSRgAgrBpPqz7jae-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQrgf3AtBe7p7IEM-O5WgHyJRbEGi15KECFcwpnU9e5UmMU32huRYdZaXr-oTuNdO4AsBBJ_omWKtYwukWurhS0lfn10ssYLtV_k-qX8sUdeOb-G_sAbiXkB607jWjAvzWUpoix0sfvesc_k3-lvibWyFTa3HOnd2GHVZTSvOL6LGyerGUakDkXRxCPNOYOGGy5w6iCWEHm3d2OZCLig9MaPBQDhsLVMw7ko5YD99NUYCdkZ7sEUKWymHr0HwM8l-CO0H9gkymKYTAbt6_iqJ6PsoUyWBoeUO_HwYVZV7OqI4TZNbdIvW4Rm1pW98FYYky5Vqkjx8XJ5J3NSFOWtqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plnbGoYQHZih867V5VXCH9laXAbTPT-a4H-aIu7i0uUpeNfwHcXzp49gIRY9JCufyu0Oz-OCOAGhGOBR0BwYNrR7oKtADa4NCbqQleu90fCzPow3LUOpaOopoqEULJInT6qkf_SIIqOVyYN7zIKLNhhd1UoaXFVL6tbTObNhbX41FH7RVPqmuMB58y95KnL_lP1yIEEP1cD3zsCczrw52BNuW66OYxQ_5P198dWCKEBuRmAqKvuGxNyDSZUbPxd4MtYeTQ6Io8s6hMrh4H0aAO17xFddCRxvzpRJXPJp7vS4vEaj-4nJuBZ3gz-ppCtA9IlvbTVZX0Fvu1HIaU5y-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=aF3Rwa6y0IlKcRuamfFdU3RzW5PnBOg9M15cCRq1tcHvJZWEwen3MOUFOOfzjRhBd0rkxk6CuI3sROr8yrRHvnZUX_ezgQqqrDZWUUxpW5zEtD3M1PbMKDE3Owtu6fLFKGb30C1Itl5H-V6DA9zZczLHPprQ5vzkh0YvJWh1vY-t6IiBXWlrnF6BwWNw62dTwK2kH1Ju9oGU_hPJsMz6_AEhoZq2WolFKl6tPHDAFYhOiApElfhLiyTuTIaIXMb4UOCaTGWjSaeydV5eA5aToA51mh_6H71puV0RJAUuk8HVDRRHne-AKZjEaLR-PWFeEpUESpydvFcoJquFWk3rZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=aF3Rwa6y0IlKcRuamfFdU3RzW5PnBOg9M15cCRq1tcHvJZWEwen3MOUFOOfzjRhBd0rkxk6CuI3sROr8yrRHvnZUX_ezgQqqrDZWUUxpW5zEtD3M1PbMKDE3Owtu6fLFKGb30C1Itl5H-V6DA9zZczLHPprQ5vzkh0YvJWh1vY-t6IiBXWlrnF6BwWNw62dTwK2kH1Ju9oGU_hPJsMz6_AEhoZq2WolFKl6tPHDAFYhOiApElfhLiyTuTIaIXMb4UOCaTGWjSaeydV5eA5aToA51mh_6H71puV0RJAUuk8HVDRRHne-AKZjEaLR-PWFeEpUESpydvFcoJquFWk3rZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUdkEE1MDK1pD4q6AOJLScq9Z1ePWqDSpmDF0vzTGfBpb2cbF_1Gi58uBmTiGRYBWqg1Znxq0SVEGkPbCovcbLS0YC_kmhbd-O693nSx9SMparhMNcSfgxSqvSoTBVOq9QUU1NfTR4sRfqoxa1cOzdsoH-FhkaFWZnKQ3CYGbG_fQaYiYbEUEftqkfDPKf9q3MINP63rWGudvEjIZ5ZFBtRnuR70BwYjZd1V0hIkNxjJyib3e14u4WCglHeHPFPEd1Z8vdcow-2PPk_BdvH4htORE3tnP_6To93-I_A149XP9WoaGbx6t0rlAUJd-B_efhe4CiX_onWBn-710IKjgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=Ul5RbpFfTBEWizo_iGaSf4MFAtxn6kxWvHEJaQfnwJeqHHR5rEwn9xEhqwCaYJ43bPrNIc0BWTOI79lO0W8Hb_2_aoIH6v1SpRXgdzXT6wSAAy0B5JDRoMO-nTHcP6-VcbPg9w2diVcT_HeTXix2MOgOV-GbWEZw4PRFOImD3kl_1FLlGewpahEvtnqV9PRQltVXLwWXks97pNxRWwHrLeV0cxzgpcF9HWx5RElBWocdfnGTzpMgsrdnT6b-GDmiiC8rKkk5t-oVJuvlV6SKArctkqJWI-aHBwnXnoE8F9KiIhG8uDRY5V8EpR6qW8o7oWUzGrNc1GWEbjOZdXuK0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=Ul5RbpFfTBEWizo_iGaSf4MFAtxn6kxWvHEJaQfnwJeqHHR5rEwn9xEhqwCaYJ43bPrNIc0BWTOI79lO0W8Hb_2_aoIH6v1SpRXgdzXT6wSAAy0B5JDRoMO-nTHcP6-VcbPg9w2diVcT_HeTXix2MOgOV-GbWEZw4PRFOImD3kl_1FLlGewpahEvtnqV9PRQltVXLwWXks97pNxRWwHrLeV0cxzgpcF9HWx5RElBWocdfnGTzpMgsrdnT6b-GDmiiC8rKkk5t-oVJuvlV6SKArctkqJWI-aHBwnXnoE8F9KiIhG8uDRY5V8EpR6qW8o7oWUzGrNc1GWEbjOZdXuK0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=PoGZ8upAqY3QqgWLLm7fX9_VcMvnR4Q2-BTjtnM5gjxAebnwn8h2vkZt5_YEKin4yGv3JuwpkVGOsPzohCL9kuOaedw6DZgvCHxd8UkVsSCH53MYIOlNCs2nKDmwUwi-OUdt249Pld1-caklRgM4QUTOAh4RpqiNJJGEf9MlB1KsIpsSmyntWhxTqqLsGHv3X9DHSBGOGR2NKH5a4__cr4Cw2slb8A2N59DBaGFuozUX1aiEResXTvnttD3wsnnZhQnisVbqcvRF9WzVb7WoXVWmNScf8dbYrAFtS0CsTYp8a3f12EL1WpHOpij9-qqgqTNNUr_Bl8XOiComxOEt-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=PoGZ8upAqY3QqgWLLm7fX9_VcMvnR4Q2-BTjtnM5gjxAebnwn8h2vkZt5_YEKin4yGv3JuwpkVGOsPzohCL9kuOaedw6DZgvCHxd8UkVsSCH53MYIOlNCs2nKDmwUwi-OUdt249Pld1-caklRgM4QUTOAh4RpqiNJJGEf9MlB1KsIpsSmyntWhxTqqLsGHv3X9DHSBGOGR2NKH5a4__cr4Cw2slb8A2N59DBaGFuozUX1aiEResXTvnttD3wsnnZhQnisVbqcvRF9WzVb7WoXVWmNScf8dbYrAFtS0CsTYp8a3f12EL1WpHOpij9-qqgqTNNUr_Bl8XOiComxOEt-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c69_kU225gN6vChVPWpQO7-ffTr-q1kTxbdpZ72mnPZBCtcTYkWQbjBSjgfzKuXzHShNirMx4pAwM1wGtV_O3XEddvI1oHuoqbS43JeorirUp8ZTItoV_dvts3KqQb6YozVZvB_2BT3GKNEebb-dRg0_-PEW2hljbGcAES4CO-m88dQBFAbiHWrCe6bbHeBMPJU46Y3BRhdcbHY8CzAelu-tD7QU19nTbToNGu_c54SA9FWEdauY1BNItQwgCy_Ec7sEqPDltE5AZD6CiKR9582M5cVpLFGICemLP2yUQbgDS2DNXfYJmqhXclXyFHnRt_iEv7uwRxebblIXVf-i7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aB8BdEDZtvSsRJwwG39djdAqeUamHV1oKTtalZByvekiclH3XRZ5tsYcnerQ5mPtjvCzwZGmw2iVn9PwEyWxj1SJnkW10EqyDK4WuJOYfjJnRMzM1WK9wYb9JxYk_AlJqhdkqAk_RgIBgyP-DxF5WMg4Tx3Rh_7UD-TkdPe3ee4rkYBBwISFzMSk5EHY95qgJRnRB8fVWe9NHaSh9BmDi6sxf33aYpQYJHv80isVTfsiOxkjrg6SW3eEJ_nx9ntK83JSUWI5Okk5Hyn_7gRWdiSF7TYi3zYJYEhbbxJycByd6N-wRsVnBCD-yof7VpiBEhDcSrUBHKVm1kuB1r2p1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=e2-OoHQ79_tRFA99k6IQEiSOS21K9lh8hhPZ63WO97o82cXkRauYtuPrqIL8U82_9AXopOF8pliY_1acseMgRPYqrDCafaK8mhlW43EHux6MVYZgIWnFaYSFL3DQLFK3eLlDOOuXcaLINdPrQyzAGdiDKWRvzmMyxV9uMQnINuadjNxug5R4lhG52jA4a1hD1t_UnQ-bqdC18NOsggkoBP7j1uqrHu98VMdm3VWfR3BgRR3b20QJivuMNAdflnVATA99QCNb3PHVgo1f20A3FJ2wSbQ8CwbljrixR1yR3NUhYhMYRqUXKm6pXWDzaJIgVBBOKw8m-53ZEEf1A4HjbWKEyXYvG8xlc5du59QHfaCWaJUsznlRhYlk344bLuIhsnyyD7eQ2VTtGwx61gK2MSzGZYgJ0Zf11mumag5UorUgs4iDCvmDGvZfsa8OrHitjriz54MBPavC2t4PZ_-fdq13KLBKFs38Br02j-msG7vZryYReRp-qougvqFZ96AIH53cifwS60Y3xz_JvWeiSZq0mGagVhh46h_KSUEE2dCOwr6U4A6IwdHSMHsNFv1AdvmVcXSsOkSHZY62m7ab4i9qpNliCLqo8JwhWcA9at4YAEmO4rPNvLfKJ5Dji-lM4TzTGWIW-VbGBI-5IOUjB2gL7e0QDqZdJuo3FVgCXXk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=e2-OoHQ79_tRFA99k6IQEiSOS21K9lh8hhPZ63WO97o82cXkRauYtuPrqIL8U82_9AXopOF8pliY_1acseMgRPYqrDCafaK8mhlW43EHux6MVYZgIWnFaYSFL3DQLFK3eLlDOOuXcaLINdPrQyzAGdiDKWRvzmMyxV9uMQnINuadjNxug5R4lhG52jA4a1hD1t_UnQ-bqdC18NOsggkoBP7j1uqrHu98VMdm3VWfR3BgRR3b20QJivuMNAdflnVATA99QCNb3PHVgo1f20A3FJ2wSbQ8CwbljrixR1yR3NUhYhMYRqUXKm6pXWDzaJIgVBBOKw8m-53ZEEf1A4HjbWKEyXYvG8xlc5du59QHfaCWaJUsznlRhYlk344bLuIhsnyyD7eQ2VTtGwx61gK2MSzGZYgJ0Zf11mumag5UorUgs4iDCvmDGvZfsa8OrHitjriz54MBPavC2t4PZ_-fdq13KLBKFs38Br02j-msG7vZryYReRp-qougvqFZ96AIH53cifwS60Y3xz_JvWeiSZq0mGagVhh46h_KSUEE2dCOwr6U4A6IwdHSMHsNFv1AdvmVcXSsOkSHZY62m7ab4i9qpNliCLqo8JwhWcA9at4YAEmO4rPNvLfKJ5Dji-lM4TzTGWIW-VbGBI-5IOUjB2gL7e0QDqZdJuo3FVgCXXk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5Byh_THY_GfkyrvzT4q3BFiNSBa-uPHNirLSh_mMK-YhRiV4hs7wORgIQSzda6o2aK38AyPIR09_oNtFzBq971LeD0-yCDXJP3KLY12h5lAB1WT73XpmrnhIVILbvB12AilQn_2tGwYrXY4UxlLgEsST0P-73ssnSltrji6nVWZYxs3dvXiomFPwVSenASaGp7aJ0xymaV4gOzPeBYvleRFFx8W_4DSwTBbj0nx8Rm6bAeN1sk3V02OYJybRFPM4YfUUM330oTz7F1EYu77rUjEhIwW3xsRMquCCFvN5dc4RQsKVesAiyvoBz6cd1uU2HbtBpPmVXpDWHJms8LNng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=GCrbeEYyvAZ0dsNhzOdBzLYrZBziEzqWNoVprycPOBu_jAA7IsnvytMvtFny1Rkh8K430tQTI-LNXLqEYmBPaTIREXg1sADWZMjScp8TjLwHu9EJPAnB8PkYYcx9gz9BNYEhmtLm2MK9SSzVbeiWKSXXMaobuj5hc2jttaZf7psyWmRdRBLqh9qNRNZOgFcLUb7-YDzfoMCFlH4S8u8SM4GLxLX3v4KzgmqhFSJaVJ75lomzUxt01L69jqhnVYt5wsgYDpGJfbkMMlwbubfVobhJrIF-82z0WPN_RQ3Nuo3jy-esl2ckbJZ2fdoCp_9Drudg6zC51OJM8yeoN2asdWvAxxHcy6mj2tiXMUXGAwHnjUSj0CsBczohSlPlFNklv48V0__9Vn5ginDZa9I7IgNY2eeMxfpEAfQGEblj5IVayKP4xSttZjVi97A2MJ-tANT49VDhPbOeF-g1vOtKhH9mH3XWhznDDHPNbFfcrUPRC_CDDaft9_FW7aJLe8lHIiB9Qw_69NFrnlSGEb6fdBfU6Bh_3yNvbUAARinAxQ1uFqEnw82NDi5nShvEZtdOV0Zi6MJKjRIK8Ngj50JK-8Ox4NJuV8AxFbwqWkA83Y9vzTMRJ4y7lQN-Vxk-4z5ZGfcCrdl-7pL3aCb81778azbx0cfliVC91YOjg6LMGJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=GCrbeEYyvAZ0dsNhzOdBzLYrZBziEzqWNoVprycPOBu_jAA7IsnvytMvtFny1Rkh8K430tQTI-LNXLqEYmBPaTIREXg1sADWZMjScp8TjLwHu9EJPAnB8PkYYcx9gz9BNYEhmtLm2MK9SSzVbeiWKSXXMaobuj5hc2jttaZf7psyWmRdRBLqh9qNRNZOgFcLUb7-YDzfoMCFlH4S8u8SM4GLxLX3v4KzgmqhFSJaVJ75lomzUxt01L69jqhnVYt5wsgYDpGJfbkMMlwbubfVobhJrIF-82z0WPN_RQ3Nuo3jy-esl2ckbJZ2fdoCp_9Drudg6zC51OJM8yeoN2asdWvAxxHcy6mj2tiXMUXGAwHnjUSj0CsBczohSlPlFNklv48V0__9Vn5ginDZa9I7IgNY2eeMxfpEAfQGEblj5IVayKP4xSttZjVi97A2MJ-tANT49VDhPbOeF-g1vOtKhH9mH3XWhznDDHPNbFfcrUPRC_CDDaft9_FW7aJLe8lHIiB9Qw_69NFrnlSGEb6fdBfU6Bh_3yNvbUAARinAxQ1uFqEnw82NDi5nShvEZtdOV0Zi6MJKjRIK8Ngj50JK-8Ox4NJuV8AxFbwqWkA83Y9vzTMRJ4y7lQN-Vxk-4z5ZGfcCrdl-7pL3aCb81778azbx0cfliVC91YOjg6LMGJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnmGVOZabM_JEYtrXLmDIm42ASp4PLLlSLCtnpAJkfnCvX_eqfPzlwkifigg6G5PdWFEOQPO-x0hy5Uz2WLLUvSWePL_QDIR3q4jUYKH3soMo0wBrZ_73OMUAoBW7-O_CAGH9c0n5fb68k0BwvQ2l3tTZ6tzOBvTr-n8vPc2ihs6Qf0DqNUIIRglGP6De2Mv0BR8GOwvitO11DIYjdrcFbB4KKYPqdKEk3HOj5wXDyGMoSJtKgmda5RRWvc6He9JBXTFBU0kOKuUCptSDR4fk2g2juuxoSE_KU_u_1sQYPcshi21KJ7vSaK7v-TlEPOpIvD1ny_tNgLUvPy14z9G2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dykbeO3WsOj0ys9VWM_cn6_CYVglN993ElSrVLu8Xcy4Ilwy8JJonu7YZnkDKE3efiiSwx47sSQHllZMYwgcwSNi24w_8Jbc5XnXgLRyvWE1hAdCNBcqXOK5e6IWxH3bknsu5q8H34OlWKSryzH7RuBH99H8bPCxPog5_rV-d3n-g4V0TRMFzUxPJ1An4SQSFNVvUyWJBciiJimEuIdOtG9tKqfGJsGQ0wDG9nBnJEAFVashJqB4sqS_yPrlDseSAzeW2pDcOvD9fVqyA8MSvsPVh8bvbsAb_IUGzzKGrrCW2dwJJ4Y_DTz_L7Rq9dgfPCNon2SHK54g0hU6-GSzPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5ODTk7qBOXEVMApvOKkygDzcJ7Buy6fsMBM9Ymvpy3EcasYcpH8FiDVmbOQrZ8yxRmzfbC2mI7TNi0lRG6Bb6MgYJqFEImT2h4jzjuQqz4jekK2VxMs-40Fiiyx5dZvFNxHKPyWpKpwiIVGqd-chQ1FThpWFkeA8Ez7slpcvjWrXUlsSlrKBI_Zx5BfHXLSP32knjHXLFf0kWBPyFWPmHdCOBSdUz-vgfyEbzficBVkeBcSexwG9HGKfn4kffaEOdONg2sqp1J5kEQ6Yl-Gx8n7-_J9OdOXLzAJnAE1XpUMfqhsQIowGNmvRhNITV50PUcX5NeNber-wTUZUroD2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCzF2LdZ2RC2g5W4e4zwDgHXz60AE15LkcDgYi3QfccZ-FQA2MVXeD4sgzcXS9iMgusk_7_Iwg1VWOOasq-06Zg_0afPpiX5ErZyecbDePZYU7Z5KcgXKWXHCRMq2VvVU_s00ltLGLNiownqWM9WquD4ZgGE-DJflEJejBYk9QJuKlnuM3bl7stLxaFVff17X5XLuK9U-q6OfGKVdupGDcF8-pa-yFpBnB_6Knj325MYnLh3JUpUrTPB8i_lJ-Vt5mgruOxivsfjvCrKbnEgsaKnaoFu2biuaSOrBCWSiF8uv7zocElLTO3IQR2poghfL3I2OwSaIfjTZLxhOOZT-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLAwsYSSMep5nOmQDBJs_u_5_2UfeSlZG4skgAdk9NYSxhgeu_ClO0UwjVV0ig3rEHDdNMMPkp_Cl-ZAi1gF1ar2eP773YGNF7-0Ljh7Yb8Pk9jxGgKz3tZ-MO6D4imqL65GleCZz6zd4WbDjFHmZU9huejp-X-zU9TReVFARq3I8-rpkxbP2G7J6YOhlC0ABp3aR-OY0epDmNurGKberKNh_p9JgVN-uwTkR2TQhiLXxHTRGSGe-l6rMyayTm6xdOsrJZKJZNQ-XNt8ixF2RS6vNRcutgEZ1foGRE1lgoE2mwdUItOOZb1h4VoXwfDx1iYCgN2UhGXEaMGthYPfSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejJd5xE_CLdWqOxxerK2T5FvSOFGYuvTMV2h5z9RkU0PhkplRriL6u1BRE7OoSiVW0OVhOhz8kHsfoQ_TdUrp38F5OPsH7-X9nu89D7n0FX_Mmor_luyh42U4NbeBRpZyAcdR6JtvILMEoSjvTS_c852V6i1Fzdyse75Y0KJsKPePY6uMIskjg5d2tJS0wtrRdpikRwVuF0_RLvWYMm_SEvPRFOCkO7c4XrJU0byEFHUB63kLnDBs49ui6-p9mX0kK-BHRMSC6HEhkvsFyEimRSLySdSHU9IU-3JOg9ZFCrbUur81dnq1RF9ikRjAzJN4sTuvObHDYfk7rtzMCSNyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkIc21LhPO9B4yPIFf2R_kYgRfOzBp2wXy5yRUO7biQVzS-diYSDhlcD241RxX-wuvJ765YCWPpkqrYjvWIUNbV9nHdSeY8ja7NvjhhNAMTslgzlhLloh_AphAZ0QlWR4UZRsBm1qIzaKt0ZpiZGLD2F9vcuXDT2XShDLIK33oDh8MxdvjGjZrhLgyfs7W3CY6lKib4rHNajfCoARMuGpu-XnO4oD7HI9CW4C5NC8jByCXitOpzrEfrH9HtFNxu1qgNuVEjM_ur_5Qkrmm3osW643Jshga5P9YXZEq9LH8d2mNvnQMX43dgpSXJc-nVX5KbIv1cVwnL32DTedQ374w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyYfmQt9cQKa1GnzoE3W5MmyJBEfbTmR7D4LqSUHJkqejgZJPEVWKZ6ZJBnbxEss53bUr6fFTdA9hxgCqncrZQ28ND0xfrbuzommKBESqAj8KjE1CEQq8QCaED_OvaXy2emMw25CesyXbj1mJSSB9NQ9rnaLk-IyXCKJ6OeL_rYuzCDZUp_NMS1ezQYjszWykgovRjcuNxL_2bym-CeVDOycAYiuTeP2hPstX2viJ3leDsRJKsigF74r-hV4ux0sBbClbMwNvVbRGMf-cnIsay9MxEDuj6uTdXWN1HJvAAlxNqLQzyjNkzc2uqi2L07ACF0rDJ-cHyzPDHxyhZVeBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIHgTCHFhJBbBFoFhJ_azsJW8DeZ7-ft5KfeKd4f3rpXgJXEPFmQbbOrngQK__Nu5L3aoCg04oZrCgqzN-WGkuyzrdQFEmTP7ns5CUXdGOtGEAS62Qm3LIFzzfb9Yl2pXG1ihKhT5QHW3E-GzIfLXzpGHYza5wdXEv5qfKIUCbOtuuBqgLFcVrpI11YrbKp4jkRgxMAU2zOJ6A2EzSXEZU3gNQAjq2n1KirRnyssqx2rN7Nqmf_Xiy2tPMOkYo7hpDEM-Yz3ez476tnC4wMqR861OGYQgcv_-8nZD6OKXZIpazxvhYNuc8aQ5WyWHvsAM1zBDrgZOGXuee8lOmF7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vS3GWUlDGh4w3MzZrPyl9Wi97cQlPZm90ZWXUAzVIPvBCwbkJIwM6A4IgUF_MhCQswQDcGrGizBlM49irkZRyglFOi_cj8TlYNtbTScFwu-AjDSjcFAbk75srjmRlbUJUnTbNtTL6hww4pQPDSOE1i_Yb3MN6qS2kd1vmJZpdBZeXuRBCy9ntmVoAKj-w1MAk8O6jMt4T0lN4RCx2ImjMRxktKF57Fg_R55xzCrZcobhdpsajz80oHojLmmeHLp8mbwldfKAr-SwdMyoMaCzi__EYvPBns1rv4oSug-6mg7WwGHd6kKBsbCqr7ttLBmfEMSl_8bYo2VkooZgRmBqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9xJ2F5de5bUDS8wluOfZsn6uCmL5Xvlzt8tYta8leZKVxdHURI6dKLcY2z38mvXOb6lRHAiJvP7LlaFMA75TuHUVtY2waxQO2J-6DGwGNdF3bxxca00W6kmceElxBhnR82tjh_ErycFwDgN9JKFOncGWaz2QkxCC1ChOHHB_zTqLYWHwOujn3cGu7ffNxI9uNnIl7zjhpj0yeyWGtFBZFOKL0t9vnMMAztf8GeyrV53kY8yUIx_ueDtliztdcDzCsfk4AvADY8caO8reP8oZSCOJjm8w2Smp2Ghf-zQtgEzXZFmjZuN-QBiCj_I4x_F7gHLEXXUH3w3QVx0BrvJpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm3rXoYvSr2vF-pLjzMLTeKabrTmNp38Ca6Y9yFbzBlXiWE9MwenfvZQC36235likbrvVLa6mXsCHVimGnOQwe7bjE8PlfsOpYMSxX10XWUdco_EjtM0rJH0LY4lD1z1BokiFSG69bie-4Zml1IxbpYWZhTPemhXew383AgcYpJE9GRjjMWP6r3kISCvgoe4vCTnbYF2z8jqQrvsl7t4UV-VtYyBztAGFvNgrARBJ3nlbFg-IAimfLqGuUGIEeFSKAOU1ju1qiFsPOsz3JaHDFrB4vRqgeASDfQnaD0X-vla3n5Hw3y8nGKlZzxYrjcHiIZGhAwEsrGVjInb7OdOGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M69W7c1CtcOzgqQSAZXQcysC33cWxGBQowtU_wcNcQhLEwXpxmmB_xe3EuEOT_F_2AOc9FvwaxDQ8piBq1ouF_VMxAjC8OXiCB2FmiRW2zhJumF-_BIH7C4m6j5FpT8Pc3GU5TYm5HCbrxW9pP5Ku1gNDZjEc7GnTzSj9DH7iHLbW3eqoVcPtAjLGkT46TN1wk9rHAl9_0scW0qKYHVF2G107yldXVF7c6Y4U8-9BtafJQLmm4hZgHUmCKIl8ltV0t3ZQZvKO2uZYnOGWjcF11aD9ZzsmcKnG_BP4spLXENpBojvr5gLYyeuszOx3G0Jaq0V_UkvhROR-sHD-dbd1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/absPKN6e4JmHliFEDQedjwYaUBnlmd3I2tDfUxowregb4Nx7qNfwgNdWOVqs1LyVsQjG9yGxuTGQKWV452cXBvpNfW_YNELALaVR7tp1cBKnv7Ey1UKjhv9rksUaOwOJXuzeQ8eUdeuo9zs_5DNt5LPQ_80LEjJwrledc9SmGWt04qPY20vI8tMQKK6tLenYFdqiCzHBx7LsPME81t8_b9AHAG0SjF1ny9MklbAYD0qo7AnwbkbkqiDsvVy5hfz82Tc7DDS0qGKFe9a-gRV7LK0UQDf7lcIPzqhO0mQDtLPwaAcC8cohViOrCXgZn3m6xRdDiyEC77oMa-McUL8Pxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3NNq2jCcWUxWqDchLhOEWz_ScV5eZPpo6hrs5a9bQZGo8d2jIB9IBoCBRi0FfqcF9fONEA3-vyyFAxOqYB8krageaAFxS370wbWL0JOMn6j8dxjC_uGykc7EkeDWillZgTzdVbJ5eqbVdyu812obvICwfefLsGMosHknR5tC3bCdHHrMhmMKObVpcxkF2sSBtxMhxfN3sbWeHrialwBu2jq-2lu37zFVVMHdbqNGExueFq4P7hOuzSVjTOR1GKLXF9w4CRW10ocKo977lANWyDJLecVImZAwAQj5_JTcdeV3SP7ZPy8nfY76yAw3VW3ShGIit-uDvP3Z59283F4SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VG-XJlx0i04tiG6xEQZr3JBKGnNjvBHQevRu6kI2SQEb05JQJH6stT8nf7EuhLW1qAqI1xusW3FJZHtAwfpUZw0K69rIMKyjThxc_Cnoip3sFAAi76h3ePtrGR6CTfZXIyCHtqoetFvH4abgZg60mZ5JEc5I_-p3WCKyWS4jD0EouVnNEtQO7Xfkvg8CQ0Uoa9fV_3C6xZz_MSViocyA5ACT4cPztboFbP2bWnGFftdIMRyRNZJ6jNUYzFTco_ZxDkcIZGv_EMyo3TkCsCva85-rEJ7ROG4MPkSCLb_cOU54tgbnpO1KAoQcBsb9Iivcxrlfnn3GH_7x3hcE7f_xJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMDna8W6NBJD5LqKnMJz7FN6gyTjvpQDgrkvSBgp85ZTNHmQVdyfDGpHfdv96_P9ueXjkDVAuGnawys7hd_-sTdo7NwEyshNNHnvxAshqByP7XcQS3qG3hDHziXeP9kJQ20bWQasIvxPYu2QY7MQl_Kc9XDjOBIEpVzsxav5vEk2NlHJHgOyXuS_Utwn5t3yZnVFk2m-9nfDnd3B8sXaiazXLaiTtQ7CbZ-ZBahxTQ0cQzpsU41kbH4Ra819_9BHl2mwpguVDcdC85_YkickXxTSrSSrkAL3ay2R4z9hbuC_lH6CZAI46YFiSSm1rU1B7satjRKd3v-_r9IPBCjUCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jAOQ93fIBteapormrG-JSRptU_J5S0woDRLHMjRckuVHbEcK42ss8l23y7fsn7XC6VjONWsg4YRXXuA7s5dNqmenvaDWQ-LunmbXS5bzOugZjkzTDw_fOhRGXAWTHD3Lm9ExW11lBHl1W4o3MVv2snT6AoKp9Qv0BSGQkGh13mLaT7JYRmSFUpEFfJD4tTOQtB3btTbKK8AnNOHIZ3H2jPvR2gazn3R_kGcyaLMEoHitkS8QS2R6q5yBul3xjOMREeslRAlEovjd8pETc99ryBMuerK23A55t0jqKd1RBZJ7T9-v47nqzdGcbzqChGPbpcM7wJzde_UfOG-faaMcog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9kiIaTMbj9JqmwrhLiXoR4A_dgvk0R8FcSlSlsmsPnaEX_rR7GojDqyI5KSnwwMNZUPu2zcDAqvgs8Q45ERRULO_WjytjoUYwn2nxZEetLgxhUSZfWguF4MNv_cQ1PV00iRz6OsKkcy18lRwMbo4pCNwfUkYSoMrfphyiUHeJV7Bxi2W-wqsm1qj3nSk5e1zvlR0z46pWDTwuyQIiLZtp7T5oQDMTXSFgABFwHJaJ9MhWB7O-fIN0hZHlOi15oSlkrZx7W8TSvl65UamUiyzfyw0klbJfeLRpX6H-wD6czdWotLmXjgZjVitK5pQeWPGOlIN5k8V3X_W8asdGO-ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTSgIkBBWMcx5mcD6yFmDgi-iAbK917W04x5jFeOUFz9UseS8L71hkJG8OCIBtZl0OnaEH0f7R9jo6WsgZ3CPeebsG-xXvcnMi36-uAqrEt6bonKACvxIEXr2ppGa8WsqDi_UnGmv4tMJQunx5rPw07LlSoSW2HFg8KWAmSX84tHkJDPRhL6BdJR7nks3j7xjIVSYnWo_eozgCKSWlre7YM6TPcyjAL5ejyUUUbTGN65WllCAdPPtTyKVPOXgzIZPuw5Gav3jm_sw0EamuDPhwjzG2UrAbp-Tu7JjNWGurC2FppUalFhugAmpMj_wjIjz_7Qgeu-7oMvD8oRp_qVfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONN7Jpab2uEe-trS2WkPYzcdcqzGdNnKeDWi3K6VgGwOI6fh1EJq3N3M5RIPAgsCDWaIrwbmTmP8I9sOb4NtMMZkYcubcCJig8JsmmzYEpvDFaTuzghC_H9niCQon_7hTQuf3ihM8nEpXjbx-nLoUgIQ54HYza03DQHCc-YXeuVprNeV_7Od91CHGbCYoanLpqDguSiUAm0vSZzwrnoF6VNDHLQyKVs9d4XcOuuXSvFD_P_aj-oZRhGdVz_rv8WjScTdPPa7jURadeqWpJRaVx49osphYjsA8CFF3Bcn5fhs9Gq6kWZlkx9sAlFh9BfklHXoVUFAG3cY-nwmcG8TnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOM3keoQOPqnAZ_CBfAcFb9cmuUCYyrS_7q_V5wa1zqZcIx7szVOtDBwIKx0pHTsE3OKrUMdL38um0HITI8uAYzC0PEH_g7TH9MkTAJYacLYmquFET0oVanfxbmHhKXXwRD0ciRLLJFUQiXZj4s0iFu8ZloI8-uROFv4JkJ42RxaXGdugsIdTpFGuKCMQHznArM_EVaDs5-RKClBxVvPM4jifzvOhPZb_QHJBguJbN_tr8So4yqeCh31tgQ1qmhmL-fgrPSi11bC8h_MPMasxllHq5wdtrQi0V5yqbgfcIuFBe3fpr6jed7UVsj-0yidhKjqmRDwGbVdxkByPCYvew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tr9c-PGZFrDgMGB-q0D_zhsLgcmxIM9oqABq5O2pCDoMpv-FHvMO17XrYLQVGMg8jTamRGebvHdTkqgHDjLHcrV1KhX_kLcINROi7Yw7wt6WaOgbhygX53s9ZuxX-0pa97SpYcdp23CPOShQuReh2LY0FD6GhjFvcUpuqQxl_vKWGpc9td9OP0DTG5bSRb6kt-v_3CGvs57f-nbG0vHBTYK0C1e8yDVQ892mCKZNkEbO7hvhr1VQ79sn0DyXE-HHumbTWsIZekIpEDjyZmVnIsChzbtf1NrqD6cSS4Ip1BkphSokFuVjEOp8PNGttVaFEN1npLscEx4phf44Tq_PIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYf7q3h2zpDSR3ximbZsKSKGxi4-EqUC_nT09oBLwazv6Z8SpOZdTqpvRZRR3vAGe07KCF-Dkyfyc4DInCsuwN2cSQEjPyjdYa6TndMIlA4CjluaUftYGLPNcC4zvS0ki6AB2Y0UTrqzvIRSQSPyZ9fOyNbVMjgLbR7dBbvYHbG5rjh57Sz-mDPBuT109Wp9k5VgGB9oOGMvHpGlPqeMNUe1DGg0FEeahmMIPuI-5e_6Ub0WCSM4NSZ1i-5hbsatY8m60fLXAQi0G7vXGsojDNrLP90VQ9CUHMDRcEEuIlJHXfwdTZLLTQ1RjJi6IhJtx6hOiu5v6qga0PMG0OC_bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwhOO2wDZuKR2T7dO_0gDNmcm4sFqF6GAvyJEFpOFuiYWLRoyTHaQOG1tqRaZUZkjjdQgLrdNHS7ZTpUUiiS01QNLY254MFz1ubNZ2iTjeERNogZzLWR4Im6m6F6ovbcYAMSkvQmx0zM4EEVUt1NgNQ56XU-CSh7flLNv1blhFYNES9YNaqhSNGKpq2wWEJfss83zcHQmrAoZnymm0yCN3BC_03kmi6fu7rCapfH9TNiQcMO1VxdcupKGIStWSCe_-T35CfHjUzQTMbiKYgEsYzjY7T0IBKTl_pnhkzx934HI_xGe0sSeuAr6RcCnmsPgffus3SUkYumoQhlnEGDQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRhnNqcQp0FZa7QqRV4VJ2oQTj-mqaX21f0kI5qsQJn2EyZJTNWiE4dA6latiBnQn-3toA-aJSXzOptxMddAka-HTensffylgAIfSo4NVtHqJh9hftFrmZR8Bs46xr4s96-5xkV4_8VHcOX3_6RH_MCPm9qVOfQIvWjBkZ15KCo3Wc2EDqmN1C7q6nW7sjc72YevV-PYn2JosAs3E-XMUVxVuAqHBtJDh6NyF94gtRxzhYhosvgoVj5JpUdzfrc47_lwCehM64a4ZFldkfYRPNDvItMtwDPAzFiZsH29FU5dNsxweC6OIPK8KFSiHi_znyNUQe9fnZoCCzubPSBCtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2sY2oBysKd8U2KOy1BxOiy9rPDUnM5X8835I7WVgco7pzQ1dI_541PQSNmTBIPpoDe2SCCpLlJmWwJgFNh6jRINyaQjEr5Qtxf1GD3O8HVzRuuAsfTkm9zVQn5K_qxaJm_luYhZ6Uz8Auf9DnQWCy1cIpwuRM6tY9cZ-VtjL7hmNBKM6KYz_uDD5v0AkU3vefnt50EQJfiUfEnGnbrKHVc2OeiaiWdbEiI4hiLleLNbPMZLZRKFVqoOKTVBUjlC7qLlmHSoQlEucTNdjR-AQXtqObHcpq_mtaLamdjseNfI8ISiqnRMEPdWa1tL_cXUFuuv08nMKVyPiXobCY2TCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjpwlC0ONxcN9c5UK8s2fgVvsuylq1aq4OmKzByy_cO8-vt8Zt8nA0sEJwgStCWV2eDu8rV36zCtCo8QLGdl9RcZ-zKCXREk-seHlpC_d6KrF2hDFMcLcl2F1mzEwyVqK40r4abX12xSe8SCVktb_vw-76WGauwONgF6pvmK0W5kXFr2l0F4soQL1OyYH8tSl-gxJmpqyjVLEhyMyV0LVIh5VVN7oUyHUZsyuWU0uIoFv36SOCl1kn2OmeXcvD24T6gs7Z2Bt9RZLwLwTvcfwwItknTVFuF33h9O7rAE0rpPGASn8aaOP4jqrp9v_APoK4oSpunymeAMX1Z0ceuzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQ8AMx0-pKaN9sFPVVM4t7jidKheQLLpld61TI2sOOb6c902aQMYQCHBjUrDPumP-whd4aVIB5W11ZrjIbno511b_EJirt-UPkxMGJFCv5l1l6kXshYXmn-HLCbKmj7cboPBB8tsO-PJlK-AuhPPTpGYNClvqwOcwfjxv6csEX-3-unljZ3Vt7Ycq50cgsBIiyurKBIc-Hql1ps041Gr5XBMnTGrqWIoJItCr_UMbfVaoK614o2_70T6sWWc18Yjn2dUcvUpyAXCSvInkt3vAzZfG5Hn2OXhYFtIFfUZPhkvY_GkAjrtDP5WBAJA5SaxxzOgmkQnN60Z5y5RemL3rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmIcaUyarm6T8Fjyq5xcRcj75pS0d3EJbcVkyuutI0puMdCNtpv9M7mzbM5H8YIr8-1yW8nChbNmCo8UES9lCNNCkqvyHUjhCRo6--06VpQOBU9dbXB300CHF2jsp1vTloztkpjvhVAqe0tgEoucEyXim0Ca0BJf5bzLxn505UPFhVnUKAuQBq7onzmpIb1XmNgsMf7b60XhatTjjdXTyxrzvjKeWmQXseDWyogfnDwNPVwEubsF5YkqnVb1Wgm39rV-867tvC2p_OgdWopnp8O3YWnKb9jiYu2i4Y5J7Usr9HqjUvHUzczOW9JYnGBd3Cxii0II9Vdrj_e6ELnl4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ubzn6GKTN0142_tZKlhrSq-5Zr-sW9D5URjbsgbe0snJfZ3G3Y-CFlkGhnXiXIjVk1OQzqG1Vm-9G_EiKaAi2xx_As20Mr3aqr-rQ9szebYfkUAeDZN_A30R9M-4UyfXEZAvUi3tDCW7OWO5-BxzOwpjOsAdF_tJekJa-hHD18heLAofBWJUoXcQcJTHiZCKT6774uAV8TJNmskXQ11-b7tYsgxe3_COO_En2TxC351HTFsnxZMUk82_gkiEypsYijNCQfci9AVqdCZWtNqeiRClfyPMfwv5iwloBF8VFmRAzKxLZSIz1luy-nE68zzZpF08ZeoRycITpHgWKockvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOx0NYycMGpUVvB89biMWablFL0OZ8qhy7-4NZPY_GG4FNkvogkeeud5vKQU2uh4wQePGGluhxuA4ITDr24gpCs5d3doz-yfLziycmSjX-53KDfCDAwYsRtlg0cbVYDZ-Iu94dmrLcQr35Ldgr2S5Q0VzwH6YmEgLpK2fGg7FXxIl86gy3XnYgIuxupZrc2VpfeQPUbVhcEWEjie8zl9eDQ6OG9v2nV4ZMAu6diP0hd1kbWN0Bby0CRnzIJcTDS5RPPqUt6JYErWluZfh-BDxo9IFJFm84bxG6rVajNijOD4IXC3keoJWFjA-a3cWGknS3hDKfT42D6pX4FjJXLH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9kmIGQmDU4eUBNaxClk2Cso9QOyTJHC9YkjmZSMCZYhp449UW2vK2Ooy1gOPnyJ07qurfDhLKadssrkN8RgLKASkywdDJdtgX3c5nQQYxFvxVR_015CJ0rIG7_X3PEtV5Z2GnAv-drPVW2Ko3LXAV4r_onQfCYh97FqTasN0L4_C3aTst1Mv4Ju3VN-tyYxe4MtfvhofCGG92fS26FgFDGSa6tH1bH8mUn46VNmzk9c4wtwB_4Himb5wkM-jMArHzyC1n1dHANcNskTta4-cBFz5IqnQqqVpl1z78hWLbBRFLajjQ_N6HVzSboEVXcOdCavvl1iQs7St3Ow93kBHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت.
ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى،
چه كسى میگفت؟
این حرف‌ها را مصدق میزد.
مصدق حتی اقدام رضاشاه در آسفالت
خیابان‌های تهران را به درخواست
انگلیسی‌ها می‌دانست!
او ۱۰ سال پیش از آنکه با محمدرضاشاه در بیفتد، یعنی در سال ۱۳۲۲ ، نطقی در مجلس داشت از آزادی حجاب در زمان رضاشاه و تغییر چهره شهرهای ایران و آبادی آنها انتقاد کرد  و از جمله گفت :« رفع حجاب از زنان پیر
و بی‌تدبیر چه نفعی برای ما داشت؟
اگر خیابان‌ها آسفالت نمی‌بود چه می‌شد؟  و اگر عمارت‌ها و مهمان‌خانه‌ها [هتل] ساخته نشده بود به کجا ضرر می‌رسید؟»</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lS3dCnqiRoh0XXni0dCc81owncpk7Ez4nlx7U9gFPkvQjbNbnka1su-6HJo0_URt-QNIN0c69j_yxbYWBodYeY6T9lO_fuI1TUh12bHDp6d64ekhWG8iE3WSNGv22goW09yEhzKSDgA9FdVn4rEOFFgSOE-R6b7i1Sl1xzWoqH0pSA7VwYTzE9e183KCbw03X2XnJzar6NRb7gLVTcRYYeReggJzgga8sn9GnSLfT5iHnBhz1yZt8JmxVAtH6yOYukqyREFLsS7qOwd16fM0072CQ-1kH6h1n99DMN0RMfhZCjTO7hNGKk6GhanBbbvUUZ4OWEAUTV-l2EwkxOJBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=su0T6W6Poj4WDWXSXQ2wBfQ4ki33JsXCgW4VXR-3YXgvD5GsD8s2zmBQDxTAw-4qYxxTrINwZF-ju0bW0av9pQgKG4LTslypJvvsnvXvSOtbtRNzUJw6QRIo6RLRYICY7WjfYipFoNIeWS_Ha7FVLFKek-Cx947a2ZVarehnbo-TtNQsMsk7UpGcMF7fsnEu3y67wB9MZFl3DY_FMXM5KhmD6bV6jfB25_nY24dHr0g0Ne9rR3En7fFjFTD6FkapY1UG3PBF8PZpNOikjqgpBNEXTQsZ-_EfmJ3EmTK4PALzAm97thV33MRWJo57XAlWbj130zKFQNJAaEo8-b29nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=su0T6W6Poj4WDWXSXQ2wBfQ4ki33JsXCgW4VXR-3YXgvD5GsD8s2zmBQDxTAw-4qYxxTrINwZF-ju0bW0av9pQgKG4LTslypJvvsnvXvSOtbtRNzUJw6QRIo6RLRYICY7WjfYipFoNIeWS_Ha7FVLFKek-Cx947a2ZVarehnbo-TtNQsMsk7UpGcMF7fsnEu3y67wB9MZFl3DY_FMXM5KhmD6bV6jfB25_nY24dHr0g0Ne9rR3En7fFjFTD6FkapY1UG3PBF8PZpNOikjqgpBNEXTQsZ-_EfmJ3EmTK4PALzAm97thV33MRWJo57XAlWbj130zKFQNJAaEo8-b29nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfRyMJpjz6IQDy252dqZrgjOrHGeldTe9Cw1HkcBlx5xw8BEvQxGwAvs8mdICYWCFBBlhAmSyMedoGZoWjKD7mR5Xxl-5-i4m00QdLNJJMH1KjpAqxb46RYHlSgTcuVB87ey8giQCOizE9803jCiTVtM23zUYm2IKF3mdk4LHPIS5NdG5sVS40x-1u_zgtUMnpPpY5wqcHEVuJTuMd23gnuOzDyzP9MtQcCoUGYpaCLbVPFFjH_rT-v2TsSXBlBu4bx9byNXKzzeanwt1sxP0k7iGEVzEY2DWP_LiX3Mrq_Z_2rQS3RVFLbd3qyZwSc0zV9_CpdONQMyhPzI535sxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=aMoD0DpNvwZTdzev9ZpSkHwTycrwL8DDCv06VRvuExO5TPjUkyjFZ1DmnMnCG4mMWLuEEgQ9_ST23b2d4cLbpw0VHBIDs0SjdYOi53o4mcMfXelt00so0J76HHLiQcUV0LIsVXDGoGJTSM7rsF-fGZ1GY9GYfBHdvcvi-c91XmagV0bDGQ8-Sr9sKQHOcNKKSMvojIPSghn0kVsA5jffFW0PAWvVMR2JtPU_UJDMl8mr3ZX8JrZO_vEJyHB5P8Uelbng8IaSyoKlyJFIMXDKFeK3DhneQCvk4k9uwOQ3RcZcCjp54P4YNP0aBf0_vaqScaXR0TJchJfkL-Fv-AHUKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=aMoD0DpNvwZTdzev9ZpSkHwTycrwL8DDCv06VRvuExO5TPjUkyjFZ1DmnMnCG4mMWLuEEgQ9_ST23b2d4cLbpw0VHBIDs0SjdYOi53o4mcMfXelt00so0J76HHLiQcUV0LIsVXDGoGJTSM7rsF-fGZ1GY9GYfBHdvcvi-c91XmagV0bDGQ8-Sr9sKQHOcNKKSMvojIPSghn0kVsA5jffFW0PAWvVMR2JtPU_UJDMl8mr3ZX8JrZO_vEJyHB5P8Uelbng8IaSyoKlyJFIMXDKFeK3DhneQCvk4k9uwOQ3RcZcCjp54P4YNP0aBf0_vaqScaXR0TJchJfkL-Fv-AHUKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ak3JbrZaTB0Jw59Bb6P1x5_OiMMGNwmlVYWMD7buMew1SVWXF_bwVyMrGp9cGwjj3JfSg7SKbto1uuzDawVxhw0oUMiQ7XDwb6s6gY0xNSLq5yuhn0Hv3lyq6UY9WgHrcy8a8Sq2T5Rj2I6LbBq4bvNYmT_IeOOZNW7i6_8v8ezvQ8sKHZ6VXdPfkFLDfWen5flKC0-cGO-w3W4km9tH6l3g0HK3284xS8w6LKrZitwDpFyqor3ofBhVhv4G4ToO8FYkTQwkdPh9Q-NY27GvhXeHxOhBxokyjeWBRmZOaobnVfeH5NQZGnwXymj2TBOf4a1y7OWzKMwPHBLZJt0ZrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9Tml5qCbtFxaSrfM6koW5Z1wO6nnTGCA6BqEeIbh81pUvdlNoP2f1z8O6UIpKhGH-7IOu9b8eq68uWKY7xPm9JPmXuH3-y3Pu4hTz_WtTSCFGmPtwjb2s3XuaBC6sjy_GBsPvrifyyRGSSdFwuFuGxGmXYH_Rqo6a_6gETD6Qb7rv8FbrBNyldA5pBPXQz3z7JuCkgJ_j3B0V3ivQSFPIrvWHumvamgokINf5jcKqQf-JXDpzmT8HgBh3qlNiqczZksMnYN8gkdiEUoU3Br4Js_e1WjVEHM8Bh4qRyb92v3wE_SeIyT0lhrpUgrZFxSdAIC5CURpgu_LicfdhGvfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=aJYKtqRgbg4lO88mGMoDiokk1PFLkSGTAvphiJRQNK-XHlf_phbpSyqfjMCTD-4Sr8tNLzTuMq-Kkh9kQ-pCfFkiKzDMWPGGH_pR54lC1AGNJJ3BAsq8RRexlRkD5hwislHahnf1Q18Wsc4dCrPH1WWNooL_wfp8TOwOCzAXuknbqud5uu2ZusVTre8hR707fbIdtTuKLgEpXqHGz5Sz6sDTBRkjZorLYGBTtL8nhW3fZVt1JsR-umt_q1axQz0urWgZtVYWl9cMdfi8FYQXXwRD7S-NiYrEzxboSnp0_67P98Wy2EKspX-bo8xq_x56lSqcHmO_--W13puWWRnglQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=aJYKtqRgbg4lO88mGMoDiokk1PFLkSGTAvphiJRQNK-XHlf_phbpSyqfjMCTD-4Sr8tNLzTuMq-Kkh9kQ-pCfFkiKzDMWPGGH_pR54lC1AGNJJ3BAsq8RRexlRkD5hwislHahnf1Q18Wsc4dCrPH1WWNooL_wfp8TOwOCzAXuknbqud5uu2ZusVTre8hR707fbIdtTuKLgEpXqHGz5Sz6sDTBRkjZorLYGBTtL8nhW3fZVt1JsR-umt_q1axQz0urWgZtVYWl9cMdfi8FYQXXwRD7S-NiYrEzxboSnp0_67P98Wy2EKspX-bo8xq_x56lSqcHmO_--W13puWWRnglQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhwm32HG6KivNq05qSk7XqTmwzOeSR4ltIFINBpyjDl9Byn6YRs4VE2wxCbcOoXm5qA4SDOe6p2L0Spr8x7FoKezNG5ZGqdlSM_U6RXbUZYuEW4xP8eqP-wyNU7erVLqbsZL8GuV5q4H0_Lol5UWHKDsApYALfvIFgYw3xsntPr22NVSbMBvUjxk04k6DiRux4eWNjd87kGsKxk2dLmqBXl_Ob1wihqoFKxxraQ9DG9YWgi93tlnYyPdk68i4v1c_BzZ0fw4B_1T6fx0J-8292enwmRV6N3Nk3r5EjyskBHP1cjXZwvza0io52hhj-fldoJ8IXMPAxcGXIvIEAJrTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNEKe9XvGAXxFtaEgZxrQ29q-vOdPteG5BjI5KP2555bPy8LTFQlX-2oIEpZCxWhodyrbpknguLcw5ACu4mNoXYu21V438iH_v6uVNqaGJ94nc3Xk21FDooSoR8XBJUKZyOUbXRgx-LfI-6fl3P9n0OXcECJrjgkMgR4hnyqdCBWgdzTTcEGSYT7zl5bva7lltI5z1XTqryLC0Bx5hRdzEokoEAPzYVWA8zLQstxe3-XO4J-OpWRWQtLOuYFDifVIluAy3dk87g2d6mVVlecR0ZZm-ouWsE8BES9hgWYXJhe1Vn4fGZci1-es08s8dA_eB-Clg7O8D1B6BJ2zMCi3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kP7wqtlGBK0OJ9jy1_OkTqBLyFDhXKKqGK1K9ErH74GyavZPoL6tQsgLBn8fTaR4fKFy-bxJlk7u6Ij7c6eZD5ERJ0PvutKzY3jANIk0OcVmBLCLkfOGnma8jUwaUlqgh4DmKXFUCx3XDvxV7g7ZZZ4BQ_nBa_uLxMuq1LX4iMXXodttqEnShTxJJGl03krknvLw2C4ZF3zmBBqRC7kCCKUT65_Xb-8g2nOyRRkMbgbLGb5rviZAVlI8Z70hT5S6P22DnV02Xcqw31HRNfGwjp3U1wQHYyPsUnb3GVrkat9AV5RpMGzcokNsW7e7r6fVdsgswitYCggJqnGZKFZFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=edW8QdUIGKdy6EA25L6OGr_k94W26ckKa-rf5g4j2IMS3olawj2Pfpmsrd-dmpFALLh9HLtkHCWgjyjz8jaNSBTnGY5skljAthsU9-_WLAFqNw_kkX8Ntk-W7K_SugMZbomQe6kj9s2gQW6ZDlobFceDvAIpVo1TeDnvRkeBYhFMvAuE9OdVWGRnvQ7MRZIT9cULwwAvxD-G0MrSR_sGUFAOVKCNp95n7gynbfEJCVoLGT2asMYFxLvczEiAJFsXyQ1b_ju9ZErBBBr_NiCBZsP1aqAYYdnHkT1EmdSJJuVP3S9A0y6_2zlqA9SlrJDhACqBC0P8yHMaRNXZ7-4g4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=edW8QdUIGKdy6EA25L6OGr_k94W26ckKa-rf5g4j2IMS3olawj2Pfpmsrd-dmpFALLh9HLtkHCWgjyjz8jaNSBTnGY5skljAthsU9-_WLAFqNw_kkX8Ntk-W7K_SugMZbomQe6kj9s2gQW6ZDlobFceDvAIpVo1TeDnvRkeBYhFMvAuE9OdVWGRnvQ7MRZIT9cULwwAvxD-G0MrSR_sGUFAOVKCNp95n7gynbfEJCVoLGT2asMYFxLvczEiAJFsXyQ1b_ju9ZErBBBr_NiCBZsP1aqAYYdnHkT1EmdSJJuVP3S9A0y6_2zlqA9SlrJDhACqBC0P8yHMaRNXZ7-4g4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=nIGN1-2eJtECi4tZBgkBLs5dFLeQnqyDBj5tUjXG1uN7HA-TSyffQG-LNU1ymFwEEYqd2VdGpTv_p7huuBozsSBiN7xHwjEn0_pjLbwjRKHOqRcIUyj8LD0jfHFu-HRfopeV0pF6mXDSK-p0NPGdhnR1iE7ln7ML2rdPvplcDCZfii9FBRpuSwBfZ-yBk1rklxx3Q5ehcBQsp5tuAM3keJR5qVdpYF7kFCArdaUfryjx9W25S_LVnnb8wknbWMEgFa8xJSJs_jSldjsiFrhHBmHu9yY_bXU4lBxpUFULLQbeADTNoXkyJtF72LLaNISlnJ2dRJdyMtN_ZPXpcgriwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=nIGN1-2eJtECi4tZBgkBLs5dFLeQnqyDBj5tUjXG1uN7HA-TSyffQG-LNU1ymFwEEYqd2VdGpTv_p7huuBozsSBiN7xHwjEn0_pjLbwjRKHOqRcIUyj8LD0jfHFu-HRfopeV0pF6mXDSK-p0NPGdhnR1iE7ln7ML2rdPvplcDCZfii9FBRpuSwBfZ-yBk1rklxx3Q5ehcBQsp5tuAM3keJR5qVdpYF7kFCArdaUfryjx9W25S_LVnnb8wknbWMEgFa8xJSJs_jSldjsiFrhHBmHu9yY_bXU4lBxpUFULLQbeADTNoXkyJtF72LLaNISlnJ2dRJdyMtN_ZPXpcgriwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

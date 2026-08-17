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
<img src="https://cdn4.telesco.pe/file/bQDxknggJqln7zRwrkQSKk1uGBfiA2rIKrTZWOe1eFWTBigNziZnRqw7ZO_T61ePnJrW4UlSFqK92vRpWVymlxMD6dwDVfqy7f7HacuXy7WWMmyV9oLSPPh2qwig5tBhs8q5iiqlKU519Nk_XeFyfqh1Ob3nSfuxm6wnlhEIofvIRrGSfA17Bvmx75KRCqRWsjJ-NH8pxGyt3Asid-ZoPTkjUiaydi5TqbGE43X-IW6-RYU9L5EuSDRQP8C0ueAgUoiujOkFsbgOuDoOAPjS1inJLGxV38lrP-5Bn3EkufFRn8m5Otub_txSFWjPTICr7ugaObfqVY1yQWfyhfxlbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 01:44:30</div>
<hr>

<div class="tg-post" id="msg-19979">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اگر تن ندارید لااقل آماده باشید!</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SBoxxx/19979" target="_blank">📅 00:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19978">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خب رفتیم برای موج C از ۲ و چند صباحی دیگر فرصتی برای خرید تن و دلار و نفت</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/SBoxxx/19978" target="_blank">📅 00:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19977">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o59cz5B0UMJuPxO9jHH2zNKbVImdpcMG6KcYeOP48hVKLXLpDcOg_TU1n8MTedZLB7Vw5-sKMVJHjER17Qub8-7K35icmGj3WRFUPZ886t6Bom7fayvunaB-IkW1Z0hOITtv0riICVf8R9tvfhNkoYzE_V3f0CNQJIB6Cd3SQB54Z4X2oWDr3B83k6ywM-2OeBYhbKAJn1IaX3h9ED1MjluJIIIdkkJIoFaBPV5bjGzeTy3ZRHmWauwf4E3zPTfHZWdEdw7HDf0E_PuacomCUu36FbZgKlTPRVrBZDU9sFABGZpE9gP81tOBZoq4z_dmCwDNKGtzphW0GUajfh1D8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H4  پوزیشن پیشنهادی.  ریوارد به ریسک خوبی دارد.</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/SBoxxx/19977" target="_blank">📅 00:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19976">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">محسن رضایی :
تا حالا زیادی صبر کرده ایم ، لازم شود از NPT خارج میشویم و خودتان میدانید این یعنی چه!</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/SBoxxx/19976" target="_blank">📅 00:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19975">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vx0NoAO-2X3eJsnFn59eEcoOn6Ep-vhqrwbZ7FfJA_sH3eHCf-QhVm_vwmUfIJWvJ007Tivg1V9QOtc5B46jVx24j8oLI1E2Lp9QAR6_1n0C0kNFU5TWVJwwrlx7cxnBv1X1I9Aca0VUQG9XinReeSwx09zxmTfkpG4G1yYpGUB91PX2-Put42nQqSTnItsxaBeN6cPgr4uXi4MaKd31dnyEYKFInfUjdY5lwdi1NkuQT0aRATBFJoaY9x-yOgQzaImH5y2rSZXZQKw22Bx9HRcSXwzNBd_newrVV8IVnyit2NByE3BNmj2fwQ7c8rDjvz-EBrc5BdUdjhl8yBXekA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/SBoxxx/19975" target="_blank">📅 00:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19974">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جرد کوشنر درباره ایران:
در حال حاضر،  ترامپ بر فشار اقتصادی متمرکز شده است.
اگر ایران مایل به پایان دادن به توافقی است که آنها با ما در مورد آن صحبت می کردند تا از توانایی خود در ساخت سلاح هسته ای چشم پوشی کند، واضح است که او مایل است توافقی را انجام دهد که می تواند برای مردم ایران عالی باشد، اما در حال حاضر آنها هیچ علاقه ای به انجام کاری که برای ما منطقی است نشان نمی دهند.</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/19974" target="_blank">📅 23:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19973">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c96ziMlOSJzZO9fwwJphdtxt1YALkDvyrcw6Go7nJ4V0aP8iw0UfFLaWpA51uJo4OTpBZLL1OUiC4cPfyKWv3w8XNnyJUBDVcYAVKGnRzWpJ8ho8eOLSP9aPMP_oeldEql6MJbTWFkip22nmq9HRhNSq69j_TiIECLSpSkb-BR-RUBBEOgpwdv8GaNwnQFEOampDNe4pMP6yiatSBwhvQZKWbHP1R-yFobt0sAj6C9EB5UfveGPthujBe5wu7HdwG2Pw8pawLWOb_s7_c55PbL7fNCwmr7iQpSPuutl_GyaylIBQ7IiBGueil9pudN26K58agQCLPw2OTJwQmbZqTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/19973" target="_blank">📅 22:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19972">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ:   توافق با ایران را لغو خواهیم کرد.</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/19972" target="_blank">📅 22:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19971">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ در مورد ایران:
آن‌ها می‌خواهند توافقی انجام دهند، اما قصد ندارند آن نوع از توافقی را انجام دهند که من احساس می‌کنم ضروری است.</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SBoxxx/19971" target="_blank">📅 21:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19970">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SBoxxx/19970" target="_blank">📅 21:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19969">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ:
توافق با ایران را لغو خواهیم کرد.</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/19969" target="_blank">📅 21:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19968">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گویا سپاه رفته کشتی اماراتی را از دهن آمریکایی ها کشیده بیرون و آورده قشم!</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/19968" target="_blank">📅 20:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19967">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ می‌گوید ایالات متحده تنها از «بادام زمینی» (استعاره از بخش کوچکی) از انبار سلاح‌های خود استفاده کرده است.</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/19967" target="_blank">📅 20:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19966">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwWFSdAgYhCRgPQU50udzkyt15sy-6sE68XXvIRjL2yyLbOa7G-rh23VJA6LQbiFG_aShzHxIXAMGOlmhPTog4dNePtzthDaeIvwMzjDt0UZgkp3srqDKHSaM62wNvbWJc-p2eBJ2KlHylLsQ91DCe4M1ljVvNaRKWhAmZMQcDOp2tbmdbH4eWyg73fFJnLqKSdZpTqW90OAoK_naQlP9AKz6xfSRNwdHMWh2Rft9oHSuyrn8OHJB9cqSbmCnYLfUz4bI8UT5Fj_Pq3KK5UuvvkC8_2mF8ZeMArvaTR79C5b3-LCFE4h9aZsYFquzKRiEKBWhjv5wkQJf-rVCEcf_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم:  داده‌های ناوبری دریایی نشان می‌دهد که یک نفتکش متعلق به یک شرکت اماراتی هنگام عبور از تنگه هرمز، متوقف شده است.  نفتکش امارات در نزدیکی قشم متوقف شده است.</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/19966" target="_blank">📅 20:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19965">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تسنیم:
داده‌های ناوبری دریایی نشان می‌دهد که یک نفتکش متعلق به یک شرکت اماراتی هنگام عبور از تنگه هرمز، متوقف شده است.
نفتکش امارات در نزدیکی قشم متوقف شده است.</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/19965" target="_blank">📅 20:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19964">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یک مقام ارشد ایرانی به خبرگزاری رویترز گفت که تهران از یک سیاست دفاعی به یک سیاست «کاملاً تهاجمی» روی می‌آورد و به ایالات متحده «چند هفته» فرصت می‌دهد تا توافق صلح را اجرا کند.
«تمام نهادهای ایرانی آماده‌اند تا در صورت شکست دیپلماسی، تنش‌ها را در تنگه هرمز و در سراسر منطقه افزایش دهند. ایران به طور نامحدود منتظر نخواهد ماند تا ایالات متحده به محاصره دریایی ادامه دهد.»</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/19964" target="_blank">📅 18:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19963">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یحیی سریع طی بیانیه‌ای اعلام کرد که انصارالله یک کشتی نظامی متعلق به سعودی را در دریای سرخ، در حوالی سواحل مخا همراه چهار شناور نظامی همراهی کننده آن، با استفاده از موشک بالستیک مورد هدف قرار دادند.   به گفته یحیی سریع اصابت موشک‌ها دقیق بوده و این عملیات…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19963" target="_blank">📅 15:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19962">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یحیی سریع طی بیانیه‌ای اعلام کرد که انصارالله یک کشتی نظامی متعلق به سعودی را در دریای سرخ، در حوالی سواحل مخا همراه چهار شناور نظامی همراهی کننده آن، با استفاده از موشک بالستیک مورد هدف قرار دادند.
به گفته یحیی سریع اصابت موشک‌ها دقیق بوده و این عملیات منجر به سوختن کامل کشتی و غرق شدن تعدادی از شناورها و سوختن بقیه شد.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19962" target="_blank">📅 15:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19961">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19961" target="_blank">📅 15:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19960">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnmKk-8p9XYn4a8mAEf0ZYwLQUz6Ge2ymCPc0xDInReMJIn4NPe8nDtTV7It8xHTeJ0zu9urAtjtVyj1XMsCP3LqZt2zpmd6ZE69pUcXvfmrCMmlAIaGoLvyCkzN_RoxI9OHDXXbviqA-D91TJ1YDyqdpOfrx-4EobAJLaAmv4yqTYTrqQEulJb5YSuCg9-VMyrc9b3DD01THvQuBq7fQ3gH-QTHPFN_b6YaVgt7NT4KDr2Jn-39F2hWqT9lLnzOzph2Adg2kzuzMksIgEShxGhwsdakNvCNh8fpisPgXah_E-lp7bMU5DJq-ScfKI21N1CHStSuBGqUDkWyJm124w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ترامپ: اگر عمان سر راه قرار بگیرد، آن‌جا را شدیدا بمباران می‌کنیم.  او هشدار داد که عمان نباید در تلاش‌های ایالات متحده در مورد تنگه هرمز دخالت کند.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/19960" target="_blank">📅 15:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19959">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔹
ترامپ: اگر عمان سر راه قرار بگیرد، آن‌جا را شدیدا بمباران می‌کنیم.
او هشدار داد که عمان نباید در تلاش‌های ایالات متحده در مورد تنگه هرمز دخالت کند.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/19959" target="_blank">📅 15:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19958">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ به فاکس نیوز:  ایران باید پرچم سفید تسلیم را بالا ببرد. آنها پوکربازهای خوبی هستند، اما دارند می‌میرند.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/19958" target="_blank">📅 14:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19957">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ درباره ایران:
ما یک کانال پشت پرده با سپاه پاسداران  ایران داریم. ما مستقیماً با مقامات سپاه صحبت می‌کنیم.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19957" target="_blank">📅 14:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19956">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ به فاکس نیوز:
ایران باید پرچم سفید تسلیم را بالا ببرد.
آنها پوکربازهای خوبی هستند، اما دارند می‌میرند.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19956" target="_blank">📅 14:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19955">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ایالات متحده و ایران بر تمدید آتش‌بس ۶۰ روزه توافق کردند
— العربیه</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19955" target="_blank">📅 14:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19954">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">درباره اینکه چرا ایران مداوماً مواضع تجزیه طلبان را در کردستان عراق می زند، یک دلیلش این است که توان ترابری نیروی هوایی ارتش و سپاه در جریان جنگ 40-روزه بشدت آسیب دیده و در صورت ورود زمینی نیروهای شبه نظامی تجزیه طلب، کار پشتیبانی هوایی و لجستیکی بسیار دشوار خواهدبود.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19954" target="_blank">📅 14:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19953">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">لطفا یکی به نوید ممدزاده بگه
وقتی روی مواد هست
گوشی دست نگیره
مرسی
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/19953" target="_blank">📅 13:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19952">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPQVngRJRy6Guy2nWK3CCKmmkgWCpamprwYFvqlTPgRMSN51Kq5unVtZOIY9zKjzSTF6h4MBdfq0IWq5z6PPoZI-PBrudNK-Gqe_QAht6MWRtKRn2mX7A4aIaohIsn-2XyN59TCh2VBXHALRMe7s_KKBKzj4wc8GHUP0c995Vf5cI4Q4jW6vvCeWGBRAJOm9ZAJ-nWLJ9LQAyWxAgaIWGdxtfdK2pVR73WiSrnw1PV75L1eI3VhE8IPMn8-0ZLKhMT2EQJLqBjImAwXha7w_h6YUu4kXvi5B1V2HxNY5MV66loX50slzX5R_aeYWrw8ncRuU9KyoDXBcErYJLs8b0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً بالایی قرار دارد و افت قیمت طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19952" target="_blank">📅 12:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19951">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mU-8OI_0Ly3BGc6w-7omoxwZ4sdzLPkX08CIGeuR9-l3ASR909f-gYKlzlfpZ3kuDI3QqM_oIIcTIqeIod5iWlX5UZuVJnT4AelsUQeztoZXn2ZI-Hf1RQ65eoKkBXO4CqaFwY_f2iqpZ0hbo-xAKlasukAGJ7E27rFbUrRS_3dpE6j6NnsAu6g-CnLuygmcsA_DabG4PYY26bb085bt5SbQMyp5cD67wQnJc21IN_jF_8ty6no9IjDECPt-v2JPGc5Nexgm5fBLSslTU_uK6AOU8TvyQ6Bv-T-7LP9znT80ypJm5SSzsL4sBMSSV2AYpFon-d_CoCzrCXOfyhSawg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاهی به فیلم «رشته ها»!   امروز، ۶ اوت، سالروز بمباران اتمی هیروشیماست؛ روزی که در سال ۱۹۴۵ برای نخستین‌بار در تاریخ، یک سلاح هسته‌ای علیه یک شهر به کار گرفته شد و جهان وارد عصر جدیدی شد که در آن یک بحران نظامی می‌تواند، در صورت خروج از کنترل، به تهدیدی برای…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/19951" target="_blank">📅 01:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19950">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC9X9E9wYHCBhuRLsjbDE0SkSVlfc2yMu98dLO-IJs6PhOD7b-b6xcf5DsVVxygvWlLl5vSQsdYOgg6lt6Gxxyoy59fA5nLkc7BCNCEtdnmxD67AAzwsESSFPwnbIyLTSQZSJGMZ39ojtIuLf1KTdp8X2yiPgxN6G-NfmFhEdr63PXjJpym7eTaFq5W0scFikQQKZLWjSfnjdAblqNNPnLqI7mNHW__SHxJk200HoWpxs4V-IpS2d-KaLmJrupr75C5Hn5Q3UvEzP-oWYWTgc1hHz7KVgcBH6ppPDqyG7lUWxNGoitRAxdPvj0u1ivxjv4KqyNPK97nZBa0HM6xFzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ادامه برخوردهای نظامی میان ایران و اسرائیل بسیار محتمل است؟</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/19950" target="_blank">📅 00:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19949">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/19949" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">چرا ادامه برخوردهای نظامی میان ایران و اسرائیل بسیار محتمل است؟</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/19949" target="_blank">📅 20:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19948">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/19948" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آیا به پایان رسیدن مهلت 60-روزه در فردا، لزوماً جنگ از سر گرفته می شود؟!</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/19948" target="_blank">📅 18:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19947">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بر اساس گزارش واشنگتن پست، کشورهای حاشیه خلیج فارس در حال بررسی امکان انتقال پایگاه‌های نظامی آمریکا از این مناطق هستند، زیرا اعتماد خود را به طور کامل نسبت به استراتژی جنگی دونالد ترامپ علیه ایران از دست داده‌اند.</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/19947" target="_blank">📅 15:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19946">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بر اساس گزارش واشنگتن پست، کشورهای حاشیه خلیج فارس در حال بررسی امکان انتقال پایگاه‌های نظامی آمریکا از این مناطق هستند، زیرا اعتماد خود را به طور کامل نسبت به استراتژی جنگی دونالد ترامپ علیه ایران از دست داده‌اند.</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SBoxxx/19946" target="_blank">📅 15:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19945">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">از فردا با حجم کاری کمتر فعالیت کانال از سر گرفته می شود.
سعی میکنم شاخص GRI دستکم بروزرسانی و ارائه بشود.</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/19945" target="_blank">📅 02:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19944">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مدتی نخواهم بود...</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/SBoxxx/19944" target="_blank">📅 16:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19943">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQQAm0zEygxWuO7-_vVWL-VkfqxRuFpr3uOI7dJglVQ7V-Be39vwAlK5Q3JVR66cNJe6dS9GZx9BxwRbVjUCOwHMir11RVpt-ALCBEjtJfJCOZ-Xr03ldaDH7xUv-P2F49171hGAb-OH_T704a-3qvQrJaqsJRWkMkpY_sVI8EaLU9coFvLzJbuDprJVBUDDGdeUQvhO4IJJq7VKZm-jSqR378oQwDKKJPcyNnkUW24OQroNUJ5mBW3acdM4X593h_CURV6WBbTxDvNzq1nX2ns6gbgrwJF6TI3PVOIAmKRyA0utm2JpDlSsvdDgdN3efC8aEetISze-8SPb-QNydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه به دنبال تایید ایالات متحده برای ارسال ذخیره‌ای بزرگ از سلاح‌های ساخت آمریکا به اوکراین است!
این بسته شامل موشک های اتکمز و ۴۷,۰۰۰ گلوله توپ خوشه ای است که به گفته منابع، ارزشی حدود ۲۵۶ میلیون دلار دارند.
واشنگتن آماده تایید این انتقال است، اما سازمان دیده‌بان حقوق بشر از کنگره می‌خواهد که جلوی آن را بگیرد و به خطراتی که سلاح‌های حاوی بمب‌های خوشه‌ای برای غیرنظامیان ایجاد می‌کنند، اشاره کرده است.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/SBoxxx/19943" target="_blank">📅 14:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19942">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">چقدر خوشحالم جای پاکستانی ها نیستم؛
فردای امضای پیمان دفاعی با عربستان، یمنی ها یک کشتی سعودی را زدند که در اثر آن چند پاکستانی کشته شدند!
الان هم سه روز است میگویند ایران و آمریکا دارند سازش می‌کنند اما ولی خب</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/SBoxxx/19942" target="_blank">📅 14:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19941">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سخنگوی وزارت امور خارجه پاکستان:   فرایند صلح گسترده‌تر بین آمریکا و ایران با مشکلاتی روبرو شده است و ما امیدواریم که دو طرف به گفت‌وگو بازگردند.   ما می‌توانیم توافق‌نامه همکاری را قبل از پایان مدت اعتبار آن تمدید کنیم.</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/SBoxxx/19941" target="_blank">📅 14:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19940">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آذربایجان در پی دریافت کمک‌های ایالات متحده در زمینه فناوری‌های پیشرفته برای پاکسازی مین‌های زمینی است.
دهه‌ها درگیری این کشور را به شدت با مین‌ها و مهمات منفجر نشده آلوده کرده است.
باکو امیدوار است که روابط نزدیک‌تر با ایالات متحده بتواند تلاش‌های نقشه‌برداری و خنثی‌سازی مین‌ها را تسریع کرده و بازسازی پس از جنگ را پشتیبانی کند.
منبع: آکسیوس</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/SBoxxx/19940" target="_blank">📅 14:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19939">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سخنگوی وزارت امور خارجه پاکستان:
فرایند صلح گسترده‌تر بین آمریکا و ایران با مشکلاتی روبرو شده است و ما امیدواریم که دو طرف به گفت‌وگو بازگردند.
ما می‌توانیم توافق‌نامه همکاری را قبل از پایان مدت اعتبار آن تمدید کنیم.</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/SBoxxx/19939" target="_blank">📅 13:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19938">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اردوغان:  «توافق مکه» علیه هیچ کشوری نیست و تمام دولت‌ها می‌توانند به آن بپیوندند  نباید این توافق را به بعد نظامی محدود کرد، زیرا هدف اصلی آن تقویت بعد بازدارندگی و امنیتی است</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/SBoxxx/19938" target="_blank">📅 10:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19937">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حالا باید ببینیم ائتلاف «مکه» پاسخ می‌دهد یا صرفا برای دوشیدن گاو شیرده حجاز و نجد تشکیل شده.</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/SBoxxx/19937" target="_blank">📅 10:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19936">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حجم تحقیری که ترامپ به عنوان رییس جمهور آمریکا دارد می شود کم نظیر است!  پس از افشای داستان فرار ترامپ از ترکیه با یک هواپیمای فرعی — آن هم داخل کامیون کترینگ هواپیما ! — دیروز خبری منتشر شده که ترامپ حتی داخل زمین گلف خودش احساس امنیت ندارد و همانطور که در…</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/SBoxxx/19936" target="_blank">📅 08:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19935">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">— کریس رایت، وزیر انرژی ایالات متحده:  به لطف تلاش‌های هماهنگ ارتش ایالات متحده و متحدان ما در خلیج، میانگین هفت‌روزه نفت خروجی از تنگه هرمز در حال حاضر به نزدیک ۹ میلیون بشکه در روز رسیده است.  وقتی این مقدار با ۵ تا ۷ میلیون بشکه اضافی در روز که از طریق…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19935" target="_blank">📅 07:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19934">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxtcMiJE6jBRKThdjCdoL1VElR4kD0S-jLhRAWYlWCxopMY8E06lystrZ0RfOV2BVr3WD_cmjmwxJ-LH6P4n4klUdtorf7I-kh1g6U1EDo6YYauM3s-L9OR2XdgsWrxZ52cJyI4ZLrqqy_YH5sp6JwCF6IggoJdvpUVWn0WvaWOO4ovAeKyH3ka7Ua_b-vhR-RCOaIPftU9nE4Dt2Et7oNFqvqN-ZjGoVvQEi3aSUu3NmICcOr_opDUFERikqiSwevwR8fFcjlnxi1bcadiWQek4dNchWLY_wogEQPwOYWJpHKRSNNx6g_n-_EONdryCXkRi_FeIIY-_AaMaeWQ_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— کریس رایت، وزیر انرژی ایالات متحده:
به لطف تلاش‌های هماهنگ ارتش ایالات متحده و متحدان ما در خلیج، میانگین هفت‌روزه نفت خروجی از تنگه هرمز در حال حاضر به نزدیک ۹ میلیون بشکه در روز رسیده است.
وقتی این مقدار با ۵ تا ۷ میلیون بشکه اضافی در روز که از طریق خطوط لوله و تأسیسات صادراتی تازه ارتقا یافته از منطقه خارج می‌شود، ترکیب شود، مجموع جریان‌های نفتی در حال حاضر به طور میانگین حدود ۱۵ میلیون بشکه در روز است.
فقط در روز یکشنبه، بیش از ۲۰ میلیون بشکه از منطقه خلیج عربی خارج شد که این رقم بالاتر از میانگین پیش از درگیری است.</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SBoxxx/19934" target="_blank">📅 07:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19933">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کوشش ژاپن در تقویت توان دفاعی  ژاپن با تأکید وزیر دفاع خود، شینجیرو کویزومی، بر لزوم تقویت و تحول توان نظامی این کشور با «حسی بی‌سابقه از فوریت و بحران» اصرار می‌ورزد. گزارش سالانه سفید دفاعی ژاپن، منتشرشده در ۴ اوت ۲۰۲۶، بار دیگر بر تهدیدات فزاینده چین، کره…</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SBoxxx/19933" target="_blank">📅 06:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19932">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">صدای انفجار در شمال غرب تهران</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SBoxxx/19932" target="_blank">📅 02:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19931">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">صدای انفجار در شمال غرب تهران</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/19931" target="_blank">📅 02:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19930">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">▶️
An oil spill has reportedly polluted a coastline on Iran's Qeshm Island.  @PressTV</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/19930" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19929">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPress TV</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de69aae9a6.mp4?token=ApekSCr_KkJ32zS-myFXSgvO1ub9eSERMbdp2qXpZElOE0Y0i0W-slxTd30AZKc98Bslq3tb-FphHWJlAodaJF5b5pZ4l8kpq2KiGT8cq10HaOoMwIsimdnDqH3xTsUtgfLq0FbTia4NDudHNvQI_9smZxQ23WkKkHorAS2ryALdtzm0NdBPVsmaQN2EF-_Ptx3xZepu5BcPZJTZvXcFgcmL-1o78tk-yHF1gOW1UFVOX9bRWJThKy0LN9AKlJVB-uo-0TuT9DEYOtoEi7yhXXwPZN0pZOCkAx55tGB6v4yR41HOucZ_WiqZ7dfzYMAR_YQ8_2FRN0cM5T3dTLh6Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de69aae9a6.mp4?token=ApekSCr_KkJ32zS-myFXSgvO1ub9eSERMbdp2qXpZElOE0Y0i0W-slxTd30AZKc98Bslq3tb-FphHWJlAodaJF5b5pZ4l8kpq2KiGT8cq10HaOoMwIsimdnDqH3xTsUtgfLq0FbTia4NDudHNvQI_9smZxQ23WkKkHorAS2ryALdtzm0NdBPVsmaQN2EF-_Ptx3xZepu5BcPZJTZvXcFgcmL-1o78tk-yHF1gOW1UFVOX9bRWJThKy0LN9AKlJVB-uo-0TuT9DEYOtoEi7yhXXwPZN0pZOCkAx55tGB6v4yR41HOucZ_WiqZ7dfzYMAR_YQ8_2FRN0cM5T3dTLh6Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
An oil spill has reportedly polluted a coastline on Iran's Qeshm Island.
@PressTV</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/19929" target="_blank">📅 02:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19928">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fP31hPbm4gSncsBAHnQE6WaNMfpFHRtFvgzqRoaQISKG6Hgp6FXmXxGjSUFA-md-QrtTd3vglcSmG-EbLVW4pOzNDw5O5P7IQa6Wrjp2toLkedwY9E-WeoBBheM8M5-QpZHBWitK33DKkXGaGF7vqq8tsKARZ7jt7rGzKTF0fbQib3UKhxU5rJBXkdLxvcojh7qqPCZRIyTTVq-5HCOWr5UToIe6q-CIA7vFLTkixRfziJDS7Xy85o9oZfwq3f3y2YjvQQkljr9Y1sed8dSxJz1zjoWI4_cYTTRY_wYDENEXC31LpKBLQ553-ZdWlIB3OsNIzysZpNQgNrjKyew5aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19928" target="_blank">📅 02:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19927">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ:  ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.  این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/19927" target="_blank">📅 23:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19926">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">این ترکیب و چینش سیاسی و نظامی خبر از جنگی شدید می دهد.  تًن ماهی یادتان نرود.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/19926" target="_blank">📅 23:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19925">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اساساً به حمایت خاصی نرسید که برای خرید اقدام بشود.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/19925" target="_blank">📅 22:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19924">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yud-iKfg-4bYTnl5ay4fsHlNQiG6gqyxujRXl-j2fVgXebBUQnr9SIVpZgXmvhyU-Ee7vODLchpxaNjQuuAsiWAZn9w1hEqnD4EIlqZELuSIxqVCmak7h9f5LkYgfUy77O-5EEuheXHDfMzQzLlZBClrV8jYGgq6m7OkSjb1V8cL2d9hTF3Qi3p5SbQKe-tcv-PdhesQpgXceXf00LOfxxwyE0KSKc5i3hEU6iGG9toCb3aos5cEv758RN3aqsrk30WfaSeavBgzQITf2TMMP09-YTix_Hhxy5kDkjqFg_oZsBpGqi3Fi__ycA83J8xc5Bad6QqTS8N-LD4ErQ2t2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه ای قرار دارد. در چنین شرایطی سیگنال قوی خرید یا فروش صادر نمی شود و بهترین راهبرد از دید من خرید در سطوح حمایتی پایین تر است.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/19924" target="_blank">📅 22:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19923">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بازآرایی ساختار نظامی و امنیتی ایران؛ حرکت به سوی فرماندهی متمرکزتر و مقاوم‌تر   ایران پس از تجربه جنگ‌های ژوئن ۲۰۲۵ و بهار ۲۰۲۶ در حال بازطراحی بخش‌هایی از ساختار نظامی و امنیتی خود است؛ بازآرایی‌ای که به نظر می‌رسد مستقیماً از آسیب‌پذیری‌های آشکارشده در…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/19923" target="_blank">📅 20:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19922">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گریدم به اسلام آباد و توافق ش. نفت را دریابید.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19922" target="_blank">📅 20:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19921">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران:  پیام ایران روشن است: تنگه هرمز تا زمانی که آمریکا جنگ و محاصره را پایان ندهد، دارایی‌های مسدود شده ایران را آزاد نکند و به آتش‌بس در کل منطقه، از جمله لبنان و غزه، موافقت نکند، باز نخواهد شد.  تا زمانی که تمام…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19921" target="_blank">📅 20:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19920">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">محسن رضایی:   تمام توانم را برای افزایش قدرت ایران به کار خواهم گرفت</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/19920" target="_blank">📅 20:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19919">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این خواهرمیانه درست بشو نیست؛ ببینید کی گفتم.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19919" target="_blank">📅 20:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19918">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3df015c88.mp4?token=FBUKDB7f28GI3o0JDhwTQRB1xnE-rBhJ3s64V-CNh1RCNaVwOYZ7W3Fylp4tmmOcV-vsW4Ay3ZuBe_gC7Gve_BMQ_8G-KuoO_9icxP2RNmnqZjTkFWZnckkaRX1MG-XUXrzWZ4ooSQ1xFKmgvDZ2TrwhM3nYYgkmINFvNWfUKcugANElCSYTvF3NTYv3hhUYoT4cm0tcWmxUnlZDi0ZqyZPFcvs7TYOY4O1L3l0DhZMs3HWnr9CUEsGptmf1Uk-DK4DzjsteRMc-phQ1HBZEAwbhyVc7TM9ajH0GbMnBw0zUyH3nMQsfCNlaetpKxV0K_8wh2V8Xpq6LlCTuqVyMvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3df015c88.mp4?token=FBUKDB7f28GI3o0JDhwTQRB1xnE-rBhJ3s64V-CNh1RCNaVwOYZ7W3Fylp4tmmOcV-vsW4Ay3ZuBe_gC7Gve_BMQ_8G-KuoO_9icxP2RNmnqZjTkFWZnckkaRX1MG-XUXrzWZ4ooSQ1xFKmgvDZ2TrwhM3nYYgkmINFvNWfUKcugANElCSYTvF3NTYv3hhUYoT4cm0tcWmxUnlZDi0ZqyZPFcvs7TYOY4O1L3l0DhZMs3HWnr9CUEsGptmf1Uk-DK4DzjsteRMc-phQ1HBZEAwbhyVc7TM9ajH0GbMnBw0zUyH3nMQsfCNlaetpKxV0K_8wh2V8Xpq6LlCTuqVyMvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز زمینی بچه های تیم New Castle !  همه هم پنج سانت و ده سانت و …</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19918" target="_blank">📅 20:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19917">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حجم تحقیری که ترامپ به عنوان رییس جمهور آمریکا دارد می شود کم نظیر است!  پس از افشای داستان فرار ترامپ از ترکیه با یک هواپیمای فرعی — آن هم داخل کامیون کترینگ هواپیما ! — دیروز خبری منتشر شده که ترامپ حتی داخل زمین گلف خودش احساس امنیت ندارد و همانطور که در…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19917" target="_blank">📅 20:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19916">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ:   ایرانی‌ها با ما بازی می‌کنند، در اتاق‌های جلسات موافقت می‌کنند و در رسانه‌ها رد می‌کنند.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19916" target="_blank">📅 18:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19915">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ: ایالات متحده می‌تواند به زودی با قدرت بسیار زیاد به ایران حمله کند.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19915" target="_blank">📅 18:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19914">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuei5a8UWmtFgJuhEwIgn5G7olc4TB1hQT17pCgyzioZJ9BKQBGil0kXBvi0fpTizHZSWDj9QxOAM0FZLspCmQYACFk2bcrkwjOzwBeoTDsY2hOfcai7SxuMpQeXQtd-nDER0gtFPsy3s73d2kxP3OWgyI6zniBIPT3h9IS_hUvXz3MpnmXpzIDnTJotb29mRLMgJ3H4VxahkaUBmPYg4NyHlkWR_ApA6dTt4XuiqeCeKp2iJ747kW9NirMZlqZUuqN-i7nJ36_Pwh6XqKTfzOnTWJVZNuLYbyFEMgPv3X6SOkCnpra61OJnUbN9UtkVBfcRXm280MRRDkKjYVk5dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط کم‌سابقه قتل در آمریکا
داده‌های جدید مربوط به نیمه نخست سال ۲۰۲۶ تصویری کم‌سابقه از وضعیت امنیت شهری آمریکا ارائه می‌کنند. بر اساس داده‌های Major Cities Chiefs Association که در نمودار نیز منعکس شده، در شماری از شهرهای بزرگ آمریکا میزان قتل به‌شدت کاهش یافته است.
این کاهش‌ها صرفاً محدود به چند شهر نیست. تحلیل داده‌های MCCA نشان می‌دهد که قتل در مجموعه شهرهای بزرگ آمریکا در نیمه نخست ۲۰۲۶ نسبت به مدت مشابه سال قبل حدود ۱۷.۲ درصد کاهش یافته است؛ بنابراین با یک روند گسترده‌تر در سراسر کشور مواجه هستیم، نه صرفاً یک اتفاق محلی.
یکی از عواملی که می‌توان در این تحول مورد توجه قرار داد، تغییر شدید سیاست مهاجرتی دولت آمریکا تحت رهبری دونالد ترامپ است. دولت ترامپ از آغاز دوره دوم ریاست‌جمهوری خود سیاستی بسیار سختگیرانه‌تر در قبال ورود غیرقانونی، بازداشت و اخراج مهاجران غیرقانونی اتخاذ کرده است. بر اساس آمار ارائه‌شده از سوی کاخ سفید، دولت در کنار کاهش شدید عبورهای غیرقانونی از مرز جنوبی، تعداد اخراج‌ها و بازداشت‌های مهاجرتی را نیز افزایش داده است.
از منظر سیاسی، دولت ترامپ این سیاست را مستقیماً بخشی از برنامه بازگرداندن امنیت عمومی معرفی می‌کند. افزایش فعالیت ICE، تمرکز بر افراد دارای سابقه کیفری، مقابله با شبکه‌های تبهکاری و کارتل‌ها و کاهش شدید ورود غیرقانونی، همگی می‌توانند از دیدگاه دولت نوعی افزایش بازدارندگی ایجاد کنند. داده‌های موجود نیز نشان می‌دهد اجرای سیاست‌های مهاجرتی در دوره ترامپ به‌طور محسوسی تشدید شده است؛ برای مثال، یک تحلیل مبتنی بر داده‌های ICE نشان می‌دهد تعداد بازداشت‌های ICE در مقطعی از سال ۲۰۲۶ نسبت به نیمه دوم دوره بایدن چند برابر شده است.
با این حال، نباید از نمودار فوق یک رابطه علّی قطعی میان سیاست مهاجرتی ترامپ و کاهش قتل استخراج کرد. روند کاهش جرم پیش از آغاز دولت دوم ترامپ نیز شروع شده بود و خود آکسیوس نیز تأکید می‌کند که کاهش جرم در دوره پایانی دولت بایدن آغاز شده و سپس در دوره ترامپ ادامه یافته است. علاوه بر این، عوامل متعددی مانند افزایش یا بهبود عملکرد پلیس، تغییر الگوهای باندهای جنایتکار، وضعیت اقتصادی، کاهش خشونت پساکرونا و سیاست‌های محلی می‌توانند در این روند نقش داشته باشند.
با این وجود، از منظر سیاسی می‌توان استدلال کرد که سیاست «مرزهای بسته‌تر، اخراج سریع‌تر و برخورد سخت‌تر با مجرمان» یکی از مؤلفه‌های محیط امنیتی جدید آمریکا است. کاهش ۶۰ درصدی یا بیشتر قتل در چندین حوزه قضایی، همراه با افت ۱۷.۲ درصدی در شهرهای بزرگ، نشان می‌دهد که آمریکا در حال تجربه یک چرخش مهم در شاخص‌های خشونت شهری است. بنابراین، حتی اگر هنوز برای نسبت‌دادن این تحول به یک سیاست مشخص زود باشد، دولت ترامپ اکنون می‌تواند این آمار را به‌عنوان شواهدی از موفقیت رویکرد امنیت از طریق اعمال قانون و کنترل مهاجرت در برابر منتقدان خود مطرح کند.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/19914" target="_blank">📅 18:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19913">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ:
ایالات متحده می‌تواند به زودی با قدرت بسیار زیاد به ایران حمله کند.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19913" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19912">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خواجه آصف وزیر دفاع پاکستان، گفته است که ایالات متحده و ایران به توافقی در مورد تنگه هرمز نزدیک می‌شوند، با وجود اینکه هر دو طرف اخیراً مواضع سخت‌تری را در مذاکرات اتخاذ کرده‌اند.  او گفت: "به نظر می‌رسد که اوضاع به نفع صلح پیش می‌رود."</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19912" target="_blank">📅 16:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19911">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">محسن رضایی:
تمام توانم را برای افزایش قدرت ایران به کار خواهم گرفت</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19911" target="_blank">📅 16:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19910">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خواجه آصف وزیر دفاع پاکستان، گفته است که ایالات متحده و ایران به توافقی در مورد تنگه هرمز نزدیک می‌شوند، با وجود اینکه هر دو طرف اخیراً مواضع سخت‌تری را در مذاکرات اتخاذ کرده‌اند.  او گفت: "به نظر می‌رسد که اوضاع به نفع صلح پیش می‌رود."</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19910" target="_blank">📅 16:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19909">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خواجه آصف وزیر دفاع پاکستان، گفته است که ایالات متحده و ایران به توافقی در مورد تنگه هرمز نزدیک می‌شوند، با وجود اینکه هر دو طرف اخیراً مواضع سخت‌تری را در مذاکرات اتخاذ کرده‌اند.
او گفت: "به نظر می‌رسد که اوضاع به نفع صلح پیش می‌رود."</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19909" target="_blank">📅 16:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19908">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یک نفت کش که قصد داشته محاصره دریایی آمریکایی را بشکند هدف آتش نیروهای آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19908" target="_blank">📅 16:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19907">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بازآرایی ساختار نظامی و امنیتی ایران؛ حرکت به سوی فرماندهی متمرکزتر و مقاوم‌تر
ایران پس از تجربه جنگ‌های ژوئن ۲۰۲۵ و بهار ۲۰۲۶ در حال بازطراحی بخش‌هایی از ساختار نظامی و امنیتی خود است؛ بازآرایی‌ای که به نظر می‌رسد مستقیماً از آسیب‌پذیری‌های آشکارشده در جریان حملات آمریکا و اسرائیل، به‌ویژه عملیات هدف‌گیری فرماندهان ارشد، ناشی شده باشد. مهم‌ترین تحول در این روند، تلاش برای ادغام ستاد کل نیروهای مسلح و ستاد مرکزی خاتم‌الانبیا است. ستاد کل مسئول سیاست‌گذاری و راهبرد نظامی و خاتم‌الانبیا مسئول فرماندهی عملیات مشترک در زمان جنگ است. جدایی این دو نهاد از سال ۲۰۱۶ یکی از منابع بالقوه موازی‌کاری در ساختار فرماندهی محسوب می‌شد و اکنون ادغام آنها می‌تواند با هدف ایجاد یک زنجیره فرماندهی کوتاه‌تر و منسجم‌تر انجام شود.
منطق این ادغام، صرفاً اداری نیست. ساختار جدید می‌تواند هماهنگی میان ارتش و سپاه را افزایش داده، کاغذبازی و بوروکراسی نهادی را کاهش دهد و سرعت تصمیم‌گیری در شرایط جنگی را بالا ببرد. اهمیت این مسئله پس از حملات «سر بریدن» بیشتر شده است؛ حملاتی که با حذف فرماندهان ارشد، توانایی ایران برای هماهنگی عملیات تلافی‌جویانه را مختل کردند. بنابراین، ایرلت ظاهراً در حال حرکت از مدلی است که در آن بخشی از ظرفیت فرماندهی به افراد و نهادهای متعدد وابسته است، به سوی ساختاری که بتواند حتی پس از حذف بخشی از رأس فرماندهی نیز به فعالیت خود ادامه دهد.
انتصابات جدید نیز همین جهت‌گیری را تقویت می‌کنند. علی عبداللهی علی‌آبادی در رأس ستاد کل قرار گرفته و هم‌زمان نقش او در خاتم‌الانبیا، وی را در مرکز ساختار فرماندهی مشترک قرار می‌دهد. سوابق او در سپاه، فرماندهی انتظامی، وزارت کشور و ساختار ستاد کل، ترکیبی از تجربه نظامی و امنیت داخلی را فراهم می‌کند. در کنار او، کیومرث حیدری، با سابقه فرماندهی نیروی زمینی ارتش و فعالیت در خاتم‌الانبیا، به لایه بالای ستاد کل اضافه شده است.
در سپاه نیز تثبیت احمد وحیدی در مقام فرمانده و انتصاب مصطفی ایزدی به‌عنوان معاون فرمانده، نشان‌دهنده بازسازی سریع زنجیره فرماندهی پس از ترور محمد پاک‌پور است. انتخاب ایزدی، که اخیراً مسئول حوزه سایبری و تهدیدات نوظهور خاتم‌الانبیا بوده، می‌تواند بیانگر اهمیت فزاینده جنگ مدرن، حوزه سایبری و تهدیدات نوظهور در معماری دفاعی جدید ایران باشد. انتصاب حسین طائب به فرماندهی بسیج نیز نشان می‌دهد که بازآرایی نظامی با لایه امنیت داخلی و بسیج اجتماعی پیوند خورده است.
در سطح امنیت ملی نیز تغییر دبیر شورای عالی امنیت ملی و جابه‌جایی مشاوران ارشد، بخشی از همین روند تمرکز قدرت و هماهنگ‌سازی ساختار تصمیم‌گیری است. در مجموع، تصویر ارائه‌شده در انتصابات اخیر حاکی از آن است که ایران پس از تجربه آسیب‌پذیری فرماندهی در جنگ‌های اخیر، در حال ایجاد ساختاری متمرکزتر، یکپارچه‌تر و کمتر وابسته به یک فرد یا نهاد منفرد است؛ ساختاری که هدف آن افزایش سرعت واکنش، هماهنگی ارتش و سپاه و حفظ تداوم فرماندهی در صورت تکرار حملات علیه رأس هرم نظامی است.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/19907" target="_blank">📅 16:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19906">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REQcD8thyrFmTWrjqzOLP5zSqoK4bfyYoezTQwe6ceACSCTaN7urA1ltr265Ch_duormT7bFC-9kSv6xZ0lxTzQtEX1TdzDC0jzmgabM-btHquKBximYEwerRzvdS3N41XE3fInl-0vC10iB7O-Y01NPtiEI_k-tQsROZeg2EAZjkaCtDxeqByHOpxNuCPM7cUPYvYt9-y-Acl1SP2URftVaS-CqhzTkjQv3DoXx_bpZIk56myfAJJgZoX8-YackpZUaHi_w5D4uh3IMZoRe4Vqybcs4ME8uQoiBV4lefG6cMdfZPFVyKQ49Lpx5A60pDu8x-9D725kKbmlOdbZVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه درگیری های میان انصارالله و نیروهای دولت رسمی یمن</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19906" target="_blank">📅 15:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19905">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845af07e2f.mp4?token=biKGn32vJq-4klISEdNzCwUJnMeGeZ6Ei2V-2mfPtIsBbU3Y-g21n5aU3gZYAq9_tRMGuB6sDTpVThNzt6oO_bnlbDGyh_qw9nLZ8zVA2e5LARx0HAM0U0DTo4hZlzo3m0xcFIopSq4J0b0L_26B-dDkhN7P1Q2XNdXogo3hq2_hhef67bpG7vKttVD1FqyfM_eos12CEFjjCyLeqrC68STs_3AYyK59ghjBiCH89w2NISd8kwyHlTDhsCn3tTigEX08eqoRLFnEDz0RFDrUa-oJTNmu04VBNQZ9X2ZoM-YdsTF-rIgEj2z80botDInrzQuaWJoWPsx7lNKmn1nDeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845af07e2f.mp4?token=biKGn32vJq-4klISEdNzCwUJnMeGeZ6Ei2V-2mfPtIsBbU3Y-g21n5aU3gZYAq9_tRMGuB6sDTpVThNzt6oO_bnlbDGyh_qw9nLZ8zVA2e5LARx0HAM0U0DTo4hZlzo3m0xcFIopSq4J0b0L_26B-dDkhN7P1Q2XNdXogo3hq2_hhef67bpG7vKttVD1FqyfM_eos12CEFjjCyLeqrC68STs_3AYyK59ghjBiCH89w2NISd8kwyHlTDhsCn3tTigEX08eqoRLFnEDz0RFDrUa-oJTNmu04VBNQZ9X2ZoM-YdsTF-rIgEj2z80botDInrzQuaWJoWPsx7lNKmn1nDeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل بن گویر:  برای هر اشک یک مادر اسرائیلی، هزار مادر لبنانی باید بگریند. تمام لبنان باید بسوزد!</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19905" target="_blank">📅 14:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19904">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">302.8 KB</div>
</div>
<a href="https://t.me/SBoxxx/19904" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 23</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/19904" target="_blank">📅 14:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19903">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">صد رحمت به جنگ (تحلیل ژئواکونومیک محاصره دریایی)  مجیدرضا حریری، رئیس اتاق بازرگانی ایران و چین، طی گفتگو با خبرآنلاین با تاکید بر ضرورت فوری پایان یافتن محاصره دریایی بنادر جنوبی ایران توسط سنتکام، گفته است: این محاصره باید پایان یابد؛ با مذاکره، خواهش، تهدید…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19903" target="_blank">📅 14:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19902">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آیا صادرات نفت ایران از مسیر ریلی می‌تواند جایگزین صادرات دریایی شود؟   در هفته‌های اخیر گزارش‌هایی منتشر شده مبنی بر اینکه ایران در حال بررسی استفاده از مسیرهای ریلی برای انتقال نفت خود به چین، به‌ویژه از طریق خاک افغانستان و آسیای مرکزی، است. این ایده در…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19902" target="_blank">📅 14:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19901">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 23</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19901" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 23
سه شنبه 11 آگوست 2026</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19901" target="_blank">📅 13:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19900">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارشگر: گفتید این آخرین شانس ایران است. حالا چه؟  ترامپ: خواهید دید.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/19900" target="_blank">📅 11:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19899">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1_4_2arJkbndq-H0507J0O85z1Pvsb0vA1wMA88z3q3wKSTfohkHa2fqBXxiTgXoPPo2c_pFomDPPLL7V-Ttg78o4DbDhgBQqOCL1N4S1e0jdA6WnyhxDuGR8fpHX94LNaUqT37jybe85s8xKpmDmfmQZLxyd88bAlCRkmuwO4cBn10lhHKnC_H_6rHrb-lkm-depyNEOuVCIBIc1T4cISB1YAorzgJijwHmEC16TDhv8rMXFpdmkds2zMo9zQitueOiZVWiDO13qo1zdH0SG3eb2hv_ZvmImXDECurmBw8Ejq9_KuM5OOQgaEJfY1McxxA3_oOQvMNhVrZbnFNYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه ای قرار دارد. در چنین شرایطی سیگنال قوی خرید یا فروش صادر نمی شود و بهترین راهبرد از دید من خرید در سطوح حمایتی پایین تر است.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/19899" target="_blank">📅 11:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19898">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6_6L-UvNC4ZXCYnpGREVl_AqpwVgQbmCzipbj_pJDuM2WdjbXn41G6cMc2Xcl6vP6KMMOyKMIrUnunADMrKXnkdrqpQ-ruIuPwUi0qheu9jZIGhsp4WZMCslwBdOFs8Ppwfj3M4oWOeGNbhMVPKvZFKfFpOSLKF2sN5WPTYICed8N2DlUDxeUXmRiYDqJAkzRV0wIcnyTXZXwkDkO2ozYa2cw5_z52nWXJWpelChdZLvf6lXi2hkgtr_RSp8Sv6OdPN8Cf98gMw3uheSQHGzMa7cZugs0jl8AeGqmbYF6ri7ROSwqOH3seWT0UfG6GELJWg9fKWvZCasCfH9MzZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با برجسته کردن بیگانگی فرهنگی امثال این چپول عرب تبار با فرهنگ غربی غالب در آمریکا به دنبال کاهش امکان شکست جمهوریخواهان در انتخابات نوامبر است.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19898" target="_blank">📅 11:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19897">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انزوای روزافزون در جهان   کاهش اهمیت راهبردی خاورمیانه برای واشنگتن و برونسپاری مدیریت خاورمیانه به اعراب مسلمان  قدرت گیری روزافزون ترکیه و محور اخوانی  نیاز به حضور مستقیم در بازی کریدورها</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19897" target="_blank">📅 11:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19895">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oA3WfNLDNR2bM9CcKY_2n5A9OkQMwdFAuvNHYUyBEdzB9yWApSlhhMS-06VQNj9JN_19hhYgLFNzodt_LozjftSJKAgNfUCZFqmVYbQGQAFThdw8fYZEBR7x-_4wNkN3gh532qcivsXJ3nibrpjvchuEw6kfThUnozUIb4tERJ0NTP6zOu3wn0lZUY_zCyDBR8MS-_he5FOW_dh4RKzJ03cQT5KEmhW7R35VtvBaXwkA4_bWeJn5CC6Ms0ojzZM_m-OxlM5f3Lta-Hm3Qsbk682dbSoKXQGRLDToKLf_CPxj3CueuyCvMfuXdmwK1F_aAwGd5toYiDMNcU-7hqWoiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CHts3MqQ9C1l6ZUIXCJtFETyTDRZf5GQ3Fn1vrRA7NPqoWtjwNTsK7auj2cydljvG3BKN2G_V1LI5QbNA_I__vEdyDNBnj1B5rW5vEZrM210VSLrTnNtKu7nifheIGPSPmwXghOCUzR_F6AlWcUXMBXzyz3FcwTqFgeohO-M4lxpKW619JcnpOuHNmThURZSru0JWnyyi91if69ZM9Ry3Dp2NlkO6VKRkL4Rejevol-xQ550S4e53D9s7EyDKvwaID6JQ9t1T8Yqohqgh-M2UXy5CfXwFgCWLR4QjkieHDYSeJdD_sFeVuPSjBMHfo1FL6vRjH12tnzI1sFaaIJ0Tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گزارش واشنگتن پست، دونالد ترامپ، رئیس‌جمهور، ماه گذشته پس از نشست ناتو، به دلیل تهدید ترور از سوی ایران، به صورت مخفیانه با یک هواپیمای C-32A نیروی هوایی ایالات متحده از آنکارا، ترکیه، خارج شد، در حالی که کاخ سفید به صورت عمومی اعلام می‌کرد که او با هواپیمای…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19895" target="_blank">📅 11:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19894">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انصارالله یک کشتی تجاری عربستان را در باب المندب زد و ۳ نفر کشته شدند.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19894" target="_blank">📅 10:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19893">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فعلاً 2 کشور در خواهرمیانه با ائتلاف «مکه» مخالف هستند: ایران و اسرائیل</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19893" target="_blank">📅 03:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19892">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">طبق گزارش واشنگتن پست، دونالد ترامپ، رئیس‌جمهور، ماه گذشته پس از نشست ناتو، به دلیل تهدید ترور از سوی ایران، به صورت مخفیانه با یک هواپیمای C-32A نیروی هوایی ایالات متحده از آنکارا، ترکیه، خارج شد، در حالی که کاخ سفید به صورت عمومی اعلام می‌کرد که او با هواپیمای…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19892" target="_blank">📅 02:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19891">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zfy_kw6CwpyZyUC-7Pz5OTU8WKqiwNax4wWLijTujjcwuv35RGtwQwEoQ7Rg4hrD2A8w_nO4J0yyw4aHdk9yzAgfMJ75gtkNgzTrARSpf37BLwDTEl4WhthO83GE0UpWPH22Wt32Ihluo9L6YK8ypYmHVXMvAj0taBQ3Zd5vNCWgrJa5U56eJIAaTHk3yha_6WuI3lWzEJ2PQz7u7YIYKHrRwFGseHNec__J5w7uGkUMP46gy82EB9kJhlLUH3rMASRmG6yC3ay10xAPdlgM8HbUReUztWzWc7-Rtk7o7jnsJ45xUj2h6991GE--ltrUrBXUHgyxJF4OkGh5IeoYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفته می‌شود ایران در جریان سفر ترامپ، رئیس‌جمهور آمریکا به ترکیه، تلاش کرده است او را ترور کند.  اطلاعات ارائه شده توسط یک منبع خارجی که به مقامات آمریکایی در مورد این توطئه ادعایی هشدار داده بود، باعث شد تا در آخرین لحظه، هواپیمای مورد استفاده رئیس‌جمهور…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19891" target="_blank">📅 02:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19890">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAlS4LcZr8Icb1_7X7NBNkiZqFu6qDIoLKA_d8ro1wxta-UDHmAY_l_r-LFGnHqyfEMq_7qdlpCY5B_xwjhB_22yXcBhrj-WBbN58aeXz78HhKSi9If60x94EjZwjlt8xoFyMWS4e1R_Dc7gL0RY3AenOfEly9MmxKK8ozZktsKQErqB-7Z_c0UywP2mjFyzsHe_EMdCHI9C_iUEiC-jDm5IwNiDV_NXs0T_l-aL1IAgnx1sSGQG3rmTv9XXq4SVkOvLR2bHBsZHfqAZgQP5xEksT_Q3eX6TlTZmFxlZI_Uftfk8wYGxbhD8A_zyvOfmzTNZitZB_0znk1nD1u1FHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلاً 2 کشور در خواهرمیانه با ائتلاف «مکه» مخالف هستند: ایران و اسرائیل</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/19890" target="_blank">📅 02:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19889">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFXarbuBuTrWlXFq4WYGiJ3NmYFqnWR1vxc8Fpq17-3mGhpR01WIHg3Yx5KDktPogGVwMeGX0crBbDClVVGdqALBVfJo_97I11ug0sbtELXyW1KKJdt6Z-R30lHQFC3whmK7hSNu1kGgB-MVPx9XgRhoZRWSzV3woU4cNdnBsCP_u9360tTk80ZrDrWqVdUkJKmUMDp6VOlxQTeb1TJfg7C05JwBHfdF-oKOEBTVYq_VZ84xcqQcoHFZvHWpYuouyAgG4R6DbygdoUh4CHbToUvpJb7F4JX8X0czg7sx90RJSm-TWKyoYZcgndOatOlDdXoJoSB4vPmfJFfsAdUm5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زمان آغاز جنگ ، ایران بیش از ۲۰۰۰ حمله هوایی، موشکی و پهپادی در سراسر خاورمیانه انجام داده و حداقل ۲۰ سایت مورد استفاده ارتش ایالات متحده در هشت کشور را آسیب رسانده است.
این حملات تا ۱۳ میلیارد دلار خسارت به تجهیزات ایالات متحده و تأسیسات نظامی وارد کرده است.
بیش از ۴۲ هواپیمای نظامی ایالات متحده نیز آسیب دیده یا نابود شده‌اند، از جمله چندین فروند که در پایگاه‌های هوایی پارک شده بودند.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19889" target="_blank">📅 01:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19888">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e06c6847.mp4?token=rbML7LhDIjwWCuptrQirTgMnnSr6hIH1OWCDIELcApHs9-us-lZwXyu5qQr3HWRr9sGtWfZSDja8LPQW3QKIMi20j3uqJitauLpEZ2mSFy5y6fd8d5zuFgI7KGYNR37-Iq2oT98oyfy9ph0YLcOOBewCzDHjYp73GB7gsCfQJ7_q8KBpc7BUS59pWFdCbOFA-qy2inp75r2NTa7bYtxBj6n7GbRAR-tcLe00wr_yd4F6zlYbCifJpkRx0gqn9_qcgPp4yBXBoNByG9EAbtASgVbDCPEDxf2sSSnAAqHWH9yUHjd1y8r5hHvTUoqqoJ8LRTvA3WHVhx-R4lO8YcqVoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e06c6847.mp4?token=rbML7LhDIjwWCuptrQirTgMnnSr6hIH1OWCDIELcApHs9-us-lZwXyu5qQr3HWRr9sGtWfZSDja8LPQW3QKIMi20j3uqJitauLpEZ2mSFy5y6fd8d5zuFgI7KGYNR37-Iq2oT98oyfy9ph0YLcOOBewCzDHjYp73GB7gsCfQJ7_q8KBpc7BUS59pWFdCbOFA-qy2inp75r2NTa7bYtxBj6n7GbRAR-tcLe00wr_yd4F6zlYbCifJpkRx0gqn9_qcgPp4yBXBoNByG9EAbtASgVbDCPEDxf2sSSnAAqHWH9yUHjd1y8r5hHvTUoqqoJ8LRTvA3WHVhx-R4lO8YcqVoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز زمینی بچه های تیم New Castle !
همه هم پنج سانت و ده سانت و …</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19888" target="_blank">📅 01:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19887">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ درباره ایران:  آن‌ها می‌توانند دردسر درست کنند، اما ورشکسته هستند. پولی ندارند.  ایران کاملاً ورشکسته است. آن‌ها به سربازانشان حقوق نمی‌دهند.  تورم آن‌ها ۳۰۹ درصد است.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19887" target="_blank">📅 00:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19886">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارشگر: گفتید این آخرین شانس ایران است. حالا چه؟  ترامپ: خواهید دید.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19886" target="_blank">📅 23:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19885">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارشگر: گفتید این آخرین شانس ایران است. حالا چه؟
ترامپ: خواهید دید.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19885" target="_blank">📅 22:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19884">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ایران_تا_چه_اندازه_می‌تواند_تنگه_هرمز_را_به_یک_سلاح_ژئوپلیتیکی_تبدیل.pdf</div>
  <div class="tg-doc-extra">538.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19884" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکات بسنت در مورد تنگه هرمز:  تنگه هرمز دیگر هرگز به وضع سابق خود باز نخواهد گشت، زیرا ایرانی‌ها از آن به عنوان یک گلوگاه استفاده کرده‌اند، یا تلاش کرده‌اند از آن به همین منظور استفاده کنند.  آنچه در 2 سال آینده شاهد خواهیم بود، این است که تنگه هرمز از اهمیت…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19884" target="_blank">📅 22:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19883">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Po5wSHU_rRoSrYd9wZl7_YCA8trnh8pwwJJokLv7XQ_QVgHr60KRXLLI804PJQNSZ3PaZ4ht4vL4PJRC-qGvKv2cAKGxYKvbIpCr-bfvYigzwg-ttXpsQUsHHMbGF5AGzUdbpYYj92HXub7eUHA9vaSiN6d-sFWLCYh9va36ltx-qt6eVI4b6muCE4619nW2SRyR2nSQY_NO709sJWx4VH4pPLlGLXsyks_SDKuzDsVrMSaPMknLVhf5JxdUj3ezOMkPvTp5aM3mMfcx_kFyRIDvmHS__tddvxrKCRy3rzcslXUi_TL_UdkdcT_lk-0LSh6cyIlwl0hlYMdPPQkYVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح پایینی است و لذا اصلاح های محتمل نزولی طلا خرید دارد.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19883" target="_blank">📅 21:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19882">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">302.5 KB</div>
</div>
<a href="https://t.me/SBoxxx/19882" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 22</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19882" target="_blank">📅 21:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19881">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آمریکا پس از سوگند یاد کردن آبلاردو د لا اسپریلا، که با حمایت ترامپ به عنوان رئیس‌جمهور انتخاب شد، متعهد به ارائه یک میلیارد دلار کمک به کلمبیا شده است.  او وعده «جنگ تمام‌عیار» علیه تروریسم مواد مخدر، سرکوب نظامی سخت‌گیرانه‌تر علیه گروه‌های مسلح و روابط امنیتی…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19881" target="_blank">📅 20:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19880">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ:
🔹
من متوجه شدم که نمایندگان جمهوری اسلامی ایران درخواست غرامت برای خساراتی که در طول درگیری نظامی پنج ماه گذشته به آنها وارد شده است، دارند (درگیری که به این دلیل آغاز شد که "آنها نباید سلاح هسته‌ای داشته باشند"). با این حال، این موضوع در هیچ یک از…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19880" target="_blank">📅 20:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19879">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شرایط ایران برای باز کردن تنگه هرمز</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19879" target="_blank">📅 20:38 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

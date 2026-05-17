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
<img src="https://cdn4.telesco.pe/file/crjvH4-wtC2X585RNZps01PPoysuokcr0RHmiNBbTsMCM57zmFnsmzQ8Pe3r8pO6x9VlB7NAetwaXlzhPbvjaQJxl4DUlmdYCYYm6nuJlRIL7oM37vqo1e6I1ElH9JD0AChQqxeDl9w_BsFZM2Ry8ctt_m23S1N2TLoQEInmmsj0cw738mYvQh7v687_JT5TsN6VmZTDgJ3yr2s_jxLoH5ChyDZVDRj38Ac128hF8YP4EX-30F8mIYUEjaizNlSwM3e3cpnCW1XZPNzlVY9NH2jGRmHv8C5IaEBnZCzjrndDAhOmE0ac6LDjXDE6IokHnBvy9gVkgaTZHM_3_2s-MQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.2K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 15:06:57</div>
<hr>

<div class="tg-post" id="msg-5016">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !
‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا
‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا
‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای
‏۴️. عدم آزادسازی حتی ۲۵٪ از دارایی‌های بلوکه‌شده
‏۵️. توقف جنگ در همه جبهه‌ها [لبنان] فقط منوط به مذاکره است ‌‌دست یابی به توافق!</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farahmand_alipour/5016" target="_blank">📅 14:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b64429192.mp4?token=sLyQxVy0fVD9wQjSMltydo1nkuZVUDf_BnsbUkUyvW73O-bhZPcNv6ZBVj5tfMQTpe6LEjJlsXNAdHHeN_fg1grqDRxpY479lG1LS9qcnsNj9JF04_6Cg3h3solIu1clsfZwZFD3Tps3SOBZRAquJIRMZlfUjXiIbBTlQ5KfO7-jZbG5t9Pyjhob5gxOdgN4ZhBLkr2K8pxsZLqfAP778LqbAgDLxDSWo8RgLo5qp0GtQez4nydz_PI3o06VmZCB2x9ZmKOrZd4_VlCTGKtVz9_ctDyUTt5FuI4icFgU-u5qe9B2zeaUdxuphpem7lyhxmUBDIxhs5gTopwLfDFW3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b64429192.mp4?token=sLyQxVy0fVD9wQjSMltydo1nkuZVUDf_BnsbUkUyvW73O-bhZPcNv6ZBVj5tfMQTpe6LEjJlsXNAdHHeN_fg1grqDRxpY479lG1LS9qcnsNj9JF04_6Cg3h3solIu1clsfZwZFD3Tps3SOBZRAquJIRMZlfUjXiIbBTlQ5KfO7-jZbG5t9Pyjhob5gxOdgN4ZhBLkr2K8pxsZLqfAP778LqbAgDLxDSWo8RgLo5qp0GtQez4nydz_PI3o06VmZCB2x9ZmKOrZd4_VlCTGKtVz9_ctDyUTt5FuI4icFgU-u5qe9B2zeaUdxuphpem7lyhxmUBDIxhs5gTopwLfDFW3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشه عنبر خانم!
ولی روی این حرف‌هاتون بمونید
فردا که به خاطر ۴۰۰ کیلو اورانیوم
نیروگاه برق و پتروشیمی و پالایشگاه و… رو زد، نیایید بگیم ما مظلوم دو عالمیم و نیت اینها تجزیه خاک ایرانه و… !
اون وقت برو پوست پرتغال بخور و عنبر نسا دود کن .
تا می‌تونید از این ویدئوها پر کنید و یادآور بشید جنگی که بر ایران تحمیل کردید بر سر هوا و هوس‌های هسته‌ای تون بود و دشمنی‌تون با جهان!</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5015" target="_blank">📅 10:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=STlcrwnUfp2lx0pEShHz-OxHNBrpmj6KAhD3soB4eCdXIwvPreyLPZdoxR3vmAfjrKEB7EgL3aKydZ_BtPimpaBOhSNqZN3qAsiiNTQYXWhLrb80VlkIUPIRek6VTannAmL6jzFSaHSJudcG4eQ4UAEoyv58haXowoRpEQuRG8jrrh-SNUmRIZvZcYdLsSZsWkbHj8QnwBnI__lkxU0AcAqUMzxcQhvKNOcdG8fi9bwEJpi1Ya0g_vf_E2-FdLHlJb6XeTiieHANttLes6j23yJbQG0dwUC1kG7dP7Ap7oF_Dmekj8My1N9uL-ZH-Z5c_DVGWWszZz1VGxC1zI-odA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=STlcrwnUfp2lx0pEShHz-OxHNBrpmj6KAhD3soB4eCdXIwvPreyLPZdoxR3vmAfjrKEB7EgL3aKydZ_BtPimpaBOhSNqZN3qAsiiNTQYXWhLrb80VlkIUPIRek6VTannAmL6jzFSaHSJudcG4eQ4UAEoyv58haXowoRpEQuRG8jrrh-SNUmRIZvZcYdLsSZsWkbHj8QnwBnI__lkxU0AcAqUMzxcQhvKNOcdG8fi9bwEJpi1Ya0g_vf_E2-FdLHlJb6XeTiieHANttLes6j23yJbQG0dwUC1kG7dP7Ap7oF_Dmekj8My1N9uL-ZH-Z5c_DVGWWszZz1VGxC1zI-odA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهزاد فراهانی، بازیگر (پدر گلشیفته فراهانی)
میگه ما … داشتیم و انقلاب کردیم ، شماها هم داشته باشید و انقلاب کنید!
چه افتخاری که جمهوری اسلامی رو برپا کردید!
چطور روتون میشه اینطور وقاحتتون رو نمایش بدید، در دفاع از رژیمی که فقط در سال گذشته میلادی، مسئول ۸۲٪ مجموع اعدام‌های جهان بود!
که ظرف دو شب ۴۰ هزار ایرانی رو قتل عام کرد!
ضحاک روزی ۲ جوان رو قربانی می‌کرد.
در یکسال میشه ۷۱۴ جوان!
در چهل سال میشه ۲۸.۵۶۰ جوان.
کاری که حاکمان شما در دو شب کردن فراتر از افسانه ضخاکه! این نوع از حکومت افتخار داره؟ تباه‌تر از این در تاریخ وجود داشته؟</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5014" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=XHd0facDdDaYz76imKcDp9RMMs-SF1Uth7qw3jXc6zoWwW9_g1wtpc87MvEqCQZhdr6Q6Zhc0q1sAP__IvnOcRaWhu1V1_peq4a6kxrwHB51pfknqyFGZZ8YZBRRYbs-UakMSVPpJJ2vhgsj1XvMm-7ZVrZ2_Md4F19XIr8L8K7ngzBngX7a5DbeKr6oEc4gZbUVr0hU6yPSZLteHF4Bgslq7rMctFBo8qu89bzt8EDwzSbCxUWYieCzSx_7EdS2zO893SLImzJ_oavXBLRrMV6iGPwoge-rIRFKjV-GWhziykNzNAmV6HWYFfr2BdCx1ROAKNKvm0jR7KvQr2L09g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=XHd0facDdDaYz76imKcDp9RMMs-SF1Uth7qw3jXc6zoWwW9_g1wtpc87MvEqCQZhdr6Q6Zhc0q1sAP__IvnOcRaWhu1V1_peq4a6kxrwHB51pfknqyFGZZ8YZBRRYbs-UakMSVPpJJ2vhgsj1XvMm-7ZVrZ2_Md4F19XIr8L8K7ngzBngX7a5DbeKr6oEc4gZbUVr0hU6yPSZLteHF4Bgslq7rMctFBo8qu89bzt8EDwzSbCxUWYieCzSx_7EdS2zO893SLImzJ_oavXBLRrMV6iGPwoge-rIRFKjV-GWhziykNzNAmV6HWYFfr2BdCx1ROAKNKvm0jR7KvQr2L09g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=WNzUC9LvqNTh1v8GsTktaUNvapW2U0Th0BEfQEnTyNKUZTVdyKSyHMgo2GKHm4zv5NBCOffxcz6hn164ulMhE24nm07k1wV569sDtYCjfGydxXn9Jcy8PYlWJMlAqSue4KZ4iIlbWRrzzO3NBgaQ5J0LbVZrzEvaOuOzcbRDpDyd1SYuz5THjZrlHaVIduAhTwTOT74bSMh2GxSpfQeHsiAALumGZ41Iafc8dtVbIm1SKUPcPAdNWNvYOA6utmSm8AIuj7vYPLlsHENDTGnzCOSFmcrejTRYsOvIdKPn1n73AgfxMXm-8jlgTRkVrOAxgt0JYK2hgfQ8Wg05-FAW1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=WNzUC9LvqNTh1v8GsTktaUNvapW2U0Th0BEfQEnTyNKUZTVdyKSyHMgo2GKHm4zv5NBCOffxcz6hn164ulMhE24nm07k1wV569sDtYCjfGydxXn9Jcy8PYlWJMlAqSue4KZ4iIlbWRrzzO3NBgaQ5J0LbVZrzEvaOuOzcbRDpDyd1SYuz5THjZrlHaVIduAhTwTOT74bSMh2GxSpfQeHsiAALumGZ41Iafc8dtVbIm1SKUPcPAdNWNvYOA6utmSm8AIuj7vYPLlsHENDTGnzCOSFmcrejTRYsOvIdKPn1n73AgfxMXm-8jlgTRkVrOAxgt0JYK2hgfQ8Wg05-FAW1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316762f84e.mp4?token=jA1IEzA08HcsY2yuAnVJlQa8uPoTfrwgrftnp1TcbZ-dfuRf-7kfKnnWR5Epo51vswyjkkuVIeGNbM5_ZRL5-SN1dQJnT63jgiQdWeo59gC9RG3a59_A16rdis1JQ5yw6T6FRnIqXzNTIuWGDoV0ny9igBoWrn9WVb_X_cj-Vqd91KLDOC-OdmAjS4D0g5Ug2KTQuKzWbVcLoqyVZ_OXWlJt-xt68-7R3wbq3Y9QWtn3xLmcBK_7MIVu_j9ZZFGHhr6Vf4ocrp5hQmnnOW6383Mh8RwsFAyRZzdgfIdyYrcnoKgD2HjfC3nWwxu0eBtXn9he8K5JfOMk_v-72gDAHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316762f84e.mp4?token=jA1IEzA08HcsY2yuAnVJlQa8uPoTfrwgrftnp1TcbZ-dfuRf-7kfKnnWR5Epo51vswyjkkuVIeGNbM5_ZRL5-SN1dQJnT63jgiQdWeo59gC9RG3a59_A16rdis1JQ5yw6T6FRnIqXzNTIuWGDoV0ny9igBoWrn9WVb_X_cj-Vqd91KLDOC-OdmAjS4D0g5Ug2KTQuKzWbVcLoqyVZ_OXWlJt-xt68-7R3wbq3Y9QWtn3xLmcBK_7MIVu_j9ZZFGHhr6Vf4ocrp5hQmnnOW6383Mh8RwsFAyRZzdgfIdyYrcnoKgD2HjfC3nWwxu0eBtXn9he8K5JfOMk_v-72gDAHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی  تفنگ به دست در تلوزیون ظاهر شدن خوبه یادآوری کنیم از سلف اینها خانم «هاله مصراتی» که ۱۴ سال پیش تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LbZfCG7xkByBP5up67Ovq7AoGeYCiCWTCIByWxT1kPaTs2Quee0w-GKKkKxs6QErBE9Kx2kYgMSIHFZZFbgoeyQJGt9D_QUCSzvrnxMlPJMheXFzjSv3AHWGyj0NVp64PTSRuf5zGSmctTK1pXbkjZpU1LEHQ41vKtNvZft1Yvj8FqVNZJ9ab_B8aeqT4C_r9d_DTBhm9wnmqfMHgR9rW89qlYkG4hbIvblGieUAi8MEuBKGqdcOVmuoVupXz6-eFI83N5YEL1Fz7OOGIVs9Wn1eu6qs63PCzIzOELuTIdEIlcnRn0Zb-ByR_-vQv24oBBr2GuKdPKmgjFaxQzTm2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v2-L8uJg3DeOnFDMF_KHxZ8S9aT_GNH2ZFPizgYXeoUfuWjl4PAK0xWLtamzmOsofrD7pMbybLi5pbrkHe46EDvTySnVcijAxhhALHs8ByUz1FKdXid9o88d8Q1Swk7Z1ThK64Jy_vAN6ZSD-SkwVHq2Uq_C_NBp2mSXi3Mi1gO2tSRNouEWtdFO0NuCdInvQN2YeCdVFo-it-e5aHT6UI9KCDJ5H7EXSicvXi-eCpsUEjCB597Jbzv3PLS4tcCjXFnljpP3VwI4fHk9B9F69j7-MjFzlor-4a4g1d6ZvuvrWRXxAUpCl5qhMiQRzPHjiuDT5eAnz-PoGyqHxHk1Rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی
تفنگ به دست در تلوزیون ظاهر شدن
خوبه یادآوری کنیم از سلف اینها
خانم «هاله مصراتی» که ۱۴ سال پیش
تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5009" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دوستان بزرگوار، این صفحه به‌صورت مستقل اداره میشه و من تقریبا همه زمانم رو صرف انتشار و پیگیری اخبار میکنم.
اگر این محتوا برای شما ارزشمند است و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5008" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">در ابتدای این فایل صوتی که خبرگزاری فارس منتشر کرده، به نقل از
حداد عادل (پدر زن مجتبی خامنه‌ای)
نقل شده که فرزندان مجتبی خامنه‌ای در این ۷۷ روزه پدرشون رو ندیدن!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5007" target="_blank">📅 18:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iLOwUyn-fRlgKspfHwRk34Ae-u2FeArOZyd4y7sFEg4TVkN_B2DBHh_r9R3po-nKapjz_1IQ8PL-9VrFF1sAqXwBi8U1mpsfJPtPQXKLX7fI-n5kVTXXTecyyJmXDqUWyVO1DF3XuMQEJPScnrxzbD7lsvwm09C69CqT91TgqChqcDXxsQqx-7Hf3hPBipwK7dc9tXq22NSBS83aOdvcx5o0-88MenBy5Jt2OoxphMiFdZUDHV_oSeWru3nUD7P53yumg9xAIThDawEoHmbd1tA3BDlda29hXoEjMIXK0HCFhDxm_-IOVxt9KrbfYwpdOxxPh5ZkvETI5-8dT4rCGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hddSQqW5W2IzcEtBuo_WTsODJXL4tqJiFM2o-Vp-mVHSIGjC9VATOUK1i9sGCaVb-IFsAa_vzJicIeN0hvatKflg18_u89_b8r-OrE-CjwUqz0tlJP_bg-9qHA30mNZdTWPrDK6sP8DbIieSI0DhNIotd9kHmb6tKpb8M3qxVtyj53sykdrMXpC-sqtuNT_VpcTyKdpB8-HtEu2VvNKFF8aOqn7PDdZ8UjBhHYYi7p6SPTVxJfYwdLrvljC_DHUgyfNGNLrhcnv-r8wgYqm7XhCyYAsES4C99tdcTo95_SP12o6Jg0-khdPntCvzeOgfeN866QNEe_i-g_YCXP65ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5005" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=sLppUA6iSgjWa4-HVPYKMe4SPLDmkbuP7N4Q52ty75uNjhFv0DNh0-IUx7S2NZYgi5EyjIMywc7MUa9tM13Y8pKfa5MIuLadD3IkGt8PtengEvBSR5zD3I8kqftdBZBayhpReBlLsWTn20_2zciHMizkrMFS4m_HR1Gydm7UrSMHthv2UBstq43kTLPLi8NngGF6A2a-z6hHmiOt69jvBIhJ0YvR1e1m0cV6qdEHEoRo4JV1ERQg97CTcCTFrPPJMUTuimVCa6IgDehAHYqOSwRRB0i1O4qhLTy5qAnqvSOn467IEHEuleq0eY_g_kdZWB6to6HzcSPXoyMRA2Gu9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=sLppUA6iSgjWa4-HVPYKMe4SPLDmkbuP7N4Q52ty75uNjhFv0DNh0-IUx7S2NZYgi5EyjIMywc7MUa9tM13Y8pKfa5MIuLadD3IkGt8PtengEvBSR5zD3I8kqftdBZBayhpReBlLsWTn20_2zciHMizkrMFS4m_HR1Gydm7UrSMHthv2UBstq43kTLPLi8NngGF6A2a-z6hHmiOt69jvBIhJ0YvR1e1m0cV6qdEHEoRo4JV1ERQg97CTcCTFrPPJMUTuimVCa6IgDehAHYqOSwRRB0i1O4qhLTy5qAnqvSOn467IEHEuleq0eY_g_kdZWB6to6HzcSPXoyMRA2Gu9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟
چرا خانواده ، چرا فرماندهان؟
چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته
لذا شرایط عادی در بیت بوده»
صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5004" target="_blank">📅 18:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پیام‌رسان‌های حکومتی «بله» و «روبیکا» دچار اخلال شدند و بعضا از دسترس خارج شدند.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5003" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=aTzijaqj3SOf_d0w7LffZQPGYtHfe6ewVp1Pprx_zYYFjMeylNKMRxlwa3fiQaufyR8GUXM15o3V56DV74Nnxy7d9LkJvgpH1G7miFNT-sBER5mhTD8-4fdrznqMTs1ECZJyY19SlnxgZbfogyxTmZd0IehvI-OiNPJEIewhVvT3torO-YsbZHlJ_vP_oLC1CXW3XuaC9Mqb-y1J2IH0liX53Fkierz2sJ4DQKl_pUGrZjfhxFXITPSZ_WPvlWJsKpHaC0zyEKHwgySGAi51qzcx4RNhoY44EmOLUjd62GBC9DsZp2YOf2JWTUZAY9QILXyByVa-XBTXOEPTLUOJIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=aTzijaqj3SOf_d0w7LffZQPGYtHfe6ewVp1Pprx_zYYFjMeylNKMRxlwa3fiQaufyR8GUXM15o3V56DV74Nnxy7d9LkJvgpH1G7miFNT-sBER5mhTD8-4fdrznqMTs1ECZJyY19SlnxgZbfogyxTmZd0IehvI-OiNPJEIewhVvT3torO-YsbZHlJ_vP_oLC1CXW3XuaC9Mqb-y1J2IH0liX53Fkierz2sJ4DQKl_pUGrZjfhxFXITPSZ_WPvlWJsKpHaC0zyEKHwgySGAi51qzcx4RNhoY44EmOLUjd62GBC9DsZp2YOf2JWTUZAY9QILXyByVa-XBTXOEPTLUOJIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=pJSSziJQBOZnNQbwT4OXWI9PpjTcJIuGjjEymGpT-eyFCFLRXl8ADjaBq4h7REY19B25i05OtQ5sW18UIDzfvziilSjtnwjwvHwgFSeN5X4TUOmvc8gopTKWaUAosUSDYKlXlMo0WnRNMCludkgTrCQ-5Tosc9f5_TCK1hfcRBkaz7FHGKv-JpmlvA6JNs3ZXlu3ZxdOOzD07QAfqhtDH_VzZTifGdyNWk1isLFYkRwqCYts3XTKIK9373efb2C9WxrLAjT1ogczqzxilIE8J5e7nPXHo8jBrOYInrwbv5xsCYS-mlI1_ZD4uQ2JsO2nUUeOhF_EfuBjJ-Px7aoZsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=pJSSziJQBOZnNQbwT4OXWI9PpjTcJIuGjjEymGpT-eyFCFLRXl8ADjaBq4h7REY19B25i05OtQ5sW18UIDzfvziilSjtnwjwvHwgFSeN5X4TUOmvc8gopTKWaUAosUSDYKlXlMo0WnRNMCludkgTrCQ-5Tosc9f5_TCK1hfcRBkaz7FHGKv-JpmlvA6JNs3ZXlu3ZxdOOzD07QAfqhtDH_VzZTifGdyNWk1isLFYkRwqCYts3XTKIK9373efb2C9WxrLAjT1ogczqzxilIE8J5e7nPXHo8jBrOYInrwbv5xsCYS-mlI1_ZD4uQ2JsO2nUUeOhF_EfuBjJ-Px7aoZsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.
و نتونستن چیزی پیدا کنیم …..
این همون حادثه‌ای است که میگن
مجتبی فقط کمی زخمی شده
این همون حادثه‌ای که توی
صدا و سیما گفتن همسر خامنه‌ای (مادر مجتبی) هم کشته شده
، بعد از ۱۰ روز  گفتن نه! زنده است!
یعنی وقتی داستان زنده موندن مجتبی رو پررنگ کردن، داستان مادرش رو هم تغییر دادن!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5001" target="_blank">📅 15:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5000">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOk6yVnCyKJ-lKQ261QYzONTKnuJNHfdaDIW54dEYAfrrk5DGKYL1V2eLjEHp-WSuqNz8o2YMHSuTrzXo0Ro9R49Wphi6RR_n1XBHDJbvo27zyiwFoe3HyF7_HhS6apBlOEzj3Aar42eCLUDutuVCcrYs36rv6JOMfwqMXOodpu1E0yiOkWTzx7H5Kjd9imEykZgNjn6-q3oPdcUpDkzPOOXw1J7rYxYHWoxqy6I6JoVY4e3klYSd6jnHoO0HOay31BvvrxE3UuSKsdR6tWDpq76y0RWVQZ-LRGpRWE0RcSN35R-8KwVCrpyNqtQdTjVp8hNlS0A75K8qcv1p_2atw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5000" target="_blank">📅 15:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=Q_thJFQ9Twl2s8EUg1dVFRjY3XOWAvuAojf59yz0lBEoFJ73YH1Wt-_lbUDLwtnVSVmAzXcZEDIHk0jRy4cktAvOg5Bf_nF1j8_6AveXvA_cPoIBP1iD-9YzKY6cUQpX1pPsQpZ0e6wkw8A4I2gtvmRrtevBKsXXEX-CmjFg2wjLxPXQRDB4myQfuNfZfJhp3hDOEWtfJUFsORnhBqJwGXMFgkFjR05J5pq2h1kYAlBUbCmIT6NFNOrTHegf_uYu4EU7IbMOLaaayKK1Y2p5GODEb461ltRYf2-2CO_FJelgEHuL3-cTsc7POFjiemDEZcpyEoObPiSDCp1brFTXeBrM7F1fBIS0pszfBmTAJQUGNFklskdK1IAvWjVWYH-G1k7CNZQWyM40dU0d4tNcIglPILy0p0jI4HlZtwK2Jf5aOePeaOZGBpjJ-Sq6tJRUDmrwPNM8sbJOV9-s1s76rGAXD0xWl_oKjc8EdkVxcA6Da69N29hb9IhkhR8vwbtd6L8pgT_vOHejM8GK1sjrJTfsrgbxrGRqKq2n9rSSwTTjIIOcqwyETMMtjc1qKAKzwnZlr69iYYu6e1YROq1AFiKgbZA64tiR7j6d-VjT1mA59L8p2OK8fa9PzgbVBa03GwQ97a59mQculQ4G5XyAatlG_8UanN0ftiQjYY16AOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=Q_thJFQ9Twl2s8EUg1dVFRjY3XOWAvuAojf59yz0lBEoFJ73YH1Wt-_lbUDLwtnVSVmAzXcZEDIHk0jRy4cktAvOg5Bf_nF1j8_6AveXvA_cPoIBP1iD-9YzKY6cUQpX1pPsQpZ0e6wkw8A4I2gtvmRrtevBKsXXEX-CmjFg2wjLxPXQRDB4myQfuNfZfJhp3hDOEWtfJUFsORnhBqJwGXMFgkFjR05J5pq2h1kYAlBUbCmIT6NFNOrTHegf_uYu4EU7IbMOLaaayKK1Y2p5GODEb461ltRYf2-2CO_FJelgEHuL3-cTsc7POFjiemDEZcpyEoObPiSDCp1brFTXeBrM7F1fBIS0pszfBmTAJQUGNFklskdK1IAvWjVWYH-G1k7CNZQWyM40dU0d4tNcIglPILy0p0jI4HlZtwK2Jf5aOePeaOZGBpjJ-Sq6tJRUDmrwPNM8sbJOV9-s1s76rGAXD0xWl_oKjc8EdkVxcA6Da69N29hb9IhkhR8vwbtd6L8pgT_vOHejM8GK1sjrJTfsrgbxrGRqKq2n9rSSwTTjIIOcqwyETMMtjc1qKAKzwnZlr69iYYu6e1YROq1AFiKgbZA64tiR7j6d-VjT1mA59L8p2OK8fa9PzgbVBa03GwQ97a59mQculQ4G5XyAatlG_8UanN0ftiQjYY16AOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راس امورشون ۸۰ روزه تعطیله» :)</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/4999" target="_blank">📅 15:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUDtIp2G8tMZEb0kI_gi4UrPzSROJFYO32J-ZCZVxBjRYIlA7VOzv_UfI1upf6g6dxIXKW3ixPd-3oYlVw74TTSXApPoDPSrN8edPUoF9W7DiSYHHsKgeD__ZXSEfByHNRkJYngytQ4ZS22C0_wH0ODmew4sHdzLIgwfnIib2A9LEmZ0b2-TMtMC-V3Dl4QvbTBsLIeuZalWBZ780BGiZWAHVPFMw-rk1t8z61dVmi1XVIM5cCGTpcDUHwK1BZ4QNobMEhXojgj-RjHklnmbao6-sg90iTb9R0NWLj3hPj0LkrBoG3EGwBnUgKmMNXie5J7YYMNXZqEgDNFvFB3hLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/4998" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af299654a.mp4?token=CSqUaePytlHb2Cyp_x_556s2YEHWo8AssITGXYn7-Y4tzcWbtimHiHuk1rrWsWoiRW9-6NYaycFT70UjEJBCeRPoNdcZzHhY2iCFdlnibRcVHE4sjJ7fbz2g7zvJN0yva2Nr_s98O8uTe8DP92MWtGIHwQ76sBjTfEWUxJ3axqUVJ-e2ZZMRwIk22VlYvn4-3ct-wnIlecU5xLbwqHV2K17aqAIb6Zy67NPCGxv5dLZZEXg8a5rQ1nkBBE0N7e612OGuMCYhkk3GycRtiXztZGRSQgXZAJRkoYzF6uTRgJyBkNH3b6SlVVjgN5u3Hai_Hbure1bgZf1OaeSLpbZa0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af299654a.mp4?token=CSqUaePytlHb2Cyp_x_556s2YEHWo8AssITGXYn7-Y4tzcWbtimHiHuk1rrWsWoiRW9-6NYaycFT70UjEJBCeRPoNdcZzHhY2iCFdlnibRcVHE4sjJ7fbz2g7zvJN0yva2Nr_s98O8uTe8DP92MWtGIHwQ76sBjTfEWUxJ3axqUVJ-e2ZZMRwIk22VlYvn4-3ct-wnIlecU5xLbwqHV2K17aqAIb6Zy67NPCGxv5dLZZEXg8a5rQ1nkBBE0N7e612OGuMCYhkk3GycRtiXztZGRSQgXZAJRkoYzF6uTRgJyBkNH3b6SlVVjgN5u3Hai_Hbure1bgZf1OaeSLpbZa0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری تلویزیون جمهوری اسلامی:
- بگذار پرچم امارات رو نشانه بگیرم
- احسنت</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/4997" target="_blank">📅 15:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuPdMCq-qnWh8JSYyhSbnSIaHGzVTyDF8Y2iqcFPKmIfhTxTkm7AtEgQNDI05I3Jt6xRjxWPPSEn0SEbd4GwynqyiI9MsS953WcrfT0QOVQaxcH1g1z0fFVPCHbJRHnR2_U09Yk9xPAJXGl4nUv115XMtGp26TFnBaupXzlFSjy8ydpA2cUtgPZWy8ez9IiJuZftY499Vd_SmFyPfO_panU5fsVUXEnKoqunbQFOBHm7fX0H7bSU60e8PxeUKKZ_3wVc_AhM_H9j2Uqf0LVNlOpuLAlaQ0pKu17utCvIky_sFX60I8eVaZw88DgVvLCdGAUAaDVnIrjWFwexlaPo1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل نیروهای قسام در غزه دیشب به دست اسرائیل کشته شد.
قسام در واقع نام نیروهای نظامی حکومت حماسه.
مثل تفاوت نام حکومت «جمهوری اسلامی» و نیروهای نظامی اش (سپاه پاسداران)
البته ج‌ا ، متفاوت از همه کشورهای جهان، دو نیروی نظامی داره: سپاه و ارتش.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4996" target="_blank">📅 14:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4995">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0upvZX8wblEbTq3dNAt0CiJ_TLZmdIoTECyjI-_lv5pbd8TwjOONk3xsiBnedkalgXcnIExefeAdtS5FlQs8GuzAtYFCFuUVvJQQHfz8Fh6ZmeVfesNknFlmtm7FQ0Ul5KqbUBG4XaNt4zckZilv9ENUmoIzwBHdbtmHA8NWscsS3MEHig4VRaJy5q-DPY4SvKhb-zK1VGBTy7zkduqIPY29p8tQ56li86JEy6mxr-4uz1LNOeTei7a-Tp12wnxZr3FiMSxfAMEGOsYUdAK3wYbCdtn9Q2rOM3Z4bPeV_2u4OsturWU2Ij3PowyMOp-6tKXQZbnp3iBAA8CpAfYwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم جنگ بعدی‌شون در ۷ اکتبر که توی تهران و قم و مشهد هم شیرینی دادن و اینهم از ۶۰٪ خاک غزه که از دست دادن!   دیگه توی آمریکا هرگز دولتی سر کار نخواهد اومد که بره به اسرائیل فشار بیاره بیا و به گروه تروریستی اسلامگرای حماس خاک بده کشور اسلامی شعبه جمهوری…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4995" target="_blank">📅 12:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiGs9-3gidkTH--RCRnXerX2yYtKeZXMvQU-8NTaz5OOfvh4qPP0FSEuzHtjeKtvaea4_xuqfzU76XPBzvUV39YxjvAZwbGQXe2IbaA8OvCZP1ETRBBjEfVL2GEhvAToi45ug9KGDYo7SaEX89py_D9t-0nr2kAPfFb-v5B-Kotu-skfsSEA1J8ZHAS93pILPdoWcpNir10cSrzY_T3L4UPmPe6iD-SFjHdad4Fc2jKb4eSg5Mhyat6JCkQ4LlLzF1c-APUgzo4F-HPwtAn5AaHp8Z_Paj_C12VrTNJ9gN5CQyDky5IBBodGRtSztpCDHXD-XRtFjD2k4kr7Yhoc7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا سال ۲۰۰۰ از توان خودش استفاده کرد، به دولت اسرائیل فشار آورد، به شما کمک کرد گفت ۹۶٪ خاک اشغال شده شما رو از اشغال اسرائیل خارج میکنم (در کرانه غربی)  غزه رو هم که خود اسرائیل رها کرده!  بیایید و کشورتون رو ایجاد کنید.   عرفات گفت نه! ۱۰۰٪ ! کرانه باختری!…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/4994" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWM6ze7Bjt5R7aZ-M6iPBRPDhFnKCU7-3jszXf9_67diFDN1iis8u1f0H25WwaQleGfZLv6JC1d_ajUlyrocAjFecYfiULbcm9wpyAZ_59QEgvx9rPIAHNEKkWE78TxJLHJ5P35Pbna7siz6El1HCsP7OYVMtERstnZHd_Mpeu9VL3Myq3sPhsIm-D72W5L3fmsxmeYpqEbQVgCMuv88aOX1vS3PyGa9MtZcFqqe7LbkIaFfiTjL9kZglsoSwV577pVNyQB5jUNyH8aeCRDwTPwp_a0XHhYwhtUc1aODSJR6UlnPetlVo0Tah9D2mdC9iFLkHKy-57VPOvQhqCZZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض ۶ روز ، مساحت اسرائیل ۳ برابر شد و غزه و کرانه باختری اشغال شدند!  ولی اشغال نبودن!  برای ۲۰ سال هیچ وقت دست اسرائیل نبودن!  دست مصر و اردن بودن!  دست عربها بودن!  گفتن بیشتر میخوایم! نه بیشتر بلکه «همه» رو میخوایم! باختید! شکست خوردید!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/4993" target="_blank">📅 11:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crNC0ZfbIpKWUe7Td53CDp3A5Iyse0TRbDJXV5uhx4_bfrJ-8Q8LK0TXgCGW9NKPcLrtHDu53DEwU6_oUZ2FyZpQEqWiudrDNlyKlkzJrHjFQaYqJuWavQxhx-fwmnyOm8wjP-XjboPAcfzN0oTHqkfTMamnTGzXgkbfhixEIV92oVT0RjVES9DXmSrdy1AtD7r8AyHwDiJDO-bELMjWGDnV9FjSKCqSGwnI49Wgf7dgUfrH24IZHmKix_cF0XvQY6Uiq-MoElVTckP2AvVWxiia8VsFyj21XuFQdYUy-6a89Icuq-5OCXADkx-MAQYyKcZPO26at6qQP0lVlwYIcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد برای ۲۰ سال!! از ۱۹۴۷ تا ۱۹۶۷ نقشه فلسطین و اسرائیل این بود! تمام این‌سرزمین ها دست مصر (غزه) و اردن (کرانه باختری) بود.  توی این ۲۰ سال می‌تونستن کشور فلسطینی رو تاسیس کنن! اما این کار رو نکردن!  چون «همه سرزمین‌ها» رو میخواستن!  اینکه دوباره حمله کردن…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/4992" target="_blank">📅 11:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0qfEp1qUT_a0Csi4b3yvy5QasuQTIk7yNSrjTzGJYSlnKi9YCgjgjmFkOQAogf59KMd6O9AsGGcAc44GIGltQsjsFWJAQPl7LIzKjncHkaaZbJuSWjCBMqgbRz-4A54sB2nApsJbwrZFuslOvxeNLpWColEm0KgC9B9ij6uxWidQ7fpCHborKnSZLOSG3Wh2aw4z6hM92rwFrzJiE-_uPPUzlzw89LnpzoQi0GoXKMfJ1E4yRUwBV49aPfQFIUpmffg9iEvlevhCFfQ2OUTI8repUwuH8TFEesbQRQ2mYdJFHph8HFrWB00hnOOMjHTORh6xyNldIMleGTtb2hsTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی سازمان ملل، طرح تقسیم فلسطین رو ارائه کرد (فلسطین یک واژه و نام یونانی است برای این سرزمین و هیچ ربطی به عرب بودن و مسلمان بودن نداره!)  اسرائیل هیچ سهمی از «بیت‌المقدس / اورشلیم» نداشت!  در سرزمین‌هایی که اختصاص یافته بود به اسرائیل حدود نیمی از جمعیتش…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/4991" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTz_pXzUdzhgoh1QFKJw3W7KEBrsbmO3x7WcKXxg1hrk-VWpXyiXZx8XY9kZMCIz3-G_G_KSQwv6Nbu6VFTWExmQe6fw1xIs9Kv-5s4pgEQliYc0lX59fQ6Sy77Bj3gEUM91OmeHcU9QJTsj2iQq59O9NyxqnrU_WuhwLYLF4PJzI22quz_0i6L19tTa_aV2GFsseHi59dl521bMzYaLVU1RF5YHlU-soCX-SwJRGXXGjVjr4haeGAZQu5dlIJ5pNwEV4trIWrHBltjz2oLFtQ6BlPYnb5vj1u8Ybaypy2XQZ7l-Ue1wYFc__sDrYDEK67dTTa25ANFCZAY6lO3VqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیل کلینتون :  به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.  اما قبول نکردند و طرح رو رد کردند.  حماس به دنبال ایجاد یک کشور…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/4990" target="_blank">📅 11:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=nXTFhKw6bm-M5P_g-vriKhrlxdMj2LZJt3SGR4GDa517KcJMmaK7HXMk7cY-1OARTL2rqjpmWb6mocLcYjjwIZLci8kvKAKzOo5WgoIM-RsTT4MCEwuICx4xFQ_jW--uxLDDxPHnl6tXFZ03jzlJU1jRCm01a1Gmd3uvbJASIdbkPOEn7HYIr0YtT8xsfMULLEVJ9r5JY7o8n5MceWsU4SML9e7QTki0Wc_CB22YCoN85HWSKLOjJIflgsD5lmEU04EVQO2bU65IOhQ9-U4MyqDZjM11abS4IjtrNnwabOFR_woWpinj59Lf2LgBzFD3aJrTTDYQfaXGKq25FF-R6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=nXTFhKw6bm-M5P_g-vriKhrlxdMj2LZJt3SGR4GDa517KcJMmaK7HXMk7cY-1OARTL2rqjpmWb6mocLcYjjwIZLci8kvKAKzOo5WgoIM-RsTT4MCEwuICx4xFQ_jW--uxLDDxPHnl6tXFZ03jzlJU1jRCm01a1Gmd3uvbJASIdbkPOEn7HYIr0YtT8xsfMULLEVJ9r5JY7o8n5MceWsU4SML9e7QTki0Wc_CB22YCoN85HWSKLOjJIflgsD5lmEU04EVQO2bU65IOhQ9-U4MyqDZjM11abS4IjtrNnwabOFR_woWpinj59Lf2LgBzFD3aJrTTDYQfaXGKq25FF-R6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیل کلینتون :
به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.
اما قبول نکردند و طرح رو رد کردند.
حماس به دنبال ایجاد یک کشور و یک میهن برای فلسطینی‌ها‌ نیست. فقط به دنبال کشتار اسرائیلی‌هاست.
🔺
بعد از عملیات ۷ اکتبر ۲۰۲۳ ، اسرائیل ۶۰٪ از خاک غزه را نیز تحت کنترل خود درآورد.
در تاریخ ۷۰_۸۰ ساله اخیر، هر بار جنگی راه انداختن تا با جنگ، سرزمین بیشتری بگیرند، بیشتر باختند.
🔺
امروزه در دنیا، نه آمریکا و نه کشورهای عرب، هیچ کس هیچ فشاری به اسرائیل نمیاره و دیگه سرزمینی به فلسطینی‌ها تعارف نمیزنن! هر بار بهشون تعارف زدن گفتن کمه، جنگ کردن، بیشتر واگذار کردن!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/4989" target="_blank">📅 11:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLqjZoisW1ljczgoATxhoUkuUjiZ7uqx8NqFAGOlKevVBZcFZ9mn1AiiYcZYKNXIRif5cvMa1H3Id7REcw4Ve3q3nPNh_FMOmXm_eYuvr6yjUI0PflJ-tZ3stSXDGYITtpNnZNK3CwHVhfKqCgq2CEpshkQ_NlIZ13AAwLpggUREkAiYLq8JkopTa4-QcvhrkHWx_NIkwNJD5TPdWLh4OLNFSf8B1ohBCZ4PQ4oiHEXlnF-uZKbWMMSQjS4ohGgwv8YV-TrVGx6Iy5Xx9iWXsYxM0zDwElsRDqSNOnVJWYzV_LH3msPTsO0WaYGAPOYUFKyO67tL8HQAZFOxS0NgEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/4988" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oL8Vx7Al5oHrTgzh5b-udeHRKvilW3_UrRt0nhrDarhihJv6vNROWbwWztHRYULhuybAwcoxJB4ZZurjRZIM37GxEK0Q9ugxvB7XlVCeAtVPPAUi_TWhkmomcKQJTvqa6epQUR-15yRd5C-vEuqRYewPmj3sF2ddjDs170yoGKfCRhk5d3xtdsSatwcBHhwyZlUaUG33lGoy6KwnxXuFy2oj6ZzJ27S2CFynECEMEm3Vfn2ALGkbrgn8UuGw2vbb_96npvMZv4TQgnmImZlRxmPg-1R4A1h1225DYaGeAsfANOUSWt30aCBfCbj6NEvleQ89EiWpFPQPRS60kuY5cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4987" target="_blank">📅 10:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4986">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=Q4W-zGFFmVDp5OuSjldFD4X5Te39zgJsp7S-muJZMSSooaiVR2YqgB64P7Lm7DivnN35h3MhhCZCwcJPqD2KSXLEzSzq-4w2uiGRzs5d2LhW4WGVKSnTUwKORgHS3KYbIen9dbNvTtrFGbWf1b2IMzOdJ-UJqPGWptSkS8gy6jsGiwdBTIe7ugp31YTwQHoo55y0iKhranAkCXd0vVZSH8z8czNTrfE2lTItBWu3mfVh71MnC-9c_teL4dCFTWKq86c9uWbRHLUjzxF3pHk46eSzcgwGZlMJ3OEPixpdKW9JPUaw9pzCXtT2vKuJz3yYVxXBfBoZR7N4MX09jDWqJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=Q4W-zGFFmVDp5OuSjldFD4X5Te39zgJsp7S-muJZMSSooaiVR2YqgB64P7Lm7DivnN35h3MhhCZCwcJPqD2KSXLEzSzq-4w2uiGRzs5d2LhW4WGVKSnTUwKORgHS3KYbIen9dbNvTtrFGbWf1b2IMzOdJ-UJqPGWptSkS8gy6jsGiwdBTIe7ugp31YTwQHoo55y0iKhranAkCXd0vVZSH8z8czNTrfE2lTItBWu3mfVh71MnC-9c_teL4dCFTWKq86c9uWbRHLUjzxF3pHk46eSzcgwGZlMJ3OEPixpdKW9JPUaw9pzCXtT2vKuJz3yYVxXBfBoZR7N4MX09jDWqJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین یکتا، همون چهره‌ای است که قبل از شروع کشتار ۱۸ دیماه اومد تلویزیون و گفت خون هر کس ریخته بشه پای خودشه و بعدا گلایه نکنید!…
این همونیه که اومد حامیان رژیم رو دعوت کرد که هر شب برید توی خیابون‌ها
حالا هم در کنار تیم ملی فوتبال، در یک اجتماعی اینگونه رسوا، داره مجری‌گری میکنه و میدان ‌داری.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/4986" target="_blank">📅 09:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4985">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمملکته</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=MP7Cyt6_nGudX4YMNOvXz4M9At0p7gVIwXTBUKtjwqVD7uNSazR1nlyIg9cLh92oAgMXd5t6s1xKhFeFVdCe_zcvm7_TpVFnE3I4Ie_m609EYLDKN_rz8MNE0bee2RABulCTTxEgMcZDe4anaHHUQ0EuoZDCotXMAep5Ac1sh8sLL-zkDd8geo7pK9c-_IqPmeboMH8gi9JvlaTThkJIz1AsvVOw7S9NeB9QO-LdipdEP4vdR8hG_Ev0T0d5sAlEfRjU-d_RrxDO1CIWUQ6BR9pa_DCRE6NzsFQnXthuGx6iT44f8RrucgOg-SI3no91feTS9qqMlpF3vd65lBC1Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=MP7Cyt6_nGudX4YMNOvXz4M9At0p7gVIwXTBUKtjwqVD7uNSazR1nlyIg9cLh92oAgMXd5t6s1xKhFeFVdCe_zcvm7_TpVFnE3I4Ie_m609EYLDKN_rz8MNE0bee2RABulCTTxEgMcZDe4anaHHUQ0EuoZDCotXMAep5Ac1sh8sLL-zkDd8geo7pK9c-_IqPmeboMH8gi9JvlaTThkJIz1AsvVOw7S9NeB9QO-LdipdEP4vdR8hG_Ev0T0d5sAlEfRjU-d_RrxDO1CIWUQ6BR9pa_DCRE6NzsFQnXthuGx6iT44f8RrucgOg-SI3no91feTS9qqMlpF3vd65lBC1Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
جمهوری اسلامی به جایی رسیده که نفر آورده با ماسک آموزش کلاشینکف تو برنامه زنده صداوسیما میده
📝
توان جنگیدن با آمریکا که ندارن (در صورت جنگ زمینی)، این برای کشتار مردم بی‌سلاح ایران در اعتراضات آینده ست.
📝
اسلحه بیاد بین مردم، فرصت انتقام تعدادی از ده‌ها هزار نفری که توی دی‌ماه کشتند هم بوجود میاد اما ابعاد این احتمال بزرگ نیست. ابعاد احتمالی مسلح شدن، اختلافات بین باندهای مختلف مافیای اشغالگره که با تنگ‌تر شدن محاصره اقتصادی، از خشونت سیاسی به خشونت فیزیکی دست خواهند زد. برای پول راحت‌تره آدمکشی تا برای عقیده.
@mamlekate</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/4985" target="_blank">📅 09:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4983">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUinDCoRUP4s8nyOiTMk0fY5A7pQmqV4osk77dCOHNOEX0oG96ZzaVfBHOKRYZQF-dUUc02TidBUkW_dwON9x48FiXxunQWE8Jkd5n9JdOyIu1XEINzPGc6wrtWugSwgwIEnAtwSMijRK19EjrT6um8l3XbpUsBnrQCcLdw5YCWjXWql4sUSB88byIatzXM20lpBQ5GCsPKHxkvtUXab53fmMpO8frXg4qs5DAXSHCBzBoDV4JEdbZf5pWk_rsXmb81hSQwRtfRw8E0yhRR_6TuRpltPK6U866jRqzl3Tx-xmaWwRmzgMhEi7AnUbvMcu7lt_5VVOCp124_T-1THVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=lLCkhIkrSgqMBM6Ik6Ei0XZ8byLxHVSRovU4zw3sUjNOmrPrS6fTp4ewXCJhzrIs1SF6lwdEpseso_MLRk9mg3yQEyXUJdomTlRu0N6jkUAi7CVuyDgTH7lE7f0HNTxL0sSVQlThfSxMQ-3k0sLEToXuq6o47lJMHopHfgb-1MKE0YUuBQF5lxkHHAL9a-6QNF5VRCF8B__ReCJ2yl6Dkln6IojxqBW_p3um_m0VTCr_VBBe0vdktp41yGe7gmQtJcsI1myFgXAOp3_tccY7jjbtc5tEPu3TUd7IrR8nWIjUEEi1m2nH3K-hG5aV4ObeIli3hZjmNDXOBK2aWRtukQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=lLCkhIkrSgqMBM6Ik6Ei0XZ8byLxHVSRovU4zw3sUjNOmrPrS6fTp4ewXCJhzrIs1SF6lwdEpseso_MLRk9mg3yQEyXUJdomTlRu0N6jkUAi7CVuyDgTH7lE7f0HNTxL0sSVQlThfSxMQ-3k0sLEToXuq6o47lJMHopHfgb-1MKE0YUuBQF5lxkHHAL9a-6QNF5VRCF8B__ReCJ2yl6Dkln6IojxqBW_p3um_m0VTCr_VBBe0vdktp41yGe7gmQtJcsI1myFgXAOp3_tccY7jjbtc5tEPu3TUd7IrR8nWIjUEEi1m2nH3K-hG5aV4ObeIli3hZjmNDXOBK2aWRtukQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/4983" target="_blank">📅 09:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏ترامپ: امشب، به دستور من، نیروهای شجاع آمریکایی و نیروهای مسلح نیجریه، مأموریتی بسیار پیچیده و با برنامه‌ریزی دقیق را برای از بین بردن فعال‌ترین تروریست جهان از میدان نبرد، بی‌نقص اجرا کردند.
ابو بلال المینوکی، نفر دوم فرماندهی داعش در سطح جهانی، فکر می‌کرد که می‌تواند در آفریقا پنهان شود،
اما نمی‌دانست که ما منابعی داریم که ما را در جریان کارهای او قرار می‌دهند. او دیگر مردم آفریقا را ترور نخواهد کرد یا به برنامه‌ریزی عملیات برای هدف قرار دادن آمریکایی‌ها کمک نخواهد کرد. با حذف او، عملیات جهانی داعش به میزان زیادی کاهش یافته است.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/4982" target="_blank">📅 09:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=Y92kxe8dwieFwwFHuPNgGqxfFIHhHmpJ7aO_Ub618IB1E1P7tjAlgVUdBM4zKTBgxbKXjnvuppyrHPv0WhwCRypVqGgJykhIRVBAacexzgXyfne0GE_XY-RXDbsKNUh48NmALTuZe0eMd1A_-uMatOVLfCNdafQOYYGjlYkP1JqrUkzXsS5pyyTdrhjmoV9VlJQTb0e4OcaCZGzfWY3aPzVdj4iYJHS3ypRhHtV2cMKtCuL0ajDBOaAI7TJ0CN4S_jFEG7rM5KrZXz9AE0eHthKNiDivUmtpZJSfBO1kf2WTqbPjwJXgEImRqBT6goWkUj4hvu2XFqBPGAgFsunDJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=Y92kxe8dwieFwwFHuPNgGqxfFIHhHmpJ7aO_Ub618IB1E1P7tjAlgVUdBM4zKTBgxbKXjnvuppyrHPv0WhwCRypVqGgJykhIRVBAacexzgXyfne0GE_XY-RXDbsKNUh48NmALTuZe0eMd1A_-uMatOVLfCNdafQOYYGjlYkP1JqrUkzXsS5pyyTdrhjmoV9VlJQTb0e4OcaCZGzfWY3aPzVdj4iYJHS3ypRhHtV2cMKtCuL0ajDBOaAI7TJ0CN4S_jFEG7rM5KrZXz9AE0eHthKNiDivUmtpZJSfBO1kf2WTqbPjwJXgEImRqBT6goWkUj4hvu2XFqBPGAgFsunDJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها نشانه سقوطه. نشانه هراس.
پروپاگاندای پوشالی رژیم رو باور نکنید که میگن بعد از جنگ قوی‌تر شدیم!
اینها ۷۰ روزه رهبری دارند که خودشون هم تردید دارند که واقعا داشته باشن.
اینکه ۷۷ شبه، هر شب هراسیده در خیابان جمع میشن. اینکه ۷۷ روزه اینترنت رو قطع کردن و علنی هم میگن چون ترسیدیم و …
ترس اصلی‌شون هم مردم ایرانه!
و اینکه خون اون چند ده‌هزار ایرانی که ظرف دو شب کشتن ، حکومت ظالمشون رو غرق کنه.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/4981" target="_blank">📅 08:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWAfKfSQDrU5OTGMzed8jrGq3m-KZ6BCpvMtrZLxXJ_zXQv4MYYpf4YIE3nVi7bXZAOwpWxgG2Zz7VY6Tvd0HenYcwtThJq6_LUVG-y2FUxsWmGrP4o2k1kcSbksL68ea0_enQZzaheD0t-umt9fZRm8tkPc6LYxrIZsxcXyb4unDI-8a21sEBHT3zB69QaAUUWomNyauJLcOS16YZl8HaA--fBNYWn5uDfhtIkhZKQdKJRk3f3Y0ARghUwNnf1b3VgVz7kbU1PMhC3ZXLizWiwTiY2tIBWcT8k6E8ryIUoH60YYUOI27yw1nBcMfI8xafw9jtfN7sGSEnscm3UbWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفت‌وگو با فاکس‌نیوز با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او 'گفت: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا گفت شی جین‌پینگ، رییس‌جمهوری چین، برای کمک به حل بحران ایران و بازگشایی تنگه هرمز اعلام آمادگی کرده، اما تاکید کرد واشینگتن «به کمک نیاز ندارد.»
ترامپ گفت چین «۴۰ درصد نفت خود» را از منطقه تنگه هرمز دریافت می‌کند و افزود: «اگر او بخواهد کمک کند، عالی است. اما ما به کمک نیاز نداریم. مشکل کمک این است که وقتی کسی به شما کمک می‌کند، همیشه در مقابل چیزی می‌خواهد.»</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4980" target="_blank">📅 08:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QV7BYjWh5YT4uoLfvL7mfvCZJ5NejJwL0UVTYscEoBBp-uW6b_hd6CrR5UFn6zzI2ICNdblj7oEqTxf-3sexjI36FQXKXX4LxUJ8bGxpHz5VST4CC_5nVJGplODAGof9rFBfO13RIp8Bl_7knjxqDAbfc_wR_dKmxcn4WtnP2T9Ty2LMwIpaNwr9MYEHCnKocwTJplJrDKj1CtaJj7wlgzVBB50I1nYLsJAqLCZyqpAfzMtVqisduofia5guY7LVdHXqQJasYB2z7hNqy2wsTf3WTECvp8eVkI7vJk0nX64q-1lqMM6OZlN7Y8Qx6MHnp5lH_3S03xGUc7Ddqs8duA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن رهبر شجاع‌شون  ۷۰ روزه قایم شده
یک عکس بیرون نمیده!
یک فیلم ازش منتشر نمیشه
یک فایل صوتی ازش منتشر نمیشه
پیامی که میده حتی امضا هم نداره!
از طریق امضا می‌تونن جاشو پیدا کنن؟
یا موضوع چیز دیگه است؟</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4979" target="_blank">📅 19:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FU8_TgJoJYXoCIHrHg5f0U6toHA9mDj-Fh7ShckYA7S2eNvsNzX93kHWmhPB5LGSr9Hfn8JNXYM2ddMCmze4r6m7WdVkkRQY6yY4hZyvr_jeocXOt0gduOLehq4tVL9LZrp7WS-R3oHdwSjxgpVbyF6CVaLCwK3wNyseo8_qUuh2X0VkF-9SiKx2DP4Q4wcxwmNckwgo_pZJS6V_6PUEZXLcP2KB8-0ca-Id2XTLW-wZWL7vXNJeROQ4S4qegN7vH3obFzp2N8kcw8hiw8_URKE4GZ5rGubRnxv7rGk3R2_kQpiVCsN3xWMAHbxFv7GHqeLv0WF6xihuvCDRXlwD8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4978" target="_blank">📅 18:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9OVvbolGykXARFz7r9eVbQRZljGtnsLwV0kVn3pxmAFlbdITeUnkTyGsiV8qKonrUtm7I2zfyBeIsgKg3_PksOBYIoBYRa6cebHVgNMGhSuwXxyzvyrkD3wApC_fWspKlKCQvVqLsPluhpbbkDOph2XDTlftWzFo0kbitHK7CuHJTkATyTWXjtPGqItnfLGxwxz7LoIBAETutAvvFPToagweA_n4ry3HNLACflSXOk5LM7t2mu_t_uY6BYK1R0qpLOrG3tzeiYSK0MDrk6GPg_aM0qoLipYjqPhHRHfHVnWFi79cLpe_paiUDVc7vy6jtl7MXJbaJS_CVkVAtZtXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت آمریکایی تمام هدایایی که چینی‌ها بهشون داده بودن، قبل از سوار شدن، در سطل آشغال ریختن،
نگران از اینکه مواردی در این هدایا باشه که برای جاسوسی استفاده بشه.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4977" target="_blank">📅 16:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
برد کوپر، فرمانده سنتکام، گزارش‌ها مبنی بر اینکه جمهوری اسلامی هنوز ۷۰ تا ۷۵ درصد از ذخایر موشکی و پرتابگرهای پیش از جنگ را حفظ کرده است «نادرست» خواند. او در جلسه کمیته نیروهای مسلح سنای آمریکا گفت ارزیابی‌های منتشرشده درباره توان موشکی جمهوری اسلامی با واقعیت مطابقت ندارد، اما از ارائه جزئیات اطلاعاتی خودداری کرد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4976" target="_blank">📅 16:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=WYRcu8zqLp0i9A9z5-r3T9DFcYZHClTkCsZM2RAtBlbtN8AOqX0NuEBm4plfcmH3QEkvwVqtdqDtpG6zkl5f825NUWVPfynr1wP3EmpefKPEFhC6njHVKcPOU4oL-NZnHxX3lUGRWW9ABrZ-ZGfBsl5xTaKgu5m77Y5bZKL5wH3mSGpg-JbtwaleNm7GOtpPaIIaJqKrxYEzpT04KVLhxk5BoBT1ZxYvSO_iVkDsR_Rw5LwNuqqmPGZ1yY3be3UmlrxjhwSHoGoEDZubENJjHRg5uReOLhCjhCh0WPPyCvfZght6QoxsShxAQ7Dfbr2Ioa6BhnY9E-LTJ5oTib2i1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=WYRcu8zqLp0i9A9z5-r3T9DFcYZHClTkCsZM2RAtBlbtN8AOqX0NuEBm4plfcmH3QEkvwVqtdqDtpG6zkl5f825NUWVPfynr1wP3EmpefKPEFhC6njHVKcPOU4oL-NZnHxX3lUGRWW9ABrZ-ZGfBsl5xTaKgu5m77Y5bZKL5wH3mSGpg-JbtwaleNm7GOtpPaIIaJqKrxYEzpT04KVLhxk5BoBT1ZxYvSO_iVkDsR_Rw5LwNuqqmPGZ1yY3be3UmlrxjhwSHoGoEDZubENJjHRg5uReOLhCjhCh0WPPyCvfZght6QoxsShxAQ7Dfbr2Ioa6BhnY9E-LTJ5oTib2i1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : می‌دونم سؤال‌های زیادی در خصوص سفر چین وجود داره ولی بگذار اول در خصوص پیشنهاد جمهوری اسلامی بپرسیم ، آیا شما طرحشون رو رد کردید؟
ترامپ : من طرحشون رو نگاه کردم از سطر اولش خوشم نیومد دیگه انداختمش دور!
خبرنگار : توقف ۲۰ ساله غنی‌سازی برای شما کافی نیست؟
ترامپ : آره توقف غنی سازی ۲۰ ساله خوبه، اما در تضمین این توقف تردید هست باید ۲۰ سال واقعی باشه نه ظاهری</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4975" target="_blank">📅 15:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
ترامپ در خصوص ایران: ‏«ممکن است مجبور شویم کمی کار پاکسازی انجام دهیم، چون یک آتش‌بس حدوداً یک‌ماهه داشتیم.
‏ما در حقیقت آتش‌بس را به درخواست کشورهای دیگر انجام دادیم.
‏من خودم چندان موافق آن نبودم، اما این کار را به عنوان لطفی به پاکستان انجام دادیم، آدم‌های فوق‌العاده‌ای هستند، فیلد مارشال و نخست‌وزیر.»</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4974" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا دیروز گفت که : «در جزیره خارک در سه روز گذشته هیچ بارگیری نفتی انجام نشده است. معتقدیم مخازن ذخیره کاملاً پر شده و هیچ کشتی‌ای وارد یا خارج نمی‌شود.»
او افزود که این وضعیت باعث تعطیلی قریب‌الوقوع تولید نفت خواهد شد.
با این‌ وجود امروز خبری منتشر شد، مبنی بر اینکه  یک تانکر بالاخره بارگیری کرده و اعلام شده که «برای اولین بار» در طول یک هفته اخیر بوده.
جمهوری اسلامی بخشی از نفت اضافه خود را در تانکرها و نفتکش‌های کهنه و‌قدیمی ذخیره می‌کند تا جریان‌ تولید، نفت متوقف نشود.
با این‌ وجود و در صورت صحت این دو خبر (عدم بارگیری در سه روز اخیر، فقط یک بارگیری در یک هفته اخیر) این به معنای مشکل جمهوری اسلامی در صادرات و یا ذخیره نفت است که می‌تواند به توان استخراج و تولید نفت ضربه بزند.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4973" target="_blank">📅 10:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔺
رسانه‌های اسرائیلی : ترامپ در بازگشت از سفر چین، در خصوص از سرگیری دوباره جنگ با ایران تصمیم خواهد گرفت.
تحلیل شخصی‌‌‌ام: گره میان جمهوری اسلامی و آمریکا و اسرائیل، از زمان روی کار آمدن مجدد ترامپ تا وقوع جنگ ۱۲ روزه با گفتگو باز نشد،
سپس در مذاکرات در حد فاصل جنگ ۱۲ روزه تا وقوع جنگ ۴۰ روزه، این گره‌ باز نشد،
از زمان آتش‌بس تا امروز ، که ۳۷ روز از آتش‌بس میگذرد، از جمله در مذاکرات سطح بالای اسلام آباد باز نشد!
بلکه حتی این گره به واسطه بسته شدن تنگه هرمز، کورتر هم شده و هم به واسطه حمله جمهوری اسلامی به کشورهای عربی منطقه و پاسخ نظامی آنها، وضعیت بدتری پیدا کرده.
از آنجایی که هم جمهوری اسلامی خود را پیروز جنگ ۴۰ روزه می‌داند و این موضوع در مذاکرات اسلام‌آباد هم کاملا واضح بود و عامل اصلی شکست مذاکرات شد، و هم آمریکا خود را پیروز جنگ ۴۰ روزه می‌داند، اما تمام مشکلات هسته‌ای، غنی‌سازی، موشک و… سرجای خود هستند، پیش بینی وقوع جنگ سوم بعید نیست و احتمالا این بار جنگ با حمله به زیرساخت‌های ایران شروع شود.
برخی از کارشناسان جمهوری اسلامی در صدا و سیما حتی پیش بینی وقوع «چند جنگ» در دو سال آینده را مطرح کرده‌اند.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4972" target="_blank">📅 09:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VYFnrGBhdFhFSLzBQA9zWR9In29_GIiMbIYM6-WcAtHfj3-2c4FKWImSY71HecxdE1s6mI6lEADO_HcdItEAz4IEcbet_ceJWyCR2VV7HRz-EWC5CnLFvbtQAsKBB_kK_6Wlchnn1L96lkBdNFO3WKu6aR9ZLSGxEhZp1UJf_KEU2M81zMrNG1efw7riuCpS3poq-mYJEpv1Ijfm1M-G9RFy7G8nx74v-UdPUM5KGDf9SlHF-akyxptxM5NYSB1FSlVLtc0lh9DSz2hTEsuMiDX8C13ybSM6MX3NoR2ugl4g3dZ7tuuK7O6pE3vfiXeYVlAkKPOqCTvwIR-PGAhKrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yo1norauL1NagSMKj-ckPwRGJ4ID3B3ugbjmnSjgR8P6PbR1TBkno7Cpm8TQBDtlrNjar0BpeuOXrEoJ6bJY2m3ulc0_GO_oCZufw2qWomlN-_djpH-ZyTCHnZ1uGUogT8EyoyBslKRtWdDyFAiUlykpP4pycGcdBublpSIs1v4N6Nbuc_K-wHqH39ucZnNaFLLdm3dlYiMiB18NQb6pm91UIEPqaAv6jgzVjm49NnIfmA_i9fT14lIiYWVftoRt-XFj9N_YsJaKYj4niRRZxQw6b03R1CEWZE1sOeKndSPlxy8iSyyTAuQGvtF6TrLfISXSU2moGgjpSu1Z4oK_Xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی توییتی زده
که «هر کس در نهان خیانت کنه، به طور علنی رسوا میشه»
که منظورش اماراته و بحثی که بین عراقچی و نماینده امارات در جلسه «بریکس» رخ داده! و اتفاقا حرفهای عراقچی نشون میده که امارات بوده که اینها رو رسوا کرده و به شدت ناراحت شدن از حرفهای نماینده امارات که چرا در این جلسه چنین حرف‌هایی زده.
اما با زدن یک توییت! اعلام پیروزی میکنن!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4970" target="_blank">📅 08:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZhBlWfJjxsA5OeOYaw5bUjR06VrZXvzl-VwJmhoi2-kBkATc-BXvp1tofJrYNEorsexs3Qp9zJdSTVxiEVBSDo2hAjUsB_7Mr58rP0Bp9aUEliOHKEZb20gIlbop-YqM_tdRjBhYfwL6odwMh5W5ytRLAHdRlX-dl8U6opT7vr-dl9ovQLUnD92K5jZBOSHs3LoiSIbX5I9BQDlhAElMDJZdEwsZjU0OglTdG7O0fH6718-z7Z4D0e5Slk6DsWop-Hmb-cQRQHXQvY4_DcKUVRL0TwFeQyWQq4kfo9pJo_F3zIOf7NHIzBE_NlqA74LOMcFvrP0oKDvoNx4KuGk3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس جمهور در صدا و سیما:
با علی افشاری، پرستو فروهر، عبدالکریم سروش و….. تماس گرفتم
و از مواضع آنها تشکر کر‌دم</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4969" target="_blank">📅 08:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نامه رسمی کشورهای عربی به سازمان ملل برای درخواست غرامت از ایران
بحرین، کویت، عربستان سعودی، امارات متحده عربی، قطر و اردن در نامه‌ای مشترک خطاب به سازمان ملل، خواستار پرداخت غرامت از ایران برای خسارت‌هایی شده‌اند که جمهوری اسلامی در طول جنگ به این کشورها وارد کرده.
این درخواست در نامه‌ای که دیروز به آنتونیو گوترش، دبیرکل سازمان ملل متحد ارسال شد، گنجانده شده است. در این نامه، آنها همچنین ادعای «غیرقابل قبول» جمهوری اسلامی درباره قوانین جدید عبور کشتی‌ها از تنگه هرمز را محکوم کردند.
پیشتر نیز در اجلاس اضطراری وزرای خارجه اتحادیه عرب نیز قطعنامه‌ای تصویب شده که رسماً از ایران خواستار غرامت شده بود.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4968" target="_blank">📅 21:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=gNdYh4xOBIhdCwFCq2VDMwjfw-lKtrf538OdfXv3hoE6qhCMFC608AMuunvKXN3BDqGYlPHqSlailcQRU643iJtQUMixyr6joxkG5eZ9xpJkxxblFbX9MpJGLrZ95es2Ljt3_4Vo8F7cymrFHmX61CtmkQdlRTX1Pmrft0k0OkdjJJej3-2n-GJWgXg5Te7BJFtUXOnkVJ0ZNb4pHmYzN3RtwtPNiEugflEzozW9WLrzLaqdBjowfVK7CXHKKeaRO7P7XlY0XTv0Db51StHzZpTEgNV1kZ56GywkOIGWWjk_v8cZDqqdln1M1cD_GEK_ZNTNEX2ZvTWS65C4f-bPAD3R5ZBunPoWFTjMYOwdZ7YMkR6wTku2BuGjfv7YhagWniLFaxE5Juf0ajrHmbnrVUMRLLK-298ypAV13GmFEsLYIwSUqOskDWgT1h5_jBFmo_1-sn6yI0ZpeTd0xRJOsYF8Do0G6YDofFu_MtH47wPoPIknn4mkBva83SPuC0-mr7HyOYAV6yPMAeQoODX8MTTgpTQp709Kijl48sEGbkro0z8fSpfDP4zeU_PepRP-6cepZTasJ5o7pL2J-5tQygJUBW0NL0yn7WhOwqhaRM0ruOFeByzjGzUrpcCO3tT2lkx6XPE_jLR4lnFDZSf1YcVtFaj_apUjp38sPyJBwF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=gNdYh4xOBIhdCwFCq2VDMwjfw-lKtrf538OdfXv3hoE6qhCMFC608AMuunvKXN3BDqGYlPHqSlailcQRU643iJtQUMixyr6joxkG5eZ9xpJkxxblFbX9MpJGLrZ95es2Ljt3_4Vo8F7cymrFHmX61CtmkQdlRTX1Pmrft0k0OkdjJJej3-2n-GJWgXg5Te7BJFtUXOnkVJ0ZNb4pHmYzN3RtwtPNiEugflEzozW9WLrzLaqdBjowfVK7CXHKKeaRO7P7XlY0XTv0Db51StHzZpTEgNV1kZ56GywkOIGWWjk_v8cZDqqdln1M1cD_GEK_ZNTNEX2ZvTWS65C4f-bPAD3R5ZBunPoWFTjMYOwdZ7YMkR6wTku2BuGjfv7YhagWniLFaxE5Juf0ajrHmbnrVUMRLLK-298ypAV13GmFEsLYIwSUqOskDWgT1h5_jBFmo_1-sn6yI0ZpeTd0xRJOsYF8Do0G6YDofFu_MtH47wPoPIknn4mkBva83SPuC0-mr7HyOYAV6yPMAeQoODX8MTTgpTQp709Kijl48sEGbkro0z8fSpfDP4zeU_PepRP-6cepZTasJ5o7pL2J-5tQygJUBW0NL0yn7WhOwqhaRM0ruOFeByzjGzUrpcCO3tT2lkx6XPE_jLR4lnFDZSf1YcVtFaj_apUjp38sPyJBwF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور چین، شی جین‌پینگ،
با موارد‌ زیر با رئیس‌جمهور ترامپ موافقت کرده:
۱.
در موضوع ایران، به آمریکا
«هر چیزی که ترامپ نیاز دارد» بدهید
.
۲. سویای بیشتری بخرید.
۳. نفت بیشتری از آمریکا بخرید.
۴- ال‌ان‌جی بیشتری از آمریکا بخرید.
۵. ۲۰۰ فروند هواپیمای بوئینگ بخرید.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4967" target="_blank">📅 20:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=erI5IJPXbkNyBscF8w2gNOqXBQffC5Ue2u0zs0FYjEiUsGGfdbbKzFp7MW9bT-8DsfKYyBWJtUbE5DSfyx05C5kEahMq-bv-pFYT6PqvgVZpcXPiHQMUU-icQNOT2BeBVHv7fsKg4pPtGj9HbHCHBc9rtERkrWWj3t0dEb3j9Y9F9GtfN_7OvtQFAndqNzGJAEoOlAVK77GidJWYKHA_xDxYkhSAEf3ZcJt4ysqhKo0sU0pgqJh9w4zJ3ZKRaj-yGLTgBBkBHEDdDo9KDxBYjgfAZwksUa3yt-3RJWFTH1C5SYJqTdwn01ytzgM7lXSXAbX4qh0I-fcUjkfnepcQ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=erI5IJPXbkNyBscF8w2gNOqXBQffC5Ue2u0zs0FYjEiUsGGfdbbKzFp7MW9bT-8DsfKYyBWJtUbE5DSfyx05C5kEahMq-bv-pFYT6PqvgVZpcXPiHQMUU-icQNOT2BeBVHv7fsKg4pPtGj9HbHCHBc9rtERkrWWj3t0dEb3j9Y9F9GtfN_7OvtQFAndqNzGJAEoOlAVK77GidJWYKHA_xDxYkhSAEf3ZcJt4ysqhKo0sU0pgqJh9w4zJ3ZKRaj-yGLTgBBkBHEDdDo9KDxBYjgfAZwksUa3yt-3RJWFTH1C5SYJqTdwn01ytzgM7lXSXAbX4qh0I-fcUjkfnepcQ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4966" target="_blank">📅 17:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2182de948.mp4?token=QB8v0ORkknVeWtjCbWG9mqRTb4P-glgj-4psA9wfGnKEFpFuGK-uY5-kDTxu2k9ujqYJAuH9BNCDYrjO2Is2XVGANbzMHmRSTkOpW9eqxFtlp9GUuu4M2FP1cpxmEcna82HExTMpu_yonF2dss0IBiDl2KvWn9qOCfTcUjFzn_CFRlHi3ObvYm56HhsjlH8TMhDWm_4l8tSLqN7QkT-ETmQTxqsaGhYjhA34T0-8x_5Nm52MK15v3MrTom81AIOoF5hlPDWwTB911owQnecl0YWfG2SU0sHzMSdu_d3LKUmIq-R00dVHItDOVhLEfqWY9S16aaB04MA0AXFTgQAXBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2182de948.mp4?token=QB8v0ORkknVeWtjCbWG9mqRTb4P-glgj-4psA9wfGnKEFpFuGK-uY5-kDTxu2k9ujqYJAuH9BNCDYrjO2Is2XVGANbzMHmRSTkOpW9eqxFtlp9GUuu4M2FP1cpxmEcna82HExTMpu_yonF2dss0IBiDl2KvWn9qOCfTcUjFzn_CFRlHi3ObvYm56HhsjlH8TMhDWm_4l8tSLqN7QkT-ETmQTxqsaGhYjhA34T0-8x_5Nm52MK15v3MrTom81AIOoF5hlPDWwTB911owQnecl0YWfG2SU0sHzMSdu_d3LKUmIq-R00dVHItDOVhLEfqWY9S16aaB04MA0AXFTgQAXBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4965" target="_blank">📅 17:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
سپاه یک کشتی رو در اطراف امارات (فجیره) توقیف کرده و در حال انتقال اون به سمت سواحل ایرانه.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4964" target="_blank">📅 11:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=oRExFwvb8reOugkbv4iHlEJOixw6X9aaGsk_-PMoACkJjuqCjhfXzAuKM0S9qwrWgICOuP3bLzDeqrHkya2PhBjPd-RFBN7KIpOITtwQ6eAcFMtgZU7qkS9IGUrvewaXfcBhUVk8EUT4A5N6ws9MKezmA0nH67umKfWAQe0_6DZ6388WXhho7g_XgtSgDBx3woBb3LR5Tt_sgvP8ikMvGYqvUUO7_ihFD6ogSCQpe7-JzS_T-Rd0NKwcH5seBYChofoRVq1Az3H4OUuSb-dr9X_gHU84_aR4zWNxIn55yeeyfw1JrC_uvw0ZGRK3eF7yprc3Zo0AIndr-9xKwbedZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=oRExFwvb8reOugkbv4iHlEJOixw6X9aaGsk_-PMoACkJjuqCjhfXzAuKM0S9qwrWgICOuP3bLzDeqrHkya2PhBjPd-RFBN7KIpOITtwQ6eAcFMtgZU7qkS9IGUrvewaXfcBhUVk8EUT4A5N6ws9MKezmA0nH67umKfWAQe0_6DZ6388WXhho7g_XgtSgDBx3woBb3LR5Tt_sgvP8ikMvGYqvUUO7_ihFD6ogSCQpe7-JzS_T-Rd0NKwcH5seBYChofoRVq1Az3H4OUuSb-dr9X_gHU84_aR4zWNxIn55yeeyfw1JrC_uvw0ZGRK3eF7yprc3Zo0AIndr-9xKwbedZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب اگه نهادهای اطلاعاتی آمریکا متوجه شدند که جمهوری اسلامی به ۳۰ سایت موشکی از ۳۳ سایت موشکی در کرانه‌های تنگه هرمز دسترسی پیدا کرده،
[دسترسی پیدا کرده، یعنی در حملات آمریکا دهانه ورودی این سایت‌ها مسدود شده بود و دوباره دسترسی پیدا کرده]
نمیشه سریع اینطور نتیجه گرفت که : پس اگه جنگ از سر گرفته بشه جمهوری اسلامی قدرتمنده و…. چون دسترسی پیدا کرده.
این گزارش یک بعد دیگه هم داره
:
اونهم اینکه نهادهای اطلاعاتی آمریکا روی این۳۳ سایت موشکی اشراف اطلاعاتی کاملی دارند!
می‌دونند دقیقا کجا هستند،
موقعیت جغرافیای اونها رو دارند، و این گزارش یعنی وضعیت اونها رو مرتب رصد می‌کنن!
و خب اگه حمله‌ای بشه، می‌تونن در همون ده دقیقه اول شروع جنگ،
اول دوباره دهانه اینها رو ببندن!
اگه قبل از جنگ ۴۰ روزه نمی‌دونستن
موقعیت این سایت‌ها رو،
و در پی حملات موشکی جمهوری اسلامی پی بردند به موقعیت این سایت‌های موشکی ، الان همه رو زیر نظر دارند و رصد می‌کنند
و شناسایی شدن!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4963" target="_blank">📅 10:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فهرستی از رهبران کسب‌وکار که به همراه رئیس‌جمهور ترامپ در سفر به چین شرکت  کرده‌اند:
1. ایلان ماسک، مدیرعامل تسلا و اسپیس‌ایکس
2. تیم کوک، مدیرعامل اپل
3. لری فینک، مدیرعامل بلک‌راک
4. استیفن شوارتزمان، مدیرعامل بلک‌استون
5. دیوید سولومون، مدیرعامل گلدمن ساکس
6. جین فریزر، مدیرعامل سیتی‌گروپ
7. کلی اورتبرگ، مدیرعامل بوئینگ
8. مایکل میباخ، مدیرعامل مسترکارت
9. رایان مک‌ایرنری، مدیرعامل ویزا
10. لری کالپ، مدیرعامل جنرال الکتریک
11. سانجای مهروترا، مدیرعامل میکرون
12. کریستیانو آمن، مدیرعامل کوالکام
13. برایان سایکز، مدیرعامل کارگیل
14. دینا پاول مک‌کورمیک، مدیر اجرایی متا
15. جیکوب تیسن، مدیرعامل ایلومینا
16. جیم اندرسون، مدیرعامل کوهرنت</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4962" target="_blank">📅 10:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=MODewtDGsEFZYPXmyfZu-o1TdcphLlt4ORL0it1Mc-MJCHg--Khgy7zD_CJM2V8XWtfAodh4b0tWTfDe134QPpUj5L87aBmTSkUVyvzkbthNu0s3OMBXR3SxlgJ4M8bsYsMHj3rT2DrDnCPiH8B1oZiPGuypM46IoimbseACfZDhMSp2G2T7n9_QslMssyrZrbWJkAbmFelsqvZ-585JeQpYN3XOlAyB8w7dNa6RL0YyHHg_i-hN1OHH5OGTNYgzH-SIlzQ_adyHKo1GYv0m3DhjviUDXVE6M1TOO5iqEA_4O6VjPT3gkP9JkQrDy-KE-U4hCwpA7QQBzqIDxgH4xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=MODewtDGsEFZYPXmyfZu-o1TdcphLlt4ORL0it1Mc-MJCHg--Khgy7zD_CJM2V8XWtfAodh4b0tWTfDe134QPpUj5L87aBmTSkUVyvzkbthNu0s3OMBXR3SxlgJ4M8bsYsMHj3rT2DrDnCPiH8B1oZiPGuypM46IoimbseACfZDhMSp2G2T7n9_QslMssyrZrbWJkAbmFelsqvZ-585JeQpYN3XOlAyB8w7dNa6RL0YyHHg_i-hN1OHH5OGTNYgzH-SIlzQ_adyHKo1GYv0m3DhjviUDXVE6M1TOO5iqEA_4O6VjPT3gkP9JkQrDy-KE-U4hCwpA7QQBzqIDxgH4xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور چین در دیدار با ترامپ :
چین و آمریکا از همکاری سود می‌بینند و از تقابل زیان.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4961" target="_blank">📅 10:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtaDvwWzLD6AZPYg_UlgN7uKyDJZybyYlxIyDJjRsC4knXJqiA9YBqy6V4pB7kG05L-xw3GWEWGQqYzJadrBaWHfIKdWPnjwF2A7sf8eWkcH7tFBCxj_oaJ7GuINCKc7csIgg0UZ5AiVAIPDz1KT79S9Hbc5oBtT4nqCXQw6mtw37TpM9mVTAE9mMKFqutNnfBi6AmOhoO-YG48EHAz4gC7qsKjQ2sNjXe5HGYu5kFnNdBYeUJTpXEnt5yFmIoqopv-Q8UsDhDKOevy4M9d7RnTAJnflHnDIB_WreGbbR4shVsz7S3aJ3fWbfo0_fNjoEnKXu7xFRwJq4DFF-Ug-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات در حال ایجاد فنس‌های محافظتی برای دفع حملات پهپادی است.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4960" target="_blank">📅 21:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">جمهوری اسلامی : ۴ مامور دستگیر شده در کویت در چهارچوب ماموریت گشت‌زنی دریایی بودند که به خاطر اختلال در سامانه ناوبری وارد آب‌های کویت شدند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4959" target="_blank">📅 20:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
ناکامی «هفت باره» دمکرات‌های سنای آمریکا در طرح محدود کردن اختیارات جنگی ترامپ در جنگ علیه جمهوری اسلامی.
دمکرات‌های سنای آمریکا هفت بار طرح محدود کردن اختیارات رئیس جمهور در  جنگ علیه ایران را به رای گذاشتند و هر ۷ بار شکست خوردند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4958" target="_blank">📅 20:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
در یک اقدام بی‌سابقه دولت لبنان با طرح شکایتی در سازمان ملل، جمهوری اسلامی را مقصر تحمیل جنگ‌های ویرانگر به لبنان معرفی کرد.
لبنان در این نامه نهادهای جمهوری اسلامی، از جمله سپاه پاسداران را مسئول درگیر شدن این کشور در جنگ، برخلاف خواست دولت معرفی کرد.
‏این شکایت می‌گوید که این درگیری منجر به کشته و زخمی شدن هزاران شهروند لبنانی، آوارگی بیش از یک میلیون نفر، ویرانی گسترده در روستاها و شهرها، و اشغال بخش‌هایی از خاک لبنان توسط اسرائیل شده است.
لبنان در این نامه گفته با اینکه سفیر جمهوری اسلامی را اخراج کرده، اما او خاک لبنان را ترک نمی‌کند!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/4957" target="_blank">📅 20:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4956">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrExWp1OTlNubQtj8-ZMQ5irp9NUAPIHsDeqEfBHUogpwfZSY8XTx_rWRKF-J3_DHa5E9zw5euraQHWo2P7YjL4P4bgFAUJk5GDF3uvrtKVw5vuj9BV-xLKnaMGJFc2G5EnNfKXxzndmUCzkibfMADKTkknYRzfpwLmrZQAyKBBMHJHAF9ZGx-aGu9kPBZnrJoGkvG3toBe49qJSpzghLIxr9SaJ2l3ag8Cukvw69YZ7eNsNe93OEtVU3_LHWYj_sQo5ekL65NuNwGs_olYF3_OXpivzbe1p-Udo9lqa3cvYd1xQtthyzQvtDrJ6IpoSaZuV6M5-YBY6ISifVfz5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی از رسانه‌های فرانسوی دست به انتشار گزارشی به نقل از «فلورین تاردیف» خبرنگار «پاری‌مچ» زده‌اند که حکایت از روابط پنهانی امانوئل ماکرون و گلشیفته فراهانی دارد.
این خبرنگار فرانسوی در گزارش خود نوشته که سیلی که زن ماکرون به او در کنار در خروجی هواپیما زد، به خاطر همین رابطه بوده.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/4956" target="_blank">📅 14:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4955">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تداوم انتشار اخبار مشارکت نظامی امارات و عربستان در جنگ ۴۰ روزه توسط رسانه‌های غربی :
وال استریت ژورنال : رئیس موساد در طی جنگ ۴۰ روزه حداقل دو بار از امارات دیدار کرد.
‏گاردین: ‏اختلافات داخلی میان کشورهای حاشیهٔ خلیج فارس، به‌ویژه بین عربستان سعودی و امارات، در محافل خصوصی معطوف به این مسئله بوده است که آیا خشم کشورهای عربی از حملات ایران باید تا حد تلافی‌های نظامی ادامه یابد، یا این اقدام ممکن است سطحی گسترده از تنش غیرقابل کنترل را ایجاد کند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4955" target="_blank">📅 14:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4954">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
‏«کنگره ملی کردستان»، نهاد فراگیر تشکل‌های کُرد، با انتشار بیانیه‌ای صحبت‌های دونالد ترامپ درباره ارائه سلاح به گروه‌های کُرد برای مقابله با جمهوری اسلامی را رد کرد و هشدار داد چنین اظهاراتی خطر ایجاد یک کارزار خصمانه هماهنگ علیه مردم کُرد را به همراه دارد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4954" target="_blank">📅 14:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4953">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UF37mglg_khR7YlZ2aO1h3dUgtQUfshVkoG6qX2u1XcDN7UWSzksf6QZ1uTEVaCYSGDd2vq90P5oeae3ieumCPZF0L_KzCdDnuTzDX2a_w7B96mwYhp2wTRcaQrIDXejqslEwGnSQtyLY9-xHIt9ItkPUZf8a9Ul-eEnaOVx_dgH_iAAjv_jHio5PF1AfY2tGEbNES1tPYVEnjn4SA5KeU9DfAfMATRfXkmjeqH_CsQV-J8JnW7dXnDYe3VKn0Kpb0h_ZKOaGsls7URNiiiNY9KOCTfgL4Wj5yJjzkVEIKejov0JOt0TK-hjCWn9saGM6OjPuGw8GEOfaxqahM1ABw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دولت و حکومت نیستن
مشتی راهزن و گروگانگیرن</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4953" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdi7ul2XIr7EkH8yDOFzIqYuYiNtfGvinxq_WFv2HN-8P_2_7Y0IkttYvqZG8Az9dn7dWje6vv7ZLhFS35DSlcgt-7-7jsJmIUVBFR5ZU5RLea7hI2jAczkBjEkrn2ydAI5M8c0kiwgr-W68q6kbrMS9lPBWs6kUfxDDNKd7VpTOjWUylgQNDe1Yq9Hpy2WC5ekviE6yejqwJF2l616OhMkMWgKcg5SDfyhKpfErcgOmmv8yifoYJbI1GPu3ZsZgK3RAyBWo1fUpPnClMZA_WtLgQlx_xPt_XYMXsxRr9o1JF_dvcFSdbKfvmgAHxZhaaySm_4BgB9DOBCv5cg2Rxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا به خاطر حضور اسرائیل مسابقات «یوروویژن» رو بایکوت کرد و دیشب غایب بزرگ بود.
نماینده اسرائیل اما با اجرای یک ترانه عبری - فرانسوی - انگلیسی
به مرحله نیمه‌ نهایی رفت.
در اسپانیا فقط ۴۰٪ از جوانان حامی
این بایکوت بودند. (در ایتالیا ۳۳٪)
یعنی از هر ۱۰ جوان اسپانیایی
فقط  ۴ نفر حامی بایکوت بودند!
نماینده ایتالیا هم از ناپل بود و یک ترانه
با حال و هوای جنوب ایتالیا اجرا کرد.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4952" target="_blank">📅 10:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFsY0hbrzfV5ZvGvsoliol0c-lnUgnhmwv6ynW7KRkALvJVuL4N_mZebZcRIkK12fOrQWSPqGHxRcg5jEhclL64R7BbA0XfT9Zp7Rif6CpLF0a6bLXhayF5NQrgELAni7zYLca-sjqybcnDYCaYL7np74r2oGef95wXpUNCWnudD6bCRH4bQsWmO11IB_vR8FUwvSF6IqGq1Z16AqxK-HmWRY4R0gBLm5H3hZHCtgUHEH6I-k0Vwvbsa-hKvMZEB1REjPbQPm0yMjG-48SrnNBtWVQ3yaB8e5OjGwgjqm9eK53vtTphM3ssK2UV4LALuGIXYo98szUzC4XJhzCIJ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏نهادهای اطلاعاتی آمریکا:
‏جمهوری اسلامی دسترسی خود به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز را احیا کرده.
این سایت‌ها در زمان جنگ ۴۰ روزه با حمله به وردی آنها مسدود شده بودند.
همچنین ۷۰ درصد از لانچرهای متحرک خود را همچنان حفظ کرده.
‏و مجددا به ۹۰ درصد از انبار و سکوی پرتاب زیرزمینی دسترسی پیدا کرده.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4951" target="_blank">📅 10:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rERzm92Rw-0-1RuQFSzW3BkDOUjgxEtc2kDtojwilzz_Q2fAspLp1uOkQyw4Qgdb1bQDk3BumfvL6p8R5tRwcZ3s-2NbaRXSt-JCWF3vIZ5lWLD7xhTXQL_tb3TAAwdtbv5bkWZJKrj8nZM0Q9i80o01PBgNa1uKaP8xgmFHlKx8QeuLzY2KwYcsdH3KB-QyJi5YrwZdtuhjwfBnBVhwu2CSFBH61sZ7-bvK3tpy528Z9TlyXB0Cblrpbo5ooYRQkwSIGvxye8S5YS8LlHJHSgcKFJPWR3ta-a9sIxvNWOcnsdz7t09QcvzZCTLHEKYF7ew6f5-9buD7wHAYOe4IqG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rERzm92Rw-0-1RuQFSzW3BkDOUjgxEtc2kDtojwilzz_Q2fAspLp1uOkQyw4Qgdb1bQDk3BumfvL6p8R5tRwcZ3s-2NbaRXSt-JCWF3vIZ5lWLD7xhTXQL_tb3TAAwdtbv5bkWZJKrj8nZM0Q9i80o01PBgNa1uKaP8xgmFHlKx8QeuLzY2KwYcsdH3KB-QyJi5YrwZdtuhjwfBnBVhwu2CSFBH61sZ7-bvK3tpy528Z9TlyXB0Cblrpbo5ooYRQkwSIGvxye8S5YS8LlHJHSgcKFJPWR3ta-a9sIxvNWOcnsdz7t09QcvzZCTLHEKYF7ew6f5-9buD7wHAYOe4IqG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شاهزاده رضا پهلوی  از سیاست‌های ترامپ، «از یک طرف می‌گوید مردم باید قیام کنند و در عین حال می‌گوید صبر کنید، ما در حال مذاکره هستیم. این همه را گیج می‌کند.
شما نمی‌توانید سیگنال‌های متناقض
ارسال کنید.»</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4950" target="_blank">📅 10:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=ccf3usB4plVdsOdTxf1EmSXmzaqxM8s79lhV2aNVLpqVygNS6v2FMbp5DA3EjY690ez1SbJhjEUluzOllUUefEqWfte9OYJp3jp799dXm6rq1SRtNfl3a6Y3Pu0xAoOzMAGVwrpPof88hgK05KDqM-Hrb3X5lZR5lNZJuUsJ_uMm_IgTTqlxbcSX86Xmd2yiT7Nc9QFvJtK7yjQpCqTJ_zkDSMkrpMknWvStJltG2-6RwjEHQCuX_iE6i5wyvrbDMGcM6CCTh8m5bOKfqO0eTaei_-Aug0sOVJtYFQXjlw7CKP8pckJ6VpZaf_tfyBRRLs_DdMPWoveTT_Duc-EBHF42gnhsjfkkJ4OPC1VrrzMi75TNBJ--f9WSAUo5OmLBE46zBZsM54Wrr39LKiV6b1UgoS_K1VPwf2_EzuMqMqCNoYtstwSCI_RHqtGKYMWXItzHEppWUeKEFWRn8maq0AhZf7X6piuwayYaTtRQAmCCXW8MCX1FMSlKA2rm6CZp6zWBNuxjpU4EhztduE3kJyS3MOrMxZY5AVmUMLlvyCBzSG09NqNMgMQZ_WVwg3I1sOolFIM6N8HQAOuQKziY3dYjx_YRpcaJS9tzwvIE7VDVBU3viLFmjG7gB5_hzpFutj8ByMAGTaMx1RmEKLCi-aHW5EXcmwEGPJdhid9Ru5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=ccf3usB4plVdsOdTxf1EmSXmzaqxM8s79lhV2aNVLpqVygNS6v2FMbp5DA3EjY690ez1SbJhjEUluzOllUUefEqWfte9OYJp3jp799dXm6rq1SRtNfl3a6Y3Pu0xAoOzMAGVwrpPof88hgK05KDqM-Hrb3X5lZR5lNZJuUsJ_uMm_IgTTqlxbcSX86Xmd2yiT7Nc9QFvJtK7yjQpCqTJ_zkDSMkrpMknWvStJltG2-6RwjEHQCuX_iE6i5wyvrbDMGcM6CCTh8m5bOKfqO0eTaei_-Aug0sOVJtYFQXjlw7CKP8pckJ6VpZaf_tfyBRRLs_DdMPWoveTT_Duc-EBHF42gnhsjfkkJ4OPC1VrrzMi75TNBJ--f9WSAUo5OmLBE46zBZsM54Wrr39LKiV6b1UgoS_K1VPwf2_EzuMqMqCNoYtstwSCI_RHqtGKYMWXItzHEppWUeKEFWRn8maq0AhZf7X6piuwayYaTtRQAmCCXW8MCX1FMSlKA2rm6CZp6zWBNuxjpU4EhztduE3kJyS3MOrMxZY5AVmUMLlvyCBzSG09NqNMgMQZ_WVwg3I1sOolFIM6N8HQAOuQKziY3dYjx_YRpcaJS9tzwvIE7VDVBU3viLFmjG7gB5_hzpFutj8ByMAGTaMx1RmEKLCi-aHW5EXcmwEGPJdhid9Ru5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد یه عده زمان جنگ با آب و تاب می‌نوشتن که تیم جمهوری اسلامی همگی «دکتر» هستند! دکتر قالیباف،! دکتر رضایی!
دکتر لاریجانی!
مثلا دکتر لاریجانی چند سال بعد از اینکه
«سرتیپ پاسدار» شد و رئیس سازمان
صدا و سیما بود و صد تا شغل دیگه داشت، تحت نظر «غلامعلی حدادعادل»
مدرک فلسفه گرفت!
اون محسن رضایی و قالیباف
و بقیه شون که هیچ!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/4949" target="_blank">📅 10:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.  هرچند…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/4948" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnuSvWxoquVW_EtuRoDMNjihZvNkFfznbpwpABAnK4wgF5BMijQmr1tvpCoRZjP2wcvhmYZ8F9ZYzqPUamk7s-lPJlTuIcf715HdGovQ1Ij3WvG14eCjqV33xVkKxEaXbJQlWLkmYiOL3IS9ZX80GYZhEWDhX6RWFgzcSfZwI2wn5kO6BOYBqu6w1KTwrtCsU4D6UHij9wijAb04-A1bfiwnZsz_OKXcDly4Nvfm2LlJpaQ0KSI2ulL_X6Ld5dCR8iB5ehh7s_ydiuaOYsDPUqMMfTaxZrrDswSEpTSjLOj5Twe_t07Z9PEzwFpgrL0A0uNCZQ43x8-Y3trWKLmjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.
هرچند این نشان معمولاً بخشی از پروتکل دیپلماتیک واتیکان محسوب می‌شود و معمولاً پس از چند سال خدمت به سفیران مستقر در واتیکان اعطا می‌شود، اما فضای ژئوپلیتیک کنونی و اظهارات اخیر پاپ درباره تنش‌ها با ایران، باعث شده این اقدام به موضوعی بحث‌برانگیز تبدیل شود.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/4947" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VE7B4GFylz-WpIJ1s1_9wrsi2-CyNJZ5YOll470VSFj-utY2kIg59geytPuUfJne9aENCy8GJzQ9o2jrYFebJcBT320VkoA-TWUUegyaGmPYoF1oAUZ4-ZWsI9xyoAhvODF4x6PTamZji3IV01jcMB_SII7vhM7m_WSOpcwVXotXs0SRs_wD9K1APeP0FoCjE3RcG_-F-GKHaOexo7PiZNCQTvRGCtvlnTDRTk3aNeVHfXqVejiywaAqT0V8VuB6wg7EVPEYS7vKB9EUgtw-9DnOaNVl4obzeCrH6jIVujWjhusz0PvnEFhTUMYXM9TBbvXQiHXSLy2MuM0cJ-Kbig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش و ‌پرورش وقت، در گفتگو با خبرنگاران در پاسخ به سؤالی مبنی بر تقاضای برخی نمایندگان مجلس به استعفای وزیر و برکناری مدیر کل آموزش و پرورش استان آذربایجان غربی گفت: «شما چی؟ شما را برکنار کنیم یا نه اگر به موقع خبر می‌دادید مواظب مدرسه شین آباد پیرانشهر باشید این اتفاق روی نمی‌داد.»</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/4946" target="_blank">📅 09:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJsWpG7F4ircInztvVm8hPZaY1a1VdwEI_PYpl2Ho38zpR4bzGeNHjdp4IYsDUB1REZmS28_AZey-Z0qDI3TRk0Hiy0V1S2MXbOmDRqbPylaI3YM6-ke9hlj7CyeR_yfLvFUxvkq8daKMqXogf2hDcf3Cp2b34_pQ6Kz3d1DP7cM5QN1Q6A0MNN-r77nHKhdvsBV1P2HwFopj5Tssa6Hs9_vQbh2a6lK9P4aUGVmqY0HChWgU86MHXYQbsOHUpQe-xhjO1cOCZVfdT9Ds1NW36mPairxc_S8PRCWX9gNkIAV15QaWY-Dv9RYVrV3PzcX82iLELUeYg571YpaH-1w4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4945" target="_blank">📅 09:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4944">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZeDM7dtQmAnfTgw1wpIqp7dkYLUMbXWjLnLiAaJbbjbdGKBSv-50OXb3RipnpGNSHoIW5iyycaaTgZkJjmZYb1DeXCFWzJWsL91ttKxQeqxL0omVDJAAdKtaQA7ME3WBAFG24WKsNCJsaOrPqaywLxpAritQyZi0_VoHs_G2pGXIdLcA_lM0uwDJrMA53EHpJRWRS_MTKnRR7KKhav1IeBAT-c03GP68-sBRJPwIJUyfsDbVFT_0nfWjvj7IM-iUCtJDRWHaTteKM-xaEYrSfuULxCAOPm-8CxUNCe6h37WqfQjK2fF7Ln7Dx-IQx2TVC_Z6n9fEQYlWzoJF6qGkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحی دیگر ….. اعدامی دیگر
بر اساس گزارش توانا
احسان افرشته
، متولد ۱۳۷۳، دانش‌آموخته مهندسی عمران در مقطع کارشناسی ارشد اما نخبه شبکه و IT، اصالتا اصفهانی و بزرگ‌شده تهران، او در ترکیه بود، نیروهای امنیتی پدرش را فریب می‌دهند که احسان را تشویق کند تا به ایران بازگردد
و می‌گویند خطری او را تهدید نمی‌کند.
احسان برمی‌گردد و حکم اعدام می‌گیرد.
پدرش چند وقت پیش و بعد از صدور حکم اعدام پسرش - توسط قاضی صلواتی - سکته می‌کند و جانش را از دست می‌دهد. امروز هم خود احسان را اعدام کردند.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4944" target="_blank">📅 08:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJI0fzk5f1DzMH9ou9hsHHFzL5CzkSBfaZyLoVl9G15Aimlm56WYLalm-eWydzIBl0GtVddlTZPR4OTMNzt4e0CSRWSynF50ISGUN39JCFHg07MAD8FdI05JDaDMIzFkGneeK0V6TMbYrPyStt9kBrHjt83MEG0YDshh_ZZ0Qjs1gTlnY95Rp-k5vgFIeW3kCrERXPFMFuHxH0vit0ZOcH7wF5EP4_04t8aCvwIO7Nms1nUP4Pc-GuNttt6DxB8FEI_zvbzE9d52isI_UTiF0jSCUm4qSnrTW8SbiLb-BPdjA_RnmzqwgAUODqNf724hOxPDvrpgwTaQCjimCJ490A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4943" target="_blank">📅 00:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4942" target="_blank">📅 23:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
پنتاگون در حال تغییر نام عملیات حمله به ایران از «خشم حماسی» به «عملیات پتک» است.
پنتاگون میخواهد به این شیوه از اختیار قانونی رئیس جمهور برای دست زدن به یک «عملیات نظامی ۶۰ روزه» بدون نیاز به مجوز کنگره استفاده کند و با تغییر نام عملیات، دست خود را برای دور تازه درگیری نظامی باز کند، بدون محاسبه روزهای عملیات قبلی.
بر اساس قوانین آمریکا رئیس جمهور می‌تواند فرمان به «عملیات نظامی» دهد و این عملیات می‌تواند تا ۶۰ روز ادامه پیدا کند.
صدور «فرمان جنگ» اما بر عهده کنگره آمریکاست.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4941" target="_blank">📅 23:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4940">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDdQRnHRaA1jkObb4_f3MHFQwWkdHO3Q2Hm4SJLUgcNOBnaAzwmdrFxhRw5ZjZhdJMjDbn371YkiEoNsmiGwZ7QhYIwsvJwXxjkxv8jEyvdm-8WxijayLR4cR4a2URPbypv-_afZQcWBAA0n4K7f6M5aHc-v9YoZG7gCjiJpGMU0e4uUC2AyD0Dw3eWbJ_pGhCsq4ieuaX-dR_MrRHnFy1wysXy26wmMO2quSAZItr03gMEI7qBJzi0rQLhTftzE3NmlnL-ogYFQX9kC1axz6LiILD-EaOyv-JD3uWHvGDEPi2pNxdxzeMz7qVjAO_TDK2jS0pnJWvKv9A80xDNK4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای  رسماً جمهوری اسلامی  را متهم کرده که گروهی  از نیروهای ۳ پ  را با قایق ماهیگری  برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری  یک نظامی  کویتی زخمی شده است.  کویت که امروز سفیر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4940" target="_blank">📅 23:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ7c_DKtihdle2v-JXwIWySROVNKL70Ejjz8tAvJd_GEeEWutixn0oaVNuCPtVpcCMFANxdDliV_uZ-wFboNqHsx_mHHddC_QZdEhqWWgXoR7A56PKouc-erX4JWkOnkI39Gt1daQObSd5o4aErk7d6-rYl7wQ749FB8y9KKjAQE5RoZVGJESF-y4HP-aBQUWx1kqnmT2BtnvMFU6lxkjoczgxLNs79zosR1HkNDQnEl9YjASmPrLIHaTRdR9kUrNNKkUCRclaO8HIN9eBG3ywMgqHTlCR5mVDrY8uPHvpnxGPg-0CFgP0o9ZnEfJZZTXjVMa9Sj7pmqD4ma3Gr9Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان اما در میانه جنگ دست به حمله به ایران زده، در واکنش به حملات مستمر جمهوری اسلامی به عربستان،  نکته جالب اینه که رویترز میگه عربستان حمله کرده بعد به جمهوری اسلامی گفته حمله کرده و هشدار داده اگه به عربستان باز حمله کنه عربستان بازهم به ایران حمله خواهد…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/4939" target="_blank">📅 23:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6o449L7kge_sgKm5ltDsn_K2sFvpdfKIaDJCEq9fmAMvAOlZ8I7j8ZSQYA0M8LXwcrjArclr9KxBGwXke8R4dalxxjGx4uG6VcQGSxDnnmGpVLMaA5bOcxylHN4lifnz3127SEe1h9kthgiaA8RN7vZBfUiRFxCus-2dK3pxwVxH7FKY3kODDW6_hsaSjFkomysvTHnJVbSxPPz8_ormVl4Bl7WXP0Vl7rpaP5IjF8x65MPG8hYnhAexNa3NZOAc5-1oyUlghiax6i1xDsCsYHKz_SEyzaqdnAD4TO0uyOvKWgbsHxczanhfFX0h2ispg1W9xTa7gEg_QRZWopZcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی  به ایران داشتند،  امارات بعد از شروع آتش‌بس دو بار  حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.   امارات در صدر حملات جمهوری اسلامی بود حتی بیشتر از…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/4938" target="_blank">📅 23:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O752COy2tdGkmrQPpXUeGnppvHhFj1xbrDRaQ0ig8KWN3u86vTDy4o9iS-0buvtAH5BWH02tb91O6g6k2vEOq6aLlFIg4RBwRbgzTK6IHXADidhhPvmngaky0W2hb3D0IskpiCE9iSefIjEirEZ2pJRMzvtMt-f2q_wt_5WFBuMjbVGQJzECBjXoLzoWfhp7iUzQZLQvDSriZpzazPmI3lMsa9KIkYf-FZBrCtk03s57q5ZypbOKgAtphk1PE1mZ5UYzrLCt3pPRv7UBzsPhvJ4KM0ksm78Rnx1Yf7nKwP27x2nHoSfL6LQSvCwk9AnTmeNnlpSIaRrRgPQ0tBRIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی
به ایران داشتند،
امارات بعد از شروع آتش‌بس دو بار
حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.
امارات در صدر حملات جمهوری اسلامی بود
حتی بیشتر از آنکه اسرائیل مورد حمله قرار بگیرد، امارات مورد هدف قرار گرفته بود.
امارات پاسخ خود را بعد از شروع آتش‌بس
بین جمهوری اسلامی و آمریکا داده بود.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/4937" target="_blank">📅 23:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=uBMZwzLfy6PMY1x-laGIUenhB77fs8CREPB5h3cQDwr82xVI7h7LBYfrXhtlD1CgMQ76FapczbfnCE4SRKDNJo9MIOF5ocoFU21zRCegg7ujvUU3G00B2utpJAy7a8FS-ifdR_4wZAHjJRZK4yk8Y0TneSmC06HaO4bOTIXpHy0CVAnSP6TtZx8fwC0slxyUs-RggeVDC8drvbEABGbl-DCp4WzIT7OMf6gs9qGtxCfwI2XSi5npRZAKPO5vxxIk4gt5Xm1VIHb6K974M0Skb4OT3ndUOMJy_85AGjEDi2fv3jielBaxdf_auI3f5UHM76DTa0OXWvLUpwBf5BhS4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=uBMZwzLfy6PMY1x-laGIUenhB77fs8CREPB5h3cQDwr82xVI7h7LBYfrXhtlD1CgMQ76FapczbfnCE4SRKDNJo9MIOF5ocoFU21zRCegg7ujvUU3G00B2utpJAy7a8FS-ifdR_4wZAHjJRZK4yk8Y0TneSmC06HaO4bOTIXpHy0CVAnSP6TtZx8fwC0slxyUs-RggeVDC8drvbEABGbl-DCp4WzIT7OMf6gs9qGtxCfwI2XSi5npRZAKPO5vxxIk4gt5Xm1VIHb6K974M0Skb4OT3ndUOMJy_85AGjEDi2fv3jielBaxdf_auI3f5UHM76DTa0OXWvLUpwBf5BhS4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ راهی چین شد.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4936" target="_blank">📅 22:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u-W8Kuo1rGjQ0hUghfQKwuoPqnpzFkktgEcNgPH3OcjLZyKAqOtiE1cK5rpxXWX25tJErNDQOR28uNhn-q65LieAnTVw5s8pkt_j178LAyklkKPHv1ffjAMh-QsJUfkgc1bulYGH8eQBFtu6sg69ig33OZ4S-koQ9t-fLX7DykqjejzGJuCh09Zq9pcR40ksSVtlTtUJXfwIPkL4rzy7NVEUDUs3WU2xofkHsv9nD4L-m_hXVObAyQOc3x671oV74_t629I5jpY-jpYehb4n-KkwjQBZ4QLln7sYJwWoZf7oLVTs6M8WeYiQEghmThahkNsd8kK9KBnrtK-dwaG37g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKMSZkdJxGVKKidDo7dQXgNq9EZRYfqJwiW7IilLuuGdL4z9e_mI5iZx52Lb6-uqq6JkNxVWtywpe9oWha_CTY_2onL9ZPyPOyQIAxvoMgb8W65mfYUe-1tK7NxL4DPBlhEUNBQ3YWnlBP8WriTCCZpFzbauXFgcNR289g7Jp0NH-xRxFbdU44lq8KYpJiXF2hnUtQ4XlJQfHGOCF-tCviA4kiBhKdLX9scJ7_Z6_UfjK80oEGcJjuSab2GHk3eGiAG281xSvac8oVrmGvsAyhS4ymPdOm0QV0w6K7ScWKpC6PXHN_uo8_iTU5cGuTR0NoP1l3diZ_qaMuINmOjoww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fs9ah3uFRvV4SlkuwMhO9uPTHM3tu-bx0EjeN-kPjIINj0Cxzen04xKBb2BlED7hOXDwJ5tdgAOu1eiwvOFXIYR_XVc_XyXWVM5z8Nl9nRiDIvgL7ykq4xkKI-Hy3asiNgFdHpzfOhD25guETVibo0GgDDuBc_OKm9_myrEGEPvWxf3bz4XRSuBoTPqfZPeegXqtmZ19OVuwGU5Nb6j4mEWsN41zxXXkRSjMBWFm3G3PsU2jNPrRwukhqkusVMutThF6u4yPzbc7t2RGvttb_isnEwnFdFiB-YlxU3B8PBb38KwSKEeBtr2tEgx6nzfbmz8hLDfgfYYohbG_PcnhIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۵۹ دانشجو امروز از غزه وارد ایتالیا شدند.
ایتالیا در مجموع به  ۲۲۹ دانشجوی اهل غزه بورسیه تحصیلی و تسهیلات اقامتی داده که امروز اولین گروه آنها با یک‌ پرواز وارد رم شدند.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4933" target="_blank">📅 22:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyu3QmBauAghYwa4uMRhzlhoElOv2rNJDyhf_dpTX0cALDvOawWuL8i4jCmF2LDOI37ZxoL9BK0Y5nmcPdZU6VpaGbw3-VqmySzn7Ct5wkkasIANsC9dp5ytLggOP8fmAyVw2CrQudI4SS9WkLZdCuG1g6SVxTTYIZJBwQfyPp89lp0u5UYkLnAv-om8unTL4kLJAhGVIZkWzK2G7yocGDFJeW-yIj3XhdUwVQKxfF0FhKJlw1WOi2fjHSZvw6xat_jrcJwKeBhfUZ4_ZuDTt3u6_NdZpwXjt2WMwXB-o7A2_qMDcmnpAb3fVY9DIWMUjxY70ubfYoD_FfugSL13mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بر اساس گزارش رویترز عربستان در طول جنگ، مجموعه‌ای از حملات تلافی‌جویانه و بدون اطلاع‌رسانی قبلی را علیه ایران انجام داده است.
🚨
🚨
آمار رویترز نشان می‌دهد که پس از واکنش عربستان و حملات عربستان به ایران، حملات جمهوری اسلامی به عربستان کاهش یافت.
🔺
عربستان سعودی به ایران در مورد انتقام بیشتر هشدار داده بود اما کانال‌های دیپلماتیک حفظ شدند.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4931" target="_blank">📅 21:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
ترامپ در آستانه سفر به چین: نیازی به کمک چین در خصوص ایران نداریم.
🔺
یا ایران مسیر درست را انتخاب می‌کند یا ما کار را به پایان خواهیم رساند.
🔺
‏من به یک چیز فکر می‌کنم: ما نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد.
🔺
با فوران نفت در بازارهای جهانی مواجه خواهیم شد.
🔺
همه زندانیان سیاسی ونزوئلا را آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4930" target="_blank">📅 21:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UUIf0zbav_tBurJhAKjeKWQWBZtCvkQAA-FqGUdwc2XpiGyHVdVmmiWBjJbXJ8RGs2ukD7NaItGB8Nh4lpQuzYtrN9MSNBuuCL-TlvvZZE82Q8xGEKXx4RW-sPJ0c1htyJM-364cae2L8YoaO2XkaGLzujncTGX8wSfkT3sQiIP_SnJLaZ2UpmSvgc29ltrtWFqJi7ZmLjHSQgLY0WyzABIqnyHNU_5swfg0Bj6uY2vzxP7uwzwsP6IQcub9EWPkpf-SQkaJEQZadGQci9bkyR9abGn_24Eqs5SEmiwN8Br0X2BqQtw1cAZTOzPq9u6Hzsgd0ZldgpHvfOajCqubDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IOM6KjYYSZ6Hh8iRq3R_IXNdtl2LAYW6Ge_feOU2BGvKRVHq5erPj3aTJdLrH5ytJWzouIfT4L-LxqGNT8yhfT5F9KNCLgKtV9eB2UGhYqMZFwkIvUW1t8fcu9Wg21v0Lat0NGq2AyNgLy-mejM2Pl-jGiM7xzRZyJrHW7tbHrHqs_NhUHUcoHnwURnI_zO_o9suojzTS8yT4SXYY19WuwakOfarCZrPWzhxc-Nv_fazsmCfwbYNshuTTd1wXGFI6YoBg344JdCWPChbL_IPUXzwXT_FcZ3Iy_m2GBaRJ303g_zBs23hX-x4vLL13ecaxqIGKt1MvHG1YtYWdRzUAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای
رسماً جمهوری اسلامی  را متهم کرده که گروهی
از نیروهای ۳ پ  را با قایق ماهیگری
برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری
یک نظامی  کویتی زخمی شده است.
کویت که امروز سفیر جمهوری اسلامی
را نیز احظار کرده گفته که ۴ تن از عناصر وابسته به ۳ پ را دستگیر کرده.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4928" target="_blank">📅 20:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اینهایی که آرزوی مرگ یک نوزاد ۳ ماهه کردن، عمدتا عزاداران کشتن کودکان معصوم میناب هستند.
همه چیز این جماعت دروغ و خدعه است!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4927" target="_blank">📅 13:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4926">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSY-QM1F1zVq1zoevj0bh8QHfOeHoVt51diEZ2EEdAGrjrlRIcvrB8ZNBwxuRopoT-KyhxXvOkOBK2cI7XnqXE8AcHxGBc2X7rjxf5kUkoBsGgCMuhXfUBfT96BJ0xLLCtDIHF9cdqTzLH3pUgzV1LmXgDjfnbXAevPSjkhjH-9piuy5ifGZu8RGPo3zO_SDG5AfmdkiMJJUF7ICbK03Z2yEy8Ek7mibGij4zZOlu0-IXmaiNA9Afhny6OGtU8xLr1l9DzmNjOGvaQ395fuAEE582b1LURDDr1wZdYRiMzE3J3YpjENmT2-VUF58UGV_z7KSIcIzU7ZrlKHKOY85mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرامکو (شرکت ملی نفت عربستان) :
در سه ماهه اول سال ۲۰۲۶ به رغم جنگ در خلیج فارس و بسته بودن تنگه هرمز، این شرکت افزایش ۲۵ درصدی درآمد داشت و ۳۲ میلیارد دلار سود به دست آورد.
بخشی از این افزایش شدید درآمد مربوط به افزایش قیمت نفت است.
عربستان از طریق دریای سرخ روزانه تا ۷ میلیون بشکه نفت صادرات دارد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4926" target="_blank">📅 12:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4925">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
خسارت قطعی اینترنت توسط حکومت جمهوری اسلامی : ۴ میلیارد دلار!
اینها زیرساخت نیست؟ سرمایه نیست؟ یا اخوند اگه نابود کنه ایرادی نداره؟</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4925" target="_blank">📅 11:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از منابع آگاه : پاکستان مواضع جمهوری اسلامی را «مثبت‌تر» از آنچه ایران بیان می‌کند، به آمریکا منتقل می‌کند!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4924" target="_blank">📅 11:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx2chhOxmBq4ORwosQVvfieXxuuU0zt2x-_HNZ9Axu6BsUoktsbov425E2mBm-E7F81vmEhdy8onGdcplKAMn3eu4hiHx03r-OhBq_H1IYHm3JOroAOhQVSCfYus-Fm456sQ2GokFvndU9n_F374ZrCVclQKFSkXmQ8G5pM39aKEBfMIthHQ3UFavMclOH-CSIXLKKVKC0u6ZSSPTPxdzJGqZS7ZA2I23lwt5WVLfy4VLNxBh6WRMND_YV6MXSd7Ktp1uf7h8QKK1U0pX5fkManvk9e2wWsUgnrXDTR2FLUOvS5iT4rJZajHKKbk1KWGQgvkM8ZFCcTJVHr46iOSUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=DtBkKr-JlDDigfs8GEFDCExPH8wT6F3DO-dO_ew176GY-8JRL0o4cOtMwJyT4hYJ5ARwYdGwMkRzNElK9Nw6NhsQ4DasLHpsBIpd6fMJLrd-kRUxIGSEGL9BHIWgJHUn7mK8UawJxXqEgiTA-qbJCBoY11d1ku2tZPSMdqMDbQEl7ZmffuML02PSuwjEaGszn6VbB-KR9oNKFlzx297MfeW1Tc3AAfb9Np5a7k6ee16QiVovIkgecy9RzH0Cfp0Ey0M1AlqTogqVfEAZLuOyhB0My5Q3Kpzu9Gp3lJkJmoHqAOxoKCASmDSLbd8qGd3DW5vFiR-iDcT9nlv50O961Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=DtBkKr-JlDDigfs8GEFDCExPH8wT6F3DO-dO_ew176GY-8JRL0o4cOtMwJyT4hYJ5ARwYdGwMkRzNElK9Nw6NhsQ4DasLHpsBIpd6fMJLrd-kRUxIGSEGL9BHIWgJHUn7mK8UawJxXqEgiTA-qbJCBoY11d1ku2tZPSMdqMDbQEl7ZmffuML02PSuwjEaGszn6VbB-KR9oNKFlzx297MfeW1Tc3AAfb9Np5a7k6ee16QiVovIkgecy9RzH0Cfp0Ey0M1AlqTogqVfEAZLuOyhB0My5Q3Kpzu9Gp3lJkJmoHqAOxoKCASmDSLbd8qGd3DW5vFiR-iDcT9nlv50O961Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلویزیون جمهوری اسلامی، اعترافاتی از «عرفان شکورزاده» دانشجوی نخبه، پخش کرد که بگه : القا می‌کنند که در ایران اگه درس بخونی آینده‌ نداری. که ما در ایران بدبختیم.»
بعد بردن اعدامش کردن! تا اثبات کنن درست گفته بود! ما اتفاقا بسیار بدبختیم که اگه نبودیم چنین حکومتی بالای سرمون نبود! در جامعه‌ای با درس خوندن میشه به جایی رسید که اینهمه اعدام نخبه و فرار نخبه و دادن سهمیه و پذیرش و… وجود نداره.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4922" target="_blank">📅 11:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeG8vBpfQV5FL1dRYFMHgI_3HzLrQMHdq9rN4hYFidx3dxntwGNjRMmZrc7MtCE_pZuH513gcO2kKC7c67dQvZdqbOxsgNVVz0g2HRy-UtSPhw4ndSn0qW63TvsQPrdHppQN9fhnU6q4b8zJJnG_l4qnns-Re_-kmfkW7J_OY7n7PFlgCcVZTVlsvRA-PkMu1jJ7ReviL4dQraaW10wrNUTFd2jmQvz2Lg--7wjQKB2h8yHvQlg0muF4QjqQgC-Pm7T68Fz3bMjB9dcUQ8Ke_h9fZNj65vUp2EJQkRH1Rq6SDpOSGlxykRMjEEXHoJQNslV8bILbyxip_5-54gXoOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی تهدید کرد که در صورت حمله مجدد آمریکا و اسرائیل سطح غنی‌سازی را به ۹۰٪ خواهد رساند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4921" target="_blank">📅 10:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkMCvhfpdCmXFu5C9nWKq_CThr_kjHX21jlDIs7qg7cAO33M0zy3_fZI1FS50cGgEQxgdHwT5YSDWlTenp4ATQovwe-07gbNaEWha8qoaVOTJwiFJAscueBD-Hp-bfWfuRFM4M5F7Zy2AUCml74-I-PMTvi5vZ7UEN5opCFMvOqXXcTdadNYSLOzL2-5ETlGcPeh-Mp92r_98Nhwg7Pr5ZlcA5HJ90AjKlPdFljnmZQlNZYjNc_Zh-da0nxyKtq8J40AGZZEIwFOhtK3ZLIMC6mdBhvi4yFo28T6vkdH2fKCWGq0MGl1cSiYH7oKaFmWLw5E0ktGGjb2oNvxS2ZnSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4920" target="_blank">📅 10:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال: افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند   ‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4919" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwdnBd8K0LRuE3VeKBOwDr-pEUH71apji5BZBqJRgrTIeeI6Fh--hPU4LLuWsNr4RvR-j8luBpAW9ze28G4E8D89TOawuGvdTe1aU4xmXNKBDT2E87eatg59bTkX97fN5z2i90u6FaYjZeXfmKWh8B78FENSJwlE0C2L7ojv_eGZZrsJmJ7xsmEZO0DIlgbxUKhh4Rc5CzYBLsg6yCIbWLCdkAh-FsiroKNmJXFj6naVScfpy_eL2dOUEva26FdXb8o04kqq7ltw8ch9UCiIGU4H2CfXVKsMXh4ldt_1ZVPH0J4mVwWR9wOSbWU3jFT-M81AhQq5_-0nNBYWCBsoYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند
‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه در جزیره لاوان ایران می‌شود.
‏پژوهشگران به تصاویری اشاره کرده‌اند که ادعا می‌شود جنگنده‌های میراژ فرانسوی و پهپادهای وینگ لانگ چینی (که هر دو توسط امارات استفاده می‌شوند) را در حال عملیات در ایران نشان می‌دهد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4918" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4917">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">در حال حاضر : جلسه ترامپ با مقامات ارشد نظامی و امنیتی آمریکا در کاخ سفید برای بررسی سناریوهای شروع دوباره جنگ با جمهوری اسلامی.
🔺
یک منبع آمریکایی به اکسویس : جنگ احتمالا قبل از شروع سفر ترامپ به چین (پنج‌شنبه این هفته) آغاز نخواهد شد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4917" target="_blank">📅 23:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4916">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏منبع ایرانی به الجزیره:
واشنگتن در پیشنهاد خود خواستار دریافت ذخایر اورانیوم با غنای بالا (۶۰ درصد) شده است
‏واشنگتن انتقال ذخایر اورانیوم با غنای بالا به روسیه را رد کرده و کشور ثالثی را برای انتقال آن پیشنهاد داده است
‏ایران انتقال ذخایر اورانیوم خارج از خاک خود را رد کرده و آماده است تا آن را با نظارت آژانس بین‌المللی انرژی اتمی رقیق کند
‏ایران آماده است تا ذخایر اورانیوم با غنای بالا را به سطح ۳.۷ درصد و ۲۰ درصد کاهش دهد
‏واشنگتن خواستار توقف غنی‌سازی اورانیوم به مدت بیست سال شده و ایران آن را رد کرده است
‏واشنگتن پیشنهاد پرداخت جریمه به ایران بابت خسارات جنگ را رد کرده است.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4916" target="_blank">📅 23:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dsm0DmDdXgMZQ0qpaCNmaon7cl_yPi1w3zYP_yTy4IT0wwUQ3axI_K78yPKMs0_jl1e31HCR1NGDxQlYCBfmJNVjWEZjBYWcigB8tQc-pOSKe38Teg5ELlelQ-DuSX_pASOro1rQh8FGM6TfxH6A-XIg0XfV-1RAz67GXZLY9A_Pfb6z0XgVIuQMDxna8omOsklFfdvHHLOqNFLJfT_yh4oLBbpT8WK6lM2ETIXpHXFCs9QcPmA2J2loIRgPeU-VuHoePsdYxHKTSlAGW-w6qEhtgQ-o-YLSFRNKLFtYDQI2MOX8os3yEYf1kWaCc0DCTFeHQiN29zLW47h1T_LubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏قالیباف : نیروهای مسلح ما آمادهٔ پاسخگویی درس‌آموز به هر تجاوزی هستند؛ استراتژی اشتباه و تصمیم‌های اشتباه، همیشه نتیجهٔ اشتباه خواهد داشت، همهٔ دنیا قبلاً این را فهمیده‌اند.
‏ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4915" target="_blank">📅 21:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏ترامپ می‌گوید قصد دارد در مورد فروش تسلیحات ایالات متحده به تایوان با شی جینپینگ، رئیس‌جمهور چین، گفتگو کند.
احتمالا ترامپ قصد داره غیر مستقیم به چین این پیام رو بده که دست از حمایت از ج‌ا بردار!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4914" target="_blank">📅 20:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
‏آکسیوس به نقل از یک مقام آمریکایی: ترامپ تمایل دارد برای وادار کردن ایران به امتیازدهی در مورد برنامه هسته‌ای خود، اقدام نظامی علیه این کشور انجام دهد.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4913" target="_blank">📅 20:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آتش‌بس به صورت باورنکردنی ضعیف شده، در ضعیف ترین شرایط است، بعد از خواندن آن ورقهٔ آشغالی که برایمان فرستادند که حتی خواندنش را تمام نکردم.  ‏باید بگویم آتش‌بس با دستگاه تنفس (وضعیت فوق‌العاده بحرانی) نفس می‌کشد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4912" target="_blank">📅 20:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4911" target="_blank">📅 19:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4910" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ به خبرنگاران: «اگر اتفاقات آن‌طور که باید پیش نرود، ممکن است دوباره به «پروژه آزادی» برگردیم. اما این بار «پروژه آزادی پلاس» خواهد بود. یعنی «پروژه آزادی» به‌علاوه چیزهای دیگر.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4909" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی: « آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4908" target="_blank">📅 18:36 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

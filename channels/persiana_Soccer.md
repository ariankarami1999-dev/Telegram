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
<img src="https://cdn4.telesco.pe/file/WBzt2zUGlmcITvCdpAhzq3bbONodZEvLiZioWT2xcJ_ftTkxDoiMmeSEPr1iLurQyq_kRuoIG37squRxOUfB2BB4zKcVYX5VQWDjO4UixvsN6ZvJAVOia0fDVx6rWCBkifsF3L1kTVKX2GIis7oviniXTDtzy8WolvHF_yyR9m1KENEHmi3EqXyCtDNLnXH-87ZgERrdrdhaVwzYkSQysNYFtF0xDDsedcXh4kYfL-PCMBIZyerMbDcaeprbOpYDVs4X74CGAsDxz3nYQnDHBaxZYo42MJbGZNleXUVhUx8dax7VYNULG22ips6zc7tPVbaCqMjTMafkDZTMfnevyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 385K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 14:06:16</div>
<hr>

<div class="tg-post" id="msg-24993">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pboEtNtmdQ4dEgkdkSKREXestPB5RFwpRKgygzfe3v_S_rqVvAv9Ph5CG-rebqqX-hUyFOxihM6A8_qlsNcWwvRYroNpjFhQygxHLiBSi_XKSd-D_H54Ji-x82x1k_ws9gPkMfFZGU7KjslV8TI6Yk4v0ttoicJH4F8UtYfKZhCX9ONd8Co9s9BIBMtw4rmFBTmvoNX8utacstyxIw92cr8hG7Zc2NJ_fbSOGixBQhrgxWelG3vuDdhpOSGL5kbM1TbyfPHXramak0T-6FNRA2ijK53KpMoOrsJ6Je1rYviIZ9shpmuuBkUZAGxkyKUAn5LPhIHoDDwdHxy47vK28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار عصر امروز مبلغ 20 میلیارد تومان به حساب باشگاه گل گهر سیرجان واریز خواهد کرد و با عقدقراردادی1+1 ساله‌راهی پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/persiana_Soccer/24993" target="_blank">📅 13:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24991">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxdOSjnZzBuAYWqP5C1ZgidK_xVWwc68wgts-7zBfaUi1QpKWm9qTZ9I1my0lTo2Lvf1MMtKDLfvlaW_mgMCbAGOxPXJ6bGfrxpSRQmnFu4eIBtuk4otCS-Ci9VkUnpYTgnM8PdlAISGk8PGQ6bD7RQpu4xqfztDprrtWn9srk4cmBa7GPSKa8gwK87PCy0yU4nvn3YJA3bFScjiweRDV_xvOAW2w7EesRX49qrMGPFv46gVTYpZK1L0BGYDlc7V8jdGE5F8QmC-43WL_eoEKZWrshwrRuNGyd6OVj6c-akalLOTFds1eKvbsVneYZHaziP17-gfXuG2JdGmX1EVBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/24991" target="_blank">📅 13:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24990">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEnTNAzMVpp_7k2aTTcQFk7oeiu1f9ygvctyBUqyJ6PnYIqjH8WSDNpu3QGHOY0Yuvu2E5MS__D7ZmKIzyE0c_mvqAJ9264Xxl_0LAjU-IFOpwLEc_lIOZzLb5ejBzru84OUMCOW9UZmYWDLoCLIleuaWIad7F8YyyT5ipKLllCnjum5TxrNHfCnR3WOsgioQrFbWVzBpGD3xMKAEoXNK7_YNNLVZss_i5UYPELOywmKuAJvWeMiIgMQ1itp9CCxz3il8jRxdWLEVKGSKIH-0929O893X5tFWE9rdILxPV3AiEyihLn_1k6RjlnbMx00Sks5WVkO4Ixof7Znp72LCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/24990" target="_blank">📅 13:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24989">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVAa5BXRTBYjlsT9RKn43o5zQaZJ4N8Pnk4noVOoLBhUgL_HN7gs8GjSPDG5-uyXyltqb2J2NuWvhdPMRsJFtxEiiFUA7zhZy4aVB7GQKv3-JA6ncigxNW52k0_iSoNyy6V_3Z2f3uItpqvUiiaHatzAVaoaygwAQXO4pXOHE-wwsW3Tt2UQQ6ato-2raxjo1a3FRKvZ61YuTlZdWJVt9KNoid02263mJDSKT8sNAg5kk6ZKTED4uBK_guUIRDo8G_n7KuCF5oJp79WOCV4d52gGlKeCXxbQxm4DFF8fwPVHywpJy5WpcYtPkJYtK65m-ZlgYQTpwwiqsWx25rSQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رومانو؛فدراسیون‌فوتبال‌آلمان با ناگلزمن سرمربی خود قطع همکاری کرد. یورگن کلوپ اصلی ترین گزینه سکان هدایت ژرمن‌ها در یورو بعدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/24989" target="_blank">📅 13:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24988">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scH8ShAdeCD9RiC5lzvoDSHawCU5g55Swj7lC94vRh-uiiXcLKsom6gztmlRkB0O_0LksrWfu-QnTJnmj6AZht8Q5Ctdfy_tdjKVIIRAf0ob-m2oMh478FEdSVul4RSZ4pzpuN1d7HS1D9FcQxXgF6jXk-ZkbVr4bLOB8furlBNq-77lPQPdiechIcoFlzMQtTKEeZidJTfuWtPqEbNNC6T5N3nhNTvxz8EzJluMpCpyCK-c4aNzu-8HKv06m5jlWHTHjJj8rMvTkxYb5vK5heYICHH_JtD9XJVxrqgx1aopmcfIpIX3H078pQ7_erS2hy8boBZLfeqgo3wQ-dj0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار امروزاگه‌بتونه‌رضایت نامه‌اش رو از گل گهر بگیره سرمربی پرسپولیس میشه. در غیر این صورت مدیریت‌سرخهاسراغ مجبی حسینی میروند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/24988" target="_blank">📅 13:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24987">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ll9EkuL7IdocoWceTlaodEcn9fK6wHuH88evM051Tiuyj-PzlmEODelRs5ZqG9rQJKT_zqUre9lfWPSjMPJ7Kr2FxTT1jz_q15-zBQS34SroEBXemslozZP6X8kJirpm4tEHKCUBHRRj5RZwIwvb0WfKUgkHfaSe2ALurcp4NKdjSgnZcyJgUr_S--byCZPtfLNzK0gyWPCtchOmQi8EqWX5mjzwyMkrisArzFWNOHneg6dZToCJJQLMoxiFbENCXU7V5QZNzXB9rn4TXXeoD7Elh-SBBoXtUbOdA-heC7MtEhWBP09-k48uHsO_sahm89Ud3l6x2jlFz62VBpOxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/24987" target="_blank">📅 12:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24986">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ht2GfrqZfbjU-B4iEVvHxYAw33eG_ORTopl1tZtsrvB2j8VOu8dVEpikkSwLVQbeZ_naa6mii6THZf4FHV__5VA6i2QogjlRZ8GGdXQt5PQaTYAFLCRQ98argqiljskgeZ4sS1IgEw9TDxMVPcn72X2ZWq4zpHvslyZR4BKUD2a88AReaJ9eWR_fRZ0tnyxfRBdb_pMFqFkxCbNNeFjQZFpvaywJB6GN--Qf8ThQvqxQocqJ8POAeBVXV2ZSzMlboU7mG71d8y-rc4Od9vcBne6NVDWBV22N20kQK_dqRVYUz-0BhwEBAlP_x9a9mpDrq656S_wMmvXnzQh2GPZbPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#نوستالژی؛ یادی کنیم‌از مصاحبه قدیمی کارول سلیکو، همسر سابق کاکا و علت جدایی‌اش از او:
‼️
کاکا هرگز بهم خیانت نکرد او همیشه با من خوب رفتار میکرد و خانواده‌فوق‌العاده‌ای به من داد اما من خوشحال نبودم چون یک چیزی کم بود. مشکل این بود که او برای من خیلی کامل…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/24986" target="_blank">📅 12:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24985">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUqZzU3F44c63usYF2jUbX3ypKlgnaC_YbksjA002-XxGvFa4Y4lVC0qL_Jln4v-zvExR4Q09aeDMhrSgIBZQMwxnqMeHxUDBVygqsOJDYvzKKcyBbVpD73UQ63eo-CO_Hjwn-ZOAd5qIr-NjOFZ9CdnFe8BaxWWC4Pu1hdFUcgWul1t4mLllgHsfaND6oBOxS58cqJrUcN_X6LWfOxlUJXddOMuHz5x9aw7Q1gDjFuy5KI9IUc7ZxXrsGSRiNXzRf27gE3xurl2bIrNu_VbzF_36cowaiDy_FGoF1_eTSa7BD6RbQz4JNrz3Ql4zsIHeMKWay0f8M8Zd9jbV24NBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ طبق‌آخرین اخبار دریافتی پرشیانا؛ عصر امروز جلسه نهایی بین مهدی تارتار و مدیران‌گلگهربرای‌فسخ قرارداد برگزار میشود. همانطور که شب گذشته نیز خبر داد مهدی تارتار به مدیریت تیم پرسپولیس اعلام کرده خودش رضایت نامه‌اش رو از باشگاه سیرجانی…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/24985" target="_blank">📅 12:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24984">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HU-UpIwdF3zcm4e-0CCkxWLcjW9fzpozzt6nPPytcnnmoOHvHYgo5AlRNT0X1P455qB4F-brlIZQ7zbXD16NcwItV8xHsQhmOa586NafcoQYVVGL6AF01OaF5Kd59fn5oghpdib3aHqBw44VLNLMZMYiEKxGjfB6CeORdnny0oeY0PwAzYNj1FJsRjSIlwj3_nW2WNanfI2WioG404T2LOhDWL8Jn_91i0ZvPNhGlsiwi9kcqbWh0irKWeb8QgxFREs1JbCsOpdBwgFjMLBk_KdmtI8bmMRWRdSiBVbGW5L1F-_L7JcSXkwmMee3Gq66GRx4C3YatffJo_Khelz86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24984" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24983">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdOyIubnmliPcK43sACt5tuo9kKEIHoV60eYK01dPKFgo7xZGTOJdXDQJf6AinUcDnXRXRsRrtbb8_0WLH9MnX0xEjPYPPXx2j3H42yG57z3igWiWfdBuwI8jmvowRZSmUB9ldu2S0r3Si-_vETBTYZvD595JTo4kqHfXzZmQVKbxnGsrXi2dwjqRzxek9ZA-pH1zP6nwzY8MLGBgJPkWDW775-joiPB9y9fzsqwsyCzQn7kSxyyRl3kKNh5XsXHH_FYZ-kMCw3qtrPz7G0r-HqXXWB63ZGaGra3BReCjt2DugfqjjKX0LNUm9YJSSbYXkGWrgtWoAiAcjV_-gYxTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛ فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24983" target="_blank">📅 10:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24982">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpYQpd4Z_h17HwGgm_vlZA32y2HSG7MaWnpA8sjDvLLR_y7v1aOhiL1lH8iBWF6aZ2b3kb8Wd7QxnUZHAjN3-flgcNLyN8ajH3m6fnCmbHE5IfT8s9kfvlgqazmArEoO1f7R5ZFt9dKOYllxDFTQWa9P6V0_U6LHmgTjw1rYlXq7TrSiO5s5kyilK-7UBZGHSMaXRSmLydmhcl2rK8ffaQEKeHSyC7K2oHlAA3D9KMxDCK8EmHZIczHh2bYYCYLajeE8MwM87oAc5ZQaYttyg7wRp3Mafl_nJQpK8QQIP13o_mPPnwEl5o4WM-EqGSezz7kk_GoAapmh8xINTbtSCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌داستان: امباپه‌‌کم‌عقل؛ رابطه‌ی کیلیان امپابه ستاره فرانسوی رئال مادرید با دوست دخترش، استر اکسپوزیتو باروشدن‌خیانت امباپه‌ کم عقل تموم شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24982" target="_blank">📅 09:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24981">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRmdm1uPOM5rRHkWowlWNvGnoTD80oIouWTsY-quLyCdpJ4NcA5U6L7asBVftCtnJ3-a5xTJCT4xkXnqv0BysnYiZKy11xguhBBaeiUt26eBcxslaIILx0GgudK1MbIHRuiitw9xOrMuLMMF1BgceAmxS1KAOs29Cz1AABJwTpLJMxty3umVSb0ThUBqFAPRn1KDAmL6EWs69mGTE7Ynu8g81jLI766_fe9wzCd5tWM7skCRL9XcCOhKV8awpeNfICLbdS-B5KdmDmJTp6crWXeMubQopOij0eWihbLW_jdK3niISWgvwn5E6HGlEZSoV4M5E00A8RkXpUNgMCkOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24981" target="_blank">📅 09:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24980">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=VsMNtbhzoMTUAFAo6f5xTPHNkan4UNq3ipb54mxidB8wD186GSK_eS-hfHEA53n8jlj13rLNv59lXdeoNjKh88R9jGAkmnsCE6alrWD1J7hpwLIytqRGQbaxa98vEW0Y_gbED0G_egdgT8KXnUWQnai4fnCi5nwdzj1Ysp39mjIJpC2qJz1iSKfjXKcG4IiIkq3dw5Xinr2QDfN9QoUh3ps9u077ABAXCZVrOSOju9RQzDBFUh9DCaOGgPPiLe0gCEpHJZDEE4gSp206GllQ2cCWN1BeDqP4kNXmPHXdUVtRB6AzT9Pnb8HqCwiHplh3jcfPpY1MaGnNoBVJUPf9Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=VsMNtbhzoMTUAFAo6f5xTPHNkan4UNq3ipb54mxidB8wD186GSK_eS-hfHEA53n8jlj13rLNv59lXdeoNjKh88R9jGAkmnsCE6alrWD1J7hpwLIytqRGQbaxa98vEW0Y_gbED0G_egdgT8KXnUWQnai4fnCi5nwdzj1Ysp39mjIJpC2qJz1iSKfjXKcG4IiIkq3dw5Xinr2QDfN9QoUh3ps9u077ABAXCZVrOSOju9RQzDBFUh9DCaOGgPPiLe0gCEpHJZDEE4gSp206GllQ2cCWN1BeDqP4kNXmPHXdUVtRB6AzT9Pnb8HqCwiHplh3jcfPpY1MaGnNoBVJUPf9Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24980" target="_blank">📅 09:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24979">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDRrnCg7pM0S7HmdHX1Ul8Dd4bnCIEOQ8Q8CqGgVwg0-UGbajiqxXeXUnW_PTVo_ii_A96VeI8FBEPkGWgibYL0XruUfrHEWRvaWMwdyQynnbdSbaVxmvoBdCt5-3uS40ZAUd5vDAjEmDEHjPRONYN6BO3ntjQPfWMn-kjm8hnk7gOVSpeLMUXFZXLph-YugBX53zIRDc1O18MoRz_54EBPXau9CWnJ7KIx6_aDUdLIcJPW7zbKbKM_il9lV5SFMFmLJvSKvIIVYLb9RCyZJYWcYSnZaRkfawO3qdiwQKEJljfcsB579rtiW_nnsI6RmSnOAyxQJJfFZvGa-C1oq1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گائل کاکوتا هافبک‌تهاجمی‌سابق‌چلسی و استقلال در سن 35 سالگی از دنیای فوتبال خداحافطی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24979" target="_blank">📅 08:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24978">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=aepufbKeNiKlMYl_yNTp3AZuSzMpUM7UvGutzFDrnEO6oGyuFUitnjWlFUwPidTWz5QpaMboF7yViFEmMpXjww2eKQy2seoZyNRvIvvCIzzIUrhKlLJzUiWENzA6g77Xp066_N16OmmIzOc4N8au2g6q5xUAFinLDU_7h7gS8y9L74nuSX63xkKf5k_IMKfbzjBQKlBu80ybJw7CCrY7vOEV13MEKmdP6Y613d-QUOIDHGscTAuE09G-XvALZL9Oew6oQqcFQtcj4DHGaNlVreFvrKIuyT1eTLNJjQXCX9v42DV1XNMhtcuiiY_OG5FEOLCwcUXoAwGfU78k0mV0cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=aepufbKeNiKlMYl_yNTp3AZuSzMpUM7UvGutzFDrnEO6oGyuFUitnjWlFUwPidTWz5QpaMboF7yViFEmMpXjww2eKQy2seoZyNRvIvvCIzzIUrhKlLJzUiWENzA6g77Xp066_N16OmmIzOc4N8au2g6q5xUAFinLDU_7h7gS8y9L74nuSX63xkKf5k_IMKfbzjBQKlBu80ybJw7CCrY7vOEV13MEKmdP6Y613d-QUOIDHGscTAuE09G-XvALZL9Oew6oQqcFQtcj4DHGaNlVreFvrKIuyT1eTLNJjQXCX9v42DV1XNMhtcuiiY_OG5FEOLCwcUXoAwGfU78k0mV0cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه خطاب به تیم پاراگوئه:
اگه لازم باشه دستمون روکثیف‌کنیم و وارد جنگ‌های تن‌به‌تن بشیم، این کار رو هم میکنیم، ببخشید که این‌طوری میگم. ما اصلاً مشکلی با این قضیه نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24978" target="_blank">📅 07:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24977">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHHxO5KBnvtJSNWhwAC_8Lta3NoUuuqk0ICkK1KTBTcj5Dov5v1WT3Q8Hj5bAEV7fZhGM7GwL8aBCc_T86_t8gF6nwb8yv9KjUxYk_XKQ4K02bee_O7J7yxqfIaKTx-j2bxZePKdBd-TWIaQTJCz3cXcBZVZTsWiln8W4dly9I8i2xgbRv-iJFT1AzM37uqpVhByHXI_ps7RVCOFuArFI7H90IBRHhvramMMUe95m5tAqhaYlrIbx7PSGWcSHkmTnEq_z67mM3tY26r2ii5eBvs4l-a2qN8Bvgj8H2HfOn0QeA-gIfQenkDLGEZAtwUvUBFIHHUmV-P2J29FFv84sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛
فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24977" target="_blank">📅 07:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24976">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=GezN3ksoTu6rNwnp01shMoZMDusfd0yKil5tND-FbS9cXhnHhLICGAEoPMUwrZFWwcsJStz_MVAaQu3FfQF9oKlu3zCLSZzlA9es029n14NAXBhtMpvMx4rhDRrsTAqnS4bs0QsQ8jdnMquQcDVmbRNWXAwxn8oyxQD1Vmez_n-JkyvL_GHMwPyefwOHvLyO8u9hbHIcHyOkVUBjW-nt2Y6lDjPqDpulqpBJHgCI4WD0mdLBzREuICncjV1SnTFVBr_HPRnLKHGPCZaxj55564rUJk3e9dqhYJOn7ryouRwuaEMHYB0_oag-9NpXXHpySzdzugRhNHkixExm6txj2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=GezN3ksoTu6rNwnp01shMoZMDusfd0yKil5tND-FbS9cXhnHhLICGAEoPMUwrZFWwcsJStz_MVAaQu3FfQF9oKlu3zCLSZzlA9es029n14NAXBhtMpvMx4rhDRrsTAqnS4bs0QsQ8jdnMquQcDVmbRNWXAwxn8oyxQD1Vmez_n-JkyvL_GHMwPyefwOHvLyO8u9hbHIcHyOkVUBjW-nt2Y6lDjPqDpulqpBJHgCI4WD0mdLBzREuICncjV1SnTFVBr_HPRnLKHGPCZaxj55564rUJk3e9dqhYJOn7ryouRwuaEMHYB0_oag-9NpXXHpySzdzugRhNHkixExm6txj2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
👤
این‌روزها ترکیب جواد خیابانی و خداداد عزیزی خیلی‌سمه‌خیلی؛ از دست‌ندید. این بار خداداد به جواد گیر داد ولی دهن سرویس کم نیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/24976" target="_blank">📅 00:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24974">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fs0cpzgNs6BwDOPPznL5uOQj2SHuSfFVme6fA5Lc_QmMe3UKV6rtmroMOMKFCDvKS-iwSNa-Z_FR729-IZBBJJIU9146vvlEGes1CMTLaZ0ooJ36kF0MLeBlAJWJ574IMiWozVg1lXbmeGjKR-OumT511hHfE6aR7cL-HwPWxj5jKqTCiDRtMR2_rUSq8AHi79_zyWClBbUXoxUYmdLFEK-B8Or00bFwrDNvzq3ehq-ENWCSa_ojbZEQf7tUtKcfLqwd8J2cKCG1qJVgUWUjVAM2UtyUhznSBTwb0GDR21R77oX0qHk6OAsduzDogEScOTwH3C50-c_zE9pdHfz2dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24974" target="_blank">📅 00:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24973">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO5yBqTVBE2sm20Gn2dHqnv7TIdzpYHLOYlknWz869D-_CAnyMG2ptkbvEpkZXRBNz8X5WL-aNYPGksOc_ywjvaOhhMcS5YVE_pBSOtcyVEq6pLH5R8ailGmBGSVII0KWQ33i3trdpMC57V811BW1IZQdnbQCjaOq5tD0ex1_nukJHQdLhxnEC6lnVdLK6T9BQbPokCBqjv14-cV7ERuXNN13CTCTBv2uEEahWq4a7RAo4qolZxdf32pqNmIHPjN0VGwf7taeFNXbYpZvBZ146tgNmyLA5xBF4F3aqYIP2eLyBvc2xnUh33z8wneRjrocXTzWVpQ3WUft03E7VbgEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛
از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24973" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24972">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdMH_NIDsspAZrlQy8RerpBR-Cl6HqA6-e-Z1IYFMUHKJKfiTZKKvgMJjTAO9Qx4wqEiQlDZeZJEIEBTHz6Z8yChtDF8Jwjx7D2NSyfj73XmPeOSOdhcTPvVq58vB94Ov7cFRJKUlqAgpDbPn0Ld3CLUr4L8uzbb-V6qrRBJwq8NVlqcRQD89W41iKrlV032j9mBn7mLG6Y1Qn0DTWZp9FqFijr_Ac8oiragTeWaEwc7YMTC_rHHgKi2_9zu3KyJHjwZdxZpsTB1ArJuEJFQpXAZRDc_qiEACAwWAdQ-YHA4flmix7uRSl9prLkAdvhrPQFH47WS6f54LDGU7TaaQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود دشوار و نفس گیر یاران لیونل مسی در دیداری تماشایی مقابل کیپ‌ ورد و برد قاطعانه مراکشی‌ها برابر کانادا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24972" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24969">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNqgkvMUhul15PXaRNTNu_AvJPBfuEcXEVMZeAAQH_gie1If4LUdhwH5dB3eZWzsrrDLEwk-kRsggZYaNV_8wJTfj7U1XYTjEgE3SPUOv2M84-CIMYxWDtsjGKps5B5Wlhuzy77nzCkMvoy0kx9d8cy9hP1PHY2ZjxbyfNMSejMlLvVTT2pGonf1LBsjX8_x9QONvPqlA4Wb8SvXfxqw6-6213XEFa5-XfpOqNSxVTsWBHmwBA-fKh_HnF-0pd7gaLWJzsQig3EjTjcNFSefUqMGEmcqVb_9TdoZ_fQe9T2u9jlrQ8-mzgM7Q0CLjnZY8CdPPxsvQ5HGGjN5Y7BaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الاهلی عربستان؛
ریاض محرز ستاره 35 ساله تیم‌ملی الجزایر از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24969" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24968">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDL0LB70NJOFzaXs0iIy36eAE8QqsaQSvkL2adBqt24Ei3OF1Sk6bR7ObbDGcteAr8jsfIu6HbcajcopxfsnRXIpZ1y2BZ-ihqAcp55Uu8B8pkXOz6_zwtUvJ5aMg3bzXPbGhdLUFIANLqps4i8af_d52Ru1D79-qPbtyD05tL1eloGFSvGWxGZ3YkMI12kgrUuXp3SghpCSzjGvxySEd7txWF2kFGyY-npVyYGrFe01MjfoZw6HmkzRVHxN-DCD1ABDVbbJzEyLoJEh5y45VSi_Uti6knFEyTTvATkgyMgLwebFXt2OBMt3LZskWFfCbAzr5GZxc-oGl_OWBIh0cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24968" target="_blank">📅 00:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24966">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQbPyBUYqaCsvFw390eV1aIVkLiSzXVTPtuOAJV4DUtWbzSKKT3kbbJgx0aoTUtLF3_hHWu3J64FgU148YkUAEdWCkvGGKFDysmsyClnjq7BDvTVXr3HvDvOROcRTcZkY7JW9lAOGQ5v_NxuGqIYRy89guX8xgku_D8UvB2nD_Sn8onVdyI2TDU2Yx3pXHWD2oi6RnIsKAneCXs_iJSQ5UY8P5K-J0YlJWoPAjzuvuBYYZtnKpfq3qi8Bn10qFHWqZkJ_kKJpYr1Z7F4QikA21L0ohJDTgbXtaR-0Xn1yZC2mKru9R2EuTIGCqwEhKH-pGgzkAE8H7PmGb7qMKjVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24966" target="_blank">📅 00:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24965">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pnlm3DCZgq-QU8dSTinAKWwZ3XRK3gKieW7Foau9i2bFK4SkkaLeIjPB8HHfh1tsolHmecAKot7Pwn4k62NozMxdfkZHG4y2YyEocvP2v_zvhvtUAiNhR2pM731rrJRTMrPzBnmueWlf4XkzYmoB9wT_QouFTwDbeoMac0RrE3RoH_-CXMMg589GzeK1HYyf5qj168oUXsOzar2z4AoRFxCSYasRQ-CRfOmetrY3vUOGmq1YCjzLzaHdYMYtO0ecAXAri2ysO2m5r7OmNCSE8GKZanKa42CSQaK6wngWB_f5mQwHfaVlSDGtFU2OysaSVYPgLY0KRxFoPpM-9YysMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24965" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24964">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCqVlt5rACVvAvD4oozXQyYb0x1SB4r148h2_KQMMPepYe0q8oGeARe11pQE1jAnMEG0rXts2bSEhZJiXS78kCOCw0m1t1ju8A3wPoYvcw9mUvJYlySUdW6zVj0MwfosrtjL89-MbV0NmxGuTHcjnFosjr772bxElo32-yWaF-7cKMiVy7kBW-pfRRzWNmCDaOJrcBUUpXkaD7g7z-StLuDfVMYcAiIJk5ePeXJFJbClzdO4UOBaFMdDsZdoxqwTFSEepWARNnXlPhEGHue_UxKO9hnW4VlX1G18gb1xr_hK-aN3oe4dbAE8obd4l3yUpmi8gG6VzM-wliucFIiC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
💰
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس با ارسال نامه‌ای به باشگاه نساجی رسما خواستار جذب دانیال‌ایری مدافع‌ملی پوش 21 ساله این‌باشگاه‌شده‌است. سرخپوشان به مدیریت نساجی اعلام کرده که 90 میلیارد زیاده و تا 55 میلیارد ما حاضریم برای رضایت نامه ایری هزینه…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24964" target="_blank">📅 23:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24963">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7KcqKLOMIPTmc1pVN0nqF5N5bu7h2DDsEaZqTA9oU91-rf0VM295kPKmGYlgzUl0vBaK74XpyT4YlSgmtbMzMHNBpa5rcXDMmg4JKYddt7IUbiFj_OGH_o_kp86OojwM7Dxuvr9hoERMHZ1R3ZFxrOflncO3ia_3wC7wwajTBhyNYA_GfTtqpDE55QcBU9sW-gPna2LBBGcmjhL-bQjph1kWvPhv_V9r8_pyYXKgGrlUPKF50PyaIDzcwI84wn_3cFeyyKQoR3AKhOUetE1ee4SEvp-FnGLpnlyZ5BNu-uVVIHpsJPiodz8VVVwRNW0_q3cabWwkU6uYg9BZU2QXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
در بازی شب گذشته؛ این هوادار آرژانتین کیتش رو میندازه برا لیساندرو مارتینز که براش امضا کنه، مارتینز هم کیت رو برمیداره و با خودش میبره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24963" target="_blank">📅 22:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24962">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdyVwVCqCppy4ECoxX1N5CtL4icCEXfiTWJ7t6dWZgfYijK1mgmsQx3ivZrmkpZusc5mh8jd92HCeyNoHNoWhVCmi8Mk9Kpd3n--JcRVGbFgXCKo6fAVEDRm_50220D5UUlDa_cFFFMZFfxeoLB2qNtBIOZcRU8x4-bdEuU_6suPnripZEcmeadP4_967xQhk5FErabVWOpn5TXxZcp8nTOysUub4KTb-V9JMcuR9OlWaQyLiuerfsku6xOlbCQ5K8cTw18zzQDw8FRReJU92_ZHhy4mMzN7LSUPVhZ9Jqq7shAFztTawB4NZSE6xdHT-nd-zDViH_thb3tpIKOF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک هشتم نهایی جام‌جهانی؛
پیروزی ارزشمند و شیرین یاران اشرف حکیمی مقابل کانادای میزبان و صعود تاریخی به یک چهارم نهایی رقابت‌ها.
🇲🇦
مراکش
3️⃣
-
0️⃣
کانادا
🇨🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24962" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24961">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpCV4BTwW6WUGb848v2_gi602iVqAxeHWSyfsMT9evlmFbshD6d4z4fdk97PDYlaVkCd4_sGw_bhygPhVOqBEZrPGfEb0l2F65M20iz0z7h6-PFqcadsZFx3QLoJjBiAifV3hsEtm4btGp73D3_X8zKPym-ITPmSCQrbMvHt-Ll2WSXHLZqeOg1o21unfvmGZqthoV18izzvsnouHdxxOc0aWN8unoysJLfuvsYjXT0QGUizLW93CZ6nCQeSlo7edWPDzkRgkgpq0H1c91KnvLSZWJLAFVdVibjAEw5rxj6MAg9E1RXxCHIhilbUY5HX6pJV_A3597i1SdrgPZkNbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24961" target="_blank">📅 22:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24960">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuxasjW53ou1ruU4QIglBeo_10JbC1cwylpdFuLeFLsIs4sZNzkh8xKFY9vmzeYkX1MUWSNQfoXp3xiOAzCMXBk1j0nRwhTt1cBV4tTYRHOSGHqrM9zaLV3kYR3fwQzIKztWlsEwdepw30gJJuDbHXK8YKGc6l1n0d7fvc5pGa9DidHKPRRw10oN-kpr89XKg2EX9EIfrRypVQd9jzI-p6CXpN_c0N1RpbZEfaNQRREuAUHv9kq7zRz7NYouxXmikyIrl0h15ipEb02b52ArXLbug5EedGwfIP3SoCuIIw9YIjRpzPntxfOWdOFgBRRXoqFVs0ATzFv-BaMjguCSvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروه رنار سرمربی مراکشی تونس بعد از دوباره از عقد قراردادش از این تیم جداشد و در حال حاضر سرمربی آزاد بشمار می‌آید. کاش بشه ایران آوردش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24960" target="_blank">📅 21:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24959">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXrPpvASUSYyDpx3LqvtFpIj32AaaVCcDRiejfI_l5qNnbN4tbMQM_IiD76n_ZIJuAxf0KreZPnS7mzZxCwE6zzPtXmhFwhUWQUFszuz6TtibWqIPvAMhby0kPoZTpUs8OZA-JPq-ILTpdFAHZ2q1r2kSJCf7b0BzugkiyQAnh4CSXLLhkp4sfsE2nw-Fsb7zBlaKquEb6fjrIswIMLVQxr18Z68_DV1yYzmk7swIicMph9EC6VdAWf0Y0sqeQ5NEeqeQkrrau0_jmVtMLP4eN-WezNnWxl-GaeJaRR1MdK8oquIaybF14RUiBC0mOSED-P4CW1pVBetcqTtbHbkvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇮🇹
🇧🇷
بااعلام رسانه‌های برزیلی؛
کارلو آنجلوتی تصمیم گرفته بجای پاکتا مصدوم نیمار جونیور رو در بازی‌فرداشب‌مقابل نروژ فیکس کنه. نیمار در تمرینات روزهای اخیر با انگیزه بسیار بالایی حضور داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24959" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24958">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx9NTp-EvM-zzjZhaN3FamwpZ68GhioELq8yXwmeqNJ_uqHRTXU5U9ywWXzZWTQuwIIOpkX_Yi3I4yYu0Nzax44JtC1lDTH8OkOBRg5Ee95HWaJXxRmf79mK3mzImq6l5p3zVD_xlHKZM_HKVfkJx1YMIJsIFCSv8M5Pg0sgWu1IYKgoq82kbtx9HYznYSnxXpimBDtedRzAVLF50aFAMYSox-NXXLMshG5g9EAUEq9N02QF5X7VuNSz5je-B1orA-9_P8yy2yUJgUshP-48QnW7SeCsUp3a1kpsk5iybwSY81HjrGFJHMZusCOTqz2SheVIsMScMJtLrcc3VBCocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
منیر الحدادی ستاره مراکشی استقلال امشب در تماس علی‌ تاجرنیا رئیس‌هیات مدیره استقلال اعلام کرده تا روز شنبه با خانواده‌اش به تهران باز خواهد گشت و به تمرینات آبی ها اضافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24958" target="_blank">📅 20:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24957">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mILzayPobTG84Ui0EGYP4g1baVIa70lxmSPfIRYyBduD-5wGrhlpRIZQbA37OhS23p8UHQ3_ito6w89Za83EA4k9qEuPurBfN9gPYhK55t7E1JMjZZF1ACla1G7PI73XUnZtJfjRYdW-2DKKteNVAIhxXPJpSbu9_z0fcONxVwHDW9J3TzVUm23TR3mGHfBcaJR-ewAUl8Kt4mOzqEis_Ts3eKzqEO8QJxOhWNiFDxDfBFMWOjXa8MCt39n-CjxZtmSE-I-TxvZmBUQcfnUK81DCVMpGbPvXTCO4-DrQBAr5aLwQC5hh9kTzS0XUxlhnPFbi0mNcFUY7_J0o3csF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24957" target="_blank">📅 19:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24956">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k66H7myEe-65TurEUsEzpIfm9c8aEdFBUUxV6w1ADt1h4rQV6WzDdmC-e-XvRGHupWffd8zPZSAE3OnhF14pOxMny-TffXy6E5uH5FC3omu41OZSUNzUj_Xi_rDP2cx9OxbBCSl2KVx_g-5N3085iGWuHj9Iuo7bDlqK_2BZsaIZjMUN-vHyDMv_A00YIRKJN-rrAy2kNeY4pKOEEh1Pw8ziDpUk48Ev1Q5_JOqYGQ-c-zV6hiBEZJifiasXNLI-F7Z5Vi3B3s-hG6a0KvXvAwChwx4vnilOZzSYfHV2KefNp8mjv8VVfBBXkKgmxnekAJzLaKYa3t6MY8PEv89wfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گلزنان برتر جام‌جهانی در پایان مرحله یک شانزدهم این‌مسابقات؛ لئو مسی با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24956" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24955">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‼️
خودزنی‌خداداد‌عزیزی روی برنامه زنده جام جهانی از دست جواد خیابانی ؛ میگه اگه زنوزی اینجا نمیبود همین‌الان برنامه رو ترک میکردم و به ارواح خاک پدرم دیگر به‌برنامه برنمیگشتم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24955" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24954">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_mXgC4r7ErgrsNUiK1nT0xxmvi0aHmtiY7qkAX70TavRbO9WLiujI3ClvwSLDlY29Tk1zFIWzO3-LD42RxlwF7sC4bLfltq6yj1SPypNVrzAthITuY0Kzsa3t8BaNTiuVOZtbEPtWRUjaCLQad_PdXXcuUfcEnmAf9m9yT6sGFjcWq4kWOpjyqdRfagCP2V9z9hHY5gL-v_uMMwgLKeh6A2alGwFGbN9UTf2F5snTM5ydQPmdiF-EzwpYftrcDLqCnPBYV-wbcCXQVLWDxNhgS_veUfOwcPNB1Fq8_nrkVmF_P5bdTLFPnlZBl2SERdjavF-OSDoos2UR9_ReDbnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
کانادا
🇨🇦
فکر می‌کنید کدام تیم برنده این دیدار خواهد شد؟ رأی خود را ثبت کنید و اگر پیش‌بینی شما با نتیجه نهایی مسابقه مطابقت داشته باشد، در تقسیم جایزه
۱۰۰۰ دلاری
بین برندگان واجد شرایط شرکت خواهید کرد.
💰
جایزه به صورت مساوی و مطابق قوانین و شرایط سایت، بین تمامی شرکت‌کنندگانی که پیش‌بینی صحیح ثبت کرده باشند، توزیع خواهد شد.
⏰
مهلت ثبت پیش‌بینی: تا قبل از شروع مسابقه
👇
انتخاب شما چیست؟
🇲🇦
مراکش
🇨🇦
کانادا
شركت در قرعه كشي:
Https://t.me/betegramd
📺
پخش زنده بدون سانسور در کانال تلگرام
🚀
برای تماشای مسابقه و ثبت پیش‌بینی، به کانال تلگرام ما بپیوندید
عضويت در كانال
Https://t.me/betegram_official</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24954" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24953">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsCVy7HkJzSXItO0doahyRo-7JdCITUDU5HlxghxAFBuvS7JKXLEVAMw5Ns-TFTIll5Le_fcT769b-HyEFFz1QmfPdg9ZYhje6sVkTzl2gjd2u3KBIgwQ_S0s3eyD3Yf46iAwvv5VwMu6eXlo0Ic8RulHZq9z69mpN2BqvHu4yZtJ1R3XEKCKBZHCPh6QgFRJ61bLwBr4RIlepwe-T3WCohsfLjXa7phQ1x0qvYsIdkhECGB_vTyptCPsEW_RU0R76FrGEE8bDN5OA47GYEYXR_dLiuY5YCl5YnLZqJnqMFQYBB4-LqaLc7bjjo3wq6wCuyXj9fkWc8JP4LyvYqjaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24953" target="_blank">📅 18:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24952">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keDUlb8Lt1zXOGNy1XsSLx00LP95OvBb4Mb1nYW_NLHhzc2dZJkU4m_3kFiHk4F8X3PGkgRmc_5Nv8bd9gClp1RG3eemR9dWkxoDFZqZS1ykqyEptww23it4nmSu_OEo1UZ2qEUqod33u95-MlT566B4i5ETV44_2MFBLcg4dUlXCaMGKF-AYGAmatceiGQxruxf1iZ-P6YmfxjLvsnJ9uZtk0M2p18pM4bSS_PUoshkYj_t6ZLZPHnT91gHzm4DpTwzPO4oPts4YKZqhNyNFfhpWHuRqMPnhlTyqRxAp5kF70XTsWvmaZZylDyjvYhiQT7v0-iOHNsJuNnRqRjA0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24952" target="_blank">📅 18:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24951">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFbMVMOY8Bdi_f3Jgxw7u9peIijKzWbnqsbSxQLINIfBaudXV3lstxAAPQuUQR6xO31_3hh6-sDo_IkbUWSozdkU2tgMVuh1wY2-VZM9Qso6R0iDtIvK2a7KwE1E9KW9cB6WYejyxWHPk3gT7qbrP47Cv2jwz-H2an6ms4m5eTNLKxiNCtdl9ex1aBWUBCBvCZGj1FkiVDqV4ufNcNyc0JU20sqwvcpbvjsnkLY90AZqB0ALSq1epMZnftGJ3Dv-UPIjxgq6shGTvqHc7K3p4D2G0xJTVItBghtTx403bOV-3rxIFYBILP_cMZrAktVl2YyxjYIAIUJ2iU6cLdQ9Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا
؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24951" target="_blank">📅 17:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24950">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiwP1GgLoS4zYgx9Lu32s2IKGBiuba_GamQ3qxrNuzxaHzwRbMBtdSKBMfKSQAmR6EfOwdWvJ2qCJ1Rmi_vhrqQA7l_cmFpmJmxIUFOZCcYJBCKOjKGxeLC8_yaUSAN5f8kffFKH8-Zsv6WGzmx6bAOUYJkZZ3KdUiCeHp5pLUAL5hTpS_MsRw7FZZ3MQGKJkdsFHGE9hIbbuwaTYq6IB4eTXF8By4X-mhgyze-7ncYAebGO-W6hUO2k2swlo6VsQMiuHLlcGj7M2rXpPXxYmXUTBcWLzhncLU1mKR3eLduGhhzGKbhxd-WwQunAo7Z_qB4twL8-Qp5UmbZKJOOktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24950" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24949">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLf36UGC684DEG5fzwKmpDpqOy5WD0Wn9U3A7NUHp8g_sU3naeZW1FrE6RAqqj8vJ0tJ2RNx5T-LoxUS83I3UwBWaX0-3K_Lgofq20WV4CyI4RVLY9OX40y744eI1wxSvLkPH8cx_qE1UvLu9Qknzxd2oGQtxZ4XJPtGCTQmCi9nRYRMhxAMNhXEHAvCYAk2hxwr6zfxTxUvh7v3fFaS6ge35YT6MQhwe2w7OgIu6QWUe16TDYnsww9TzzWfDQB2OXxxz1KekV9p5NO1tC4zbx4-SYk5Dl-I1i418fcZrUQ23i4sWSceZB43-sQYRQ5dx0DHxTDcyB_jzUvb9iCneA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24949" target="_blank">📅 17:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24948">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMv3LyU3p-KR6uPnnKpKrxxmYxBgzBMUy2sbgLE1b3ilqmr-GPBpIKCuEiF1gMm79yWUSAkWpJsI1C8hZvuXwmwCtrMcRMhcGHw3v8HeydGN_Z6qgyK3wVObxGVO6EkAlPxKvHqwRgQDWqy9T5aLYiledR0-xZijRDWOxOG9SEyWXbbgeoMUUhlU034XVcuyO13hPm5utCf0SauCHEwyCUFJHkvfbs0nNZ-Z73t0JGcO1pVsfrw6ZN5A-aEm7YXzXBla8pFvv6VQWTYfabFongAi2JSuOEJOy1Ob7R3Yq2QWTuAxMKNeZa8zijCBCDd8EASf7aMxuW9SH7oy3hIjZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
15 تا سیو مقابل ستارگان اسپانیا و آرژانتین در جام جهانی سرنوشت یک بازیکن 40 ساله که تا قبل از جام جهانی تنها 50 هزار فالور داشت رو تغییر داد و به رکورد خارق العاده 20 میلیون فالور رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24948" target="_blank">📅 16:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24946">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tPwI3oYuAqnmhfUToWvedRLL2S5J88JbqEM-XD2Waqmgwj1MKWTs1JUGzUq2voBEU6gAp5UUayBnhBsvyNdCu0YDMeKX6wb-NTtdhJZlx3ZJTl6cfMl7x6cZ3bshJ5ZP6RRLvNYRL0XdgXce-ybsY4Ci-ZBfjeEyIU7_DWbMrbiItYD3KJ3HdJVKf5ZRIYyioU42FqYBuVW75_xMW4J91n8_kC1xvmrNuW4LndE0fBhmPH-sR338U6YpIeWi7HR6WYmJSszXrE5cu7hzMT_kRJskAyF1-HvY8tB2Av1btTvNB-j82My73uoIROdWBYfDaf606jVJ4wbEVC6KNmeMUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/giThAnPNWJivSbfjN0a2bghiY4wkyzHNE0An9h1IGfbN6A5pFbJD8u2Ky27ZIM8SuCVvLaqGVkGlVLMR9qaCRUeqIW8XLRoxk6gejhAlc4CZX_N8n1R1LYC5x-Mm-9-bPtwGlpfrct3yWFJY5Rb90f5NkPirM-Uz_xMfRX09atb7GT8XXm6iK8srTv8Bn-bidcwMPkQJk_5A6j0C3EOypMU4k0ld3X-pKG0QblBl6oLYEEZuf8UBGi7o__272yRi_Jdoeuo2AyERX0mdNBk0Re7OYNqa0u4dXMICaTDccoyXkNgVSkw2CpfRASk6VU-0rir1Pvf4gedbWBiB8UdZ9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24946" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24945">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDTyANe1GF5CWkP5XajatjzH7Nay7zDZYzOkIU-ADehVn8GwEFMQFty4-Mk6ul8cFp7Ubi6C9rgJUSR_HoK4K1siOic_U_iufa9FlYHSnoTWVYfK5D6l1isDDcS8M8ot1X1DpAgdOE_FBc67QFC5UkPMMZ6acY47GjZPb7BQdnlDixamQdKnBeWuHMbcMygl_GK_NLzZFR2AOE7gCMz9usA_UzvlU2--fM-yU3u7xsjU6BaA587Ccu6g53HvtL_8_urV_hNNvtKTCRGBGs1x-1Ohpixc_3P-eNKQ8vq60d2Ke2gI7qifHscWQuACym0WeYB24Ppf7Otro575Ig0HNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مقایسه تعداد گل‌های لیونل مسی با پیراهن تیم‌ملی آرژانتین در دو جام جهانی 2022 و 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24945" target="_blank">📅 16:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24944">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkXkhU-D03AUS3FqAj3ARZzzwtip1o43cXl3-hnY5kvRGUPZlMy6PHOZjMHdocl7zXzF_BL3LOEO8v26hhpWI0seVB2Em7VYJwm_gmBaJAuvZIrq4n8JA2QHHuI_iTekFXamHnmySGpAZu5T1ief8MrIad-oPSki1_9HY-OwdxNMQKxALOB9fxJFip_uWKyywb3BSELz7u57v4StQjsWSODWEZQGKrfOscPLxA64BpS47mXTKL3k2453qERhtWmX3FD5MDcmkwN1z3bM0JATv0c1sjTmy1agwxqdEqTO4BCn0w6sIMm2b7RP8DmYKpUNtEDsoUfRqosB0pcJM6xIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24944" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24942">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXH8-L6-xZ3Wkd7QGk37svDKXFkKELvbMfkl0WVHKL-cS-Bv9yBLV3q4-fCYfgnkq-q2eqVpiJJs0h2C72DUyGSVsia6zwO-cDkackiat41mbCzlvgDYCDLoLPH_GVZ8nLdqCiZROtn3dc3HmK4QI45zgl_5TN7tSN37SOwv7gdaBkQEbA-4kn-TvBSCbEOuikQrXfGW_zsvthtFIGJxJJ8yH_9YrsELTApk-ODsb2nTHpJLIzZoAHTxL519nAkOU-_67c7O2s4DlZN-CK6jnshtB6cptMTbidOsYJ6ocLKSMDXF54erwGESiM2HITcKG_9y-57c8kVGqqDBTqJJZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات
|امیرحسین جلالی‌وند وینگر جوان فصل گذشته باشگاه استقلال خوزستان با عقد قراردادی به‌مدت ۳ فصل به باشگاه سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24942" target="_blank">📅 15:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24941">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCcHJuYmEsK2nOP9fv9GBgusLkzTPzi8o4LizrTRJN5_T8OV2mmDsA_8_hjt9ySXfCtVh_iSkSMqcCHsoLZ4krz_QTzf9xdKUFpQObC-isj8ksnCBoyZ6RjZOFlLKZ7qnT6vN_Rn4aLHyV98YHQexgTfig4Z5AwGW1N4rX5D3gl8I_n1zyT3VYsIJDIbtrMQjN82EFPptgAuiuP6nmVJhaC-RbWdAlfRNHsxpK_Qnxpkt3M2ytYfsVpO1h7o92O752ioZ13ZjvWortNciAxKC0axQG_ZLy6C6pGyBmKUm6IqiqHEGUbL0v2Ywp7qoM5fhwCVH77X53pXUaQ_Zf6WgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه تیم های حاضر در ⅛ جام جهانی 2026 با تیم های حاضر در ⅛ نهایی جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24941" target="_blank">📅 15:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24940">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjsKHD5n80oHUwpN4JGBZHqngk2B6gY02kqMI5IC-X5roOhoOVQoJtAvGU_SbeGxmuWUvR9ER69mzrzFq8JMkzFiDQdkkUwdKEkCgO36AAkPC4JsiHLCW6BsrsUmTMuywasSztl6NrYl1o6s5H5HczwGp3WPYFW3Oow2WXNTEpl7_2g8NaIRuvkWFgTKrAmriBRp8WnKfO8uvxf7RSJpk1SFhA_EgVx90PHySvJyH-Tpm_8vb9PsqRXP-_y-IxHybWO1--g3qhHNEUcUWROUPpKm1_-YdT2CJu9rZNpM50Ekivu8x3eYPCLiALbntCshhVRVTVPv_JJ2165MKOA_4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
همه از عملکرد نه چندان درخشان بازیکنان تیم بارسلونا تو تیم‌ملی‌درجام‌جهانی2026 حرف میزنن ولی کسی از این حرف نمیزنه که این نبوغ فلیک رو نشون میده که با این بازیکنان تو دو سال اخیر ۵ تا جام‌برده و تو سال اولشم تا نیمه نهایی چمپ رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24940" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24939">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5Uj9Q6uoeGXoQuX4cUXugg7n5mQYMQJMpegXbWgBLop0RhBKIDHNTywLUdVWByPGT-UQrm4Jv7J2F868f6GM2Oi1ziunI9ISfMSbN7eerUeQnaljktaDZHwqNW6d_989B1dGer_L5ULa4FtANj8YjM_7kcYP3ki57ViqFx85pCA4NrN0ofOvTYLUIYha1Vb-V_UnrPJ6Y9vd_kO3x3C5a_VteIuyq4Z8sSvkZrtq7EIljXlN9bHNJZYcRE3XpNtsWUo0tsDJkCxXxIqScZsU-1VuBEQkcYpPxlqp6EiwWyVv8aA8zGdt6HA13CiGedQRzoj6HxGZ0LGfL1aTtNoHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛ لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24939" target="_blank">📅 14:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24937">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O7uXrzaribDEoWzoiv7-ZZtiFdUTTvUFkO-nWN5rbB1oJVwuVvTLRJWk52rnpsEUAjyW_bvZY0a4waIzoLMKNW0kSJpXy_O8JWqWk0NFrsp_jUyceNQheJmvRKtu8IcQ4jv7ZkpMDzWIIfJHdAj1cszB1NslTc6x6G04KhOa1cLkLJ-TGVpwdRId9F2BHfgfIXbqmyTt9fzZvzuSoYMou9xnazysSxqTqlICSN4PLRkPnq5fW-Hm2TtM0-DvRNx-DoLoGB-yMlwO4TLGMiCCo6gijYrvrQV55bUz72bYuxJsclI8ryfyNS19f-OY5ZMAgxdI1INxflcHy7plLP9izQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aytexsODlI5TBHo0KpCkuVPvYcLM5-1wkHLNAfc_h19RMC11LlK0ElzGT4BPnpWRFb5RBUsuuuBJN9lFOMWbNDBXvvRLj_CF_W2vyYkPAsln8HPk1NOah0_nBbJQ4P7PDjWuWPzlGTGojOhHaguB1jumVpZct1rDsFu2PEVkOSpUfTJ6gg4qy2v2YpYn1sPLoAJPzMDxL4vlPla7qtvlQR4Od8w5JL6d46EIHGIUz0sDeuO3bADjbXMoxIHoEPZHGFThE_KpeJsDcVRW6d_KKPw8aKJpNA8rTKr2svUL7dPNCkZrO7J1NngiUzbHoXzBZvISTybuTjxppi2vZlkBvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
احتمال صعود هر تیم به مرحله یک چهارم طبق میزان شرطبندی ها تو سایت پلی‌مارکت:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24937" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24936">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=L1U-VX0TPt0Grcqq5C2ClnI6UueyH5wDFvcROCDUHxjuQErAEFpj7gZjc_m3YLUik-oqw0--N_-vLGI-wkuI7SyKgJx6Gbq8xmNqEb0HT1TwhGU77-qwpQX6lXK8DaP1nB5j0H0kfCvYVx2Hvbk6eWYJw5yrNatEj3aJXoXf8hM4AKYhdX3xPGNrFlM-xaXOmgxWj1Xg4xO0gPLN2qFmU9qr5yJ4ryhG807KMQmmAnh4GVU8HoA9O2g6IpreKYstvjrygE9E-VGbKZAiIaNi5P3r6EjvIL81b6pB2t4Xzrmu9GO5NEQlqWqb-Gjlc7gRTrvVbVirMMq-NcglftzWxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=L1U-VX0TPt0Grcqq5C2ClnI6UueyH5wDFvcROCDUHxjuQErAEFpj7gZjc_m3YLUik-oqw0--N_-vLGI-wkuI7SyKgJx6Gbq8xmNqEb0HT1TwhGU77-qwpQX6lXK8DaP1nB5j0H0kfCvYVx2Hvbk6eWYJw5yrNatEj3aJXoXf8hM4AKYhdX3xPGNrFlM-xaXOmgxWj1Xg4xO0gPLN2qFmU9qr5yJ4ryhG807KMQmmAnh4GVU8HoA9O2g6IpreKYstvjrygE9E-VGbKZAiIaNi5P3r6EjvIL81b6pB2t4Xzrmu9GO5NEQlqWqb-Gjlc7gRTrvVbVirMMq-NcglftzWxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24936" target="_blank">📅 13:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24935">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jwsg1CafkfneSY2pxORlVeXi2AZQZbN049_RiYtLQgoDnURO4HzHbSGn6o9cSMl2hwogRuormRdNNa2KhzwaW7comyOKSZKXN5GYTH83Lkqf9ixGfWlhPzHQUZAQRbjn3aVWge3am6QJfD2AMYHxlVcyjmMwZ8jWec8ZC2PETEC0eIvC91ZoDDC9ckjaPySGPo5dyNzvkuDbsIZr0oxLH6k0HVeuN755_fUBObWtx1GwdZmkgnxBr23vUlvYKIunkIGrotTtEJVrKIZz4uiXLm2O6iXd7Yl3DUofeV_ke0qF2hWSI7JtlpDC6FxRqJl-oWX60crtcGXhZsmAafiSgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دیگه با استوری که‌شخص دراگان اسکوچیچ گذاشت همه‌چی‌برای رفقا مشخص شد که اسکوچیچ دریکقدمی رونمایی با پیراهن پرسپولیس بود و هیچ درخواست جدیدی نداشت اما اختلافات بین مدیران بانک شه  باعث برهم خوردن این انتقال شد.
‼️
کانال مردمی پرشیانا هیچوقت خبر رو از روی…</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24935" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24934">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDWQv2Ac1FHTqtL1eEUhJS9g7Y81JcLeCXXD2iuhOpVP_XKtFR-__ITWVv7Qu7ax7t9xMOEoL2burswHRcQWpguBwAenZDIIo6T7-fcsJ5qczUTB-p2u2xR_wqWc1zhl49d_zjX3TYpRc3x8KhwpJ916JRW51hqU0IJy5xwvhqUK9E17sTWnl_mIeg33u_sMD6d6RWah9ckzs_xv5DwiT8VsF62Yg2xoOeDkiHzkoKGRiS1ylE_sudj7_lXqqxdv07cYPfoINrFI5ZFxiBikJ_kTfukohjHOd0dI3y8iWfk_x3v3duJCGxxwqC47YfSbhT-pUFbEkgpGu-3wsIg3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24934" target="_blank">📅 13:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24933">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5NnWM_qGVceoE05ENeeTvhZibG84FXxiQzGJOCDZuuGFqHKkkq7vCysYlkbXP27nAyLraxmIZRgULA8bajSsu_bMp00GP0iwBWpm3KHHap8eiDOjxx64b0BW7bl5SF2YVRE420YrNGd2X_ntDdfmb-4YalFBLrs90DUdaqOBt2_O3a8VL5OJXfRLSi7Gkz_-tyMkD8KskyYtPSUXSom2-Xrm9ntz-AnjEXjSgXofuqKCG0uAcpC1aK_fTMU3juEWNjoLISclr2u7dza_GSrXulK8-01UuhD36_SwpHfMSpXI2anB4RjUWzx9xmOmFH8oSpMR9Mge_NbwoM4T8Xrrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24933" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24932">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGMykWRnFUcmqUSis-0COXLiD9FPPwwD9D6EUTzS5h5U3jigFoMPCl0DshwNgqI9BYI2zp5G55aKf2ttr_gVAOzfNutiO080JEgj1IUOdIc3Cc-sOA5qyjxfrpa3tukFnUE9RLFPF1urx2SMIe7DCINBDa3xk43SVLZ65V9IDi3aSnzC8EDQf6rC4zVMSOnJWTsDqBGOWc7d_eW7hljRFs5cT5bfGiHACrnr_TopnFrPJ5Pygs7XOo_yzgG556FRucLTucZClY5tBOiU1NmxTh1EL4pHvztjRIrhH-Pc2kl-YDtYSu0g6nj5lP9BgH4CPDWKRX2GM0w298HFXrFWYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کادرفنی‌ مصر برای‌ضربات‌پنالتی پنالتیای کیلیان امباپه در رئال مادرید رو به بازیکناش نشون میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24932" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24931">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZo8SaE5XPC6ov7xcOz1JN7PbHEKiuUonGP9ksYTl8zF1Hr3zmhJ4fCYS8n8Cer8M5eiMYBDo3tV6xgN5olMSAAZ6MT0gNvg7YYCjhCZbd6B8rtytyXvLS1HJnhjho--acwHO_FJvKMcKX9Bo0Zf_89Kj-0dSTWIMtAyo8mU3y1oJCq4oM3E84liVrq2DHESka3YD7i5BS791F0K_wTCua8FYEk8_WUjwNfOymX-aWjkmlQdNOoN63byKq6wHfDpx_KmQw93AaOeiVgLsdoReI8Crr2KYQ5SRTdXqmfwUtokkBljjkkXaeYQvioXLHHO8Vs897ZXAN_pHmlF61Jt1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبن‌نوس:
هنوز با ژوتا صحبت‌میکنم، چیزی که افراد کمی از آن‌باخبرند. ما یک گروه واتس‌اپ داریم که من همسرم دبورا و همسر دیگو روته کاردوسو در آن هستیم و همچنان در آنجابااو گفتگو می‌کنیم. هر زمان که اتفاق خاصی رخ میدهد من چت‌های آرشیو شده‌مان را باز می‌کنم و برایش پیام می‌فرستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24931" target="_blank">📅 12:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24929">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=pATj3zf-SfkcI-Jd6HBp2ds6JI-LnDNLSuvEmJdKkqxRInr2KESIrHlRR3mWOXf2o7CIwBCzLJ5jMoQYUTLoBvRviuP3u6i95E1SWQ3-TPtZpxXi64lMikFAyD1tLRKOJS_h7JELnLlNdT2bIelKVFABmQG22kUfDQYosh8ngLml6HF7ayXcfU6Xw1pypHom5bt-YD2iVm90IKuPyYId6KLybI8nldaQop0vpA6cdd6WlhzOvX1huxPMgwermtiFat4Ig3ar9XUf1AFHfDrIejmUSX2cRuHzCxT6wmt42YLU0TF2u6OqGVuHROPdNpudnBz54yLAJoz6qkbMSGh_fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=pATj3zf-SfkcI-Jd6HBp2ds6JI-LnDNLSuvEmJdKkqxRInr2KESIrHlRR3mWOXf2o7CIwBCzLJ5jMoQYUTLoBvRviuP3u6i95E1SWQ3-TPtZpxXi64lMikFAyD1tLRKOJS_h7JELnLlNdT2bIelKVFABmQG22kUfDQYosh8ngLml6HF7ayXcfU6Xw1pypHom5bt-YD2iVm90IKuPyYId6KLybI8nldaQop0vpA6cdd6WlhzOvX1huxPMgwermtiFat4Ig3ar9XUf1AFHfDrIejmUSX2cRuHzCxT6wmt42YLU0TF2u6OqGVuHROPdNpudnBz54yLAJoz6qkbMSGh_fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
در اقدامی جالب توجه؛ مربی مصر قبل از ضربات پنالتی، خلاصه بازی‌های رئال مادرید رو برای تیمش پخش ‌کرد. مصری‌ها این دیدار رو بردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24929" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24928">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=ieG2F-q5qyDBBEBQHZCWjxXqjzkX_O7gUMk-0ySNgzAX6r444H4es961p3llS2_lzjniuq2A52g38ucoq86UBPVeN4t1D8HAlNxdJIwvlby_VNxlRAgxrLdQDfSx8fybcybbmdXej4ishzTdnOXEJcr1qbk7QWB4rknxyUIMPZxpMXnokNcpfPH_AVhAvGKedIK5ca5KY7_vbCs32egnAB6FaIG5Q_2ng-ptZ44240yacGxJxLcDWenGkNF8MNZ08wH_CqIv-nje9gz8aEAAp0ioea77f0vhsp4nutKpbEaA_lYnwOtKAN_AsrrILMHPChW2QrDTK5Hjol7cdj__ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=ieG2F-q5qyDBBEBQHZCWjxXqjzkX_O7gUMk-0ySNgzAX6r444H4es961p3llS2_lzjniuq2A52g38ucoq86UBPVeN4t1D8HAlNxdJIwvlby_VNxlRAgxrLdQDfSx8fybcybbmdXej4ishzTdnOXEJcr1qbk7QWB4rknxyUIMPZxpMXnokNcpfPH_AVhAvGKedIK5ca5KY7_vbCs32egnAB6FaIG5Q_2ng-ptZ44240yacGxJxLcDWenGkNF8MNZ08wH_CqIv-nje9gz8aEAAp0ioea77f0vhsp4nutKpbEaA_lYnwOtKAN_AsrrILMHPChW2QrDTK5Hjol7cdj__ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛
لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24928" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24927">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJOLNzg4wMyH3H-qjsHMYj84HE-Dam_qkcGRunBcN9MztwI226dZcsCmokHAqbtTlQ7drUTZG9ZleyiEctau1adDiJxDO5bcG_Jo98PywyHAQwK-JRiPgXH6qwSUwUXncv4fOGuQG-SheC5JG5rffMLcDBuJb4rErnwnpC2Zj0RqXjlIwJ3FDB8CsNheJxeO1qr5iwdETn4C3w3dVn5tQOD10zGgONs6XqgO2H1Ez4-iix9v3nweEM2ZInIfoqA9K5ODfjTy1h-B7K_7IGfU_Dk6mFvX1Kk_PR_2YrXDYnoHW-mFPlW-fCUFNVoDjrE0rxORLkuMzR021JOB7J9u2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
طبق اخبار جدید دریافتی رسانه پرشیانا؛
تیوی‌ بیفوما وینگر 34 ساله تیم پرسپولیس با باشگاه فولادخوزستان درحال انجام‌مذاکره‌است تا درصورت توافق نهایی شاگرد حمید مطهری در این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24927" target="_blank">📅 11:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24926">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIJ000ZGa6lK-Psj9JxAQdm1D0hIZvAO2RswqpQiucnb2A0Cozf7Iw19dw-FJyo83g_kDa1JTm5om4DrKSxychNDvtCl6YGkFimRTrioIX0EukedLRmGsB2PGvHRIZ5UkXrIqWIqACcfhPqjZw8WO_8E6KOXAWM5tiOppGDVEBGjbq0GrGyLsCkNNLlMe9g3EXmkQjhGFVzkU7cIfW0DupxqiuQkad_mGF6jHuJOGrpZXodsNEqxG8_p_JpQ3ZjJ6E6F9c64awHKH9VUYC_S5xxDVkAdxNossvXQugjfPmrzm_y5PNC85Ai9WTgKncu18HrsJLyPfUsG78DjkTKPOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24926" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24925">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knKOXvjzg64yx0NVlHugbvMJgUHXsZ7Krlelcphpf5pNXAjh4AmFAdv0tNGgbEL-h_fUiidfHY4cVJV9DUk2ULU-SB5Vl3Oj1mnrkhqsrKC2JmAqXD1JCjyn_d6CE81B_BotrCMdsHE_2RefALSlIUASFX5KW2ZuaxvFc0M9AfRBROxszO32IykVhuGFY82jMmdlmEDFYWcej0UjHY0DJ6TT-RQoBXYDLR_yn5PltqMsyRQKQspf9ZnXKE-Uxz9OrHhyLIPgB0qszoLlkxZh6leiIXHVyfm4ZAtsAatYEjRztohRQylqJ84jdFFz48TC_YNOMKsHqVFb5wIkp_bMDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛ به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24925" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24922">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEzB-K4riCiWTUtSIG_Q3xfx5pclNyGEyL3ShNJUr9vVJWnWq-hJnx3jcPySMY2LIwvhOJb8TqgFIcC-qtwh_x99Z7jAQXsPkAE08J28OM5EGqA9i8CKqxI_X5keM4_lRKYwiLOos8W_0tA1EnCB-iJq11m7l5382jQep70BV9qMw950Cv9vuz9i1KH5KF_Fd4XOXjT4htYaxjomZ0zKTAaao34ZWXhdzWetj986tGk-WX4fno9Lracvyfb8kASnMnK02husVdgdQA4OlsUN_FevjP0TFldMC1k5gJm2HdbP2OUoFmXHGM2PRDNaXlyHpfjHYhnliCXh-_mE2TGWOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24922" target="_blank">📅 11:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24921">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fq900YhLiQ-r6OoO2FtJxtfK5vr3Zsgbm4-v3Q3JFhxzGEecCVG5uINCb3JNfPYEqpjeDEdWrDss7Ize7_ct0U8cuwKOzSkaYTwV6Wgeidfh6iv9KoN1JQuHyPcvXzDjJCLVWlX7ue0VmLOFz2sjA4XUzhEwBO3gNE5U883mXO66lrEGKH6sDJo_WEy2CUsEmZHa_g5uHlJvduOx2_GaZZEr26Zp14yrPfnMNBLRAkic4l7GIfoLfZQgi69debrSrQyyz_cvyG8d-eV1216wVJVM8C5AhceGRs7CQpiIpjz3L_ZUtKA8usvVPIPlZQSo_Ro3Xr_3tnfUyiKFSbF-gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های رسانه پرشیانا؛ آلومینیوم رضایت نامه محمد خلیفه رو به 70 میلیارد تومان کاهش داده اما باشگاه استقلال قصد داره با 55 میلیارد تومان این دروازه‌بان جوان رو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24921" target="_blank">📅 10:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24920">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv7szkLgs_Ve67N8WjMIiGv6a6k8nQQjM5XpqXn6IfvnhnBROGddeEANq2f0l2nRenguWpYrBcDAnHBNg5QrmJ5kopwqwpatRz0YcworTi_wjTGdhUIdEiT2SkMLAa6-Cjdgk7O_FWCdwCbPQhlYM_GNjeXQLJ9aHsvsrq5d6lpgSOVYoK1a5Dpvnjm0d_Uc9bRO_mMs9TuQ40RpPH4b9AtVGjiI4jqCcHz6HtSCqDrM4QLN6X0iXC_sk8rClzanFVKPuNxVgtf4R2XnZ48272L6h1R34qhGSmiygJW3Y_rvmNVpCxMRcSMAjhwA68ATOK4NdSeIfIAbyJ3IwCfVnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24920" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24918">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJsdU3RR5ZzvjX5wb9FVsxv_zi5wyGOcTpN0wsf-yL8cXP693NxakUHvVKA-K_igPU0w0xtsIYLkPwdSn70khs2Xn454e0RbLnDWzyALqSfSFJ5wRCHswaRBJm6i6HQn2_U469JlJefE6aWF52W6bbGe7syqT6RnQHE0jl1zPoZn33nwmStJ-Daf253Ksc8or7HnQn84G1gdyqtuTe4Yhb3RQUQM0UudLSoymxx4idQ33kBMbDitmBCT7mzykv34LVV5jqfvNBMVgzGveTTPD2kFn8Hb_VHuSzGHARRTgBmn-49X3UoVgbsQgR7DDlOQ7CFePmoDwMZamvG7yGyDjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24918" target="_blank">📅 09:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24917">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=e-iQWdbiV8yvwg9on0xSSR2whCvV-j8teJwX8bEn704nk3qS9NKZvkwFRD512J0wiKusH5gJCQiOM6h4zROXeV7MmFEt92DN8FndclauNHLf-TUX9PN5YtU0MiJJCtMyJG-F3SLeSA9E7E3LU2Pgb_xL5rc2ECZjLqpgahc6gZ_tnbeBMeiFureQ2No1PPNoqV4EjOdZoI9_4enMbcnJQullFaVOUR3fLFh_tyxJjtguneyaGd_CrRjUwk53x5nt6dtTYUPa_rKFsqPm7MbUy5bGQ_jgqQB_Q3APzDtI_a40XMqG8AiYr2Hm1Qg-DsrCYnGb0Tyjn7VCa9Q4eH6XOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=e-iQWdbiV8yvwg9on0xSSR2whCvV-j8teJwX8bEn704nk3qS9NKZvkwFRD512J0wiKusH5gJCQiOM6h4zROXeV7MmFEt92DN8FndclauNHLf-TUX9PN5YtU0MiJJCtMyJG-F3SLeSA9E7E3LU2Pgb_xL5rc2ECZjLqpgahc6gZ_tnbeBMeiFureQ2No1PPNoqV4EjOdZoI9_4enMbcnJQullFaVOUR3fLFh_tyxJjtguneyaGd_CrRjUwk53x5nt6dtTYUPa_rKFsqPm7MbUy5bGQ_jgqQB_Q3APzDtI_a40XMqG8AiYr2Hm1Qg-DsrCYnGb0Tyjn7VCa9Q4eH6XOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24917" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24916">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcPTO40ooxUFPEq3pUFO2g5wcp0lyjdCUqUYiijBqM-8p7mi08YcOD9GAtGt3UKHmE1rXl5jgxik9VJANetOS6Vvb5YzaOGeKcnZBPr1YNARYaztLhMxuKP4uHdEJ4GKJm1_szygmZZSxMfqHRJBB55inYm4Dcr6zy8OvdgxJL-tbhiEKHwTlJxcEB-f473HpJNgA36Pw78uvL40-dRUH_Seyhuuud5Yd3c7fWzIm6tBVp-DgmQ01H3niSqb-Zne0EGTr2hLCwyzEFoxm64m7wofBjCFCp5T5aDt3sDEIr1Ve7qnqThUleW9ROL057r2D58bwaDBr_QZJah4tMhR8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مسابقات ⅛ نهایی جام جهانی مشخص شدند؛ لیونل مسی و یارانش به صلاح خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24916" target="_blank">📅 09:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24915">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBK_z-6LMCO4UZLopKPQkrBnO1zUF9M44kvosYhcdygCi3kNBNl1NyULocIAWuU_1t3lOIPI1_XJKayWAMfN-iZQGULHi19LnhcKyp9HayBV89KODl7k0SToCb0EphluCp9gddp2b5W36JLzQTOtZrEib5V56EPEufcUoEZydT2YHnWqbcjr09Pf_Cfrbo29K40kchCKlvAYB_uICf93X_2dLrIc5lLcUAKcnk-ij4-pDCrOXq5oEGv4f5GpyPQL_hzjdJt_p7Zl4PP2zp2LqF3j6JKqKfhqJUKukmSRqye3JmC2JeDJHZ2Dje6LWMf7nGcPgciT-TkUUiagMREBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24915" target="_blank">📅 09:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24914">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=nXZijH67SVQFAWz_1o4yiKss-ASHqRXWihiL9RpiXlFA_65x210izchrfstMRd4VCp7BO_WkFJo3LLfZUaiiMjNJkxf9ARksouYS-xPbUgYldD9qGDE0sYMBHRcnWUoRhZN9S_zBBL37GyxfaFWkq-uLuH3ziXusyeMoHmu7hwvq5qXIRiPLzF6HsRDIi8-Pc28GmR2yhozU625lx7-CHMDIeN9v5ESgZ2RpSIn74nnSI26bfC987GaNO0_Wp937zrSRFNVI4E3PZUpXGSyHRctIpLIafN8FD4oC06cSDAROm0z-h2DuYpYBtZbmHYFk2LobUeYB2JHXsCV5nMPjEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=nXZijH67SVQFAWz_1o4yiKss-ASHqRXWihiL9RpiXlFA_65x210izchrfstMRd4VCp7BO_WkFJo3LLfZUaiiMjNJkxf9ARksouYS-xPbUgYldD9qGDE0sYMBHRcnWUoRhZN9S_zBBL37GyxfaFWkq-uLuH3ziXusyeMoHmu7hwvq5qXIRiPLzF6HsRDIi8-Pc28GmR2yhozU625lx7-CHMDIeN9v5ESgZ2RpSIn74nnSI26bfC987GaNO0_Wp937zrSRFNVI4E3PZUpXGSyHRctIpLIafN8FD4oC06cSDAROm0z-h2DuYpYBtZbmHYFk2LobUeYB2JHXsCV5nMPjEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌وداغ هادی‌حجازی‌فر سوپر استار سینما و تلویزیون به میثاقی مجری صداوسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24914" target="_blank">📅 08:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24913">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=kA1ln3Oqwsx5PP7fHYPnpuYIZbW4-PdvGevLzfcTpbBx_9LDJM0dqF883AelD5-fSuQjybjiY0yCmDqo05QD396e-THJ3xKTpKBKyBsLPpql87Yz5wxvlP_R9am4-tTI-pg57cH1Il6tiKX0AhCDupDGmtHuHCSFGMN1tvVxO8ekP8P2EjuH50CXx__rDA23lnXE2oBF2up6P71k7eCLFe7RlNGPm984K2jsl20WA_vB4XdCyA4TqczRKrjnZ8ExpS9c_A7g4K76YpakeBz2VvHqoDCemPbx2SjvGdrLuzVcF8vGPRc2-tu3cdUx_bChj60ePcOYiqdorqOrgA1Alw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=kA1ln3Oqwsx5PP7fHYPnpuYIZbW4-PdvGevLzfcTpbBx_9LDJM0dqF883AelD5-fSuQjybjiY0yCmDqo05QD396e-THJ3xKTpKBKyBsLPpql87Yz5wxvlP_R9am4-tTI-pg57cH1Il6tiKX0AhCDupDGmtHuHCSFGMN1tvVxO8ekP8P2EjuH50CXx__rDA23lnXE2oBF2up6P71k7eCLFe7RlNGPm984K2jsl20WA_vB4XdCyA4TqczRKrjnZ8ExpS9c_A7g4K76YpakeBz2VvHqoDCemPbx2SjvGdrLuzVcF8vGPRc2-tu3cdUx_bChj60ePcOYiqdorqOrgA1Alw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل‌های‌دیداردیدنی‌بامداد امروز دوتیم آرژانتین - کیپ ورد درجام‌جهانی؛درسته‌حرفای جادوگر درست درنیومد ولی‌کیپ‌ورد 120 دقیقه بدجور این تیم رو اذیت کردند تصورهمه قبل بازی این بود که آرژانتین همون 90 دقیقه کار حریف رو با 3 4 گل تموم کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24913" target="_blank">📅 08:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24912">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
👤
خداداد عزیزی: بااسکوچیچ تفاهمنامه امضا کردند اما به یک باره همه چیز عوض شد و مدیران باشگاه پرسپولیس‌درخواست‌های جدیدی داشتند که درنهایت اسکوچیچ اعلام کرد با این شرایط نمی‌آیم.
‼️
دقیقا صبح گفتیم که باشگاه و بانک شهر بشدت دارند سنگ‌اندازی‌میتونن که اسکوچیچ…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24912" target="_blank">📅 08:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24911">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAt6kL2cyVFHnkyBmh-FdpFQi8EQjS3wmiZ5cIP7Qc95azTBROiNSMFS0GW1GVWSSGJAn3jrMOlzE9dqdF1odzCiaAAUI1Ksyhm5kDLDFKwY6jhYdqQXyvAJM5UD8DIm1KjCVmKQfjR9pU2yMdeiRzSU5FSFooeLSUEa7B6TvY9NUpJ3rvGUk4IdkALP4czcdJC5S8pf5Ifo_FfHcVe-Ya5YT8cSmgJGJpnfycO-fGNYLSHfqzlMNsMHyOp8lBg4pDzxMtI7bLnpzmmsOwVR38a5ULsr8h9InT7Xz2o3ZkwAqy6R_bapc2CEfJUUjiOWj2lYWIolYKU9vpQgek-tEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دریک خواننده‌معروف‌کانادایی - آمریکا رفته پیش‌کریس‌رونالدو و بهش‌گفته‌روی‌قهرمانی این تیم در جام جهانی 5 میلیون یورو شرط بسته است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24911" target="_blank">📅 07:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24909">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24909" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24908">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxhGo5FR2JKWzl3CWp1cQz2cHtOxUoxiP7BUlKtptSIXV-SpMK0HLJMOy178tn8hhRV4Ena2L2EQB1gUDZSI5xNbfn6ghW-kG4gdPL43qWg9RBQkZFSIWlUKA4eZMxzbXyvOfAfc0G77fetQjRSzmp2P8uzJ-uTqFiNqSOypeJIVn9888KiQ_VZA7wMqNfNLpNHo3A71B8F37Ur7pnyff5Re6qSPgN0e1gjiqMKRPQs3DKm-bafD1mOVByzi5JUb5kBMrmCAX3pZap91z7hI3OGBF_xnLY7kDEGCEJ9GO5p1_5kumwaiNBF1Y7-J6okuQOJXJ_qtGCe4JwkJmrRCbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24908" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24907">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKJ3FpsSZrDEF0t-6oFp-yCQLml81KBghzx88ZJZhHAJlrvuBAwLU_DSOeC2DJv6Nml9kIHMYameLk-fckJPFM3rFh1x0Uh1ndSkTIS94UgBf8RdxAFqJFtRYAfqBVpd5ubaGpUckueycM3kl33C_9MEbwACOaLzjLQMwXbs6JSLL6oAeIx02XVShaBtqKJsTCneQpuR98wX0A52kfus6GIROp6_kirFtMYWuc3-20bt9Vc0fPmOGguzxYMrEGZczXzpVWFL792mB67PJqAuv5DScyFQ3HdlfGOIW75sy85BMYQ4gMqX13yfC2f4SitPSc0tVV01Ft4qsGptLuqL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24907" target="_blank">📅 07:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24906">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wlxrw45B43s9p8nDYliJbvAIULjh07nxd8Vr4N73_mmKBFytxjpTKMCXRZk9KhErSEuMNklcOVsnyQqhYGgaUzZERI4s0onOKsrtMYNpRxFKOEj17ySMjEfelXXoooHv1juM2BVPpj8CHklomXCjxvNQNBosbQezS9lhtBrjJfB19ls1cPak6KkRSJVadFO_gPiOVEte0wwHJVJ5KBPOHts6Pk8Od_IkOFTsQZtSFr1ojzquGNpDsFXQAKKCy9tBY7GOy1RNqGQJmvbFBL9Sehm_Evp2cSt_l7Vb62Cn7_cmQLsGp-BpgPv2GSvndJD1k05OC2dvTA6t1aQlsoTVUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/24906" target="_blank">📅 03:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24905">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAOz0IdzKsP1ERmDvk3VVwOZI1v9D-rjqSIMGqz0w5BOG_kdvgneQYCReZbat43tBJxXp1oaS-Fr_dZNtdf6jHinZqeC_YPwfNI574BK0Jv3qML1ZS9m8joyEuVh0T1MaJBxVvEnnHa4qlQYQrsuUJAvAxLZzHAbxVDMWFrBuPHhaabQls1nVQJ61_DOmNmtC9uEWsCNe65Zgp1V_fHOv560Koykt2-ioeZhzHNYNknfPvXcMW_S08Qcn8TZaCIz-VYtyewxnBO3YbBKs1_Y12ahVZdPN12sLZFrGrc5AI0qy748OVIoHQKB3-jrWfOJj6Je_VehK5sqp046TECTQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
گلزنی‌لیونل‌مسی دربازی امشب آرژانتین
🆚
کیپ ورد در یک شانزدهم نهایی جام جهانی؛ این 20 امین گل لئو در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/24905" target="_blank">📅 02:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24904">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=P6AZ59qS_4ua_qp4O6DFBnsrLY_B7qdAu1Nr-0_40XgN_2AgB6yMbJ393c5XG_iHWdn2McmExvRIdNOZlq_e2rvPFx9vtouvSP4xt49x5KRSD9Gf_vWjnv3WifzCerk0QGm253o3gwYnEuqJBkeAHSS_aTdbdJjSN4wQj2CKwXL0iiLfKCI9GNTPUScPYoQGKT_5U_LvUVbsNfEEHi8hMSqaSlScU5qaoHn7QOQ5oFrlJLED2-jdncKK5YkxBy1R-VVR1X2GwrPlv0jVwGo54J4f4eRF1AM75niethp5S-dRfoWtrIWsVeRTx_WwYyJFgSOmV-ra8d0Vr9X5jRjd9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=P6AZ59qS_4ua_qp4O6DFBnsrLY_B7qdAu1Nr-0_40XgN_2AgB6yMbJ393c5XG_iHWdn2McmExvRIdNOZlq_e2rvPFx9vtouvSP4xt49x5KRSD9Gf_vWjnv3WifzCerk0QGm253o3gwYnEuqJBkeAHSS_aTdbdJjSN4wQj2CKwXL0iiLfKCI9GNTPUScPYoQGKT_5U_LvUVbsNfEEHi8hMSqaSlScU5qaoHn7QOQ5oFrlJLED2-jdncKK5YkxBy1R-VVR1X2GwrPlv0jVwGo54J4f4eRF1AM75niethp5S-dRfoWtrIWsVeRTx_WwYyJFgSOmV-ra8d0Vr9X5jRjd9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛ شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24904" target="_blank">📅 02:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24903">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyI8N3IvVNJIOJGThwrN0GArlAeIhqeQ-xQmKBPv75Ft2Yb6tfKDB86K-y5RNxt0JC9N1Du-RsyIRu3DREG6nP3oGyIcZBcU77bKm4sAISDLTKpwjEhkNGWDZB17FTE9Q5r37A78x1LiZ_bbyghO97RSoMnQXF-RuHgeK1h7qN3S9OYEKK9T7LroX3zLW07a6B-3CMQ4i8eKekQKG0PN7ASY6tO7CQvcikDzzS4bgJDGPB10zwiO6ETYAB_W1em3teW8HZQWTdUVrJ7nbLjiw5v7CAND6Bc9XLraf-81F5MW_zurnBuZyOhuk5WOOAttIKxizLhixP8C48xSaKsFpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24903" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24901">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiZ7m5yDsCQjvP5P5bOUYRfVIIt5DuACmL-lPJsVTQUKsrTkagKutDEZJJO7i88fXNRTwbnIs2GqF4qOnKcsdxhMsUirdfPEhQDDainXsxusWqRcX_8fXfRwkYKJsYnDNEBFKRul_MN2bIMneh5-63s_1CPzCqiLWLAwfqRUg-SW-nU_GQcM6b88lJdUcEtm9q1-r4_uCJMJm--ydamRSgihGbkzqxfyoEhqS8rF4w9Ga7sYZT3bfwBuYpI8wEoIVJQhR2jSrZMnJVi27AcGPgVHkLrRuI6VCZxyjhGT38rVjK9mkLFMgFPmUdAmN3y4ynDWsKxcRuGQxvXC9nhaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24901" target="_blank">📅 01:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24900">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZpNE9BU3wOeJCt8bEC_psDMza6Lu9XFz3oFCZA4PnlauJDlkryr26nZ1eOmeUE7GWh0xByt-2Ha189_SH-9UFG2YFXpc9SUBPVWMrP8vSJLf92eoE30r_QBagbOqJ0XEgYEexJRcE0R50sWNfMRqPgG_uNbjws42XLmZujWnw_9U3w4HUPng8gONcVaBp6vw5R37MHb2d-wSFQSnnI594pbcqCZKdOE-8IcB7R5NFOSxg52vPPTPcAJn_sV8ve0xWlcYRroN11AGBg17QME3dhfGfa5s1JTwmmTPi-sJJUXqWaun4MlGyo4_gS4d9DcOddvQ_mZpUMIcEVT6Kh4Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24900" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24899">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knGp2Ms8SMnvHvYqG_VT_CTVcxC01EugFAzZbkPMf0fArMdtA9bo-uTLKlUBbNUTT5Pn3CVuWWvQr7b5ocZp4aLcHFO8xnTQstxWaUYOfeHREWlmjLED03L9Tqh6NLhcpXCQtg5wuF1hBEibmjmVl4pjSH8mE9HFP_WIz5OPfNRdju5aIu3W7hDtjJ3KPC1-2D15V-9ONH81WmJogySy6xUqmUJLZpYQdFj95wJWfYmdLrocESAJtE-CGWryh9m3D50c-2X9N6NM43ic45IoX7xbmAU9_xPW4SWrc0sJfyvyLbL2EZTypMmjYK0V25QT0gfyrHqwyC7kW7zwHPm6eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌کامل دیدارها‌ی‌‌ امروز؛
جدال یاران لیونل مسی مقابل پدیده جام‌جهانی 2026 و بلافاصله آغاز بازی‌های حساس دور یک‌هشتم نهایی از امشب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24899" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24898">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U87-Wl-Dog7-xPN65WjkAZsaRr5kB1LJ3aaNxFYdlU6zR_UreVH9luE8to9gBvupg0mXnMp9_hOJwjruOu567h5Gf9FNKK2fvnUaBtvUb1wPKweT1U1EuzFClOb52U9UKw5spK4Ood8TouANBU47R93BILXHGuX6iTIMI7kxlP5zjs_3J0u0msFxJAswCkuKpt4ZXwXrbUU8mJuO_C-LrJ2192_mq3XwciGbaw7F57GaLC4lPRqUkfLD-NMaLaXLspE4U8NdM562tPqPMsol1OmJgJIqbHhXzgCiS1ZXVVoHLZxZeQsFy4P93dr0ELiOT14DsW7RrDyn3ri0GaaL6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد دراماتیک پرتغالی‌‌ها درجدال برابر کرواسی تا راهیابی یاران ژاکا و محمد صلاح به دور بعد رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24898" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24895">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6HaXruze_q8tLIZn_I9-Q9Fghg3fJ73sRSHg8h7S3H9COgmhuMe7jot-e3Ul2q_CVMbRGOTKFR3aCjaTRIJrW_mxXloqAMLgjZuAXeKi_7BSFy53ZlIzw10MATdEe3pQ3ZpFHEe4xH709tmzoXzglL-OUplOZ1TCWLkhASmDxCkwaBygkroyQOvpHYXlxtrP6pEqy5zO5uH5bZ0WXo3k9QLfIbI7bvAI0LKs1YA9E74S6Nshh4Wxr1CPVkMTc5FXpkjJWi3e6fsb8QBnU35pZbzbzXPpKBdO62sDwC9oLWcCmnJSw20FM6yc99XfbhgyCEIm3paFXyLJeNG22Zxfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دراگان اسکوچیچ حتی لیست ورودی و خروجی خود را آماده کرده و به نماینده و ایجنت ایرانی خود داده تا بلافاصله بعد از رونمایی بعنوان سرمربی فعالیت خود را در پرسپولیس اغاز کند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/24895" target="_blank">📅 00:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24894">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=lCPhd1PGkHx-rAP1Coh8oDJC3N2a5FLszOcsG9zzuhrR9Pj1ixtHCd1HqUNSXX9AbFYOfs3VSKQehJCOw-xeftjVB6GhCbGdDdSC2HdsMRcLvNzbBATFs9mwm_Xnw-dqKlWgP2yYB5WfDJTekEQCbOlhILVxm-3bD1_VtJR0ZC3CG_0vdffcT8t2cgltWD3B96tuSjHVJN1kuwVw6Ie0-U8l7XML52tI5Myrevb17rpRHR8pSrNmILV-1des8uJgTEhRx991cuENFZIA64ZCBpjibOUo3hYkhBq1ICV3e8RPzweYcYzPyhDD0_ZoVDGboFV-oJoQtHHrGbjjoLHZTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=lCPhd1PGkHx-rAP1Coh8oDJC3N2a5FLszOcsG9zzuhrR9Pj1ixtHCd1HqUNSXX9AbFYOfs3VSKQehJCOw-xeftjVB6GhCbGdDdSC2HdsMRcLvNzbBATFs9mwm_Xnw-dqKlWgP2yYB5WfDJTekEQCbOlhILVxm-3bD1_VtJR0ZC3CG_0vdffcT8t2cgltWD3B96tuSjHVJN1kuwVw6Ie0-U8l7XML52tI5Myrevb17rpRHR8pSrNmILV-1des8uJgTEhRx991cuENFZIA64ZCBpjibOUo3hYkhBq1ICV3e8RPzweYcYzPyhDD0_ZoVDGboFV-oJoQtHHrGbjjoLHZTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛
به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/24894" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24892">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SA1r4IZRx2swZqCC6s4W8HSJq6yjRbduj-dAYWWEwXbEfUokHhl-yVWvgNWBF5SsesdU2xbZ_S4e1yZPgLigxoxHABWTNeO56PKtRwgar263m2UiVQykF91dg9tVv97gOBJknkFcBRREpSma-LOR8bElycFIONYXc_0Ss_iwL5tHfT-qP2AXUX4yZQkjAlLl9CFzpTXzGIn6XJIGiYfYGt38_YoiXUTQlwhwjUUmfKACYSlVhK5UOVx_yzkwBUJ4tpJvzZ6yBzCncL3GQuHsSfiO9t20czs0DFPEXQHZCosbLnUAraz6I2BbMBTbPMzmjTQv408yEZHUQjPeD_x4hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OVtqcKmXXNNflLpj_Lw93WLs5rIHggqsNUdE-yLn65v01zeaV4rWEs4BTjlrGFLTwaAs3bSPc57HZct6IomCuZS_BOCT0kuf07NktG4gGn74H_dolyRvWVZMBzHNHAWm-EQw_4yquca8xidDA_jjSHB2h4Y1PycLXq-L0bophsaiokOXKZ3yZhaqs3yYBkSyJA6e2j8DHZzwvYmscxZVzqXY22oAbummcT1SGfVBRlF_-IyvZ_uVmbnAmnumHHSdMCgir9W_arIIn3t7qcDZFCWJQ-rAmFYYGCVuhFc4-7FNvtwYNVDypsdiqhmWoHUXO2_fpAPx-n-sbB5iEAJKxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛
شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/24892" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24891">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9CYgYXpE3Lz_scN8oZOcwCCuNAZ81DfC1X8GwujD-gudY-gjGyb1mtsvI6CKHH9SdrRr49LhG8wb8WZOhELkkEyDmLRH2pk4qCKOjmcJ3CoorNG6zglM7w_dO7K5Vs7EjNURqOrUURLFkMN6LBnC90HnpD3x5bIJUDwA4SXT2gWfswNWagU0ZiLrqxec2tLEXRxi-N_YPZvcnnbXoQokoDDrxNjSfEacuwe8keVt1WyQPz1eg9V8mt93ayj4yoER9gqP7fpH172HDFwXrrjW7eFRsj5hxiy4MyyOKbwY9jfVqBqzDSM99pLSGsJmYZrqLI2atZW7O6g9uQwwxb5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هواداد تیم اسپانیا در جام جهانی 2026؛ لاروخا در یک هشتم به مصاف یاران کریس رونالدو میره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/24891" target="_blank">📅 00:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24890">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-gx5Tq5G521pJnxAVDo0WhXFAAg-UqgdXT1IgWYDTG65TJY_7IA03X_qX1GUU5CB53c0rhBvRuQzJa6kiyQFuB7lA2Vs8nIgJe4H0ulyCC2QTxBYeB8bk1YYCSbHiIpFyA39qI8MKYFvaYjBfY-Yjb-31lYcxZoVWI686xhL6Hf4rRjFhzNpGFphDyL99VQdlq5K6ZcQFymqe9oQwX22c1PIHCBnJKiwoa-5exsKQ-MH3sUaVgiUwStllNXZCSycjeTyHlnsxyTrBin5LHWdt4vPe0clPUs9cv_QT_-pxWFmtWbtHT599f-aOQ-A2Hg-cZT3AI8d6jOIB93C1wBpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/24890" target="_blank">📅 23:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24889">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7AqvQqQBXhX4l2PgzxfRjg0Y_p1hFZUDnB-__FQR2k7Bwf9Moyhv7Q1i9Wae4rlzmGOX4rbum8jM698xjob6ENSmQLKNbcVPVTBOc7VFwrjjhMtXLqm4PEHRR5C_2iJmn2dy0y9p-QJKDOKJhfWCLtXTpQFL7Fu-DWIZkUkwsOxpZI76HRNIopr0w5xYmypLCPx0whysHBtaQ6NhEdYnpU-qbjh_BHc29VIRcJL04zeO9Zh5pU0rsRrB00f6CZCPx1OsNwPMZ9AhXoVivSGlTnEexG9-v5qz83uGq2H7BZeaGR7sp8DxzN2NgxbEx2k2JTt86PsBkRW5wUv12H_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/24889" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24888">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTuI7muY5ljNEkG2k_z2f5q8G3MPJ2imA2g9WF3X7I-ulmfJWfYVAl_-rRoOLEO_RwDREiSpR2xDfel6zdqOwHri8yonm6YyhMw4myBsWWVzRz36Qu9XgA0b5u5HD0abdGFvw29yOGaM14NED0l2JC8thQoXfD3ThAflKjP7gixY6tHc17JDncDZGDjhzTbZId121yTCZlz5iQafcvn6gJmPrZEcnSyD46UpgEGXPzuKmyzMgfyXKs2mGE0iDsoZt3tMFZVNNKVIC0yUxv0-F_0k5YP-eTaAMso005KhKynGb38sVadNBTVTp1mWtvz1BgevrMJu3fmD29bQLGyFuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/24888" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24887">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPEW4ewIO5rpW_WT4cZFvBFrrH-mIcYfSCnwWwEsCri1q12Blma-aycQCx3lTf6S7f3FB2P35vAI8tb2Go0o5z-dbIzwtcSO9YeEKoFWRqDxTBXsOnB855kVZB8NaxkAhSRClMm-i8y3uW31VD9akqy7bpwBH8ei96uqdwJU9l8Pwco9iIRMzSW7Kpx8iacg8htbtnsfyWGxGXlib0GLaO2Ln0gu-hwVeac9aF30cgGOyXWoeax-RQQ_wA-Qo8OoL1MMBtulGKxK8pAVqm4J-ptrwkIArG2D3_0oeM5bA9tpE0XafZw7JmPF1wx1mP-qf6j2VIoNbY51fwlWoVymDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/24887" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24885">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FciE2kq4vvPGtcC-BhAxMf-Bb0e85B6CNAEFEmonXJ2fOaX84UeFfGRHyBpxsNQ_ULaAtfH-wrgPncbT8t9AbBYZy2FNX7hpV-YKTqKLjZ5LmmXQp-hYPAw-1uuFKyknDMpzbiAJc2v3B-uNLQZyq2R4H3rOZQeakLpP-fpMnMK8zgONjEiLmpd3N1sc-SuntAWMy81zL_SxSV2aNTfn0_AEB6kyWFKvrFMIw3wgg2tYlBDhOuR-4J_9m5qWHypCFWXWni_hGGYhP-qmJQqq51udkFrQ4vS5ggssO_OATC1prqA6215pKQBKNhXgTtfZdFMcC5Ga9LCiHvAzqnifJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق آخرین اخبار دریافتی‌رسانه پرشیانا؛ وکیل ایتالیایی باشگاه استقلال عصرامروز با ارسال ایمیلی به باشگاه باردیگر اعلام کرده که ظرف دو هفته آینده پنجره آبی ها قطعاباز خواهد شد. وکیل آبی‌ها در این حد از بازشدن پنجره‌مطمئن‌است که به تاجرنیا اعلام کرده اگه پنجره‌بازنشود…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24885" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24884">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEZYQX-RoQF4JckxE_cwLTe7STj6VMiK1ld5vBpjERaDGiNd_8wmoyUqUw5S4qsId7Cdl45M5FTrwxHyJ0u3hPbObISwB4xBkCE6vuh9tJUczkNlcKvbkfoZ3vqxHyu9CqycVBDlQLc3iC2R0WbsA6UY_5y93SVr2-KhzBqH51H9QEutW-rIihHd3CIABQTKY-h_an_GUfvyafj1oJ9yMS91jTASLqHRyXRuunWsh9RvT9r2lSmPt17PCXsYClbYjyZ5iDxvMQkN1u9IvnN9Rifv-xOJpqO1FUp6JlaCTvSjkMlXa98JgJnYfZfuLNrvg5I6E7gD76NjHZ4FexV0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24884" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24883">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=ht50td9ntBd3NWMlu6RIsJ7yokxjV1LfX9-DucI8o2XIjNYhBagD6Z2YyLyXVyoNAGUgZJvxFEfviSF361bztRZmu3E059BFb0u6JXX0tyRs677GScKMoRp7qIrsykgoE7BnMPqrD_1BfHw2soto3-TAn70kGIgqGQcFB0_vf1vFBm4A4KMhrHE4-2gcvPE0AWzOV451GzjTV1qDhVshIcZYp3G3B7aooY7zR-zL8pCmnpOiU7joiXWv2JUBSLMjOmkN7jb2LotumnHHGS0BnJ-z4qEdjW2YO79QhVZq8F4lKZiqWy9zrdn-huGMd27s8NcVj2GSUq6T4Se0fZIDSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=ht50td9ntBd3NWMlu6RIsJ7yokxjV1LfX9-DucI8o2XIjNYhBagD6Z2YyLyXVyoNAGUgZJvxFEfviSF361bztRZmu3E059BFb0u6JXX0tyRs677GScKMoRp7qIrsykgoE7BnMPqrD_1BfHw2soto3-TAn70kGIgqGQcFB0_vf1vFBm4A4KMhrHE4-2gcvPE0AWzOV451GzjTV1qDhVshIcZYp3G3B7aooY7zR-zL8pCmnpOiU7joiXWv2JUBSLMjOmkN7jb2LotumnHHGS0BnJ-z4qEdjW2YO79QhVZq8F4lKZiqWy9zrdn-huGMd27s8NcVj2GSUq6T4Se0fZIDSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بامدادامروز دربازی‌پرتغال-کرواسی‌شوت Cr7 به جایی برخوردکرد که شبکه 3 مجبور به سانسور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24883" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24882">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrTRdAJShz2Sg0ISp6_mIQZRTO_itQ6xbhJBdM2PA7iFYU_k-UJTdT9Xa81UhHdgkRa4pUa_kGkmsgZLVQbmmj9jQKLJXrftnNfPidyztymI3xeeTA8VOzDtn4_qyipmfusE2rPR-MEf1TngS3PZUlYpMVZ08kiOGJ9BdEAbsTX_D5xXh0o2XZ1Fqikt_eGEuBY1oSMJbCTgU95_8yi0L4ZRP_8n7thSsx2NR-wEFPZyfZ-TkLXJ8oKNGM-lUJQV_0NOGwZui8LhK0SWCS4HENnkUX_TbL_5RnWetVxbgEiWYPic9FrBuWp2tsPWqn-LP2KCskEss8vAH4FJjX3cSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
رودریگو دی پائول:
یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24882" target="_blank">📅 21:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24881">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPH7pMo97IXgaL6byKGk2cDl9l8FSBUFg7MFcvslxsAsLDrFtj1xd-dzmdS486lHP5jzeDGpD7D1LMqN5urpj4ycqqYMumNmI6Sb-qgoOQi--n7Dn-vz6yl-lAgp1dU82yRTtUe9egK2lxoxhoLY4RvV0RSJq_Uq8S1_wxnImfOo2QBKCTijOF_LWgrjsilvyA0b3b_yL8rYRNlV3MiS5_-wIdxcOCbwTxgMcDplhF8rWkSYXY37hqdaRYV3e2nweXuAkpWI3ka83niAIFdSDkK4K_s2Jjg9BCwJdG_zpN7od6RXSbDs2AWpcAq6svNkZxe_593sK_P6abotAEQqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی داور دیدار انگلیس و مکزیک شد. به‌امیدموفقیت آقاعلی عزیز در این مسابقه حساس. ایشالا خبر سوت زدن بازی فینال هم منتشر بشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24881" target="_blank">📅 20:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24880">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crVrGn_7bBkIBElLpo3Xt9MT725TfiJEFOuDjKgsxcuqtGIQ8Iuu_AGa1xOEQGxTezMohkoLU4KlBl6MYFogAlt__yDHOZMwN8AhsBehSrRe602cK6edi4k1lZJNS2WMlMZMLLEX7X__3LBMuQxvwiBf8CfOs7oq0uvgOnfBEOf3jC8BitXRaEoOxJimkHbVPKnCl3RjfU1iot7QY1AqIjS7BYSLiRx_2mQyWYTqkAua5vWQLjepxIAbiii5QBud6eD03S0WkX0RrQ61uQOjD7oPGMopQAVJ86xeCAsu3iYiZ4kqaAnQDIQ6TmIlhHzGA4BQ2wnnQftQJRymuiCRFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپهر حیدری رسما اعلام کرد از ملکه پاکدامنش جدا شده و دیگه رابطه ای بین این دو نفر نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/24880" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24879">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9736fee745.mp4?token=TGNQ0F4ksgdshi0Yq0EYpjnI065OLGociQzz3UbnyG4q8Cv7bcv86E21MS96gy3FsiCZSD9wO7mCU9QeOo8NNyfJ842iVu6ki8KFoccbPR02QIlMuWluCEiuzixPeOSLyMm46U3MrdaE5wfCk72QlrZkdOkEKgo48cZOOWtlEM1t2Uew_o2yFiFPTCowf1pU1lv_jgujy-S22FdacP6ZL6Z-VWyr9dGDGPE9efTjbtTUZ7bjF3a3HbhrPjZe-wSlUpf2TJOHZ8qaS2HLamsePdlLryMnXKNZfwXKmwgeIOU-MtrCQbpvd4qQ5QnezK5fpXuPhFQuwWbasR2QNnQb5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9736fee745.mp4?token=TGNQ0F4ksgdshi0Yq0EYpjnI065OLGociQzz3UbnyG4q8Cv7bcv86E21MS96gy3FsiCZSD9wO7mCU9QeOo8NNyfJ842iVu6ki8KFoccbPR02QIlMuWluCEiuzixPeOSLyMm46U3MrdaE5wfCk72QlrZkdOkEKgo48cZOOWtlEM1t2Uew_o2yFiFPTCowf1pU1lv_jgujy-S22FdacP6ZL6Z-VWyr9dGDGPE9efTjbtTUZ7bjF3a3HbhrPjZe-wSlUpf2TJOHZ8qaS2HLamsePdlLryMnXKNZfwXKmwgeIOU-MtrCQbpvd4qQ5QnezK5fpXuPhFQuwWbasR2QNnQb5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
وقتی‌قانون‌برای همه حتی لیونل مسی فوق ستاره تیم آرژانتین هم یکسانه؛ فقط خنده‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24879" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24878">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKyZgK643g3DpXgIKeJU0rZiEjrFraJ9o7KBLu28tV3f0BQNv0KxdyzKLfVYZyLPUWVLzP0JevFvqq9U7nE_VrMwa5C7WIXbDjhbcml3B5AyifUxAhTODMdm73MZPlvTw4s7bdpqHsf-V3OzHhy-fuNf8d99LL7SF4zWVEJYsI2mxe8zJnzvMNDj_DyOZhiacFEgDmU9cn7CFS3sxRq_e4rQBw6aYdNbf7ajCmH1_wi0Zgxo7ylWHllgx8DBPoBEB3e96TK5j7DMI-J6i2C-hY4AKZz9R9No-fQ0KNYFKT57V_3bDj2ub1vTbidlGkIT9WLvVK3i0aBiXzZaKbNN1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا
؛ کاوه رضایی ساعتی پیش با حضور در ساختمان باشگاه سپاهان قرارداد خود را به مدت یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24878" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24877">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/459003d30a.mp4?token=Cvf2oaHj8eL4SsQnDWaGMqSmeOVH3lsVb9jvQj3nYq2E3oWX17wRaHKFnWT6ogPs3T9wf6ETgsORDVUl5NNX8ptM3_O1-om0nX77Dsk1O0jtbXK_e7QkxXkY7Gy0WtjVZE9dlpGRFmeoH73Cd5-gT8Pyqy2DWgNHvSGdL977QyOTh_bFCl54PFYHwlMBN5Is0iMeczTyoqJD8X1Iiwr0lCoex98Sg6I0SvA6rpGdhEFOAHKJnUD0dq2dkpmnCiklFjmWDMeJUCQzdMWvrw1Byj0-QnovOh-tL6QhGdGsGZEb1DFH980jkwVGoBgLogkSBCznWir0HBQcxnzSviPZzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/459003d30a.mp4?token=Cvf2oaHj8eL4SsQnDWaGMqSmeOVH3lsVb9jvQj3nYq2E3oWX17wRaHKFnWT6ogPs3T9wf6ETgsORDVUl5NNX8ptM3_O1-om0nX77Dsk1O0jtbXK_e7QkxXkY7Gy0WtjVZE9dlpGRFmeoH73Cd5-gT8Pyqy2DWgNHvSGdL977QyOTh_bFCl54PFYHwlMBN5Is0iMeczTyoqJD8X1Iiwr0lCoex98Sg6I0SvA6rpGdhEFOAHKJnUD0dq2dkpmnCiklFjmWDMeJUCQzdMWvrw1Byj0-QnovOh-tL6QhGdGsGZEb1DFH980jkwVGoBgLogkSBCznWir0HBQcxnzSviPZzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
طوری که‌‌ تیم‌های حاضر در مرحله 1/16 نهایی دارن بمرحله‌بعدی‌جام‌جهانی 2026 صعود میکنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24877" target="_blank">📅 19:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24876">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjpLI4Lcsp6GgMSX_Ia24k-xGCQVBX3ZTgvHd1AxqZsvNx45vkAYoTXygSLJRPH4-X1OE27b_VloOeH3SEpLV6zQN8AAxTN0f56zzqhN_ectpSdok6SOsTr5vjiEm_fMedVyxvySyGItplwbFpk45IP5zx6PrBJkbxmc-faDx6kg53PUHen-a0ZpHh4chY_mf7eZ-Ep69R6v9wSOImlc9DM094kt0ch5d0Y-d7LWug1_B3lBR3FwKKrnHjEqE-Q1Rg4mU74TaNOE2FEkSImvx_truBKMynxuGgXIJdbF2NsyE29sZ4rNu1Lm4WWJMELCDQB9-_jw4mbjtOwnQg_pNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/24876" target="_blank">📅 18:37 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

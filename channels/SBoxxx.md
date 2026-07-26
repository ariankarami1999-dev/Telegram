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
<img src="https://cdn4.telesco.pe/file/C7lThbsenk-A65iE9hy_oz97jZFpsoIAICZC1UX1oXnaGizaJFzmrJI7EXgIhNDC_QUMtQ3JRHtxUodXRpu9TaH0Ifjcpfc0q6mESPPTtd5U-UHb7XsZwwDTUDMLhNWtwL7rjqGX-fWz4s1xiwtw5-7PlbsqVZpKFutpB9-POOipGUkR5dC4D9yUKUnM_lqn3kAZb-IHX4jWeLYEX8UoV9av7VchIHrQIuHRSqLLaGY3yEIZsGeAxrToQepRkRmEyU-zJoHj8V1gr8Sf3ihMZiA5izlcUHK5rPNra3oQ1_ELx2lTmgdxNe_6GUE_-gyUzPOg_p-1nYrrJ9ke0G977A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.5K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 01:57:18</div>
<hr>

<div class="tg-post" id="msg-19308">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 406 · <a href="https://t.me/SBoxxx/19308" target="_blank">📅 01:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19307">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس شورای اسلامی:
▪️
هرگونه حمله به ایران همیشه هزینه‌ای دارد و این موضوع امروز نیز صادق است؛ آمریکا و اسرائیل به خوبی از این موضوع آگاه هستند.
▪️
اوکراین نیز ممکن است به زودی درک کند که ایران اقدامات را بدون پاسخ رها…</div>
<div class="tg-footer">👁️ 500 · <a href="https://t.me/SBoxxx/19307" target="_blank">📅 01:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19306">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">▪️
لیست کسانی که اشتباه محاسباتی داشته‌اند همچنان در حال افزایش است</div>
<div class="tg-footer">👁️ 651 · <a href="https://t.me/SBoxxx/19306" target="_blank">📅 01:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19305">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 681 · <a href="https://t.me/SBoxxx/19305" target="_blank">📅 01:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19304">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRJJ2t1MvF94yFyxNO2vT4Pmlnqu4ab0_jd6DqemvZWpcnlrhqoVIActtCDMflgF_7DT6zmdPXeyLphpaDTkJkZKSbKzMQzvJcleDPtzV14wcO9263cqL_e_CdE66TuNb9lotI9QPfAKMCDOUta6aKtyYT0bE_Er5_RLNXiksX3pySFeSqChNaS7hrN05QPTRxqo1xjyLH_szrXsd5ThiVqPUZnBiC3CWuN2LlEOSwQPFNb9jBQI_SmxOss-sOh7fqGs2-Azgy-Frp5Nty8gmPCCWCMudrn110RuO1BDjFRU-3BUGnU3CeyuveR5MyJqFkrJ6Ot-TqSuTHGRa69eTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشایی نفت با گپ 7 درصدی منفی!</div>
<div class="tg-footer">👁️ 838 · <a href="https://t.me/SBoxxx/19304" target="_blank">📅 01:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19303">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDS87z58SkZuGsDNIgJxggtklZO3HnDKiU2GZAH6r9Yeg7kN3miO7bpeQB8ofQP57K44cMkSIozCzyn6SbKalkAUrESM9bcgll6FTxN6KZgsc-WA4zM1jPa_xLZaC47b9Dm-3FcUXsa3YnwRy_Bd5zw2jzXyFht6aNQRrgXvakKGGGI5K7vNVqDJjJq31DFLFm-2LE0UqSYmU8We5f69jDIXXXS_MTsteOIR-l4_Qh5OnO3gB5lw21nnryP6FKnyZ2HcB2pAHudpaP8jkhK5W3fMOva-xh9L50vMp876s74rH0GwuWbbGtz4Z_Aiom8WcmtZ_WhKfvcIaKjWvu882g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از جنگنده جدید دوسر بدون دم توسط ترامپ</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SBoxxx/19303" target="_blank">📅 01:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19302">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8tQodypWQABXAdc6dNfbHD29RuYPgcn38GPpwcWY6F7koCDQh-ojecgB6lUe8DeZzbnruolujJj51QrmnbX8ayKXsiyoZeirNnM7FdjsWoUc6TC-PJ7jMFLz04S64PgWK8VKgHEYGuUVv2XaIEK9wA6fDvJLTWDwokXwVNXYnVBaZcqSNcrhRXY1b5yskn6PT45smWDrIQyG70LdKzWbMx4DLOJIJm_VId4UFSATTsMsb9qwjzliHkr-9hUlTkG7B8PNo1eB1NN8TTvcbCi2DP8zqNNeRMjfCdLMel3Y3iacUkOsBKm0DjTabqeQTwhL3a5lt1MITDXd4LxJCiANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SBoxxx/19302" target="_blank">📅 01:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19301">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtKGWflHs8XYfQ7LjQqxo1xPJwhrbLeIBlbDk4PRMAUPwPPwojraXhJ6Jor5ZTZ4Z2jVY7sAtt-H5g9dbKdkXYoeLCXRikBBNEYD3k_LcXZPzLXnI34FE0AoJhVKFZ9y4n0r1qivRpK8SZ9rGiwDk9CVjrhI7p7ioxIgSE7fXkSBnJ55rMWsGLaPiz5t-iVGbNb_EOqgnvcTlVQPnBSyFPS6dfWzxQVNKFW0SUQbwG2A4lfzW9Oi5E2fliErFeQPfTc7tBs4_htozDH6bFQ8aoClL2D0ucAghLVA1jKjPxkP-2WbgthODhUgIJKwsLq9KSl8WZ_PNXB2wrGK711JWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ول کن نیست!  اشاره به زدن موتور نفت کش های ایرانی که می خواهند محاصره دریایی آمریکا را بشکنند</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SBoxxx/19301" target="_blank">📅 01:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19300">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رهبری ایران در نامه ای کتبی اعلام کرد:
در برابر اسرائیل و آمریکا راهی جز جهاد و مقاومت پیش رو نمانده است.</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/SBoxxx/19300" target="_blank">📅 00:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19299">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وال استریت ژورنال:
الکس هولدر، فیلمساز مستندی که به زودی درباره لیندسی گراهام منتشر می‌شود، گفته که این سناتور در هفته‌های پایانی زندگی‌اش به تدریج خسته‌تر به نظر می‌رسید.
وقتی هولدر پرسید که آیا او خوب است یا نه، گراهام پاسخ داد که برای خوابیدن زمانی ندارد زیرا هنوز باید رژیم ایران را سرنگون کند، به میانجی‌گری صلح بین روسیه و اوکراین کمک کند و روابط عربستان سعودی و اسرائیل را تا پایان سال عادی‌سازی کند.
بر اساس گفته‌های الکس هولدر، فیلمساز، لیندزی گراهام به تدریج نسبت به هر دو دولت ترامپ و هم‌حزبی‌هایش در جمهوری‌خواهان به دلیل جنگ با ایران ناامید شده بود.
گراهام گفت که با «تعداد زیادی از افراد در داخل» که با درگیری آمریکا مخالف بودند، درگیر شد و افسوس خورده که مقامات کمی از دولت به‌طور عمومی از این تعارض دفاع می‌کنند.
«تعداد بسیار کمی از افراد در دولت این جنگ را تبلیغ می‌کنند. من شوکه‌ام،» گراهام گفت.
هولدر گفت که گراهام همچنین پس از اینکه رئیس‌جمهور در ژوئن یک توافق مقدماتی با ایران امضا کرد، از ترامپ ناامید شد.
در مصاحبه نهایی آن‌ها که چند هفته پیش از مرگ گراهام در یک مغازه باقلوا در کلمبیا، کارولینای جنوبی انجام شد، سناتور گفت که ترامپ بیش از حد مردد شده است.
«او اجازه می‌دهد این موضوع از دست برود،» گراهام گفت. «باید بروم و با او صحبت کنم.»
در اوایل مارس، لیندسی گراهام پیش‌بینی کرده بود که رژیم ایران ظرف «سه تا چهار هفته» کنترل شهرها را از دست خواهد داد و مشارکت بیشتر اعراب «تکانه‌ای تقریباً غیرقابل بازگشت» ایجاد خواهد کرد.</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SBoxxx/19299" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19298">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcEIqfJHMWF4_CXphnCKHtVRA887a_FuF6yakKZdfHFVRylNE6S6yISirDU3g9hsYMVcygWWxSLRsBOZ1s5TKiQYk4IJXkzQ-Hvbxh-iwD6RE3Yj6eRZISCEkJoT8ZcfjtgEJJ2VIGAKCoZVRjWVvJEC4HoejPjR-V-NmNbR9bzCidswXUJ1D2ZZSypZoIxzgisa7eb-t0ZcZQ98wViC-2kRiwO-QhhiJRr8Qelu5FcwjxMhVZZMkBYZAEb8k8ujUny6iNTaqsSRzjAAlPjCBFZK389iDl0_iifb_ng9Jthyc6AsPrBei3kSEgDHlxTEo0mtPUKYrqLqZGVMz_qH2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آن عرب ها کیستند؟!</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SBoxxx/19298" target="_blank">📅 23:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19297">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5WydgEBwS2qpSFoxLzv_-Z07-GempMLezbLU5oRbzv4KMyyca2tHVmFWAP9yf1RGAsJxHmaDndZVkFS2UcVhgfvSDOenfny1nEe8DI1Prn3dlVH7qSEqUM4f0CPdlppsMkKAriaOQohA3XZhiZGXOfFCdRWpS4J21Ycejkok-DHNtREJCHLREH_tm0_uMHMxgohrKfzlS_jNp08iaSJkbCdMQmUL6GWFBfurqnmj0dCyGPN29I-mF4ZDzhnrfRVchSiK7ZTJSslh3vzCIG0yl7TRhrulY34DjfzCk6T9OahIpfdLIZrJn8Fmvvg8PbLkZPevDZXqdYoGXT8F4eFCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/19297" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19296">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNIKKv0L5J_OdUMbpbNLoGb6RDf2IKi6h4xERsXPNLJVdwglPfYMd7faILLOCiIjDSvF33ryU4Gwwa679dOTUdwI9Ei5FXZtVYJkFG7UYEtM2zkyNHGTzX_hZ1LHVxK8oVcIzEHJrqbruwWIMtqtv3f5jvjDR6WYwNUH5K_ImriYpr9YTs9G8MYw6aF3kmIelXs2agQamld-lsxON7xcCN8h2qaWeruYLtbJTmakh_I4gKp7BNAyTnQbX8kEuOJt6wATt0k0iBVCLr1AzeU9Bkca2aI7mGN02DqewtcpSpszg6DA8fnDRNRR1gfh6T-i94GIe_uYxjLljXhvvraPuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SBoxxx/19296" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19295">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قشنگ دارند به نتانیاهو پاس گل انتخاباتی می‌دهند!  میانگین IQ وکلای ملت را دوست دارم.</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/19295" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19294">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/19294" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19293">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/19293" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19292">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-amZG91nGsnTe4BWT6gc5j7WEA0_w70hhkZ-wk5wk5_p2uvQwF98OSI5P5zsLwTx8-fUQshFmI3LCHfCBQOPXI8FH6UthqpJJ9K0jeDGSa1H3F7g3J8mW7_XEss87dvqVw3z65GO6YCLdayZZVT4NCerLWrNtoE5LBJ0UCba60ZmkmqesVxehhpCVSznK3YZBm84kSpEvy_LThoxcOKrfQtbE6-lFJ0a3MjWB6n3JefH9tMSKXPluZxEqCkJ7qNmXyAlZzQKMRmQ1MMyF3EERSaa-OxoXFNDYCsh0cYPB-AyttCLMCATLaNFFuMy1PNONYfx5JDXQ-2pRaz-uUEFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب رئیس اول مجلس ایران علی نیکزاد هشدار داد که «عمل گستاخانه دولت اوکراین بدون پاسخ نخواهد ماند».</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/19292" target="_blank">📅 21:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19291">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnHDz0C1D4kOGFe5WvRr9rgFMRKVKTxG007Z1bbAoS6tEBCHCVNiVPfx5rYa6R-tUHq5rUaOlOkaDLdy62dKmpu4sKurmW69aqA3fhyavrVp7WQhdrYvE08ovOZ7o54j92ilStM96ByiNzNgbQ96Cbu81xNIpfK5CDO0JxpFJGI0Ay2qdxZcB1uxGJXMFV0NFJuiuC5NGZhM1oPy0v8XgVzqGIprJQuUPCxThEQJIsRgG5vAZszQ33eVGUQiv_HH4kCmSaCjLkCamyQK7ZY-iQaz_Vs5n-wLvcp-dxttcHDzKU07aA6a60HwCqMNt3GRusw-HL_hEAnOS5RrtA2Hjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصارالله یمن:  یک فروند پهپاد آکینجی متعلق به ارتش عربستان را بر فراز استان الجوف سرنگون کردیم.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/19291" target="_blank">📅 21:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19290">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">آکسیوس:   فرمانده سنتکام «برد کوپر»، توصیه کرده که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به حد نهایی کارایی خود رسیده است.  به گفته این منابع، توصیهٔ کوپر (فرماندهٔ سنتکام) به همراه مشورت‌های دیگر مشاوران، بر ترامپ در روز جمعه برای توقف…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/19290" target="_blank">📅 21:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19289">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سپاه با زدن پایگاه های زمینی آمریکایی ها در منطقه به نظرم دارد می کوشد تا تاریخ حمله را به جلو بیاندازد و نگذارد آمریکایی ها بسیج و تدارک کافی داشته باشند.  وقتی می دانید حریف می خواهد حمله زمینی کند خب طبیعی است پایگاه هایش را بزنید تا نتوانند آرایش مناسب…</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/19289" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19288">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsKsCdJXNYapTfEX0lWZUM-ADt0WF39SSRJhrN2tP90qcngbXkkVGGG10ROrKPHWckM7_I5rGdAvHaChoUk4a6at0vWhE5-6wrCRXxN_anN-uv7rYmqiloozQfS_AoE5WZvbm03vaUodNeI4_BhcpCqtStuiv2iecBVQiCIDXYli3h4wQS6iEH0FO1bKUVccJCj29-hOUykcFIxvBfX1P78XWYfBrealvG3ochzMNRx_iPrM9nqUmfn9ywCen3DY9eGH6lrQVamRfFOZ7Csy3ZF3q3d__Xsj21yErujfevW-iRvh7B2fG--mtzDYjQst2VvCBXpENtkDj6bs5lYWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت های پیشا—گشایش نمادهای مهم در بازارهای مالی
ریزش سنگین بهای نفت برجسته است.
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/19288" target="_blank">📅 20:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19287">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">عراقچی:
زلنسکی به دستور اسرائیل به کشتی تجاری ایرانی حمله کرد تا اروپا را به جنگ بکشاند
‎</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/19287" target="_blank">📅 19:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19286">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وقتی میگوییم اندیشه چپ باعث زوال عقل (و البته شل شدن ناموس) می‌شود یعنی این!  شاید فکر کنید این صفحه دفتر دیکته سید محمدطاها ۶ ساله از مندآباد باشد، اما نه! این نامه غلامحسین ساعدی به معشوقه اش طاهره کوزه گران است.  لابد با خودش فکر میکرده چه کار بامزه ای…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/19286" target="_blank">📅 19:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19285">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukbWCQa7nfTmhrKHn7hTq7RxibTrDpmEggKtEcASRZ-E8ZDIkLRe05B6dh7mlej7y76cUR1T-YoToocddz3figtdmRXZ-6iNQAWJf_bXSKUmgRbyQNXTlw_7NXzfLQivN8tkosMXuMOi5sB2NxipTCYIg6D0HkaqesXiJ3r7HDycp6EfXtCFXuwYdb_I3AFLNuxSO94qZKRl6fEPip2ZeMZxHVwWeYwMjHqW57VANhtsTt98p-mbHbICEusLk_B0fN8I-KMLv82fAGPWVGmnmLnUgqHYdtrC_nXEhyeU1ZMwM0Cfe-ESd1iqp_v37Jsbm2Gw22SYbNNOaGh0OoqnEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توئیت عجیب عضو کمیسیون انرژی مجلس:
فقط نفت!</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/19285" target="_blank">📅 19:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19284">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hE-gvdWCTfjgzO4m5h6xEZyIlU2U4jz-2KwqT8tWpAPdYYvS702piJmcrDChmgLqq4TlDCuqRzDhlLasaMO9Q22KxRbpPozloThGcAeqiwWkoHaTn_WE9CmtW6Emx5WI0cDzLKSrEBEIkCN_-BP9HS4z3pIwyiHC9iFINf724w_9h2XaTk6w5ibIJ9svXeSruHnX2OXkX6vs5aTVEMUSCHrXiUCTaSomth1RE52h38CO3sWLt-ZUWdWdpZ6hh5PzTPoY_ZlJuWsNodGRn5N7LVoV1T0dD66NxqWc9f5LvLD0JqiJK5TK28WodpGUaneNvluwvOROYSbTJ2uQAImJ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استالین و بریا!
بریا رییس سازمان اطلاعاتی شوروی در حین جنگ جهانی دوم بود که هم حمله هیتلر را به درستی خبر داد و هم با سرقت علمی از آمریکایی ها، برنامه تسلیحات هسته ای روسها را به نتیجه رساند.
جالب اینکه او پس از مرگ استالین در سال 1953 اعدام شد!
#تاریخ</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/19284" target="_blank">📅 19:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19282">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نتانیاهو به فاکس‌نیوز:
جنگ زمانی پایان می‌یابد که نظام ایران سقوط کند یا چنان تضعیف شود که ضرورت پایان دادن به برنامه هسته‌ای خود را درک کند.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19282" target="_blank">📅 18:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19281">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=uYh4yezWmwZmZLp0WQOUg7CaUpmCPrYVpfgiH4qaUzZf_0tVkXxdtbB3_yVBLAi-mXDOYGCYab748uoQvYdvRCj6hEzwU38iVtEsCO9lTvC1ekflbdFF5Y8aG1amduVkWE3W3tmrhHk3uwuFp6Be10kCn7_xq21vkUxczqMj7CL-1BC6D1EtITPjkuFumaefBNyrcp-_RAtfH8fs4D162kxp4Dufn8GQYhcPlq-YwE0HWtSx8s7fnda3XUjQfjaa2Ys2yX2lFx_OQr4KLLK0euwnPk5Yox0n-KmYlAshvNVeYZDkqnkF3-Nr2YVhJQ4EVW3PMUcWdnqy_SsX5JhkbBJ5tl9gDMpPdEMH6cCA5wrJQMbadqi4iPQD7VPhLWQ0RdoqkaHuV6cXDX0kcvsSbtKJnFvoY34htgSxbByoerKXtNAEH88mc5C80UY_s8wTo9fa9BvpApBzXgQ8GWgQt8vxrdq_szT_xJhCvInn0vyP5tF-IcM1DDke4I3PYI9TMVuv4AOQ0gU3iyUim1EGNMnXT0vC8HdwqHZ5J0tPx0_42xmeknySXNmaOWwmwI2ViBe0lnlEVlTlBo5TCRvCggqPyhX4ifo6ronZHhAxzwZG7VSFH5xkQCyPFjLWWmWL1QURxp0dgAeNY7S-mZEqDyIVfg_9CGZY8q-NynBx3RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=uYh4yezWmwZmZLp0WQOUg7CaUpmCPrYVpfgiH4qaUzZf_0tVkXxdtbB3_yVBLAi-mXDOYGCYab748uoQvYdvRCj6hEzwU38iVtEsCO9lTvC1ekflbdFF5Y8aG1amduVkWE3W3tmrhHk3uwuFp6Be10kCn7_xq21vkUxczqMj7CL-1BC6D1EtITPjkuFumaefBNyrcp-_RAtfH8fs4D162kxp4Dufn8GQYhcPlq-YwE0HWtSx8s7fnda3XUjQfjaa2Ys2yX2lFx_OQr4KLLK0euwnPk5Yox0n-KmYlAshvNVeYZDkqnkF3-Nr2YVhJQ4EVW3PMUcWdnqy_SsX5JhkbBJ5tl9gDMpPdEMH6cCA5wrJQMbadqi4iPQD7VPhLWQ0RdoqkaHuV6cXDX0kcvsSbtKJnFvoY34htgSxbByoerKXtNAEH88mc5C80UY_s8wTo9fa9BvpApBzXgQ8GWgQt8vxrdq_szT_xJhCvInn0vyP5tF-IcM1DDke4I3PYI9TMVuv4AOQ0gU3iyUim1EGNMnXT0vC8HdwqHZ5J0tPx0_42xmeknySXNmaOWwmwI2ViBe0lnlEVlTlBo5TCRvCggqPyhX4ifo6ronZHhAxzwZG7VSFH5xkQCyPFjLWWmWL1QURxp0dgAeNY7S-mZEqDyIVfg_9CGZY8q-NynBx3RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی جالب است؛  از 6 کشوری که شدیدترین بحران های انرژی را تجربه می کنند، 4 کشور در منطقه ددخیز خواهرمیانه هستند و 3 تایشان (سودان، سوریه و یمن) در ژنده پارچه ای که به عنوان پرچم رسمی معرفی کرده اند، رنگ های نجس و نحس پان عربیسم (سیاه، سفید و سرخ) دارند</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19281" target="_blank">📅 16:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19280">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19280" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19279">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19279" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19278">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQxLxCn28CglUl5Bx30sT2Qp4Sz9mZ57cY8Y-82e1ZCh2HFvGMV-aB3CnSGs2MpmlT2XkVa0PJAnEFsO-a0Lyv3Gc8ChPC1_1svr-DHJjj33yRRtJgO-0sh4kZumBJvVsSWVLlgZ29zlWqaZVGWBwkKvJajyK78c_6SfPbGt8aGBhbAD1y2wKgYAMNXPRbYonr4QChzAzk6zNvUOIaSm08JvhwcJkJhaoxOQEKLFPfLhEamzoUMkUz8L70Rp_d4bTLHjyApyRPiGG37Z8LJqF6FoxP20vvsDgoYekXNghKuRXTzYIFGD_u6M6L4d8smpr25ULhOokdoXVVRuDFi6rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19278" target="_blank">📅 14:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19277">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19277" target="_blank">📅 14:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19276">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وقوع دومین حادثه دریایی در دریای سرخ
سازمان عملیات تجارت دریایی انگلیس از دریافت گزارش حمله به یک نفتکش در آب‌های نزدیک سواحل یمن خبر داد.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19276" target="_blank">📅 14:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19275">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">برای نخستین بار در جهان!  کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19275" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19274">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=P9A8ChUX-3j7RhsCN3oCIFHow5LFxY7IQfbswZuScdi52ZDAMdXOHPwKB4EgLdfbYnOUlfQBHRuY4ut1cM00X086eW7RTz8_67y_4Lhwx9ONH4Jp9oMvg5bfaagt7JJyQx63ghXggw9LrV1YX40q4vEQpie_Feaiv2XPDfRn0nb-n2ClrMKLaixKTt7hN2P3xc9IJXdQ4CCywpOlPNMZmluPS1DpgYVrkOW3oe2Tcgtg0YN4LulOiMdii0LLArDnfgoYPUfjbUD1Isv7jsvM4uElhYth_jAAYl8VzvNQ4hzFH-4PzToH4U5HrP6or9lCGgaef5pYCwurB7i59ot2Z3gsVwzoLSU7CBgejMeXbtCLUzSL98cXnfH6FssqmTl8CpNX_kMLvq9DH2pd955PqwF7wECQwZqdhinL2w3EyxLyhVkDzGFTwHwj60hEoluDmgt8ONlj4JSpA4zPTOZTY1ixkPUkq62Tte7yCogBrpYsJ2-qd5b5qRH6C1EOkvu4KoMbWfi2O9y2LEjumhRnDUEg7VheHtaP4yISN9yFdmTlUyhbzWR0Sej4ZqyvfkD2dATQVgMArWmsQGV45vKOtzyekbSP045nrup15BVrozFFKhGYJTMpf1RzajVbXgxJQF2iEDr_-iLMoxzGiemBknn_KQDF08mPCAVgk_RFmb4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=P9A8ChUX-3j7RhsCN3oCIFHow5LFxY7IQfbswZuScdi52ZDAMdXOHPwKB4EgLdfbYnOUlfQBHRuY4ut1cM00X086eW7RTz8_67y_4Lhwx9ONH4Jp9oMvg5bfaagt7JJyQx63ghXggw9LrV1YX40q4vEQpie_Feaiv2XPDfRn0nb-n2ClrMKLaixKTt7hN2P3xc9IJXdQ4CCywpOlPNMZmluPS1DpgYVrkOW3oe2Tcgtg0YN4LulOiMdii0LLArDnfgoYPUfjbUD1Isv7jsvM4uElhYth_jAAYl8VzvNQ4hzFH-4PzToH4U5HrP6or9lCGgaef5pYCwurB7i59ot2Z3gsVwzoLSU7CBgejMeXbtCLUzSL98cXnfH6FssqmTl8CpNX_kMLvq9DH2pd955PqwF7wECQwZqdhinL2w3EyxLyhVkDzGFTwHwj60hEoluDmgt8ONlj4JSpA4zPTOZTY1ixkPUkq62Tte7yCogBrpYsJ2-qd5b5qRH6C1EOkvu4KoMbWfi2O9y2LEjumhRnDUEg7VheHtaP4yISN9yFdmTlUyhbzWR0Sej4ZqyvfkD2dATQVgMArWmsQGV45vKOtzyekbSP045nrup15BVrozFFKhGYJTMpf1RzajVbXgxJQF2iEDr_-iLMoxzGiemBknn_KQDF08mPCAVgk_RFmb4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای نخستین بار در جهان!
کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19274" target="_blank">📅 13:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19273">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">در حالی که اساساً مزیت پهپادها در کوچکی و سطح  مقطع کم راداری آن است، ترکها رفته اند یک پهپاد غول پیکر (همین آکینچی) ساخته اند که ابعادش دو برابر یک فیل است!  طولش 20 متر و عرضش 12.3 متر و 5.5 تن هم وزن دارد!  قیمت آن هم بسیار گزاف بوده و بین 5 تا 6 میلیون…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19273" target="_blank">📅 13:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19272">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBa_3FuZFvCEYF5YGVsXuiF1hP76DDeigzzY6ddBebv7wj18ndtnWE-pPOTV69h66-Fn9Eg7voQFKAy8C-PbB_hCA6S4464hcQkCYibkw6uPcFzpMUcnpIggJ_qigDEH3EdhHKqJeRTPEj9JAWH_mQUTGeaT0Dq24Tu1k1B9rzFOrqlSYh8_YQW0QjdUcG74YDmxFdMDQb9d3z6YYiGCRVwEZdgj_wMxvG5OJ21OsUhZ61zn_soZTZ-JXUB8B3682vFDDch9AZubNH03a46dTlQ_p8-Miv5qAbhDvgfj1rK6qMeakfgziKvcU2PlR2Ub5h1BflpbSsMnd8neBtAD-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان بالای مهمات پدافند موشکی آمریکایی ها در جنگ با ایران</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19272" target="_blank">📅 13:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19271">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=usygqmmmvIB3Y9r6hQt6xiJHDAUZghmaIRlTzGZ4XdB5zkCdViB8BA5mz-MhSjZwlnZ-NoC3uZct53IgvmBEnr5gl1DbI8vu3OLc44FSJAhUp8uS7VokZUCviRe6a1MyWqU1x1456F_yagIzhAmtvaRGgCI8t2B-FlGVxbc8ns3jDFb1hyYuUKPIkSKYD1jsfCBPu6avghYONwrAduufs_cz_DUrZAQUVszrSz-gqRCtM9xMLLUGw8ugpbjOk1EYAncNWZN0x9XCpngOdaRXmGX0EONlENwOSkiJrjau2W7F0StxwcBFt67Q3DC1DMtdNi386sy9Ajp5zb05HLxNIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=usygqmmmvIB3Y9r6hQt6xiJHDAUZghmaIRlTzGZ4XdB5zkCdViB8BA5mz-MhSjZwlnZ-NoC3uZct53IgvmBEnr5gl1DbI8vu3OLc44FSJAhUp8uS7VokZUCviRe6a1MyWqU1x1456F_yagIzhAmtvaRGgCI8t2B-FlGVxbc8ns3jDFb1hyYuUKPIkSKYD1jsfCBPu6avghYONwrAduufs_cz_DUrZAQUVszrSz-gqRCtM9xMLLUGw8ugpbjOk1EYAncNWZN0x9XCpngOdaRXmGX0EONlENwOSkiJrjau2W7F0StxwcBFt67Q3DC1DMtdNi386sy9Ajp5zb05HLxNIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران هر روز برایتان یک سورپرایز دارد!
توحش و بربریت یک مشت گوساله در مراسم رونمایی یک یوتوبر ریقو گه دیروز در ایرانمال برگزار شده و ۵۰ هزار نفر در آن شرکت کردند!
حالا بماند که گوشی عستاد را زده اند و دست و پای ش هم شکسته!</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19271" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19270">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyOym20_B53T9d58iDm1SLVl8wY9qWVXNtp_lmdxW6hkeZ0ic1exUvUsKCN1Hz4xIJZLwu1Kr0SWqNE2lYhCK6nhsBBYlZfXcUFo89STs3tsX0Oorhqy0fY3whhdaQVudBAhRxrJE6RHMoLS2DKPykE_zDptGIGOXtpH_Z6r0_muDezJxByWBTfAgSCte6JphagGPdcFinjEQ196x6W0bSPM-rvtrirI5EjrIsSMeD5pdMbVuo6zqM-6Y5fT_NFMNb9pfiRA6IkTG4yFReizuKdzoNeMjJdF92h6463LzAFb05tosVp2DkbRC5KM3MgHCicmCPzOjHBYk3ce0BdyrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این منطقه سبز بالای مرزهای کنونی یمن که جیزان نیز در آن قرار دارد، تا سال 1934 متعلق به یمن بود که در پی جنگ آن سال به چنگ سعودی ها افتاد.   هنوز هم برخی ملی گرایان یمنی نسبت به جیزان، عسیر و نجران ادعاهای ارضی دارند و آن سرزمین ها را مال یمن می دانند.  #تاریخ</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19270" target="_blank">📅 11:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19269">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxeJFY2kk0DhuPayo7BMaTx6MKEm7eYgwMaRYcXn4sl-4Qg9X00vMu63A_cUcP-P6bCOyJ7rneVoTPQmhWrnvzZU86bz_vJG3u5wTizSwuFEmI6acQigrXK6GAallyGxlDay1Yohh0BQOgu0Ojq3s_lhFfidyh_WJfff6cwhs1S0I9D6PnpxhLpb4Q110uzJ_BhnIQeA3IrDXopOK-X7NqAY8IVyRA0rG5l0sU500QYzNTB7W9JWJTgxxBcT-kEPBk-R6AendiUFWKb-60l5HHP6ot8hvSi5acw48EZqkTHc_WIHVvlHQW6caXUQVwo9e4xIIdB4XE_7WXPeoLWAbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19269" target="_blank">📅 11:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19268">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhqUV4gZHPdZhCg1f3HuN08DavWFAEoqcE-30we3bnlc84E1tSCWDN1sD0JIN-3xCVw8e2UftO7HjmLM8_RN3xYK6Xz8PMHEZleUz64xgK_lQ3UqYraJGWXpE4eOVHvxITil3hISzx_P0Ew9Qyn6HMJJ51aT3c9pz1dJ6d12ADRQRYtp_XxQT0wwdSqgAdaqQnmN9RrsiGJZy7Xni5CO4_mKIKYSAvdHSxP4-T6Vd5t1qdedagw3f_rFrC8TNZu3VOeE8V4sRX79zYcx1tKeiOOeHZG-CjWjEaW9WBTfYFbBRfJRF8IL4vKWn4qB9LarntvOtTbRI98ivGVuOELq3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19268" target="_blank">📅 11:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19267">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بقایی پس از مذاکرات دو روزه ایران و عمان:
مفید بود اما تغییری در وضعیت تنگه هرمز ایجاد نشد</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19267" target="_blank">📅 11:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19266">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=mkO48m8o07z5OIxTSN2It5TbArGx3rskkMSD0MFlOW9IxvCtyJZn9Yx2llmjn81LBjGm7xQ3-ymlUNoQ2w1CN3wkopOEdbFBBY7toMi6xhgrQvVQf2lg71VxFO78L_hg0TbsZ44lBSv5h8a1t6Hr7Jhv9D3envGDQN4gDSLOROiCQ8fVEDxIV9TSzbKGE8ssmGdh0jxXAoUk7wi1sSIXyLE04Idx9KAKGE5JbTR-niMSxTdHTTIoklkx8wKH_Qn9LqVdcvs98S1zgcFo0g7eWbmMBu7S6-uoLZ2zrFDxiV4y02eRb6NP8vqdWR382kz_seLqVit283y8GDCBf54GpnWQ9Og6GwEKVRdNbNKZYyqC5z26xTwEgYDyLc_CS99PXhMyKDdabNxVIOCvJQ0DgOTqxkJJgZJKGVqCV9_2ZWqQBxTXnbOpqR2CR4_V93LFevpf4D9OjktjtZS2k6LLDTQc9p1u3rRinuZ7sw2IHP6Symmp7wKdkuUBc9VgryIsPgb-7mte3SIe9AOlAfFv1_iPNPNQ4chewHjdE8OE82ddAuAsuE_KqwjKDYUsSyyPwLKUBeTkxgsRvADDQx1qx8j-j2vToj-XTEV4MD0jCYM7mRp9ReT_fr7XZGCwm5nujExlAik-jlLJD-dBu_6s9SmTjwykx5RG9wuJq4NjaEE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=mkO48m8o07z5OIxTSN2It5TbArGx3rskkMSD0MFlOW9IxvCtyJZn9Yx2llmjn81LBjGm7xQ3-ymlUNoQ2w1CN3wkopOEdbFBBY7toMi6xhgrQvVQf2lg71VxFO78L_hg0TbsZ44lBSv5h8a1t6Hr7Jhv9D3envGDQN4gDSLOROiCQ8fVEDxIV9TSzbKGE8ssmGdh0jxXAoUk7wi1sSIXyLE04Idx9KAKGE5JbTR-niMSxTdHTTIoklkx8wKH_Qn9LqVdcvs98S1zgcFo0g7eWbmMBu7S6-uoLZ2zrFDxiV4y02eRb6NP8vqdWR382kz_seLqVit283y8GDCBf54GpnWQ9Og6GwEKVRdNbNKZYyqC5z26xTwEgYDyLc_CS99PXhMyKDdabNxVIOCvJQ0DgOTqxkJJgZJKGVqCV9_2ZWqQBxTXnbOpqR2CR4_V93LFevpf4D9OjktjtZS2k6LLDTQc9p1u3rRinuZ7sw2IHP6Symmp7wKdkuUBc9VgryIsPgb-7mte3SIe9AOlAfFv1_iPNPNQ4chewHjdE8OE82ddAuAsuE_KqwjKDYUsSyyPwLKUBeTkxgsRvADDQx1qx8j-j2vToj-XTEV4MD0jCYM7mRp9ReT_fr7XZGCwm5nujExlAik-jlLJD-dBu_6s9SmTjwykx5RG9wuJq4NjaEE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عمومی بودن اطلاعات برخی نقاط حساس نظامی - امنیتی در ایران</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19266" target="_blank">📅 10:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19265">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پدافند غیرعامل به زبان ساده</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19265" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19264">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQoR0DyLn3FDjFIuPi80ltdMus0uxzBJhULJGNavTMuRPuWQ7Xa6jeNjF1wt0J6h-pxOfO7GI9w13SJ9JlNpj9fCVwYuVArgZpIOsbfOyp6AN69EIkdfcByLn_8gJQsYd-M8nDndBfRc1GjNk693CWobupZMYiqSRVmXAtTBq87P-zgW7VfKpArquMexNhoPVGyZsQtYAfjApcutjIFiRiohzSlkQKwNreCm6Y7Vo-Ky2MQJoCw7UrmgMOqKamJ7Sy1xwBAdG1u6353J1Ju3a0rrj1r1c3MO6s-j_xVkxlhkIBhffbFlvEKaLBcdMUqkkmxrLND6Fh3ojAO2y4BPHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/19264" target="_blank">📅 09:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19263">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نیویورک تایمز:
ترامپ، حداقل فعلاً، برنامه‌هایش برای تشدید قابل توجه تهاجم نظامی آمریکا علیه ایران را به تعویق انداخته است که دلیلش نگرانی‌های ویژه ای است مبنی بر اینکه تشدید درگیری می‌تواند ذخایر رو به کاهش سیستم‌های ضد موشکی پاتریوت و سایر مهمات دفاع هوایی پنتاگون در خاورمیانه را به شدت کاهش دهد.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19263" target="_blank">📅 02:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19262">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انتشار برخی اخبار تاییدنشده از شنیده شدن صدای انفجاری در بندرعباس</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19262" target="_blank">📅 00:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19261">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آشنایی با پهپاد کشنده اوکراین  پهپاد FP-1 (Fire Point-1) یکی از جدیدترین دستاوردهای صنعت پهپادی اوکراین به شمار می‌رود که در سال‌های اخیر به یکی از ابزارهای اصلی کی‌یف برای اجرای حملات راهبردی در عمق خاک روسیه تبدیل شده است. این پهپاد انتحاری دوربرد با هدف…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19261" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19260">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی حملات هوایی را در منطقه دمط که تحت کنترل حوثی‌هاست، انجام داد.  این منطقه یک خط مقدم فعال بین نیروهای حوثی و نیروهای دولت یمنی که از سوی عربستان حمایت می‌شود، است.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/19260" target="_blank">📅 00:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19259">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اگر تُن ندارید دستکم آماده باشید!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19259" target="_blank">📅 00:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19258">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19258" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19257">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19257" target="_blank">📅 23:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19256">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLCLujhkb4psH_DlRYw9mQWXh-JRJXMcE70vyDLH79paubpfJtAyQlgP7uky0OGcwFnV4rHT5qqnbEvI7BE5ljNjq4Ov-4O-OPutNKog66zDE0HFHBoNN_iQBIIlqqIQ_cwAXTpsoBvhrRu7XxZ9FNhby8GaesRWZ1m8iT_49GXt0aZR6xY5KwGtru13IE6qyJ_lQu03dRk6hOyTlk7Uoxlzu9vLsHu_gqIvdYJTGgvsw2wlFPB_JDXWZOHgb1NVM04rzQhe8ZF-Dhtrja-sO41V33_RfraxPrsAak7bEqtvDtOetIrlqw1tasMCGRJqeKO_sLT2yCk3z1pzRcVSiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/19256" target="_blank">📅 23:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19255">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سپاه پاسداران:  «هر کشوری، چه بریتانیا باشد و چه دیگری، اگر از آمریکا در جنگ حمایت کند، برای ما هدفی مشروع خواهد بود.»</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19255" target="_blank">📅 23:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19254">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">در عملیات 2 شب پیش دو فروند بمب‌افکن B-1B لنسر نیروی هوایی آمریکا از پایگاه RAF Fairford در بریتانیا به پرواز درآمدند و در بمباران جنوب کشور (استان خوزستان) نقش داشتند.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19254" target="_blank">📅 23:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19253">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYDqPNkVYhXJCR-HvWtSJE9f-J6gOYBc95nqHngH0_K1hfFpyErxYo-cMHAlfBtnoCv0qTd8_kuqH6nP__vLRsqST22Y-6TAglQfc2wZfkoa7UopmqcmcA246A9BmUSTM_qvOneHwu5cnXZNlqqbqd9KZEQw8GgRA2wK4ne7DB2DTU2DgEDP5wgNe3w6rkj14bwuScxsOjDsuhiFndyXbaBh0p9NuCVWGM7MBXEM3OEc6tveZwoOkk42Ka4oViTqRWcxF-Kf6teUk0SH_pMEzzCtlwJ798OKyctAL49nimq5Zid1QFsMUD2C0xLl65_wo50Rh87khaf_PnPoyhVo3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عملیات 2 شب پیش دو فروند بمب‌افکن B-1B لنسر نیروی هوایی آمریکا از پایگاه RAF Fairford در بریتانیا به پرواز درآمدند و در بمباران جنوب کشور (استان خوزستان) نقش داشتند.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19253" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19252">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نیویورک پست :  «دقت وحشتناک موشک‌های ایران» این هراس را دامن زده که دشمنان آمریکا در حال کمک به ایران برای هدف قرار دادن نیروهای ارتش آمریکا و CIA هستند!</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19252" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19251">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ درباره ایران:
اگر ۱۰۰٪ آنچه از ایران می‌خواهیم را به دست نیاوریم، قطعاً از سرگیری جنگ تمام‌عیار را در نظر خواهیم گرفت.
منبع: LCI</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19251" target="_blank">📅 23:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19250">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی حملات هوایی را در منطقه دمط که تحت کنترل حوثی‌هاست، انجام داد.
این منطقه یک خط مقدم فعال بین نیروهای حوثی و نیروهای دولت یمنی که از سوی عربستان حمایت می‌شود، است.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19250" target="_blank">📅 23:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19249">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شین بت از خنثی کردن یک ترور دیگر ضد بن گویر خبر داد.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19249" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19248">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رسانه‌های آمریکایی: به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19248" target="_blank">📅 21:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19247">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19247" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19246">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBzfO-zWueM_K7KNOpLhHCm1E7u1Gac82jZ8AX3AwxLM_odOKcfnJbHW7I6p_e-ATxg1lb1GqthOMRHVXYAojtgFH9I4K2YJ3InAwGIaLWr6qn5z1PcIJhoscX4pgHaIqdIxu-g_DmOE9VxcL4vyg8MD0DF_vbQUmS3FATfVQ27o_esZem9go4Dxf_HzZotk96yXidkQqZnc2oUgWiQwBa6kiuZdVxNsOVVRCNmhxsUEpZfPeZfTSYvhMtQg1w51UxWS4RsXGVWTb7dKQjQpzt0WDc-CxMB0A8XZwZM7zG3WpEwzWOaW5tJXt3dfhmeMdY1puJq9-jVpfyaQNrSqAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19246" target="_blank">📅 21:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19245">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSMf9ldmLJRNF_Z3TbxBrgM2A9CHc7T4BbDKgwhjqJnTX3f8TaYoAsfxMq1kSdDKT10cIfmckpAGCgUyHaZTQPwiEFGid_jij3VWj5FQ53DeNuPDH8DGr8h8ecNmKW_DYWIAlqhnAkyJfcoeb9MKCTEQWBLK7oz-t9q38uu9iCBcOoVpgEhad8ji57iIyTRNhrhl6S_w5PstH6hGDLhh4xpssej-PPn0AkzmgJX3lv9Gwkb51BQnWLDFn4AWrJ6YPyaerMJ0_APuu7wqj-E2IPx4dtZEowhVg4epXM062mY7YExMGs2vIh-rd4v-eT-5KibvuUxkRHr-_OT0VwKzSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر داریم وارد موج 2 از 5 می شویم و موج 1 از 5 تمام شده است.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19245" target="_blank">📅 21:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19244">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ، درباره ایران:
ما باید به یاد داشته باشیم که هدف نهایی ما در این کمپین—و این لزوماً با مواضع ایالات متحده همسو نیست—این است که رژیم ایران را تضعیف کنیم تا به نقطه‌ای برسد که فرو بپاشد.
ما نمی‌توانیم با وجود رژیمی زندگی کنیم که به صراحت برای نابودی دولت اسرائیل تلاش می‌کند، این را علنی اعلام می‌کند و گام‌های عملی برای دستیابی به آن برمی‌دارد.
در حال حاضر، بهترین راه برای فروپاشی این رژیم، استفاده از ابزارهای اقتصادی است—یعنی به طور کامل آن را از نظر اقتصادی فلج کنیم.
به این معنا، این کمپین و فشار مجدد رئیس جمهور ترامپ بر تنگه هرمز، به همین هدف خدمت می‌کنند.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19244" target="_blank">📅 21:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19243">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b9e36a3a8.mp4?token=UdxPrpxgSTNRdTKj1N-xY8VHTxS3-SGHkQOmhHbLy8zARW-VzHqjk-rjg2r0SCv-8S65sWrUyF4u5hGKDZIu2tDCBCaphi7o8wuoJdXrUuEto0IxipScEYKMHgEgr-R71uWnotZ82MmmUzUrcZcbkToYWdatN8LBjMJmd5fWi6XAozeEUyCgKs6RittAWNII8cbIvIgj3lJwJfrXrmfg25ReNLBzoj0Yhx7fcyljQ_lEy6C9fRp14Rz5x4UZ81k2MuhGKw6CCl9L_-UskiEn34vVekN3QWmv1xeuj5JRCKX-x0kWgKtgQjA4cbIDQm0O21n-dbJ5AIJaipGORcx2Pb9j3I-EyKkoQB_kxb1nVQvfYgX_CXWwIm0jyEpThTt0AuSUE5ZE2pUszaCLGCg61dJbzNDGugLMWAKraUFlsRJuZJBoJ2Nvdeke1rWHVS2rAYWNts-L5UHxXHW6NAk_4r-e6OdvWs1DsVPmIa_sZWCsJgTv3HAST1PiHtYTi_HLhQjDlJ460HXhs7eFu0MizqNIo8IbxSeB1N03_Ygcf_QtVxpc-eMyRk36xS7TSO1Xak-5JnT3WzDiOi7nPPTCoKhi2MFwupLYX7Rzw4oKMNJOp3vKe12x7oZOBzAw5H5xbyL9oZP5bGbF2oD9n_YqkXoIDQ1D7ObmKW3x1lu-nr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b9e36a3a8.mp4?token=UdxPrpxgSTNRdTKj1N-xY8VHTxS3-SGHkQOmhHbLy8zARW-VzHqjk-rjg2r0SCv-8S65sWrUyF4u5hGKDZIu2tDCBCaphi7o8wuoJdXrUuEto0IxipScEYKMHgEgr-R71uWnotZ82MmmUzUrcZcbkToYWdatN8LBjMJmd5fWi6XAozeEUyCgKs6RittAWNII8cbIvIgj3lJwJfrXrmfg25ReNLBzoj0Yhx7fcyljQ_lEy6C9fRp14Rz5x4UZ81k2MuhGKw6CCl9L_-UskiEn34vVekN3QWmv1xeuj5JRCKX-x0kWgKtgQjA4cbIDQm0O21n-dbJ5AIJaipGORcx2Pb9j3I-EyKkoQB_kxb1nVQvfYgX_CXWwIm0jyEpThTt0AuSUE5ZE2pUszaCLGCg61dJbzNDGugLMWAKraUFlsRJuZJBoJ2Nvdeke1rWHVS2rAYWNts-L5UHxXHW6NAk_4r-e6OdvWs1DsVPmIa_sZWCsJgTv3HAST1PiHtYTi_HLhQjDlJ460HXhs7eFu0MizqNIo8IbxSeB1N03_Ygcf_QtVxpc-eMyRk36xS7TSO1Xak-5JnT3WzDiOi7nPPTCoKhi2MFwupLYX7Rzw4oKMNJOp3vKe12x7oZOBzAw5H5xbyL9oZP5bGbF2oD9n_YqkXoIDQ1D7ObmKW3x1lu-nr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نمونه دیگری از گاف اطلاعاتی - امنیتی صداوسیما از یک محل استقرار راداری</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/19243" target="_blank">📅 21:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19242">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فراغتی ست برای خرید تن ماهی و لذت بردن از دلار زیر 200 تومان</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19242" target="_blank">📅 20:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19241">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رسانه‌های آمریکایی: به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19241" target="_blank">📅 20:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19240">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رسانه‌های آمریکایی:
به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19240" target="_blank">📅 20:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19239">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بر اساس گزارش‌های منابع متعدد منطقه‌ای، 8 فروند هواپیمای بدون سرنشین MQ-9 Reaper نیروی هوایی ایالات متحده که به تازگی تولید و مونتاژ نشده بودند، در جریان حمله موشکی ایران به پایگاه هوایی ملک فیصل در اردن منهدم شدند.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19239" target="_blank">📅 20:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19238">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حمله دوباره حوثی ها به یک کشتی دیگر عربستانی</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19238" target="_blank">📅 20:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19237">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNl6h6zuZYqQh52Yu67P-9F50Js67RqxoMELUhBLODE68QRNGX6qq7bdWX1_O_VifefFg0wEy-ydi12Chdt0ZYLX5s-zKMtQCahdE4yQAjrH2RiL9pZx6RXVitrkwPIRlD87CECOTgpHmJx2zwfcpOSPzjEfzpz9tg_emJwb3uESaL3jA1XJrBxLCHPDW9-N1Eo1wegwkPP8qAqrLncc2sBxwu2HNjk8hLi_7Xw6mZ4HNCIZq04sImJ04qA7C5L1VHdi3tIC0ccZIkV_KRqUNGyff88XJgeNHPyPhZtRXO9pNA52KSydU4goLgGjY0oWcMo6p_qC8oI1njuZT4bugg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی:  نتایج بسیار خوبی از حملات دوربرد در آب‌های دریای کاسپین به دست آمده است.  پهپادها به کشتی‌هایی حمله کردند که برای انتقال محموله‌های نظامی از ایران استفاده می‌شدند.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/19237" target="_blank">📅 19:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19236">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">روابط عمومی سپاه انصارالمهدی زنجان :
روز یکشنبه ۴ مرداد، از ساعت ۹ تا ۱۲، احتمال شنیدن صدای انفجار کنترل‌شده در منطقه غرب زنجان وجود دارد</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19236" target="_blank">📅 17:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19235">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhtDWwzi9SFfhVauceXI7OP5-YgJL3UQnCXH-JRf4KS1H-z7BSTNEuNNxwzAaOcsNTq24lDEyeXWBqFSGzhDT2SOSHk_EgOKmqppZqOPC2xC-RmfWV1pFQmV1fpOZLpC8LCHdetpHnHz-dvZU_AQ4Hlbp7E-Iv6kdiqvRdng0jsCpl8_5whV5Lzrrn9RrXre8uXWcTF_CfGU5zLxa5Ekmq2bysOXjZWa5Xa1_wXIB0PBm8cyvn5VW34-9Aam37lvbSg77hJYNdrx_A-wSQO1rpljDRSr3oeZpzYhnBpJULHLnEbujmW7ifz1_PK1qsFlCAEwgw9BYkWLvpc4CYg8VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به طور فزاینده‌ای از موشک بالستیک خیبر شکن خود در حملات هماهنگ استفاده می‌کند و مسیرهای پروازی، سرعت‌ها و پهپادهای مختلف را برای پیچیده‌سازی دفاع هوایی ایالات متحده ترکیب می‌کند.
مسئولان آمریکایی می‌گویند اکثر آن‌ها رهگیری شده‌اند، اما برخی از دفاع عبور کرده‌اند که اثربخشی رو به رشد موشک و تاکتیک‌های در حال تحول ایران را برجسته می‌کند.
منبع: WSJ</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19235" target="_blank">📅 17:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19234">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">به نظر می‌رسد ایران عوامل مخفی مشکوکی را از طریق کانال انگلیسی به بریتانیا اعزام می‌کند.  افرادی که ارتباطی با سازمان‌های اطلاعاتی ایران دارند، توسط مقامات بریتانیایی در حین تلاش برای ورود به این کشور با استفاده از قایق‌های کوچک، دستگیر شده‌اند.  — نشریه تلگراف</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19234" target="_blank">📅 17:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19233">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">زلنسکی:  نتایج بسیار خوبی از حملات دوربرد در آب‌های دریای کاسپین به دست آمده است.  پهپادها به کشتی‌هایی حمله کردند که برای انتقال محموله‌های نظامی از ایران استفاده می‌شدند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19233" target="_blank">📅 14:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19232">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دولت بریتانیا سپاه پاسداران انقلاب اسلامی را در فهرست سازمان‌های تروریستی قرار داد که بر اساس آن، عضویت در این نهاد، شرکت در نشست‌های آن و حمل نماد آن در انظار عمومی جرم کیفری خواهد بود.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/19232" target="_blank">📅 14:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19231">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">#WHEAT  بروزرسانی نمودار گندم!  یادداشت امروز را هم بخوانید.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/19231" target="_blank">📅 13:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19230">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">📌
هرمز؛ گلوگاهی که می‌تواند قیمت گندم را منفجر کند  تنش یا اختلال در تنگه هرمز تنها بازار نفت را تهدید نمی‌کند؛ این آبراه مسیر حیاتی انتقال کودهای شیمیایی است و اختلال در آن می‌تواند هزینه تولید محصولات کشاورزی، به‌ویژه گندم، را به‌سرعت افزایش دهد.  از آنجا…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19230" target="_blank">📅 13:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19229">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">زلنسکی:  نتایج بسیار خوبی از حملات دوربرد در آب‌های دریای کاسپین به دست آمده است.  پهپادها به کشتی‌هایی حمله کردند که برای انتقال محموله‌های نظامی از ایران استفاده می‌شدند.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19229" target="_blank">📅 13:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19228">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حمله پریشب به انزلی به نظرم بیش از آنکه یک محموله نظامی از روسیه را هدف گرفته باشد، از جنس حمله به تاسیسات راه آهن در استانهای خراسان رضوی و گلستان بوده و پیام تشدید محاصره و کور کردن بقیه کریدورهای حیاتی کشور را داشته است.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19228" target="_blank">📅 13:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19227">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اوکراین پالایشگاه نفت "تیومن" در روسیه را مورد حمله قرار داد. این پالایشگاه بیش از 2000 کیلومتر از مرز فاصله دارد.
استاندار این منطقه تأیید کرد که یک پهپاد به این تاسیسات اصابت کرده و باعث ایجاد آتش‌سوزی شده است.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19227" target="_blank">📅 13:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19226">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هدف قرار گرفتن یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/19226" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19225">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWp8SNerkCOIjLwO8ZrfgpzbQfzDx7CRT7ak1OGoj1DtGLyQY7vuTO-X3OebAhGP4kac8DCd7LTa_gmSnxm3BByrE0dG5AJnObNaUCp3qLgxmKIUyeUjw5k3yVNuAV3qZosBxx3PbiBwTkfhvcRWfIR-qG1fq1yqD5EWPFiGoiD6h7QEoFm-t48bQmOf4z-qbvr4uvXnjOz1Q2h_FziTJs0gIc56_f-MN-_dxCus0MYM9dDxZrk5BCb7cA_iQBpDvz4bS_lJGMvJwRPSz0SR7tQHQhnbnzy-F6NBFBOpPUcjavV38CE72bUvvVZYj5BQUZnx21N7wvU_qDtpYuk_lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهان سوم جایی است که در آن برای یک سری بوزینه دستمال کش بی عرضه برای راه یافتن به جام جهانی که 48 تیم دنیا در آن حضور داشته اند جایزه 350 میلیارد تومانی می دهند اما برای نخبگان علمی اش هیچ!</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SBoxxx/19225" target="_blank">📅 12:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19224">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جولانی اماده حمله به حزب الله می شود  شبکه کان اسرائیل به نقل از یک مسئول سوری گزارش داد دمشق آماده اجرای عملیات نظامی علیه حزب‌الله لبنان می‌شود.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19224" target="_blank">📅 11:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19223">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب و غرب اصفهان  مدیرکل مدیریت بحران استانداری اصفهان:  از ساعت ۹:۳۰ صبح امروز عملیات کنترل‌شده معدوم‌سازی مهمات عمل‌نکرده متعلق به جنگ رمضان توسط تیم‌های فنی و تخصصی ذی‌ربط آغاز شده است.  محدوده اجرای این انهدام کنترل‌شده، مناطق…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19223" target="_blank">📅 10:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19222">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">برای نخستین بار پس از ۱۳ شب متوالی، ارتش آمریکا دیشب هیچ حمله‌ای به صورت رسمی به ایران انجام نداده است</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19222" target="_blank">📅 10:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19221">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">منابع اسراییلی:   بازگشایی درب‌های پناهگاهای زیرزمینی نشان دهنده نزدیک بودن وارد شدن اسرائیل به جنگ با ایران است.  تل‌آویو در صورت مشارکت ایران در جنگ قصد دارد اهدافی را در ایران مورد حمله قرار دهد که تاکنون هدف قرار نگرفته‌اند</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19221" target="_blank">📅 10:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19220">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اگر این خبر درست باشد و اهداف نظامی ایران توسط کویت و بحرین که ضعیفترین ارتشهای عربی منطقه هستند هدف قرار گرفته باشند، یعنی اینکه عربهای جنوب خلیج فارس با راحتی بیشتری می‌توانند تاسیسات زیربنایی و غیرنظامی ایران را نابود کنند و اگر تا کنون چنین نکرده اند ناشی…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19220" target="_blank">📅 10:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19219">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">استانداری گیلان اعلام کرد   صبح امروز نقطه‌ای در بندرانزلی مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19219" target="_blank">📅 10:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19218">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بحرین و کویت با حمایت امارات به ایران حمله کرده اند  به گزارش وال استریت ژورنال در ۲۴ ژوئیه با استناد به افراد آگاه، بحرین و کویت اوایل این ماه به صورت پنهانی جنگنده‌های خود را برای حمله به اهدافی در داخل ایران به کار گرفتند که نخستین پاسخ نظامی مستقیم شناخته…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/19218" target="_blank">📅 09:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19217">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یکی از تأسیسات حیاتی عربستان در جیزان مورد حملۀ موشکی یمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/19217" target="_blank">📅 09:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19216">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یکی از تأسیسات حیاتی عربستان در جیزان مورد حملۀ موشکی یمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/19216" target="_blank">📅 09:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19215">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">برای نخستین بار پس از ۱۳ شب متوالی، ارتش آمریکا دیشب هیچ حمله‌ای به صورت رسمی به ایران انجام نداده است</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/19215" target="_blank">📅 09:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19214">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فرماندهی سنتکام ایالات متحده اعلام کرد که یک کشتی تجاری دیگر را که بارها تلاش کرده بود از محاصره بنادر ایران عبور کند، غیرفعال کرده است. این دومین کشتی تجاری است که از زمان بازگشت مجدد محاصره، متوقف شده است.
منبع: خبرگزاری آسوشیتدپرس (AP)</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/19214" target="_blank">📅 01:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19213">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">این یادداشت را دوباره بخوانید.  یک روند ضدتورمی عجیبی در حال شکل گیری است که طلا، بیتکوین، سهام، مسکن و ... را همه با هم نابود خواهدکرد. به نظرم اساساً پول عوض خواهدشد و آنچه بستر ارزش خواهدبود توان «جلب توجه» و تاثیرگذاری بر اذهان خواهدبود.  همان که آخوندها…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/19213" target="_blank">📅 01:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19212">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUJxoi6nEHUDIbpCxMClumPN7JOrgefq5Rexjtitzazj0RnfpiXBj_YknSZBCsYJFL_KTPFb7H3rlargfNCBVqY_5hQbzA5V6Kb0-RJx9rJqIwG-35EMtRmkyQCFCx3Nk71j3Md9Oka-u4BIK7ZKxRDwc1tXKzWKIlWYbbB63y2ShdJVLwtEHe8D2Z-_R1Bet28g0G_Z3P0AU_qe_6zr_dIb6jDUrsOHY_GR3ZeG3tTglc-vVIO6oWT2wEJtlP03OflBMBZSVHG9FLOG1oKtBu11KltRNU1yLAQ9VbHgLDyiwi_IpgtwiE8t3TFen03ftUz0bjrtBWO5LUJL9JHpKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح میانه ای قرار دارد و پیش بینی حرکات رفت و برگشتی و رنج همراه با نوسان برای طلا می رود.  محتملا بین رنج ۴۰۶۰ تا ۴۰۳۰</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19212" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19211">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌
یمن (منظور یمن تحت کنترل حوثی ها): حماقت عربستان تاوان سنگینی خواهد داشت
وزارت امور خارجۀ یمن: ما رژیم عربستان سعودی را مسئول تمام پیامدها و تحولات ناشی از این اقدام جنایت‌کارانه می‌دانیم.
رژیم سعودی به‌جای تسلیم در برابر مطالبۀ حق و عادلانه برای رفع محاصرۀ یمن، مرتکب حماقت بزرگی شد که هزینۀ زیادی برای آن درپی خواهد داشت.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19211" target="_blank">📅 01:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19210">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19210" target="_blank">📅 01:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19209">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/na4alCrJpEjNRgjGKmG0fTqGC-FskcK2ezvS4YYj3NT-pWuLIiH6SnFqgz-9aOX8ZVY0aku7f9_IusUBjLvsntFtfCmDBFfuKR7EN70A-ZbHy1x_9R3WkffNjfI9wV2ezx5p9wiHuHv0ovFYjP85H4RTyixwiIbhas0Zx-0uoDWGPV4gqu69B0vWBhk9liLvd1wNmEKOw4X6Q7i6Gh1MU_DPEq6HCD8KHjWfsCSSWVB_TdQGL4zmnrgS-n0w6PTAHgTC0h7fYSHm_4r631dqkAcI_WDR5qgi7vcsK2pfPNOLxd1rX62rQXkMRd2iFrcMfVQjXsKPWMWQ9xEubGOIWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان آتش‌بس ایران؛ ضربه‌ای مهلک به سرمایه سیاسی جی‌دی ونس   تا پیش از فروپاشی آتش‌بس میان ایران و آمریکا، جی‌دی ونس یکی از مهم‌ترین برگ‌های برنده خود برای رقابت‌های درون‌حزبی جمهوری‌خواهان در سال ۲۰۲۸ را در اختیار داشت؛ این ادعا که توانسته است در کنار دونالد…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/19209" target="_blank">📅 00:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19208">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">308 KB</div>
</div>
<a href="https://t.me/SBoxxx/19208" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 12</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19208" target="_blank">📅 00:51 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

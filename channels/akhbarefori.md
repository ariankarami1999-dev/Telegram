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
<img src="https://cdn4.telesco.pe/file/QNOjOX7QBytQ6vWu5Rzw5o-_PndxbAStToeN7ermZG4r5YuZTcs2mJRwDkYz2m30htpwX4f4NoTU7uLSbh_-vUFBHc9WsHZ_zhZh8cHwTmECSPbzoE3FyVmUFklxmCo3MzeJX7MmXHYtT-aHCKBHZ3JB3OtrGHJhJDlrEa5ukKmRBaqOBMOqaa9YrUrvuEeHX4Fzzcdj9rJVTrGXVUi59g3eRRQ8-UDEQreZ8VZQe2Ib4xjDCYmzYjpcpsVK2r-cm7hZzQ9GpzIVZfT4XI4qwFz2Apk9dcNIEJZvYgyVw_0Nq3gmFBqmChceX7Z1onFN4SLmKTXF_TIXqUutcEl7JA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.25M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 14:42:35</div>
<hr>

<div class="tg-post" id="msg-683314">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIiOINJjuDQ3rVLhTFlYdpFgHqdsieSNbC7vO3oit20FMrnaNpcsH6hNoJISZZl1-gMtQS4aSWUujJrivYanMiPYQJ3ql3LGT23oQQSLgpSEwUjROfIgOMtMv812PxwqbTLbZT1BM9mp_KXFxiz6RznDsG90bzTOeyyjy-wK1pip0Ej5YKfWV_F7Bs9bGJnHLDrZla05HhnmaP7ipGiYvdikpNUqs1C1M9UaR0LFRQMjRAR4vHub6HzbgMliTpkckiO18ubRmU0taB89u5rHAFkNXBOkAcZdPrhXIeo9ho2rpi5gKuA1F_ijpZsrDnW_DFIWKlxs4KFqyoFue2pfHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف ۴۱ جمجمۀ آهو از چاه آبی در شاهین‌شهر
فرمانده انتظامی شاهین‌شهر:
🔹
۲ شکارچی غیرمجاز که در یک سال گذشته بیش‌از ۵۰ آهو را در مناطق حفاظت‌شده شکار و ۴۱ جمجمه آهو را در چاه آبی مخفی کرده بودند، دستگیر شدند.
🔹
متهمان گوشت آهوها را به‌صورت غیرقانونی می‌فروختند و سر آهوان شاخ‌دار را نیز برای تاکسیدرمی در اختیار افراد سودجو قرار می‌دادند.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/akhbarefori/683314" target="_blank">📅 14:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683313">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر علوم:انحلال دانشگاه پیام نور منتفی شد‌.
🔹
زمین‌لرزه‌ای به‌بزرگی ۳.۴ ریشتر در عمق ۱۰ کیلومتری زمین، ایذه خوزستان را لرزاند.
🔹
آلمان حدود ۱۰هزار پناهنده در نیمه ابتدایی سال جاری اخراج کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/akhbarefori/683313" target="_blank">📅 14:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683312">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522b06e6fe.mp4?token=mB4-Zj8LYVGnxjqCrZIKCsPtDPzXMyuFiLAgAO11tStVFT9XWqk7abzZDbDidxr-994wMnmMrrYef8DtrgzE9zarRydDHZcESdi8BL7qlN4ROvF_EIv6urJsWxNrT-xwUC8P5W6-7XHnU9LY8hAiR1--p0e92bNOugdNaS9GW4rjUF6V3Lt6EOYJxGB4ag5iO1wZ9S2NgUUP3sAvU6a3s1bOTOiWXzCGeXk0Y5cKWxKtDMRuTLvTrC8CpHRvhRTr2JPPRBK9u_EPKMTPxmAeiqb4idAufQdGJ_wkYhO0NbU85cces4DAMP_u0q2MG6VQqJz30wXF9jwVtRtPgeXF3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522b06e6fe.mp4?token=mB4-Zj8LYVGnxjqCrZIKCsPtDPzXMyuFiLAgAO11tStVFT9XWqk7abzZDbDidxr-994wMnmMrrYef8DtrgzE9zarRydDHZcESdi8BL7qlN4ROvF_EIv6urJsWxNrT-xwUC8P5W6-7XHnU9LY8hAiR1--p0e92bNOugdNaS9GW4rjUF6V3Lt6EOYJxGB4ag5iO1wZ9S2NgUUP3sAvU6a3s1bOTOiWXzCGeXk0Y5cKWxKtDMRuTLvTrC8CpHRvhRTr2JPPRBK9u_EPKMTPxmAeiqb4idAufQdGJ_wkYhO0NbU85cces4DAMP_u0q2MG6VQqJz30wXF9jwVtRtPgeXF3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این‌طور آتش‌سوزی شروع می‌شود؛ وسیله برقی متصل به پریز ناگهان شعله‌ور شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/akhbarefori/683312" target="_blank">📅 14:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683311">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d662816f83.mp4?token=cj8YvCKYyMB1a7JP7F28G7_diKJTabCXI6uGTtTJA-9dfvEdOMEImYjdEDzwwAVxztggACgK8IyyV8CKyFj-L181A151pnDP7HZki55EsU4QRhbxWh2xtZvQuLlDSYLpd6L8z1yG-2InTNJNU8SH_ZkXHfaJ1Nb7KgXFZr6Zfe2amW7gnlmMs7WAEu_fp12ZMl9plSn9c12_A4MJHQ-2KpkBmSeX8iMXowoNkuwcv_f0Awpn-zzQRBOnC-vHdds8yHWvJIPM-yd_CbIU8UZ6W4YMh6mYPUXi_9p9wABcV05Da11h9fVQKv1ZzapQC-tIpRC4Y28iJeXHPR86-SscRoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d662816f83.mp4?token=cj8YvCKYyMB1a7JP7F28G7_diKJTabCXI6uGTtTJA-9dfvEdOMEImYjdEDzwwAVxztggACgK8IyyV8CKyFj-L181A151pnDP7HZki55EsU4QRhbxWh2xtZvQuLlDSYLpd6L8z1yG-2InTNJNU8SH_ZkXHfaJ1Nb7KgXFZr6Zfe2amW7gnlmMs7WAEu_fp12ZMl9plSn9c12_A4MJHQ-2KpkBmSeX8iMXowoNkuwcv_f0Awpn-zzQRBOnC-vHdds8yHWvJIPM-yd_CbIU8UZ6W4YMh6mYPUXi_9p9wABcV05Da11h9fVQKv1ZzapQC-tIpRC4Y28iJeXHPR86-SscRoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس ستادکل نیروهای مسلح در بازدید از یکی از تاسیساتِ زیرزمینی تولید موشک‌های بالستیک: دشمن باید بداند نمی‌تواند با ارادۀ یک ملت بجنگد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/683311" target="_blank">📅 14:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683310">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxAGgVmcA156ZnJfmZbz0JM6fQJHc07QYDZxPNVoaDMRPTJMRca934ep-dTfGHL2MDHh764eoQTAl6URy1vWSaTj4goBXbPQ_7mD8nlHlwcC7GnhJeKhusHk83d2iPVsMClVWPo7K_K9GBzStsEneVF9IMgsaHckrpcjM3Mxfu6Yji7nfa9cZnz0okANzbeXzHyweC70FBzS5qNbA2EUNsnpoZhmB5oKXYx6eQ-2a7cZ9g0TFgdvNgD-4u8ygkF8jcLRH8l6eZDQ_M_3DT-rOSOr8gPwcKDS8xdogk8k2ALtG7WGUsd3Y1GceLUzwWkDjbIndoZt4efycxzlm-4MNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصاحبه اختصاصی خبرفوری با پروفسور پل پیلار: ترامپ بی فکر است، ممکن است به ایران حمله کند!
استاد دانشگاه جرج تاون در
#گفتگو
با خبرفوری می‌گوید:
🔹
مشکل اساسی و بنیادینی که مانع از دستیابی به توافق می ‌شود، این است که دولت آمریکا و حکومت ایران هرکدام معتقدند می ‌توانند در فرسایشِ طرف مقابل پیروز شوند و بر این باورند که فشارهای اقتصادی ناشی از فقدان توافق، سرانجام طرف مقابل را وادار به دست کشیدن از تقابل و پذیرش شکست خواهد کرد.
مشروح گفتگو را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3239554</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/683310" target="_blank">📅 14:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683309">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سردار باقرزاده: قطر با حضور تیم کارشناسی ایران برای دیدار با خلبانان اسیر موافقت کرده است.
🔹
رئیس سازمان بسیج: آمریکا پس‌از شکست، به‌دنبال فشار و اختلاف‌افکنی است.
🔹
وزیر علوم: انحلال دانشگاه پیام نور منتفی شد‌.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/akhbarefori/683309" target="_blank">📅 14:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683308">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258f3e48da.mp4?token=qs3lpjSgeIStdV7EmK7FW8wmgsxD5k-Wl5Ha-ZVfgW_8dsP5DjIVP9HueXupxZR-4dgi6Nv38g_YFDjWwULML_QWEsEBZUfKKjNwrjcmsukxxSUENwbJ3Agc0O0xm4KWDZtKImqfCtdDY-cg_8H-bonoFm14VhECj4sqCRYDdvrjpCTN3FzadYMzEXrNQSvW-xPXfTcXjTTqi4OzmUTxqIYI6wyH7ifpGdvpNPXI5-io-rhnsUQPoykPbsqWSn3D8iXAm71eCsIdbLcCTws_cZhzKkNpvM3EbAAvuESASfNKCHm42o8MBgbfUmz9IMoCsGh2zzw6jWn6w2IQzPjtYJWYctfr-XQPjBvj7vRnx5SrJJL9IVe9Gzx9cyOyrrme4KwZAjKi8BqyUEbklfyqFoHxjwuYoWM63eEowZsqAZFMyZYNsnnTC2zRBxYUCazirh_QW0vai5LKI9U2A8YFhcLwrMZWUdv4rrG1AWN2eudlgrn24acmswftTtN6K5iqcP6Kvi9ReL4X-w7vPehDEshbFvknMe-7aPZ2ZolYdApvq4r7PXOI2KPf1tIHBcMmn7xE7Fn6KD5XmySFW3OMxB3ITOkHLOnfxf84hHs7u4Na5lXAPiIyhGZz4KWevK9CCiCfUKE85SCahG5LD1daZniK4-EGvWuoDCYaeCngNAM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258f3e48da.mp4?token=qs3lpjSgeIStdV7EmK7FW8wmgsxD5k-Wl5Ha-ZVfgW_8dsP5DjIVP9HueXupxZR-4dgi6Nv38g_YFDjWwULML_QWEsEBZUfKKjNwrjcmsukxxSUENwbJ3Agc0O0xm4KWDZtKImqfCtdDY-cg_8H-bonoFm14VhECj4sqCRYDdvrjpCTN3FzadYMzEXrNQSvW-xPXfTcXjTTqi4OzmUTxqIYI6wyH7ifpGdvpNPXI5-io-rhnsUQPoykPbsqWSn3D8iXAm71eCsIdbLcCTws_cZhzKkNpvM3EbAAvuESASfNKCHm42o8MBgbfUmz9IMoCsGh2zzw6jWn6w2IQzPjtYJWYctfr-XQPjBvj7vRnx5SrJJL9IVe9Gzx9cyOyrrme4KwZAjKi8BqyUEbklfyqFoHxjwuYoWM63eEowZsqAZFMyZYNsnnTC2zRBxYUCazirh_QW0vai5LKI9U2A8YFhcLwrMZWUdv4rrG1AWN2eudlgrn24acmswftTtN6K5iqcP6Kvi9ReL4X-w7vPehDEshbFvknMe-7aPZ2ZolYdApvq4r7PXOI2KPf1tIHBcMmn7xE7Fn6KD5XmySFW3OMxB3ITOkHLOnfxf84hHs7u4Na5lXAPiIyhGZz4KWevK9CCiCfUKE85SCahG5LD1daZniK4-EGvWuoDCYaeCngNAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ست‌های رنگی خاص مخصوص آقایونیه که می‌تونن شهر رو زیباتر کنن #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/683308" target="_blank">📅 14:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683307">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LL2iONv3lmzKtsjxJiTeUVd0OCFVPhGYaSQZoeVfBkk3SKvXmgjrAOs5vmpECDQeLz7f_HAES-TAMWY7ooiYp6eL39Mktcb9uabRJS_GQ93kYF6XmT0_gC2K4fFl4QAYfOgvSPS9Zzhb-SaZcaU7i0wLc58JF5zttElxkYbpSZ_QzmDHWvH9GU2e2YUlhPD3YLx1Gy2axHB86MdcuA8mO6HqCq8xwGA2uQo4cQ6tQUizEg9Mpt423rsFNvLE1Z9RHKBl8MzyROdWpNltSB8sBW_6zjmEqQy3Ww2eZaxcZJPcFJp3XFByeDZksNzi35jr6Jr2VrVVr_CmLr-BjG2TzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت قالیباف از بی‌اعتنایی کشورهای منطقه به اظهارات خصمانهٔ ترامپ: پیام‌های متعدد برای شکل‌دهی ترتیبات امنیتی و اقتصادی جدید دریافت کرده‌ایم
رئیس مجلس شورای اسلامی:
🔹
ما پیام‌های متعددی از کشورهای همسایه درباره شکل‌دهی به ترتیبات امنیتی و همکاری‌های اقتصادی جدید در منطقه دریافت کرده‌ایم.
🔹
ایالات متحده امنیت تک‌تک متحدانش را با قلدری و بی‌اعتنایی مطلق به منافع آن‌ها به‌خاطر منافع اسرائیل چنان به خطر انداخت که آن‌ها برای لحظه‌ای، تمام هستی خود را در خطر دیدند. یک نظم بومی و مستقل که واقعاً صلح و امنیت را در منطقه به ارمغان خواهد آورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/683307" target="_blank">📅 14:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683305">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a425c60cf9.mp4?token=hpGlwEuxfGiQ0IhBsjeXIaotRg4O5kldZAKC2k971FWTwdcJJYu4bxCEEKWcv4TLH1jF4QXuRQIGficj6FdXwo_Jy5dZKzoiFkCiemVsghXRZx4PsZ2A256pmt7w79-1akBi0UfwG88Tzcca4p8Kw-smU5gsxJp-jI9-curXupPqaZc90_-7TrJ3yrpYC6hHUmB4YNG1b_qosEf9jxHMy7KYtznFWoQioSdsJ4_3DzJx8ctHmAxWSFLhSjn5ZKs1tuv2fMz0fyvoCZKur7P30gL0g4EByngH0UaeT0vzxVrB2mQJNnS92QmQkap4WY9LlWdfOPYq0ZozvZc0XeA8B4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a425c60cf9.mp4?token=hpGlwEuxfGiQ0IhBsjeXIaotRg4O5kldZAKC2k971FWTwdcJJYu4bxCEEKWcv4TLH1jF4QXuRQIGficj6FdXwo_Jy5dZKzoiFkCiemVsghXRZx4PsZ2A256pmt7w79-1akBi0UfwG88Tzcca4p8Kw-smU5gsxJp-jI9-curXupPqaZc90_-7TrJ3yrpYC6hHUmB4YNG1b_qosEf9jxHMy7KYtznFWoQioSdsJ4_3DzJx8ctHmAxWSFLhSjn5ZKs1tuv2fMz0fyvoCZKur7P30gL0g4EByngH0UaeT0vzxVrB2mQJNnS92QmQkap4WY9LlWdfOPYq0ZozvZc0XeA8B4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین موشک ماهواره‌بر تایوان قبل از رسیدن به فضا منفجر شد
🔹
اولین موشک پرتاب ماهواره داخلی تایوان در اولین پرواز آزمایشی خود با شکست مواجه شد و به جای حرکت به سمت دریا، به سمت خشکی و کوه‌ها منحرف شد، قبل از اینکه سیستم خود تخریبی فعال شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/683305" target="_blank">📅 13:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683304">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c6e0c64bd.mp4?token=T5y_WZy2tNiAg736eFkjnlPRQg3AHRmJWsZE3m7JgDQOLaVW04l7JRvBLMuLB-unzuqXGVHTtix97XdZdIrjSBjwxYslXn0Z23aD4KVfqlKJgOPahwOfIILVTPQpfpDLCgmXIKWpnKNms_PBotHvXkJkVef8ZybQgOcy0F5PaUlKh8WaE1eASoFGidlXy5J_Y243BcrtIcpOpx9L9d9R-8kLkHXi6HQQXOmIGEXE0wSo0D5h2L2GtxHLmF701mOVyCBib0St_x5VlTm0afA_mGsU_ANBsdIq8-5tUFJRVPiM6R5bGDWvcli6HLnc_6u2_lyosF381EiwkyLMOupqWhXtEOPC3U_BvgOnmaaQQuuZGCKfYfGVrf9XvwdREwFhyTPA93qALWKexIh-8bBmUO1O61VHcbOgKcZi85eYb3JdLnltQICCV6YT7lIHJ5IRWG1D9i2zki7_6n_HgIc-hDM4wpKlI3sCTxuQsKrnjipbMn4AJf29dFc__xg1u81dAJrBgs1nZOfHvbG1ygk6SjkbBOm1y82e0XpzP8-IDQC7YoGQtVZRgIz-RNn5f7iebwhVlZGGnut42Y4hLVXSPg4vX2BBR52nyO3yLpzOgb6IE6JujSHQEpAiuFiVdMSxLBLFoSyhZxPZPmBVViasCcGaL0V6eWVkKUiy_L0wqtk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c6e0c64bd.mp4?token=T5y_WZy2tNiAg736eFkjnlPRQg3AHRmJWsZE3m7JgDQOLaVW04l7JRvBLMuLB-unzuqXGVHTtix97XdZdIrjSBjwxYslXn0Z23aD4KVfqlKJgOPahwOfIILVTPQpfpDLCgmXIKWpnKNms_PBotHvXkJkVef8ZybQgOcy0F5PaUlKh8WaE1eASoFGidlXy5J_Y243BcrtIcpOpx9L9d9R-8kLkHXi6HQQXOmIGEXE0wSo0D5h2L2GtxHLmF701mOVyCBib0St_x5VlTm0afA_mGsU_ANBsdIq8-5tUFJRVPiM6R5bGDWvcli6HLnc_6u2_lyosF381EiwkyLMOupqWhXtEOPC3U_BvgOnmaaQQuuZGCKfYfGVrf9XvwdREwFhyTPA93qALWKexIh-8bBmUO1O61VHcbOgKcZi85eYb3JdLnltQICCV6YT7lIHJ5IRWG1D9i2zki7_6n_HgIc-hDM4wpKlI3sCTxuQsKrnjipbMn4AJf29dFc__xg1u81dAJrBgs1nZOfHvbG1ygk6SjkbBOm1y82e0XpzP8-IDQC7YoGQtVZRgIz-RNn5f7iebwhVlZGGnut42Y4hLVXSPg4vX2BBR52nyO3yLpzOgb6IE6JujSHQEpAiuFiVdMSxLBLFoSyhZxPZPmBVViasCcGaL0V6eWVkKUiy_L0wqtk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پلیس تهران نوزاد ربوده‌شده را پیدا کرد
اظهارات عجیب متهم دزدی نوزاد دو ماهه در تهران:
🔹
علت اینکه بچه را به خانواده دیگری دادم، اختلاف پدر و مادرش بود
🔹
پدرش اعتیاد داشت، حالا می‌گوید ترک کرده‌ام و بچه‌ام را می‌خواهم
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/683304" target="_blank">📅 13:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683303">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg6vYRemfVeoXrrttijKP6O2WaA8prszl3-ms2xCION_DM9OksBa1r3NG_MBu9aLEAeR8XAYQR60N4Z40hwHJvaoZyxqu5Zq1qgZ7MNoBkwJcuaU_EdNc_ZFAriyqofYiZpxxVXBXIkcd4riMxjSfFh-a3Wj7V7f0JmFivPpgZLuOx2hYxqNEPNofA97VvNcvYz9eGtnMbSqZkWwg-xNau69BAjlIHbfzwU5qSuRQBAbraJYMHeHm7aiu0kgn-hMnbFuNn292DluyXTeJsgVJAw03SakRm2D7WZfgKVaBXgD4LwQub_OwAOCL1f3W6Go3OYk491L-Lql0foJGz0yOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کمتر از یک هفته، قیمت جهانی طلا بیشتر 15 درصد رشد دلاری داشته است.
یکی از امن ترین شیوه های خرید طلا، خرید صندوق های طلاست که برخلاف پلتفرم های طلا آنلاین که ریسک خالی فروشی دارند، صندوق های طلا زیر نظر سازمان بورس فعالیت میکنند و ریز تراکنش های آنها تحت بررسی و نظارت قرار دارد. آنها ملزم هستند تمام سکه و شمش خود را در انبارهای بانک و بورس کالا نگهداری کنند.
صندوق جام_طلا از گروه مالی فارابی با قدمت طولانی و عملکرد مثبت خود از صندوق های طلا مطرح کشور هست که از طریق لینک زیر میتوان معامله مطمئنی و امنی روی آن انجام داد:
https://ifrb.ir/tlt3</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/683303" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683302">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42d0c904ac.mp4?token=hkG8LCRRFgc6O_VOJOPTa_X5pqiuCgGmxnd_5SpNVwhM3i54Nx-TYeQQbHVZ616cXKJcrC40YXV-knODEYx21eA0ipvOVB5FjPiB7q-tVyiUm4OQjD5hUGE8wcD_yYBWbMCqI07Ter0V_0zkJwZtQZ-zThGj7_aqR9_nao-487QQPPLkQqeiF5q0zbo8ZRAlz0IAhWptz3rAwEqXD84bIlM7k4k3ZwAt-FXrAC0H0ZthbdtHbrrPTF2usxz2q_gO5xRLCmLxiL7LsTvOxAMlaZmovN2ZGr91pT6CkDsBa9HjElvAcGQjWIohRYJVBM2Mrs8eXAitPuoEPSW6M4mM9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42d0c904ac.mp4?token=hkG8LCRRFgc6O_VOJOPTa_X5pqiuCgGmxnd_5SpNVwhM3i54Nx-TYeQQbHVZ616cXKJcrC40YXV-knODEYx21eA0ipvOVB5FjPiB7q-tVyiUm4OQjD5hUGE8wcD_yYBWbMCqI07Ter0V_0zkJwZtQZ-zThGj7_aqR9_nao-487QQPPLkQqeiF5q0zbo8ZRAlz0IAhWptz3rAwEqXD84bIlM7k4k3ZwAt-FXrAC0H0ZthbdtHbrrPTF2usxz2q_gO5xRLCmLxiL7LsTvOxAMlaZmovN2ZGr91pT6CkDsBa9HjElvAcGQjWIohRYJVBM2Mrs8eXAitPuoEPSW6M4mM9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غاری که دری مخفی به اعماق زمین است!
🔹
لاگوآ میستریوسا استخری طبیعی است که هرچه پایین‌تر می‌روید، مرموزتر می‌شود؛ عمقی که تاکنون به‌طور کامل کاوش نشده و همین ناشناختگی، آن را به یکی از جذاب‌ترین مقاصد غواصی جهان تبدیل کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/683302" target="_blank">📅 13:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683301">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بانک مرکزی: کارت بانکی ویژه گردشگران خارجی در ایران صادر می‌شود.
🔹
با حکم رئیس قوه قضاییه، حجت‌الاسلام‌ والمسلمین عبداللهی به عنوان دادستان انتظامی قضات منصوب شد.
🔹
گرما در اروپا حداقل ۳٠ هزار قربانی گرفته است.
🔹
منابع خبری از منفجر کردن خانه‌های مسکونی در شهرک «کفرتبنیت» در جنوب لبنان توسط نظامیان رژیم صهیونیستی خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/683301" target="_blank">📅 13:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683300">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
محدودیت سفرهای زیارتی گروهی در سوریه
🔹
منابع محلی در سوریه می‌گویند مقام‌های رسمی این کشور، به‌دلیل ناتوانی در تضمین امنیت زائران، فعلاً تنها با سفرهای انفرادی برای زیارت اماکن و مقامات مذهبی موافقت می‌کنند و سفر گروهی همچنان با مانع روبه‌روست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/683300" target="_blank">📅 13:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683299">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PejObsnjPXGyDjOC_ioOHBnJDK5ivwZY78rGMaAYfi17Si_etSSpOcaJPoOs7gdG7LOjzJmJ5JyEs9VO-cT35tM_eMZrOVutlZ1MdCacuF3K1ZJCxQVBNXo8wWD_X9pUozgjfncSe71LT11NJ9i0Uiwr3sFj9Xx61v1aznyH6abmfD-qV5wQW3zwz1eqFJ6tKfrWrmV58Na40MnQe42i9nEjlVEbAtbvRyvaMQVZEuZwRdnwXa5nU6vToQnKFWHQSPP3Qs1Jl2LAwy1kOi9nbDw0Jkmh6OyovnWaexAYtEOh3e9QYFu6FaYywRSsiy_hfNl4ChWeNZiNAc6kL5gQGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزانه به اندازه یک کلاس درس، کودکان غزه شهید می‌شوند!
🔸
اسرائیل به طور متوسط ​​روزانه ۲۸ کودک -به اندازه یک کلاس درس- در غزه را به شهادت می‌رساند.
🔸
از ۷ اکتبر ۲۰۲۳ تاکنون در جریان نسل‌کشی اسرائیل، دست‌کم ۲۰ هزار و ۱۷۹ کودک فلسطینی در غزه به شهادت رسیده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/683299" target="_blank">📅 13:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683298">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f04d9628.mp4?token=aKa_BF8ucvjf_s6UiCvvZtWKJBF8_-x5Byzc_K6JbMMiLeP_NnozC8l_L9zHurOoKQgIWTSaKPCsh6NM9-DYw2fjDX8iKgPxwPBwJkYwxr8tW-bqDybjr6zimRP1j7V7XYBFiJJyrMAaTIRXUxTU7i2l5w_55aHnnRdvghOTp_b6umOLLXf2QnchzX2mw0yrBMPn0l_h7_4HZkOdgzUfvFHk2TFSHc-usQHYsa4nwrt97NxZd7l2j4jXF7TiklUBxzOK111og15_bITDut8dTaoHfbATKxPVUmzJDGFZ3Cgd1wndJlRFs97aiO-_62eBYlPdvLriVIGNTf5UPlkglw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f04d9628.mp4?token=aKa_BF8ucvjf_s6UiCvvZtWKJBF8_-x5Byzc_K6JbMMiLeP_NnozC8l_L9zHurOoKQgIWTSaKPCsh6NM9-DYw2fjDX8iKgPxwPBwJkYwxr8tW-bqDybjr6zimRP1j7V7XYBFiJJyrMAaTIRXUxTU7i2l5w_55aHnnRdvghOTp_b6umOLLXf2QnchzX2mw0yrBMPn0l_h7_4HZkOdgzUfvFHk2TFSHc-usQHYsa4nwrt97NxZd7l2j4jXF7TiklUBxzOK111og15_bITDut8dTaoHfbATKxPVUmzJDGFZ3Cgd1wndJlRFs97aiO-_62eBYlPdvLriVIGNTf5UPlkglw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چه اتفاقی در پس‌زمینه تعویض دنده رخ می‌دهد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/683298" target="_blank">📅 13:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683297">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
انتخاب ۲۲ بازیکن تیم ملی امید ایران برای حضور در رقابت‌های آسیایی ناگویا ۲۰۲۶
🔹
محمد خلیفه، ادیب زارعی، آرمین عباسی، امین حزباوی، مسعود محبی، دانیال ایری، یاسین جرجانی، فرزین معامله گری، سهیل صحرایی، ابوالفضل کوهی، امیرمحمد رزاقی نیا، قاسم لطیفی، پوریا لطیفی فر، مبین دهقان، یوسف مزرعه، عباس کهریزی، اسماعیل قلی زاده، امیرحسین حسین زاده، مهدی جعفری، سعید سحرخیزان، رضا غندی پور، کسری طاهری و پوریا شهرآبادی.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/683297" target="_blank">📅 12:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683296">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MF8nwSDplFXB71yYk5T0okUm0VWuJ4EiAzp_4D4_EciLOa6V96tIApRWIOI64rfnI9DqEcGcbPKmvTFUxOYLIKpyxQRbQg2FByG1KqGtwCVABghfT1QnrMoyqxc58uwylGsh2sVaP2UdqMfH3K5vEZ4UlU4HR0nILCrUFvQUfUsyrKuJGyoazY7l4Ja5ubYmM2pbjayXeUs3ALXxNdOAT5nipQX95kQIWWrcHLSipX87DSNk8PX5Meyk5Kz9lrw_TNbixY3v3RyYK6RsKmMbaUJMV3SyZUO6AX0jAeZSTuP3Kfuhl-W0QRMWh9Oz2drzig9lUYrpkmF3BLc2mgrKrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۳۱ مرداد ۱۴۰۵؛ ساعت ۱۲:۳۰
🔹
دلار آزاد امروز به ۱۹۰ هزار تومان رسید و طلای ۱۸ عیار با جهش ۶۵۷ هزار تومانی، هر گرم ۲۰ میلیون و ۵۵۸ هزار تومان معامله شد.
🔹
این بالاترین قیمت طلای ۱۸ عیار در سال جاری است؛ رشدی که از صعود همزمان دلار و اونس جهانی طلا حمایت می‌گیرد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/683296" target="_blank">📅 12:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683295">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
تعرفه ۵۰ درصدی آمریکا بر کالاهای کانادایی/ کانادا: تلافی می‌کنیم
آسوشیتدپرس:
🔹
پس از شکست گفت‌وگوهای تجاری میان واشنگتن- اوتاوا و اعلام اعمال تعرفه ۵۰ درصدی بر کالاهای کانادایی از سوی واشنگتن، مارک کارنی نخست وزیر کانادا از اقدام تلافی جویانه دلار به دلار خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/683295" target="_blank">📅 12:47 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683294">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEJUSZmGD8gD5x-sj-G9CDi3S-nR5D8imqUIMV-Yq-dASLTqeZk0KtVMv_CyE9Tb6zkT7v16fWcrIZEiljh0gT3dRQ_c14zNqCxo2Cct_25kQHIwAkU-0okWyOKlezsTU58am66t9zK8TLMi_tpHOORiEqkxNSBjPkAfJom8qf-tcBeLVmSSDfeEBg2Ys7qOA6G-UZ7zgJIeU0dlGc3Frhwybs_ghv0KLfarQysHNu-6iRVAOwPdlBjSI2wJNEOJpt11gdwZXENemU7XWza12_KlPO6BYJgkFOU4WGxA75OL-ew8ktrClwAwKBv1IvIcsY2fB0l6Xs0VJ4fXmVRXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس بالای ۶ میلیون ماند
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۰۹ هزار واحدی به ۶ میلیون و ۶۲ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/683294" target="_blank">📅 12:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683293">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-bNEWOXLRYVMIomlOWGJRA1FKG9skD-yNxZjhNX9YAh-cpSewYIktKmaHdpr5JGzQ1qeLN9iRJ7jL3Tmd-PDVakrHGk84zXN6DKn1s_cIpvmuTaN4ITUQAjAqIz0tLJKtGefA4WshOlGxDttEAV3rtjxhrYkJmkPHP4HL9BFZXdkP-8lVGMqAWGAIVKJezk6mjP4GapSfjbate-pDUbmkRrVyMvi_c6xRHtULbAr76-mBRNtlS59L8g6UW83FkrDRc1_eCcZgitHa-EoagUxFfFtXdsyPQ6x87NnAwtWGwSnyJCEEXhHzZbavwfxoEgm_b0l2qqpGTlhImveOO-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: ترامپ خواهان دیدار دوباره با کیم جونگ اون است؛ کره شمالی: به این زودی‌ها نه
🔹
ترامپ می‌گوید قصد دارد اواخر امسال با کیم جونگ اون، رهبر کره شمالی، دیدار کند. اما پیونگ‌یانگ به این پیشنهاد با سردی واکنش نشان داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/683293" target="_blank">📅 12:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683292">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a225862f30.mp4?token=fGy6zVVmg7zImmdkXHeqZVW2RF_vyViGUQJWJ3POoU4z_HnEuCb5pQ8oZpb8ItYqvLRn8t8su3AaFsIwS8Uuepl_HGcflID0SpBKEvN3HdLpoYEUPGkS1dNsi3NS9RKwj9xbH5UvOoIZUtSGQrAk9GlFPO86yDI7qcuy1cw-aCCxKC5EGJDj9CQ7SlTu3TnCo53lediOhfj5Jok-6r-qx1EwV-zoTPmnhj5ksJR3H7mjfMBcR3R9weh8bxMmGyGj_ojuN7dlBgVL1PAISrHiXiQF42GEmbcIDNRN-QbOyi_Ej7vZZZX7jH8MN0-HIoZvpQr9i9RXWfYe1SDvNid_2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a225862f30.mp4?token=fGy6zVVmg7zImmdkXHeqZVW2RF_vyViGUQJWJ3POoU4z_HnEuCb5pQ8oZpb8ItYqvLRn8t8su3AaFsIwS8Uuepl_HGcflID0SpBKEvN3HdLpoYEUPGkS1dNsi3NS9RKwj9xbH5UvOoIZUtSGQrAk9GlFPO86yDI7qcuy1cw-aCCxKC5EGJDj9CQ7SlTu3TnCo53lediOhfj5Jok-6r-qx1EwV-zoTPmnhj5ksJR3H7mjfMBcR3R9weh8bxMmGyGj_ojuN7dlBgVL1PAISrHiXiQF42GEmbcIDNRN-QbOyi_Ej7vZZZX7jH8MN0-HIoZvpQr9i9RXWfYe1SDvNid_2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۹ ماده غذایی برای پاکسازی ریه‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/683292" target="_blank">📅 12:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683291">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
حکم نهایی نظام وظیفه؛ بیرانوند از مهرماه سرباز است  سردار زاهدی، معاون نظام وظیفه عمومی:
🔹
علیرضا بیرانوند از مهرماه ۱۴۰۵ سرباز خواهد شد و دیگر امکان بازی برای تراکتور را نخواهد داشت./فرارو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/683291" target="_blank">📅 12:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683289">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAz-F48E2WYkZd8bYoKBRGfnD5NyWFeX3fnLqDJ0U46nYUPtwqfsxD3RaN4se2Lyf-h_Sag56M5qr1LAIwXfo7cbQmdKfW9Mpj6q4didOdGVTOyfrum-7KMnILJ_CNxtIMTdF44vlucMcnq9WYfl6LJvvLD3kn9LzxHYO8XhNTOfIstIXH6xabvmd8Ytq2kDkThiBYGEmNjz2wtvTKPTckW6XYWnRDXz93ng9D2l8Jpnnoatgi_N6mchPs0vwjM0EZTyxHRz5qzrWOVIyd1ZhSFWFNXhI-MmxQFj-f3jMahJ6QTeOwmFBrDCHEzPA7Mr94K_3eMCveQPdZtu0Q8n8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
معماری و تزئینات منحصربه‌فرد مسجد نصیرالملک، شیراز
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/683289" target="_blank">📅 12:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683288">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی هیات رئیسه مجلس:
جلسات صحن مجلس در هفته جاری مجازی برگزار می‌شود./ایسنا
🔹
سایت و اپلیکیشن فوتبال ۳۶۰ رفع فیلتر شد.
🔹
فروش کتب درسی دانش‌آموزان خارج از سامانه‌ رسمی ممنوع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/683288" target="_blank">📅 12:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683287">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e615f58192.mp4?token=QJBtTsaOUtp03OXywEIyOgyuMseETZrsJRnjK32h4u-0vdif0lz6f3NuXfNzDg7lcx1txBdMKYI6fX-oZq-QJkGyuqppzRJHMk4MP-EHLlVAgcwkonaPhF01KEJaR_9Q2Hs9u4lm4SpoP-_ByoOrVevzgvsIiYjtxzLoLqw9FNK3JfIb9guiC3pdxn_hfbpN0ltK55ARU_Lj2V3zfGYURMIMZjnVRjibzMQFgn3XAHzV_hShY-Kn8ZZhGFnpXL4UPXvOoen1ZCme9MvcAVIjuPLXgRfTOB4hD9LkWzmaRtDYJ3OnFv7lgCIHwnN2VwpinChz3cD6LNi_zo9PHa1EMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e615f58192.mp4?token=QJBtTsaOUtp03OXywEIyOgyuMseETZrsJRnjK32h4u-0vdif0lz6f3NuXfNzDg7lcx1txBdMKYI6fX-oZq-QJkGyuqppzRJHMk4MP-EHLlVAgcwkonaPhF01KEJaR_9Q2Hs9u4lm4SpoP-_ByoOrVevzgvsIiYjtxzLoLqw9FNK3JfIb9guiC3pdxn_hfbpN0ltK55ARU_Lj2V3zfGYURMIMZjnVRjibzMQFgn3XAHzV_hShY-Kn8ZZhGFnpXL4UPXvOoen1ZCme9MvcAVIjuPLXgRfTOB4hD9LkWzmaRtDYJ3OnFv7lgCIHwnN2VwpinChz3cD6LNi_zo9PHa1EMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در یک دقیقه با خطرناک‌ترین بیماری روان‌پزشکی دنیا آشنا بشین #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/683287" target="_blank">📅 12:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683286">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
آخرین وضعیت پیگیری وضعیت سه خلبان سوخو  سخنگوی ارتش:
🔹
همان‌طور که قبلاً هم اعلام کردیم، ما به طور جدی خواهان روشن شدن وضعیت این خلبانان عزیزمان هستیم.
🔹
اقدامات حقوقی از طریق وزارت امور خارجه و ستاد ارتش با طرف‌های قطری و طرف‌های بین‌المللی انجام شده و این…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/683286" target="_blank">📅 11:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683285">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b2ac23bf5.mp4?token=fNdP8OMo9SMLU92nNfT_kgz5f3d_yqFP9_kvf4-MlVoRiNlOM6FCp9zBkdgL942Idkw2il3YWXWGMC23Y4i_dQKbPPxwdaLCOYSUnx4xZzUiToghy_4p0YwbIVVAANzhejYyjd64WIUdP-xQvZ1-zjkUw0tx53dEk6nqzaBQLAopzsDm929X_mER2fpmv2FvbOFB6FSadKgLxCYGnuTrfbGwKSKx_FpbQfNOQp0oUCsmv3TQ1c9LszQJPCwKj6WL1pg7KwdFL2FCVUTqRH5QAoBgqngAqiy4V3W_n7NeZdYUdx1MiH5HpDDMXl5h4cByhu-l0nNTBO6TAfQVIYXR1DmVgMFZuxUitUdUziGhXXakhzoJXaok4ubyHrQw8G7sikT062tH2aXyAjyWdCX4QWp6kWD0VtIUsx0yDUdENvknzmv5Eo9lHvQ1tW7A5nCQtOX18FOxYZTL2ECe5V8vGlfii6NzB76odLaCU7SsJ3jh6e-UaJZj-WsEQWoCoF_8yQ2LvdLfC-ZqLAITgbcKnTX_L0_M27rnxr4BE706ASXw2yGrC0i_IZ561kaMtKlEj4BIlLiTazC8pAxHEA7PMGNzfyjXT3iyd2qXEq9qoMGquwZnQusLZDx6RIBkIo2AuIya2-aV9X5eQNHDSu4hhtOnEEIC5XNiHYEwLIDllQY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b2ac23bf5.mp4?token=fNdP8OMo9SMLU92nNfT_kgz5f3d_yqFP9_kvf4-MlVoRiNlOM6FCp9zBkdgL942Idkw2il3YWXWGMC23Y4i_dQKbPPxwdaLCOYSUnx4xZzUiToghy_4p0YwbIVVAANzhejYyjd64WIUdP-xQvZ1-zjkUw0tx53dEk6nqzaBQLAopzsDm929X_mER2fpmv2FvbOFB6FSadKgLxCYGnuTrfbGwKSKx_FpbQfNOQp0oUCsmv3TQ1c9LszQJPCwKj6WL1pg7KwdFL2FCVUTqRH5QAoBgqngAqiy4V3W_n7NeZdYUdx1MiH5HpDDMXl5h4cByhu-l0nNTBO6TAfQVIYXR1DmVgMFZuxUitUdUziGhXXakhzoJXaok4ubyHrQw8G7sikT062tH2aXyAjyWdCX4QWp6kWD0VtIUsx0yDUdENvknzmv5Eo9lHvQ1tW7A5nCQtOX18FOxYZTL2ECe5V8vGlfii6NzB76odLaCU7SsJ3jh6e-UaJZj-WsEQWoCoF_8yQ2LvdLfC-ZqLAITgbcKnTX_L0_M27rnxr4BE706ASXw2yGrC0i_IZ561kaMtKlEj4BIlLiTazC8pAxHEA7PMGNzfyjXT3iyd2qXEq9qoMGquwZnQusLZDx6RIBkIo2AuIya2-aV9X5eQNHDSu4hhtOnEEIC5XNiHYEwLIDllQY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا داخل یک چاه آب رو دیده بودید؟ چیزی که انتظارش رو ندارید!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/683285" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683280">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dqh-OwzJFWJdqFqIo2pOvVt0dNGMJupqvdHiaMcC7xdwgTTFJtuJ4ZJhQJq_hUHpqGIZVwVVqOAdezsnBOcRVuylQICn4rGJyVxD_xLqAMfDdxkfCqeLYmL0hs9YWZNR_YuQoWrvpzT3UD28f2pimhnEmRDewKWFddNWYQA9w3ROSQoXimFaQQyzB-Trp8_gYojHydsGU9rbIjVL6DOqS7wtB6-_HOhBKI-TaZf_vT7qyDyLyPdD_dtn1qizxbGGQB844i31YwF6FpduCbTamxtGpF_UOg5Y7QR009cVnA1mkNuy8xRCkmJYqXPpfU-vLiIagkKTDDpRouNc3KXO2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DVz0APPLpCPtLOrVB4sA-yCG5id7Y3sejmh6IjwawRJvjnTDVX_HfZdZzbM5oRSKRaQhmn83dJvQIIIa9MD4Hynngoqyfq3GDhKfJe-aFlcPPGsUYKkSwG_mz-f-8swphRs9Myu1zVI7bQ6yLh2WpFrj3NmDG9UKzIwtTFAC9C0JKCEuLp5S8v8CnUdvuyUW2mODla0ewDwVu86cmMjuXtw5qUqxxzxOF0R4n6H4WgPLoZi7o4ACuPOEMOemZX9xfp44zNJoSmtBvf9m7m-f-9_BIWJ2O0tHX731a9ly8epftC70TgG28wzuiFd1401AX8CWGpoyDTTYwWNNkbd5RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fV9kCUzlwIE33yKG4IiDqHu8IIZi6PzJBMskCzjpZZdwPXZrrod5gSargj0ZOhPZYBW2IAOiCsV5lVp6y1DFw3Koodllho2mlrhLOhfcjaMwnaJ3yeH_cpkv3p2Js-XgXLxyKh8oj1q40EXNbQTSi5ZNSC1XgtAuStWEvlL3zm_ZOgD1kL21alMZEUdkNMNP69lGn0qg0BHNV7YwPd44vZX4rJxvBqmWJYt4taHdjL_uHVfOxuQubFtiDpCjAZH9QUXCZ4AlImSNLreUpu0OHYXxWYB0d1fjjYRVYAYHi7zpY1Kdxv2gEsdA4wvyacgur6qOlPXKhjigFRy6s5LDdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LenxLHah1FhcBqq9_0VZXUgabltDLXvdOIpnSCvmsoF4K3x8hx9INgjFvtz-oCrSZrUet3yC3FFag4Y4uftsPX-zjbuZ9OlDIf_lCNedsw8v1W6tH-MTlIPPzBAFhXCxTY9DgsHZEdhQIl7K9oK76152oKpSjsOu1PF2OlTeTy82kTfO8r5xvZxDnD7YqIJX8QaD7STr5PWpdWlzp6tfwYnnLD7NP6n7WY8Cd-CJLHyd6CPQEhYvzkJiJyA25e8HDcPpVObxMn3WKrxfhetakA3b_gZ_NSS0UqtDJWdFrXkJSTMAlPSPxm1VigEoGcuFPz4n8N9__YM74U33K4KyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ofYHRdaEaI7oFH89w78EpVz9ImvfSzgkGLUHrP5xYKqdcCc2G7Gv_oSDpNq9coxypyz4YfyKSlWhALGUdX4hLNUPFPFBPkcqfhJjpPg-jiNpDggqmV4g5RcTeO9ydU3TwdiCZlOcNmjSsZrnECxzqkCOHrhveGwXIcJuhhR6sJDzGrKpcY-xcZEyDAtNb8gkHhqOBdjq2Mj1tXk0RJoUvbCxmJHg-doSXWbZxIOJgjO171BaaVHeq-aZxf2RY9QsaqzqBTL4XvenkwX4LoNOLtRd0nIU-rCcoLO4GqXKLEPRWyS9NT4jSvkq6SsLwQy7sGEcFppzd84bOfIr6mYtUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت اهدای خون در ایران و جهان
🔸
بررسی آمارهای سازمان انتقال خون و WHO نشان می‌دهد میزان اهدای خون در ایران از ۱.۷ میلیون واحد در سال ۱۳۸۵ به ۲.۳ میلیون واحد در سال ۱۴۰۳ رسیده است.
🔸
از نظر شاخص‌های کیفی، ۱۰۰ درصد اهدای خون در ایران به‌صورت کاملاً داوطلبانه انجام می‌شود، در حالی که تنها ۳۶ درصد از کشورهای جهان به این سطح رسیده‌اند.
🔸
شرایط اصلی اهدا شامل داشتن سن ۱۸ تا ۶۵ سال و حداقل وزن ۵۰ کیلوگرم است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/683280" target="_blank">📅 11:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683279">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2hgjDscBuGfstHKLgc1YX6bgfpO4w2BQmrG2eZAE8Q2YYHHePLOZTzZOghuQmqtZD76TbrpNO5JlO53rKt87SHs1o-obLP1_oQnre3Teo2UIvqwqTiJA9yV_kDntpqjuPoCgW7zPhRP2nryOYhiDnl5xELM2CrHq4pRDmPVln3BlqcKns0QKaKeufaIIfN2-jc36dpnOdhiuCCTaLOS5ajT-aQXSsRA9EV3S4Ln7ypLfDn_s92WVrHgR543RbDYdXbY2YeWzj8il73IKGY9nMhZrRM395nNdLCVfOMAA3RVGErhpwYUXiYyMnxcmD3_zVgrystF6o77rGoFVTINqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر‌ رویترز از کبودی انگشت ترامپ در‌فضای مجازی پربازدید شده. بحث مشکل جسمانی ترامپ ۸۰ ساله و بیماری احتمالی او در فضای مجازی به موضوعی داغ تبدیل شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/683279" target="_blank">📅 11:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683278">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c259796c9b.mp4?token=KM4LIgcFjgpPIPxl6Sm1CyAdZ31F3gluWxBQzzMF-MddCWs_p3qrtUwnmMDPUfmU6P25Ciqocy3pxHNvisNroINTeDXlVdrIroav9ZuaQPM8dclN21FYNMrEwbxBnIS_aSqxHSROr55OOyW5zb_ppDdKv4tqz6MQ1CSIYAsQBOnRtaGBa8UHl_IUK-yruCyvU0L3qywL7KJWJU9ADPt6buK2_aKmmNn1j-GS-58GmvIEkT8qoi6Yjd9MtmnyT5UM5qIqdGP6Y3ZwhEvQaw5uWfAvhIJOTrI-Ty2OMwarAMlxgJaUo8RsompjQBaSM7osZWTfo3j9q9z8Kj-DLK_6HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c259796c9b.mp4?token=KM4LIgcFjgpPIPxl6Sm1CyAdZ31F3gluWxBQzzMF-MddCWs_p3qrtUwnmMDPUfmU6P25Ciqocy3pxHNvisNroINTeDXlVdrIroav9ZuaQPM8dclN21FYNMrEwbxBnIS_aSqxHSROr55OOyW5zb_ppDdKv4tqz6MQ1CSIYAsQBOnRtaGBa8UHl_IUK-yruCyvU0L3qywL7KJWJU9ADPt6buK2_aKmmNn1j-GS-58GmvIEkT8qoi6Yjd9MtmnyT5UM5qIqdGP6Y3ZwhEvQaw5uWfAvhIJOTrI-Ty2OMwarAMlxgJaUo8RsompjQBaSM7osZWTfo3j9q9z8Kj-DLK_6HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات جنجالی استاد دانشگاه تل‌آویو در برنامه زنده بی‌بی‌سی: نتانیاهو برای حفظ قدرت خود حاضر به هرگونه اقدامی است و جان شهروندان اسرائیل برای او اهمیتی ندارد!
مئیر جاودانفر:
🔹
در صورت عدم پیروزی در انتخابات، به دلیل پرونده‌های قضایی جاری، احتمال محکومیت نتانیاهو به حبس وجود دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/683278" target="_blank">📅 11:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683277">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Epc-uflNg31xa3jrc0kepriAuJoMMpkNmJyLjMt-KeRsf7M3ubv0t6p_ErrCyqEP-ZAKdcgR4fL9lJXB2Pdu0QzsjnKe_jXSt65pzFUzbY2BscBxNB6hg33jJJ3MiCOV86pTihpsc3H7v6IskdKcYO5G6ZyXpnI4hSRmZDsh-GCh0ncYSXX0sF7HE5p5T8zFAE332VnJL-UGGahieRO2Y5rH3uYNEHaqCPDwoaLpzIECVSweQDOXQL7L6xf8Q9mloEq7yN7BI-B6iKQtnomhPo105Qw8cehUgGwfyo-foITW3lHTO-Xrznap-HrewcfLSyJ4dbzG89yWK9X5KGXyoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز مدعی شد: آمریکا روز دوشنبه تحریم‌های اقتصادی جدیدی علیه ایران اعلام می‌کند که احتمالاً خریداران بزرگ نفت ایران، از جمله شرکت‌های چینی، را نیز هدف قرار خواهد داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/683277" target="_blank">📅 11:47 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683276">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6_IN0xSss5oLeNrOt_75ieCwV_LUXPy-eZu2F6Zz6emkDeJokszYvDWc3d05QLrzAgC-wP6EFMEUwE9OulRGBsTU6RbEP_TMowGU9mCTGfK6MaiGnFTrEZa2C2XaCarYHz4SYknQmsdzb-M--6NKqQiNpse16lO8Q3UR_px5Wfp5vAPAR1xxcizP3-jm8zvwDcp5SYUFmuAESEqPhMHTzH_9-EU7WZOcYF7C8arg6MVF_jSE1ondGDtLhyQasroEneQQna2_f3y-Yrv_VvYkHIpGUCKckHaS60TX7Hbu5ItOSgSAA8S7O_GYH724ZbY6DTyGCrV4RMsF04ZmLUfHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ ویتامین و مکمل پرطرفدار و کاربرد آنها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/683276" target="_blank">📅 11:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683275">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای آسوشیتدپرس: مقامات مهاجرت آمریکا با ایران در موضوع اخراج ایرانیان همکاری کردند
آسوشیتدپرس:
🔹
ایمیل‌های تازه منتشر شده نشان می‌دهد که مقامات مهاجرت آمریکا با ایران برای اخراج ایرانیان در سال ۲۰۲۵ همکاری کرده‌اند.
🔹
صدها ایمیل رد و بدل شده بین مقامات مهاجرت آمریکا که توسط شورای ملی ایرانیان آمریکا به دست آمده، جزئیاتی را از نحوه همکاری دو کشور برای ترتیب دادن بازگرداندن بیش از ۱۰۰ ایرانی به ایران در سه پرواز مهاجرتی جداگانه ارائه می‌دهد.
🔹
این ایمیل‌ها نشان می‌دهد که مقامات ایرانی تا حدودی بر اینکه کدام مهاجران ایرانی به کشورشان بازگردانده می‌شوند اطلاع داشته‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/683275" target="_blank">📅 11:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683274">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
توقیف ۱۱ شناور حامل سوخت قاچاق در میناب؛ ۶۹۰۰ لیتر بنزین کشف و ۹ نفر دستگیر شدند.
🔹
مدیرعامل تراکتور: بیرانوند به‌دلیل افتخارات ملی باید مشمول معافیت قهرمانان شود.
🔹
رئیس سازمان اداری و استخدامی: تلاش می‌کنیم از ماه آینده حقوق نیروهای شرکتی هم مانند نیروهای رسمی، قراردادی و پیمانی، بلافاصله آخر ماه پرداخت شود.
🔹
در میان سدهای تهران، ماملو کمترین و طالقان بیشترین حجم آب را دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/683274" target="_blank">📅 11:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683273">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebe703340.mp4?token=fU8rvqH-nUFnpC94_orA6sW9DX5IbuUxoPhosOwdYSRXTLPojqcQa8djSjwLlE_qpC0uuGZVTxDqY_i2M6bh-p7nDH3OpDooAIqUaRD4g-wwLjZcpsAtwM36B48l4Xp2vf4FlNt-aP2MXh7TE95jDK8Dzt7piCygEk_Mdt7RnzJ0R_9Co5fft3JCJ0doDAC8enIkmjAP33PLsf54aJ2KOqZlROdzd27D6J0YvQjs00ysej96vtxRCOl8qrX9aMDW88sTsU6qNhlqcL8tOxwWy-Z9dI-oP9bW9Gy4dDZc7Mjwb7-aIcIu2HJpCmiaRclbl-HDG3U3Pbt10Mndvfqf5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebe703340.mp4?token=fU8rvqH-nUFnpC94_orA6sW9DX5IbuUxoPhosOwdYSRXTLPojqcQa8djSjwLlE_qpC0uuGZVTxDqY_i2M6bh-p7nDH3OpDooAIqUaRD4g-wwLjZcpsAtwM36B48l4Xp2vf4FlNt-aP2MXh7TE95jDK8Dzt7piCygEk_Mdt7RnzJ0R_9Co5fft3JCJ0doDAC8enIkmjAP33PLsf54aJ2KOqZlROdzd27D6J0YvQjs00ysej96vtxRCOl8qrX9aMDW88sTsU6qNhlqcL8tOxwWy-Z9dI-oP9bW9Gy4dDZc7Mjwb7-aIcIu2HJpCmiaRclbl-HDG3U3Pbt10Mndvfqf5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کفرگویی فرستاده ترامپ: خدا هم نتوانست خاورمیانه را اصلاح کند
🔹
در شرایطی که آمریکا به دنبال کاهش حضور نظامی در غرب آسیا است، «تام باراک»، فرستاده ترامپ در سوریه و عراق، تلاش کرد ناکامی در منطقه را با کفرگویی توجیه کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/683273" target="_blank">📅 11:28 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683272">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf6b0631de.mp4?token=UcibKOV9p0z9lMyClpPee8vXWrqUsJSnuwUgEnrURu4406MRPy_m68moN96eWMF4TZmn1UfTwiq9XrI3tYbhmQPykB0JUdaSUdBcZR16PkV5W5dK_SaiFma2kZ_U9NrPbW3FF60VuDTdGSPdGVMkNMocbQnhnOI3vjnaJqmm5Utbsvr4V25Fu5q9pU5D1KHluZ1fuZ_jOB_xBkHx_9kfw8a7p3FyvMKyASedlRiMPRpMxnldGhFw-Q5wWE3YC_li7KYMnotQHHKCtczA-E5CAJnyXm8AHVUaTrPbsnu4auiI32M0sW4geYTyNrTzCt-Z9tHX6LS_0Vgdg_7qiDijmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf6b0631de.mp4?token=UcibKOV9p0z9lMyClpPee8vXWrqUsJSnuwUgEnrURu4406MRPy_m68moN96eWMF4TZmn1UfTwiq9XrI3tYbhmQPykB0JUdaSUdBcZR16PkV5W5dK_SaiFma2kZ_U9NrPbW3FF60VuDTdGSPdGVMkNMocbQnhnOI3vjnaJqmm5Utbsvr4V25Fu5q9pU5D1KHluZ1fuZ_jOB_xBkHx_9kfw8a7p3FyvMKyASedlRiMPRpMxnldGhFw-Q5wWE3YC_li7KYMnotQHHKCtczA-E5CAJnyXm8AHVUaTrPbsnu4auiI32M0sW4geYTyNrTzCt-Z9tHX6LS_0Vgdg_7qiDijmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این هند نیست! چرا کرالا این‌قدر با بقیه هند فرق دارد؟
🔹
کرالا؛ ایالتی متفاوت در هند که نظم شهری، سواد بالاتر و همزیستی ادیانش توجه‌ها را جلب کرده؛ اما راز این تفاوت چیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/683272" target="_blank">📅 11:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683271">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LK2ScuoEaPej5MzncOfrb-_BEWUJZhEKfgSbHEdGYIuGOOv6JWQfjK98Tm4odVcC82J-EExzHG95vsqkdQZkP_T6JclvdB3L1GZQpLCADmQ-Wuq6IDKUDikrQYszlCmuXWj6uL-fNy_jozKESfISQMZv1w8l_gZyTZnw8K_SYNhyvAwzH_fKUzKidn8DSXpyAwpj5vXsDUl5xx9_GJZi8tptKX6RgcjJOj1CTarjj2Cr7te72pxND_LlomR-ISLVPau8jn6U6GnacMYpWxRSK7IWjJR4IKuFbk2k9izZxKx8JX3R4b-pVLkfvNw4UxgGfk2fvgvjOvUreIMCV-mzsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلا از مرز ۲۰ میلیون تومان عبور کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/683271" target="_blank">📅 11:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683270">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
قیمت گوشت در یک سال تا ۱۶۰ درصد افزایش یافت
🔹
هزینه تولید گوشت طی یک سال ۳.۵ برابر شده و قیمت لاشه گوسفندی ۱۱۰ درصد و گوشت گوساله ۱۶۰ درصد افزایش یافته است.
🔹
کاهش قدرت خرید مردم، مصرف سرانه گوشت را از ۷۰۰ تا ۸۰۰ گرم به ۴۵۰ تا ۵۰۰ گرم در ماه رسانده است.
🔹
واردات گوشت گاومیش از هند نیز در دستور کار قرار گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/683270" target="_blank">📅 11:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683269">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_qhaqurva3_pq0-Mc0FD8zTsplRb0zWhXpDAK7Bux3B69zI57SfpJrfNVSz6Ttr4hKWunQuBVSXH8VZPiBi6Zvn0ORqZjGDw6wu7TFQIroEfEl7Xxnl9VFRGQh5m0Pu7J_nu83ByNM1yoGLFDxWscDI0Sxcj-2fAWGn-6Rw4U8F_nz-2A1ReQ6-CCWafbobqB1PjujQwc4ARLT-Tbw7IxPGk4wDrVm228quxfyIEGAJdjgsRvp-RqSTPPEXFkLITYqw0vbPTRSffPnOolI5rBudNfkKneXoNDq2q9Fjmksk8R8ec8pS2Ngyfkn2WCgI2Gor8PUPnZeYamdTMMKN9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمار کنکور ۱۴۰۵؛ ۶۵ درصد داوطلبان زن بودند؛ در کنکور ۱۴۰۵ از هر ۱۰ داوطلب، ۶ نفر دختر بودند
🔹
تعداد زنان در کنکور طی سال‌های اخیر بیشتر از مردان بوده و سهم آن‌ها نیز افزایش یافته است.
🔹
سهم زنان از ۵۹ درصد در سال ۱۴۰۰ به ۶۵ درصد در کنکور ۱۴۰۵ رسیده؛ به‌طوری که امسال
۶۹۵ هزار و ۶۵۷ زن
در آزمون شرکت کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/683269" target="_blank">📅 11:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683265">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZwpSODpxb_hoOcgkA4fcyuVY9b_97Fay9eI5GJwO6H8WmWgxxqMBnSH-nfOluWiN9Qq8YfmyRu2KjYjILgWC_qS4PgThNjNsx6u59PQD3Bj0l3ku0oj12H_SWNbh7r5ol3Roq4Klgpp6a8UdqjurSYWIVGpswTU66F6L4QE8Wnc9Qr2nOoZHjKxujKKf59accnrgUxUfayBM41wXr6ZCmvd-GV0jc9p4oXvswVkF2MBsm-GYbkNhMN1CraxMNadykoFmGHHuWDZ0yuzlurV1iBN86QRSjgzsK9Er1R6Hb6TD0Sj2-U0g4kWQs3ZzKMRP1nbhqUgaC1avr4ks5oXnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lGaaKpH2_dUo7ZGU-LkHNa2256FSAjZDXAQzCFTkvMXhlkCK_yy2I3vMC8YApOog_hQmrb4I5PxVHgMbFE0wYiZCX8SP3GugM3Oy6Tjyv1nvpkwJEt_wnP-iJocwzKWSnNZz7d5iRnsu3mI5XQOT91LqHJj42wS6uNxYWsrU7ZgSir9cOGybbvyjS6I1E2PtVZvPcFTHsvBgxKIaY5YM82AjbJnX0CgzTzGuA3f54B0hYER_QCTjRgpgkIOFtZJesLtiOSMUnZM8gVHK9UEin6IqdtOWQwS22zvoFXs7kjn_xSI3ZOcom6KsHYXcEs6Q4cSbArKdsNP1-hF3iqK3NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CnGr9UCQV4VguuH0E5hV9FUIjvE81h5i97mVjm2FqaGJw6KJ0rZ3UDuIFNBYbss7g_E_fVnuecOek34XIRVQGNfwohEla0Si1gzBFsMLk5U1mcM4NEYvaGCyEWIYk5qvgXBErSRL5B9ja9P3dDVFiz8HRGRckT7PgQAJN_--v1C7Ej7a2F0zgiTViHO91N5E4Of69cz_qtPgsXni4VwJsq0bqOe8aYZ9v44im5yasJyA9pGrkfOh4jHhTHYdNToRQ07JCNkqVXtbItdygvL4GUOysQA7S6u2WK6Q3DT0DaI8jhS0fACbEEdy0e9r9al2OKjqUkpfKzEFtK3_mqKNyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKeJPxVp6YSd9KG7ZhaxTH0fdt-qJmWdF1jZdUHwRZZ4dWEQc6zavT2CEI9288gI_IIHfzaOMRLfzghWo8SZe0TMnVD52SDOwZZ2jw6M3efguuepRkOlUEaYO7LwDZGWabX7JdvPhnMrnvy0GB_F_ymRnhKhz_9QKhmSMjLy5ouB0dPjDJ-dTuuXEv9vU-CBubVFWCixvPJPV4aIlWhxwwWR44aYHBmMF9DsG4UV3DZQyqH4nAwuFOfHAhjErf_Efs9y-DTioMr8FzmonmosBMjDQod2WwyhCfFNnRgqegzc8XKUUF55p0mtQR0axtT9CDvratCuu2xBj5dBnYrNLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۷ گوشی برتر برای عکاسی در سال ۲۰۲۶
🔹
از زوم عجیب سامسونگ تا عکاسی شب شیائومی و جادوی هوش مصنوعی پیکسل؛ این هفت گوشی جزو جدی‌ترین مدعیان دنیای عکاسی موبایل هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/683265" target="_blank">📅 11:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683264">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1568d8a38a.mp4?token=gyPrZycpMY4D_mbm24IAsnEDdBFS9GbK32zP5pufPFlU7PIuI6O8Mht0ESw0QXaw9GVtr0TCVifG3r70JObUMo8GY0dBrZZFzv1idSqFXTWyC_P1D6cd2fj2z6uP67FEJ1_8cbKNjs4n2GnD9kQaZSL_LxQC3ikCwE0e8jH6G22RV1JmB5_r4wcYk7ZF3bGU8m0AgQHAYBYFxNxE-8E3HZiO8Zl0DeA8oinJz8u2YXZmKGZsEVFok2kjzYPPY8HpHYPWMuSGJJbNZMOpJ--l3hYUAQ07lipnBX8-54HdSEocsf_0DkDqR1SxJyw0K3ShmA962N9_ng0KiuzeOprqjm3cmGogWePlLEg-AtEREpoezvYgcNOoHIMLbvEx5U2J5n5LcK4a7FKpsyD55PMBiUINKCqZ9jm6vfzn0OVYvFIZmRB6xL7WNGwWtmBWTxNCYr-QY0oDla_TMNXpO-hZ0MLr51wYfWf7nwrfveWICS7NBWnKanHNdon6h3Gj3x3XCO2XJxr18NN8OLE9norvyvh4cgswtpaDNSQVycz1FCW4Meomg02Ycglc7iJLC1vA44afPcm2E2eTZpOGXEj0CR0Q91xOBDHu9r-bzhRI0iIrJYW977RukCk4sDrij8HuzlSaVz8G659SMTyOwTC9CgJbY09Bb131KUmvUCDUYFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1568d8a38a.mp4?token=gyPrZycpMY4D_mbm24IAsnEDdBFS9GbK32zP5pufPFlU7PIuI6O8Mht0ESw0QXaw9GVtr0TCVifG3r70JObUMo8GY0dBrZZFzv1idSqFXTWyC_P1D6cd2fj2z6uP67FEJ1_8cbKNjs4n2GnD9kQaZSL_LxQC3ikCwE0e8jH6G22RV1JmB5_r4wcYk7ZF3bGU8m0AgQHAYBYFxNxE-8E3HZiO8Zl0DeA8oinJz8u2YXZmKGZsEVFok2kjzYPPY8HpHYPWMuSGJJbNZMOpJ--l3hYUAQ07lipnBX8-54HdSEocsf_0DkDqR1SxJyw0K3ShmA962N9_ng0KiuzeOprqjm3cmGogWePlLEg-AtEREpoezvYgcNOoHIMLbvEx5U2J5n5LcK4a7FKpsyD55PMBiUINKCqZ9jm6vfzn0OVYvFIZmRB6xL7WNGwWtmBWTxNCYr-QY0oDla_TMNXpO-hZ0MLr51wYfWf7nwrfveWICS7NBWnKanHNdon6h3Gj3x3XCO2XJxr18NN8OLE9norvyvh4cgswtpaDNSQVycz1FCW4Meomg02Ycglc7iJLC1vA44afPcm2E2eTZpOGXEj0CR0Q91xOBDHu9r-bzhRI0iIrJYW977RukCk4sDrij8HuzlSaVz8G659SMTyOwTC9CgJbY09Bb131KUmvUCDUYFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی به ماشین پارک‌شده‌ات زد و فرار کرد؛ چطور خسارتت رو بگیری؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/683264" target="_blank">📅 11:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683263">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R35rede97Fb0WFzEqEJETE9IZXjOauP1vGYb-jPegm0RfddRnRd4Yn9Uv51vWu8ie4utJ8C_ychzjjh616AghdJ8WSVM8AgwPXBCy_oy-U3XooFNXyKFJJ1qQ5n-O7R9SK2RbFQd00-W6Ew79TRFUIw3GcFnaUloSyELmqMYAmFrmdlZCwDlxwzH6Q79svZbOfsPDoG7IjQqyqJDIvJviJJzjCsgZ6Cank5ZOMYx46x8zApG6Ycnf4LmHD_AdpC-MOVAMeagngLkbP94RvNt5Amjux1YmUnhcacqo0MnqVdgryjnN08CqPqwF5wBxi6NHNOfYfXJ8NqZ-8evPyPhTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بزرگترین کهکشان جهان کشف شد
اخترفیزیکدان اسپانیایی:
🔹
بزرگترین کهکشان شناخته شده جهان ۱.۷ میلیون سال نوری وسعت دارد و آن‌قدر بزرگ است که ما نمی‌توانیم مقیاس آن را درک کنیم.
🔹
این کهکشان هنوز در حال رشد است.
🔹
برای مقایسه، قطر قرص ستاره‌ای کهکشان راه شیری تقریباً بیست برابر کوچکتر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/683263" target="_blank">📅 10:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683262">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIf9sQ-dFNkJYCTKgKyPqoKjQWuf8_OB2sHkP5J3L_8NIEx6YqpY_oI43rHPi4eFCy2OGY6DgKlrkeu_er_SqKN7MjJ81VJp1TE09l39VgrJqRzVfh7Zg32q6jLtzwkRhTZWJ7-NOMqRebBP4VA0igILtqv3Rg7B4QSTiJXAD7Y5-t-BCmEjG-_XzA5UsmIc0_pPQyntbtswd-HIMMlqwjgeiPYE0tWMz71NyV5c2E6dhPBDI4n22mpND58ovqtJI0DLnGtKOEHETFaNfuBKCc32TdNdcQOuchx9SrD_1yZTr_CUevuj2rLB9yhQEkByJef4o3S7kccf5K0ogKhiWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای فاکس‌نیوز: ایران از شریان روسیه و چین برای جنگ اقتصادی با ترامپ استفاده می‌کند
فاکس‌نیوز:
🔹
ایران در حالی که ترامپ جنگ اقتصادی «خردکننده» را تشدید می‌کند، از شریان مالی جدیدی استفاده می‌کند.
🔹
تهران در حال تعمیق روابط مالی و نظامی خود با پکن و مسکو، دنبال دور زدن تحریم‌ها و عبور از کمپین «فشار حداکثری» مجدد واشنگتن است.
🔹
ایران به بلوک‌ها و اتحادهای غیرغربی روی آورده تا بیشتر با روسیه و چین متحد شود و در عین حال خود را به عنوان «محور اصلی» شبکه‌ای قرار دهد که مستقیماً نفوذ آمریکا را به چالش می‌کشد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/683262" target="_blank">📅 10:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683261">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/647ad94e5f.mp4?token=Z3li6igKXTL6yfK_a5xOwojLMiBwdptg1MGMgDjYJc6exiuC64L7SZfN8Dhv-QoZIfuONNzXdSHpR_NBcqGFfLk9Gtun6pklzvKeTYzd2c2v3Fgc3VIZBlyPLKJZ60a-BnNL0AiNUKDhR2xut_i-BE__HhbRs8oczdQbANx3TlQxDZnwjGGqp5kdNeRwRdrp-zxp9yctwHZ7IwEO2upVUJu1d-MPU7zCFZO-0WbwMcjR5B9Q-ot7_CvBu5EMpeZcfkraKa88QRjnbS4qUCjf28uoIv3bTjFpm6riQs9r1zjZwNu_JA91tqlhBY_LlhwBgjtYe5yvVFSx9JHDtRQAQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/647ad94e5f.mp4?token=Z3li6igKXTL6yfK_a5xOwojLMiBwdptg1MGMgDjYJc6exiuC64L7SZfN8Dhv-QoZIfuONNzXdSHpR_NBcqGFfLk9Gtun6pklzvKeTYzd2c2v3Fgc3VIZBlyPLKJZ60a-BnNL0AiNUKDhR2xut_i-BE__HhbRs8oczdQbANx3TlQxDZnwjGGqp5kdNeRwRdrp-zxp9yctwHZ7IwEO2upVUJu1d-MPU7zCFZO-0WbwMcjR5B9Q-ot7_CvBu5EMpeZcfkraKa88QRjnbS4qUCjf28uoIv3bTjFpm6riQs9r1zjZwNu_JA91tqlhBY_LlhwBgjtYe5yvVFSx9JHDtRQAQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بالاخره از ماکان نصیری، دانش آموز مفقود الاثر میناب یه چیزی پیدا شد
🔹
فقط یه برچسب روی جلد چسبش..
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/683261" target="_blank">📅 10:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683260">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ5rC8RhkJiBJbnKaDi-oomSoJ1NQLXmFoO7Ec0NdZmPZEd5YD_mdeeTTDY-BcHXJ0ZgND4tq00OIBVXYlhZSqoxzaBNyIHrcXg2AAAy5VX0Nk0G9XptIK6-HeFdbCtEwUt6gu-dC9uDfxwl7BQsC4gEw_BDSpRSCpmebqTzfrvXTw0u1mLBl55pUF7_9Hj6PowPGKxUVkwEHXVWodpUYaXtEUkW7jCrvULtanrMbEZAM2DMpnrxYU1ujCWD92kSXmrxGLfGN9-95-8Oy1V45jcuvPmMFHlMFFOOod4XaWYTcygouBZc0Fu9PA6DcIZKYXEPwN5TSZe7aaimQf1uOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌼
بیعتی دوباره با صاحبِ زمان ( عج)
💚
به مناسبت سالروز آغاز امامت حضرت ولی‌عصر (عج)، در اجتماع بزرگ «مراسم تجدید بیعت با امام زمان (عج) و رهبر معظم انقلاب اسلامی»
▫️
با کلام
: حجت‌الاسلام و المسلمین حیدری کاشانی و علی‌اکبر رائفی‌پور
▫️
با شعر خوانی
: احمد بابایی
▫️
با حضور
:  سرکار خانم الهام چرخنده
و حسین حقیقی
▫️
با اجرای
: امیر مهدی باقری
📍
وعده ما: شنبه ۳۱ مردادماه، ساعت ۲۰
میدان شهدا، مشهد مقدس
🤍
بیایید در این شب عهد و انتظار، دست در دست هم، بیعتی دوباره با امام زمان (عج) کنیم...
@Heyate_gharar</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/683260" target="_blank">📅 10:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683257">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f1Rp2AsrmZJVLXMmkqKz7QYoQ0J39hyxhpR62Z0IqfrhXNQlO6XyeJrZqzkKR_-u_YDP4S7L_w-iunlR2KvLLtkLRBJ8v7_KWDMCSp2R7mnFsBcWFKw3Jnu75Q_dhzqAPONZnKS_iWwcRHW5ths6aSoinwrErjG7AOTNmTDl6GXqNMWMZoa816ZA8qwyE7kMh6im_-nEKSUBsStp0X86YMWStto95C0j-1BKFjxcQivxPGsKfx7kch2jDEs-v16T_pfqeU1O7pmN6fmO-GMjdg3r03tjoFx94OVW7KE60nULsb2o_h1GC7ucD_0-HS3ZXCc8j1R_s1e07w4mJqXt-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IzbAQU1HJA2JEbLnsUTfO7gAp3V2SMsLOhfemsAvnZStoB2_fC1TCOyL9Gv7SEgQjK67fKMYNGvTY3v8phEE887l_MhwZ2R40P_D85bJ9LvMduprhvL5Cv3LjenoBtF9F8m2uiiv619PJEYz57AwO2cxoN-DMGArzs1GZj04Q2zbILdgIs8rK00WShdsz5SeCwboBkFRWJrDBhhNZRySbzxemLG7NvAT8-KX0kpV9fE5O9oTIep6ohdh09_KngOUK_wtH7mouzLd5gLUD4KYqj3IXOeIb5OtBL7ntvtEnoj4t_IOJPRSnx0FdVCNvcYThdlR-VEz6AP-a_k9NMrvxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZvJFlm_GdRsSByvd4N5Naeud004O63Mx3hHJohVG6Wbqpg1XytMVV_uTshH4GNwyGXLx2Dou14KR-0rVldD1l5JfHp1pivKjPEo58Mfe8yCFOKgxkLOKlbr6cUacYC14whws_Sp_4FN88kF05XwEJCnKCsLZJLy-WdoaY9mJiht9jvYdGFWiNDzP5BZHw6C-5iOxIN-L4zOz7KG7P81sGVMYrqMqxDDg17VMArdly8GNR-QWlMpFmxo6P0F6ehtyqi-eHr_Rkqw85MK2rB2cuMTgwGFOyNnX6BO5dxvu3O3KLWZ3_RnwJSdQWwX7PG27c9QLogtaHCOzjvtGyGbgpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مدل موهای مختلف کریستیانو رونالدو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/683257" target="_blank">📅 10:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683256">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
‌موتورسیکلت زیر ۲۵۰ میلیونی دیگر در بازار نیست/ گرایش مردم به بازار دست دوم!
رئیس اتحادیه فروشندگان و واردکنندگان دوچرخه و موتورسیکلت تهران:
🔹
از ابتدای سال با افزایش ۲۰ تا ۳۰ درصدی قیمت موتورسیکلت مواجه بودیم.
🔹
افزایش نرخ ارز و رشد هزینه‌های تولید و واردات موجب شده ارزان‌ترین موتورسیکلت‌های تجاری به حدود ۲۷۰ میلیون تومان برسند و دیگر موتورسیکلتی با قیمت کمتر از ۲۵۰ میلیون تومان در بازار وجود نداشته باشد و مردم به بازار دست دوم روی آورده‌اند./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/683256" target="_blank">📅 10:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683255">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
استفاده از متانول در بنزین تولیدی ستاره خلیج فارس تایید شد؛ احتمال افزایش خوردگی در برخی قطعات خودروها
🔹
مدیرعامل شرکت نفت ستاره خلیج فارس استفاده از متانول در ترکیب بنزین این پالایشگاه را تایید کرد.
🔹
انجمن خودروسازان ایران پیش از این در نامه‌ای هشدار…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/683255" target="_blank">📅 10:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683254">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">#چند_خبر_کوتاه
🔹
شرکت ملی پالایش و پخش:تاکسی‌های اینترنتی هرچه سریعتر به دوگانه سوز کردن خودروهای خود اقدام کنند
.
🔹
وزیر علوم: آموزش دانشگاه‌ها در سال تحصیلی آینده حضوری است.
🔹
فرماندار سیریک: انفجار کنترل‌شده در سیریک انجام می‌شود.
🔹
طوفان تمامی ادارات منطقه سیستان را تعطیل کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/683254" target="_blank">📅 10:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683253">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/974bcd2f48.mp4?token=Fj6zF6zblPpIylm_HeF3AZ6QOQz3BaKJ75nSGv84Zs_b2xgLCXBYjx1vUGMhlzW6yfjtgfR2azCjDQ-9sqm4zBbjXgK7roOkQB-_7kvvOo5WWFqwHV3TzKLesdVF4s8GnI7fm8tMvvMLf9mo2DHjW9_bIZ9ZZoU-lbIsz4NZy7g3EDeWIyBzzOgtGsKZO9PLGh6Ll4opfbzTFs0nOnto7JXNkjLFSJkqkXQu1xTVe8Z06q9E2B01lSI8Ey-EyTCOsQj3E3f01ajRZg8Rf-UljrTsTkg28roa0VrwWxCXt9bARTz4mWbiUJOfklM_IZeAAT32JjlKm1WSnDFZDKVd6oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/974bcd2f48.mp4?token=Fj6zF6zblPpIylm_HeF3AZ6QOQz3BaKJ75nSGv84Zs_b2xgLCXBYjx1vUGMhlzW6yfjtgfR2azCjDQ-9sqm4zBbjXgK7roOkQB-_7kvvOo5WWFqwHV3TzKLesdVF4s8GnI7fm8tMvvMLf9mo2DHjW9_bIZ9ZZoU-lbIsz4NZy7g3EDeWIyBzzOgtGsKZO9PLGh6Ll4opfbzTFs0nOnto7JXNkjLFSJkqkXQu1xTVe8Z06q9E2B01lSI8Ey-EyTCOsQj3E3f01ajRZg8Rf-UljrTsTkg28roa0VrwWxCXt9bARTz4mWbiUJOfklM_IZeAAT32JjlKm1WSnDFZDKVd6oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نابینایی که اسکیت‌بورد سوار می‌شود!
👌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/683253" target="_blank">📅 10:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683252">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYDM7GgCIcv1UHF_sVQqPziVBJ4GokLXP_DM9V5XVm1loPmkGKYllc-VHBO8GuqBgWmrITzu8aX8Xl6qsT8N8ScbzG2tc1u349sZP-t_93_sO2agCIOY5skYdDvGR2XZ48NUaUedOLoo9hu_Lvap9XFYnQIAxoFM14f7cVzvYUxCLbt3pmczUvQqI34Vwx4SgMGU5ujomp-T_wEC0KfPEh0BSVZyiZCGk-E7B2ZJ5GPzvK0onJiwA7xsTud_7eGPIKtriYh19kwL7wsaK2yRX59PMbsaRQ6j2xzH5mYyCwHMPsCszXd_-MKj0EYn5J2j2dYEsP2nmKSjtdSFHJGFWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره
02191551808
در ارتباط باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/683252" target="_blank">📅 10:24 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683251">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1995235159.mp4?token=I2zcl0DvL4wWlWDqg_oNAWcbPJKMsRIf_AvRN9_0VPsh6DEwkQ1LjB8G432BdZtzBW-X_guSX8HMrpq7kpoGRfPw9TQ210TYeK0rWel8rZE8LTALcIUvwrWUyAN7t0E7f76SA9PEdlJLsvYlSjSd_oqGyCdha58Jn9yoPef8fYk7eRlFBbr1SQtLdxN8o0iEsatXPeTk6lA_A-Cvrd8ZO82bk7uM8jiwA5h9JxKyt2R9I_L2ON8v2MdaPHSwk6O5u-pubT_ZagdwMy7Mkhgqa3hXDUmZPCcl8CY-OWDgBexCmVl5Aske9TIuVBOOrKFdFn1Rzow1On0uMuMMg8VjQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1995235159.mp4?token=I2zcl0DvL4wWlWDqg_oNAWcbPJKMsRIf_AvRN9_0VPsh6DEwkQ1LjB8G432BdZtzBW-X_guSX8HMrpq7kpoGRfPw9TQ210TYeK0rWel8rZE8LTALcIUvwrWUyAN7t0E7f76SA9PEdlJLsvYlSjSd_oqGyCdha58Jn9yoPef8fYk7eRlFBbr1SQtLdxN8o0iEsatXPeTk6lA_A-Cvrd8ZO82bk7uM8jiwA5h9JxKyt2R9I_L2ON8v2MdaPHSwk6O5u-pubT_ZagdwMy7Mkhgqa3hXDUmZPCcl8CY-OWDgBexCmVl5Aske9TIuVBOOrKFdFn1Rzow1On0uMuMMg8VjQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر کنجکاو هستید بدانید ماشین لباسشویی چطور کار می‌کند
این ویدیو را ببینید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/683251" target="_blank">📅 10:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683249">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f0759c5d.mp4?token=B-AZaKqvW-FOCShbEbijmcuFqDGSmNCDg01P6VW4xkW4Z365nKteT9mYD1v5i1LSpNQjg_WPXX4kqUMrHBttu6hatI6nYrMelfkPNcPt4ZN-hWx4ubBgZgKn7UFv6RTJUxOUUumfQCtAkWooWc0oX08OQsbmYwdbyVvm8mrbGIArCg4AWCN8Sr-RKsfzqogL1Dp0NOr5HZDh-fS30w2r8MWNw2ef2v9lbawNC9vu9OU3vSlFEnhlOvpBIT6byuDa8t1yaEZa-qjvForeAfuql2MTdTQRKhygYSBiXtuIaEp2aKnih5vISMwpf1-R4s5t6SMEp1zaigAu6olCrgvJZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f0759c5d.mp4?token=B-AZaKqvW-FOCShbEbijmcuFqDGSmNCDg01P6VW4xkW4Z365nKteT9mYD1v5i1LSpNQjg_WPXX4kqUMrHBttu6hatI6nYrMelfkPNcPt4ZN-hWx4ubBgZgKn7UFv6RTJUxOUUumfQCtAkWooWc0oX08OQsbmYwdbyVvm8mrbGIArCg4AWCN8Sr-RKsfzqogL1Dp0NOr5HZDh-fS30w2r8MWNw2ef2v9lbawNC9vu9OU3vSlFEnhlOvpBIT6byuDa8t1yaEZa-qjvForeAfuql2MTdTQRKhygYSBiXtuIaEp2aKnih5vISMwpf1-R4s5t6SMEp1zaigAu6olCrgvJZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عارف: دهک ۱۰ درآمدی ۲۳ برابر دهک اول از یارانۀ بنزین استفاده می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/683249" target="_blank">📅 10:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683248">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی وزارت دفاع: تولید تسلیحات دفاعی افزایش دو برابری داشته است.
🔹
رویترز: ایران به درخواست بغداد، اجازه عبور شماری از نفتکش‌های عراقی را از تنگه هرمز داده است.
🔹
معاریو: نتانیاهو در صدد اختلال یا تعویق انتخابات پارلمانی است.
🔹
روسیه از سرنگونی ۴۵۷ پهپاد اوکراینی طی شب گذشته خبر داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/683248" target="_blank">📅 10:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683247">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c213ad4251.mp4?token=KjxZuy-b8i6MKRZIFSAubSrS-NuoLoT2cQ8DpcTqhbYGlg3yWaJachz9XvlrXC_85YoZncjpEEJ4wqdQx1L5a9CRFqCqqNlGe0KPK-H1iIFyABgzXBFsxq-48pas0Z-RSj6WnFK3Mji1Q6XC8KFsZwlWbcSDJaRwT5F3PKLCZzmYCus_XIzV_8ihPmVsOUvGm18qw76jPR8yTCC50lmj_1_SOEkVpYIO2B_USxenDIozGW_EVA8WLZKGdgVD6HplyCwQvXAnDCayPB2j-Q_mDfCo7JD7pvqsltTU7keSzlGoLiW2zT7rXAIdRyFgyABDGTLxIQ6UKwWuR57jcgw-Y4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c213ad4251.mp4?token=KjxZuy-b8i6MKRZIFSAubSrS-NuoLoT2cQ8DpcTqhbYGlg3yWaJachz9XvlrXC_85YoZncjpEEJ4wqdQx1L5a9CRFqCqqNlGe0KPK-H1iIFyABgzXBFsxq-48pas0Z-RSj6WnFK3Mji1Q6XC8KFsZwlWbcSDJaRwT5F3PKLCZzmYCus_XIzV_8ihPmVsOUvGm18qw76jPR8yTCC50lmj_1_SOEkVpYIO2B_USxenDIozGW_EVA8WLZKGdgVD6HplyCwQvXAnDCayPB2j-Q_mDfCo7JD7pvqsltTU7keSzlGoLiW2zT7rXAIdRyFgyABDGTLxIQ6UKwWuR57jcgw-Y4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قبول کن خوشمزه‌ترین وعده صبحانه‌ست؛ پس بیا با یک سیب‌زمینی‌املت تکمیلش کنیم
🥰
🤌🏻
مواد لازم:
🔹
سیب زمینی نگینی
🔹
روغن
🔹
زردچوبه
🔹
رب رقیق شده با آب
🔹
نمک و فلفل
🔹
تخم مرغ #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/683247" target="_blank">📅 10:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683246">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9cbce3fcd.mp4?token=stn8ikTkdtGV3fYGC4xXf-mG0wt-57B-hvA7JzN02AGa2eu4wwAPS5b1rWAs4PGwjXgpYA2CkQebpStQMGu7eN4R2Mjj37K6zkphmrNeHtldcuOqB6EpWB3Qs8gf293BjnJjwXSHZcZww8mB9XeEhLjuZqfYUAnLjvA18-7ZL-65yk4_uBImDD42RHgJZ-dEohFZyA1sw6na2J4leZpJrjeVVnSGiM7ZE404-HYeJJNn_ikT_PzLp483kStorHSOX4HeBfHRgP5fGQD06Hj7bvN69OdGUec2p_l1yhSkM6ukL8Hu9c2jQ0mflq08bJzyrRs6bNbWHgMU6Cy7oebp1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9cbce3fcd.mp4?token=stn8ikTkdtGV3fYGC4xXf-mG0wt-57B-hvA7JzN02AGa2eu4wwAPS5b1rWAs4PGwjXgpYA2CkQebpStQMGu7eN4R2Mjj37K6zkphmrNeHtldcuOqB6EpWB3Qs8gf293BjnJjwXSHZcZww8mB9XeEhLjuZqfYUAnLjvA18-7ZL-65yk4_uBImDD42RHgJZ-dEohFZyA1sw6na2J4leZpJrjeVVnSGiM7ZE404-HYeJJNn_ikT_PzLp483kStorHSOX4HeBfHRgP5fGQD06Hj7bvN69OdGUec2p_l1yhSkM6ukL8Hu9c2jQ0mflq08bJzyrRs6bNbWHgMU6Cy7oebp1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت سلیمی از ماینرهای غیرمجاز؛ از کارخانه‌ها تا زیر میز کارمندان
علیرضا سلیمی عضو هیات رئیسه مجلس در گفت‌وگو با ایسنا:
🔹
براساس آمار وزارت نیرو‌، حدود ۵ هزار مگاوات برق در حوزه ماینرهای غیرمجاز مصرف می‌شود.
🔹
مواردی کشف شده که کارخانه‌ای به جای تولید، با استفاده از برق یارانه‌ای، ده‌ها و صدها ماینر غیرمجاز راه‌اندازی کرده است.
🔹
در مورد دیگری، فردی که در خارج از کشور زندگی می‌کند، یک واحد مسکونی را اجاره کرده و ماینر در آن قرار داده بود؛ مأموران پس از بررسی متوجه شدند حدود ۲۰۰ تا ۳۰۰ ماینر در این خانه روشن بوده است.
🔹
حتی در یکی از وزارتخانه‌ها، ماینری در محل کار یک کارمند و زیر میز او کشف شده که با این فرد برخورد جدی شده است. این کار نه‌تنها غیرقانونی و غیراخلاقی، بلکه غیرعرفی و حتی غیرشرعی است.
🔹
در این حوزه خلأ قانونی وجود دارد لذا طرحی برای برخورد با ماینرهای غیرمجاز تدوین شده  که در آن مجازات‌های جدی برای متخلفان پیش‌بینی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/683246" target="_blank">📅 10:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683244">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f74ef4bc95.mp4?token=BfXVEXbcYu3tI-HYibqKF-OGRFyqApnhPikTpYusBtXKPFPz7qv9s1tLnY2ZZGsOHL35B0vKvKzGFguNtzHj4JkuZ0fler-G8Y2lEg0ZPsfusxB3PWbwxRmMVzILIATpwHMZvXwYGHGTwHlyrd75n-GqWkEJlh6v1yezcric13F6wDIUgjp0sapPjT32E6NuEHl8cO8Lsx4JI9l0reUja-LaQqehg6MRMCqoR-0GaDcnnfudaRP1qXC55-34E6HwhBh3mv4JkXVdHmZCIA6QEJBLMWs5eRqIp4Q3WwPWcbDjK1c4EXmXCQOwQCae7MzBPW6aXzptNG28-Hu1ZWQCQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f74ef4bc95.mp4?token=BfXVEXbcYu3tI-HYibqKF-OGRFyqApnhPikTpYusBtXKPFPz7qv9s1tLnY2ZZGsOHL35B0vKvKzGFguNtzHj4JkuZ0fler-G8Y2lEg0ZPsfusxB3PWbwxRmMVzILIATpwHMZvXwYGHGTwHlyrd75n-GqWkEJlh6v1yezcric13F6wDIUgjp0sapPjT32E6NuEHl8cO8Lsx4JI9l0reUja-LaQqehg6MRMCqoR-0GaDcnnfudaRP1qXC55-34E6HwhBh3mv4JkXVdHmZCIA6QEJBLMWs5eRqIp4Q3WwPWcbDjK1c4EXmXCQOwQCae7MzBPW6aXzptNG28-Hu1ZWQCQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آشوب در جام‌حذفی آلمان
🔹
دیدار تیم‌های فالدهوف مانهایم و کایزرسلاوترن در مسابقات جام‌حذفی آلمان، به‌دلیل درگیری‌ شدید میان هواداران و پرتاب مواد آتش‌زا، به صحنۀ آشوب و ناامنی تبدیل شد.
🔹
در این دیدار ۳۵ مأمور پلیس زخمی شدند و ۱۴۰۰ نیروی امنیتی در محل حضور داشتند. چند هوادار هم بازداشت شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/683244" target="_blank">📅 10:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683243">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvmRL2Js5cswbbAt-WlOLfmTIvFz4SxqsNvMQBH_mdZLumuFBIhllye-KhVh3xcfEclIomAKRPGE8bNmPCauhPaz7emI4AgMNMuwsrxAYQQkx8KyifXQiq81LTD0iM2uXU5WVmG0gLTUiWFJmKtOgOQOsYtchmKXz5qs5R1oB3Efss65MryjyHavpf7miehXcgEHvMITUv1Hveil7YmjuM8FE8fqhVOTLG4EziU-xWXGeO1rFHD4jkpbOP65EuI1ATtNiKBxEtMYfCiB7FbXsdOasnJBaKMwxBGNCapM7mJ9-EpKihqWZfhDefqIDxd_hKHZct9UeDZyuhNIxq9QXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
إِنَّ مَعِيَ رَبّي
🔹
در ساعت ۹:۴۰ صبح شنبه، ساعت شهادت «آقای شهید ایران» و به یاد نقش انگشتری ایشان
رهبر شهید انقلاب:
🔹
جمهوری اسلامی با اتّکاء به قدرت الهی و با باور کردن قدرت حضور مردم، از هیچ قدرتی در دنیا هراس ندارد. اگر کسی به تقلید از روحیّه‌های ضعیف بنی‌اسرائیل میگوید که «اِنّا لَمُدرَکون» -حالا به ما میرسند و پدر ما را در می‌آورند- ما هم به تقلید از حضرت موسی عرض میکنیم که «کَلّا اِنَّ مَعِیَ رَبّی سَیَهدین». ۱۳۹۵/۰۹/۰۳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/683243" target="_blank">📅 09:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683241">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba2079f6a1.mp4?token=gofmoQOV5rKQor8vV78rM8sIX0qm7zFOW5vWyxTvdMKWq8UO1CCfKf57jm9FnkWpCifWEw9gcEP80MObW-pHDPMgi9IXlyG_PptpaQRQWbPXw5OUAbM2YhTJfoyhAmIfKE7vKWWu9A-uP7dAC0ujSoihIalnorR6YiDoq8jJbDHlaGDDngs7BKeLRSXMxWUU7fffVOWYpY0at4P9P-cZLwR0R8YvCmQuIE0M04ASEXWe31IY03Qcjabycay43Am1ro-gOc0hJ-5APpMT6jtbLFMhz5hLB09aZSuCX9MJPcHdJSkaLkX-4aSImiCd8QgTvbKODG2BLnnHlRK-nljlww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba2079f6a1.mp4?token=gofmoQOV5rKQor8vV78rM8sIX0qm7zFOW5vWyxTvdMKWq8UO1CCfKf57jm9FnkWpCifWEw9gcEP80MObW-pHDPMgi9IXlyG_PptpaQRQWbPXw5OUAbM2YhTJfoyhAmIfKE7vKWWu9A-uP7dAC0ujSoihIalnorR6YiDoq8jJbDHlaGDDngs7BKeLRSXMxWUU7fffVOWYpY0at4P9P-cZLwR0R8YvCmQuIE0M04ASEXWe31IY03Qcjabycay43Am1ro-gOc0hJ-5APpMT6jtbLFMhz5hLB09aZSuCX9MJPcHdJSkaLkX-4aSImiCd8QgTvbKODG2BLnnHlRK-nljlww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای بسیار زیبا و باشکوه برخاستنِ هواپیمای مسافری از روی باند فرودگاه SFO با پس‌زمینۀ خلیج و پل سن‌متئو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/683241" target="_blank">📅 09:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683239">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udnzr9JIAzKXYTKCjFI1jVOswGp1pdiFdvSk9KDv-yiwyGX1dKgKYJi4JTl3LS9CcSOF1LofhH9R8jaPTPMzBJlsuKlmrj5gx-zyMZKHM_CF9ZmFlLcvFBQlZvbnM7LdUSA_gx64oUXpr_jdawGNLI0UG9geKgELKXzJNBTA5fhmwSaxj3f1RFCXlEoW_77tx35q0MzDL5b_VOV10NONRFaCghNO6fP9QUzJ0dbQg1egDa0CfINJ2M1_dI_b7TTIN0cUlifHdsO1SPtxJYu1UwdHgvxGutSSXDWKEg0Ur1J8lRPkKTOLs18TQOI3j5uzGduvzne5xShxXrJ1Rq9-cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
آبشار نمکی پتاس تنها آبشار نمکی جهان در ایران واقع شده است
🔹
ارتفاع این آبشار ۲۵ متر و در شمال مجتمع معدنی پتاس در شهرستان خور و بیابانک استان اصفهان قرار گرفته است.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/683239" target="_blank">📅 09:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683238">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55024570e7.mp4?token=BbWmAkkWut7a_keHSP8mB0W1_FCjRVxiJGNYRhmN3xd0G727puT60NLuO754yZABG2Zd73amYsYj62Z4U7oh-SSNVZG0NX7owlWuB1OszOHobO-Hr85xAoc1lENeKtnbjLb-q4L_0jRupCG03qVeaQmB8_nj7nugP0-XD1kuzHU4wd-aUTIe9ZEvpN0ukkXr9E-d_hCZ3V9DxWDC7U_KJVlq1CWNh1z-LGP2l_Y6Md5co66hOQE6UBKWdZZENMX1okmjN6oJS_aKFAHsHrtc0Z6N3H6ZcNdveyqcjzDZi-l70vGJGJV8fTZ3KK3vlfu01www7ELYYDBb76LYPHQH-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55024570e7.mp4?token=BbWmAkkWut7a_keHSP8mB0W1_FCjRVxiJGNYRhmN3xd0G727puT60NLuO754yZABG2Zd73amYsYj62Z4U7oh-SSNVZG0NX7owlWuB1OszOHobO-Hr85xAoc1lENeKtnbjLb-q4L_0jRupCG03qVeaQmB8_nj7nugP0-XD1kuzHU4wd-aUTIe9ZEvpN0ukkXr9E-d_hCZ3V9DxWDC7U_KJVlq1CWNh1z-LGP2l_Y6Md5co66hOQE6UBKWdZZENMX1okmjN6oJS_aKFAHsHrtc0Z6N3H6ZcNdveyqcjzDZi-l70vGJGJV8fTZ3KK3vlfu01www7ELYYDBb76LYPHQH-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرگ دل‌خراش دانش‌آموز هندی زیر ضربه دست معلم، خشم عمومی را در دهلی برانگیخت
🔹
این کودک پس از دریافت سیلی از سوی معلم خود در کلاس درس، دچار حادثه شده و در نهایت جان خود را از دست داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/683238" target="_blank">📅 09:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683237">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
معاون هماهنگ‌کننده نیروی هوایی ارتش: چهار خلبان پایگاه شهید دوران، مأموریت بمباران پایگاه العدید را انجام دادند، اما سرنوشت سه خلبان هنوز در ابهام است
🔹
تاکنون به جز تحویل پیکر مطهر شهید مجید کاظمی، خبر دقیق دیگری درباره سرنوشت سه خلبان حاضر در این عملیات…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/683237" target="_blank">📅 09:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683235">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معوقات بازنشستگان تأمین اجتماعی این هفته واریز می‌شود.
🔹
اراذل و اوباشی که به یک سالن ورزشی در نسیم‌شهر حمله کردند دستگیر شدند.
🔹
وزارت بهداشت لبنان: شهادت و زخمی‌شدن بیش از ۱۶ هزار لبنانی از اسفند پارسال تاکنون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/683235" target="_blank">📅 08:52 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683234">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef507mFtBtPbXCh6q5FjtVLMkweWnfzgB51H2yaG-MnYc1KnMk3vEXWxJI_Gc_8PlwochUkl-7vIh3r3GmZGcTy2jBUz4OpkWoaTLyQp4cuLiWtlL98zcHgYijD9JTp5VVUOWNfsL_lVZBhHOwhIup4OQE8TuEf-el4_fsYcWveuCPyxyK_Row-evOmp62Bc8Q_SRZD0S_QzYPHJmoolcNeh99dLvprCReo4KFegRjouY4D3prwdJz4Vu2EAL5MjIohEssEGNYLWXO-bdbJOhPtq_Ecnuh4x74ZXEZoW3SpdRGe67DahK_IJ9WGxHY1Tc_AV_19e3JjLWcCa38zKiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۸ نظامی کشته و ۷۵۶ زخمی آمار تلفات ارتش تروریستی آمریکا در جنگ علیه ایران
🔹
بر اساس تازه‌ترین آمار پنتاگون، شمار نظامیان آمریکایی کشته و زخمی‌شده در جنگ با ایران به ۷۷۴ نفر رسیده است؛ ۱۸ نفر کشته و ۷۵۶ نفر زخمی شده‌اند.
🔹
پنتاگون طی روزهای اخیر ده‌ها مورد جدید را به فهرست مجروحان اضافه کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/683234" target="_blank">📅 08:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683230">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/unkZ5Ptb-qJ3StgU8wONbTeVR-6Uw45bj52vWcHypN7kR1mb8itNYI0niRkMYp83hRy-i1-aXXV7ahmEnSmn7zkcWC50Sgl5VI03mNlqMfa8V69yOL6c8JfAOHXVOr1yjmxfvdQgTceoD4BDF3QyUd8lci7GlULfWn0IoXYlDmpxJzf3H3XrfK0mJTBGRmStspuoMU0vdoMftKtw0avY-Q6XUFQ5rqK29tVwDpOc8TWJDNnqRvZxV4D9Nqc2h8WSZYxUOYTE-D81Kam6Gf2T4JgoOUVQXOg64BsiqPhE9Mb1x0tBK2UE8riVMticjh2DaXl4hp3MeBGWJPMKqmMcOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/itepqndtiP5EsIQBKudzHI6xAZQJsDdk0W9EAFbFPk-g6WBVnxaSkb5Ex54qgUZrhNMhqi_BlNosP-1xm-TQzXWh7ey6a3_z0qUGg_jf5PxhmI1RhMVrM0Aa1WjzuHEPRH1218YFe_-fYlaknRTEtNRmiYNpfKuen4IJq4JNHmYyS5JorzQcK6xM-zzPZRSTmSOEL1buUZ9VmcxuhCfxQaGUqk8UJSdc_H__b2qYN_JG81IrMzPfmEJ-eBsLd30K18H_LLUK68SJnMdSVW1SJDV-Q7McLxvxDAtD6SlrOBVmIjhoDg__cGlQ0LREwFdLS78xvl6D4fsJ5wy4lB7cuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nT6_NKFQy8u_dx51F7uUI9eYEHcXtOhlghDciVwmosYD9vV0q2fb029YdlJ6GHR9Rd6kAaVFSgMyTlY6uJXsO2xcdKsm03vctsvaxOkb_flrwj_8buL0CsEqDcYHz_Mebm5es6FIf0cPeg5y1hiwL98q1GuGh-kH_ldhHHO5oQ-ri9RuBd4JTQpLyc6zCKFP4U-fFVT6UTA5R2xT3oxqe2xBPL47eHO7bGWXQpUK6TT8wKEmxr4dFUtKEAA74akt1Tc8eBN_6gyz3Y7ZYQOj2827B7Lp4Jsiv5d-A9Zm3n7aIgZDhhO2oPTpB5qoLdS_bOl3vSlA1Vmw0INYXF1RJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XEIX54Gavj9rcI23OG_dagHg10l4xk5uj3T3Ljz1lspna4yDA4am4OKcgg8KSwWQ-WkAQj3LlDIJjUgcEfN_sJ3gHXCxdtz6m9FWPeySn9azKOmFzyXW1JpdXkquKLgKod6NS50A2gLS-296mtzvnz4XR_37soOUnYQVpom6dPPTbzQ2e4VDW8UyQC9rnQawTWNrI5sFZit3D9OIg9Qg4TzJZZE1cZcr8zG1JAWZFbX36VOgSKaGjIZtqYGKXAWHjlzMdZVU6IfdPYelH_9ndCslytLSfF8rQBUNqoDs33gKpHFpKteai5uxaiJxLvngO7-18b6Hshe7vEyOa6Hbrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اگر لباس بنفش بپوشید، رایگان وارد این جزیره عجیب می‌شوید!
🔹
جزیره «بان‌وول» در کره جنوبی با خانه‌ها و معابر بنفش‌رنگ، به مقصدی متفاوت برای گردشگران تبدیل شده و بازدیدکنندگانی که لباس یا اکسسوری بنفش داشته باشند، می‌توانند رایگان وارد جزیره شوند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/683230" target="_blank">📅 08:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683229">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
تنگه هرمز قابل دور زدن نیست
فرهیختگان:
🔹
دورزدن تنگه هرمز به‌آسانی ادعایش نیست. اگر قابل دورزدن بود، دشمن مدت‌ها قبل اجرایی می‌کرد.
🔹
ایران می‌داند خطوط لوله جایگزین در میان‌مدت اثرات نسبی دارند و از مشکلاتی رنج می‌برند.
🔹
اگر میادین تولیدی منهدم شوند، آمریکا با بحرانی طولانی‌مدت روبه‌رو خواهد شد.
🔹
خطوط جایگزین تحت اشراف محور مقاومت هستند. الفجیره و ینبع بارها ضربه خورده‌اند.
🔹
عبور از هرمز به ۴ درصد پیش از جنگ رسیده؛ میانگین روزانه ۵ تا ۸ فروند کشتی.
🔹
قطر بزرگ‌ترین صادرکننده ال‌ان‌جی جهان است و راه جایگزین غیردریایی ندارد.
🔹
خط لوله ینبع و فجیره مجموعاً ۶ میلیون بشکه صادرات دارند؛ در حالی که صادرات پیش از جنگ ۲۰ میلیون بشکه بود.
🔹
هزینه بیمه هر بشکه از ۱-۲ دلار به ۱۰-۱۵ دلار رسیده و اسکورت هر کاروان صدها هزار دلار هزینه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/683229" target="_blank">📅 08:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683228">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04c72a6e41.mp4?token=fMXDJgSsE5o4DoliRXZPQb6BL7eieBAEJF_Rv7iJClqtrk4jMJaSFDbEzuAo3ImMBP_ycbKaYVwaKGcpRML5ieMFuFLxr-lwk-7ysjDjcWW_hwmLDmjOSYtE2FOGvft6AM3djFs-qT8MssJ_SwEgi-TkF5a5pKLVIF1npZ9DfaCbmxhdpmCy9s0sNREEkrf_BV5Jokm7EgG1nWHUD4nzjGXGAbkIB9Vf_f7M4iYyB3a22G7M0Zq6bHlytXWaAeZFQYNRXI34xRylyPYv0NRn3SodGinP0Ex1DPVE-VfwukXTvAmVZqujpf1ErA51BrDCW0Sea3oTf4AWsuSQbM8F2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04c72a6e41.mp4?token=fMXDJgSsE5o4DoliRXZPQb6BL7eieBAEJF_Rv7iJClqtrk4jMJaSFDbEzuAo3ImMBP_ycbKaYVwaKGcpRML5ieMFuFLxr-lwk-7ysjDjcWW_hwmLDmjOSYtE2FOGvft6AM3djFs-qT8MssJ_SwEgi-TkF5a5pKLVIF1npZ9DfaCbmxhdpmCy9s0sNREEkrf_BV5Jokm7EgG1nWHUD4nzjGXGAbkIB9Vf_f7M4iYyB3a22G7M0Zq6bHlytXWaAeZFQYNRXI34xRylyPYv0NRn3SodGinP0Ex1DPVE-VfwukXTvAmVZqujpf1ErA51BrDCW0Sea3oTf4AWsuSQbM8F2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرونشست متروی پرند بازهم به مرحلۀ هشدار رسید
🔹
تصاویر جدید از محدودۀ ایستگاه متروی پرند نشان می‌دهد که علی‌رغم گزارش‌های مکرر از اسفندماه ۱۴۰۳، فرونشست زمین در این منطقه شدت یافته و ایمنی زیرساختی شهر بار دیگر به مخاطره افتاده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/683228" target="_blank">📅 08:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683227">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
هر آمریکایی متجاوز به ایران را بکشید یا تحویل دهید، ۵ میلیارد تومان پاداش می‌گیرید  طرح جدید ارتش که توسط سرلشکر حاتمی فرمانده کل ارتش اعلام شد:
🔹
پنج میلیارد تومان پاداش برای کسی که هر آمریکایی متجاوز به خاک و آب ایران عزیز را بکشد یا به واحدهای ارتش تسلیم…</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/683227" target="_blank">📅 08:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683225">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/647bfc14dd.mp4?token=vw9xe3ZONp3Nx_oirudeqFzeSOOMgJoDDCD3mrFvxkCEhxUVkEDRvfo8uCo2zwRoJ3rZoR7AW8CdbFQKNpj-JI99cmktNVe-5zjNd1dAWjMxLrI3c91MHRzaxnUcjN9ISnDkEZG2wMnKd0Vd2LjwAvWrQ5SXhEfsQtl505xc7J0iLO6fBMPI7gQ3ED7TviRWETND2cqrSO_wCXRSWtiVnQlxUHdeadW6i5hyh8Swxm5iepmko12l4M1aFRRlT95fyhEpEa-fQ5kCVkC-pc-R2giQEocQfmsA6LrzlkstBdR96ATwARTHYgUJidpVBDaR3sPajzGIDqIG5oWaFbbqqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/647bfc14dd.mp4?token=vw9xe3ZONp3Nx_oirudeqFzeSOOMgJoDDCD3mrFvxkCEhxUVkEDRvfo8uCo2zwRoJ3rZoR7AW8CdbFQKNpj-JI99cmktNVe-5zjNd1dAWjMxLrI3c91MHRzaxnUcjN9ISnDkEZG2wMnKd0Vd2LjwAvWrQ5SXhEfsQtl505xc7J0iLO6fBMPI7gQ3ED7TviRWETND2cqrSO_wCXRSWtiVnQlxUHdeadW6i5hyh8Swxm5iepmko12l4M1aFRRlT95fyhEpEa-fQ5kCVkC-pc-R2giQEocQfmsA6LrzlkstBdR96ATwARTHYgUJidpVBDaR3sPajzGIDqIG5oWaFbbqqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت هیپ‌هینج کلید تقویت و کنترل کمر #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/683225" target="_blank">📅 08:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683224">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eum9eVN1xeKw-cnH6kxkcrTKK53_AujsvOxl9Ti0OY3CjUTey_pxMBTzU95rR-HugA0xrakvnUTkjFH-n_CdfsyhTHHi4DTsfti99jEsiNvEGxo7KQ4XDD7BWl5d7erdb_AXG9EyBBIovWs-NldjbzPaWhlbgaJ7pENEjUzXpKUmBBjj4QuqpCz6L3p_XNnCaMPwF5v34oq3QzpmEzJLREyknfJ9ptLOH3KEexM0IuWTieNYY-OoqbaLS8NMAXHBzcCQKWECBKaY05oZqYkzxnkGuPBam4N15TTJRLOzVSA0ZqbNdPJkuSP9BhYnstQgMsOP1numqKOvuMcnnaKsRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲۰۲۷ می‌تواند گرم‌ترین سال تاریخ زمین باشد
🔹
براساس پیش‌بینی‌های اقلیمی، بازگشت پدیده «ال‌نینو» می‌تواند روند افزایش دمای جهانی را تا سال ۲۰۳۰ تشدید کند و سال آینده میلادی را به یکی از گرم‌ترین سال‌های ثبت‌شده یا حتی گرم‌ترین سال تاریخ تبدیل کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/683224" target="_blank">📅 07:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683222">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
امروز؛ پایان زمان مشاهده و تأیید سوابق تحصیلی داوطلبان آزمون سراسری
مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش:
🔹
داوطلبان آزمون‌های سراسری و پذیرش دانشجو-معلم برای مشاهده و تأیید سوابق تحصیلی تا پایان امروز فرصت دارند، به سامانه جامع آزمون سراسری مراجعه کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/683222" target="_blank">📅 07:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683221">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین|فصل‌دو،قسمت‌آخر</div>
  <div class="tg-doc-extra">روزبهان بقلی شیرازی</div>
</div>
<a href="https://t.me/akhbarefori/683221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
روزبهان بقلی شیرازی (شطحیات و شکستنِ نقاب‌ها)
🗓
در قسمت آخر از فصل دوم، بزرگترین کلاس درس تاریخ را برای «مبارزه با ریاکاری و ظاهرسازی در سیستم‌ها»، «پایبندی به حقیقتِ وجودی» و «شجاعت در شکستنِ تعصباتِ منجمد» مرور کرده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/683221" target="_blank">📅 07:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683220">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f964f5414.mp4?token=GMI10ifLy21GHefO3ABBHHO4QgJQ2iB3IWmzDhYziEkoTR1GpcygT_12d-DqrCREurKnu94ahEb8e9AWHnq95e6-1qhC0-TtvqnzJM3IIdTXzsiXyjRr2uePPIzQKkWdvQ-m1MbtH0-XQW2icN5Az1SJuQogUF0jJ_w-128w9ehooMbEl2OZS2QrvsX-nB6U-9CRf3qTS_lsnjFNP8e72kpOEcAB4I2hmKbqFfY_SWSQba827Ght5vGkUUWccMYR_TTTVJBITFRnFYOAdJ4DrL1ncnzo6fKgVNQw64QkgKDVEOcdRfr_7BlYf_rFM4VmaWeC5Z48HRINLpwNRG33I6LlsN2aiqYGQQoyEMHeqkMQuDZZ7g4tieI4fa49PMDGVZWnp1hbu5iFiMPscAGptSWbxL7LJFLY3H4VgrfQZBPUdbtix2ilZh-T2CvL3Dp_nkxB0qAMd5leSpjVXeHTZA5WPsIOOxaAsQa_zaAZ_zSgemSmD3N0ez5bNEMm7IAe64Ad_Om0VQLYCjzpQ6qaa2WlBd5g9IRCiPd2KBR2pfZ8XSeB5sJj3ez8ggGmNn1fEJgBuzSxcLnbvWtyrqbI4NK2s-D4oTz5yeEj_y0rFqw46fuab8gYIS2IvNSb7R6nLPCYIjEmhpUkJO1G7plDcudn5rFmcesBBU11s7x4Lm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f964f5414.mp4?token=GMI10ifLy21GHefO3ABBHHO4QgJQ2iB3IWmzDhYziEkoTR1GpcygT_12d-DqrCREurKnu94ahEb8e9AWHnq95e6-1qhC0-TtvqnzJM3IIdTXzsiXyjRr2uePPIzQKkWdvQ-m1MbtH0-XQW2icN5Az1SJuQogUF0jJ_w-128w9ehooMbEl2OZS2QrvsX-nB6U-9CRf3qTS_lsnjFNP8e72kpOEcAB4I2hmKbqFfY_SWSQba827Ght5vGkUUWccMYR_TTTVJBITFRnFYOAdJ4DrL1ncnzo6fKgVNQw64QkgKDVEOcdRfr_7BlYf_rFM4VmaWeC5Z48HRINLpwNRG33I6LlsN2aiqYGQQoyEMHeqkMQuDZZ7g4tieI4fa49PMDGVZWnp1hbu5iFiMPscAGptSWbxL7LJFLY3H4VgrfQZBPUdbtix2ilZh-T2CvL3Dp_nkxB0qAMd5leSpjVXeHTZA5WPsIOOxaAsQa_zaAZ_zSgemSmD3N0ez5bNEMm7IAe64Ad_Om0VQLYCjzpQ6qaa2WlBd5g9IRCiPd2KBR2pfZ8XSeB5sJj3ez8ggGmNn1fEJgBuzSxcLnbvWtyrqbI4NK2s-D4oTz5yeEj_y0rFqw46fuab8gYIS2IvNSb7R6nLPCYIjEmhpUkJO1G7plDcudn5rFmcesBBU11s7x4Lm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزبهان بقلی شیرازی، عشق علیه دکانِ زهدفروشی
#پادکست_کافئین
| فصل‌دو،قسمت‌آخر
☕️
🔹
عارفِ سبزی‌فروشی که نشان داد چطور می‌توان در برابر انجمادِ فکری و ظاهرسازیِ مسموم ایستاد و با بیانِ شطحیات و حقایقِ بدونِ نقاب، تعصبات زمانه را متلاشی کرد. پایانی باشکوه بر فصل دوم کافئین.
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtu.be/55g94bwW9F8?si=URz67u7w_S1WBO8N
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/683220" target="_blank">📅 07:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683219">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6zDjUkBI2FDqrf0nVaHQtXTLc7FtawTkBMAsaBJmFdkRlaLq3UZ1nxQXMM4-uA4l1Ad7S1DyAZcmc-zvQNo9ppFqJj4GyPgpVxXDQSqZC2GIx1uGmIVnPEDRPccRu8ZNE0ww-mYvZbODLqTGo8G5F8XE3rwyhGkhnIWK4sbfgsbcc72rgOt6_Ns6wvxLhlhWoYJcSHPHQY28QCrFhTqWDbsk8_tVV9x1D8bWnzgLBGLLDtXtmVMA7cr9jqCJDHcrEamF1KPqo5mQQc1yQ26ktCWM1mPL7BAB5yCDpDgnyB4ha_7EAzVnE3s60Ti_W5LKl2GwLeE-Cnq1w7Jj81Pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۳۱ مرداد ماه
۹ ربیع‌الأول ‌۱۴۴۸
۲۲ آگوست ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/683219" target="_blank">📅 07:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683218">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f9b48103.mp4?token=K0MrY2pOYamhEBHopgE123fDJvKyAWhKagRxog-Db1D24E-cKybThd9qk5KsVdPQjqU8FQaXZOAn1emCvkTtdD8GI7KziMcqJMUmqr2YWNNeSc-dLtpKa5hj9ZLUkROMak_V1K9zwrrUGYUZBDGEfsUds1Yx0KrgBvUtQ8fKl2RGKswQuHvsroEINZj6WN-Jk4h8jNti1inMOoKqStw1C8nkBUWzpugbFsDvHejNL7zuSxq6f-VGt51NzJ_BuvEggOW2pzfFY633UJ4GOgJaIUnalG5cjhCalUTo71VeSx4Gu-RfN0HBnlobJRR-ochhQYVExzj_3m1edWZ7i46l4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f9b48103.mp4?token=K0MrY2pOYamhEBHopgE123fDJvKyAWhKagRxog-Db1D24E-cKybThd9qk5KsVdPQjqU8FQaXZOAn1emCvkTtdD8GI7KziMcqJMUmqr2YWNNeSc-dLtpKa5hj9ZLUkROMak_V1K9zwrrUGYUZBDGEfsUds1Yx0KrgBvUtQ8fKl2RGKswQuHvsroEINZj6WN-Jk4h8jNti1inMOoKqStw1C8nkBUWzpugbFsDvHejNL7zuSxq6f-VGt51NzJ_BuvEggOW2pzfFY633UJ4GOgJaIUnalG5cjhCalUTo71VeSx4Gu-RfN0HBnlobJRR-ochhQYVExzj_3m1edWZ7i46l4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اختلال در سخنرانی ترامپ
🔹
سخنرانی دونالد ترامپ، رئیس دولت تروریستی آمریکا با حواشی تازه‌ای همراه شد؛ ورود یک معترض به میان جمعیت و فریادهای انتقادی او، روند این سخنرانی را برای لحظاتی دچار اختلال کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/683218" target="_blank">📅 04:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683217">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAOHbBcmpGsGqro2ym4IVh12T51NOkxXGMndIj6H4T5aRmygSYbggJN9pvY99Yk3yOv7qJeC50mIMbQkSB3kOdxykJWARjGb4hJKgtBD6L0kVbsbNA7PKcNc4kMGXVrxOJFJuGTe3TJG7BrbnIiz3t5S_GJkoiYi7DSNo2-4Vp0ThLCl3qY3RkDv41YYbXX5_Vaeq_GI1T87GbUN-JM6qR0aaDkfxIwpPyWuZhirUwYrFQJsFw93MKJZXR2fQ-_vEyd0PW-sv4oNhCgMUL1cVv_XVlGATFr3CCk7aKORALIG-LJUQt_z_lGAQMucdWSnUaiZeurXR-fPU_oBkrTXbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش وزارت خارجه به تحریم‌های جدید آمریکا
سخنگوی وزارت امور خارجه:
🔹
تحریم‌های جدید آمریکا بسیار فراتر از یک «جنگ اقتصادی» علیه ایران است؛ این اقدام تلاشی برای تحمیل حاکمیت فراسرزمینی واشنگتن بر تمامی کشورهای عضو سازمان ملل محسوب می‌شود.
🔹
هیچ دولتی حق ندارد بانک‌ها و بنگاه‌های اقتصادی کشورهای دیگر را وادار به قطع همکاری‌های مشروع با کشورهای ثالث کند؛ این تحریم‌های ثانویه هیچ مبنایی در حقوق بین‌الملل ندارند.
🔹
ارعاب اقتصادی برای وادار کردن یک دولت مستقل به تغییر سیاست‌ها، یک عمل متخلفانه بین‌المللی است و همراهی آن با محاصره دریایی، مصداق بارز عمل تجاوزکارانه است.
🔹
تمکین در برابر این سیاست‌ها، مقدمه‌ای برای بازگشت به دوران استعمار عریان و فرسایش کامل مفهوم حاکمیت ملی در نظام بین‌الملل خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/683217" target="_blank">📅 03:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683216">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aab003f1d.mp4?token=cCeuHNdzeHtkw1IyzY3SUifYLLOmTeTiVlAiSO8emst7HvnluR_XtryfKqwscZyt3RAof49UwWJ760I-xJZZWkvdvUrYdIsR5-B0Ee_fNPkL4-DTZ5uYgLz8XdAcB_0DKdhGuUBpZtp7uASezzrWrC_rKv9MzWQOX6CLHeEMsUK68WG7FedHBm3xvi2NXPFNP8VXbyQcm9vdClu6CUcCv_YDKihz1NXZBgiLJqVHJ2u2S2K7YgeDDtmg73_IFY0Zr0Pyze4QCLkLoNdS5lsuFc8NIG_S_9pyC7Q64w0SGkg398QhqwqWJ4RNGHokqi4DT4Znpx3WJmYLRoxXoRTcCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aab003f1d.mp4?token=cCeuHNdzeHtkw1IyzY3SUifYLLOmTeTiVlAiSO8emst7HvnluR_XtryfKqwscZyt3RAof49UwWJ760I-xJZZWkvdvUrYdIsR5-B0Ee_fNPkL4-DTZ5uYgLz8XdAcB_0DKdhGuUBpZtp7uASezzrWrC_rKv9MzWQOX6CLHeEMsUK68WG7FedHBm3xvi2NXPFNP8VXbyQcm9vdClu6CUcCv_YDKihz1NXZBgiLJqVHJ2u2S2K7YgeDDtmg73_IFY0Zr0Pyze4QCLkLoNdS5lsuFc8NIG_S_9pyC7Q64w0SGkg398QhqwqWJ4RNGHokqi4DT4Znpx3WJmYLRoxXoRTcCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ قمارباز: اگر در انتخابات میان‌دوره‌ای شکست بخوریم، من استیضاح خواهم شد
🔹
آنها من را استیضاح خواهند کرد. اصلاً نمی‌دانند چرا #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/683216" target="_blank">📅 03:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683215">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
سخنان احمقانه ترامپ متوهم: در ایران هیچ کس نمی‌خواهد رئیس جمهور بشود  رئیس جمهور جنایتکار آمریکا:
🔹
در واقع یکی از بزرگترین مشکلات من این است که نمی‌دانم با چه کسی در ایران باید معامله کنم.
🔹
این تنها کشور در جهان است که هیچ کس نمی‌خواهد رئیس جمهور شود.
🔹
آنها…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/683215" target="_blank">📅 03:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683214">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
سخنان احمقانه ترامپ متوهم: در ایران هیچ کس نمی‌خواهد رئیس جمهور بشود
رئیس جمهور جنایتکار آمریکا:
🔹
در واقع یکی از بزرگترین مشکلات من این است که نمی‌دانم با چه کسی در ایران باید معامله کنم.
🔹
این تنها کشور در جهان است که هیچ کس نمی‌خواهد رئیس جمهور شود.
🔹
آنها می‌گویند: "چه کسی می‌خواهد رئیس جمهور شود؟" "نه، نه، من نمی‌خواهم رئیس جمهور شوم."
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/683214" target="_blank">📅 03:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683212">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
گزافه‌گویی مکرر ترامپ متوهم درباره ایران: من در حال حاضر تنگه هرمز را قلمرو آمریکا می‌دانم؛ این یک قلمرو آمریکایی است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/683212" target="_blank">📅 02:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683211">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDOAwAXlIBalv0PKTjOOSytwEFzkGl-Rqb4JLWDHpKGQGMQy5HnvrrzrIwnvgNHEGFNm51bvmUTv_IZ1CUdVPzb511fqUhBwJR0sg06y6tW0qclnrFmBsO-sz2Zal86ZJZLqMLxupUbOjwqYuUsrKuDofOHaCobP7SUBXqkprMhs-GAe2tsfqtvWJKc_Xt8nK6Wdtkaao4Fl9LObI1j9JfXW_O_QA3rUoG9gM_CVErWSrVHPpLRxhT9vS3BN4mG3ICaL_RkUrRj15cNolxLEFiVM7ByDqU5T9_1-ed6jzr3hx-v30_wruWpJL1RsZ9iQgZat3W1JOvino5Suz9QrMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون وزیر جنگ آمریکا کناره‌گیری می‌کند
🔹
منابع آگاه از تصمیم معاون وزیر جنگ آمریکا برای کناره‌گیری از سمت خود تا پایان سال جاری میلادی خبر می‌دهند.
🔹
اقدامی که در پی ماه‌ها تنش و اختلاف با «پیت هگست» صورت می‌گیرد و خلأ رهبری در ارتش آمریکا را عمیق‌تر خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/683211" target="_blank">📅 01:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683210">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed38c6c628.mp4?token=VK9-qkEX2LWst9AViR31x-sKinhtgEJ8umkG9hdQpZ3VScG2410SHuyWLuG5HuQErv9xvYsoo-UOEb4cUWo3jUbWSuGPNENIzvW0Vos5s1xVlum0X4AAv3K_kvz_pNWqeVzcQCIn3nywzUUYj_J7PxcLTc8-0DKvBVckyGwknOdRBsimxvDVllSZoMpK6xe__R-zbLqRm5TzZwfPHO9ywgcl8sNSKDuYkq5ht2-xqVKG2H9JU1WVB0xdr6jJLnFGw1Dvw7mTPTigZOci5NuW1uoVTWXK-ihrNlpMXuIX0P120JSsPpyXaMqjIxeWaTN1NpvJYkTY-qoNba7_O9CMfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed38c6c628.mp4?token=VK9-qkEX2LWst9AViR31x-sKinhtgEJ8umkG9hdQpZ3VScG2410SHuyWLuG5HuQErv9xvYsoo-UOEb4cUWo3jUbWSuGPNENIzvW0Vos5s1xVlum0X4AAv3K_kvz_pNWqeVzcQCIn3nywzUUYj_J7PxcLTc8-0DKvBVckyGwknOdRBsimxvDVllSZoMpK6xe__R-zbLqRm5TzZwfPHO9ywgcl8sNSKDuYkq5ht2-xqVKG2H9JU1WVB0xdr6jJLnFGw1Dvw7mTPTigZOci5NuW1uoVTWXK-ihrNlpMXuIX0P120JSsPpyXaMqjIxeWaTN1NpvJYkTY-qoNba7_O9CMfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجارهای مهیب انبار مهمات در لیبی
🔹
گزارش‌های دریافتی از لیبی حاکی از وقوع سلسله انفجارهای شدید در یک انبار مهمات در منطقه «الغیران» واقع در جنوب شهر مصراته است که موجب وحشت ساکنان منطقه شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/akhbarefori/683210" target="_blank">📅 00:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683209">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
صداهای شدید در مرکز تهران برای جشن است
🔹
امشب همزمان با آغاز امامت امام زمان(عج) استفاده از برخی ترقه‌ها که صدای شدید شبیه بمب داشت، باعث ترس گروهی از مردم و تصور وقوع درگیری نظامی شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/akhbarefori/683209" target="_blank">📅 00:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683207">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0fcce2754.mp4?token=K5FZUdS14_KqR-WXnHSZeslu5hxT6II0dJyIsVL5LfVHLkcf86OzSao-HJQu2fXvdw7jeItggHuLcpBVQ4eIpAITLp-bGMvGqWsaQR5RHIUZAaCZuHxp1GATtTYsRJ_4Xq-QAliEblK-thl00biz2KTtsVB35_rSpNgKKjHjx7jfpsg6LN9RQAFee1MGs8lRZFsdf8ytDE-ksTKusFW_P-miqfLuxPhTwPv77y45jQurQ_kKfnh3HhUfKOSlVtHcf41pOkPiv5tqmTPQDPdfK2SuZnHG_Pd77UZ-CrkW8sTVVrX7NThe6W3ot0Ve4diYtRGiF-cBdcJeU0MvlDgLWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0fcce2754.mp4?token=K5FZUdS14_KqR-WXnHSZeslu5hxT6II0dJyIsVL5LfVHLkcf86OzSao-HJQu2fXvdw7jeItggHuLcpBVQ4eIpAITLp-bGMvGqWsaQR5RHIUZAaCZuHxp1GATtTYsRJ_4Xq-QAliEblK-thl00biz2KTtsVB35_rSpNgKKjHjx7jfpsg6LN9RQAFee1MGs8lRZFsdf8ytDE-ksTKusFW_P-miqfLuxPhTwPv77y45jQurQ_kKfnh3HhUfKOSlVtHcf41pOkPiv5tqmTPQDPdfK2SuZnHG_Pd77UZ-CrkW8sTVVrX7NThe6W3ot0Ve4diYtRGiF-cBdcJeU0MvlDgLWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: درباره تغییر رویکرد ایران به سمت جنگ اقتصادی؛ آیا این نشان می‌دهد گزینه‌های نظامی برای آمریکا محدودیت دارند؟
🔹
ترامپ: نه، اصلاً. این فقط به این معناست که داریم می‌بینیم چه اتفاقی می‌افتد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/akhbarefori/683207" target="_blank">📅 00:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683204">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENvadn7ZPh_ViYEik13FsWaN1cvo1BQTj3GKLLxo7DcYNsqyoNSWMqJVgdOUpa6e-NsZoixGzJ2gwNgPo8KiCeT_nLwh38eIYJL5NgbOgM_J4FIsxZQhb78l79hoEg8XriGtScQiu6fudxxrJcj4yCeR_4LokGCC6Z5DEgJaYuL5cuHN9aJ7BdD8gOS02d0c2jTBjLB3MND7dwWCA35xgkDDRL-jkTjSgDwVsBOEf-d61JHvQ-TSIzU4D8Sl7ZW1CmciqifO3M4UThExT9-TogjVuNkVVLYzTa4r3G6Jx_JB0cP8b8v5nnH-eMFm511j-zDoMLF8QqVjmO-Hja630g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار اطلاعات جعلی از سوی اسرائیلی‌ها علیه ترکیه
🔹
وزیر امور دیاسپورای اسرائیل، آمیکای شیکلی، ویدئویی را بازنشر کرد که مدعی بود ترکیه به‌طور مخفیانه در حال انتقال سلاح به سوریه است.
🔹
شبکه ۱۴ اسرائیل، که از حامیان نتانیاهو است، نیز همین ویدئو را با همین ادعا منتشر کرد. اما این تصاویر در واقع مربوط به سال ۲۰۲۲ هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/683204" target="_blank">📅 00:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683202">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcB_90slyn734zRDCEsP-5UBnrt7cdZJIof_UiMZORoO42t2AFTTU7ce_Lm3HDpIwm0axbxeoxr9ee4vKotyMIPNgwIsBkAxYvD3GnAw6v0FAKfBQIuBBz5M7guGMtvKZQVlfeDuLgmgnoStU64R3k43iUNLFLLenFtHKsQa8s8EoqnHOuxrU1rDmbTVamzoMFPDBZ9i9F2ijXc3Jfz_0AIBp8w237Ls_lB-qmg-ZF328Ig3vyukAtV6mKei1dIYX0caDUrWL99lJUKr2YeSU7ZYVZXSWTi-6rx43sEKxXc9Z12oISbna9nBL7bSLzMOgYLNjcUm5QaiVGfGEN1rAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/683202" target="_blank">📅 00:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683201">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
ترس ناتو از حمله ایران به بلغارستان
👇
khabarfoori.com/fa/tiny/news-3239213
🔹
ماجرای جمع آوری کمک مالی برای پسر و عروس معصومه ابتکار برای ماندن در آمریکا چیست؟
👇
khabarfoori.com/fa/tiny/news-3239408
🔹
کار به پیک پیاده در ایران رسید / درآمد ۲۲ میلیونی بدون موتور و بنزین!
👇
khabarfoori.com/fa/tiny/news-3239303
🔹
حرف‌های جنجالی شاکی پژمان جمشیدی در حضور ترانه علیدوستی
👇
khabarfoori.com/fa/tiny/news-3239280
🔹
اظهارنظر جالب یک روحانی: در هیچ روایتی نیامده که صدای داریوش حرام است
👇
khabarfoori.com/fa/tiny/news-3239216
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/683201" target="_blank">📅 23:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683200">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d311a6232.mp4?token=vYtSI6mJXnuFvtr38SMLXql0ZQ-FGhGr1Xq_L-hIsrXSi3qc7N-VgeEAh5SUmQlLX1xtNoMEYDNyGgTXihaBdEOZOqdNyil9y0i8Se-P-W0agBKmY5l_pD_jFmn0DkgNbT_TJlQpR6KX7V7c4XC-9dz8DCJF0nZjNcQeB2FXMtMV7SAxFgrUaLpSFVcjb4rej7iRGC69TkqhiCVerP6vBD46WMgsZx-acgNrAsi7O05v-SNPyJBXl4k2jf9Yh0MjLFyniglNjclvAkefSCpkdqiG3u6nFNF6DShpQIhApVxGMPZOzSbFjq22APDIl_rYHmOTFb6x1cg3sV5dyI2qbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d311a6232.mp4?token=vYtSI6mJXnuFvtr38SMLXql0ZQ-FGhGr1Xq_L-hIsrXSi3qc7N-VgeEAh5SUmQlLX1xtNoMEYDNyGgTXihaBdEOZOqdNyil9y0i8Se-P-W0agBKmY5l_pD_jFmn0DkgNbT_TJlQpR6KX7V7c4XC-9dz8DCJF0nZjNcQeB2FXMtMV7SAxFgrUaLpSFVcjb4rej7iRGC69TkqhiCVerP6vBD46WMgsZx-acgNrAsi7O05v-SNPyJBXl4k2jf9Yh0MjLFyniglNjclvAkefSCpkdqiG3u6nFNF6DShpQIhApVxGMPZOzSbFjq22APDIl_rYHmOTFb6x1cg3sV5dyI2qbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض مادران آمریکایی به کوتاهی لباس دختران؛ ترند تازه پوشش کودکان در آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/683200" target="_blank">📅 23:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683199">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpMbngukxT8JBuEN39xhBRrkljzv8g8Km-ISDcKg2dURYFBGe-Y2YI0gcwBkerWvt0nqqzxofrbBNHSakpOJ2vv1u46BubV1wdMdUJbqGXWSbcmIjN8nFep8bztbqNgBAvGwIJot0lAMwXz_GBflsurdN70lBXSElUqsAN8D8ZjEbaDP2Ists-MzhDbK7soet6wueq2fmI1DPhDMsobDlQhmHYmOeVBiwiMvx0Jo75Idj4EfJUDNARvplCik6mK67Js38GDlmmCw2CBOr74LWNu6O1JqsbyNHvsBhpqwwdNUgucB-bDZKwfYs6Xk_Vb-9J-nWFbwxl0WtAyftQdwLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینستاگرام، صفحهٔ «رواق دارالذکر» مزار نورانی رهبر شهید انقلاب را مسدود کرد
🔹
صفحه اینستاگرام «رواق دارالذکر» که به پوشش حال و هوای مزار نورانی رهبر شهید انقلاب و شهدای خانواده ایشان در رواق دارالذکر حرم مطهر رضوی می‌پرداخت، ساعتی پیش از سوی این پلتفرم، از دسترس خارج شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/683199" target="_blank">📅 23:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683191">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NaYle84aFLteA2usjQViIWnJUtCFWmdP9yLve0W4Yufp7BqTVmAQmkJ0sdKuTUZxzbVvlOtiBHRd1MB1oe2f4Sl4aSAibEmQiAxLiU9PgeeVCFpuqtJAK4cI6GcG5i_q6YPlMPJOOI0xhbBsOOihyqkW40QVMSu4mQ_fQHW0G5ZWeHTXjJnpy7ALdWTC4lwGUoeuD7K1KnQZS1sM6JnEk34pRRpg-P1mYVXNAxS_i0zlDhx8en1CO1aBMtY5DAptdX5CKgQbz4Y7UueQAzuNzlsj1PdhSn3d5cRVQNVYd_P6Lvw91GGCCVl-9pwg1P7VgxyqIY9Y5DPT9z5CRnf42g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qh3xQ99GbxYYxTjKzNLgitFWmCpuAXq8cTrZm3SA4xeSof5X-ij9DaA6vQSXE6LgcAX_ZkkeYNMyfALjMWd9S5iiLdEQ26nsJOcYCglvfqF0GaTmAy9iVUozM2_R3vKGI4PUDu4rc48uyKfiIl2khx541ze5JMicARq7CEY90y-xSy2j5o5ikNEnY2AcuyuFd3qabuJcRbelrm41175tReIuBa6UzprzdH0Z8KgbKjYBUXluJPiTt1oRKVy2j6tmbnc7b-d8JjcbLzLxGuOsF7-NavnZHRmyWQxPnqHkeZhyCrXrXkhRdidkm7h1Cd6EUfTviRbMX0l8Zc-LwwI4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XXkpEzat18cLGLGX_Hb8RsqJqKB89v4PQyP7LOyPanj9zlZs3GCuSrTPLLX-XZQW3wgFCnIpjaaH-y_4UD5i3rlNTuwErjtR7ALGYiAXpGF10X1mSoqcd7lyZSxK0nC-_GWJku-7AbMh2eM1gVSq1aYgHBZRfqnJ-v7P_qim_VaoaEO4FMb2MhwPVwxGuTCLaDDNb8de3GnVDqZLOGiicG7zGepscUrcTnTgYqjjSLVY-GAnYgbpB-qDkjz0aAy-9UZ-_UszjebBmZ3_j--UgE9it98OjmrIGTt_KdE6wm8pfNCEGGJDxvMbLp8ntwM00ZyoAw3alaKGJBMkLrU7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAkhmw8tcpfpgCqvHH6PrqNpfnGTAyOTD6Mi4c4wvNCaHTf3Vh6Uy3mpBC9lAUQfFk3KsafpLz8K0ozs8_-CHTETNqlsjliFqxZA6rNCEQ6sBhE7aJKR0asuHQhL6vu_Dm1NKbcP4S7sQf8_wUJGtdYlQBFArbG7Bb9h-aCWbFUXcMEHOTKfXsQTvTsjxSkHxAJYQ7o-8Q4_5idBuELmddZNqHinW2M4AVhkWx9nFP1IOOffw6i9nyEF9llju09nYC58tsmVVL4_t_KbBPm_AwQ87B3FWSx_e7b_RPWXrWPHI11iOsXIFEzFF104tUmsw-GctlgOWcMETrgkEA76fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T749nsDttiBYV15VIz1HCXfSuLrT60onVQbOLeLCpL1kPoUyy-PUkiuOkG6DPFF8gNGxuAp3-6A2lfWGojO5NTkvIGYoeTyCLqi7i5oKr010AgI52FmP4ERKc7HHtmLogfzOFj__1wNV31uj_IaLTD6oCMPKNJdHON9p6Ycwr4exqmpjM09tPPM0eJNAFtqY5uKfAWT2JOzfGBYgj1Na2T3X3-TT2r_yw6Hl5CQOGp4cfDp19T41s5RZXoLplujWK4HYBgDgbvFdeKOl0Yk7Al3VDJW46Pon6eAD9NB8JqYqbiF7L15fm7jrI731qd9TjMxw9pkYohVF_xVIZHCd_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQvPdMwTXttcM6AH5xYd2DeGLf8_0wpXYq3gx74E1ywV9ZX_MtKOBA4Vs7Rvi2oIK4iU9aOK5phA5cNJOsyoisGh5Yxuxt-lacflcOFd--deT1bHriWL2w0LIIwj4v3tySkvfNqDyj-pe8wd3oSPlYfy6K2QCdJlR1CqZr7QwfUan2iWcMItjoTLAjPX6yOSxHW0EcspQ6y-dmH0AquLz41cYsAKF51KpyDJzyz--3QgrGsuCzduUIljge4R1ivUqE6rSub0xVNOkcZhmXoWBlYAznx1ZayyeSxO6EWJGacDJ_s6BuVrBfdqBAexDNfp9f77GGn_1nt1EYZvZJZ2kQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند ترفند خانه‌داری که زندگی روزمره‌تان را راحت‌تر می‌کند
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/683191" target="_blank">📅 23:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683190">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrZzWG_LhPH25DlUy9w1pXGeS7y2Nl4Gt3VPQdKl9HXBzgPtjXTBfErD4qg05-fdONM0bWKsCj1emCJLUhaPuujtFD2uOLNijM3K9oOkjwo6WgFBIFla2uI1UIT6ixjR8VUAqAXsG4MPKiWNDANC_7kzNsCiNa7EFcXujADJIwXR24nYgCKc_3zIp5k59_wUj5i-NxOLFCDzoZFfDUMux4YVLuH10-XmyP8XYFmu2XliXJokOdE0J1Fi7H23FP97Ed2g234mRDzEZ3yUtdScLwQllDkQsyQQgI3dwESTMl9Ld74MJaBCx3dHgWz55GeLMsB33b67tToQXpt6V2MJWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری متفاوت از پزشکیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/683190" target="_blank">📅 23:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683188">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f36536d542.mp4?token=CIOFKi6VouQKnfrvFLanpHA1H2DGdtwnSQMnsjyKtP3hsKOrl5lD1uh-kwFDnHBXnr8o1VJxRgYDR3nlMXLzADXJ3jPvAPWxFNOqt7OxEWCvPn_yGNTELUEoterx0RSVk5sPawQsqDY8AfebWw9fUFL_-1PN48biTLGeQCzuV_vnfz4XIqS8mYoG6dkTm3YlB32EBHLANvMUhjDDA0_XeKMwnX5t44P0PDI1OawCZU-JkQGhkc1T5mOl8kggYMNDnXfwkuYoKq8CoW5tfWZfP8v51bM0TjoT6bWvNxh1W4upJoTEZSJnbWWoREM_nJJ6O5v8kmPo3PftjaAKonlYOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f36536d542.mp4?token=CIOFKi6VouQKnfrvFLanpHA1H2DGdtwnSQMnsjyKtP3hsKOrl5lD1uh-kwFDnHBXnr8o1VJxRgYDR3nlMXLzADXJ3jPvAPWxFNOqt7OxEWCvPn_yGNTELUEoterx0RSVk5sPawQsqDY8AfebWw9fUFL_-1PN48biTLGeQCzuV_vnfz4XIqS8mYoG6dkTm3YlB32EBHLANvMUhjDDA0_XeKMwnX5t44P0PDI1OawCZU-JkQGhkc1T5mOl8kggYMNDnXfwkuYoKq8CoW5tfWZfP8v51bM0TjoT6bWvNxh1W4upJoTEZSJnbWWoREM_nJJ6O5v8kmPo3PftjaAKonlYOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار طلایی‌نیک، سخنگوی وزارت دفاع: یکی از عللی که سال گذشته و امسال نمایشگاه نظامی برگزار نکردیم و رونمایی‌ها را متوقف کردیم، برای غافلگیری دشمن و برای صیانت از اطلاعات و اسرار صنایع دفاعی کشور است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/683188" target="_blank">📅 23:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683187">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRr0Do97Aow6mBrRn00ZxtQRLj8JyYiruR4VbeSsBVaJDhaRUiGPQpheuURmKMS5Ej4wwD0sCubSqp7f_vjJDvbS4YWWRINjSZzorhamxStoeVWRdhj33z-xJGeOn3k3raUDInPybIM3A1TWaxNccWMIiXA0oWGh34sniOxMNPqIkcnVDZTE6MnJDVox9weAazHnxYX2-YbbC2R57mBASTE5ifD4bvocGp4jM2iOcLLyqAGnWpT--71ZdLgTnO7ZUZsC_NJOUolyTreJTzQTxL3nJWcKF1zY5pqM2EER7hR7HGKCnJPLqxpbrMNS5Wu4UPKeB_lZDU3kj09iyX33Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه وسیع انصارالله برای تنگه باب‌المندب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/683187" target="_blank">📅 23:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683186">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ea7675b3.mp4?token=cbcwh0rqAa1V0Sx41wMXgUQn9z0Z3THZflNrn0wHZ-j3TfeoLZy0A_63F0VisLMDsib2nrm1Lx-doPjJjTdXa_JbQQVVHLny0RvUS_nQvSoC8OasW1Len5hdWREUiBk3XZbZaLHi9McUnKLeRg9BViQGSdQSA-hMpqg0JcGpMGVlmeO2K9553ZJLWTE_jCh-XfoWBZAmaA7We6ahVClmMg5IfcyiCk9xCbyqlSrIUo_PSOUtNTAyMh3wsw8HseSlmY_NsNXUHahhMQVQwyAxwRwlF7yJXcGbhEp8HWEHsP5WNvturx-NGdeieWWCL-c_5omszMPXNcbxe0n6dS3wFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ea7675b3.mp4?token=cbcwh0rqAa1V0Sx41wMXgUQn9z0Z3THZflNrn0wHZ-j3TfeoLZy0A_63F0VisLMDsib2nrm1Lx-doPjJjTdXa_JbQQVVHLny0RvUS_nQvSoC8OasW1Len5hdWREUiBk3XZbZaLHi9McUnKLeRg9BViQGSdQSA-hMpqg0JcGpMGVlmeO2K9553ZJLWTE_jCh-XfoWBZAmaA7We6ahVClmMg5IfcyiCk9xCbyqlSrIUo_PSOUtNTAyMh3wsw8HseSlmY_NsNXUHahhMQVQwyAxwRwlF7yJXcGbhEp8HWEHsP5WNvturx-NGdeieWWCL-c_5omszMPXNcbxe0n6dS3wFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهر ونیز چگونه ساخته شد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/683186" target="_blank">📅 23:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683185">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFM1X4KtUjz1wh2sYjMuYlcTH__oG0tattUgXjQ9eAQ05CnVFnzzo0VC-04quS9kRPGoop5cgRrwb7fDlhY8yuKoMxn0WJcIGINZUg81udIjoD-xhb1x5VNLZtvHniWDXdtD-Sz21OZjLaE7LVXoNcLYwSQwMxbfW510UaIGsZOXOwtDld7D4z6kr8A6I3UsWwvrn2afvWtzvv3plRzf4coAdbAPMysnHiAtV7SMcJceIG2i61_NV8_i4xmdrbgX2UUCDNdmCEXBMw2Iqcl6_FywyEOn2-vuDvdWvY2mSETIIjTkQa3nz0wp2ifoStKF_aj3duTPMnldnLetMUrzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسکات بسنت وزیر خزانه‌داری آمریکا در حالی از اعمال «سخت‌ترین تحریم‌های تاریخ» علیه ایران خبر داده که تصاویر او در کنار همسر هم‌جنسش، جان فریمن که در این عکس پشت او قرار دارد، بار دیگر مورد توجه کاربران قرار گرفته است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/683185" target="_blank">📅 22:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683183">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UryGa-bXNJkGsbihavRz0ZLNUD10zDtScItn05hozEu7TK_WcJhZSL-sodm5CjdbgEik9m75cWCptYBDqexxq4nfX1l4uH-A52HEle2rjz873h9-VMrHslmZ3AR6qqK8jfo8KwV_typBbQ-aBOg6-6j1aSlfl1bXIcV_jGIwLqDkpQ35uasHxbsvxUr6D7jGVZlGbQaaAjVaiGtmqASJrVUWhBam60SqKAwBs6UXL8oe5l7eFU9-Cexhk3qDwY9Sc67U3v7RPe4EWm3W2ZfzAPMZvLzimtLiynBm1eWRU4jBmIvhlA5DvRk93nWRoLdjQoDm8--UJxdwkiEhAMOt9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فهرستی از با ارزش‌ترین شرکت‌های هوش‌ مصنوعی دنیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/683183" target="_blank">📅 22:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683182">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29cbf6bd8e.mp4?token=R8B_SMxsFg26fNZ3Z2yTNF_rEWpZ5mFWIS_eG6zgmJztYJXMjCbqMq7jNyW-UAd51VZyVVMMoEN1nJN7oYsy3_tP6Hvy79oNL3W-Xay96r8q7W0pApJUanFFKCbfSfSyIPyOHzELdy0F0j7ahJDAbjvN_-JoYaox8ee4PDuVUZloifiCUukcKik60iHP-ZtYVKSTvi4QH1qPwLACnwOY4Pzv7vR3Ldy_7K03QBWhcpiT_JwGAmowoIPbrESDD2p4b_Q7xa3m_9cfmSdjRBSi-deimm09pIq5Yl8JacJ2ACKa40Ja9EPuxR2i6JJ9m7p37QQe9cwHalDNj0qltfOPlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29cbf6bd8e.mp4?token=R8B_SMxsFg26fNZ3Z2yTNF_rEWpZ5mFWIS_eG6zgmJztYJXMjCbqMq7jNyW-UAd51VZyVVMMoEN1nJN7oYsy3_tP6Hvy79oNL3W-Xay96r8q7W0pApJUanFFKCbfSfSyIPyOHzELdy0F0j7ahJDAbjvN_-JoYaox8ee4PDuVUZloifiCUukcKik60iHP-ZtYVKSTvi4QH1qPwLACnwOY4Pzv7vR3Ldy_7K03QBWhcpiT_JwGAmowoIPbrESDD2p4b_Q7xa3m_9cfmSdjRBSi-deimm09pIq5Yl8JacJ2ACKa40Ja9EPuxR2i6JJ9m7p37QQe9cwHalDNj0qltfOPlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر سابق فرهنگ ترکیه: ایران برادر ماست
تامیک کمال زیبک:
🔹
ایران فقط از آب و خاک خود دفاع نمی‌کند، بلکه به باور او، در خط مقدم مبارزه برای آینده بشریت قرار گرفته است.
🔹
ایران دوست نیست، برادر ماست و شرط انسان بودن در این روزها، حمایت از ایران است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/683182" target="_blank">📅 22:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683181">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4748c9bb82.mp4?token=IOc85Ybl19m2hTXvO6UXJfuFJgDdRcRR8WIj_97678kXhp24Vvl39-rF631hRrisrbXK0WLtt43SZHcGC0gQmfoRKcxpjtlvzf-PTeAGNlh0kR1PBKpM9KfrUrONfL2fgvl9KPKGHsUNNYBFaAIH9hnsP1rCCT8g7QM0ch1mSS_Rpfzg9hO2CzbJzLA0rs4K-wnDEmQUxCzCw-BhlgsENT-tkjqJuVv0CPa9MxP3hIyZPzoplVoyqXb9ZMfPsyH25-9_0RDH_VORUvFwzKURyPt7WjrgxKStmt44-ZQovyoC47_cmdmu74fdnsbtFPqwZmQl3YyAJ5_CGbr1SbfOWyd0Jt0KRs-TyU0_4mCYhBoI9zYKGuWfUHeCL9Jl4aidIBzqSk5BlF45WfPIvGNeSzoE2Ep7cq6qy1BfP_DajS4MqwF3GDht3q83nuDvnEXnxzrc9WEPPvvKdoesL-ONG5KxwZCXMBh1UHo_FUHU0q9mjhSY31FuCW0avJqSARmyLFXtVL0bukW07IgekxXbcrIiP6puNlcW_jXQizLDmIjQshosKo2bjSRDsRzLDZiaH28Z6r9PKplLvFF7OvzPCXf1YcTcsCMqMzBiCeUVCqgmfiRvXcC9ynrbtYJObweVu9rcYHECDOWoBQBBu63dprWmcE-ABmXNgOibDDcA-ho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4748c9bb82.mp4?token=IOc85Ybl19m2hTXvO6UXJfuFJgDdRcRR8WIj_97678kXhp24Vvl39-rF631hRrisrbXK0WLtt43SZHcGC0gQmfoRKcxpjtlvzf-PTeAGNlh0kR1PBKpM9KfrUrONfL2fgvl9KPKGHsUNNYBFaAIH9hnsP1rCCT8g7QM0ch1mSS_Rpfzg9hO2CzbJzLA0rs4K-wnDEmQUxCzCw-BhlgsENT-tkjqJuVv0CPa9MxP3hIyZPzoplVoyqXb9ZMfPsyH25-9_0RDH_VORUvFwzKURyPt7WjrgxKStmt44-ZQovyoC47_cmdmu74fdnsbtFPqwZmQl3YyAJ5_CGbr1SbfOWyd0Jt0KRs-TyU0_4mCYhBoI9zYKGuWfUHeCL9Jl4aidIBzqSk5BlF45WfPIvGNeSzoE2Ep7cq6qy1BfP_DajS4MqwF3GDht3q83nuDvnEXnxzrc9WEPPvvKdoesL-ONG5KxwZCXMBh1UHo_FUHU0q9mjhSY31FuCW0avJqSARmyLFXtVL0bukW07IgekxXbcrIiP6puNlcW_jXQizLDmIjQshosKo2bjSRDsRzLDZiaH28Z6r9PKplLvFF7OvzPCXf1YcTcsCMqMzBiCeUVCqgmfiRvXcC9ynrbtYJObweVu9rcYHECDOWoBQBBu63dprWmcE-ABmXNgOibDDcA-ho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سهم وزارت دفاع در قدرت‌ ملی و قدرت‌ دفاعی کشور چقدر است؟
🔹
راهکارهایی که شهید نصیرزاده برای وزارت دفاع داشت، استمرار دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/683181" target="_blank">📅 22:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683179">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5FcTu9j8_6Gt6z3EbMzMqn_dY3hQqv7eCQNN83OkIRH0P9P4Lj4RfiHqvLb026S7sDUISTIXOC2W_ar7fsBweD_OibJquBFviL9YuMNKLnaiGDNjHvwsidex2I5IXwUl5AsX_khuYhPWhOO76krf508L5aIObR3mzPkANbhonOxV8QQGXS3BtpCLbXefiFT8j03HaXCHhlWay_QN9H_B1z268-UOwxpV-7MK8cLexYRyUR49UGDyT_YlUfvOe6oZFmNAoMYBEFiYDk-i1n5hm07o19P4rC1v_bXJJObLCrn5w3ewCbwn3jcp72JIjS6VyRaSzV4aUDAv1NLRb1wYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‏
ایلان ماسک: رسیدن بدهی آمریکا به ۵۰ تریلیون دلار برای کشور بحران ایجاد خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/683179" target="_blank">📅 22:40 · 30 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

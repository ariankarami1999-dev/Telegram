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
<img src="https://cdn4.telesco.pe/file/XPfkhj0kr-pFMsqxHFhiW86i4nohER_4qs0rNvfIfJ7Y4uODZc0h_JfhFCDWGWliVyohipV4gQT-srIpscBC3juU5lMpEVvgara4x0kxuaYMge6VZQduQ1afOjdL1H3EyoF-K3eqlDjv9QtNmLIQ37t1pl_AAyazE-63qQ-8NKMhpmoCKXKCFRPRI9EFRoF8R9KJb9o8PFTQavLRX9qDns0SP9P-tYA4-12hOo83P5rVQP-1ezg3ewjsKBMUKtpP-m-ATvg1vlRwvQOaNW7C5g7EjYy88upx5hu18ekpPfdE4wfXljXWjW6dFxEnHvrzQW8T3mZ2SS6TAalnmz2bqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 20:32:49</div>
<hr>

<div class="tg-post" id="msg-684020">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmszuJ1fZSLtEJAlZYuvuMftDk4hlSaVLtYwwPuaSqRrGNMFgEiDQveYuk8RX1MDiKVmufodoIO34nCF4xAfGr7lh2qlAhP8Ml6WK9fTjcCQ5h0QIjDc3PXeQM8uRcIAq3MbXy1vFEPRAA68IZCQKiNIyE7x2n8A9L9BES-CuxuJkPb2JYy1JBPpoYfWL4ll9ZUDarDRyGROSrpRgBxXiH80nAnssiBwnc98_XG7En4uIRfCQ7XmLj3XhZR4ctF1G21yZe9fmHTsesVcdXoOxGVrWIpd0-UgXP7YWh-qxgkaGnG7GOel-nJtrqR3lKW8VQ7ZG7_XuK9yxR7qNFotEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: کسی گُنده‌لافی‌های آمریکایی‌ها را باور نمی‌کند/ شرکای تجاری ایران به ما پیام داده‌اند که تهدیدهای آمریکا را به هیچ جا حساب نمی‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/akhbarefori/684020" target="_blank">📅 20:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684019">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40949b4013.mp4?token=ZeEekAlqMZ6VwCjLctWzuDU5Bfh0K8ANvJTmNx0hmdmlAFanFQh1gCE2RQWz0IJsW9yohQfqUgnwox_cAl9yrD9iw35H_rW2v1ReWhJ4NJd2gNE6P5ppK-ya2LNfMje7q0wjmC6hAh2NZ0DKEgW8xqGIuA9t1TExdnUPXnyULMejuFX8FfB1b7JGoXqrwmbX5TinoiENu9coqsCUfab1rsCFJE8rSE4yAoFEByQd0MlbQO_b5-Nm_bp3z5xgPX9kV245oQV85llZbRNb0aJdD24C1SBNxwMvokC4AE1_tAp3gVRl0Q62Xd3d4vXhIwJwTWLG4GqB_OF4GTB8h6AKJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40949b4013.mp4?token=ZeEekAlqMZ6VwCjLctWzuDU5Bfh0K8ANvJTmNx0hmdmlAFanFQh1gCE2RQWz0IJsW9yohQfqUgnwox_cAl9yrD9iw35H_rW2v1ReWhJ4NJd2gNE6P5ppK-ya2LNfMje7q0wjmC6hAh2NZ0DKEgW8xqGIuA9t1TExdnUPXnyULMejuFX8FfB1b7JGoXqrwmbX5TinoiENu9coqsCUfab1rsCFJE8rSE4yAoFEByQd0MlbQO_b5-Nm_bp3z5xgPX9kV245oQV85llZbRNb0aJdD24C1SBNxwMvokC4AE1_tAp3gVRl0Q62Xd3d4vXhIwJwTWLG4GqB_OF4GTB8h6AKJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با یک ترفند ساده میتونی شارژت رو درست کنی #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/684019" target="_blank">📅 20:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684018">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb175d00c.mp4?token=i9Ws1SW6fFa4VdvgXMlJKYH4WBxlnXOIwlzgCUf0T-lzUBTriJK52BTdUcXWFm9up3zqHVK2bzjZCtMVrR9F8JChFjA6iupEJBwPe4R6w49e_Ih6RgHQbUlipIbhP5ytZWAWZeT5EGezHjZG9KJL1Saj_4Dp60ZZOt8YBmMSzxJgfQY9o42RpSVob93Sn8MCRQdasa-PnACiCBQJ7Tt6Hep-x_UsoE6I4ExDuJS1MhRuk7b72DVa_o_hrUrbCPuMO1HAOe1F3ZVS-blfGhNnafHGKS-qI4MPqmjJS4YKir3R1FmqomjYG2qMGWRB8rxL7L6IQfw8wxLhNFBgOVwdIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb175d00c.mp4?token=i9Ws1SW6fFa4VdvgXMlJKYH4WBxlnXOIwlzgCUf0T-lzUBTriJK52BTdUcXWFm9up3zqHVK2bzjZCtMVrR9F8JChFjA6iupEJBwPe4R6w49e_Ih6RgHQbUlipIbhP5ytZWAWZeT5EGezHjZG9KJL1Saj_4Dp60ZZOt8YBmMSzxJgfQY9o42RpSVob93Sn8MCRQdasa-PnACiCBQJ7Tt6Hep-x_UsoE6I4ExDuJS1MhRuk7b72DVa_o_hrUrbCPuMO1HAOe1F3ZVS-blfGhNnafHGKS-qI4MPqmjJS4YKir3R1FmqomjYG2qMGWRB8rxL7L6IQfw8wxLhNFBgOVwdIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عادتی که باعث می‌شود شما پولدار نشوید!
🔹
یک دام ذهنی ممکن است شما را سال‌ها بدون اینکه متوجه شوید گرفتار کرده باشد.
🔹
بعضی‌ها فکر می‌کنند پولدار نشدن نتیجه درآمد کم است؛ اما گاهی مشکل جای دیگری پنهان شده.
🔹
این ویدئو را ببینید چون باور داریم که حتما کمک‌تان خواهد کرد!
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/684018" target="_blank">📅 20:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684016">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">03 Ane Manaee (1403-07-26) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/684016" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه سوم
حجت‌الاسلام امینی‌خواه:
🔹
شهید ۲۱ ساله؛ پرواز عارفانه به سوی حق [2:22]
🔹
سیر و سلوک در عصر شتاب؛ شهادت، میانبر راه آسمان [3:59]
🔹
جهاد؛ عرفان عملی در میدان نبرد [5:33]
🔹
کافران؛ بازیگران نقشی شکست‌خورده [9:20]
🔹
چرا مؤمنان در دنیا و آخرت پیروزند؟ [12:41]
🔹
قرآن؛ چراغ راه مؤمنان در فتنه‌ها [15:16]
🔹
آزمون صبر: تا کجا باید منتظر ماند؟ [23:41]
🔹
حکمت‌های الهی در مسیر آزمون و اعطا [31:33]
🔹
فتح پس از مقاومت: مسیری روشن به سوی آینده‌ای بهتر [34:21]
🔹
خداوند انتقام گیرنده: وعده پیروزی بر ظالمان [38:28]
🔹
وقتی ملائک، سرباز شهید سیدحسن نصرالله می‌شوند [49:52]
🔹
صدای حق در برابر باطل: داستان شهید آرمان و ایستادگی او [50:26]
🔹
مکر الهی: فیلم‌هایی که پرده از جنایت‌ها برمی‌دارد [53:23]
🔹
از کوچه پس کوچه‌های محله تا کتابخانه‌های جهانی: سفر کتاب سلام‌ بر‌ ابراهیم [58:08]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/684016" target="_blank">📅 20:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684015">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqA6Y5Y0ZqamT2ihaXtpd6RecqfMqFAHlQmeqjBnFknksovDKx9ERDZj_7P76pYzD2YTy_cm6fI1Kjk7M3jdhcClnDSEx6iKJVzzxyI2YCGWWARMxscZrBkHsjCcS1NlAWqdkt6GMmjj7Jadh0q3R6EzAgG1kFwfkrLj4Gg_t5fZVuraaAIlmKVrldDjnzkTPCXT3zWqJkZrDxAUUXMJOLD4HrOjUmRVi04XRGfCC8X_1mI-45ajews3NPh4lGkZio8OrUDf_XhHIALVAOwIJ0KanjWh1lmF1nC0k0_jGSGGFSRdWPQUr3kkIhwR5-gH0oXFtPEHQ5wrS6MsDiq_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلفن ابری فونیک، بدون دردسرهای راه اندازی
برای راه‌اندازی تلفن شرکت لازم نیست سرور و تجهیزات بخرید یا متخصص VoIP داشته باشید.
✓ بدون خرید تجهیزات
✓ ضبط و گزارش‌گیری تماس‌ها
✓ تلفن گویا (IVR) و صف تماس
✓ بدون نیاز به زیرساخت پیچیده
✓ مناسب تیم‌های دورکار و چندمکانه
✓ مدیریت ساده‌تر تماس‌های پرتعداد مشتریان
تلفن کسب و کارتان را هرجا که هستید همراه خودتان داشته باشید.
🎁
تست رایگان ۲۴ ساعته فونیک
https://isp.abrenik.com/fonik</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/akhbarefori/684015" target="_blank">📅 20:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684014">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای جدید نتانیاهو: ایران قصد ترور یکی از اعضای خانواده‌ام را داشت
🔹
بنیامین نتانیاهو، نخست‌وزیر درمانده رژیم صهیونیستی، در چرخشی تازه برای فرار از بحران‌های داخلی و شکست‌های پی‌درپی میدانی، مدعی شد که ایران برای ترور یکی از فرزندان او برنامه‌ریزی کرده بود.
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/684014" target="_blank">📅 20:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684013">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfe1319de9.mp4?token=ARVlJ7tDLH2ZmZ-5t3aYzKNSN-o5_VMxdGUF3YBr8b2EdcTl1Hfy5yKVdE6Y8T-fv4FYfGRP_NylLllItFkjeaTqWZWLQ1lSdKsM6YKLh_twahIfXpRx7V8XDytIzrqsvaOqEkyZZY9bANHdMG_nLplqGemp_b1aFCKywhQgOMfczxg54qq8zeXxtQpt2SjbxG2DqHeaduLob5_SgsDjgoLCCWa3ZqYpPcWSPqQCCH1GptPTPuprJhpLqPcYuir_F8azvqdWoW89UzFlXMTBWfGtZqKTlaJOM3ScWJhoZJkMMoiDQT10F2WEvkUE-Zond6iu1e09F7gVXkHGD0i617RZcy4_U1HOLOsoufEkJ5fRPkDUPzGvpBv8abLqG75IAxW0Ej7nJacmFXAHaC1BxjYl4_WI6SID23TxnFWtfSNV5K5aaUNT6mS76YatjCs-zOx9VrnvacNRUW6SI7uUHCwFeOw4W0gZesAeaU4RBqOLIqLnYwSjZ6nXqY5BBkJnlMM9SSHZklAqJumGPTzm3PSYhw-UaVNh3Tww-9VhhTdcrIS_TpRx8BIwA5i77dtaNqVYRsC9Orx_GRqu5y2xMEaCUTsooTxzcVz_ptraGnvLgxLNCkcc_UlPMuSsN6I9QSYTZfxG8VI8AftWUDU8hU5dOqX_BS_xrpnRNoIctRo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfe1319de9.mp4?token=ARVlJ7tDLH2ZmZ-5t3aYzKNSN-o5_VMxdGUF3YBr8b2EdcTl1Hfy5yKVdE6Y8T-fv4FYfGRP_NylLllItFkjeaTqWZWLQ1lSdKsM6YKLh_twahIfXpRx7V8XDytIzrqsvaOqEkyZZY9bANHdMG_nLplqGemp_b1aFCKywhQgOMfczxg54qq8zeXxtQpt2SjbxG2DqHeaduLob5_SgsDjgoLCCWa3ZqYpPcWSPqQCCH1GptPTPuprJhpLqPcYuir_F8azvqdWoW89UzFlXMTBWfGtZqKTlaJOM3ScWJhoZJkMMoiDQT10F2WEvkUE-Zond6iu1e09F7gVXkHGD0i617RZcy4_U1HOLOsoufEkJ5fRPkDUPzGvpBv8abLqG75IAxW0Ej7nJacmFXAHaC1BxjYl4_WI6SID23TxnFWtfSNV5K5aaUNT6mS76YatjCs-zOx9VrnvacNRUW6SI7uUHCwFeOw4W0gZesAeaU4RBqOLIqLnYwSjZ6nXqY5BBkJnlMM9SSHZklAqJumGPTzm3PSYhw-UaVNh3Tww-9VhhTdcrIS_TpRx8BIwA5i77dtaNqVYRsC9Orx_GRqu5y2xMEaCUTsooTxzcVz_ptraGnvLgxLNCkcc_UlPMuSsN6I9QSYTZfxG8VI8AftWUDU8hU5dOqX_BS_xrpnRNoIctRo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جهانگیر الماسی: پول غذا ندارم؛ هفته ۴ بار غذا می‌خورم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/akhbarefori/684013" target="_blank">📅 19:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684012">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFu7VFiyLnMOJ6H3gdCOoBe52MOuezutlwS9aukLfMXBFUlz2dA7uTc5wB3vsFP87k1W8o-1PXoy7jkbzDFvUIT1ZGzMYb2XK_tbnXbM8H8akK8ngyzoI64UHpIjYJEWvPvcyySD_YH__bU5OiQ02Blom9Xw71ZDJgNZDR7ucE5u53TEFDFkbTvUpoBA94NDLNGVN8NHgrL3msaP8a10GJyARDB1-R487QR2vEkR_CQJ5aE_Z4ckuQAHdzJcldRR1sbricZUabPUI68bOohxoHSUMprP9iAwY2gbEbW7_F8Nyc1EIRhleokPIt3ObwDnTGHv8r8mgph15CY7x6gTzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت کودک فلسطینی در حمله صهیونیست‌ها به غزه
🔹
در ادامه کارزار سیستماتیک نسل‌کشی و کودک‌کشی ارتش رژیم صهیونیستی در نوار غزه، حملات هوایی جدید به «دیرالبلح» جان یک کودک بی‌دفاع دیگر را گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/akhbarefori/684012" target="_blank">📅 19:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684011">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
فرار رو به جلوی ترامپ: دموکرات‌های افراطی نظرسنجی‌های دروغ منتشر می‌کنند تا ما را قبل از انتخابات دلسرد کنند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/684011" target="_blank">📅 19:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684010">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGvgNpG1mrxjf_QEFz1qMBZJAqWLiDTOhmDQRHpcFeLJgbajTNLdkhTCkDapEUrenwJoNiwJ_qcr4B0tGS5lV-URGbQ7x3Q5QlUHYAGht2JMoNSDEKDUVezX9j3H6We_BDAkvgpnwmYjI4sCsAsK_Jpugcg_ykExGFxIIfqvVcyiCeANB4RawFgJzpGcQgls2zoQNLxQj9VPICBJHXoUGZY5af6WnPB6O1FrrzWF1y7DFV4v4MKQS6Mbw0VGOLzFJVN22yemzQmDANOex3ucxfPMDbKVQnripMGx-wUFjJqaj1tgllKrzW4Xv2qleaPVQpxXlNpKDHg1PrNaZu4QRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاهای خسته‌ای که جای چرخ موتور را می‌گیرند/ «پیک پیاده»؛ فرزند جدید فقر و فشار اقتصادی
🔹
در پیاده روهای کلانشهرها افرادی را می بینیم که کیسه هایی به دست دارند و می آیند و می روند. برخی از این افراد، خرید کرده اند اما بعضی دیگر پیک هستند. شاید تعجب کنید اما چند سالی است که «پیک های غیرموتوری» در بازار رواج یافته اند؛ افرادی که موتور و ماشین ندارند و بسته ها را با پای پیاده یا از طریق مترو و اتوبوس جابه جا می کنند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3239896</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/684010" target="_blank">📅 19:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684009">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
۱۳ درصد تورم ایران به خاطر مسکن است!
🔹
یک عدد در اقتصاد ایران به‌سادگی قابل چشم‌پوشی نیست، حدود ۱۳ درصد از تورم کل، مستقیماً به بخش مسکن مربوط می‌شود.
🔹
این سهم طی سه سال اخیر تقریباً ثابت مانده، چون قیمت مسکن به‌عنوان دارایی سریع‌تر از اجاره رشد کرده و همین موضوع باعث شده این بخش در برابر کاهش تورم مقاومت کند.
🔹
مسکن همچنان یکی از سرسخت‌ترین موانع کاهش تورم باقی می‌ماند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/684009" target="_blank">📅 19:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684007">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcuQVYl0RMcyOqTjFiQdUWEV0Gb1khDqPYLp6ZUwQbO7dZ5BzfbOCzhPak_3_inNI7JMl28GGS9-eZzbLX_Hv8pHsamgyLIKwnO1nmJ_o_jmh6rpl_1P_rlCwCUkjOuW25GldXUrA-LqaBw_SieWSXmolr6INCE1k6H5H2Wz1abe850Sr0XWAZ-KJ626mHgNzkCfjWcnbjYkxmBqzCcRtgpiTCXsMibUkzRmAEbVf1Xl1frWFwlSRSa0DeY3UwwwIdTQg4aPDuW0jFnGYnUNqqNyR4GQbFQPZcmMyy3_rmVRfqW4UUu8Ut1V59Lfj2sTgjsP_cuaeWHXLB-ul9aguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jbhiu3gmXNxU_LMRz8DrvVH3mw_Vrca3vu1Gi6BqCzA5pD8ZKNBX7ZowS9K6CKt0DYl_iWTYzgKQnJALXHGQyxh-BxEjtkrDnSnzrxG-tu_OLElEnHEPaxoZeW8QJENIs1v0cQWiNOresCk-Yxl4z7U_CXBnr-X5scC6qHV_pSKlm9l0DhinMOPTMaMTT9BWxg6633H1wAL58jMSeqapxht1Owo5ms5Pbq5DSGe8wf5xpn-NKzvOQfOTdIaxNhszJxDNfoyas50wFbLL5e4w_2xNCPUbfeD756KaGRVDhCJ8xQUH2zP_0MOGWgWiZuQGHlKK_Gc59eEUBPOKbUSpdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ورود فرمانده ارتش پاکستان به تهران
🔹
عاصم منیر فرمانده ارتش پاکستان دقایقی پیش برای دیدار و گفتگو با مقامات کشورمان وارد تهران شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/684007" target="_blank">📅 19:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684006">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aScJzd2zBrnalLnyjxrqpZN2ljz0VMlIVcU9kqNOCk31UXbaL8MxhUYEQDbvHRORzU4DM_Zy05rOnr-EhB1wiVQ4zGdAeCxKtLvDaOpgLTSkDGRN3h2elTV__2jMZmkUK8OA5i0qkVE8q24UFF9xCxOG_LNI8YnkzZ9vQEYwf1EN1HZs1T_yCHeYuppU4HVpeqzaIU4sGVrRKSZJZZnY7sDuXmVLLXFhws7ROrq0dn6yFKOmwfd72hqQ9e_NFXRDAX15Atrrp3zL_keDPeywS_XHcwX4ygG-ymcxBLkDNKySzwzhAek5JS2gPgBrp3vt_TqGXJ1G0yE_Nh3EtefDMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دو دو بازار
🔹
بازار امروز در ادامه روند رو به رشد خود قیمت‌های جدیدی را ثبت کرد. دلار در بازار آزاد به ۲۰۲ هزار تومان رسید، طلای ۱۸ عیار از مرز ۲۲ میلیون تومان عبور کرد و سکه امامی هم فراتر از ۲۲۰ میلیون تومان رفت. با این حال همتی رئیس کل بانک مرکزی در واکنش به این گرانی‌ها گفت که بالا رفتن قیمت‌ها در بازار ارز براساس هجمه‌های تبلیغاتی و جوسازی آمریکایی‌هاست و در روزهای آینده قیمت پایین خواهد آمد.
🔹
هشتصدوچهل‌ودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/684006" target="_blank">📅 19:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684005">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGLNvUTrJBl6HC80-YAUMqtFIQ8qXpbjgqrMaGrjVydi9RxOusubm-NiAY9rftfWXaubi7tXO_gCDn-o6LQlgCB8glKVSE9d4PfnmHlJUsN36lHs6THNwQ-54kp94t_jzI4ZXE0_8uXzJ85m6ZsEiw0vf4snymDCI19s7zWqq2szwEVgYM7LwUJCjvzABMQvyvvRBWa2fTEt2T9N2soa2WJYBLnAaLJW1OtsTALRsBb2X24lFtE3J_hLkNcIQVzfEW4gbeyjDGJ_BjzCJHVA2cmKmsoeyVi_48KG_XzF9rGR_fFIxJyJsbcK4Mm1Nhgdgv8w8FXVulKXyym1ohQslA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: بگذارید ایران تنگه هرمز را کنترل کند
نیویورک تایمز:
🔹
جنگ با ایران دو چیز را آشکار کرده است، ایران نمی‌تواند تنگه هرمز را به طور کامل ببندد و آمریکا نمی‌تواند آن را به طور کامل باز کند.
🔹
ترامپ باید با واقعیت روبرو شود تنگه باید بازگشایی شود، حتی اگر این به معنای دریافت عوارض از سوی ایران برای عبور و مرور از آن باشد.
🔹
این نتیجه برای آمریکا یک شکست خواهد بود. اما در حال حاضر، این گزینه کم ضررترین گزینه است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/684005" target="_blank">📅 19:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684004">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
الجزیره به نقل از منابع آگاه: ترامپ هفته گذشته با فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان، تماس تلفنی برقرار کرد
🔹
ترامپ در گفت‌وگو با فیلد مارشال منیر درباره موضوع ایران رایزنی کرد و از او خواست از نفوذ پاکستان برای ازسرگیری مذاکرات استفاده کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/684004" target="_blank">📅 19:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684003">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b94af2eb.mp4?token=r1fdJxx8ES4ailODJgVIcNcpl6n7mJr2R7_WXcyk1nvQIpyKZjPAkw20HdhV_dEIR5Xri1vpHi1u5wZWuYnVD_YBcrfFJ7kO33ntgdFwVyA2B8bXPP05s7ByU4heE5VXVuH8QTQy_ai--tyK_Orr5GIGC595-D_Y0TUxk5jQOabBnQAoul6ejyKF19dx1G7nLdU0IUapKU6fqWGpxv7Vq-q3z0SyBZx0CM_sgSayp1DMJatOwNudx69QlfYRsczpx3k1IOvCq9_Tb0vgStbSLJN2a0xy9TZwF4HcnWSJXtlzVpzjycnNBrIivCjrBcnqFnzSvyF6foSen7ymV9V_fEnlejkLet5B_v8ZyASyaIbGHI1BQp5PGD_YaUdU4C6pBNxc2HuUC2QKSvTCTbghYh4B2yrVB-54kOkxjtGOHMyTLwuT325OFWgvBA2TEnlwCE5arC9LwdrB1rM7GrN79iBLWosSrPUPOmE7I_SsXWlgHYeJ2OBFFgqlWVais7RcNVjTrw28iDGY5plcylsYJe9DLLV-r7TaQW3I_Uq1r0EJyDUOkWCoLA1ZDIqMUHCF37K6FLKy0Ae5aKGcqUlyogDKwzIv34gl3yMcgAlhXdBoHU9EmVA-flQ4jHBUF1_H56EfrLBwOhkIq4PgBKxSWQYzHAqHG0XILWz4sL7wIVM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b94af2eb.mp4?token=r1fdJxx8ES4ailODJgVIcNcpl6n7mJr2R7_WXcyk1nvQIpyKZjPAkw20HdhV_dEIR5Xri1vpHi1u5wZWuYnVD_YBcrfFJ7kO33ntgdFwVyA2B8bXPP05s7ByU4heE5VXVuH8QTQy_ai--tyK_Orr5GIGC595-D_Y0TUxk5jQOabBnQAoul6ejyKF19dx1G7nLdU0IUapKU6fqWGpxv7Vq-q3z0SyBZx0CM_sgSayp1DMJatOwNudx69QlfYRsczpx3k1IOvCq9_Tb0vgStbSLJN2a0xy9TZwF4HcnWSJXtlzVpzjycnNBrIivCjrBcnqFnzSvyF6foSen7ymV9V_fEnlejkLet5B_v8ZyASyaIbGHI1BQp5PGD_YaUdU4C6pBNxc2HuUC2QKSvTCTbghYh4B2yrVB-54kOkxjtGOHMyTLwuT325OFWgvBA2TEnlwCE5arC9LwdrB1rM7GrN79iBLWosSrPUPOmE7I_SsXWlgHYeJ2OBFFgqlWVais7RcNVjTrw28iDGY5plcylsYJe9DLLV-r7TaQW3I_Uq1r0EJyDUOkWCoLA1ZDIqMUHCF37K6FLKy0Ae5aKGcqUlyogDKwzIv34gl3yMcgAlhXdBoHU9EmVA-flQ4jHBUF1_H56EfrLBwOhkIq4PgBKxSWQYzHAqHG0XILWz4sL7wIVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متشکریم به وقت ایران!
🇮🇷
🔹
تشکر متفاوت لگویی‌ها از عوامل «به وقت ایران»</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/684003" target="_blank">📅 19:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684002">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFqlHKLUtKjb87ZiPgAsUkrzmZRLZ5tXSDzydoY7k6Ge0hX3VTNjZfcTa2IQjtHeQuG2Ind94wzbcR42DJTpBq-gk2enDAJ2KC_VBJisGL9Gk0n4V_3qVi451WbfCIBFvb_InfdkvE_ja2H_RfTO30b6VqwyKze8uw5yiFSHc_IvCK_ttui4BEeFJmzyzxjtONM8NN8L9dX8pbEdhFhuwFO6FRH4dUWrjizYw_SQsiya7v87Gic6QQkyMhVZQ5eYg0UTq06v_6NP7Jp3O6vRkSQiUsxq3zFgINdAoUFQoxLCjfMOo-ikb7CCkjfOxKkHacMep6GY9RwxYxjNvskseA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطع برق در کمیسیون انرژی مجلس
🔹
کمیسیون انرژی مجلس تشکیل جلسه داده بودند تا علل قطع برق را بررسی کنند، که برق در همان زمان قطع شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/684002" target="_blank">📅 19:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684001">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/367508c21f.mp4?token=S8Bau3DkRBZxWO6QczQgmMsQtkghBPPl7KrjK7f_zstYQl3R_CIdu0nf8yMo6MLKsUJlNxfMYebOZc10drOSHCNsbvyIDvXZLYozDpuTKHG6meaCdgqcUipiMOQT5b0qplbQQIBG6oOT3WVYFuh5j38slJ0x5u8AxyoT4oBngfTCLyNQYkr-kqweiQJAFrtT89xp6t_CRi3Mm0YYXuBOE2sTVJGlvTHWZ0RWEpy7FG8EoZxELZfdA6Kx3dpGRW19oLk73CyUKRWsijl1uQ8DKtg1Yc_fJ_Gm2D0uyptDROcDr94aItIe-lji6mygi8Z9aBdhckBbH7GP0oPhb7SzyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/367508c21f.mp4?token=S8Bau3DkRBZxWO6QczQgmMsQtkghBPPl7KrjK7f_zstYQl3R_CIdu0nf8yMo6MLKsUJlNxfMYebOZc10drOSHCNsbvyIDvXZLYozDpuTKHG6meaCdgqcUipiMOQT5b0qplbQQIBG6oOT3WVYFuh5j38slJ0x5u8AxyoT4oBngfTCLyNQYkr-kqweiQJAFrtT89xp6t_CRi3Mm0YYXuBOE2sTVJGlvTHWZ0RWEpy7FG8EoZxELZfdA6Kx3dpGRW19oLk73CyUKRWsijl1uQ8DKtg1Yc_fJ_Gm2D0uyptDROcDr94aItIe-lji6mygi8Z9aBdhckBbH7GP0oPhb7SzyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام گلپایگانی: همسرم به معنای واقعی ام ابیهای پدر بود
همسر شهیده «بشری خامنه‌ای»:
🔹
بنده با همسر شهیدم ۲۶ سال زندگی کردم. به دلیل برخی مسایل ۱۱ سال آن را در جوار رهبر شهید انقلاب زندگی کردیم.
🔹
سیده بشری خامنه‌ای به دلیل رهبر شهید از بسیاری از وابستگی‌های خود عبور کرد.
🔹
او در کنار کارهای خانواده، کارهای رهبر شهید را پیگیری می‌کرد و مقید بود آقا هرگز تنها نباشند. به معنی واقعی ام ابیهای پدر بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/684001" target="_blank">📅 19:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684000">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9cIJJA2aJdHYqDr9xxRHT6s08gtFx2R99IgWOhDoV-HmwsNgIdeZ5ps-vhjQTeSRJTIojSnCYhYOeUni-tRvlStreBtqmagwcj5f2u9jgcmdtIGgJLsBXsfCUoLvInyTJ50PVfsDdHh9ZfAc1DF6bJtpLCjHPWl18iA46qTtd1guhV0JBerMItDsqNhGDzjhzX9ouJ8bZlBsh9ZxhnuvSi0oVbChrB9NOs-JxiAH6me78_3Tymlr11JVpoN8lOT1VkqDYHsrLvRveejIRTbGqOkjJ9uWKbSzpYGcfvmAfXr3Fkw84ILBZUDf6SS885lYR5xh6zIDNqHlBerboh38Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا: کشورهایی که سرنوشت خود را به تهران گره می‌زنند، با مسدود شدن تمامی مسیرهای دستیابی به رفاه پایدار روبرو خواهند شد ‎ ‏
🔹
هر کشوری که به عنوان شریان مالی برای نظامی در آستانه فروپاشی عمل کند، باید انتظار داشته باشد که در انزوای آن نظام…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/684000" target="_blank">📅 19:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683999">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کوثری: با برنامه‌ریزی تنگه هرمز را کنترل می‌کنیم
کوثری، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری :
🔹
آمریکایی‌ها به هیچ وجه فکر نمی‌کردند که گرفتار بسته شدن تنگه هرمز شوند.در حال حاضر با مدیریت و برنامه‌ریزی، تنگه هرمز را کنترل می‌کنیم.
🔹
ما ۴۸ سال است که با محاصره اقتصادی و تحریم، کشور را اداره می‌کنیم و همه دنیا پیشرفت‌های ما را دیدند و اگر پیشرفت‌ها نبودند، الان جمهوری اسلامی هم نبود.
🔹
آمریکایی‌ها بدانند با این محاصره اقتصادی، ضربات سنگین‌تری خواهند خورد.
🔹
سیاستمداران برجسته آمریکا دائما به رئیس‌جمهور قماربازشان تذکر می‌دهند که از روی نادانی، ملت آمریکا را دچار مشکل کرده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/683999" target="_blank">📅 18:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683998">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYHaJQ6UI42Fhdz4MkLpIsGuQ7lUpIQbUn0t-WNy_QPEf7f8Q7kIletgVe9EcGYPjT3q1G9BZdofcJNUpC5sdU-NkRJCgr3689Zj4YW4NN7afTjc7mokIEneuxUxAZWLZW7uSLEUjMb9tJAF61FkA5jW9yiVNJaFBGlUlXjihYcPunUWfEqheGwxnSnb6vO71CNBrUB0I3y4ZljWgx8VU1PKKlhLIMtpZjVD9bv4JIjgjRGz0aSSwWeCPnuq-8hO711nXZd5aWZwJ-I9K3-MtV5Qb9ysfmSbzFKWxRhy2RPBeuWfhgNWKOwO-b3wSbvT0ThioWS1G37nV5jRv4KkiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ مدل قهوه سرد محبوب که می‌توانید در خانه درست کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/683998" target="_blank">📅 18:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683997">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7iVYNVaTe2iWQDAUDIT-AwEy1HAQLA6nBJL0opIr54qeG9K85MSadAVcMIBQuJVY69m-SoG7SqUNv2IKqQHz6ToWQq3i0QD3ndUGstULuND5yHOKA92qR_KPnNSW1KUgSwz0lu_5V-b3pBq0fBygy4eemg9O6OkAJylXD5ZMtfy45FYylQUWK3CwBomM2GR2tkYLMJCw0O4Y78UQeA3GAs9Vb4UTdh3XYN6TXMFqU-dMJ6OCs39aoa69N5P5x-ng5T5WJmgQMM47Kwlsre2WhzvmF_Xcn6mob6kht4CXHraWPcELitriv45jBgMaQqJu82JIa9PgdFEG_HZydmnpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصفهان؛ آغاز سفرهای هفته دولت با افتتاح ۳۹۰ پروژه ارتباطی
🔹
همزمان با سفر دو روزه ستار هاشمی، وزیر ارتباطات و فناوری اطلاعات و نماینده دولت، ۳۹۰ پروژه ارتباطی و فیبرنوری با سرمایه‌گذاری ۶.۴ همت در استان اصفهان به بهره‌برداری رسید.
🔹
با اجرای این پروژه‌ها، پوشش پرسرعت روستایی به ۸۵ درصد رسید، ۷۳ روستا تحت پوشش قرار گرفت و حدود ۲ هزار نفر به شبکه ملی اطلاعات متصل شدند.
🔹
در این مراسم، تعدادی سایت 5G اپراتورهای ارتباطات سیار و چندین پروژه ارتباطی در شهرها و روستاهای استان نیز به‌صورت برخط افتتاح شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/683997" target="_blank">📅 18:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683996">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyz_H0OoMWUPb0ZDLsNzqvtB9AGbV3mbkOzg_MkW83fWiamstu2itZQ69_y6tzKhpJhbMVaHLMK356KQgNCgl8jSyMhPae0cqdy7NiKwoXCG51mBSQMAomObTngiE5WrgHd5C_usuVVUvlKJ2XSSKYIJ-aJ31gTiaZFZlTBUJw9qznCfDX58ecQ-x-9YZUFeXpqbjNI12G4m-AAoBJp8d-irzG8bFuac6alxzZph3XpIzrtpkUXp5Zmjy8tqjYm-9zPp3a3GEkgsjY-te-EQYGvD9KGiBIccb086ONxgQyjtUfhmU5d_9My1tiMs1VDNi_bnWB8wIShM_3uHP7OiHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکاف جنسیتی امید به زندگی در جهان
🔸
شکاف جنسیتی امید به زندگی به تفاوت طول عمر زنان نسبت به مردان گفته می‌شود و در هر کشوری که این عدد مثبت باشد، یعنی زنان بیشتر از مردان عمر می‌کنند.
🔸
این عدد در کشورهای اروپای شرقی نظیر روسیه به بیش از ۱۰ سال می‌رسد که ناشی از سبک زندگی و حوادث است. در ایران، این اختلاف ۳٫۸ سال به نفع زنان است.
🔸
در مقابل، کمترین شکاف جنسیتی زیر ۲ سال در برخی کشورهای آفریقایی و جنوب آسیا دیده می‌شود که عمدتاً به دلیل چالش‌های سلامت زنان و مرگ‌ومیر مادران است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/683996" target="_blank">📅 18:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683995">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ادعای الشرق الاوسط: عراق مهلت خلع سلاح گروه‌های طرفدار ایران را به تعویق انداخت
ادعای الشرق الاوسط:
🔹
یک مقام ارشد عراقی، مهلت ۳۰سپتامبر برای گروه‌های طرفدار ایران جهت تحویل سلاح‌هایشان را به تعویق انداخت، بدون اینکه توضیحی در مورد این اقدام یا تاریخ جدیدی ارائه دهد.
🔹
عراق تحت فشار آمریکا برای مهار نیروهای طرفدار ایران قرار گرفته است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/683995" target="_blank">📅 18:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683994">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
سخنگوی سپاه: تهدید زیرساخت‌های ایران مساوی است با ضربات سنگین به گلوگاه‌های انرژی و منافع حیاتی آمریکا
سردار محبی:
🔹
برخلاف تصور دشمن که ذخایر تسلیحاتی ایران را محدود می‌پنداشت، تولید موشک‌های هوشمند و هدایت‌پذیر ما استمرار دارد.
🔹
مهم‌ترین دستاورد این جنگ، انتقال آسیب‌پذیری به زیرساخت‌های حیاتی و مراکز وابسته به دشمن بود.
🔹
امروز آمریکا به خوبی درک کرده است که اگر تهدیدات خود را علیه زیرساخت‌های ایران عملیاتی کند، با ضربات سنگین راهبردی در گلوگاه‌های انرژی و منافع حیاتی خود مواجه خواهد شد.
🔹
واقعیتی که موجب شد دشمن در بسیاری از اهداف اعلامی خود، از جمله بازگشایی نمایشی تنگه هرمز، ناکام بماند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/683994" target="_blank">📅 18:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683993">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZopbbwsHGJdcia43Dj8gv7IlBv_SPoOV_iOIT53QGrjnYY8MnEqJXDx9eq2Yyx_rwTuFL2H-A1xfiZpJZXUDqkv0kmzZ5xxIPQURr63T_PqZegxarnReVG_6CSGcOj5qO0zxwxX82VWBxJ9T_SygjRmvPeDY0JR8B4tAzGbq1yYIX3_K0SBHMgLCA1vY4mCzt0jYRXNuIw8tJxEOGVFnV_Tp0ecSL1f522wzE-vX1f7L1DC6Gfj10OOXymLNFIG3esRaCF7QN-f0sMQMYAy-4ESPH9fAGyDzfD3dJIX44O-VPFJZ6CKO0swRnUnfmxkCqvpjr29BMnMTr8kzuKVGPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیلی محکم یمنی‌ها به سعودی؛ نفت‌کش متجاوز در دریای سرخ به آتش کشیده شد   سخنگوی نیروهای مسلح یمن:
🔹
نفت‌کش متعلق به دشمن سعودی با نام «أمزان» در مقابل سواحل «ینبع» با یک فروند موشک بالستیک هدف قرار گرفته است.
🔹
اصابت موشک دقیق و مستقیم بوده و منجر به وقوع…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/683993" target="_blank">📅 18:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683992">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
جزئیات نسخه تازه مصوبه مجلس
🔹
بر اساس ماده‌ی ۱۵، همه‌ی اشخاص حقیقی و حقوقی ۳ ماه فرصت دارند تا فعالیت‌ها، قراردادها و ارتباطات جاری خود با کشورهای خارجی را با سازوکار جدید تطبیق داده و در سامانه شفاف کنند.
🔹
تولید اثر هنری بدون مجوز از نهادهای قانونی کشور،…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/683992" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683991">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb1915b85.mp4?token=B4YnTwhIbKycLklMWJUl0uH4Op1I75crWtHdm_aJg4Cuo6A29BRBJJjBEdC4JuPm7RFeLLmPVtFweqombSWSP-HmLqPQi80Du8M1M0gXYaP4dJybFmnikwa6aWWbRJVRqqpjnEDRSs8ymYSUsIz_iXHGxh_pyT3RWzEM-etFyx0g5EgukuHX1NZJPyhyspvNkdJVM57KL3FTVVE4bbNcGMfV5BlKvo0m0gxZteH3_R7L2vCc-YbiUKV0YyHhJvBZUfI3UyNa9sVSCVJ0eF3-SifJiBjxVqNb_2slwyhHVKjgMwrYk6HK70lX4YT-U8dgt9XReNLoTOqM3eAfiTdnHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb1915b85.mp4?token=B4YnTwhIbKycLklMWJUl0uH4Op1I75crWtHdm_aJg4Cuo6A29BRBJJjBEdC4JuPm7RFeLLmPVtFweqombSWSP-HmLqPQi80Du8M1M0gXYaP4dJybFmnikwa6aWWbRJVRqqpjnEDRSs8ymYSUsIz_iXHGxh_pyT3RWzEM-etFyx0g5EgukuHX1NZJPyhyspvNkdJVM57KL3FTVVE4bbNcGMfV5BlKvo0m0gxZteH3_R7L2vCc-YbiUKV0YyHhJvBZUfI3UyNa9sVSCVJ0eF3-SifJiBjxVqNb_2slwyhHVKjgMwrYk6HK70lX4YT-U8dgt9XReNLoTOqM3eAfiTdnHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وسیع‌ترین کشورهای جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/683991" target="_blank">📅 18:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683990">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/280cc51c55.mp4?token=aklKxO_sGwwHlx_806pHFpDfaU4TbDVvgfb91siFE2OZ9tB9TKJ0ajYNtHHb6c2jeAFtpclv2hoCQPQp1ePv1QYsYU2LZrvZ6NGe23sg-CxwboUoG0GTPwOrneYuKnTvpd2qk-gUF-GHxMa8sZvJmpqvHKKsTebRjz5Cwwfq-ydZvBVmVPdSR8VqGKuNSoc_gsO3Wmd3GmK0mp8mw-mMKSD8uWuTGFd1cAwfpMVpU9CiI1Ow0oO066lj9YPZn80ODowVi8xK29JMfA9dnr4jLOb8B1ir9I_mKYtDwm5dKCl6g1eQsYUHfZc8GlCJNPg4MObgUwQyLaIixRZR2AHbKhJDIfs-6wYjEGGx4H49f0L-pt7MAJGx9YlKAJm1sL1iM7d6AX28xJTBMmcZW9xwnwquq_PAkRWlWGRHiwPLNsAoe9NeePZ1Kp4XKt72Ioxgu8o8QrPjFSvgj-rZDidxMEQLxxtZV842Jr-Z2VzSgzyPJMDz3pf62k21KLs2btnMeqFGfTsTsD6MMAmUcSvVIyh1mq8Af8lLZOD6A57FKPHipRMM5qScaWzyPWqjGVZktECSDTEFydMRNsmnYlsT6iInsvrH7djqkGanU2quX-FwLi1VG9U8fMG1E7S009C_M05VdJDXcMm4UyeueBWGaTlAP8DSYgRIm2DSwvOeGHI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/280cc51c55.mp4?token=aklKxO_sGwwHlx_806pHFpDfaU4TbDVvgfb91siFE2OZ9tB9TKJ0ajYNtHHb6c2jeAFtpclv2hoCQPQp1ePv1QYsYU2LZrvZ6NGe23sg-CxwboUoG0GTPwOrneYuKnTvpd2qk-gUF-GHxMa8sZvJmpqvHKKsTebRjz5Cwwfq-ydZvBVmVPdSR8VqGKuNSoc_gsO3Wmd3GmK0mp8mw-mMKSD8uWuTGFd1cAwfpMVpU9CiI1Ow0oO066lj9YPZn80ODowVi8xK29JMfA9dnr4jLOb8B1ir9I_mKYtDwm5dKCl6g1eQsYUHfZc8GlCJNPg4MObgUwQyLaIixRZR2AHbKhJDIfs-6wYjEGGx4H49f0L-pt7MAJGx9YlKAJm1sL1iM7d6AX28xJTBMmcZW9xwnwquq_PAkRWlWGRHiwPLNsAoe9NeePZ1Kp4XKt72Ioxgu8o8QrPjFSvgj-rZDidxMEQLxxtZV842Jr-Z2VzSgzyPJMDz3pf62k21KLs2btnMeqFGfTsTsD6MMAmUcSvVIyh1mq8Af8lLZOD6A57FKPHipRMM5qScaWzyPWqjGVZktECSDTEFydMRNsmnYlsT6iInsvrH7djqkGanU2quX-FwLi1VG9U8fMG1E7S009C_M05VdJDXcMm4UyeueBWGaTlAP8DSYgRIm2DSwvOeGHI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لقب متفاوت مجری شبکه سه برای محسن رضایی؛ «سرلشکر فیلدمارشال»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/683990" target="_blank">📅 18:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683989">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3296509c0.mp4?token=Lb09gPQKWcPuIVGNqn854HXY9960l2BGYwtGmDqN-d7zFCYTifqq6QPffhuCCbSH0Kq3mt3UbMyyPNRiy9m3kUAihcCx4AOiXv66aApE_xZcpi5OOAgjDbv7SUVJSjcDWX_RORWllC1Le1V03q0ymTAW-Za4CqZty2TNTWuIpWREI0KAXHwW5Ems1vVwbY_oxP_1Rn009JE0g23pg6cqhAf_8nGaGrYAx_4HMHwiYGo_DqiXzdGhykiJNNb2n2d5tBzB8r2b7xtXwqvYy-d6-9MHSwsPlYEpulfBOAtTj1Ie1tl1bngMKV8TXRtd3q7jg5-GFYYh_ugMvM__oI9CD4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3296509c0.mp4?token=Lb09gPQKWcPuIVGNqn854HXY9960l2BGYwtGmDqN-d7zFCYTifqq6QPffhuCCbSH0Kq3mt3UbMyyPNRiy9m3kUAihcCx4AOiXv66aApE_xZcpi5OOAgjDbv7SUVJSjcDWX_RORWllC1Le1V03q0ymTAW-Za4CqZty2TNTWuIpWREI0KAXHwW5Ems1vVwbY_oxP_1Rn009JE0g23pg6cqhAf_8nGaGrYAx_4HMHwiYGo_DqiXzdGhykiJNNb2n2d5tBzB8r2b7xtXwqvYy-d6-9MHSwsPlYEpulfBOAtTj1Ie1tl1bngMKV8TXRtd3q7jg5-GFYYh_ugMvM__oI9CD4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳۰ تا رنگ کاربردی به انگلیسی رو خیلی ساده و راحت یاد بگیر #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/683989" target="_blank">📅 18:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683988">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌
♦️
حملۀ موشکی یمن به تجمع نیروهای سعودی  نیروهای مسلح یمن:
🔹
در حمله به تجمع نیروهای سعودی و یک کاروان حامل تجهیزات نظامی، بیش از ۱۰ کامیون حامل سلاح که از خاک عربستان وارد یمن شده بود، هدف قرار گرفته و منهدم شده است.
🔹
همچنین چند تجمع نیروهای سعودی در منطقه…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/683988" target="_blank">📅 17:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683987">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مخبر، دستیار رهبر انقلاب: مسئولان نظام برای احقاق منافع کشور هیچ اختلافی ندارند
.
🔹
رئیس شورای عالی قضایی عراق فردا به تهران سفر می‌کند.
🔹
رئیس‌جمهور چین خواستار تشکیل کشور مستقل فلسطین شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/683987" target="_blank">📅 17:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683986">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarmaye Bank | بانک سرمایه</strong></div>
<div class="tg-text">⭕️
💰
📣
✨
نسیم سرمایه
۳۰۰ میلیون تومان وام قرض‌الحسنه
با کارمزد ۴ درصد
‼️
📅
حداقل مدت میانگین حساب یک ماه و بازپرداخت ۳ تا ۶۰ ماه
🤩
🧮
لینک محاسبه مبلغ وام و اقساط
📱
لینک افتتاح حساب از طریق اپلیکیشن سرمایه
🔷
اطلاعات بیشتر
‼️
وفق ضوابط چنانچه حائز شرایط ­باشید
تا یک میلیارد ریال بدون ضامن،
تسهیلات دریافت نمایید.
#تسهیلات
#تسهیلات_بانکی
📞
با ما در ارتباط باشید: ۴۳۷۳-۰۲۱
#بانک_خوب_سرمایه_است
🔽
بانک سرمایه را در شبکه های اجتماعی دنبال کنید:
📲
اینستاگرام
📱
تلگرام
👨‍💻
وبسایت
📲
بله
📲
ایتا
📲
روبیکا
💖
آپارات
📲
سروش</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/683986" target="_blank">📅 17:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683985">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
سیلی محکم یمنی‌ها به سعودی؛ نفت‌کش متجاوز در دریای سرخ به آتش کشیده شد   سخنگوی نیروهای مسلح یمن:
🔹
نفت‌کش متعلق به دشمن سعودی با نام «أمزان» در مقابل سواحل «ینبع» با یک فروند موشک بالستیک هدف قرار گرفته است.
🔹
اصابت موشک دقیق و مستقیم بوده و منجر به وقوع…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/683985" target="_blank">📅 17:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683984">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
عراق به ایران و عربستان پیشنهاد تشکیل یک شورای امنیتی مشترک را داد
عراقی‌نیوز:
🔹
عراق رسماً پیشنهاد تشکیل یک شورای هماهنگی امنیتی مشترک با ایران و عربستان برای رسیدگی به آنچه بحران شدید اعتماد بین دو قدرت منطقه‌ای می‌نامد، ارائه کرد.
🔹
قاسم الاعرجی، مشاور امور امنیتی نخست‌وزیر عراق، این ابتکار دیپلماتیک را از طرف دولت علی الزیدی، نخست‌وزیر برای آشتی دادن تنش‌های جدی بین ریاض و تهران طرح‌ریزی کرد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/683984" target="_blank">📅 17:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683983">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24152d0a7.mp4?token=P7oRsmZGdQiEAU9Iaj975wwR6kzu406VsLcUMai67zvOYnMxFpe0JIovKhMrjPywzPmIhP-Oox_KKUicSfwkJ3-oB6evi6QCgqdqkszSILcnLv-hxM7u8q2WdKbi4BuNDu1sq6HTTU0X4ZiMgNB-x2Vn2PTX-Ku868EnbgnUu6Ip_iBXZzKTziqmyqhKhKKG43I4QdkiCOaoaLtQbWZSUcdr_PbQfuxpATTbBdkb_MlVG7fp_bsUrjJezN9z63qXNf087XglKTx1BiU4YNJk9DHFpkUTdNv3e4wrv1xovHE-T6VJc89CCURfkZyn4RrHLmM8kllRDS3y-2CSwy0WcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24152d0a7.mp4?token=P7oRsmZGdQiEAU9Iaj975wwR6kzu406VsLcUMai67zvOYnMxFpe0JIovKhMrjPywzPmIhP-Oox_KKUicSfwkJ3-oB6evi6QCgqdqkszSILcnLv-hxM7u8q2WdKbi4BuNDu1sq6HTTU0X4ZiMgNB-x2Vn2PTX-Ku868EnbgnUu6Ip_iBXZzKTziqmyqhKhKKG43I4QdkiCOaoaLtQbWZSUcdr_PbQfuxpATTbBdkb_MlVG7fp_bsUrjJezN9z63qXNf087XglKTx1BiU4YNJk9DHFpkUTdNv3e4wrv1xovHE-T6VJc89CCURfkZyn4RrHLmM8kllRDS3y-2CSwy0WcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تقابل جنگنده‌های J-16 چین و رافال‌های مصر در رزمایش ۲۰۲۶
🔹
جنگنده‌های چینی J-16 برای نخستین‌بار در رزمایش «عقاب‌های تمدن ۲۰۲۶» در مصر، در تمرین‌های شبیه‌سازی‌شده با جنگنده‌های رافال مصری روبه‌رو شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/683983" target="_blank">📅 17:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683982">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KapISF7rPQtYAfhrS-2oYXr1H6ks5zlQMoagY76icheEgTJ1POqpLJajKPfNJK05d0QJfD2tFZK6JJePkpUVZIC6d9n3jwFZMUbYgPW6p2Q0pLk2yJuVFUfUKSBB8_psXp6EWpkDRPibWPRgTFzrRRkONovgsTi34R9vNWCcinQZ7YoCS1WJtgrEuU5DElWzRpEoow_j-D_KyWvexBSTbql0bDRcegFm7hWcIKHh4CEIAA4LcA9npiSBBJ4aAHW8rrz5Fy8M5BnF2qxV8lBRYkcYyT7150rqD2miK7_1SyCFZBaCIlO80EMruMO07q3-MWNjOrb_4G0GPqovPztTiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا: از سحرگاه امروز، گسترده‌ترین و بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد.
📲
‎
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/683982" target="_blank">📅 17:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683981">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFSOctC-5_-vhZrjctbrkwLgOsBaDxUiw7I_ripHGBkFwJUrb-dIHcpIDndAwwyofRIG6tzKJHIMaP2vHmg8fCpGmUOlWRhQ86Wd9lUXVahtYTDU273KtfTfxOZm0WmgWv3B_l3LifXqEg5RDSHVERftdnMDwKT3qpsO9v5APMYWusAG9MpnS2Lj3g8LH7C9gJtep1q0hN8xjDHG9KFWRB9UYw4tBnb-tUceELlXU2SbcoKRwECF1i25wruu4wC_d9GiWJmx--Dde38hAGfKlFC2d-iT_SWFwr4p3NKU1n1sPOy_Ycii_67eJuPNALA9UlavPfecMz7YKsE53dFG_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکوردشکنی جدید فولاد خوزستان؛ بازگشت به تولید تنها در ۳۵ روز پس از حمله دشمن
🔹
امین ابراهیمی، مدیرعامل گروه بزرگ فولاد خوزستان، روز دوشنبه در جریان بازدید وزیر صنعت، معدن و تجارت از این شرکت با اشاره به روند بازسازی خطوط تولید پس از حمله به این مجموعه گفت:…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/683981" target="_blank">📅 17:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683979">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
سیلی محکم یمنی‌ها به سعودی؛ نفت‌کش متجاوز در دریای سرخ به آتش کشیده شد
سخنگوی نیروهای مسلح یمن:
🔹
نفت‌کش متعلق به دشمن سعودی با نام «أمزان» در مقابل سواحل «ینبع» با یک فروند موشک بالستیک هدف قرار گرفته است.
🔹
اصابت موشک دقیق و مستقیم بوده و منجر به وقوع آتش‌سوزی گسترده در این شناور شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/683979" target="_blank">📅 17:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683978">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd3d5fbbed.mp4?token=etQ5FwsBUq0YZ0WZRMIDL7wLTJSdV_-14QypEJbPtmM0-rxAirGNQ-QO3RwVTFwzaccO8LA78-fiqmtkfxjJqyogF1hCGklmuc1q5VFB3LveUtrccvYqhAwk7v6XCaELlLMUOYG8_L1Feye28fufS1gN2OF7fbJRxPy1ZcrTDKX-u36O49g1OY70_pQ0HVcONzhCg2Z5DjO1VUbM-3znI01aDJ5h5jIPXPbnn6_w15S8TYj_NnjRF16O1JCh9U3G_aYIX-brRTaMNZLZ2pFQk9rjtBnaf2Yec-xI8L1gf6LxCtnjewbkimG9pMk2ynq8kx5Bymq-QbPioI2BXKgn6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd3d5fbbed.mp4?token=etQ5FwsBUq0YZ0WZRMIDL7wLTJSdV_-14QypEJbPtmM0-rxAirGNQ-QO3RwVTFwzaccO8LA78-fiqmtkfxjJqyogF1hCGklmuc1q5VFB3LveUtrccvYqhAwk7v6XCaELlLMUOYG8_L1Feye28fufS1gN2OF7fbJRxPy1ZcrTDKX-u36O49g1OY70_pQ0HVcONzhCg2Z5DjO1VUbM-3znI01aDJ5h5jIPXPbnn6_w15S8TYj_NnjRF16O1JCh9U3G_aYIX-brRTaMNZLZ2pFQk9rjtBnaf2Yec-xI8L1gf6LxCtnjewbkimG9pMk2ynq8kx5Bymq-QbPioI2BXKgn6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اخبار تائید نشده از حمله سنگین یمن به مواضع حساس و انبارهای سلاح مزدوران سعودی
🔹
بنابر گزارش منابع خبری، نیروهای مسلح یمن با اجرای حملاتی دقیق، مواضع حساس، انبارهای مهمات و تجمعات نظامی مزدواران سعودی را درهم کوبیدند./ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/683978" target="_blank">📅 17:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683975">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvWYBjz39FTcxywlFkUP1yoAL4VM8GsYzD5pIWIU3eF10wQGRGKzaG3ZtrvH9E1-6baS2-gja1lTk4Y5VSpNDLYBrTMh98-GQ85TRx9ZVQYiZ6YWDo0nqSXICezRd01agoKslKxLs7GBuM05CE7nOkzTAP4TQPO9wiHOJSvGgnuTr7I5A_HIy8UxKczgUbLypH02z7FiPE-n-0ZuQDvA0zc_LC5zR1Jve0B8phYsG7TvEucnqrmx09E7VGHJLY1z58I0E-cNNN_MYABt_MpD3KiKyKHX3kUJHvrcIW8SWujapdv5aPHHPtJhZIEvistyryIeVunaKjmjWpPH4mmOXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران» / ۱۶
🔹
کاهش۷درصدی ریسک اعتباری بانک کشاورزی در سه سال اخیر
🔻
بانک کشاورزی در ادامه روند رو به رشد شاخص‌های عملکردی خود در سه سال اخیر، موفق شده است همزمان با افزایش حجم تأمین مالی بخش کشاورزی، ریسک اعتباری را نیز به شکل محسوسی کاهش دهد؛ دستاوردی که از افزایش اثربخشی سیاست‌های اعتباری این بانک و ریل گذاری موفق در مسیر حمایت از امنیت غذایی کشور حکایت دارد.
🔻
شاخص ریسک اعتباری این بانک طی سه سال اخیر وارد مسیر کاهشی شده و از ۱۴.۹ درصد درتیرماه ۱۴۰۲ به ۸.۷ درصد در تیرماه ۱۴۰۳، ۸.۲ درصد در تیرماه ۱۴۰۴ و ۷.۹ درصد در چهار ماهه نخست سال ۱۴۰۵ کاهش یافته است؛ دستاوردی که با وجود شرایط بحرانی جنگ و چالش های پسا جنگ در سال های اخیر، بیانگر ارتقای کیفیت نظام اعتبارسنجی و بهبود مدیریت اعتبارات و مطالبات است و روزهای روشن تری برای پشتیبانی پایدار از تولید و امنیت غذایی کشور را نوید می دهد.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/683975" target="_blank">📅 17:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683971">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVeUocX9C1k1aiv_XQhMyWKH9jEarP3PWxmERpyhqrn5SHB6vbw1QA_fbR6_CR0FNxZunw1Vqtl8O3TSIrZgLAtvyXSPjpz-yVYr4kb7e3EUaa44gvO1_fq7WFek2Progz6UxuMFjjatc6qHQfT-wV0CqDGA7xUXuESErt3Hd1YDg-t7_6gctu0n5TEEZIZN_Z0rJSzzbglsYJLcR1RWoM11i-o0dHnYVUNo7rSVkz1v3MCvhvtYcLnW-fJHStyIHZ8mVCWBwZGioWMpEUm5wl0fEVPm6_7Tdi_5_S6ZmCXVJ0nTijYgYs2nPPLx8pjr3Tgs_a0COXvuXbD2YKTJpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آموزش آنلاین ۸۰ برابر شد
🔹
در رویداد «تخته سیاه» درباره آینده آموزش آنلاین، یک آمار قابل‌ توجه مطرح شد: استفاده مدارس از اسکای‌روم در بهار ۱۴۰۵ نسبت به دوره قبل ۸۰ برابر افزایش داشته است. آماری که نشان می‌دهد آموزش آنلاین دیگر صرفاً یک راه‌حل موقت برای تعطیلی مدارس نیست و به بخشی جدی از آینده آموزش تبدیل شده است.
🔹
اما بخش جنجالی ماجرا جایی بود که کارشناسان درباره کیفیت این آموزش هشدار دادند. فاطمه مقدس، مشاور وزیر رفاه، اعلام کرد باید درباره تکمیل آموزش آنلاین و حضوری هم حساسیت به خرج داد.
🔹
از سوی دیگر، کمبود ۱۲۰ هزار معلم، ۳۰ هزار مشاور و بیش از ۱۰۲ هزار کلاس درس نشان می‌دهد آموزش آنلاین می‌تواند در کنار مدرسه، بخشی از پاسخ به بحران‌های ساختاری آموزش کشور باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/683971" target="_blank">📅 16:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683970">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fp0jzG7hugztrBPv4fWI2IBtteEgNXbMK8m37XW9Z3CMfv2nf9_yXt_PYulwMcm-FvR_-I3uDM7MdnIeD617aH6J0G0FAYGY55gAIc10isGoKAk2f5W5VwmnltWsq68G0_APlJfKxgSsZq1FkarDRI1KQ0gEVJ6Jvh0ry9xDIlvJvqOD6Nkal9eKjNFdTXtMrH1YaC_wYNZwzJHi0L9MO1Bb_6ql-qoriSGzx9XWpO_meMkpiTSGl6ljr-AC3GEI_coDWeTIbzJVCW3w7rxEJ-4cwvIB5fiqBrtyfjxoBLyl6WveU9eHfIa8BwiQ9lM4294tnXrRr-ZZqMwuWTR6UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لفاظی‌های جدید رئیس‌جمهور مستاصل آمریکا علیه ایران
🔹
دونالد ترامپی که با وجود روزها درگیری و عملیات نظامی علیه ایران، حتی نتوانست آبراه حیاتی تنگهٔ هرمز را باز کند و همچنان هیچ دستاوردی از جنگ ایران به دست نیاورده است، بار دیگر در یاوه‌گویی تازه‌اش مدعی شده که «ایران به‌طور کامل در حال فروپاشی است.»
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/683970" target="_blank">📅 16:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683969">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7VxZhQN9Ej9qLZ0plf0FlXiM6YZ3qnJHnPfpl-621RlTSc8aLWEok0-GWwJc2DFCM6cQ32Qe5ebu3eVdTrnTwJEiUYo9NrhSKt9w1AsqMaIlpF0nlio9O0KpOkWf7tFobtjGBL1KYpV__HmfZfeqjY3GuR6Ib9VcbSuTLka4Kdcr2BXMBdFLrpsn7GrOUXWG6hRiuCDakSuQZg945TsgKjXy74d85nm2xTh1QKoo7n9dIW_ifuo3ioGlKjO6sE2tS-XHPHajQameeaRzpwq5J28wNNy2Cp08HGB7bnszUL50C27pl2bzAIs0mauWcE7T948ZryguFh25MTXU7WxiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاجیکستان تصویر ابن‌سینا را روی اسکناس۲۰ سامانی چاپ می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/683969" target="_blank">📅 16:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683968">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8vny2C4aUXYx45Bk9uMsX1UKQPcVLaE1tsD2kY-2PYYeZRpbfqOiZw8o39JsY79dOM0mEG-nLBwGx8Vbtpjn4MuGadejvp8U2ND6B0d7bch-PzK_DffhIpDBHVEz03eJQWKlKcZc75yAhz2G_Oayi8xMNkNjGxV9Qa-kEig66eCoocCIUUX4A6tjcKHr88aoq6cEAePH4EwuQAz1RdugrwCVLhDFcXDzdFD5T8otreDcmyvLFzFfrbCSQB5v1dSQsb2cfbLzE3y31PUYptPQkiiag-_3y_jMVxRz-5xGjhc9DnaRhVuxx8xuPA_ApJbn6MCe3Xiry6ZLsRiIz86IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایش توان فناورانه کردستان در حضور معاون رئیس‌جمهور
معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور در جریان سفر به کردستان و همزمان با هفته دولت، از دستاوردها و توانمندی‌های شرکت‌های دانش‌بنیان، فناور و خلاق استان بازدید کرد.
🔸
در این نمایشگاه، محصولات و دستاوردهایی در حوزه‌های
کشاورزی، تجهیزات آزمایشگاهی، سلامت، خودرو و ماشین‌سازی، فناوری اطلاعات، نفت، نیرو، صنعت و معدن
عرضه شد.
🔹
از جمله محصولات ارائه‌شده می‌توان به
پودر ثعلب، فیکسچر دندانی، دستگاه کشت خون اتوماتیک، سامانه هوشمندسازی گلخانه، کربن فعال، بذر هیبرید توت‌فرنگی، تجهیزات هیدرولیک و آفت‌کش زیستی
اشاره کرد.
🔸
همچنین چند شرکت فناور استان، نیازهای فناورانه خود را در این نمایشگاه مطرح کردند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/683968" target="_blank">📅 16:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683966">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtgkhvvvIGKd7i5xvMOwKdrvt6bFl7MV1Cm8o9gcWEpYnBFNg30VYfm_EnTFprS4jLs0nHvjk2aEOm113pzIna_Hbxk_8wdrGsydCEpXLvWK3PKbKQZXlpwxyhaNO6COplLWhvdn4fERXcYZwp7NG5EKPu1m8b1PxR44159dgmtooRyswU8WM5taCWMnAM42CY3keaZqQNfwnAPiK23Z_anRAcfFktO8wUdg84UKdIw8jbax4IWKoP2D5r9MzGPFXH3yF7Sg-4UY6MM7VeQ0Gh_Mh27mnWL-rL3Vlh31RV1S-gNFmuta7usOsHKZq34-QKiwmfLymqv-A9UWTcrOgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکوردشکنی جدید فولاد خوزستان؛ بازگشت به تولید تنها در ۳۵ روز پس از حمله دشمن
🔹
امین ابراهیمی، مدیرعامل گروه بزرگ فولاد خوزستان، روز دوشنبه در جریان بازدید وزیر صنعت، معدن و تجارت از این شرکت با اشاره به روند بازسازی خطوط تولید پس از حمله به این مجموعه گفت: فولاد خوزستان با وجود روزهای دشوار، با تکیه بر توان و تلاش کارکنان خود توانست در مدت کوتاهی بخش قابل توجهی از ظرفیت تولید را احیا کند.
🔹
وی با اشاره به حمله فروردین‌ماه امسال به کوره‌های فولادسازی اظهار کرد: هدف این حمله ایجاد اختلال در روند تولید بود که در پی آن، ۱۱ میلیون تن از ظرفیت تولید تحت تأثیر قرار گرفت. با این حال، فولاد خوزستان تنها ۳۵ روز پس از حادثه توانست به ۶۶ درصد ظرفیت تولید خود بازگردد؛ رکوردی که حاصل تلاش شبانه‌روزی کارکنان و سرعت در عملیات بازسازی بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/683966" target="_blank">📅 16:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683965">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuWpajRnxnwaM33xZ2-uQogwnS79iubIjWmonVZBWm-cqRGfvGHoKlhPpQxYDKy_tGm7PzaDcMsQ5WDPGKxfmU5nNumpmb2_WwhdG2QO79wX5pDd1vfndDKBObQBhpoeJKVaCnBPjpX1jh2HEQA68xyLC3YVSIRhUdBDEsCYFaiEAF6l4GTRMZ5nVITHaoiIdVSrk_BuyprKMrOT4juxKdCcqwSQtzkpWhLJfKl-Jeg0rPO8oXLl3tafsI3KS1goOZqaKryUAVR7OPdLxARmhcRx8EBJcxS9kMFwR8KyAPjVtdy1AJgds_a0O2leifeL-L_XeKCiWYIIV5Wv-6YWKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رویترز: ایران ۴۵ نفتکش را در تنگه هرمز در فهرست سیاه قرار داد
🔹
ایران ۴۵ نفتکش را به‌دلیل نقض مقررات عبور از تنگه هرمز در فهرست غیرمجاز قرار داده و این شناورها ممکن است با جریمه، توقیف یا ضبط محموله مواجه شوند.
🔹
کشتی‌های مرتبط با شرکت‌هایی از امارات، عربستان و کره‌جنوبی نیز در این فهرست هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/683965" target="_blank">📅 16:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683958">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LEwWHauN_Bi2r9v6WMOBGCx_dNBk3FKfSfm_IUNoEs7LX5aWEJkIREpzCFfPx_KJmJr8Ji2Ls7B6JDzhS_0oSBfhJiEhZDzPCqXsm_9DewRCC2bMwUPStLh8ClQk0YhEUmHtniTxhyT6sHzzggkd5io6GTf9YMurbIv5ngIwK_JV8xPBiOGwzbCq9tjW1X1AfANG2NPkuWVuHcX1IO9m02Z7naVZtw_I7IBcw9QUwBtdHwRSs8kJQFLO9SjAWgzISat0lRqnuTaqq6nYKSpcVKG9-ID66wr0vAgs8827tuUhdIj5dNotMq6bSjK0ojZZQuZtt9n9tt99jZMIvWZoPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qe2Quf2p-Xr361ENBixx-RDUixn9G1Nlb3nnmfgQBWpcihPNqo6jXiKLC2ju1T55-owIrUSJM-W4JZAjCXbwvDoPpG5BnVq-IL6xIf5rhsSTC_fOHfqo9Qy9IhGrlSAoUjPTGd6mX2ULuRL7X2Om2B9uJLCA7OPPjmh_JvZSQe__-D9kTqGhYvZ4fwLGqMRTB7ZMds957nizAQGoAk4iVYA0Sufbhzg9rt03mJt-SxZqPQBG4ooa809niqLnFAnyKekou_34LSwpumSZCToReTES9YoT329bE2PvyehUwSU-JPwRdf5T7sKMEfqWqf2I17G_B2A9EL-84AxhebLjxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bMkK_iROHp9_ymyHg0yrcCZfZU3XLDY4atsgmENRBD5nOI-nS4rUfg82yH1ikS238j_K6uTMhYPiK7xEie2WBv_Ffin5fx8UYsUfhMUe5o7CVGWweRzdLqndIjO7NvAAMr5DPyyS0On6ANAGSQ4Z3mwkAIjym7W2TAWnbq3_y_d2DoTG7lIYlrF12KdIvdZHEqHzz9f88lhumGc_GCtY5RmN8roACXd9_NlggdZpWPqquewWtzqE79G3wVtbGPlMdCgtt9P4SCRsmEoaifAbN2vlbXMLhxoPnOMpHCcAEZsi9ZhjMEPuo_i6E8fp_8cnBUaRh_ylrgaVTky8oxR0PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N3_rveQOt4ELU417tz2jPQMAB0ku4nzYx8oVJBPmNC5XxiePL91iwzDoIgzkoU39eEJrM3f5AWXQj6PtawDuxsay1UdXdyEfmWLBpw8Uns6YkB8Ljzy7F3dyxzZKX8nd62RAQMemyvHfTdEz7TiylKWJMFtpUZi6jTNFbNQe13ADMKlt7XLBfucTeDf3JpgvM-PpNv6o-ZTvJ_O2Ie_pTu6JbKcRjjGGV3LbxcVsLFLsGF0JCCXFImINNlTWAQLe210BsWwMH4xpmSXhvG07iNnl7wALiGSzvBzX2_0fG1w4yNtPRj9cOuZgOjRRHfOmco2W01jHg4eDIMkt3c3Dxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wplpz4mqarsUYFZSuYT4m9VK4Bxzmb8bWnyZr15cPH6tht4Uk14QH_yhTraIZaruBEQmWCYqtBQsAEbJeledUlQIxt3sHeIdiZLBU2Fy6gensU4vf0UcdJvN8CtEk-Nt1Y9lGRXhDmLdU4oWZvbYvvemYLlZuiFrs9cwPQOXYrD0CB5xyqEqtXYlYF_lsmw1uY-snb6x5XTpOlo5R6aLlzJdXfvpk0qUFhuXVTQwYcm00YxatV8N6WOC0RISWVxuBXy6eBhDrRxAhzd1ldjEQfQmbieU1vHyPCCnG9KMyfQ1Om6kHIh7N5V1f9AIPWu_afadK9JxcRYAkzAL3Un_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AdXuLRzQ8Rrezd0liMTYnR-CvWiodxfP2CedbUshNiQMVQYKicX48o-IBtBg8L7SHzOO0jFt4Rm2O01OMpZb_Xb32lrh5hmBdq6vl4GiSNXnsfWYT8QoCg-GIzIAR6NPH7iFoQ4jiUMGdeX1kIOXHpRpjGmO2R8B7acj4TQkB7ZPaScIPsR75sXgvS2AF-hm-emfHAbZ4OPKNFv3YiRSlPKKH1cQ9M2aeOMibzy-xezpl2PkKeJvPidn5w91wllWNRvZ5LiKb4Ni9rR5bep2Ou2-OMeIVpCnDTJlfxx8mHEks_E8uGMo8TVjdu_QMDt6-hMUvL7GiNdJBkb8-hVioQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سکه که حباب داره، بخریم یا نه؟؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/683958" target="_blank">📅 16:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683957">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
چین و اردن در بیانیه‌ای مشترک: باید کشتیرانی در تنگه هرمز به‌طور عادی از سر گرفته شود.
🔹
نیویورک‌تایمز: کنترل ایران بر هرمز با عوارض کم‌هزینه‌تر است.
🔹
دادستان شهریار: یک نفر از اعضای شورای‌شهر فردوسیه به‌اتهام دریافت رشوه دستگیر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/683957" target="_blank">📅 15:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683956">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
خوش‌چشم، کارشناس صداوسیما: جای یک نفر مانند محسن رضایی خالی بود تا حریف ترامپ در جنگ نرم و عملیات روانی شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/683956" target="_blank">📅 15:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683953">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d432a1bcd1.mp4?token=GK_iB2A5e2DIsvhBLK84lfznPc2HWZ1cjUsBp0Ab0btscDgEorXsSk2frqE6tg1zQdyAKXXe9Cut24tEmPr6YR-UiAVzmCLJwW24JsfqwjYst_X46f2JCabFdJCRhtriOAmgau_gJPVuqB3ov3PCQWicz_6-7flVKRmydD2dnrcvHx65yzFlPdbXsrx1z0g6uFQrQllyl1PK6CzybBo2a8AMzthCHm5E-k2PLBYM2Tb_zT5GONnF8d-OxpjqEMoXsu6jqpsgnKP6RgonI_6tmqxJgs48ZN0LjJi5Qy79d7L1QNQak54Duq10SJ2qc9iI5zI32Cy32ce83YFi-Z9XrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d432a1bcd1.mp4?token=GK_iB2A5e2DIsvhBLK84lfznPc2HWZ1cjUsBp0Ab0btscDgEorXsSk2frqE6tg1zQdyAKXXe9Cut24tEmPr6YR-UiAVzmCLJwW24JsfqwjYst_X46f2JCabFdJCRhtriOAmgau_gJPVuqB3ov3PCQWicz_6-7flVKRmydD2dnrcvHx65yzFlPdbXsrx1z0g6uFQrQllyl1PK6CzybBo2a8AMzthCHm5E-k2PLBYM2Tb_zT5GONnF8d-OxpjqEMoXsu6jqpsgnKP6RgonI_6tmqxJgs48ZN0LjJi5Qy79d7L1QNQak54Duq10SJ2qc9iI5zI32Cy32ce83YFi-Z9XrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس اوقاف اهل سنت عراق در حین سخنرانی از حال رفت
🔹
عامر الجنابی، رئیس اداره اوقاف اهل سنت، در مراسم جشن میلاد پیامبر دچار افت قند خون شد و از سکو به زمین افتاد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/683953" target="_blank">📅 15:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683949">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b84e839840.mp4?token=qQZhBdg2NY_DcaKnN-A50q8LnpyFQqxZYbHjdqSitNfXdLqzjxwxdU9IHZB-s9hqvYHxa-CxnV_6ae7RIlVVnerDCIuz3aEBywtXKw9vdD5U-3L1g28_qhrTtFkT60yeCKsJWds7_4Zuw18L8sIItkPD1Era6GOV6qnueQf4i4DnymyaDpiRfN_0CI4YqDaOmisGCKx4Js00JHsUViyr9zlQ9BZnsQeyhwtRIEzEeFzfluei4htsiVE36tLtbaaei67-myJE30rdksVW9VswuSnyfASBNg11nBl0yhHbGC914o6adEVkZ2_TVk1p7Ru12PYgbD8QMPL-gI2LILMZpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b84e839840.mp4?token=qQZhBdg2NY_DcaKnN-A50q8LnpyFQqxZYbHjdqSitNfXdLqzjxwxdU9IHZB-s9hqvYHxa-CxnV_6ae7RIlVVnerDCIuz3aEBywtXKw9vdD5U-3L1g28_qhrTtFkT60yeCKsJWds7_4Zuw18L8sIItkPD1Era6GOV6qnueQf4i4DnymyaDpiRfN_0CI4YqDaOmisGCKx4Js00JHsUViyr9zlQ9BZnsQeyhwtRIEzEeFzfluei4htsiVE36tLtbaaei67-myJE30rdksVW9VswuSnyfASBNg11nBl0yhHbGC914o6adEVkZ2_TVk1p7Ru12PYgbD8QMPL-gI2LILMZpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس بانک مرکزی: کشور در شرایط سختی است اما تلاش‌ها برای ثبات اقتصادی ادامه دارد
🔹
مردم باید بدانند که مسئولان سختی‌های آن‌ها را درک می‌کنند. معتقدم با مردم باید صادقانه صحبت کنیم.
🔹
فشار آمریکایی‌ها نمی‌تواند ادامه پیدا کند و با اطلاع می‌گویم آن‌ها بیشتر از ما نیاز دارند که این شرایط تمام شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/683949" target="_blank">📅 15:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683947">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b4be905f.mp4?token=Wh9DSKzdqKAByYOeuTXzhFhJ3z__inQL0-Ozahl-8f-h0fzVgKr2r4jmt6rhfqgW76K8H8TogvsKXvuBoFHPLqDIvuOgDQty9TZPZPetEbZ7F2eFslihz6LwtCbs7JT1aywA_IFdeD0bY-kcDsDV09iHs4lyquhIH0E744DEETRQl2LmezXAaX-OGmLFh90DnU7JK4H_WTr5NGyk9_xRnjxY8ObS5M_bImwAJMQ5-7tgpaoqPV7oLNpwweoPvqS3PQw_PQFNqGoZuJT0o_4EpKEO0kAG_Edn8Z7uyY9TLbmBmlon0xIe6LoRo9qoVH_gtAxXRzgDjrrRX5tcqGEjrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b4be905f.mp4?token=Wh9DSKzdqKAByYOeuTXzhFhJ3z__inQL0-Ozahl-8f-h0fzVgKr2r4jmt6rhfqgW76K8H8TogvsKXvuBoFHPLqDIvuOgDQty9TZPZPetEbZ7F2eFslihz6LwtCbs7JT1aywA_IFdeD0bY-kcDsDV09iHs4lyquhIH0E744DEETRQl2LmezXAaX-OGmLFh90DnU7JK4H_WTr5NGyk9_xRnjxY8ObS5M_bImwAJMQ5-7tgpaoqPV7oLNpwweoPvqS3PQw_PQFNqGoZuJT0o_4EpKEO0kAG_Edn8Z7uyY9TLbmBmlon0xIe6LoRo9qoVH_gtAxXRzgDjrrRX5tcqGEjrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
روایتی از همت و نوآوری در محیط خانه؛ انگیزه‌هایی ماندگار که ایده‌های ساده را به درآمدی پایدار تبدیل کردند.
🔸
اگر با تلاش و سرمایه کم کسب‌وکاری راه انداخته‌اید، داستان کوتاه خود را در یک صوت ۳۰ ثانیه‌ای بگویید و عکس کسب‌وکارتان را ارسال کنید. بهترین روایت‌ها در خبرفوری معرفی خواهند شد
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/683947" target="_blank">📅 15:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683946">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeXkiLaWEHdNMYsl3VN074zM3NXGn91o3Jm2XxybNhprI81DBLaugmfEAG7cX7jIW0q6djVenD6DghUR3UAZr4C0gNoWivIAUiuwq3wxxfKwQ4s0n2c8tTkvzmA9DU77BEezjtObrrEsF8r-b9XUyjqBP6RGHvS1kSx5lYQOz9v4KWL4FstdGiHY7vxdn8oZgCGwcAamlOI6ayZZi-fAjtNINRMRkJRs7PeZT5j258iRscxrDzdahyxk5vegkHHXPEiMcALtZhpwVXvbsyLPlfZlgReDMNNFFqZuD5aoI3973Cn7TquWVYLxFSMifjBlsDFsm9SNuwsszAWsCZPtYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشروعیت‌بخشی به تروریسم در پارلمان استرالیا!
🔹
مریم رجوی، سرکرده گروهک تروریستی منافقین، اخیراً به‌صورت ویدئو کنفرانسی در پارلمان استرالیا علیه ایران به اتهام‌پراکنی و سیاه‌نمایی پرداخته است؛ حال آنکه این گروهک در کارنامه سیاه خود، سوابقی چون ترور و کشتار مردم بی‌گناه ایران، همکاری نظامی و اطلاعاتی با صدام در جنگ تحمیلی و اقدامات تروریستی و خشونت‌بار علیه کشورمان را دارد.
🔹
با چنین کارنامه‌ای، سؤال روشن این است که پارلمان استرالیا چرا تریبون خود را در اختیار سرکرده یک گروهک تروریستی قرار داده و برای ادعاهای کذب او اعتبار سیاسی می‌خرد؟ چگونه گروهکی با این سابقه که همچنان در رسانه‌های خود بر فعالیت‌های مسلحانه تأکید می‌کند، در محافل غربی «دموکراسی‌خواه» معرفی می‌شود؟
🔹
این اقدام استرالیا عملاً به تطهیر و مشروعیت‌بخشی سیاسی به منافقین کمک می‌کند. انتظار می‌رود وزارت امور خارجه ضمن محکومیت این اقدام، دولت استرالیا را پاسخگو کند؛ چراکه سکوت در برابر چنین رفتارهایی، راه را برای تحریف تاریخ و تطهیر تروریسم هموار می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/683946" target="_blank">📅 15:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683944">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4E6YSzsntUkhuyJGgWPXQgPFJGZZBKYymHdbYkuUkc3xu3kPru7uLaOiBZYf0Qcrsv4rGOqzwA8HJuvcRrZvJh6NPm7id5X8hhreJD5_Cm03iYRbvy3bhCO98WAiEQeeMAGon58bzbMH7SSR_MB23KxjHsqYZ1Hv30ja7XmuB7PFjGJDLT8R5H3HAiSdV77hmxA1d3YC9HsZM4J2XXuDONzWHpcHeDwipI2yz4FvWQhH0iJIF1YUH7p0R3nwgXnCnMtwB4LlVr7dwQdljNqFDm3jomuQ8mrfcFa6JEwFdNpX-xnSEH06qzjevYHhUO8cgYy00F4b7ByqzzILk_uHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار صریح سردار رادان نسبت به نقشه دشمن برای آشوب/ مراقب بهانه‌های بنزین، معیشت و اقتصاد باشیم
سردار رادان، فرمانده انتظامی کل کشور:
🔹
جنگ سوم تمام نشده؛ دشمن به‌دنبال آشوب با بهانه‌های بنزین، معیشت، اقتصاد و بیکاری است. غافلگیر نشویم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/683944" target="_blank">📅 15:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683943">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1ACv1Fm1mM7585eWpLHI98v5yawb4i76tr2I7hNRqcRDa35FoQCp-lCTXv4WnJD-wNYZ6mmwV6WS1GckCiFfPSN3MPalPUJ5mF546qT2py-l__lQl0_DLZXkgUqG_k31tMcuqI4C3pUYanWqSApftULs39ze-RBe_v_L05gyjtVRFwztVVPCc3gjPj-qRAgzmzSzwmrNTLpTkJQXZG-cJSpgi2waP_I4lkaTN_QEzDjGTJyiaLN8YHraNEsAj0L7jcG3-DXCuRvXilF3wS_H_vNuQQiPHYGekXST0kHKHGlztx4hutWzXZETbXRtlj8MuIFX5gfI3P9PZZTmef_zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفت‌وگوی ویژۀ دبیر شورای‌عالی امنیت ملی امروز از شبکۀ سه بازپخش می‌شود
🔹
گفت‌وگوی ویژۀ سرلشکر رضایی با شبکه خبر، امروز ساعت ۱۷ از شبکۀ سه سیما بازپخش خواهد شد؛ گفت‌وگویی که به مهم‌ترین مسائل و تحولات روز پرداخته است.
🔹
در این گفتگوی ویژه، دبیر شورای‌عالی امنیت ملی به بیان دیدگاه‌ها و تحلیل‌های خود درباره موضوعات مهم روز پرداخته و به پرسش‌های مطرح‌شده پاسخ داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/683943" target="_blank">📅 15:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683942">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d986e8cec8.mp4?token=cHThCLA3jSjef-PDA3Vh1t4bPobCglhqh9v9EzcOqtM5CKwnQIwsHeA9v6KfXGhDJBD0Zn5S9TOGdZtLETIlE4RUg0_UtyqGhwAL6y8dvejQ0c7b8MatYQa733ZJ4GV031Avz6X395qRQ5nV_hIY6DO2y0k5QgWMEEprcjabpBokEbWxL_HM93SpR2YsxMYupsa5IKY0jadV-7f269xoMLw3B6FrRRcoLtjuLjpllhHlDJR9X5lAMX6YQmSaZySuAmcod7xzFU215h-Ivy9sprYN5FHiUL_SEGFRretb12DuBH8lgNdvNODG56L9SjcIMggTN7qKuuFqdCm_q1828w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d986e8cec8.mp4?token=cHThCLA3jSjef-PDA3Vh1t4bPobCglhqh9v9EzcOqtM5CKwnQIwsHeA9v6KfXGhDJBD0Zn5S9TOGdZtLETIlE4RUg0_UtyqGhwAL6y8dvejQ0c7b8MatYQa733ZJ4GV031Avz6X395qRQ5nV_hIY6DO2y0k5QgWMEEprcjabpBokEbWxL_HM93SpR2YsxMYupsa5IKY0jadV-7f269xoMLw3B6FrRRcoLtjuLjpllhHlDJR9X5lAMX6YQmSaZySuAmcod7xzFU215h-Ivy9sprYN5FHiUL_SEGFRretb12DuBH8lgNdvNODG56L9SjcIMggTN7qKuuFqdCm_q1828w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقاب اصفهانی: بخشی از مصرف بالای بنزین به خاطر کیفیت خودرو است  رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی:
🔹
با اینکه کیفیت برخی تجهیزات پایین است اما تغییر رفتار، زودتر از اصلاح تجهیزات و اقدامات دیگر قابل انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/683942" target="_blank">📅 15:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683941">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
چطور با تیشرت استایل شیک مردونه بزنیم؟ #استایل_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/683941" target="_blank">📅 15:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683940">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXUl8BhbR7IVbzAorzM1wOvs8ps-XnHbqWJBjFein0dMxO8X0F9EoRnWHeE0N3Ny73tUl4J-IhQK4Xak6F5SUmdZGPBG3wb4GBUSc4GTcs0NpzCPCBhmF-nBi1AJ5akNv_nkwlhm8aDaxN5lcaHL6674pfZcG3c1_o9vVtdVsviHPeuguIXqvjuJB9DKbbDih8Bv9uC6r5q0nOtJRc7WXh9idZi1hxoHl7xklbi7F8ts_njAUVX9jAEFuEBSxoQvUMB4T8_EmvuSgQ56Q8PSANae3fVVx9sfGlAAaQqVfW1_Jg3U9WtItVMbZ-7C7wTY1-oKoqvcEoilRFp3oaz4IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افغانستان ۱۳۹ تن کالای ایرانی را با ادعای بی‌کیفیت بودن برگرداند!
ادعای کابل‌تایمز:
🔹
اداره ملی استاندارد اعلام کرد که ۱۳۹ تن مصالح ساختمانی و سایر کالاهایی که پایین‌تر از استانداردهای ملی تشخیص داده شده را به ایران برگرداند.
🔹
ادعا شده که پس از ارزیابی‌های فنی، مشخص شد که این محموله‌ها با استانداردهای کیفیت داخلی افغانستان مطابقت ندارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/683940" target="_blank">📅 14:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683938">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTWvoyfI93yjuNs9Od3QqKwI_TyxYXo1M3bJYBthBU2rnMutoW7o_7tU2mfP0Q-J0k8Dn5u0ZzWVRJtJtqbEUt-BQU-B4SxxGUtFosGr7V1iSr9Kanq3WPVk88adGKDNcDiQZiC-SBpoX-mltmGDrYdm24_JFN2Ty-1G1lJg-y4Du8X2S94wqBsegYRW9NZ29uaZj9bbyX3-m4STC6op5SP8IHrwRwxet-5xGWtmmVfE5gWeI7t4FdxSIMSi5YqK38_DLVVNg5uz2sy6S5DlqBNts8drOVmdz0TkUyWUU1LKO3t0aESLB96nT4l-YO4r7-9UtsCV9uMDElLr9crO3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ بخشی تقطیع شده از سخنان قالیباف را با هدف اختلاف افکنی در تروث منتشر کرد! #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/683938" target="_blank">📅 14:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683937">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c29214271.mp4?token=MT0mYQiomESlEMYwIO-64ggfKqqFfR3J8_SpYYCxL3BtdcmnSHBU7viqHVK1I0vBnbvaInC0CTFLiZZ9t-PJu3RTcBJ6ThCl6r05gQvNc5O1YXEZ-q63YviH9IP4JDMeebVMKcbgFtHPCootPP7piatmqQSznwyPEvV8sy1RYak1xAIj9Xpu7UOvzU-E7dcDhjc7n0667iCCCtTUVJLGtw4UnNkoM8bqq5ChOXYS7Wgegokn77OZ0Q9uDwC9WVAT2Z67-uM_XnsQL5GZc-3WeB6AdjkOn-XIhuG6yoKZFMNJmY97IXSw6t9AnSvFwoBbWwZqiVyYAAmBS9Jldq99Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c29214271.mp4?token=MT0mYQiomESlEMYwIO-64ggfKqqFfR3J8_SpYYCxL3BtdcmnSHBU7viqHVK1I0vBnbvaInC0CTFLiZZ9t-PJu3RTcBJ6ThCl6r05gQvNc5O1YXEZ-q63YviH9IP4JDMeebVMKcbgFtHPCootPP7piatmqQSznwyPEvV8sy1RYak1xAIj9Xpu7UOvzU-E7dcDhjc7n0667iCCCtTUVJLGtw4UnNkoM8bqq5ChOXYS7Wgegokn77OZ0Q9uDwC9WVAT2Z67-uM_XnsQL5GZc-3WeB6AdjkOn-XIhuG6yoKZFMNJmY97IXSw6t9AnSvFwoBbWwZqiVyYAAmBS9Jldq99Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر کنجکاو هستید بدانید یخچال چطور کار می‌کند این ویدیو را ببینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/683937" target="_blank">📅 14:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683935">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73c0a03d80.mp4?token=POoFlDd-grFkutPIu0S_9_kmLdqH-ygTHnwrwgluDw2IrU_gwBnkFw4EiR5Zkd4g6ECMStg-m4HJsPB66yKWehKmKYxsde7Kh0RGHufSm9Mk_zBedLRNznGme5U8Er12WOdSe9od9mffqUVdBi3WYYFq716gwqcoFtI0F8Aw-DC7QoEZuNQXlpTiLj7NJEhb-V2oHmAogaTJYtfff3Q95vxxNbjbqVAXkyIJUJ9C20cFF19dtSDHnn7YY8FXMd-rRFOIo94HyjF7BBDgrtspeLv5nl1s--p5eW8ArhleYtWubH1f_Ku6yzOXISQ9Ob8kcYet-oaYCs0DJIAZz32Y8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73c0a03d80.mp4?token=POoFlDd-grFkutPIu0S_9_kmLdqH-ygTHnwrwgluDw2IrU_gwBnkFw4EiR5Zkd4g6ECMStg-m4HJsPB66yKWehKmKYxsde7Kh0RGHufSm9Mk_zBedLRNznGme5U8Er12WOdSe9od9mffqUVdBi3WYYFq716gwqcoFtI0F8Aw-DC7QoEZuNQXlpTiLj7NJEhb-V2oHmAogaTJYtfff3Q95vxxNbjbqVAXkyIJUJ9C20cFF19dtSDHnn7YY8FXMd-rRFOIo94HyjF7BBDgrtspeLv5nl1s--p5eW8ArhleYtWubH1f_Ku6yzOXISQ9Ob8kcYet-oaYCs0DJIAZz32Y8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرود تماشایی غول آسمان در لندن!
🔹
لحظه فرود A380 هواپیمای غول‌پیکر امارات در فرودگاه هیترو لندن، واقعاً دیدنی است!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/683935" target="_blank">📅 14:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683934">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1edf0a1588.mp4?token=R7R63AgxBCS8GJ8ZJlWJ9HFFgQV3F524giuP3lPHHg_A8lm7uG2vEiUZScklEWf490O1qfcaJzNcOARyBp0YjpytFnUk555Ac7Y-uq-1fAkAUpcHcmVEOoKUBHaPegXuNa0Nztp9ysZbkzMlSn0-8a66nBiQWmXpcnpotTsYxwYJVz2GU7C25yXHHsejBDLxD81X7ZD3ZU7RzAY0-eirj1-QzoBU-vONWgczPMlhPxoyh3NSJ_kZT38m77BY_kN5-plLukc7IGclgGQhm9LpcO5TYwV2PHqYACZL3w8Y-mFX2qWO_t6VlaDQQsZ2wcvzTWAyII6hS4CEGk3TKWEJTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1edf0a1588.mp4?token=R7R63AgxBCS8GJ8ZJlWJ9HFFgQV3F524giuP3lPHHg_A8lm7uG2vEiUZScklEWf490O1qfcaJzNcOARyBp0YjpytFnUk555Ac7Y-uq-1fAkAUpcHcmVEOoKUBHaPegXuNa0Nztp9ysZbkzMlSn0-8a66nBiQWmXpcnpotTsYxwYJVz2GU7C25yXHHsejBDLxD81X7ZD3ZU7RzAY0-eirj1-QzoBU-vONWgczPMlhPxoyh3NSJ_kZT38m77BY_kN5-plLukc7IGclgGQhm9LpcO5TYwV2PHqYACZL3w8Y-mFX2qWO_t6VlaDQQsZ2wcvzTWAyII6hS4CEGk3TKWEJTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فکر می‌کنین کاربرد فلش کوچک کنار آمپر بنزین چیه؟
🤔
#حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/683934" target="_blank">📅 14:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683932">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4fd2d7782.mp4?token=DGqjDwYxT6n0cxrH_3PPYmKU7AhAXB8sUYMypWU_7P2Pr7QYkaf2BVv2y9EUi1BnX4EX6oEYCTXs6uL1TkoN1G1rGb1uSynvUZX_fA_-yVvU-qgHYUPN__BhHOrTaI-jddr_ul-XIBSWjad2o_k4tJC-QbNYXf83kZ2g9I-EkIwXMd-xXkZ76NnN1qkOUFh7NOCKmQmxsbE6Td_KARzTO_lqT-WWghECTDX9ly9XlNgsY1hrou5TLf1ckrnfY8XrwhZ1-l5NoexoZwcluvgfzXGXHa6LxpCIxPErvKzcuHW2cKGdhd8LmpWDBCmZRbFUBY5Ux6G9PWoZpreZYlf-UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4fd2d7782.mp4?token=DGqjDwYxT6n0cxrH_3PPYmKU7AhAXB8sUYMypWU_7P2Pr7QYkaf2BVv2y9EUi1BnX4EX6oEYCTXs6uL1TkoN1G1rGb1uSynvUZX_fA_-yVvU-qgHYUPN__BhHOrTaI-jddr_ul-XIBSWjad2o_k4tJC-QbNYXf83kZ2g9I-EkIwXMd-xXkZ76NnN1qkOUFh7NOCKmQmxsbE6Td_KARzTO_lqT-WWghECTDX9ly9XlNgsY1hrou5TLf1ckrnfY8XrwhZ1-l5NoexoZwcluvgfzXGXHa6LxpCIxPErvKzcuHW2cKGdhd8LmpWDBCmZRbFUBY5Ux6G9PWoZpreZYlf-UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس جمهور: از رفتار تفرقه افکنانه پرهیز می‌کنیم
پزشکیان:
🔹
از آب و خاکمان در برابر دشمن دفاع خواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/683932" target="_blank">📅 14:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683930">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l7ft-lgiOlUmTja6JtNZ6xXmFv3TA_IkKxbr9cf2MTr12RE31Q5ofUhQGpv8RbVWJU4sFD5jK7MCUxIewDapHY_z86XdlbX0c1znrpeuC4dr6Rmb-W1HE6Xxq_20bT0Duy8Ud6ksZ-q7zIRI0G6FfY6EFxo2x6OvT5HtC5Ulrc5meb_5xO_W6XsTbHHSE7sX5nyPBxecKRN9ARm1a6CgtUsxccevUmjJqnVrGv-nXnQ30AjsM72VJ7n8q6P-g2HRqnaKNI30d31rtevTSa602UaJmZxc4G4Zc075HDG5gfbvbIfCRtLb3BDyzxHrPzrUt7hB-iq0LiVaiFLGf5uO0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JlV1nip8fQ1JDR1abrNwiG90FAuelcD2Azwvlo06IqYjp3Ul5c4jogvANSLmjFvyNEow4267HbTKcM12BVquzdk9N1TTsXcISzL_8wnjdxJBt3t938VkF2NoMHgeMUAwE6BysRtXCkVnbFx8EViIuc8MRLjUGhAsdwQjCOFXc96BZakNeLnrNJRvKFsVATtOweLse8R_0kkCTn1AfWOf9bujSUu9GckgkD2jJmTF-qUONLZjRLGIFDu69ai0BHFZtCNfdDsqMwt3csdM55eeJvtR5bCfPAUwN84Jx4LGAM_sSHng39mYdYc7cKGoZ36JcCgnKyJvBwvqeaMg3keczw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نشان بلوتوث درواقع امضای یک پادشاه وایکینگ است!
🔹
نام بلوتوث از
هارالد بلاتند
، پادشاه دانمارک، گرفته شده که دانمارک و نروژ را متحد کرد، لوگوی بلوتوث هم از ترکیب دو حرف رونی
H و B
، حروف اول نام هارالد بلاتند، ساخته شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/683930" target="_blank">📅 14:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683925">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fracDNEQSutoRCbQydHwN3czIV9tVTX-nj2EYybxfIRXkMJH8MYbF2X4IDNF8cUI5qsaFm6xkFCqfDbCXjBiqan1o3doIqphY2lrbgCI4TKc52C2ACD8IicaGDM6UgxaBnJ6QtPRfPRYwgdgHDNug-TuZplXwpd_895g9u2zlRIiRfJPLFDzTWDzYtwlL6le0sJ-6dTXRN3p0A0inuLFAHlknV1T0Kvf3NzhogfpmAnFe4DaYBoQrOqCNYSYPXOEV9PmBeWzY8dVKp_ufBqAOjW7RnAit6Qpcf0nL2Q0hx4hyN0sDhZcIOohawCT0gEnJxTyS30dRfHETGiaKdGyxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cuWvuWW_uB7-UqBytQBKQJPLucml5zrr6-VKYMD70sMzQZ6DDiwvE5XycT0kXSfO7nRqbeXqQM6g5zTcOq1lPGzFs_M6227J1Y3svK-tJMUn56OZfVHy0x__hNAE2lRPVvijEMOfuT9QBHsBOfzGSOkKiauGTCguJvB4fTjDooFvSUBlThVPrKU9hWZRwEq3lFkDi7SPP1u76k6Obw7j2qJi55320RzadqLZ1CAZ3PxiiZ6pYqWjYoM_rjt8SaBc6a49UvEDV1mlQPITibHnplqU2qHjHm2whvZiqkpB_SybZdj1TErXre_7x5vZsOqQvTFZFeecJA1t5oURwpYNtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/463a3f0b88.mp4?token=eM3jp2MWuQo9VAxEY4aAstzFRis1c8-LYEvJvyNpj4U_LUUeqGBkY9acA8nWoqQ1dq2Az3PRvtZEVnFg8vDIciXdfOwP8SzlwdS-uop5EAleFF3vO65vyVF7VoV0uGMirN9Y41DslUzT2Bp41k3NXhBmAJRpoxybjTO7C_FNoEpMzOdo_YobDOw0mEd58uF7Vqy6vw1E-Bl43g0Qzgai_99PSSDKTvofUW0QlcfmCOPLuzrA0VuZdjHxwJmmG3tA4wEKxOZAEpPH6QSdbpHP20jHXSoCH_3fASrcWzPD1UWuZBJDPcauj5nlhlil0F2NOupdgTLFQbOmjL6hrhaN6mY23U3ImrYxmxpedmOjamYpcsf9VGDc62Z56gCHGYAw5VCU3-hFgjsLKg55NuX-QscyvokzRsRS1T74hkchDT-Nx415IOxVZ6X-MD0SyEDG7FhTs8p-HryRqW9rZor7sMqyGunuIbOpVNR5w1-nZrA3bxr3dk09lHKs0wEnJ2MhOBC6aOXjynq3yMknqK8NLGiPxQ4WHFuBhOkgHBKtDMBhKb_OC1OCXIvNcN3uUGWbeem35rCVKaIV_KLjL_cQOgDcCExmFa1Os7_1wZc4fo9-xrQM_Pse8T0kEznNwmQieBC72ns-ywYnMC9y7iDweAMQEr-0qy_bTJ6svwHm8gc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/463a3f0b88.mp4?token=eM3jp2MWuQo9VAxEY4aAstzFRis1c8-LYEvJvyNpj4U_LUUeqGBkY9acA8nWoqQ1dq2Az3PRvtZEVnFg8vDIciXdfOwP8SzlwdS-uop5EAleFF3vO65vyVF7VoV0uGMirN9Y41DslUzT2Bp41k3NXhBmAJRpoxybjTO7C_FNoEpMzOdo_YobDOw0mEd58uF7Vqy6vw1E-Bl43g0Qzgai_99PSSDKTvofUW0QlcfmCOPLuzrA0VuZdjHxwJmmG3tA4wEKxOZAEpPH6QSdbpHP20jHXSoCH_3fASrcWzPD1UWuZBJDPcauj5nlhlil0F2NOupdgTLFQbOmjL6hrhaN6mY23U3ImrYxmxpedmOjamYpcsf9VGDc62Z56gCHGYAw5VCU3-hFgjsLKg55NuX-QscyvokzRsRS1T74hkchDT-Nx415IOxVZ6X-MD0SyEDG7FhTs8p-HryRqW9rZor7sMqyGunuIbOpVNR5w1-nZrA3bxr3dk09lHKs0wEnJ2MhOBC6aOXjynq3yMknqK8NLGiPxQ4WHFuBhOkgHBKtDMBhKb_OC1OCXIvNcN3uUGWbeem35rCVKaIV_KLjL_cQOgDcCExmFa1Os7_1wZc4fo9-xrQM_Pse8T0kEznNwmQieBC72ns-ywYnMC9y7iDweAMQEr-0qy_bTJ6svwHm8gc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جاکلیدی رزینی؛ یک ایده کوچک برای شروع کسب‌وکار خانگی
🔹
این بار در #چرخ_زندگی سراغ یک ایده ساده و خلاقانه رفتیم؛ ساخت جاکلیدی‌های رزینی دست‌ساز.
🔹
با کمی رزین، قالب و چاشنی خلاقیت می‌شود جاکلیدی‌های متنوع و شخصی‌سازی‌ شده ساخت و با فروش آن‌ها، یک کسب‌وکار…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/683925" target="_blank">📅 14:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683924">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RE5uNoNyZjU8-exRzzPoGfq5NROg193hCdWQaYPHHtYVfO87fq51DyJhgnvKuEB9W4PoZQvJHIND17lFoV5lnwkaEjJqQZH4Qa1cRvNDHrzr39tg0H8R3VBOD1xohZ3M7y9B5WDMSah41VqRyNmAEnCDLTc1wqFeGln7s2qdFRjiCAuz9HHdsbZ2-3JZ79YVRKtVeR3vJFLvrc4oZ0SyHRcSUasiWjkdJ9iJVxZ4UZXFask_792YxR2QamSjoxq8bjLOEFDPZiTkaJ37qPWj7AEkz4EMCZ3faaqxHGf286hzVVgrfXA4wZynD6e_lb1E-hlv-Lf8GQ3JzKR8QZRDtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلعیدن موبایل توسط دختر ۱۹ ساله برزیلی برای جلوگیری از افشای پیام‌ها
🔹
دختر ۱۹ ساله برزیلی برای جلوگیری از دسترسی نامزدش به پیام‌های گوشی خود، تلفن همراه را بلعید و پس از جراحی اورژانسی، جانش نجات یافت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/683924" target="_blank">📅 14:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683922">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/683922" target="_blank">📅 13:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683920">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
تقسیم اموال و دارایی‌های متوفی میان وراث مشمول مالیات نیست
🔹
بر اساس بخشنامه سازمان امور مالیاتی کشور، هرگونه تقسیم اموال متوفی میان وراث اعم از توافقی یا قضایی مشمول مالیات نیست، اما انتقال اموال و دارایی‌ها از متوفی به وراث و یا اشخاص ثالث مشمول مالیات بر ارث است./ ایلنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/683920" target="_blank">📅 13:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683919">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651a0e2e99.mp4?token=VMaiqlYdBdZlQm-SgwNqnr4jODEMZZpne0gpUosL4ojcZ5xpR6gEEJeulH1imNKhjkvU4O9I2lQwou1t5rni4f4wWVpV5ApXEUs4tk-92eWWUXitupIiXSkry3QrI3eBwTIHhe24I1MR_3SWatX0T5CxQ39xMJkjQpjPJSnUR3MJy_2v9oWZhT6VgJPOPnu53ioF-v0ksov2NIlKf4Iz07vCVXxHyHOwHZKtriH7mWOK6MBSYPH4fJSvqPnSE1_f3_80fIcuoMAEXoCd3DdLtOwS8bpNmNoAJp1_CnYy9rvQVUd1L77TLs6PCEEfipRFTNBqnGo86FdLZR2NwO1FQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651a0e2e99.mp4?token=VMaiqlYdBdZlQm-SgwNqnr4jODEMZZpne0gpUosL4ojcZ5xpR6gEEJeulH1imNKhjkvU4O9I2lQwou1t5rni4f4wWVpV5ApXEUs4tk-92eWWUXitupIiXSkry3QrI3eBwTIHhe24I1MR_3SWatX0T5CxQ39xMJkjQpjPJSnUR3MJy_2v9oWZhT6VgJPOPnu53ioF-v0ksov2NIlKf4Iz07vCVXxHyHOwHZKtriH7mWOK6MBSYPH4fJSvqPnSE1_f3_80fIcuoMAEXoCd3DdLtOwS8bpNmNoAJp1_CnYy9rvQVUd1L77TLs6PCEEfipRFTNBqnGo86FdLZR2NwO1FQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: پیروزی را تبدیل به شکست نکنیم
🔹
آمریکا که تا دیروز به فکر سرنگونی ایران بود اکنون تمام بحثش تبدیل به باز شدن تنگه هرمز شده است.
🔹
بالا رفتن قیمت‌ها در بازار ارز براساس هجمه‌های تبلیغاتی و جوسازی آمریکایی‌هاست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/683919" target="_blank">📅 13:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683917">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e9a4d424e.mp4?token=In0NN2OYX52Afq0mkalWd2LFYCl7QmcuLo71etVHT1hg6e8LQruxu3wmXgD5G4Hu_bQ7JmGJR9kpp0q3Dzt4_ccW0EeqifNezF8udR30BW_0BWeTkzZNH3LHMpwyIu8lpGEKiI08M9C20yUiS6pOFOKABE7w-aWEUaPLy1KMrlaUzCoPEtgd4Dh3E7uzNcF_ptI-I4nddPaunwVwvTzbw1aQBLKRouWJMPI3mK1EN1_wOC9_eOpeHbysJJYLk7PL564JXY6RuAKtpi34lRIjcxqcRzdWiwxgl4mbj41XYq8wYCk0J2aqWhy_rdUDlZNT4pOcD7VEzP3xYvPQiqaUqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e9a4d424e.mp4?token=In0NN2OYX52Afq0mkalWd2LFYCl7QmcuLo71etVHT1hg6e8LQruxu3wmXgD5G4Hu_bQ7JmGJR9kpp0q3Dzt4_ccW0EeqifNezF8udR30BW_0BWeTkzZNH3LHMpwyIu8lpGEKiI08M9C20yUiS6pOFOKABE7w-aWEUaPLy1KMrlaUzCoPEtgd4Dh3E7uzNcF_ptI-I4nddPaunwVwvTzbw1aQBLKRouWJMPI3mK1EN1_wOC9_eOpeHbysJJYLk7PL564JXY6RuAKtpi34lRIjcxqcRzdWiwxgl4mbj41XYq8wYCk0J2aqWhy_rdUDlZNT4pOcD7VEzP3xYvPQiqaUqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از تخت جمشید از بالا، پایتخت امپراتوری ایران ۲۵۰۰ سال پیش #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/683917" target="_blank">📅 13:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683914">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CqmxkS7xrYy6qwgpfG19El3-1uctEkoxrG42jwNMDW9PJAxDvejNOateL_FUAMaQ9NxEBB7qRXqJIdPi58fHoA6BaO0g-33BpcMzL5shFKPPEcLpHZ4TIc9KnwbqTjm1imATvo7v4R5mkoCK1GO3555jYmqA2V3Fz_JjaS18R7ppke0ElZuZC0f1ZGC5RSFkRuYVgTZTiNmY6T7HKej4g58tMdseTv5wW90ZmH0OWH2o75OkPw9NWavmWeK6RBN3jkhziwnwX1gwJpAbibnE0yaO2dG4PbtU69tHMwaZZ2U5oEjiWezaeCuJvQ5vNXBxVztqFA0QkD_qyY2o0W08BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eFn0aQxmOPOat0xsOfl3F846ckYCObPNwsVs4smsvXcgVPdxYRV7OKxsrvaQPxZnnbztTBpHCsnuhJMlQKqCkDRMcdXMmqF-4QnDCns8I67TYOVZxkMF1kSfuhCY9j-o0MCD51tMmY5m2NxDH8grr6YnBc0313NbeG9oiqnPUJolruh2fuHf7o4DXv65nkEgx1WrKH5mamyJqOqcuuFX-C6NYKD9ff3khQ1TCiiX4KE0fEKKDhFOSEFgojvb5lCYlvqgay089-4b6kaz5gkxcroyQpB6FQVRgm8p-LIJveswP9fQb8WvcXrl5NKkI58Cy53DWpa3Mr2TottmcWrKlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FzTnUyerxgXrCAW1Gd2YaJ5bROwmHlLqUf455Z26d_tDWa4WuMWwM0Lc-MczW1H-mKaHaRVM5WxUtNNGguUhTDpNQ9VNIOjEbxgDxfJZCDwHABsZnXUxMPPpc8np37Gpe6bDkIF1rbxRZ_zEGWxu7XQrSvnAmIMSDmuNsUn1ZUe6MWgyIguxV7-kjWNMXYkyMx_Z1eBqAFHeeJLVCB2lZAdlBfFuWW8Ps8hboc3xw-7fpWpOlgQCSHCmOFka6VJOzoWv9j1xl2plBjgfDwYs7g4cBsIPCIVrJPt7SzCdRLBvLoLU5WSSuwSkFGwp0PG1cm9EweBFSF6MKhCONAO1pA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
طراحی منتسب به گلکسی S27 اولترا؛ شباهت به آیفون ۱۷ پرو
🔹
تصاویر فاش‌شده از طراحی اولیه Galaxy S27 Ultra نشان می‌دهد سامسونگ احتمالاً نوار دوربین مستطیلی و حلقه مغناطیسی سازگار با Qi2 را به گوشی اضافه می‌کند.
🔹
این گوشی به دوربین اصلی ۲۰۰ مگاپیکسلی، فوق‌عریض ۵۰ مگاپیکسلی و تله‌فوتوی ۵۰ مگاپیکسلی با زوم اپتیکال ۵ برابری مجهز خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/683914" target="_blank">📅 13:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683912">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCpJGg2vH-QRZxro-pg6WBJL92bbrLvCiftyDk6HDz1-xGrV3CL3cO5yHMQl6AqimlUvHnQoBpcsEsAwPQt61974lWTLxGuxz8-YbNuLPU-ELpCvHC8RdJqXA_OmSugAxdwYTk1-uk2FXpkptcu6beNjENSeIWtWfWkt-PAptu3nCI6EuEDG8nSOyPvvAMZlgPeHPD5WCk9BuLBw83F7bET7bfO1dK_f7J_qHyy4BZeZdmWUtrt393NWVniuDJPDxbJLmrkJTFzi38KgMSkMG0ECJmpmsybpRfd3JGahjVVgaK6mQSEoqlVvh1fWWCSJYZmvi01x9yyxoh9CF-fAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_خودرو
| قیمت روز خودرو های بازار کشور؛ امروز ۲ شهریور ۱۴۰۵
🔹
بازار خودرو امروز ۲ شهریور شدیدترین موج افزایشی روزهای اخیر را تجربه کرد.
🔹
برخلاف نوسانات پراکنده روزهای گذشته، امروز رشد قیمت‌ها کاملاً سراسری بود و از محصولات اقتصادی تا مدل‌های مونتاژی و رده‌بالا، همگی یکپارچه گران شدند./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/683912" target="_blank">📅 13:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683910">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76c7177ed3.mp4?token=FUEnUAzV-QAxNjRGTzAe177O_dVSl0So7VF3RXuI2e1D8PmuGoU8h4zzX1BXHJRavaZkOh9xP147qbIe_3wKylxGyBZH1rpejBEA2-1-fUokLketczdGGky0pcgX14CPL047tIHzfk9bljbtodEJsqq2t8IV5iOQdQmnzrwd1mDKvjWCo_IVO2T1fIpfs3fhOOo9OpM558w-P7mEU55z6cL7K71Lo4n4DHZcM2Oy4w_92QsuH7PpSa9Dk9NLtY9Miw3wX7k4_uPjKhyd036UUmFsa9xfXcr_aZ-74Hn_vVq0P-ax9WuU3kBRIpVXO1sXO5e5Kq7xe-tm5WMFlc9rIV7oYhFurjtHYbSDBHE-jGEE3Ud8lUedJzxtbDbJvD3vrbhz9D7z4PlaQT4psHRrApFiEss9wu0L6UZKgsXRWyc-UXn1cxJk_HpZ324X5Hb7v2YCReO4OxqB6uEf7cIptm1MQkumohUIMG0llqgj-LKorlHBxa0V8JGrDwmOMe9f5TTic_qJwMayPkFKzuf9lR-jMzDoGtZOaB6l9lH6uQ8ZlvMoESJoxnxhggOTq5xGWDWYsclJX6Nbeuwf5wwTtNc4ioh1URI3s6eNfNlQOStUCUrKDBCiVrHb8mkGl6hT_E6xqNyiq0Tb6WQ-rJVTbCnCA6P3RUcEm9EOkngj7wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76c7177ed3.mp4?token=FUEnUAzV-QAxNjRGTzAe177O_dVSl0So7VF3RXuI2e1D8PmuGoU8h4zzX1BXHJRavaZkOh9xP147qbIe_3wKylxGyBZH1rpejBEA2-1-fUokLketczdGGky0pcgX14CPL047tIHzfk9bljbtodEJsqq2t8IV5iOQdQmnzrwd1mDKvjWCo_IVO2T1fIpfs3fhOOo9OpM558w-P7mEU55z6cL7K71Lo4n4DHZcM2Oy4w_92QsuH7PpSa9Dk9NLtY9Miw3wX7k4_uPjKhyd036UUmFsa9xfXcr_aZ-74Hn_vVq0P-ax9WuU3kBRIpVXO1sXO5e5Kq7xe-tm5WMFlc9rIV7oYhFurjtHYbSDBHE-jGEE3Ud8lUedJzxtbDbJvD3vrbhz9D7z4PlaQT4psHRrApFiEss9wu0L6UZKgsXRWyc-UXn1cxJk_HpZ324X5Hb7v2YCReO4OxqB6uEf7cIptm1MQkumohUIMG0llqgj-LKorlHBxa0V8JGrDwmOMe9f5TTic_qJwMayPkFKzuf9lR-jMzDoGtZOaB6l9lH6uQ8ZlvMoESJoxnxhggOTq5xGWDWYsclJX6Nbeuwf5wwTtNc4ioh1URI3s6eNfNlQOStUCUrKDBCiVrHb8mkGl6hT_E6xqNyiq0Tb6WQ-rJVTbCnCA6P3RUcEm9EOkngj7wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مامان اولین سکوی حیات‌روان هر آدمیه، برای همین نقش مادرها در سلامت روان انسان خیلی مهمه #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/683910" target="_blank">📅 12:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683909">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
آموزش ۵۰ دوخت گلدوزی با دست
🔹
آموزش ۵۰ مدل دوخت گلدوزی را اینجا ببینید. با فروش این هنر دستی، کم کم می‌توانید #چرخ_زندگی را بچرخانید
👇
khabarfoori.com/fa/tiny/news-3239788</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/683909" target="_blank">📅 12:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683908">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5pqtqXpf_bynltjQFE9xAiYGFtHpxXVIjebyHahPv_dfeIg8stQCjp6TOX0HBt8sHjsInIAj5YJ31xsBBhLrH7o5Pe81B5cvJXcyDevcsOThN3i_FGm10R9UyF_QfVTjpOL3RySCANr2spj5dvV7O68-l07wwk4F4gP4U4fSBTggove_VZ88PeFk7e4waWi8hWRX5sX0lz9VFIWH_zKJ-NpcgFmrxSD87NBOMbp8nfvh64gFS08lf1wEsTN4tiVijEv524gIviDqw13dws3BcJbo6nnLzQv_fGtNF792rszR_d_xHufZvhdx6iDHYgft-PXwvwpMG7bUSvcyMQwXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ بخشی تقطیع شده از سخنان قالیباف را با هدف اختلاف افکنی در تروث منتشر کرد!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/683908" target="_blank">📅 12:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683907">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرمانده کل ارتش: ایرانی تا ۲۰ نسل هم شده می‌جنگد و اجازه خدشه به ایران را نمی‌دهد.
🔹
سخنگوی سپاه: ایران در نبرد با آمریکا پیروز میدان شد.
🔹
شاخص کل بورس در پایان معاملات امروز با رشد ۳۰ هزار واحدی رکورد تاریخی ۶ میلیون و ۱۰۰ هزار واحد را ثبت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/683907" target="_blank">📅 12:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683906">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEA8nFY2oMsE2Ecexb29TDTCi1jhTkAp82Q1Po_WNXQc44lQ7KnzQtCaJRslUc2klycDh0eBrOz7tBoT_yBUHTyPqmxRMplUgc_bL4omDQNIgfEcLrtv2YueNN2K800cV-w3uuOLqW5WGLDaXvKfJb4IT-RE94lTlhUUb05Dj0YvMrexUfnaHl6oRGLf5hlC6fBcurhQ2ElCbQjo8WBxdXzNM3Un1sFR0Jvv0U0mAloe9PNaaewyn4v8f8Os-O5eXty0R6JlEJfD1T3CrPY-o21j0I_9NlBXoYCb8uHbybvVFnDNZQ73U9FhyXPhsxH1Mqf5FGtRjh5x3nhT5PKtYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت بسیجی اهل سنت در زاهدان
🔹
یک بسیجی اهل سنت به نام «نادر سارانی سخی» توسط اشرار مسلح در شهر زاهدان ترور و به شهادت رسید.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/683906" target="_blank">📅 12:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683904">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lyep0sf4hVSgOxywXcuLMiPgaBNM5XwgAmNG3j2vV56M61HWF6_k8TG7vDC7YEzXzmdjw54Vsk4rxPc1aPnuNIq3k567nIOGaQX0Iq-tdfwQn6rtyCiS053dXCUd2dU_pt16VXTCxPFbUMAVLWW1Om7pvJ2H5KqGBvT70QOKf8OCpW_to3CiJPJ-pIlmXMI03ZTfAdrHa5ffUeb7JdsRYQ7sLHBRgLc7Uhb6EX9jxgHTWGEOQePwGHJdUMo3CbNewQUSyhQ3ck4KcPUcLdPQZ4VYsPJBZzbb7ciX8yb4ln4J1_7G1ZCbYTgonGbVO9SABmVLga8OfEhuSli5zKZQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دادستان سابق فدرال و ایالتی آمریکا: پس حالا دوستان ما کره شمالی و روسیه هستند و دشمنان ما کانادا و دانمارک؛ منطقیه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/683904" target="_blank">📅 12:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683903">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
آغاز ثبت‌نام مسکن استیجاری تهران و مشهد از فردا
وزارت راه و شهرسازی:
🔹
ثبت‌نام مسکن استیجاری زوج‌های جوان در تهران و مشهد از فردا آغاز می‌شود.
🔹
از ساعت ۱۲ روز سه‌شنبه ۳ شهریور تا پایان روز چهارشنبه ۴ شهریور متقاضیان مسکن استیجاری زوج‌های جوان در استان‌های تهران و خراسان رضوی انجام می‌شود.
🔹
در این مرحله ۳ هزار واحد مسکن استیجاری برای اجاره به زوج‌های جوان فاقد مسکن با اجاره‌بهای حمایتی عرضه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/683903" target="_blank">📅 12:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683902">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3325bfbe5f.mp4?token=kv-4OdchXN5YRX_tPZhRakCe5rRrKvsxaK33c4pGLURSsn6BDXMg6f5CkmkouVTOG84Hbrb4QB57E6Ze9Jc862czc5nAcZ5Tr5JwJfGnMehs_B6N6p33e_wjIkE2ZD3cVxHISqxCOTkOJAmCgVyAx3_rDP2CKGf0SEhei_2bhd9Rgq-xajhUk8pz67wxJu30RX38CvBK3RDpboNnSB7b6sbUJA8E9fz_ZtRADklNB7qsBNSh-mGLzDz4DKzokYVlIvBOjn30zgH72i872cwHvGBl5QxzLLG6VVVeRFHffVRNO2drnBDgmpT67Y2_j0QY7F4oUQ5pjE_XcjNLaLOIpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3325bfbe5f.mp4?token=kv-4OdchXN5YRX_tPZhRakCe5rRrKvsxaK33c4pGLURSsn6BDXMg6f5CkmkouVTOG84Hbrb4QB57E6Ze9Jc862czc5nAcZ5Tr5JwJfGnMehs_B6N6p33e_wjIkE2ZD3cVxHISqxCOTkOJAmCgVyAx3_rDP2CKGf0SEhei_2bhd9Rgq-xajhUk8pz67wxJu30RX38CvBK3RDpboNnSB7b6sbUJA8E9fz_ZtRADklNB7qsBNSh-mGLzDz4DKzokYVlIvBOjn30zgH72i872cwHvGBl5QxzLLG6VVVeRFHffVRNO2drnBDgmpT67Y2_j0QY7F4oUQ5pjE_XcjNLaLOIpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خارج کردن کیست هیداتید از مغز
🔹
کیست هیداتید یک بیماری انگلی است که خارج کردن آن از مغز نیازمند جراحی بسیار دقیق برای جلوگیری از نشت مایع و گسترش عفونت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/683902" target="_blank">📅 12:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683900">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ورود فرمانده ارتش پاکستان به تهران
🔹
عاصم منیر فرمانده ارتش پاکستان دقایقی پیش برای دیدار و گفتگو با مقامات کشورمان وارد تهران شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/683900" target="_blank">📅 12:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683899">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کلید اولیه سؤالات کنکور ۱۴۰۵ در هر پنج گروه آزمایشی منتشر شد.
🔹
رئیس بانک مرکزی: مشکل تامین ارز نداریم.
🔹
فرماندار جاسک: احتمال شنیده شدن صدای انفجار کنترل‌شدهٔ مهمات در جاسک وجود دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/683899" target="_blank">📅 12:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683896">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
مشاوره تخصصی اتاق تهران در حوزه حمل‌ونقل و لجستیک بین‌المللی
🔺
اتاق تهران با ارائه مشاوره تخصصی حمل‌ونقل بین‌المللی، فعالان اقتصادی را در انتخاب مسیر و شیوه مناسب حمل، کاهش ریسک‌های تجاری و حل چالش‌های گمرکی، ترانزیتی و بیمه‌ای همراهی کرده و مسیر تجارت خارجی را کم‌هزینه‌تر می‌کند.
👈🏻
دریافت مشاوره:
۸۸۷۲۵۲۶۹
(۰۲۱) |
۰۹۱۰۲۶۶۹۷۱۴
|
service.tccim.ir/intl</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/683896" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683895">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
الجزیره به نقل از رویترز: فرمانده ارتش پاکستان پیش از سفرش به تهران، با ترامپ تماس تلفنی برقرار کرده بود
/ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/683895" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683894">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Opr-gKStKtyhIQ8LKHC46lDUlmQ-2kSaLZMjUpPWhUpW1eUhyk64ERjwiWhw6KfyaaOgSXRLCf2AkkdL-bTb4WV3pBrhRyLP9PEKEl9ZVLdmt_CExNsAkDvaZZF3K-XovHvi3OYzEaTrAYInCJrozSWvf82LR-Th0JS4S1R7ShRTgSNEFOyunFuqPAIIyqICfDmxPYcsaLXF1AHwLSNXjdpmRW-LDAgJdu1960ZyNhd4X5XuU68kJZ38PYa-GjJZhp4j1AHYRfoA_m8-U9jQKtLij1vbEmKSSJfm8AgathI4L28TkXQy4zfQ09gP1b1ww35U61isD2GtW_DSRxkoeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرش پازیریک؛ یکی از قدیمی‌ترین فرش‌های جهان
🔹
فرش پازیریک با حدود ۲۵۰۰ سال قدمت، نشان‌دهنده پیشرفت هنر فرشبافی در ایران باستان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/683894" target="_blank">📅 11:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683891">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2803d6a33.mp4?token=NR-Kx4WDGnejljMU7VI54iXdZRlwIyfuv7lnsuGHG7ydCXZv_fDxDKGnQFEMYOcXZVyNwNEHRRnvIWyb0rzWF3PJP-EAysIetZkRbSEQheh88oJAG5TF-SkSRkRCo5t_nfYx1u3I0qofV2d6aZLjItcjtkr-ahUpzEUxaxfHZGoWTAHINw7ALn4CAvBOAQk5FyJKGEW0OVZudoPPjPxMFXVeDzNNa42TTfqKV_pn9y5uKytod2T9KSuyqigbM3UChza4-MyLf_54XuiUJOA41mAQyET4FTSuwqZy-XbJJzwL3sg34auHHD_rjNCMHeMm3H5w36j3SpAt5YilRZS4hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2803d6a33.mp4?token=NR-Kx4WDGnejljMU7VI54iXdZRlwIyfuv7lnsuGHG7ydCXZv_fDxDKGnQFEMYOcXZVyNwNEHRRnvIWyb0rzWF3PJP-EAysIetZkRbSEQheh88oJAG5TF-SkSRkRCo5t_nfYx1u3I0qofV2d6aZLjItcjtkr-ahUpzEUxaxfHZGoWTAHINw7ALn4CAvBOAQk5FyJKGEW0OVZudoPPjPxMFXVeDzNNa42TTfqKV_pn9y5uKytod2T9KSuyqigbM3UChza4-MyLf_54XuiUJOA41mAQyET4FTSuwqZy-XbJJzwL3sg34auHHD_rjNCMHeMm3H5w36j3SpAt5YilRZS4hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: از «تحریم‌های فلج‌کننده» تا «فشار حداکثری» و جنگ اقتصادی، آمریکا به‌دنبال تسلیم‌کردن ملتی است که تصمیم گرفته از حقوقش کوتاه نیاید
🔹
تفاوتی نمی‌کند چه کسی سکاندار سازمان ملل متحد شود؛ عملا کارکرد شورای امنیت و خود سازمان زیر سؤال رفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/683891" target="_blank">📅 11:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683889">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3BHuX-75eTl7Pvytg2iELDNCipXw85DnRWrtxlKXRHOJbOBHiJujZpxdXM-cTy9_wjAw0higoAJvITuWFmV1BQrjwOZ7IxTxmRbX6i9b1sZJqHavQFr-HXOyd3ajEKMnle_zbpryMDkUlUI3K-05Quv16deMdjZAS0r5wKGz6Gb_ag-zCDF20Dgy2Fmn2qE94zi1T-Bemff8bLttP8jL0q5vIPaJyHxwYk564mg9_Z34WBeITMYaCA1vbxdRMtb2sw4XLxWo7nSQxXCI9bEi2Bjvn_aLBK1KOo_OFkpTOgxFa8-K2iJRgKuAD4idU2gfm2GUcaku3DoPyLn69snwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نهاد مدیریت آبراه خلیج فارس: شناورهایی که با شناورهای متخلف همکاری کنند به فهرست متخلفین اضافه می‌شوند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/683889" target="_blank">📅 11:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683886">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fdf70a392.mp4?token=sMLRqRrVdyBgGX4lXZP5NqE-QCZYbKAmxrAwva5467G7oFVwKARJnbz_yCvQKyhZeZ5PzW-kXgPjqB1VJGhEoUPALgxBq_H_pSnlZsTH0Iqy-kGWYGqOM0fRajr1azxeNpOKdk5JhelLq8WzQmgnctvzhSmBKYKVOvmFs8NHnvSGmxaBnutXR6-R6BSEkbavK7ZE4r3URvLoz0HD7grU002mx1DXB3RxN8n7E0CNcm7MKdgBsYv_f6ndOS1xjgkhvbaKpD80Kk-_Mpu4eb-ajB4Rz37-Llzo4RZSPxMMlKq-55AP7J9occpr2wqAJ4way8K3GuLM804VuQ1MtZPnlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fdf70a392.mp4?token=sMLRqRrVdyBgGX4lXZP5NqE-QCZYbKAmxrAwva5467G7oFVwKARJnbz_yCvQKyhZeZ5PzW-kXgPjqB1VJGhEoUPALgxBq_H_pSnlZsTH0Iqy-kGWYGqOM0fRajr1azxeNpOKdk5JhelLq8WzQmgnctvzhSmBKYKVOvmFs8NHnvSGmxaBnutXR6-R6BSEkbavK7ZE4r3URvLoz0HD7grU002mx1DXB3RxN8n7E0CNcm7MKdgBsYv_f6ndOS1xjgkhvbaKpD80Kk-_Mpu4eb-ajB4Rz37-Llzo4RZSPxMMlKq-55AP7J9occpr2wqAJ4way8K3GuLM804VuQ1MtZPnlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: رایزنی‌های آقای قالیباف با مقامات عراقی روند همکاری‌ها را شتاب می‌بخشد
بقایی درباره تعطیلی سفارت شیلی در تهران:
🔹
تصمیم گرفتند به خاطر صرفه جویی مالی سفارت را تعطیل کنند و در برخی کشورها این کار را انجام دادند؛ این به معنای قطع روابط نیست
🔹
دو هفته قبل سفیر و کارکنان سفارت انگلیس به تهران بازگشتند؛ ظاهرا به تعطیلات رفته بودند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/683886" target="_blank">📅 11:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683883">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c317278ea.mp4?token=qTCJzgSAMneMWoELhbaDKWrSPPCI1iwVH3jsb_2RfKD-7E882DcLRHJRO0udigvOlD85I51SqFS4FoRsCTJLG-4w6Gsy7TZB0marqlF_C1qYA4l86TSMC_FOzHPADIEn68xw5IvbF0jwsqza3T33tAXZ_vt6QnLjT-Jwa5MjTqRSg7-ydKgU4Hi-7iIOKhZu7uz_FygJi6-souh3U855jPjmYTUsY7lUiDPQ4Yot-YkLOhKMEjYvX-8nVD4mB7rzKKrCxnz4KTo-9hhVW2w5RSPkMYRtGAdO4jsIB8gPL-6iiTmEVt2wKUMBBDY8xQcsF4rnCpj9bDRYqW99Zd8gTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c317278ea.mp4?token=qTCJzgSAMneMWoELhbaDKWrSPPCI1iwVH3jsb_2RfKD-7E882DcLRHJRO0udigvOlD85I51SqFS4FoRsCTJLG-4w6Gsy7TZB0marqlF_C1qYA4l86TSMC_FOzHPADIEn68xw5IvbF0jwsqza3T33tAXZ_vt6QnLjT-Jwa5MjTqRSg7-ydKgU4Hi-7iIOKhZu7uz_FygJi6-souh3U855jPjmYTUsY7lUiDPQ4Yot-YkLOhKMEjYvX-8nVD4mB7rzKKrCxnz4KTo-9hhVW2w5RSPkMYRtGAdO4jsIB8gPL-6iiTmEVt2wKUMBBDY8xQcsF4rnCpj9bDRYqW99Zd8gTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: مگر ما جنگ را شروع کرده‌ایم که خودمان را به‌خاطر ادامهٔ آن شماتت کنیم؟!
🔹
حتی کانادایی‌ها به‌عنوان همسایهٔ آمریکا هم دربارهٔ آن‌ها گفتند «امضایشان را با مداد می‌نویسند».
🔹
تکرار تحریم‌های ناکام علیه ایران حاصلی برای آمریکا ندارد؛ جنگ اقتصادی آمریکا نظام تجارت بین‌الملل را تهدید می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/683883" target="_blank">📅 11:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683882">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtyxZi9eSWb6nedU3-1LN_elhA9ZIq7nSedeuS3XbIC9aNOxJ-EOV6xqME0x432VgQIcTCUPzeuXwbQIsb5bFvrgkIX7Wr0IIlFEEYjuEoYm3Xg8TfncOdc-eqINI9pMfclTkhjRFMSXLPc-I_rAFN2CqOeoHHrWZkkyD0Mp6xSXVsf9xUIhvbby1yXJJhkPtDS2nFZuhLrsm1Lo72CGnfT3J6FMJksrvYsSziTG6QxryScmXPQihTAJpTB0vHhw53e7x078LMy2tTjb3aivKSuNLZy_cGgKLsE2yejko3BRm0tUSfmeEfVIAP62saWzWRfEGFdEihu8IkKyue9CYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلا همچنان قله فتح می‌کند
🔹
قیمت بر اساس سایت رسمی اتحادیه طلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/683882" target="_blank">📅 11:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683878">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1cdc830a2.mp4?token=IDS0BLP_yecVTd-WWCCY_WyJX8zTIaaEatJW03iYQawymo0zlCmL4GCCZ1U34Hj0Cmi9q3fUv231ND-O4FhYgnej2ksAlHBK24Qpen3P-Ihe35UxGfL-5GLU1r7Nl3sFAZ9y7gttf5faLBt4uiEWxvCJvxArpsRQcKloo_6u1RuoKZK5fos5BlMQ1qWxqe_tzFYiQHjWMhyny6nQPbYkO5ohxzv4Y5fhPyBI-nc-qWBiRd3PwmOrH4teJR3VdCduGdJoUCawBC-Ipd2q0wl4UMXZxpHWhIP1vC4gFlxADIEDrbttQ5AYPhzmCVAiO8_jXvkKZ4xKhIdricl-HvZtwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1cdc830a2.mp4?token=IDS0BLP_yecVTd-WWCCY_WyJX8zTIaaEatJW03iYQawymo0zlCmL4GCCZ1U34Hj0Cmi9q3fUv231ND-O4FhYgnej2ksAlHBK24Qpen3P-Ihe35UxGfL-5GLU1r7Nl3sFAZ9y7gttf5faLBt4uiEWxvCJvxArpsRQcKloo_6u1RuoKZK5fos5BlMQ1qWxqe_tzFYiQHjWMhyny6nQPbYkO5ohxzv4Y5fhPyBI-nc-qWBiRd3PwmOrH4teJR3VdCduGdJoUCawBC-Ipd2q0wl4UMXZxpHWhIP1vC4gFlxADIEDrbttQ5AYPhzmCVAiO8_jXvkKZ4xKhIdricl-HvZtwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: ایران در حال حاضر ترکیبی بازی می‌کند
سخنگوی وزارت امور خارجه:
🔹
ما از قدیم شطرنج‌باز بوده‌ایم؛ در سال‌های اخیر پوکرباز هم شده‌ایم و حالا مدتی است که ترکیبی بازی می‌کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/683878" target="_blank">📅 11:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683876">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86534c54a.mp4?token=KXbn7yEi08GcpSwfyYBvpOx7Kxhc4tVHIUFF7QOx4DBwrm01JnFEmg7nehNzXXYCvuVjlq018LXUqBzxRqv-egDXe6D7OvmnTG5I_3rizTS7Txi2Vq6qZIbVUXp8LwtlIMc5aFoQJi-aKnIgwmSGyfS2UUkiDq4cNNzZm3D9vFM5wixXfm3UMOkrZ2rQQUEW3bsjlSjfQYBvlrYpcJqlHGEOC0vXxhRWJtl1LSj37NK0roSKmZX02DtRIo9kFHWarzh2_Cz2ivs54KVjIW4ufAT5Z82MZ5UV-zXQSID8RKqEWFxYkEOOjoE9Mnshu-jyv5b98DP2MMMWAkt4MbZlDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86534c54a.mp4?token=KXbn7yEi08GcpSwfyYBvpOx7Kxhc4tVHIUFF7QOx4DBwrm01JnFEmg7nehNzXXYCvuVjlq018LXUqBzxRqv-egDXe6D7OvmnTG5I_3rizTS7Txi2Vq6qZIbVUXp8LwtlIMc5aFoQJi-aKnIgwmSGyfS2UUkiDq4cNNzZm3D9vFM5wixXfm3UMOkrZ2rQQUEW3bsjlSjfQYBvlrYpcJqlHGEOC0vXxhRWJtl1LSj37NK0roSKmZX02DtRIo9kFHWarzh2_Cz2ivs54KVjIW4ufAT5Z82MZ5UV-zXQSID8RKqEWFxYkEOOjoE9Mnshu-jyv5b98DP2MMMWAkt4MbZlDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: برای عضویت در پیمان مکه دعوتنامه‌ای دریافت نکرده‌ایم اما برای گفت‌وگو با این کشورها دربارهٔ امنیت منطقه پیشنهادهایی مطرح شده
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/683876" target="_blank">📅 11:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683875">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940e004647.mp4?token=gG34oKx9z8d-YeibADuWrMvVUcW_v-mCb1cY73rQxsgxe1b-aqXivr0AMAfGpkGFdKKAxvxrXF5-P8v-o2NlZEB3DI56HZ6CNI7Mk9bnKtVZoZBJuhyh_IyPMZcl8eLzqiL6qOrZMhxQfk1tH6_G2MgpTQP_s2JCvZvzkoEkKyLpA8dQIEzcdGCJubRKFaeIqL4CpnJN0_Rwq3YuzdJzeMwOWcs--CsPRKrzAnj4uAtfu06s_ArJ49CLlOu1vFr5FffApu4JLw58ntlaV8aY1KiMGassygZd0alzPwxG2gslTpcKfERx-H89tlc8Mka0T7fCmHVI0kz2t7Lat1uvlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940e004647.mp4?token=gG34oKx9z8d-YeibADuWrMvVUcW_v-mCb1cY73rQxsgxe1b-aqXivr0AMAfGpkGFdKKAxvxrXF5-P8v-o2NlZEB3DI56HZ6CNI7Mk9bnKtVZoZBJuhyh_IyPMZcl8eLzqiL6qOrZMhxQfk1tH6_G2MgpTQP_s2JCvZvzkoEkKyLpA8dQIEzcdGCJubRKFaeIqL4CpnJN0_Rwq3YuzdJzeMwOWcs--CsPRKrzAnj4uAtfu06s_ArJ49CLlOu1vFr5FffApu4JLw58ntlaV8aY1KiMGassygZd0alzPwxG2gslTpcKfERx-H89tlc8Mka0T7fCmHVI0kz2t7Lat1uvlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای المیادین به نقل از یک منبع ایرانی: ایران دعوتنامه‌ای برای پیوستن به «توافق مکه» دریافت کرده و این موضوع در حال بررسی است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/683875" target="_blank">📅 11:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683872">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c354ca7c68.mp4?token=MWgBZniz-YeZ14UJRfEC8N4Qo7eDjcZ4JFoBgAOVzs4ZPDjB1qCTGTvJaYaArDBN6rOX8pAkB0EhRZ8jBh5vllsIrTkyP6f0T8T0hngiljZzO9hLxQFN1QT4OwiROoIhEEskjz2TvyjIvgytY7Nc8LeUrcd0IZOIPoCvNkw0T4dWwbfFS3mE7DJYMMIQvcEM6yi51EbqK_7cvAfMRb9tv8DgC1jQ6kZ0HW0ofCfgjvoxeHGPls_3xPAqflCVLsey5ikBtwN7T7RMesciM0yWVMNMSMee8GwKfdD8qpkDySk8haB0NIbLIPnNWK0pd5k2zTNpAVlOwycHgLhjCr08I6e3TyXCTB9IOYIThsVcRp1jPInpX1x9Y4S_ScOuawng4DRb7w81whKQ8V-AQESMWo8Qsg2CWrLL0S96yB465A14jB9FJ7Y8I0E79DhrB-fKYGS0JTeM7dZ6cQGcuMevSuHXDnXfQ1prg8k5GnUnr0yDX7SZoe2HGxwiYVrxIm74cZxNsxucRkGFgIAyWXT9Ci3xasOoGnAJRFKp5u8TtHxNS27L5Ahe80d0L-OAw8zFjJQhCoYTpdb5J9-k6kIIrBoO3dyLeCXXhrcIORqRLJgcdyYCcN1IJS3FdsdnDfG79wp8HgSbMNiQ6smtzmLkVAaPZhq4Ozj45QOb5KRidQ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c354ca7c68.mp4?token=MWgBZniz-YeZ14UJRfEC8N4Qo7eDjcZ4JFoBgAOVzs4ZPDjB1qCTGTvJaYaArDBN6rOX8pAkB0EhRZ8jBh5vllsIrTkyP6f0T8T0hngiljZzO9hLxQFN1QT4OwiROoIhEEskjz2TvyjIvgytY7Nc8LeUrcd0IZOIPoCvNkw0T4dWwbfFS3mE7DJYMMIQvcEM6yi51EbqK_7cvAfMRb9tv8DgC1jQ6kZ0HW0ofCfgjvoxeHGPls_3xPAqflCVLsey5ikBtwN7T7RMesciM0yWVMNMSMee8GwKfdD8qpkDySk8haB0NIbLIPnNWK0pd5k2zTNpAVlOwycHgLhjCr08I6e3TyXCTB9IOYIThsVcRp1jPInpX1x9Y4S_ScOuawng4DRb7w81whKQ8V-AQESMWo8Qsg2CWrLL0S96yB465A14jB9FJ7Y8I0E79DhrB-fKYGS0JTeM7dZ6cQGcuMevSuHXDnXfQ1prg8k5GnUnr0yDX7SZoe2HGxwiYVrxIm74cZxNsxucRkGFgIAyWXT9Ci3xasOoGnAJRFKp5u8TtHxNS27L5Ahe80d0L-OAw8zFjJQhCoYTpdb5J9-k6kIIrBoO3dyLeCXXhrcIORqRLJgcdyYCcN1IJS3FdsdnDfG79wp8HgSbMNiQ6smtzmLkVAaPZhq4Ozj45QOb5KRidQ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جلسه‌ای که رهبر انقلاب استاد راهنما بودند
🔹
این فیلم مربوط به دوران پیش از زعامت رهبری است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/683872" target="_blank">📅 10:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683871">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXTECrbQfzbmfDV5Azv7q8PIfiw-064SwR3Bu8Jk-XhlRW2-R76QE99oazjxuA2t14xV4UEe_Eo02XLyaRcdNTyN8IlFjcmkI521uhCTsh78crd6EVvD5hKXGC_OLO9QN-HFiV3oz6F7kEqfGTTqodXGEih4ZMmY5wa8tC0yh9C0pAu6q7zakx1rbq5CvGW-hdhDNXmPTu_K8QcciT6kEUiuJ_kfXLslhCsJ3fB0DjfHF6x7_B980tk28N4mbW8FQAQrUAJJdil7v7olOcCryHHt84zFUlRO-j8brgKEqy1vHKw15hbRZhbmNQsVvM5kr4eAJEOJznJm473bAwlOsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا: از سحرگاه امروز، گسترده‌ترین و بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد.
📲
‎
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/683871" target="_blank">📅 10:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683869">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81555e7b8.mp4?token=s0dDgS6ISfHphHNnyd4BsyVm1SUBLQngWqZvgGuO9ayaD_PlSyO_53R1-qFqwxdLexWdCDIcnK-l-H02jlr5vrUy8l0iZbUOVBgsADYm9x4jF-fjJQPnCGH6Coko0f5uejYRZzIBuG0p-AQG2P1QjV59qCa_7F07ugXBN80m8ZxVOK6UAJtFM23CexcuApd4cauCn1tUBGtn9rfSim2zEpgkREGVIOWRFMyAOPjJ8ktimAAYJuQkA1cTdIAm9MON8DylOAIj8-kkTs6EZKkq5YDI4ZQv9ACU01n65FXRJQnhjZo0qzUg-TGM_R4AQ-fBh0E-30ZhzPZj3C2jCIZxpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81555e7b8.mp4?token=s0dDgS6ISfHphHNnyd4BsyVm1SUBLQngWqZvgGuO9ayaD_PlSyO_53R1-qFqwxdLexWdCDIcnK-l-H02jlr5vrUy8l0iZbUOVBgsADYm9x4jF-fjJQPnCGH6Coko0f5uejYRZzIBuG0p-AQG2P1QjV59qCa_7F07ugXBN80m8ZxVOK6UAJtFM23CexcuApd4cauCn1tUBGtn9rfSim2zEpgkREGVIOWRFMyAOPjJ8ktimAAYJuQkA1cTdIAm9MON8DylOAIj8-kkTs6EZKkq5YDI4ZQv9ACU01n65FXRJQnhjZo0qzUg-TGM_R4AQ-fBh0E-30ZhzPZj3C2jCIZxpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از وضعیت عجیب ترافیک تهران و موتورسوارهایش!
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/683869" target="_blank">📅 10:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683868">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImvIZ0LpeQNG66FrmLEXfHyZeVtuQZlk2c_O5E-f4impzRR__NDvkDvuWpt5qcRcvd25iTekY9Stq0oHMIwICwmxPmvRipfw0tdXxnxL-xjRbSA8zIYKFYmoROcthv4CNXAZ012HASm2sECvadSHldpMEFah_trb6ni0VVNlrq1hPplLrwnv-aaGhhhESUfT05_WzfSVna3vZbgUO5XoRDbdNQ3YDi_kQMDtweoye50ODV2J1Dc4vKdkdBxWI1J3Nd8mzE0LmWI8JvhhyfyTIFg-NX7oRyWX-dxqC3k-feO61ntIqpST2HJFu7IVb2aaffT7NQnZk5DpvZ9qWt2AQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌ روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌ صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره
02191551808
در ارتباط باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/683868" target="_blank">📅 10:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683864">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a634c77154.mp4?token=NTBBjhbezU9wS2CuPD9HKcvvSfrdCAFHv8nv03xkZFfwisrQXkZskNczpym0E9YaD0CSdHoUI30P3FF9WtmhRxAEKxaLtFElzfjx3h2SNLy4arGOe5jfEJQdh88URrrvqhvG9uVLG_Eon4Wr9uSuHRH1k_ljHZsOD2FmIgGWdzHYPWaKov6KIdq8XNIwfT7p_bGgAxNBdQTHNu4f01iw6PMotZERnJMkFdUv3ynGP9rhljEhbP3Xmznz3j5urIctiu1Xw97khzdaltJ2-z74ux1z7LxGhyKFvFLEkGKAIJNq4IAYeRVOlgHmyb41UNFMicQTa2Zi2yQwVPxlD0ryhGrrr-Om26HkMUmHUg4anCOXfSmN7UMTdR4eWjb42ebViAiTFWVDiDazKfsn5UusKJEsg4mfAxGAJ9aeT07CQSOGEE4uo2DmuTPZMomYF0XUIXwXPm74Q8Dc0QakNSJajOvdz_ts2G9mfhBVXX5tsm6ufvfgRBJjLlN6KPVNX4cGPNL8WpNlRoiIg5MKy4A7C-2bME4q-CfJMNKFBU8-D-Xgse6K_cyc28mQeZeHT9IbdGnaLC0D-CTLLSurLPKvBW2BMF8iw7GzrWeYxwjQJaQxX7agivS-C2ipNxSR5l8xDmgj5zOoD5kJ_PLPBvGmhCYOy19uIHp2CTGSY2D5jFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a634c77154.mp4?token=NTBBjhbezU9wS2CuPD9HKcvvSfrdCAFHv8nv03xkZFfwisrQXkZskNczpym0E9YaD0CSdHoUI30P3FF9WtmhRxAEKxaLtFElzfjx3h2SNLy4arGOe5jfEJQdh88URrrvqhvG9uVLG_Eon4Wr9uSuHRH1k_ljHZsOD2FmIgGWdzHYPWaKov6KIdq8XNIwfT7p_bGgAxNBdQTHNu4f01iw6PMotZERnJMkFdUv3ynGP9rhljEhbP3Xmznz3j5urIctiu1Xw97khzdaltJ2-z74ux1z7LxGhyKFvFLEkGKAIJNq4IAYeRVOlgHmyb41UNFMicQTa2Zi2yQwVPxlD0ryhGrrr-Om26HkMUmHUg4anCOXfSmN7UMTdR4eWjb42ebViAiTFWVDiDazKfsn5UusKJEsg4mfAxGAJ9aeT07CQSOGEE4uo2DmuTPZMomYF0XUIXwXPm74Q8Dc0QakNSJajOvdz_ts2G9mfhBVXX5tsm6ufvfgRBJjLlN6KPVNX4cGPNL8WpNlRoiIg5MKy4A7C-2bME4q-CfJMNKFBU8-D-Xgse6K_cyc28mQeZeHT9IbdGnaLC0D-CTLLSurLPKvBW2BMF8iw7GzrWeYxwjQJaQxX7agivS-C2ipNxSR5l8xDmgj5zOoD5kJ_PLPBvGmhCYOy19uIHp2CTGSY2D5jFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کوکی شکلاتی بروانی رو در  کمترین زمان ممکن درستش کن
🍪
مواد لازم :
🔹
کره ذوب شده ۱۰۰ گرم
🔹
تخم مرغ ۱ عدد
🔹
پودر قند ۲/۳ پیمانه
🔹
وانیل ۱ قاشق چای‌خوری
🔹
آرد ۲ پیمانه
🔹
بکینگ پودر ۱قاشق مربا خوری
🔹
پودر کاکائو ۳ قاشق غذاخوری
🔹
لایه شکلاتی ۵۰ گرم شکلات سکه ای شیری…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/683864" target="_blank">📅 10:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683863">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CminvTVBWkWpCv9Eo3_jOw_cp-uNtqIchEVjkLiCpyMD353OYwrn0jlbSm-C22mDcEC1LEnODHlTMA2-3wNe-wUodZoU22FW6v04me3cClUhO2_QXkc96ZYIYBzc1DZeBKmGTTVt2tzbONFt4A28jHG1152VA_-PCBvolpbSHFHaFVy706zf9edmmxhzrM-naD9eeFOgfKIvZWJjWedxYNGUeOWAp2CrKkQfQbzXX9V_-M7tpJFaoeW2iGX6RZZwVNZ9uPe6pZcc2psbMEoA3XVuITnlb7rVxlQjZawyS1RJG6X6wLsI9SqtN9HvXzcIT7XhpJTEgMGeTRBJxCFLmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت معاملات آتی طلا برای اولین بار از تاریخ ۱۴ مه، از مرز ۴۷۰۰ دلار به ازای هر اونس عبور کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/683863" target="_blank">📅 10:07 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

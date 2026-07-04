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
<img src="https://cdn4.telesco.pe/file/D_LKKWV7a9LL7VQdBcI-CRi0Xpl6zVcC4pni9CbKcYhlQtc3IGbh0uYZuUcKvASv-GwqjZvsD0GYeBiWPmu8bunj-a-AMZykpLbSbb3kzsM6KIylkTwVZ2lVt84gyC5setlLn3IJLqhFbad0PhyjHQcRlqjjhXvq4RCnEYVRPv7UInQ6MWHmqklUtalB0wnvX70FVI9_-QTcLCsRcihMpf-lt72bV8_6YjOWb9_CtTSMEVL6mw8-LbN-8FnXzoM9eUCi8KkfSvE2OVM1nEjRmlEwCrgt-KrDkKhrS6VLViS4fklY5Cy2GL-sPRy75Lj6MX8cAU3EV_hxFWLsflyk3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.26M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 17:36:18</div>
<hr>

<div class="tg-post" id="msg-666448">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: بانک‌ها اقساط و جریمه‌های بی‌دلیل را باید به مردم برگردانند
جعفر قادری، عضو کمیسیون اقتصادی مجلس در
#گفتگو
با خبرفوری:
🔹
از مدیرعامل بانک‌هایی که دچار اختلال شدند،  توضیحاتی خواسته‌ایم و جلساتی هم می‌گذاریم تا تعیین تکلیف کنیم و مشکلات حل شود و تذکر دهیم تا فکری کنند.
🔹
مسائل و موضوعاتی که مردم در ارتباط با پرداخت قسط و اعمال جریمه ناشی از اختلال بانک‌ها داشته‌اند را صحبت کردیم تا بانک‌ها جبران کنند و مشکلی در بازپرداخت‌شان پیش نیاید و مردم حق دارند و نباید تاوان مشکلات پیش آمده را بدهند.
🔹
قاعدتا بانک‌ها باید جریمه‌ پرداختی که بابت اختلال سیستم‌های خودشان، بی‌دلیل از مردم گرفتند را پس دهند و ضررهایی که متوجه مردم شده را به شکلی جبران کنند.
‌
🔹
این اتفاقات، پدیده قابل دفاعی نیست و اگر تمهیدات لازم به موقع اندیشیده و اصلاح می‌شد، این اتفاقات نمی‌افتاد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/akhbarefori/666448" target="_blank">📅 17:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666447">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfPaJeBFyEN43-Y0C5gC9oS5fTekk-IICinIKmL_CwwVQdkcP182x0BvqzCtY_ATQOD5OqLFQ7GJW2XdPPObwxn8_cVcapwZn4uCtbeh5F1sOUYvzRfS9QfRiF7TZb-NE7yj_cffxKgzmIRdjaIRwmw5h_JmlhzAbGI9YSaHk8itedzUW6b8wowOtinJgzatR1bw2Z2eDvSSbrXzDbyhS66atoWVBE8hPP8gP9I0iMjzYwKnykDdJg7RJeH9_jUc6y7-x5LRzhEaPTaAzLP6cFyZOjFjvNXHymFZSc_q4zuAoRPBiMdyNwnexArpOIne0qVFF9hDSjUpWRDyVsiupA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر مچ‌بند سرخ، یک عهد است
🔹
عهدی برای فراموش نکردن خون شهیدان و ایستادگی در برابر ظلم.
🔹
در مراسم تشییع، با مچ‌بندهای سرخ کنار هم خواهیم ایستاد. #مچ‌بند_سرخ
🔹
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/akhbarefori/666447" target="_blank">📅 17:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666446">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyyNvI4DpGXHTnNgxayD--VF01MgL17VCFMpVx0vDSWCUb6ImMNLgkufvc_VVHiFUsibDsUBrSJTohC0OLfFloUD832s4n6ZDryKAM6XYJ1mp1BkETN9WDbZyPiklahbuu0rxkAHDq_RSdZxZTZ25knX14Oj9QIQjX8VL3wn990vy2jvi-lZeYo605SIVGs8M0Mxg5H1OihGYktM5iTxD0K-bA0sShXBFJ6Ik7PVOXQ1oRHdCqkrLEPAMzdE31frojrunTLpkXoo30L8XDnFajnSwi_MW0nM0ansVK0q61DypIHMv-fDaCuHYHegzlaRW70pV-BVQe5CV1rCi8HGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قاب به‌یاد ماندنی از مراسم ودای آقای شهید ایران در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/akhbarefori/666446" target="_blank">📅 17:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666445">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a701b5bc37.mp4?token=QAUuWTeO0tM8Li-6YHsD_lZ1ZTfudh1UVya5buPvfLp0drZ9PDKEb-jJRWcRAcaPVs8_0EsHrAI-NErT-zz5Y8Pey8IprPosE07-Hn1hK_BKkUwtabgu95qGf63KZwO_-hnvzuRkHBRFnH0yvRwC0lZUozSWkqxWp_ol-Z_XIb_rb0QTLlfHDVQasdFVErleSJRKwRUp6rKiied4kmH79loRX4tJRSDoela3-tgIt-r2MoZ5wQuTErhI1YPxBfLtIyDPwAaWqQRvOLvYyDR1uYKOi84XXD96M2_H2tPVuhYn9dEKFvV49lE8YS6BBgsM_fq-moiKw2Y_dV3I5ZXeCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a701b5bc37.mp4?token=QAUuWTeO0tM8Li-6YHsD_lZ1ZTfudh1UVya5buPvfLp0drZ9PDKEb-jJRWcRAcaPVs8_0EsHrAI-NErT-zz5Y8Pey8IprPosE07-Hn1hK_BKkUwtabgu95qGf63KZwO_-hnvzuRkHBRFnH0yvRwC0lZUozSWkqxWp_ol-Z_XIb_rb0QTLlfHDVQasdFVErleSJRKwRUp6rKiied4kmH79loRX4tJRSDoela3-tgIt-r2MoZ5wQuTErhI1YPxBfLtIyDPwAaWqQRvOLvYyDR1uYKOi84XXD96M2_H2tPVuhYn9dEKFvV49lE8YS6BBgsM_fq-moiKw2Y_dV3I5ZXeCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیش‌بینی CNN؛ تشییعی که می‌تواند بزرگ‌ترین مراسم تاریخ معاصر ایران باشد!
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/666445" target="_blank">📅 17:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666444">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
الحدث: دور جدیدی از مذاکرات بین آمریکا و ایران در پاکستان، در تاریخ ۱۱ جولای شنبه هفته بعد برگزار خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/666444" target="_blank">📅 17:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666443">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5te4cDGG-kH_vwmq_axM5RNcM-3ef7CDnSRlEdXIhqVvS_Am5hq-JBoFNHCt0stri8jhBScTvsemh3DClaY5LflVdMJSHornv9DXIOrXKbqTxTxHDGrbwvHuilJMKX2WKY0VVU9yb8UKtkEBe0T5dou9lC-pgZ9T7flECIHrY85oiGRmFbhnNmXsV-HypDee5hr1PDwfcqNILFscvaLdGscdfCGSvnLSAHB01eQcSz6xjW9iC0PCULep9rTzeS7TJsRT_GeY5my2twMPGqbLHWUFisc3sOz6RH4HclFhBPwIYuhHJzR7cFKhXQGrld9kq1dQwQyI5jGIOHVdPIhYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لغو سفر وزیر صهیونیست به نیویورک از ترس بازداشت
هاآرتص:
🔹
وزیر امنیت داخلی اسرائیل، سفر برنامه‌ریزی‌شدهٔ خود به نیویورک برای شرکت در اجلاس رؤسای پلیس سازمان ملل را پس از اعلام برگزاری اعتراضات و درخواست گروه‌های حقوق بشری برای تحقیق و بازداشت او لغو کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/akhbarefori/666443" target="_blank">📅 17:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666442">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77cb53eb67.mp4?token=YW_BC9yTGgHE9Id4pxB85zj1AIJQ2l6KV8PUbmxMYmg1QneTI0RPJkFbrsZg6XG02HlB6sQruCxXFxG0tt3XpEXkBnac9HTH0nsoogMLzzqnA9sk2d965Nn6AWG5oDh-hWaQrzGE7n_WEN1d30g3Vw_5tznOF-ZvZd2_CeVbimSFJsSVFbMbDdgyIi1gAyLJN2Uk4NPfp28O4eVOApPXv8Xgn5bC_EWcVznpWGzh5ozFhyPrsxSKyjvMmWzfGJLpR3fgiJlZr2pZuPD28zYm5mGcpSFYYdsoBL4ScJ_glc91eXdQy0e8PnOw0aHuYQwiXXCxbI6voUSZhq71JNiBqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77cb53eb67.mp4?token=YW_BC9yTGgHE9Id4pxB85zj1AIJQ2l6KV8PUbmxMYmg1QneTI0RPJkFbrsZg6XG02HlB6sQruCxXFxG0tt3XpEXkBnac9HTH0nsoogMLzzqnA9sk2d965Nn6AWG5oDh-hWaQrzGE7n_WEN1d30g3Vw_5tznOF-ZvZd2_CeVbimSFJsSVFbMbDdgyIi1gAyLJN2Uk4NPfp28O4eVOApPXv8Xgn5bC_EWcVznpWGzh5ozFhyPrsxSKyjvMmWzfGJLpR3fgiJlZr2pZuPD28zYm5mGcpSFYYdsoBL4ScJ_glc91eXdQy0e8PnOw0aHuYQwiXXCxbI6voUSZhq71JNiBqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقام خون رهبر شهیدمان چه شد؟
🔹
پلاکارد حمل شده توسط جمعی از مردم که در حال حرکت به سوی مصلای امام خمینی هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/666442" target="_blank">📅 17:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666441">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
دودَمۀ میثم مطیعی برای خون‌خواهی رهبر شهید: انتقامی مانده است
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/666441" target="_blank">📅 17:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666440">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT5pefCEvvyulAZPqQThF4IpVqpGj8TJQOhSMjkZrISQMsZSAI0pncwjFSJZCGiYu1iqAVU3IZIX8WcG5IhxSAZBiidPDgisxygkrRHe32TEKvjDQQ6nhCCnbXL7I69fIklgQBlOOjibZrgx9OPoLgWq7YrHYnJcYrhJKiNXpUOKbs8Npwp-UOZG9xrHhDZtC2ER0GjrkBMu0ido41j-y-CeR8lznTAqwPwPsn5CMzeYboT0vpNYeZHHwxc57lEKCQra9EiY2cv_e46FAHWrruGRFnoVg_Aq2ToyUlSNnVGQuP28u3mBtWodpmanewpQ5A2i01QM417L6GUhNAwBvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله جدید رژیم صهیونیستی به غزه
🔹
منابع فلسطینی از حمله جدید رژیم صهیونیستی به غزه و شهید و زخمی شدن شماری بر اثر آن خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/666440" target="_blank">📅 17:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666439">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5954bb030e.mp4?token=OBvLtfHKwCNDyJ_3zr8ptPso3ctAJNC2ItD-Rh9oCHcem45-UKXY_LGPL61cxGIMInPWvVpK4qDMynqAKc4QAr-n1YpVAD3f5v4EwOVR24RiFwmZf7xb6iEBeeRxQHHzvT6HxYSqVAJ9gMmQpy9LIZHGiANA3x_GZiC1mt0jI9LOZ7gc6zz_wBPh9GIsOY8WjMADmuEt0gBTPlq4K87YLPtnFgqq_QK1qXD1Cd49qgVIOMlpWf4OdnnAPwZphjBt3D-nnoYIUEIa1F5um6cJi3wTHNgkFmR-LzJoCkGvGtooLGj4zMSF9I601QICxzHa6EzhMlW0MJBeVSNWFgB35w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5954bb030e.mp4?token=OBvLtfHKwCNDyJ_3zr8ptPso3ctAJNC2ItD-Rh9oCHcem45-UKXY_LGPL61cxGIMInPWvVpK4qDMynqAKc4QAr-n1YpVAD3f5v4EwOVR24RiFwmZf7xb6iEBeeRxQHHzvT6HxYSqVAJ9gMmQpy9LIZHGiANA3x_GZiC1mt0jI9LOZ7gc6zz_wBPh9GIsOY8WjMADmuEt0gBTPlq4K87YLPtnFgqq_QK1qXD1Cd49qgVIOMlpWf4OdnnAPwZphjBt3D-nnoYIUEIa1F5um6cJi3wTHNgkFmR-LzJoCkGvGtooLGj4zMSF9I601QICxzHa6EzhMlW0MJBeVSNWFgB35w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار حسن‌زاده: قطعا تشییع پیکر رهبر شهید به‌طور زمینی انجام خواهد شد
🔹
مراسم وداع با پیکر رهبر شهید انقلاب تا ساعت ۲۰ روز یکشنبه ۱۴ تیر پیش‌بینی شده است.
🔹
از ساعت ۲۱ امشب تا نماز صبح ویژه برنامۀ وداع در مصلی برگزار می‌شود
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666439" target="_blank">📅 17:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666438">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwSjG-NM2Dkhc1dPWgij4g-LKd0hl_rlcw2XHb5YcxMaq3JWPIK1imI7FkvlflmfsCrW3rmO1WZHLgK-pgsOVPApZ0cfcE6030P3r0NvAwK30P_PH4OpLvRXyxEzzFeJhXeKLgwr3fbIeBYQGb0cCzGUcTmHK0w9wnX8xypP5zf4EaUW0wYtyyEqPj-jGgrneZdnRnjDAyodSS3SdUcrYMaLxPEcji4rLIgSifV7SQ2fPxsRwi-NUL4jF_DfN8fPsUhW0wWzDUTO-U_x1POu2jQbyC0iH2jLaysd__D5FL7SjHP--pmVtyrId3vNjmEakYrLu3yBp887hLt9ozLJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه جمهوری اسلامی ایران به مناسبت وداع با رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666438" target="_blank">📅 16:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666437">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGl34owTrIALePKlWVjZLkeEx7Ay3dVFKbgbbklx7oyBbv_j7cnRRtSZHZTbJaSX40mveqpIL-zLkR2ZWeFrsk6Zj6v2X7SEXKe4FK7wc5g5z4G3rOckPt5U0paATWIC0C2kFDds1aUutzeVAPsFyTfQguimxH-Nqcrex-ACSiC9ISRBZjwG2maG_tkthO50l4LR7XOh4hIXGagDpnhH1wSVo7H46eQYU9hxEGw2w-vval3Ueo-8_eb32thxih4MK0PhjjwILuN5FmIfmB2_f17JUgnemYLEGtn5l5UUWr7JGf-AGRN3K14Yt2FgHGawiqf7CJJd8zkc7-7RJ8JKZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه بریتانیایی گاردین، با تیرِ
«
جمعیت انبوه در آغاز مراسم شش‌روزه تشییع رهبر پیشین ایران
»، نوشت: «
پیش‌بینی می‌شود تا ۳۰ میلیون نفر در مراسم تشییع شرکت کنند.
»
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666437" target="_blank">📅 16:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666436">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87f90c0973.mp4?token=vW-ik5vkPTMqNQFb2B8RXCGtOhVx2HghpMjBDTT45iU5HoTpY2XzDwu0dSpQCX71FM7h5N4RItpPcBzWd-RlJyaddDkqSM_ZJeGsyv7yyOYdHi-5sX2MzI7QlQzkdFRoAqHzQrOLw4i3CJ2fw-ukQo8Vg6a3wEdxTvzqDUa2Fa9PA6pRr991RDFjr9qKEERj5Ggns2FEeDbo2_S4ir8AY-rCO4gAho0Ro6kLyfC_QyJoa7r69hUhq9FGjDkUoOfAwJCZrtkSRTXw9iT6sIVLsV3gUy1JYtP9bwbhEBxgaeY1AXcSyVs9QOUQyMVnxWzgu1-5tWXvDgNazDD20v-KMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87f90c0973.mp4?token=vW-ik5vkPTMqNQFb2B8RXCGtOhVx2HghpMjBDTT45iU5HoTpY2XzDwu0dSpQCX71FM7h5N4RItpPcBzWd-RlJyaddDkqSM_ZJeGsyv7yyOYdHi-5sX2MzI7QlQzkdFRoAqHzQrOLw4i3CJ2fw-ukQo8Vg6a3wEdxTvzqDUa2Fa9PA6pRr991RDFjr9qKEERj5Ggns2FEeDbo2_S4ir8AY-rCO4gAho0Ro6kLyfC_QyJoa7r69hUhq9FGjDkUoOfAwJCZrtkSRTXw9iT6sIVLsV3gUy1JYtP9bwbhEBxgaeY1AXcSyVs9QOUQyMVnxWzgu1-5tWXvDgNazDD20v-KMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت اعداد از مراسم تشییع رهبر شهید
#بدرقه_یار
@Tv_Fori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666436" target="_blank">📅 16:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666435">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGUTw_OHvjESNBvLkI8k6lJ-jnAsrPexHN6PIcB_K4em5yqD8Ozf21b5q7HeKom4dwQunh0g5v4SjOLSJL8Xzh3QenoIoe5el16b0aV-ISg0eZ1k6DM3FL4-MFDzJ0VJWPgIVojrOKs_cwLymnVy7GZhyx19kSJ3ywFgsP4PaO8Nt-s4ACFYlSZirSK-wPXgA-9hhSW6kAan0WTNWRwYFwqCULsajXmvxUvJhtNL7V_5iddTNaCYPWN-pJWKBwj6vwB0dRfQRQC1twS8J4LOseosxOy_kLwkWLkORs8APwGOMUd81nWKQHdSEM6elURgbRkgwQVsUC1kNvXnkVH0Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناو هواپیمابر فرانسه به پایگاه خود بازمی‌گردد
🔹
رئیس‌جمهور فرانسه اعلام کرد: در پی تحولات «مثبت» در مناسبات میان ایران و ایالات متحده آمریکا، ناو هواپیمابر «شارل دوگل» از منطقه خاورمیانه خارج و به محل استقرار اصلی خود باز خواهد گشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666435" target="_blank">📅 16:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666434">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ای رهبر شهیدم؛ عهد می‌بندم که راهت را ادامه می‌دهم
مصاحبه خبرفوری با زائرانی که از راه دور خود را به مراسم رسانده‌اند:
🔹
ای رهبر شهیدم؛ راهت را ادامه می‌دهیم؛ ما برای تشییع نیامدیم، برای انتقام آمدیم؛ عهد می‌بندیم که اسرائیل را نابود کنیم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666434" target="_blank">📅 16:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666433">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bQ0a3zaYawWNHtvvpG2fLcMo_edvGjoq0zIOkUoTHH8nJkDkTfEoEP8rpmvXuw7_sf8iA6BEM3ETbtah5ySjcL3bVZdyH-1TkxCBBJlPLbF9j4jonbpNWvdGZhDhTPhFDBkq8evHn4P8azSW5ZTUhkNcDRNiZcE7wenHlR7AgrNEbGtCRVIvVfODk6fCeC9lBUoK3q0A5R00AfqrKzQC_Zi20sAQWn04JlkrW5Sk9CLEFSTQu5QQ5FCMAp3xS4T3I8aAiE_q-7i46KNKpcsmZWOjKx7-zufF95BZJfVvRje_45mJCJuuBe9JiyDLsLPYz2SSoOFE6I_zw24pekZsWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چهره ممتاز حکمرانان تاریخ ایران
🔹
این کرسی سابقه جلوس کسی را دارا  است که بعد از بیش از ۶۰ سال مجاهدت در راه خدا و گذشتن از انواع لذائذ و راحتیها، به گوهری تابناک و چهره‌ای ممتاز نه فقط در عصر حاضر بلکه در طول تاریخ حکمرانان این کشور بدل شده است. ۲۱/اسفند/۱۴۰۴
🔹
مراسم وداع در مصلای امام خمینی(ره):
شنبه ۱۳ تیر ماه و یک شنبه ۱۴ تیرماه
🔹
مراسم تشییع تهران:
از ساعت ۶ صبح دوشنبه ۱۵ تیرماه
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666433" target="_blank">📅 16:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666432">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rblu02G90-0PMVt-K4S-5dYOVIMFX3XwugvL4O3yIVAk7KGCetF8kXf3ca6jrZ9gPI5D-qs7aK09AENG5GOtFpiiMVQgdk2MrBG6jy6-mXphXqAXyF7Wp0G_EJupSn4wMxpAUcpT4f0MRsxfdBjrmnDkChcBlcQ8whz4GMCSbx0FCWzI-8linur0TaHT_0wHj5ivO_KNUiiU52j19So2NFZjo9k7mhJTPzCPvNMBf13TYKJMqdxwAXMyG1T_E3NvmqLWGu1rYK4hg7YMkSrKY7nNLS91We29KtX0ngNzXavGqOy8joxTPpSdpjexV4aim-2kIoYojhQ22-p3-lWilw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ با ایران برای آمریکا گران تمام شد
مرکز مطالعات راهبردی و بین‌المللی آمریکا:
🔹
هزینه عملیات نظامی علیه ایران بین ۳۴ تا ۴۲ میلیارد دلار بوده که از برآوردهای اولیه بیشتر است.
🔹
در صورت عدم تأمین این هزینه‌ها، ممکن است آمریکا با کمبود بودجه عملیاتی مواجه شود و در بودجه‌های ۲۰۲۶ و ۲۰۲۷ نیز رقمی برای این جنگ در نظر گرفته نشده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666432" target="_blank">📅 16:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666431">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
اگر در مراسم وداع و تشییع وسیله‌ای پیدا کردید، این کار را انجام دهید
شرکت پست:
🔹
افرادی که در مراسم وداع و تشییع رهبر شهید وسیله‌ای پیدا می‌کنند آن را به صندوق پست یا دفاتر پستی تحویل دهند تا به صاحبش بازگردانده شود. همچنین افراد می‌توانند با سامانه «پست‌یافته» اقلام گمشده خود را پیگیری کنند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666431" target="_blank">📅 16:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666426">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
زارعی: جنایت دشمن نسبت به رهبر شهید باید در صحنه بین‌المللی پاسخ داده شود
سعدالله زارعی، کارشناس سیاسی:
🔹
باید در ادبیات جهانی جا بیندازیم که شهادت یک شخصیت عظیم‌الشأن مذهبی توسط یک دولت و قبول مسئولیتش یک جرم عادی نیست و این یک جنایت بی‌نظیر است.
🔹
باید سازوکار عملی ایجاد کنیم تا این جنایت در صحنه بین‌المللی پاسخ داده شود و ابتکارات عملی برای اقدام در کنار ادبیات‌سازی دنبال شود تا برای اجرای حکم قصاص بستری فراهم کند.
🔹
شهادت آیت‌الله خامنه‌ای یک اتفاق نادر در هزار سال گذشته است، زیرا هیچ‌گاه یک مرجع تقلید در جایگاه برجسته خود توسط یک دولت خارجی به شهادت نرسیده بود و این موضوع باعث شد مردم ایران با نگاهی جدید و فراتر از یک رویداد عادی به این اتفاق بنگرند.
🔹
اگر دشمن می‌دانست شهادت این مرجع چه تأثیر شگفتی به نفع ایران ایجاد می‌کند دست به این کار نمی‌زد و مردم این اتفاق را به عنوان یک واقعه عظیم تاریخی تلقی می‌کنند.
#خونخواهی
‏⁧
#هزینه_خواهید_داد
⁩
‏⁦
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666426" target="_blank">📅 16:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666425">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6262b313bb.mp4?token=IM_kbAsq-s7wvWn1Ct5YlJnMc-wYBAEnvMbf1kYDi2qQemtIuX587SrPhGFwPSN63pyhLk5U-fT1JvCax4jkjmCwlc1Sp3USVSfBpz9wYWDhy0qDY3v1vGLpr-ONTpvWThsXb9kdiUo2qafSUD1jtfZ5HSBp72bj1lwLFVKwXAUCifL5Q7Wl6Y2kLuijD5Q70kBgyhqCPqTxiQHGFl7oxohFoOe7Xncbk3CbBiN-5HB7U356Pt6Gt1SJDvJNBcy1klpSn7R9_Euxw3SChJD_ozHASNJZQ7QhKz0ds4YhJajRyvAzE0CGG1JVRjtcNvQ79GV3HwhA00r7BrQw2U4Pd4pEzKMIMysRR52gW_xJVxnaoiMDrwLnssYLPcHTFZdCoi1sentXTN-HIcEKyFtL_SsjB-P2g1anaOUGQ6tX2sTGUgzuagoSTbQ8AkEhWLPS5k46SMO75MS8UeIDKjKKcieg1bhTPtklX2Sh3UbL_A2zfWrYhvA4qT3mYxXLdm2Oj9sb4_AXAvlI7etmdfh0N4yGbLdb7XFTI09swKV4km7xkJV4XdpQX1DmS-GHwBILgVO6H_RapN5sFS1bpJbqAETkIYGsXoCfqywWhzOt7bxIaY78OJSuIrHoph-n4syyATZfDdwYF9EFITxI4LWMytD2G5oRKyiQtHLy8uHJ-mY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6262b313bb.mp4?token=IM_kbAsq-s7wvWn1Ct5YlJnMc-wYBAEnvMbf1kYDi2qQemtIuX587SrPhGFwPSN63pyhLk5U-fT1JvCax4jkjmCwlc1Sp3USVSfBpz9wYWDhy0qDY3v1vGLpr-ONTpvWThsXb9kdiUo2qafSUD1jtfZ5HSBp72bj1lwLFVKwXAUCifL5Q7Wl6Y2kLuijD5Q70kBgyhqCPqTxiQHGFl7oxohFoOe7Xncbk3CbBiN-5HB7U356Pt6Gt1SJDvJNBcy1klpSn7R9_Euxw3SChJD_ozHASNJZQ7QhKz0ds4YhJajRyvAzE0CGG1JVRjtcNvQ79GV3HwhA00r7BrQw2U4Pd4pEzKMIMysRR52gW_xJVxnaoiMDrwLnssYLPcHTFZdCoi1sentXTN-HIcEKyFtL_SsjB-P2g1anaOUGQ6tX2sTGUgzuagoSTbQ8AkEhWLPS5k46SMO75MS8UeIDKjKKcieg1bhTPtklX2Sh3UbL_A2zfWrYhvA4qT3mYxXLdm2Oj9sb4_AXAvlI7etmdfh0N4yGbLdb7XFTI09swKV4km7xkJV4XdpQX1DmS-GHwBILgVO6H_RapN5sFS1bpJbqAETkIYGsXoCfqywWhzOt7bxIaY78OJSuIrHoph-n4syyATZfDdwYF9EFITxI4LWMytD2G5oRKyiQtHLy8uHJ-mY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افتخار می‌کنم ایرانی‌ام؛ این حضور، رمز پیروزی و وحدت ماست
مصاحبه خبرفوری با زائر لرستانی که از راه دور خود را به مراسم رسانده:
🔹
رهبر ما هم مظلوم بود و هم مقتدر. ما راهش را با افتخار ادامه می‌دهیم و فرزندانمان را برای ایستادگی تربیت می‌کنیم. آقا، امیدواریم از ما راضی باشی و در قیامت شفاعت‌مان کنی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666425" target="_blank">📅 16:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666424">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
آیت‌الله جوادی آملی بر پیکر رهبر شهید نماز می‌خواند  کمیته اطلاع‌رسانی ستاد تشییع رهبر شهید انقلاب در قم:
🔹
مراسم نماز بر پیکر مطهر رهبر شهید انقلاب در شهر قم، توسط آیت‌الله جوادی ‌آملی اقامه خواهد شد. #بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666424" target="_blank">📅 16:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666419">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KeexwYNv4orSnvR7HQq-PlND-_ZnnFLD4fu1qREyJcRrc53rBSeUHf8OLR2X2P7sXpKtqvdKC5o4kYsT331hDzKdjABLMMoWeVEX_EWOu-mJ9FkX-o_si1u-g1JUwhTnFAzn8eAfsYpj2mvnJalicOlnplTfubuSTJLkwSIVZPZ0fVMQa7ZTuDmXvibMXgT8rEJfaQbt3fKDGxZCxpofKGOaeJ7s02PMXOcG2tV4z1h7e78-lsEWrd-FSS-L89AnRJf0LlAYpNXD57k90ISq8zPqNoRfaAFBYZo2jy9eRbouZa1NwpB16LDskbigyH_96iAli1XEX1OeMHzadIBMJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfOcwtaEUbLwkvXq7MT_RGWtgqCmqLREz8WcxY0jZfHlfcZVrg9H3k6TyRuIsA0U12iOnxwR-NKrrZkeh0PVFdqqWNj8BI9q_s-516sAhQMhi2DoGsbyLAKwDbdv9ayfKhBtcsxUFzDnKAT1SqwuHAF5sCc-XYB5PWWRTbV9iFYGikc-x56Uc7FjIFPo0u5oZkOHDhKKMi64uBI9MY_oRUCoPHgIgJ_2EuCyd_DabqYMOg1BLVRxJLFHV3at8Aohd5ubMa-dZ2KG2Fsy5B7pi_V6LY5D7SVvUm3bZ7Mgp0CatWVpULtgbmtGK2uIxMEo19MnVUJgB7qN5qBAlPpSDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_0UOgFFiPHPkKQqfC0q2C6xuNrQUrobNOKwvrcIt9tOyGNMY0LxoCWFb-HVF--jXlDLifIMRFqfc3wU2dnmrsSAhzJWf0jupeVlwWEiNp0AAxjZW5T0REav5P25JBlb5gYOIiiYi27XnxLU-aGYwwD0Y-sdWvkXH0ZGPmR-Gvk8ej5vEZkRXK2xyj7baROcja6am7-pTGtmrqrnQ5blLAIJy6ePwHRatau7Y-DDfMzA05e8JGzTrQwwFJBsDaVvGWTjwW2a2BV0yIbEU1RNmYWgkv4KGOobj1J2K7x2cXfnzeHYUgm8PKzecU0hmLighRtgggJ64LkDntUNWKdfNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xey4azBOdOTeVHZqghL_oLWLElUWrj8GY3gx_wnlg9VjcNhhTvCnLVcty2Jjgy5y-squDcSmuYrXGa8ORTHVNQ-rPrT6iLXPC-YoXIqVhw4MkPCvYNgoAHh6derjuDX9KCOBUl4powBkSydo4QEiOdkFabPrILV3W2cibI1_xRcIbPFnhtqXR8ss8YUTt1zhhXFfrw5raVbRz29-4YPwsE7kcDk1N21LIiCw2MTPnPH4IZBovVaL2aiV218CjjNGTF4PUnCljzZDv_rCoZ7rqasdme6o2mYPvsZZHSsqlliQvNkzKPTkzSYOD0c7FQGXT2xU8AzFMHfXSDJkx-3nxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/asgOGpZls0R86KlsfO93lBkpeaC-bDzFi2tQwiW3kFiK4JH9oV4avB3C6T2kEggC44u7EdhWrOntrEG4MjWVBcC95Ij9SqMXQW3EBn6X5yxTIb7D-NowSBp3brDex95rjKSSDW7oZAgoF6uxHL9zlyrbqfTyJC0veGCae_KVBbd1RtLYe_w2Ydz7Bo2y24RBzHojCCPPLgT_8txoaEpnCaUo8zfkoHz7aidjBnRsscQSGA7Cmdmwixsbq2WeErEk7UrCI8CXfkcrynAI8_SS5kSto-Lu6MbO_wSyrmW49Y8Mas1meCjhn_W9ELYLU696Pos9aiy4gJ7XOkL5-1aWMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیدار نمایندگان حزب الله لبنان  با سید عباس عراقچی وزیر امور خارجه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666419" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666418">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c4a85bf45.mp4?token=E7gebDEil8GVQ1IFIBY0nsVE4ObyjJQuFO8FU1B1rc-jwhO7cykt1kaFBdpnMPP744gFQDUGnkBiURGea6rL55PPLRMgN4dNQNMCwsLUHENv4ec74LrnQfhPoVeICtPW9AcbfUsvdAP4wfPQvFXg_NZ-vTMX_TU_fm8iPfA5CdX6uNtTM2h7zyrz4gbTym1YY6i7VakAexdKdrrO0v-GKBu2IYNd4sVR8hnLl9wrA1qjY-pn-mEvCNT-mZg0rZsRRwlonY1ixJljcnItDYe83Mt3lJRqq1IM2geVHDs9yqMUvNKBHS_Txvc1pfVYOxZSzawXbpRK99JPez_whu5UxZbhxTbryyoA9zEPPk0xmb1jho61MJFV0fVIev2xzk5swYfvbAGiipnaVL4yfr7bXoBemXoMYzQjMG7SwpMYb2o_-P6LuSgdAn8mo4I7eqPB_7Cei4yxBds-N7ZaimdiBmAcU-7XZwFmhDhFlNM0Lze5nWMprzmsULPOndvpuZamIGARzCOQjDOk7rat_R_q2B_vKyh_QZuXWdvwvdrJrVgoq-zKtfbsGR2oaMsMD_-hO0_YBGvFJLu5ZlfNHViYGCXob0j-bZ6tV5iEdMqjT1WoYWA9pD_J8-mNeqoyafii5-Fdyn0QKJrkRIPGxqtbU_rSWVUoEUAB7LLzYPuePVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c4a85bf45.mp4?token=E7gebDEil8GVQ1IFIBY0nsVE4ObyjJQuFO8FU1B1rc-jwhO7cykt1kaFBdpnMPP744gFQDUGnkBiURGea6rL55PPLRMgN4dNQNMCwsLUHENv4ec74LrnQfhPoVeICtPW9AcbfUsvdAP4wfPQvFXg_NZ-vTMX_TU_fm8iPfA5CdX6uNtTM2h7zyrz4gbTym1YY6i7VakAexdKdrrO0v-GKBu2IYNd4sVR8hnLl9wrA1qjY-pn-mEvCNT-mZg0rZsRRwlonY1ixJljcnItDYe83Mt3lJRqq1IM2geVHDs9yqMUvNKBHS_Txvc1pfVYOxZSzawXbpRK99JPez_whu5UxZbhxTbryyoA9zEPPk0xmb1jho61MJFV0fVIev2xzk5swYfvbAGiipnaVL4yfr7bXoBemXoMYzQjMG7SwpMYb2o_-P6LuSgdAn8mo4I7eqPB_7Cei4yxBds-N7ZaimdiBmAcU-7XZwFmhDhFlNM0Lze5nWMprzmsULPOndvpuZamIGARzCOQjDOk7rat_R_q2B_vKyh_QZuXWdvwvdrJrVgoq-zKtfbsGR2oaMsMD_-hO0_YBGvFJLu5ZlfNHViYGCXob0j-bZ6tV5iEdMqjT1WoYWA9pD_J8-mNeqoyafii5-Fdyn0QKJrkRIPGxqtbU_rSWVUoEUAB7LLzYPuePVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصاحبه خبرنگار خبرفوری با شرکت کننده چینی در مراسم وداع با رهبر شهید انقلاب: آنچه رسانه‌های غرب از ایران نشان می‌دهند با واقعیت فاصله دارد. ایران مردمی مهربان و خون‌گرم دارد و من برای درک این حقیقت از نزدیک اینجا هستم. ایران کشوری امن و صلح‌طلب است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666418" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666417">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqI_2-Kw33M95eV1FKiavemZ8PmO654HvHBvjp71tGdHdPhnpe84qmSfLiT3LBL7-rXPDLL9CAKZa5Ab803gEiL3wMAxPapRNXOaZGvUwNwokMObqdfqkc94Aa-JLeJpCunRvpAvWRZSiOD_xyLEgR6buR82L5nowzj9nJWlrA8xahjbAaZcFsG8Jz0akWjTFTbgxY7prtxHQoO-wQ57o01hcsCUstQHLZVce3U8URejh_DA9IHmewEtRpu2CCGHDr3vt__ZwxGS3wjbF8inTVqbYfti0iQD3kAe-2Oejrklb7N4rg1f1A13EHkVjYgnqgnGvsMlLeua5aQmdK9rTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای روزنامه ترکیه: آنکارا نگذاشت کردها قربانی درگیری ایران، آمریکا و اسرائیل شوند!
روزنامه صباح ترکیه:
🔹
آنکارا از طریق ابتکار ترکیه عاری از تروریسم، آنچه را که به عنوان یک فرآیند مبارزه با تروریسم داخلی آغاز شده بود، به یک استراتژی ثبات منطقه‌ای گسترده‌تر تبدیل کرد.
🔹
فراتر از مبارزه با تروریسم، به تقویت وحدت ارضی سوریه، کاهش خطر تشدید تنش‌های منطقه‌ای گسترده‌تر و جلوگیری از تبدیل شدن مردم کرد به قربانیان درگیری ایران-اسرائیل-آمریکا کمک کرد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666417" target="_blank">📅 16:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666416">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/890723cd8e.mp4?token=dNWZUTjvRMOd5itmYngi9Oth1a8tBDutJc4QLOrL4anTBZpddqgsAdPKgoFTPZ0QKQZmVvZQisDmiaJXDrr1yed0bZh3-9Qh7Uri56h1e_PNyMT0LtqCRIwD2QRh4twQ_8v96WhlvdVNOtjT8A4lsQHorewI1yzRuomXv9jpVOfBf0i46dQ_yfCMalh7PiQcZrHI4IPaVyto-3FOCebTFxip66Y93L6wytjwTyF89auuTrkVzV46LvXG8ShuvI4ewyMJ53nYWuM9Q_XCkbyOMuv9KlsdWXPpx6JbhKdI_yVW53XR8ONwQ3jWZWwm-V2gDiUu_QI9SoXLuJS3xLuXuqGOg-GiCyw824BqTMy1lZGnVXRwECcl0Z4HWFajOk1lc-YAx7FX-zOaOAour8PvhW_Z1119mbyxRdvqfOttocW1puuZdPLmouZZElkMC-465Gmenw5l63E1Oa-L_OlnoY3nV9YqrjrA3nh3tfhFPtNEWMSKzLC4r7i6CwGvFkH7RXF9kOQTw1zGfDe-a1QKBrUy-UUz4pec2mVRPvxChAvlsexBrpXf88PgPnA676yybQaEnoxKYG1BjIIkyglK9mmJXemGI3lVn03U7cJPvXd7Gn4Jea0Ai2_dQWKCrEG0JPenHlF9wqInJwhFzebGko_Em8Tfaqbacg4peUMUA2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/890723cd8e.mp4?token=dNWZUTjvRMOd5itmYngi9Oth1a8tBDutJc4QLOrL4anTBZpddqgsAdPKgoFTPZ0QKQZmVvZQisDmiaJXDrr1yed0bZh3-9Qh7Uri56h1e_PNyMT0LtqCRIwD2QRh4twQ_8v96WhlvdVNOtjT8A4lsQHorewI1yzRuomXv9jpVOfBf0i46dQ_yfCMalh7PiQcZrHI4IPaVyto-3FOCebTFxip66Y93L6wytjwTyF89auuTrkVzV46LvXG8ShuvI4ewyMJ53nYWuM9Q_XCkbyOMuv9KlsdWXPpx6JbhKdI_yVW53XR8ONwQ3jWZWwm-V2gDiUu_QI9SoXLuJS3xLuXuqGOg-GiCyw824BqTMy1lZGnVXRwECcl0Z4HWFajOk1lc-YAx7FX-zOaOAour8PvhW_Z1119mbyxRdvqfOttocW1puuZdPLmouZZElkMC-465Gmenw5l63E1Oa-L_OlnoY3nV9YqrjrA3nh3tfhFPtNEWMSKzLC4r7i6CwGvFkH7RXF9kOQTw1zGfDe-a1QKBrUy-UUz4pec2mVRPvxChAvlsexBrpXf88PgPnA676yybQaEnoxKYG1BjIIkyglK9mmJXemGI3lVn03U7cJPvXd7Gn4Jea0Ai2_dQWKCrEG0JPenHlF9wqInJwhFzebGko_Em8Tfaqbacg4peUMUA2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقام؛ خواسته مردم در کلام مداحان
#خونخواهی
‏⁧
#هزینه_خواهید_داد
⁩
‏⁦
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666416" target="_blank">📅 16:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666415">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asD44U3eF5gDRhBnA_a0lMU1yMccIL1H0HLztUqJYYgdGQ3JqSm9RHHeEVF9sRBjlr3Ev5rizmGuax81fTHG036yhloRIqJX7yCRGFYfEo0i93tgg8JDIUx4TpksK3cO35AeYqc6caF4g4X6zBl0vU4GJpkQvxKZbJD4FxHFlBFhDY4mDhMyXFOUvCC-eUqSjzCG1U4S503B61GHBG8C63o6V3fXgDAGELpdzfEGiyxW5fiOvktK2r4mw-aodz05QNu8P4zjQ3haXaSM-0TjorSRvyzL7yfsPfZJJXGlsWg-c-9ffGgzDHuNnCjnpY8KvD4M3UWgpqezx8v1zgbFnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعداد فالوورهای شگفتی جام‌جهانی ۲۰۲۶ سر به فلک کشید!
🔹
وزینیا، دروازه‌بان کیپ‌ورد بعد از درخشش مقابل اسپانیا (۷ سیو و کلین‌شیت)، از ۵۰ هزار به ۱.۶ میلیون دنبال‌کننده در اینستاگرام رسید. #جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666415" target="_blank">📅 16:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666414">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رئیس اتحادیه لوازم یدکی: تمامی ارز مورد نیاز ایران‌خودرو پیش از جنگ تأمین شده بود
احمد حسینی، رئیس اتحادیه لوازم یدکی در
#گفتگو
با خبرفوری:
🔹
هفته گذشته ایران‌خودرو افزایش قیمت داشت؛ تمامی تخصیص ارز ایران‌خودرو از قبل انجام شده و ورقه‌های تولید بدنه را قبل از جنگ دریافت کرده است، اگر استدلال ایران‌خودرو برای افزایش قیمت، افزایش قیمت لوازم یدکی باشد، مورد قبول نیست.
🔹
جنگ از حالت قبل خارج شده و از تب و تاب روانی کمبود لوازم یدکی کاسته شد، ولی کالاها تا از گمرک ترخیص شوند و واردات مواد اولیه صورت بگیرد و وارد چرخه عرضه شود، زمان می‌برد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666414" target="_blank">📅 16:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666406">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3SqLvM3OhJYQ0lWObj2xAsncSVYcJeJcf5qSwB4j3vJMdk758j6VmXBSNACYFRKeDLZ1Hkar-fSr8jBVmkjWmY--ds-7A6-QNn40S0FeKCxGCYp_Twc71frRFCfr4F82ys_hmCSFFhMBJdP4-ah12ufFSeXasErA4x5qGrbrXrLcfn5nIkxI-Sgj_Qqgvaxl8E97UqULM4vUGiju7_Vu4Zg1Ca2X3BXBMZxOl30g7asd9SDcVK5dLVO_qTqlUvLCUAvT9alRilB6p2soGS8PWPyV1zTx_5X8dGgMDmqwp2ioE3322lbYU_zFgHZlkmmZxagieeESEtxYHIrkNk8Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C1v9ZE2ULMK_aJEaKmj6yACi5AvzdxOvysWWx8axKDgZWM0hMaj_r_tQyRZ-fX8eIIJmANmxCKlKqduQiHr0V1-rT_O1mmD6IHDk3nYc5J5d03FjxmbLiu5ib7_I4yP6vzQ4T2ywI91PkcpYOBz1RYCUd2xqeOAYtbYo2cCB4uyjs-55XO6ivmJXmuS9e5ozc2lwtrMYRFDptMgO3okTIKMvYWYpSSe5HDChUJPisH9Hqo4K2WOBMKT3j20UEwYj7X6fYsiMoDhP15v3RCrptj0aR2qw6yrh2pDEwMknM16uRcDd8DSXjgAMv_WlM_F_qs71wCjD0Y-kDrP5Khy3Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsdOq5TmiBZbirDt8Qpay40pAHqe_Ykj98QHIvDggHnk0Nu3CC5JswX9n6KI9jCQS_qEQF-YlA6-J9sYk_NLKdbnx3iHpKq578c1VoXQASimZEJ9P48Za84O8jW9ZhbTwlBlBEFpCcYRZGrJYDcMJ2HNvuBaQ20m0MWhuJGUrpwztTcvzDC-NM9N7eb5iFsjB9JiQ29qWq3CtfG1otLM7SAHqipXHIXlflRO5TXQks-ZGv4gH3s9BIvXVloS9Y6gBBRq-LCGK4bqJfhUWsroWqSszyRWtdYv58enj7GQDxfNo6112QI8EhjuMaQ3kXGFUS_p0TiBu7xWgzDfrrlKzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kXuAwfCWmd5gXz8c8GF5tLc35URqjG-Idm_m7nmrPefFTOQ0oD6cYZo0kOjDBR1--B_Gv9VIy1ZhxtI2ZdJr3kfFxkNIJLXO085nBAmGygtwUO3AcatEjPomNAw05xTe8najm6CJiEjH2Bfi2_psetYpnBPGsx5E5TrHofNCzFwrjAh4LuNajcFMSKf8wqFdwa0mKC-Z_c6XUjEV1qh1vnzGeVXi0AimfRCyXGN-Qe0ElSUC4ufC800FDRE5E9jtK1QeTozK-8jtGRct4HaNCw4xTUYmUWErj4VddQejBeLKuETTH5cKpSL7v_ZZmgTuEP2Sw4V30aj1t1-R4eAVnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7AIKqSBbSatxaYLOSvglBE9o6h_9MazLFvtaGfE6mJRfH_TER8fvBdKDSBzdrKQQQkotZboJSZ46tXYAH2DGjm2sSYrwmRP4bF5668iRaftXD05ZxBksYEWV0m-Y5ndbka4rqVglCct6DEVHqy_fWuN2wt3EJByRgPD6hKOlxSp69THuD19hz5qvTdMcPL6E5aYRVJYmUQIgh4NttLoryKlb-oFhrT8gSxX-OcS1pS0cbVmByAJqVlFGM7Geya-WntYBO2tm3XgRv-oYCyqxW-0leA0bAyrFa0WiyyVBOmZsbQYX64jeUAo2lt_ZigFJD7RnKyjZYkEoWc_9EzqGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUp1xntGnYef-8m_KqogQpHT4ytn0l9Yxo9DjzVxKID8WmkGqLVT0yWMQYgGo4LRN7cbyVUNP5hDPt_LFCkV63WKcgL6BFalpLaWRKolmTAmiI38P0HvLf8bbnfkSr-ia0xH20DKQlPO56ud9rYTKl5SbZMU1wdt1-l_edW51Dr7b-mLBTTSMmL5l0DKas3VpsM-rRbhzprk93u6ntSQ1EixTBD4sJD9k9qHsd4OQRW3h8ImYLxiBcRGgGgRLDIU_PUt7rG6fFyvTBe2EbWUZdJvg3rt5zDyudvAjskVvrcIOSN8ge_GBYFZuEfrLNf8Uo4htHuouj_0T8ptZZw61A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t7emOltZSotD_CQ1cmdjE4OjOugalPOH4jn0_6LvjC8m2V0PvayWjxcR_bf8omg2UYHWMVecdYS_dA0TRMpnF19JMBkkGAK5QHY4Z_QYBzP6PQc599r4VS5qp4tBjP18C8_uXMUBk0aOGj043uvQIkViPBOWkoGOX0eSbC1HIUWUx1QS7CZeCgQCyCcLoytied7We-EIiNRaBru0bF3tUMvIp4_54Nine92w2qTYcQ0MQYIeSzlMFRWkfYJBRCuzGhNIv0lcMEMJfBwiVHB9BFrJhvinbaEM82HgihCQRFN-_F58k31B5id0nueGVeZ4sMTkuOGNj65KgrTXAAirjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jHyjuf9gsqj07AN6WpH-tN9UurIocM7w2vqSA6E1-iXSlz4CTM7XIwF0TdLSBb8C9grjmXtEnCHIdKkp1Eb9ihjTt3xWCmsmQL-dbPEkpzPotzJbKUWbX3CM4h7KQPPciym9NusKQNJxodhABNhRNRaqB13TQE2c5EFivjdhv6-ZAegpI1Z_QkYK2gx-u5a5TuzpUCv_YGvzc7q9mVlnMI4AwayivOs74xXvcNN3v_NevfqTDGCQok-wN5vb7IMr82kCq411_nHXwK3kOPwPLmuCOtDQoelZ_gWK8HQegptpDIxZJKDZ80VzUzondY-5L7z4FHzjYqa7nLTziafUXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چه چیز‌هایی از پول به کودکان‌مون در هر مرحله سنی یاد بدیم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/666406" target="_blank">📅 16:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666405">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c24226f40.mp4?token=uA231JPqUbcGlUcZOX-z9gA-clv1443IQv2VHKBz0ahXbRUEqKbu-OkZ8Z6C0O6frir-7XodwwnfvbSye0z46R292me9xdktrBTHUJe_5ocKUediogWi-9kVezVoop439uwa9k0nsvuEi0iwb-W1YMxbPRU_-lDY4P7znmBtzPWIDW0q_VaM-Udfa8xX-M0zxJIHJXdnvAmlrxtg6JKzraxoz0Z0aHMyJp-zUUpy9yepMf2BVA-yFHvYHoEl347lNr4WL5xddnmNx1nDLpW1mMF6B81ZDfvA9zdBvSsCeS02rNi_35rpdOGmp0jvcFOzj7JWi0ULZCWpUifO56aojAR13ZMu40ZcuiBKNGkJypHf0K2tjSHuipTg1L9242mNj9fbNI7ZsnGYZesyOGGORhup4BASJwVZHZKoUd1lDOmIYu7-MSkcyo5ul3tyMbLmR8YgWY9gfuDxuddbV77TBA0FAOoF_BOUelw0wHUKW-oXIV91Fp1ZxXeEnUuKj5DjA1iLSbudDwGIMTwHf2skR94yHBew4D70OB2Zx-8am0Iw1nNIgFCcotFIjUCtgCoTbIEeWnaOqdlXAsIZGWUQNpsR1cVBwjEHtUfclJwjklTpOtvd5tbQxcZk0K6WZP3iMZa6QqYvbK-xTtn6dFV07JrQS5R4_Z8aMk2V3e2xGEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c24226f40.mp4?token=uA231JPqUbcGlUcZOX-z9gA-clv1443IQv2VHKBz0ahXbRUEqKbu-OkZ8Z6C0O6frir-7XodwwnfvbSye0z46R292me9xdktrBTHUJe_5ocKUediogWi-9kVezVoop439uwa9k0nsvuEi0iwb-W1YMxbPRU_-lDY4P7znmBtzPWIDW0q_VaM-Udfa8xX-M0zxJIHJXdnvAmlrxtg6JKzraxoz0Z0aHMyJp-zUUpy9yepMf2BVA-yFHvYHoEl347lNr4WL5xddnmNx1nDLpW1mMF6B81ZDfvA9zdBvSsCeS02rNi_35rpdOGmp0jvcFOzj7JWi0ULZCWpUifO56aojAR13ZMu40ZcuiBKNGkJypHf0K2tjSHuipTg1L9242mNj9fbNI7ZsnGYZesyOGGORhup4BASJwVZHZKoUd1lDOmIYu7-MSkcyo5ul3tyMbLmR8YgWY9gfuDxuddbV77TBA0FAOoF_BOUelw0wHUKW-oXIV91Fp1ZxXeEnUuKj5DjA1iLSbudDwGIMTwHf2skR94yHBew4D70OB2Zx-8am0Iw1nNIgFCcotFIjUCtgCoTbIEeWnaOqdlXAsIZGWUQNpsR1cVBwjEHtUfclJwjklTpOtvd5tbQxcZk0K6WZP3iMZa6QqYvbK-xTtn6dFV07JrQS5R4_Z8aMk2V3e2xGEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یک مهمان خارجی از مراسم تشییع رهبر
🔹
بخدا قسم تاکنون چنین امنیتی را به این شکل ندیدم و مردم ایران واقعا با غریبه‌ها مهمان‌نوازند!
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666405" target="_blank">📅 16:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666404">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبرفوری
pinned «
♦️
ایران یکشنبه تعطیل شد
🔹
هیئت دولت پس از درخواستهای متعدد از استانهای مختلف کشور برای فراهم شدن امکان حضور مردم در مراسم وداع و تشییع قائد عظیم الشان انقلاب اسلامی و با هدف تسهیل و امکان حضور گسترده اقشار مختلف مردم در آیینهای سوگواری، روز یکشنبه ۱۴ تیرماه…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/666404" target="_blank">📅 16:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666402">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ایران یکشنبه تعطیل شد
🔹
هیئت دولت پس از درخواستهای متعدد از استانهای مختلف کشور برای فراهم شدن امکان حضور مردم در مراسم وداع و تشییع قائد عظیم الشان انقلاب اسلامی و با هدف تسهیل و امکان حضور گسترده اقشار مختلف مردم در آیینهای سوگواری، روز یکشنبه ۱۴ تیرماه را به عنوان تعطیلی رسمی در سراسر کشور اعلام نمود.
🔹
این تصمیم پس از درخواست‌های متعدد از استانهای مختلف کشور برای فراهم شدن امکان حضور مردم در مراسم وداع و تشییع پیکر مطهر رهبر فقید انقلاب اسلامی اتخاذ گردید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666402" target="_blank">📅 16:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666401">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EomuwoiFl28sGNncjHpqiv5FwC7zpF5AG1OTmcJVRnjkXPwJELp3H_PMVhAbGfQ4FKH9t-7lWp_2PKESbzUCWtJIfUzVPn2LoBh--nsa-sj9owQlYleqeU16m68n8hrsSagAYHamR4-ZKjWt4uvCNzNXGoVodJW6nFfxetG5q9m-TSZ_6J_nAQJ94z5P88Sl79ubCg5yszMY6KpzuZ2oZcHIel0j2c30N3aLnfCIxbYa1bdTUd0CuBFrsSMur1VMLnpX1SFJ1FmS1gLnycD3cVIkYgZMg4tSXiaUXTZYQgto8oeGcon4LgdCfBm6KjqzB-YhLmK9yoAIas-aAxMWrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خون‌خواهی؛ آرمان مشترک میلیون‌ها آزادی‌خواه / جهان برای تروریست‌ها ناامن می‌شود: درسی که ایران به تاریخ خواهد داد / سرنوشت ترامپ و نتانیاهو چه خواهد شد؟
🔹
همزمان با آغاز مراسم وداع با پیکر مطهر رهبر شهید انقلاب، میلیونها عزادار در سرتاسر کشورمان فریاد خون‌خواهی سرمی‌دهند.
نظر شما چیست؟ گزارش خبرفوری را اینجا بخوانید و کامنت بگذارید
👇
khabarfoori.com/fa/tiny/news-3227630</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/666401" target="_blank">📅 16:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666400">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
نماز بر پیکر رهبر شهید توسط کدام یکی از مراجع تقلید اقامه خواهد شد؟
🔹
نماز در تهران توسط آیت‌الله سبحانی
🔹
نماز در قم توسط آیت‌الله مکارم شیرازی
🔹
نماز در مشهد توسط آیت‌الله نوری همدانی #بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666400" target="_blank">📅 16:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666399">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
بانک مرکزی فقط ۲۰ درصد تقاضای بانک‌ها را تامین کرد
🔹
بانک مرکزی برای دومین هفته متوالی، تنها ۷۰ هزار میلیارد تومان از ۳۶۰ هزار میلیارد تومان تقاضای نقدینگی بانک‌ها را تأمین کرد.
🔹
اقدامی که نشان می‌دهد سیاست‌گذار پولی همچنان از تزریق منابع با نرخ‌های ۲۳ تا ۲۴ درصدی بازار بین‌بانکی خودداری می‌کند.
🔹
این در حالی است که نرخ سود اوراق دولتی به حدود ۳۹ درصد رسیده و شکاف میان نرخ‌های رسمی و واقعیت بازار همچنان پابرجاست./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666399" target="_blank">📅 16:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666398">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
عبدالمجید الحوثی، از رهبران جنبش انصارالله یمن: هنگام عزیمت هیئت، فرودگاه در محاصره بود و جنگنده‌های سعودی و اسرائیلی بر فراز آن پرواز می‌کردند تا مانع فرود یا پرواز هواپیمای ایرانی شوند
🔹
یمن در برابر آمریکا و اسرائیل تسلیم نخواهد شد و «شهادت» را مایه عزت و پیروزی می‌داند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/666398" target="_blank">📅 16:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666397">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ze_nwxl5l_QT8KIANn5JqG-2k-OtwDvMm57J2eu1AJSV2tPgPjdD6uFi2PhPq_3lnog7IgvgDAg-125Vqo5LX4ua7rnpmEnFNU6bpHp3vBMbKDevDvajVZbOg5AwLeJJ_vaAzBwMpYiFZTeBKrtUW6vEqG1t6fzVQXsv2L6HxvMdxM7Su15quFaBqfLiSSAW-6x6lCxElTuLchm5kmKvSTJyyayVlOt6AWX5BWKyJRDu24eDAtQ6ene23D5dVodcDpcXcTCnq09fdUScybMP_p4-rhyTi0R4JwAOxs-sE4IHAEgtUeznZkpEe4THaUoelaNoHH_JynPLge26oGx01g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: ملت بزرگ ایران با قلب‌هایی مالامال از اندوه و اراده‌هایی آکنده از امید، ثابت خواهند کرد پرچمی که قائد شهید برای برافراشته ماندنش مجاهدت کرد بر زمین نخواهد ماند.
وَنُريدُ أَنْ نَمُنَّ عَلَى الَّذينَ اسْتُضْعِفُوا فِي الْأَرْضِ وَ نَجْعَلَهُمْ أَئِمَّةً وَنَجْعَلَهُمُ الْوَارثِينَ.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/666397" target="_blank">📅 16:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666396">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e7a4ba999.mp4?token=nFPo8Z3yat8ldvIAmUr9L2PG4XA1OSpyxReNtNDj90YoC8NE39biRVBTq-5uIz90tsWyafEM36Qj1JNQfzabADJLoSrLhl1mW9pFzYhqBOI7csPMoiZbWadXXc97dcv1MJcPNEcysTIO_p_wtDaauSfYiRpZFo7WeyxChy07Dj1fn9eOHe54JZbhy_tbwIVFkUJXc5qsqHMyjA57ZUWm7UWoErHQKIX7C11h3luYA_tLga8oSh6HLENLpPtzZx6zUTwAbULYsA3ykmgTaEBQsPZ4WmlOMaAXKH_VQMBPDAl6mZ-JWzF5tFeCF8ISdTbJbB7VW3wupz1JsE4lIKXU5rN5or-ZSNyIUFeFKqktZgsQhxOFkNe64mqrLykoJWxTkEZDfyLNNRZEQoZ04eTtqcrinYnaXktNAZGC4esB5HrTEvHFtwN8b0uoyKc7isdBGBaOF49U6r3ODXzlQJytwPf--Hnfk6EeRvRiFQiqd36vuKDuRNufy___pT8eYrwyNoxQR5RIHiMbs0wHsUu88vhsmygLh5bTTTnKbfkjviV1i2zUOom2Ww73OmG5DoUc-gk5tLUTYa8asihUf27NUBRv5_qdke-cQUjPhEB36hhnDAHFFLerfHW8HBZQlxEQcHOtmTiAL9nIb1XMdu7vzniQDZ9eEWWTBxycwig2QKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e7a4ba999.mp4?token=nFPo8Z3yat8ldvIAmUr9L2PG4XA1OSpyxReNtNDj90YoC8NE39biRVBTq-5uIz90tsWyafEM36Qj1JNQfzabADJLoSrLhl1mW9pFzYhqBOI7csPMoiZbWadXXc97dcv1MJcPNEcysTIO_p_wtDaauSfYiRpZFo7WeyxChy07Dj1fn9eOHe54JZbhy_tbwIVFkUJXc5qsqHMyjA57ZUWm7UWoErHQKIX7C11h3luYA_tLga8oSh6HLENLpPtzZx6zUTwAbULYsA3ykmgTaEBQsPZ4WmlOMaAXKH_VQMBPDAl6mZ-JWzF5tFeCF8ISdTbJbB7VW3wupz1JsE4lIKXU5rN5or-ZSNyIUFeFKqktZgsQhxOFkNe64mqrLykoJWxTkEZDfyLNNRZEQoZ04eTtqcrinYnaXktNAZGC4esB5HrTEvHFtwN8b0uoyKc7isdBGBaOF49U6r3ODXzlQJytwPf--Hnfk6EeRvRiFQiqd36vuKDuRNufy___pT8eYrwyNoxQR5RIHiMbs0wHsUu88vhsmygLh5bTTTnKbfkjviV1i2zUOom2Ww73OmG5DoUc-gk5tLUTYa8asihUf27NUBRv5_qdke-cQUjPhEB36hhnDAHFFLerfHW8HBZQlxEQcHOtmTiAL9nIb1XMdu7vzniQDZ9eEWWTBxycwig2QKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزا عزا است امروز
خامنه ای رهبر
پیش خداست امروز
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666396" target="_blank">📅 15:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666395">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82fbe4e3be.mp4?token=KksjzQlk1TU51T4n0MxEpZ64_5EqrT9uNBJMVl6fpXW-k1lGaiAtD4cUV7QaEaxjrXsS4_9LqHKABLZ0uavdDqNZh1M3UikreqrtNzjcgZWOKc2_WGqsNJhDrTkE2kB2bz5ni-BsXVCVogz_XivTcJxEI5MvIKjnTzT81p737sd4zBzFhpkqkoOlcMNRETripZLksi9qocPW5Bzas3JMEXwpC41-4iB6xcmir33C76RgNcanuDUbTOPceBamMSbUCuShsTOK-z9hNa1BEXd8HbNWhFHlRmLg7m8Q1U5oGk-TlUaUK5cK3hVCGVWmJdCrbNDE_ZGRp8u6WRfTntw8uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82fbe4e3be.mp4?token=KksjzQlk1TU51T4n0MxEpZ64_5EqrT9uNBJMVl6fpXW-k1lGaiAtD4cUV7QaEaxjrXsS4_9LqHKABLZ0uavdDqNZh1M3UikreqrtNzjcgZWOKc2_WGqsNJhDrTkE2kB2bz5ni-BsXVCVogz_XivTcJxEI5MvIKjnTzT81p737sd4zBzFhpkqkoOlcMNRETripZLksi9qocPW5Bzas3JMEXwpC41-4iB6xcmir33C76RgNcanuDUbTOPceBamMSbUCuShsTOK-z9hNa1BEXd8HbNWhFHlRmLg7m8Q1U5oGk-TlUaUK5cK3hVCGVWmJdCrbNDE_ZGRp8u6WRfTntw8uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز همای برای رهبر شهید خواند
🔹
نماهنگ «عشق دل‌افروز» با صدای «پرواز همای» در روزهای وداع و تشییع رهبر شهید منتشر شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666395" target="_blank">📅 15:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666394">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67b25c7636.mp4?token=SGVvxzmxnpRdqNlKVYPqH6JU1MjP5SouKQoyuinGuYZ-rbLaLqBxA_u-aqIl6IxxAzPFxHWPnaNljY3CY4cUyiKRk3zNfGyzn8Q1E9YWL-4w5Qi1TCiWUemZmYyLv_B33aud27Z_N04Keb-3mIgg9_dCzxTeGADjjVw1N0YsFCWLPVYrO98iyKxyTBNe72pEdvcokoyV9dpKaUjwiSEookwRtGWG7zgqdIQ2CfZUhLINZGKCDQwM3je4Dl87ukA4l3QqbDxytKBFQ8PQfvAAEMAoL-qMHi-EZMZrviQG4pbn_C9G7hAuBxBBk-WtK6mAKrCDB9iTu1F0m7Mjf08DoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67b25c7636.mp4?token=SGVvxzmxnpRdqNlKVYPqH6JU1MjP5SouKQoyuinGuYZ-rbLaLqBxA_u-aqIl6IxxAzPFxHWPnaNljY3CY4cUyiKRk3zNfGyzn8Q1E9YWL-4w5Qi1TCiWUemZmYyLv_B33aud27Z_N04Keb-3mIgg9_dCzxTeGADjjVw1N0YsFCWLPVYrO98iyKxyTBNe72pEdvcokoyV9dpKaUjwiSEookwRtGWG7zgqdIQ2CfZUhLINZGKCDQwM3je4Dl87ukA4l3QqbDxytKBFQ8PQfvAAEMAoL-qMHi-EZMZrviQG4pbn_C9G7hAuBxBBk-WtK6mAKrCDB9iTu1F0m7Mjf08DoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاعر عراقی: به کوری چشم بدخواهان، سراسر عراق با تمام وسعت و عظمتش به تو درود می‌فرستد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/666394" target="_blank">📅 15:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666393">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7ddc6fdf.mp4?token=alV7K_g_vnwg2qsIayh_Q4IsNIrn7htt_ilc-D8DWlKltinH4fzXLStZnLxDybpLD_sRy1CvVpibzzEAWOM12yokLhS-kMgn12ARpYKm0l8TeZPNJRQ03GtuI1Mhnic7cbPXLFYTrEk-ogCryvpKQfgLU-WLRwhCKSS6M4Ru2GocoORsD1WJbMPP3s40_sXMTRktAW-uaxTvUJ-FbEbhu55CJW3TBLT328EtWuuBd79-DMvhU3MxUyt3Vqf20DWY6vtiGtsQvFIMdjOzykOMGCqhGEysMJQTlnJhIbDSopSHUnXs6_HVo-GcSq21Or3WGP1QGAMcsuSMXKzfGq-4_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7ddc6fdf.mp4?token=alV7K_g_vnwg2qsIayh_Q4IsNIrn7htt_ilc-D8DWlKltinH4fzXLStZnLxDybpLD_sRy1CvVpibzzEAWOM12yokLhS-kMgn12ARpYKm0l8TeZPNJRQ03GtuI1Mhnic7cbPXLFYTrEk-ogCryvpKQfgLU-WLRwhCKSS6M4Ru2GocoORsD1WJbMPP3s40_sXMTRktAW-uaxTvUJ-FbEbhu55CJW3TBLT328EtWuuBd79-DMvhU3MxUyt3Vqf20DWY6vtiGtsQvFIMdjOzykOMGCqhGEysMJQTlnJhIbDSopSHUnXs6_HVo-GcSq21Or3WGP1QGAMcsuSMXKzfGq-4_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جکسون هینکل، چهره رسانه‌ای و اینفلوئنسر آمریکایی در حال توزیع شربت نذری در مصلی تهران
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666393" target="_blank">📅 15:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666391">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqZewV9lgPo5epJ0ahO28V6RT8eLyHAIbMLKFSZOeZOCmVfOtM0j0IAg1GQ6vLIiusdUdUoC8_TnToBLloor9u_-oIXSZv1Pd9VgMuBzZ0iAqhEbcA2DSCEM4f9RXo-yHxqcC6x9bXI72xiwMY7stU2CgHtM00tyMCBHzSUH2zAQxzO3VWxDlfheuOH5hsSv0oPJ--ux794keP8JsMOVu-RDq4ugPHYPB_2lqlhnFU-nNq7sUrz8Mmm_p2dQE45buOxvjEXId7ckH-Z2JxOOnt2K81Es9KSP6tpHtgGBsFMkGOqMtD8lX0PT4LoTFZHlBJaexOF_W0TImxpi-6rrMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کره‌جنوبی برای فتح هوش مصنوعی، هزار میلیارد دلار روی میز گذاشت
🔹
کره‌جنوبی از بزرگ‌ترین برنامه سرمایه‌گذاری تاریخ خود برای تبدیل شدن به قدرت اول هوش مصنوعی رونمایی کرد. بر اساس این طرح، نزدیک به یک تریلیون دلار در توسعه صنعت نیمه‌هادی، رباتیک و دیتاسنترها سرمایه‌گذاری خواهد شد.
🔹
در این پروژه، سامسونگ و SK Hynix بیش از ۵۱۳ میلیارد دلار سرمایه‌گذاری می‌کنند و چهار کارخانه جدید تولید تراشه حافظه در کره‌جنوبی می‌سازند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666391" target="_blank">📅 15:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666390">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUHMBYR3VazgKRGH5Bs6RnikgR-hl0EBywLxjxtMOM6mtXNJHNHXsKeBYnDawZOPWtTnZpvp_NWz_LoKF_B8r6sP555PeVKXBgtU4iGs1B76nKJYWdABlghXh6e0AZvwx3heSuZUuiP-i2ePZSZ8d-8Ifci45JgnA7tKfvUipyuszX_LjK74RzRr-4-70B-wxm24IqoTdwFX9_VAyFzpdFxneqfZxe_ersMzdQuHO_7Ydtoe9AJu5RePpn4tN7pA1D8N8Hd-PW7nBJnm3arUALJy7JEJSJJE8RcrV_qAtkmmOKPdIOhc2eriCUG_r1ENJKtglf7A4Et9XFBauumMmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بنر دیده شده در ورودی مصلی؛ انتقام خون امام شهیدمان چه شد؟
#خونخواهی
‏⁧
#هزینه_خواهید_داد
⁩
‏⁦
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/666390" target="_blank">📅 15:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666388">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b5f9c0d3.mp4?token=fVE84Do0fYLnugl9pdWp9A6qQE1x1YCrMyoDNByU2WoE9e2UJQDLhVpz-dbrMc9SxycfElg2ecpt5iH7G3viHXT7aWoPNKUxOp_JXPR1bunmwUIYHbRT9hXj1tL8k2KzaL0g97Nz8jJl2rMa77kuQR9QGDukRvjv4WsQOyTDalypaMG28C4yXZ_UGPCb6zvecVOedZBRghhQTy9HAySc6EgZzkNedGPrghKVpxb8TC0N1TUjldBUnut3iGcJ6OMcIWMR7z8Hur554yr1EexaFyaom3-pB18YTo4PPNs4eqgdfW41V5-A6-00fv6ZVkdw1mTU1i7wTLCgAy1fogGhCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b5f9c0d3.mp4?token=fVE84Do0fYLnugl9pdWp9A6qQE1x1YCrMyoDNByU2WoE9e2UJQDLhVpz-dbrMc9SxycfElg2ecpt5iH7G3viHXT7aWoPNKUxOp_JXPR1bunmwUIYHbRT9hXj1tL8k2KzaL0g97Nz8jJl2rMa77kuQR9QGDukRvjv4WsQOyTDalypaMG28C4yXZ_UGPCb6zvecVOedZBRghhQTy9HAySc6EgZzkNedGPrghKVpxb8TC0N1TUjldBUnut3iGcJ6OMcIWMR7z8Hur554yr1EexaFyaom3-pB18YTo4PPNs4eqgdfW41V5-A6-00fv6ZVkdw1mTU1i7wTLCgAy1fogGhCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باران دل‌نوشته‌ها در سوگ رهبر شهید
#بدرقه_یار
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/666388" target="_blank">📅 15:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666387">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_eiCo8iMXwRoWsnFIIOh9c3ccrxuY02hximxQ0gf1dkYat84S9aaLlAwjQx89Ru6Vup7ctSJB4qzsBp_aoi4ISuIOk8JqFCN5jckA02gzPi6h0gh7IeFMsEgOnO7tRYm0NHd9Z0gJ3FxCgoulF2-HSSjty_YcwGGzNfMQg_zV7kxox36_2gV7Hg1l280PaVOLps1NnweF9Ssqd9RS_j8wot3y7Dlka17n8coVdHk6vksyDyX7pK7AxGP5rrW2QXMMg6RBWJF3TSq2yJJDpxwPIMEGdQIXlpEItpgeggEoremVofKY2GlZG-XxOixkn8M9IFJLYbP-_Uw3D5jVsqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی فرمـانده جدید نیروی دریایی سپاه
🔹
این معرفی به طور رسمی انجام نشده است و در پیامی که روابط عمومی سپاه پاسداران منتشر کرده، سردار علی عظمایی به عنوان فرمانده نیروی دریایی سپاه معرفی شده است./خبرآنلاین
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666387" target="_blank">📅 15:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666386">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ویدیو ترجمه آیات قرآن که در حضور نمایندگان آنان قرائت شد
🔹
عربستان سعودی: آیه‌ای درباره دو ارتش که در جنگ بدر با یکدیگر روبرو می‌شوند، یکی پیامبر به همراه مومنان و دیگری مشرکان مکه
🔹
ترکیه: آیه‌ای که کسانی را که در راه خدا می‌جنگند، بر کسانی که نشسته‌اند، برتری می‌بخشد.
🔹
دولت لبنان: آیه‌ای درباره افرادی که در صورت درخواست، از انجام ایثار خودداری می‌کنند.
🔹
حزب الله: به آنها گفته شد ضعیف نشوید یا غمگین نشوید، شما برتر هستید.
🔹
حماس: آیه‌ای که مردانی را که عهد خود را با خدا وفا کردند، مورد تقدیر قرار می‌دهد، برخی از دنیا رفته‌اند، و برخی دیگر در انتظارند.
🔹
انصارالله یمن: آیه‌ای که به مومنانی که بدون سستی جنگیدند، ستایش می‌کند.
🔹
قطر: آیه‌ای درباره بخشش و لطف الهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666386" target="_blank">📅 15:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666385">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0c6c16c26f.mp4?token=P7TjtnA2506yMDPct-0Bb3eSycwxXQLM9jH__hybKzX0j8iVJ6sjK9tZ5DZoc4ytjJvBBm0qVZM9SPoebqFe38e0TMNko5WRidd3UhD7vIPLPat3nEb53-r3dk1zFHSdKyZS99BDGZIU1xqYe4HLDqsYnraHJwcqfECxi8xwVUKwvK4zPGCMxmu93HzrctoIUi086cFodXaXJeFmA6TDWZBg_ewMikQaLwM56JEWo7wycl2QRXAkukgu-f5kOmGpEgabnTcpcRB3ASZqYXLJDpwmGvf6uxJhgcuWlsDvtfCW7PLb40UXK6_6IntY1l02VhM1Um4FAhgl2S352MyziQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0c6c16c26f.mp4?token=P7TjtnA2506yMDPct-0Bb3eSycwxXQLM9jH__hybKzX0j8iVJ6sjK9tZ5DZoc4ytjJvBBm0qVZM9SPoebqFe38e0TMNko5WRidd3UhD7vIPLPat3nEb53-r3dk1zFHSdKyZS99BDGZIU1xqYe4HLDqsYnraHJwcqfECxi8xwVUKwvK4zPGCMxmu93HzrctoIUi086cFodXaXJeFmA6TDWZBg_ewMikQaLwM56JEWo7wycl2QRXAkukgu-f5kOmGpEgabnTcpcRB3ASZqYXLJDpwmGvf6uxJhgcuWlsDvtfCW7PLb40UXK6_6IntY1l02VhM1Um4FAhgl2S352MyziQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی دیگر از شدت سیلاب امروز در استانبول ترکیه/ تلاش برای نجات یک زن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666385" target="_blank">📅 15:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666384">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ec5RkxtV1RMNncVqVUqAFRFniYot8lLGtc2o0C25wToI5gGuMPYA3SKS3qHkCrubjgjxIIaN16G0aRWiiwVolaNCzZ8bPqyukeCO1Fi6qJyYoDDNeYlnsns8KkZzePyiPs3Q94TYtBY21gwZ3vqEqpVo_pB557t5LUz1SfHKaeaKRNSJ3nedQDvEUn_B8tqvocJBjJ85dv-cvtkPxbZ8H8yDcn5WBgk_juMSfxnVNRU3AEoac_K6fyjHfMhrjdpnIm6a-Ac0vFsKT0id0fgSrMEfx6YKK7Fj-5QCbmH0LpI56CfuEOSnejHmkcWNw-J5FzXeExnvaG6H3ANM6BjKGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اتهام جدید به ایران، این‌بار در کانادا
🔹
گزارش محرمانه‌ای در کانادا که به گلوبال نیوز رسیده ادعا می‌کند «احتمال واقعی» وجود دارد ایران پشت برخی حملات اخیر در این کشور باشد و از شبکه‌های جنایتکار محلی برای هدف قرار دادن جامعه یهودیان استفاده کرده باشد.
🔹
همچنین در این گزارش به احتمال نقش «عوامل هدایت‌شده توسط سرویس‌های اطلاعاتی ایران» در تهدید علیه جوامع و منافع اسرائیلی و ایرانی اشاره شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666384" target="_blank">📅 15:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666383">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نشست هماهنگی مراسم تشییع رهبر شهید در کربلا با حضور مقامات ایرانی و عراقی برگزار شد.
🔹
تردد کامیون‌ها در آزادراه قزوین-کرج به سمت تهران از ۱۱ تا ۱۹ تیر ممنوع شد.
🔹
نخست‌وزیر پاکستان: تأثیر عمیق رهبر شهید ایران بر این کشور و منطقه، نسل‌ها در یادها خواهد ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666383" target="_blank">📅 15:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666382">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXIvTptMWe1-weu343WDyREacrOhTB1aUKhvMKHourXeVJ6qISjm2eW_KD_9FgeXgArYQBHuJDf02_xavM5L9iiBw8EoKYbc-w7hU4AYAr1IoKdA1lYhzBkNOTwH-qKYmb5X4HfcREDtuXuEi8piVy-pS6cawuRh_wNazB96Asbat8oERV96guu_ZiIuxMLJ1J_2cNvt_E8xWlAVq2ETZudVh5O2JHR_wwf3hMPBHdCz2QwjjBWZj5ZkZQwj6GNhgK4uNPU0uJ9_cLxNJ_xENOocmaBOduMz0tzn4_qdixbiQFyElvzvYwSV7BRG2541H4a5-pE_fokAK8Umm52I5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
فراخوان خبرفوری برای مراسم تشییع رهبر شهید؛
«بدرقه یار»
▪️
مخاطبین عزیز خبرفوری، برای شرکت در فراخوان
«بدرقه یار»
کافیست از مراسم تشییع در شهرهای تهران، مشهد و قم عکس و فیلم تهیه کرده و برای ما ارسال کنید.
▪️
سوژه‌های پیشنهادی:
پرچم ایران
ثبت لحظات مراسم توسط مردم با تلفن همراه
حضور و شکوه جمعیت
فضای مراسم و جلوه‌های معنوی و حماسی تشییع
▪️
آثار خود را به آیدی زیر ارسال کنید
👇
#بدرقه_یار
@Badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666382" target="_blank">📅 15:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666381">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cdde19f0.mp4?token=ETR5heZIjEunTOTWSGakwPw7XDYJbwdrY3A-ytUNwdMXySbIcjNlkyMlvIrUUt_Ye0PAad-dbgSwI0W033NxRAw3rCGb_F0jDRR9o-FFfN-6fo6oC1nmiQnfKvzwRwGQcs4axTLPFPkyGwTOUiJy2wyFJYwW8xeaD5iXyQNuapRu90q2CKJsJxTkra9uqPY9Ip-LAldYulvvAJYZBGsFgqT0Cke8V2XKRaNJN0v08-fG9ID-Ckdp_sbHkFP8GRsmS44iX3Wxqt1F9i-iWHh4d1Y9Zd6kETK2VJ6dyHlJdnX77Ilz15Hoz6VdlBSCqcsV1XGQgqXCo4p9WIFqsogurA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cdde19f0.mp4?token=ETR5heZIjEunTOTWSGakwPw7XDYJbwdrY3A-ytUNwdMXySbIcjNlkyMlvIrUUt_Ye0PAad-dbgSwI0W033NxRAw3rCGb_F0jDRR9o-FFfN-6fo6oC1nmiQnfKvzwRwGQcs4axTLPFPkyGwTOUiJy2wyFJYwW8xeaD5iXyQNuapRu90q2CKJsJxTkra9uqPY9Ip-LAldYulvvAJYZBGsFgqT0Cke8V2XKRaNJN0v08-fG9ID-Ckdp_sbHkFP8GRsmS44iX3Wxqt1F9i-iWHh4d1Y9Zd6kETK2VJ6dyHlJdnX77Ilz15Hoz6VdlBSCqcsV1XGQgqXCo4p9WIFqsogurA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور زاینو اینفلوئنسر ایتالیایی با لباس تیم ملی فوتبال ایران در مراسم تشییع قائد شهید امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666381" target="_blank">📅 15:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666380">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWbw6K1DXVecPRbgEW8uxnNxWjdow1UFVOZPqT5-zKXl4iBW4tNP-oydt9HiBPuUG5hRKdaXX90-V_prTWQhmaQGvm-XaJZTG5rhG5ducOHXHop5n7zlPKQM5W4_evdkyuwqbKFzaF4UaU5Tgj_G83BFeTdxTiCcTk5AAiK6lo63vh8GYcPA7JTiTMBYId6oNhWAxV9d6N2jiWgZs6daFIgtc_Fi9a3g9x4hU_GSDzKwV04PeExrccatjCfq2sRIO_IZOovr0Z2Ba5r7q9ZqNQoXaiOFc1bN949e-Bc98Rc_SJyfuO2Pc9Yl-H1MUT046_6bZU_Lns-O9kNUzkND5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدمات ویژه
#بيمه_البرز
به زائران آیین وداع با رهبر شهید؛ از خدمات فرهنگی و پذیرایی تا تمهیدات ارزیابی و پرداخت خسارت
مدیرعامل بیمه البرز با اشاره به ابعاد گسترده حضور زائران در آیین تشییع رهبر شهید انقلاب، از ارائه خدمات همه‌جانبه این شرکت خبر داد. نیما نوراللهی اعلام کرد: بیمه البرز علاوه بر پوشش بیمه‌ای زائران در قالب کنسرسیوم صنعت بیمه، خدمات آنلاین ارزیابی و پرداخت خسارت خودرو را از طریق نرم افزار یاقوت البرز و واحدهای سیار مستقر در مسیرها ارائه می‌دهد. وی همچنین از برپایی موکب‌های فرهنگی و پذیرایی این شرکت در پایتخت جهت خدمت‌رسانی به عزاداران خبر داد.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5054</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666380" target="_blank">📅 15:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666379">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98297a097c.mp4?token=S8OweTtR1jQZNR6BQBJLdy7xxlQlf51kmR6uzm1mApvJD5aX69LVUJPWlj1F5lLAxLVcbusnS58KYVbXk5y02ElSkZ_q1SguI54Gf8kwPILrmxoUDUE4VS0Xj204KRZouRtiz6oEdGDZ0dIFq55a7ukr7wGBCBOw1d-HjDsMohD5_eEWNi_Ce0kzuFKc_c0Js69aAlW-GfxghHQlVFyTHCAMLB-ed9vR4n3A8oo_UxVD_mT6ELHz_pF7D3hK8Z9Jae-ixFp6NycpRmB-6lsPoe7Mh9Cs-RfqX2ip_JcOBsMhirlUOHgta8MEdqehVDUkPqrKzHpUL8Xhi2Nzn_VKJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98297a097c.mp4?token=S8OweTtR1jQZNR6BQBJLdy7xxlQlf51kmR6uzm1mApvJD5aX69LVUJPWlj1F5lLAxLVcbusnS58KYVbXk5y02ElSkZ_q1SguI54Gf8kwPILrmxoUDUE4VS0Xj204KRZouRtiz6oEdGDZ0dIFq55a7ukr7wGBCBOw1d-HjDsMohD5_eEWNi_Ce0kzuFKc_c0Js69aAlW-GfxghHQlVFyTHCAMLB-ed9vR4n3A8oo_UxVD_mT6ELHz_pF7D3hK8Z9Jae-ixFp6NycpRmB-6lsPoe7Mh9Cs-RfqX2ip_JcOBsMhirlUOHgta8MEdqehVDUkPqrKzHpUL8Xhi2Nzn_VKJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عصبانیت جاسوس موساد از تشییع تاریخی و باشکوه امام شهید ایران
منشه امیر
:
همه شرکت‌کنندگان در تشییع جانی و مزدور هستند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666379" target="_blank">📅 15:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666378">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43ebfac6e6.mp4?token=i-Hil59pncNxIccFafc9aKbvp0BvGvmzo06gN4eyaDe10XbmxfJiVTphovub5I9KPus7AFpTKctETgqLaaOjAU9UIuwEYYrCY9Uv4h44x8wKwqlrEbKWTxfQYzGGRvYV-p1XDEccLlafssARj-TgyT2XB3DdrvGKsXkVdAFlCwA3OtZvhJ8dHz221nLpQa0fTHm77SruqCOphBFErkADR0Rzx8b6noyaJ-zS5f8VQznxIq9qg9ckvZb2YrcitSWLdHeHU1X13sCktkNL7LbI25XFkyYrdI6t-RFolNjvfSdgVJv6Ok2qLt6P1REtQwvrZQExipEqf2QvnnZvi36egw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43ebfac6e6.mp4?token=i-Hil59pncNxIccFafc9aKbvp0BvGvmzo06gN4eyaDe10XbmxfJiVTphovub5I9KPus7AFpTKctETgqLaaOjAU9UIuwEYYrCY9Uv4h44x8wKwqlrEbKWTxfQYzGGRvYV-p1XDEccLlafssARj-TgyT2XB3DdrvGKsXkVdAFlCwA3OtZvhJ8dHz221nLpQa0fTHm77SruqCOphBFErkADR0Rzx8b6noyaJ-zS5f8VQznxIq9qg9ckvZb2YrcitSWLdHeHU1X13sCktkNL7LbI25XFkyYrdI6t-RFolNjvfSdgVJv6Ok2qLt6P1REtQwvrZQExipEqf2QvnnZvi36egw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طباخیان: شایسته است که این لحظات را غنیمت بشماریم و برای آخرین وداع با رهبر شهید حاضر شویم
🔹
برخی صحنه‌ها در زندگی تکرارناپذیر است و تشییع پیکر رهبر شهید یکی از این رویدادهاست.
🔹
امروز ایران بیش از همیشه لازم دارد که ما در صحنه باشیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666378" target="_blank">📅 15:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666377">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9XqOCpbgSBiUKosITQnnLBmcLCYVWfiX6ERhqyvw2eVfgg8X3qW-sBzfe2cB3VI43_lN47x1JDa0suQZR7n2L-NXMKwMDbDlZCQdIhZH0mC78l7WrjY1NLhVgIPC6_bu6SVmR4YHyAnRuhtHO8cd86ud51MUwIOWto1YsrIj6xFUa3RtnQo-p_6_dc1wGR1_rG6qgtmyLY4UTiPlAQ_IUvFd6_8ZIMeCvYxYU8mpER4DNsthj6XytL3_cQg0vEsJzlKMmyNsY9sPKA57e8OdYZHV1oti9-68vxsNp4xCO08YLpKy_LvsH8UQxwXbVC_a0pW3R-i-n5AzAtFyj-7zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بنگر چگونه دست تکان می‌دهم، گویی مرا برای وداع آفریده‌اند
🔹
پوستر جدید
KHAMENEI.IR
به مناسبت مراسم وداع مردم ایران عزیز با پیکر مطهر رهبر شهید انقلاب اسلامی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666377" target="_blank">📅 15:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666376">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a873ca257a.mp4?token=FjWkKl9OBEdUpRdh8_L4BXS-6kfffL71_KIvo9zmvzaZ-VzSPVrMqfl8qvDSQG_ExwTHnGsS-RjfJxVwI0C9jtpnSieKnEMARalNMlib7ExFMSQV7ifBZMC3DSPTc00EtOJP_QuQSd56DeZ_dvWgrDpRLhMGgcQDpPABORZExzn6h7SU5bErKH4cc_ynOQa1KW-P48uYgs5v5vz33YO9Yd7yr2L83RJYPe0EdQLzHWs7GwkA-etgf7Vg3d3xi_G11WsJSw4lD3TYuRSmfasD_1FP1NdkwdBEw08_SZjIwZNPPJ2EH0BQVWF2dZlTzQVwqlhsh7Ux_7kkBrtHyAx0qDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a873ca257a.mp4?token=FjWkKl9OBEdUpRdh8_L4BXS-6kfffL71_KIvo9zmvzaZ-VzSPVrMqfl8qvDSQG_ExwTHnGsS-RjfJxVwI0C9jtpnSieKnEMARalNMlib7ExFMSQV7ifBZMC3DSPTc00EtOJP_QuQSd56DeZ_dvWgrDpRLhMGgcQDpPABORZExzn6h7SU5bErKH4cc_ynOQa1KW-P48uYgs5v5vz33YO9Yd7yr2L83RJYPe0EdQLzHWs7GwkA-etgf7Vg3d3xi_G11WsJSw4lD3TYuRSmfasD_1FP1NdkwdBEw08_SZjIwZNPPJ2EH0BQVWF2dZlTzQVwqlhsh7Ux_7kkBrtHyAx0qDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط ایران؛ در مورد عبور و مرور کشتی‌ها و شناورها تصمیم‌گیرنده است
بهنام سعیدی، دبیر اول کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرنگار خبرفوری:
🔹
در رابطه با تنگه هرمز، هیچوقت به شرایط قبل برنمی‌گردیم و تنگه در اختیار جمهوری اسلامی ایران است. البته ایران و عمان میتوانند در پیرامون تنگه هرمز با یکدیگر همکاری کنند اما فقط ایران؛ در مورد عبور و مرور کشتی‌ها و شناورها تصمیم‌گیرنده است.
و الان تمام عبورومرورها با اجازه نیروهای مسلح ما هست
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666376" target="_blank">📅 15:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666375">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kB0WKldGfOtxAcwLNsojfTuez8CG4ibarwe_sp5GjLIB4dJFczGl8Ieokp9KzC6euzwekdp_nlN8bGDeu5jdxOmGLNWE5W5z8stn3l9krKuPj-A9j-gT3KBqjUpftuSLaLePFsE1yqBenR8O6qyzWbyjfgESp4DUr3XVTNpYhg-qTwPbVKpww4TpQc7089kMKnijTkJDfMdTiWe38D3_KbLC_0LrKaJDWWNUKy8hECAlduJI01Undzf1oYCIAIg0_enpDA-3QfrQEdeuBN1i4z-42bS_hZjWq-pBaDaxleg9iOCG3fbHMZEDYu78OfkzXekwOSv4jbgrOWOEXh2vAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غزل منتشرنشدۀ رهبر شهید انقلاب در وصف عروسشان، شهیده زهرا حداد عادل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666375" target="_blank">📅 15:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666374">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
رئیس پلیس راه راهور فراجا: جاده‌ها و آزادراه‌های تهران مشکلی ندارند. به دلیل برگزاری مراسم، برخی معابر تغییر جهت داده شده و رانندگان باید از مسیریاب استفاده کنند
🔹
توصیه شده از حمل‌ونقل عمومی استفاده شود و قبل از ورود به تهران سوخت‌گیری انجام شود تا از ازدحام و کمبود سوخت جلوگیری شود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666374" target="_blank">📅 15:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666373">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ایران؛ ابرقدرت چهارمی که مردمش بزرگترین مؤلفه قدرت آن هستند
بهنام سعیدی  دبیر اول کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرنگار خبرفوری:
🔹
تحلیلگران آمریکایی امروز ایران را به عنوان «ابرقدرت چهارم» جهان می‌شناسند که برتری‌اش نسبت به سایر ابرقدرت‌ها، حضور بی‌وقفه مردم در صحنه است. مردمی که بیش از ۱۲۰ شبانه‌روز برای حفظ دستاوردهای نظام در خیابان‌ها ایستاده‌اند.
🔹
این ملت همان ملتی است که شعار داد «خدایا از عمر ما بکاه و به عمر رهبرمان بیفزا»؛ حالا با همان عزم، پای بیعت با آرمان‌های رهبر شهیدشان ایستاده‌اند و اجازه نخواهند داد کوچک‌ترین خدشه‌ای به انقلاب وارد شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666373" target="_blank">📅 14:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666371">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b3cc359df.mp4?token=EuKe4SzA0Azvrv3q36hGvwz5Ld5DPRQgLIhx4sxVrg0NAm3KVtiQj_ACGCMyG0_XgE2yqs1-Vjnf0LoXAoStE6VPpN-KJiLRwmnzJ-Mjf4nmLt2A7GT-TrtOKwpeDhHZT46BurGo0L44hp0Y_6R8RPyMAuL1ZLjQgFutIU9aUf_Rgz3nwYzpYVF_Qr99WHMWLIX-Su65dAcQQ_UlHrGCJvRDuVaHqkTdi1cdWjLF_qra3zuHIdzekbty2xkSoXQGElAn48zc_40TKzR_i_ybMZJqqcrmpzGYoYQjKuhwO2lS5wT1Xz8dKKZ8BfImY1PxBrFa-CPHYA3TjTHe8CO_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b3cc359df.mp4?token=EuKe4SzA0Azvrv3q36hGvwz5Ld5DPRQgLIhx4sxVrg0NAm3KVtiQj_ACGCMyG0_XgE2yqs1-Vjnf0LoXAoStE6VPpN-KJiLRwmnzJ-Mjf4nmLt2A7GT-TrtOKwpeDhHZT46BurGo0L44hp0Y_6R8RPyMAuL1ZLjQgFutIU9aUf_Rgz3nwYzpYVF_Qr99WHMWLIX-Su65dAcQQ_UlHrGCJvRDuVaHqkTdi1cdWjLF_qra3zuHIdzekbty2xkSoXQGElAn48zc_40TKzR_i_ybMZJqqcrmpzGYoYQjKuhwO2lS5wT1Xz8dKKZ8BfImY1PxBrFa-CPHYA3TjTHe8CO_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین یکتا: شرکت در مراسم تشییع رهبر شهید انقلاب، اعلام بیعت با آیت‌الله سید مجتبی خامنه‌ای است.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666371" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666370">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
شرکت‌کننده نیجریه‌ای در مراسم وداع با رهبر شهید انقلاب: آیت‌الله خامنه‌ای فقط متعلق به مردم ایران نیست؛ متعلق به همه مردم آزادی‌خواه جهان است
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666370" target="_blank">📅 14:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666369">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca33fd1dc.mp4?token=mWGVfTaNogBYQrUBBJ-HX857KkrDlvIqwJxGAxsU-knUqQzEGEGBpgmlPqWTpVyQsmf0wty-8mbceJJEBnFTAjJGpYmY6u5uw2gtZldAkEKax6w0auTCtQufEkH4FW4pUwHdX6KzhtryAD_54azNpXDNFzIb6tTIKt8376B-a-wMpUBk6qEaXQhraGKFuLcKkv_tPZVcMrPGzAiFposxACUv_kMOa5-zWaO1VZvG4fF3Hd2F6RtERrpjmb5riRVIfTJ1TO7UGd6sdzQIK3QjVgA0VdvozgrnD4e7NJE193uHbPbSKMZ8hRCURXMUxjc3YSw3PEBZQEdoVq_-ZiMorzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca33fd1dc.mp4?token=mWGVfTaNogBYQrUBBJ-HX857KkrDlvIqwJxGAxsU-knUqQzEGEGBpgmlPqWTpVyQsmf0wty-8mbceJJEBnFTAjJGpYmY6u5uw2gtZldAkEKax6w0auTCtQufEkH4FW4pUwHdX6KzhtryAD_54azNpXDNFzIb6tTIKt8376B-a-wMpUBk6qEaXQhraGKFuLcKkv_tPZVcMrPGzAiFposxACUv_kMOa5-zWaO1VZvG4fF3Hd2F6RtERrpjmb5riRVIfTJ1TO7UGd6sdzQIK3QjVgA0VdvozgrnD4e7NJE193uHbPbSKMZ8hRCURXMUxjc3YSw3PEBZQEdoVq_-ZiMorzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید هادی خامنه‌ای، برادر رهبر شهید انقلاب: با عاملین ترور رهبر شهید باید برخورد لازم صورت گیرد‌‌؛ این مسأله ارتباطی با مذاکرات ندارد
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666369" target="_blank">📅 14:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666366">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Emj-CZdF7aeGBIoLFLMf9Ab2rEYXGVKcNScskcPKaAg1ganJtKxY3fV9-FguRH0_3lBmzbJHkf4kbMXjvpFl6_gsFiAXjzxQ0BUql8EMxD1Nn1BOrwL5oDjBrQeuy9H0alunGyeDxkxPfE5V7hqpF_-DztyvK4MzNUq3Az9bKq-1dnUb9W4NasJX-bNh6mq470SGyC44gL4jj6WnS9XG-Zbcnu1SnrCKFcOIpif5QP8Iw_Ykku1W6mp0BHRUhZJqKGXHkMUf2DD6N93DGLKxrhnbayfEY4bEFP3mYvx1dbcJv1I88nA72thEkC5h-4i-y_mEdXl3YrmL5mlaJ4sTgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gqFzZqk-JZ-LhtFKHnNvBr6jC8CYhnPidRqPd9SfksxFISEa2Nu0SfXakiopCZfGY9CWSQ_XY3Rzx5tglHUHYUJkKJQMQji_hJj9m3dEKjQxJBkJRxwfrzC6YcQ1RWj6VV3C54RzyQxlbLkHWed0j1wudBttyT0cpEnKom8aJESOzbx5pQSBO9b10P7dfqqCsbIFs-Cj2DrdW715CWUsSuRj7gAmE8Plk7Ieel0oY285HvyXRMCS_a7PCIFgQl_L7Jc5zD7MPYaez3sugSBlS--zuv_1C-vJSfDbu-kpOI6ogsfY0gZzPz_mr_yoQ2S99WAE1diUm7nZDJmBozaEAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8SC0DSbf1SHQmswqBI9JWQnKEuDS8rI3siJbCAhrzMJq8xDOXxQllKu_L4QloP0yVnQxaf1IxFQIb4Tg6IO3ieG-xZWJbvugW21aSMFnb-XijSBjHK7MZvhYSiRRMJ20O_G9w60xUHU7iBSVwKxHnQckJnIywJozJAEHl-13aOyean0eR-Mk9YkJw3mLkdGv3bEoF7Yh5aCkEUyrvFZDEWw-tBBZD57C1b7J_IMn5w_Zic4jhPTKAoQl544vxlI5vG3lnvALaSp7iz4wmv_99JOJom9C02jOOr3qceGJ5XwZivNCll9XEpg_Ew4rrXGdmTogL0Acqak9IjVP5GM-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جمله‌های ماندگار پوتین، کوفی‌عنان و کاندولیزا رایس درباره رهبر شهید ایران
#بدرقه_یار
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666366" target="_blank">📅 14:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666365">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29877906b.mp4?token=Dnp57LCRIkJA6_jJAZBrdVU1S2gTd83mx60NH4ALrvHAy0CJdXsp-22McE6oa_bfQdtJTwsg9L0bCilttzSMXksKWn4Xm15EppfSQYc1MxBdpAYXWy9p-34WShExw22GrhBHbJBRjyfd3NOKkTgFPMJYIszzIZPVxY-Yy1kSJHli2231Q8NLUQg6ZyrlytB2hWDr8oGsgiJyrNFNrtC6A6I-8C4IqhwPjY_SuQ3tJIwVFV4-Oe-4QE6eAoeamadxeoziibJrVRNn3TUq9bLsbdm7dH8rxQJGAGimT_UJXqd3clPYWb9XGfLByp0f6il-oENu-eCQe0e5y8KU6Ban0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29877906b.mp4?token=Dnp57LCRIkJA6_jJAZBrdVU1S2gTd83mx60NH4ALrvHAy0CJdXsp-22McE6oa_bfQdtJTwsg9L0bCilttzSMXksKWn4Xm15EppfSQYc1MxBdpAYXWy9p-34WShExw22GrhBHbJBRjyfd3NOKkTgFPMJYIszzIZPVxY-Yy1kSJHli2231Q8NLUQg6ZyrlytB2hWDr8oGsgiJyrNFNrtC6A6I-8C4IqhwPjY_SuQ3tJIwVFV4-Oe-4QE6eAoeamadxeoziibJrVRNn3TUq9bLsbdm7dH8rxQJGAGimT_UJXqd3clPYWb9XGfLByp0f6il-oENu-eCQe0e5y8KU6Ban0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال رسانه‌ای ساکن کانادا در برنامهٔ پرچمدار: پس‌از ۷ اکتبر هر بار رهبر شهید دربارهٔ فلسطین صحبت می‌کرد، در کانادا و کشورهای غربی سیل عظیمی از جوانان واکنش نشان می‌دادند و می‌گفتند «ایشان درست می‌گویند».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666365" target="_blank">📅 14:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666364">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
بنگر به قیام سرخ آن سرو رشید
با ظلم نکرد سازش آقای شهید
🔹
شعرخوانی محمود حبیبی‌کسبی در مراسم وداع با قائد شهید امت
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666364" target="_blank">📅 14:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666363">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4af6a52b9.mp4?token=S7Ppk94dbeBEtF_z8fYoHGyEWCQAfP_oEaBVIe95fMXbIIYfElTzrAvSWz65tB_emoVTGwbWJnuC0DJ-xJ9OTfGfI5dnS4a_QbTUM4g3xRc7oLndMInT-TUukvHQDaaKFLmje_IkGRLHmtFg4LyMJcIdN8ZqwRI_QV_ri5vUQXB1jPMv7V8hycJzuu9btske_kGlPVSx36w2fXJzoJVyQ5xcz3KnctWEBNd5Umh6Yj2Dnz5Rd6v9sOBEVllyx5_NsY7P3Di3YFmCZIuj-K4CKTiCgtWJIok0xoAbLrOhTDf29VABxwKTAoIGiGQhQLRCjl2orQZjuJhI-o89u_Z2CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4af6a52b9.mp4?token=S7Ppk94dbeBEtF_z8fYoHGyEWCQAfP_oEaBVIe95fMXbIIYfElTzrAvSWz65tB_emoVTGwbWJnuC0DJ-xJ9OTfGfI5dnS4a_QbTUM4g3xRc7oLndMInT-TUukvHQDaaKFLmje_IkGRLHmtFg4LyMJcIdN8ZqwRI_QV_ri5vUQXB1jPMv7V8hycJzuu9btske_kGlPVSx36w2fXJzoJVyQ5xcz3KnctWEBNd5Umh6Yj2Dnz5Rd6v9sOBEVllyx5_NsY7P3Di3YFmCZIuj-K4CKTiCgtWJIok0xoAbLrOhTDf29VABxwKTAoIGiGQhQLRCjl2orQZjuJhI-o89u_Z2CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت حامد شاکرنژاد از اولین دیدار با رهبر شهید انقلاب در ۸ سالگی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666363" target="_blank">📅 14:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666362">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
پلیس فتا: در مراسم تشییع، هوشیار باشید؛ به لینک‌ها و پیام‌های مشکوک اعتماد نکنید، هویت تماس‌گیرندگان را پیش از هرگونه واریز وجه یا ارائه اطلاعات بانکی بررسی کنید و اخبار را فقط از منابع معتبر دنبال کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/666362" target="_blank">📅 14:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666357">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDlpL-FkjW6pu7vBoeOOaMtcq97RcA_wvS-zLWgwLcI3xE6BH2uDhmDH_rbllgFcsH5Ri-GdRc1Mw6kC0_kNwEWbEU36Wab73dMN2m0ZEUsmfS4vpqeJjvzjsV1DTN5Fi4EGtC-v3g0OmiXgfP_J_6WYPeFLVGEjzzq1RAC-oBUmWYZtqc2CLqRcpKOWpty1L39eJgtValndMR5nv1SsISRqNynIsnEqCCVBNCMRvfwo4XsayIdPd0eUx1_218-8bKcjDzCTJTNs6JS4GW4Pg3eRTv_UWWG_OeUR4mPPTZSwbmh5XIIQeVadv5Vq50cVeEt07MQp9ZvkUJ5wFWD3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v9RJ6mpCGBXs54T5poIg56HRHl6eN_BXlnXNovWJ98fDDVFYTAMUCwAYkgoIkmf0Ux08nDoy7KimWGrXq5J8DHBULyZ96JjoeB5BUaKqOlHWL56PQpLXwcwHU3i6OjVUeWrCBiLRhINJ1BS_JBo8cpAKzZS9SEP2cpq1X0s0Be0LCdErajHiluRigYOPTdPdzUlUNVEyv1HVG7N40jDQEqSzbwuYxd7PTsVOllppt3mn99ssnQUAdXANQuGRNlvh4TYUmfAz6wHPtqF5B9-8TzBAZbUxvWEzea1c7ndPpo8L1s_ZOFv5Eum2zddBnUjqMqivVSjwqceLcBseAzGfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/df0fV6esiQ_RZ0yNoWQ8b-NDyyHvhrp43k1YSyPmey0SlaV6f60O9V_VtpmqJ3i633UqsGzxTPoiWceGxeRmj7KMyC8Pm9zXDNalxsqo3DFscXLxMm0TKjKOQNzwLjH_cWGfLEevykizpFZ6J3zihB8GZkj0QCRlX1-AsPqNVnOUBinleYOvFjCMSBeSGRbSwMNznqjX7IHb5XcpjvMEBP9IY3bMemY5Y3yhERgIyBngp4OG6SdHjMGZsdcEUiHpbOZQDI_WlOqm9USElU3yDIDntc2Z5-AwMZFYTeyX8ilwWWiZwk8--UwXgCBaXAD-i8QKSwhRWtSbhmUhLz_p0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pzNzpy4cZVXbghfC9PFGQvHJ9Lt6_vwk6jiGqJc1Vgx38rVrOpzvyJcuxMyDCe0NKqgw8cfEHbzT_GteLXcSer-rbNIXPzIHbo0hbi66gfoka-wXoj7XU_xIeS4mdjU8_b2dK_bSpHw3Oc_Ou-ks_HyZn5daMG6W92ETg1xDLIHWUW59MTXLvd6wk6nBlk_2qtuXsmY_GNFYuAL9GPueRu8m4YpOHTQIpUF2XAdhsSqPC02DFqykZlrrtsM3KZ3va923yzUBmtbHwYt1b1XEjWjjW7yiLm4915ShZYox0b3yg7uMGF3IBmvaD4eAmAja7Mgx3HUYNSCrOgE22Hvffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YW7unmb6HAOT-si40N0QFjYDCtU9_yJ35fLeLfdtfZlPgAwHPEhISU9vFR6oj4HWpf6g429NqnA0MOWxd2o7-WpYWpx5UYYFCgB806rDWlmP-jDIn5aCvYD8kValcOjt58VXUfueO7g41AKlT3S721Iz_uo8k9e8NzHC48CbgtBPga7SZr5JYiAp5BqVBS4rNuMZtGGrR0ObfjOP6cNJ_3x7m95fQjZtbjTDOL8kBiKZ5ed8HnywIhh-Zh1x8FfjmXe7kxr1UCOwYOsrkUDdHk6HcsIuGdQV6Zy2HPEeWCjxQuxYLeS4BWOxXsQi0Cn3CR8XZ2_FqQntSWSCzDJdhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر خبرگزاری آناتولی ترکیه از مراسم وداع با رهبرشهید  در مصلی تهران
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/666357" target="_blank">📅 14:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666356">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
معرفی فرمـانده جدید نیروی دریایی سپاه
🔹
این معرفی به طور رسمی انجام نشده است و در پیامی که روابط عمومی سپاه پاسداران منتشر کرده، سردار علی عظمایی به عنوان فرمانده نیروی دریایی سپاه معرفی شده است./خبرآنلاین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/666356" target="_blank">📅 14:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666355">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
بلیت پروازهای تهران - مشهد و تهران - نجف چند؟
🔹
قیمت بلیت پرواز تهران - مشهد در آستانه افزایش تقاضا برای حضور در مراسم تشییع رهبر شهید انقلاب در روزهای ۱۶ و ۱۷ تیرماه بسته به نوع پرواز، بار مجاز، ساعت پرواز و کلاس پروازی متفاوت است و برای پروازهای اکونومی در بازه قیمتی هشت تا ۱۰ میلیون تومان عرضه می‌شود.
🔹
پروازهای تهران - نجف برای روزهای ۱۴ و ۱۷ تیرماه به صورت یک‌طرفه بسته به نوع پرواز، ساعت پرواز و میزان بار مجاز از ۱۰ تا ۱۲ میلیون تومان فروخته می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/666355" target="_blank">📅 14:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666354">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
رسانه ایتالیایی: ایران قطب چهارم قدرت جهان شد
رسانه ایتالیایی Modern Diplomacy:
🔹
ایران به عنوان چهارمین قطب قدرت جهانی پس از آمریکا، چین و روسیه ظهور کرده است.
🔹
ایرانی‌ها خود را به عنوان یک ملت متحد نشان دادند و در جریان رویارویی نظامی اخیر با آمریکا و اسرائیل، به گروه‌های کوچک تقسیم نشدند.
🔹
ایرانی‌ها پس از این درگیری، سربلند بیرون آمدند. آنها با عدم تفرقه در جریان رویارویی نظامی اخیر با آمریکا و اسرائیل، خود را ملتی یکپارچه و پاک نشان دادند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/666354" target="_blank">📅 14:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666353">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851472217c.mp4?token=BnkdMpspTO1ZIXtSoY1OiDpAR2mAxSWQoN9riZ_QHiZB17DEvcsBrSMcgP2i58FCWQEDTYhUFwJlWssfqsVT8RFIxeovPT_9v2UEgzxCRt8ixcSaIBWylYesM1eoxC-t0h42tkJtDi1fffEOXuX9TCJoX3Fc_XSnbnYjP_CsIqtymklCigl3pn_TaSGinO-wxMjuxNc28HZEbBHEMHAN3097rfv697rKHzW7DHEFtJzKt7xmjvxzX9vuJ6ZS-Tvu_bszrHGwiu-mOlC_LjGjYaVMArHfrpAPdRXBeb84KnXCxohpa_gomBz4wPpnjG3PPFAeyehgcC4WEG9r4-QO1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851472217c.mp4?token=BnkdMpspTO1ZIXtSoY1OiDpAR2mAxSWQoN9riZ_QHiZB17DEvcsBrSMcgP2i58FCWQEDTYhUFwJlWssfqsVT8RFIxeovPT_9v2UEgzxCRt8ixcSaIBWylYesM1eoxC-t0h42tkJtDi1fffEOXuX9TCJoX3Fc_XSnbnYjP_CsIqtymklCigl3pn_TaSGinO-wxMjuxNc28HZEbBHEMHAN3097rfv697rKHzW7DHEFtJzKt7xmjvxzX9vuJ6ZS-Tvu_bszrHGwiu-mOlC_LjGjYaVMArHfrpAPdRXBeb84KnXCxohpa_gomBz4wPpnjG3PPFAeyehgcC4WEG9r4-QO1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حداقل ۳۰ کشته در پی حمله تروریست‌ها به مقر ارتش پاکستان
🔹
گروه تروریستی جدایی‌طلبان بلوچ با انتشار ویدئویی از حمله انتحاری عصر جمعه به مقر گارد ساحلی ارتش پاکستان، در منطقه «جیوانی» شهرستان «گوادر» مدعی شدند در این حمله بیش از ۳۰ نظامی پاکستانی کشته و ده‌ها تن دیگر زخمی شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/666353" target="_blank">📅 14:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666352">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPX_Mm1ESN2VNaPplrXaBv05wU05ZAkYouSk7KIiqpEXn46e8CYzJ2cqoBpxVnWkzDoH6xP3mP0ZVsueJS7d0yW6qs3fa3GHpItNG2_4CqBLllQIwKf5V24kEBSCu6ldz8_5ZPB-HQBguZGO2zQ1UlBmI94K6x9c5AA7gZiWzF1cI1KMdPN7aCZbdWRwuENUWbHTqmCz6GUkIlGYAMoZWjakIn5_9k42ykHMWsRKkOqBDCMl_DIdtIy0E4acClNiqgViIPjlEli8e3qFvqGWkwcFOzi0qmv-XgifocDZNje3PkEXSftB7Y9VG-NHbeo1cSSvoxTTJ-rmenMLM9KsJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهانبخش:
هنوز با این حذف کنار نیامدم
🔹
برای صعود همه توانمان را گذاشتیم اما موفق نشدیم. از مردم ایران عذرخواهی و بابت حمایتشان تشکر می‌کنم. رسیدن به ۱۰۰ بازی ملی هم یکی از شیرین‌ترین لحظات فوتبالی‌ام بود. امیدوارم روزهای بهتری در انتظار ایران باشد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/666352" target="_blank">📅 14:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666351">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imHuCABTwOCm2iI_T1DvlH6tGssyCO7d591_SNfLBw6WuyoRJqnuUOnn1xKq1YgldusUSB1QalLxSzRiqHnhfoM84CIQuK73Gk_N7-sPsA2pEvlulFuwZS-Rln93WcvR_FWm6wPUOw8eQqHHTAxu4VU5-FARZvlSc_uj7klrksD1RYEuVG5hmcUwFQF3n2zSFOL5Hu1B-VqWaflAoJLJl34TxGvjVQo2ara8mOuqN-B_TZbIrG7RfxrLIaHq6VZRHURJ-qOAham28IKDB_5pWbE4b79GT4hC9vZ7T4DFQyvrvjrHSFqrEsnu88HCna2DrcRa8SUMhRNOMuXw54pyTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند راهکار برای مراقبت از فرزندمان در مراسم تشییع رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/666351" target="_blank">📅 13:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666350">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a794bd29a.mp4?token=I4sPDHXZWluSb-b1k5nZZNj5YhiMDC6ZxYT5kOmS07ohKXiDWvwiU0BRbtntZr1txrV7ycrM8wVkqfSbC1drjy6XzJQD392UrZMLcpd02XD34sGbHg38bkhobKwh9W0MI5i5tHVUtgLzEjBWzS0-R8QiIZe6CWUoGHxBPRG5MuzZmR0MnEpP1HKg0eS1npORt0fAM6Hvvjb4f98bOubp4QcVPzE-TWaQJ86VwkdNAMcQ_fdEECx5qZhvKgDbZqDs_PPmBZhQRXNtiDaBb461yRd8OL-5Mnk7X-8XMRoWBY5IJYD9ugQWu4KakfMTlEIsbAcQJpdeNOUNcjbuykau5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a794bd29a.mp4?token=I4sPDHXZWluSb-b1k5nZZNj5YhiMDC6ZxYT5kOmS07ohKXiDWvwiU0BRbtntZr1txrV7ycrM8wVkqfSbC1drjy6XzJQD392UrZMLcpd02XD34sGbHg38bkhobKwh9W0MI5i5tHVUtgLzEjBWzS0-R8QiIZe6CWUoGHxBPRG5MuzZmR0MnEpP1HKg0eS1npORt0fAM6Hvvjb4f98bOubp4QcVPzE-TWaQJ86VwkdNAMcQ_fdEECx5qZhvKgDbZqDs_PPmBZhQRXNtiDaBb461yRd8OL-5Mnk7X-8XMRoWBY5IJYD9ugQWu4KakfMTlEIsbAcQJpdeNOUNcjbuykau5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پر شدگی سد کرج در مقایسه با اسفند ۱۴۰۴
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666350" target="_blank">📅 13:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666349">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPegM10byc63jrkg-jffF4Bmb0es3OMTZncI3tXVv88lCDK42pJMlD1SP71XVlECHvekdu4fvaB3J6wlTOAUMHS_wfqoVhlMfnE4g-1EygOiD9AU7zHVxPqzBb-pwwrtfm4gx_4lcXJ1m48VqejIfWhvSZ7ngIkHsK4YAkrjojEsG8bQM-tF2rjgK-TNzsJL0p51ZGpbLcm1G_yfeWBMnHpzioWASxwR9U71aNBybyHPXuxgNUtHrmKOygqQQGlXGRBQS2xjbrU6RgDqY3Avmz5_0VRItWQWNHnM6uiW-Ab-vONz6LZ8fYsEkL_8vMkFFsMu88rHKzTEeaLYKdl-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسکوچیچ سرمربی پرسپولیس شد/ایسنا
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/666349" target="_blank">📅 13:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666348">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff636b5bc9.mp4?token=MwGlOpD3mSzKLwBo46r5zEPvX95kSiYhq3PqMHupgdIZL45VeNvQ3Yh_u9z6-p4kR2EC2R2cShC8wNq0fnXj-C-IHmLXfA7CDRQ4FOSMeO93-7pfUB9CI1cjbqrL-QWxr02S5GGBNWf7ScCaCPybRdeLfc-N4fNF80Z0MOUdmmXYA0IEtlWPqPuECWHhFsEcUH-0bYXQrzlLbCBkG0E0KPCb3TGvWILtGLMagGJDJ4DPcC7pe87X6_jW_eqzSrGfZAmeiHDvmUrQ44pCoC7XnBdxOq4HAPJ3kwGWEZa3_fl-SiOsynPBHKpMR-1Lz5iG4koBaBHjMDyOOmoW5TZE0QNadmbqKXm9Slx_L02nvLX_EMm2tR2hXjSQ_lyQ83B1QANi9o_tcUci4GVLMYlgm4agknglMbBvasJaM7QWR309SuGTKPZiQimLMRT9N_xG3n6UYIw20Z1r1072XiCb3q4Ig65YoT9-u1_6sb_1R4lnIl5P0Qw_H9yxzt4TjTzFlTusFhRNhM0ogOJec8qWRSI-TlYbjI3a-mLNvaDk6RvIdpkmbPWdQ4mM0HHkXaD6oUmJBSFhWFKRlJ20iQrWsV6MjihcllGjgCh7LCCft-Vy8scwCLWEVHHIlU2jf3ga_kFGLctlXdIMlXTfH69GD6kJNRZpjASp8KMi4LwvapM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff636b5bc9.mp4?token=MwGlOpD3mSzKLwBo46r5zEPvX95kSiYhq3PqMHupgdIZL45VeNvQ3Yh_u9z6-p4kR2EC2R2cShC8wNq0fnXj-C-IHmLXfA7CDRQ4FOSMeO93-7pfUB9CI1cjbqrL-QWxr02S5GGBNWf7ScCaCPybRdeLfc-N4fNF80Z0MOUdmmXYA0IEtlWPqPuECWHhFsEcUH-0bYXQrzlLbCBkG0E0KPCb3TGvWILtGLMagGJDJ4DPcC7pe87X6_jW_eqzSrGfZAmeiHDvmUrQ44pCoC7XnBdxOq4HAPJ3kwGWEZa3_fl-SiOsynPBHKpMR-1Lz5iG4koBaBHjMDyOOmoW5TZE0QNadmbqKXm9Slx_L02nvLX_EMm2tR2hXjSQ_lyQ83B1QANi9o_tcUci4GVLMYlgm4agknglMbBvasJaM7QWR309SuGTKPZiQimLMRT9N_xG3n6UYIw20Z1r1072XiCb3q4Ig65YoT9-u1_6sb_1R4lnIl5P0Qw_H9yxzt4TjTzFlTusFhRNhM0ogOJec8qWRSI-TlYbjI3a-mLNvaDk6RvIdpkmbPWdQ4mM0HHkXaD6oUmJBSFhWFKRlJ20iQrWsV6MjihcllGjgCh7LCCft-Vy8scwCLWEVHHIlU2jf3ga_kFGLctlXdIMlXTfH69GD6kJNRZpjASp8KMi4LwvapM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت خبرنگار خبرفوری از مردمی که در آخرین وداع می‌گویند: «امیدواریم روزی برسد که انتقام خون رهبر گرفته شود؛ آقاجان، شما که همیشه اینجایی، ما را دعا کنید تا در راه شما بمانیم.»
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/666348" target="_blank">📅 13:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666347">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nudd4gjSWk8-VB22EHQ_uB-ahzyL95_ejWy4vI9xMXW1vS0uhvNkgYA6FNpKvljS-NUYLEwwUPhTrgkM41-akaFxE9WIG3Wn0h4VwOCXH9V5YdjX5pt8YG5oa5up8oE10EHuE925HUVu-KIxRzUqhCS1Gbm_vOGLfsEsk6VI28NOandBsj_t-SsIhJ6klvhjtCudCOFUpUadCTylK303surR5II1w-mIhzyzZeffTEbscxo1KUoTZHhjPdcr5Ps_z5SLz0rXXbEUuyEh5uHs4Wb1lm9Jl65ORf4qsufPSfFU5OWMt4qYBqPYJuJV-O0Yc7IkRvbd6MXkDndNfWYdCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بی‌ادبی سخنگوی کاخ سفید: جوانان معترض آمریکا را به ایران بفرستید!
🔹
کارولین لیویت، سخنگوی مطبوعاتی کاخ سفید، با اظهارنظری جنجالی در فاکس نیوز پیشنهاد کرد جوانان آمریکایی که از تورم و هزینه‌های زندگی گلایه دارند، برای قدردانی از شرایط کشورشان، به ایران یا کوبا فرستاده شوند.
🔹
این اظهارات در پاسخ به پیشنهاد جسی واترز، مجری برنامه، مبنی بر اعزام جوانان بدرفتار به ارتش مطرح شد. ویدیوی این مصاحبه به سرعت در شبکه‌های اجتماعی موجی از واکنش‌های تند را برانگیخت./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/666347" target="_blank">📅 13:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666345">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vuZhf_r8boEk9TeAjyszp-QHGGbx9ZizkKiTn0sIGRQrBES_eeE3-Iu2kn7s6U0Ml3WdcGOIJ_9Zt08g8y741qnACn8TKF64cvWh13kFSJw3NJ1ar1l1yfpACCmCRQDJ7TBNuwtNymFZjq6PPDV7smtWLQpfacwnC14pMDp6U90y1C7AQnRjq3d7Zkd-kwC5K9Yl6Bi8Lh-QH8LpJi-o-Ab5cZjdrF-FkbIKEQJIFEjrIp1-ABwPxO-ooQkiDVHCg_UhUr_fvtwNn0SjCjr9urcsLAaVYKrmi40yF2atTdMYGcv35WtJpsnlGn31whu--_yYSFvQCgQJYwXsVBNvig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSSRwaOSB1Jrq7hodIftju9DipowbvA1FvGw2aA0QgZ9PqspuZdFyHNNkQuGCoDclN7B4e1zid1wXuhncvzpLF6W_Zq1i971IgFcKRIzCC_OUzx5L8gh9fvcZ3p4StGRTsBNvbuKKpMEPjTlyTpDTCda2AbNHm_rowHUdOMPPjeEz101VTuPG1er0Pu33el_lWV-EKXNK_70-ZbTUoNdf6ZYhrhRXNlcgXxFejJB4LOVIlY-FB897rd_tw0ds2jKVvLdwyx0kWucTD6JD4rsYCpIgtsW2i7sPjhHwtZ2zJI3vUsD2THEiRKafKoRj-vSXnimsVOecU7QUALLh76xNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
احتمال صعود هر تیم به مرحله یک چهارم طبق میزان  شانس‌ها در سایت پلی‌مارکت
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/666345" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666344">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWnN3seEWewzXjTPo5AdzGNSWz5UN8MjFW7mNK6QzR37BF0HhuUEzdHmW_6adTZnvAnXj_eFD4uLXlPcdSbXNJ882mVDQu9Kl7-_0c22cwy0OEBqh3j7mVCiN2NC8V6XkXE5ZZlQmmIIBZaxgHmprAB-AJqPxI_CQ55jVYvcji2xAo0abFz4HeEXJ-_2iBqi8P-c1jzo6gc6PZlDQKqGHxLtZv2hdzhB79LgWn0wLj8jsrdC82a8QrDTTU8Oeg2w76fhYkNrKgDEamdDahZOcqszS04vKZsmerB4Ahb9iFjmb4y9b9167yUcOtQRiQpDpNP5wwiHRBooUXyt5k-P8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماز بر پیکر رهبر شهید توسط کدام یکی از مراجع تقلید اقامه خواهد شد؟
🔹
نماز در تهران توسط آیت‌الله سبحانی
🔹
نماز در قم توسط آیت‌الله مکارم شیرازی
🔹
نماز در مشهد توسط آیت‌الله نوری همدانی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/666344" target="_blank">📅 13:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666343">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fdb30a626.mp4?token=qBfu1HVthh_3_wquBRfSVUMPV9arHmFPduYLlWDlO4X6eFXKUGIj_-gXnNXmyl64enL1zHthIjgH6Fa8ss4zkt0SRXzXWGBK7TYQzD6QxlCU2Yiluc2g8zLeGwBSH6oqZQ2gnqy9Id9SFp8fWpfHtoRPxKIDDB6sQKQbyblYaOIC67kd_Dlj6v_1X0Zdly5mTMrG_AntLemW0y8e2k1OhNasR31m7BX5SHspiBXt9Me-4jLBIC-arunxvwLj4cMmSoATTfp5JzHYzdJxE-88baDdbCx1n6gc8YaJsrhW-oGWd8wnX_wMndpIenbxIW9FAkIs0G8gXkE3jbylsVYSVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fdb30a626.mp4?token=qBfu1HVthh_3_wquBRfSVUMPV9arHmFPduYLlWDlO4X6eFXKUGIj_-gXnNXmyl64enL1zHthIjgH6Fa8ss4zkt0SRXzXWGBK7TYQzD6QxlCU2Yiluc2g8zLeGwBSH6oqZQ2gnqy9Id9SFp8fWpfHtoRPxKIDDB6sQKQbyblYaOIC67kd_Dlj6v_1X0Zdly5mTMrG_AntLemW0y8e2k1OhNasR31m7BX5SHspiBXt9Me-4jLBIC-arunxvwLj4cMmSoATTfp5JzHYzdJxE-88baDdbCx1n6gc8YaJsrhW-oGWd8wnX_wMndpIenbxIW9FAkIs0G8gXkE3jbylsVYSVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهارت دیدنی یکی از بازیکنان فوتبال ساحلی ایران
👌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/666343" target="_blank">📅 13:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666340">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUo79yF8-A8ZYzMLxmRtfBb97zkYPMacOjd6wtrJKxTu1EPA_6DJ6RTRs1AtM_q9QF072bVriYQNVA3FG9HNmRpBpK7LDIK63wua7mVQu5nI-jw1a4JdwZdoSleqqoxLt6yL8xsN7tN3653JPkxuKdKls6rqWngt1ZFL4SXuUuA5ME04nmqYvi8yTGZAOdjM5x65grkD87-uySWKConi_J0WqivtcBN_Uc3P53WKOIP92o4NyrVfK44N-tqHh-o_i3XqhZvNwVS2jq7A7yBjKRp-mGoFLYsWFu8dJDxSXrYsPYXFmUK-hp_em5o6rF-IHF9rtGStlO1Td0jm8TkE0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mPRPDEv-VcCafpyR0lV3S8q949fcoTicDNQfsz2BhpvzQx9F-bg_WE8RmAhGeH4fIpTvgUZzirWuvkS9OZ3vcxeKvWQv1C1DaJVwMxo0V8XzTrfiefbqwgwxC4VBmlWnpRB8Kbabsf2KP3CnGIlEfBBgMpSY-idL72rSjR0sHI2DNkFAIIbUsBqEefFaNhSLjBXoOpPplslDCpVUIJxXA4cD1XfygxpsFwtg23txA1r2R06V8ugLij8rK4UseSErsCTDFC6ZWxDOwYRqo5RsSkPJ2S11wnmyNPhzcFicXYn4KHZfdAshkQ-wJp7xZrLNTiN7sLeNIGKfikMMx_FhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPcNGmAEPZc1CAP_i6Q7OnWYAoZRDdQ61GyTlj3jYY8hkt31bYpefjZJHHTdB3LLp_fiKtX6ncv_ecyOL8DuwKIeKV3EJY2erZMbPmL5UPHfGJ1lGI0NXOqZ1LqD8Gh8mkZ-uIyiPpcZnWmpGMdPMg6--AqWjcDEMd0tu1PdSvWdJvUyCx6a93wfFgfBJxdRmymkOLaFDS7grcnN40PchsV-KdOVkuY9nbHHM0x31b5KclZ57hHKJ2zica4rF4Pk04zSnihWM0qH7LintNVkGZAQs375VhIKeWjA5bOZpomHyRFpoJI_k0NBTq8F9GNNLmkhbe7p2_8W8No5w79i-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری دیگر از مراسم امروز مصلی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/666340" target="_blank">📅 13:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666339">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0Fl5aJua_JdGIceUUYNXeBLHlSGm6PdryOa149f9d7oyUvL-K4USrS6ZrWtg3iUxOXbg_L5ynnBtEhCnZGNrWDEB2uSd0UWZiI8tBZKIwwbzjWQcyozVlrEzPg5PENkqByuCfABujdUaoacLrzXtZfte9JuvLGprKH1ckb1m6YAeck1KNWXP3D7iIxL5OrneD6ckaE7spWltQgq-EZU2a3i3Mbo7WUyFSbSOEGOJbI6NzNOPDSjQ4Vmhh_l8dJ8IJHH3pkw7Uwal_4qAmQdwBeXWsYoaK6QeLU3kt1C5vwJsJFPMedZXWHkf87tgxWJ7QpagsNJMglxpnO--v2OEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدودف: ایران سلاحی قدرتمندتر از تنگه هرمز در اختیار دارد
معاون شورای امنیت روسیه:
🔹
تفاهم‌نامه حاصل شده بین ایران و آمریکا، مبنای ادامه مذاکرات خواهد بود و مذاکره همواره بهتر از مذاکره نکردن است، اما این گفت‌وگوها باید در نهایت به نتیجه‌ای برسند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/666339" target="_blank">📅 13:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666338">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e3c7ae948.mp4?token=ME6DROSaYRCJoek7GsgoYQI1PkTO6BEtfwq1dYEmycMW75vf3ZMP_XgZfqHuLeqQwavRFbOapGZSpgAtDRmWDDY_rOsErgTIAiUA1LFdynYp_X-ALB3boj2u1_rNXmTFySBCH-MYysoDy_HvvfFblTTb3ZXy5l2JIAPQSdYpUEW30fioOhcEFg2VPQXlvJzmBgVNDVSQJMeyuHKfpPGWPORvuxeL-2a9Ck7slTcAt-ldXjadnQn_8IW-VlZoarxnL3LAEQzrytUsBlqWb8qaExvmbitmWeGWg0bWq_9gS-32sHFjanwnlhOsGCuuvM46240kQXeaxmFnXD_CregzJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e3c7ae948.mp4?token=ME6DROSaYRCJoek7GsgoYQI1PkTO6BEtfwq1dYEmycMW75vf3ZMP_XgZfqHuLeqQwavRFbOapGZSpgAtDRmWDDY_rOsErgTIAiUA1LFdynYp_X-ALB3boj2u1_rNXmTFySBCH-MYysoDy_HvvfFblTTb3ZXy5l2JIAPQSdYpUEW30fioOhcEFg2VPQXlvJzmBgVNDVSQJMeyuHKfpPGWPORvuxeL-2a9Ck7slTcAt-ldXjadnQn_8IW-VlZoarxnL3LAEQzrytUsBlqWb8qaExvmbitmWeGWg0bWq_9gS-32sHFjanwnlhOsGCuuvM46240kQXeaxmFnXD_CregzJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمادگی شیعیان عراقی جهت تشییع میلیونی قائد شهید امت در عراق
هر پرچم تیری است بر پیکر استکبار امریکایی
قوموا لله …
🇮🇷
🇮🇶
@Tv_Fori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/666338" target="_blank">📅 13:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666337">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac0aTm3cZLTEc0U-2J9nMsj_lVpdKrAqN76VVFzqBl1qd8AafXfqpWTz0ybvNKLjYP9pKQzFuS0DOe3hr9LgmxwH2Pg0w4f8FXwStZeXOPsfzRYa0kXbEhMb4MxNkU6d_ptyiplk0uPCWwUB4HnXXr-vYW9ekmb0XowpjsvpxaWvkeGDhg6p56Oe1ASc4XuA-oREYffTPo0IEXxM-g93JM2W1bbKNaZWI0Zrikm44juCK8Pzf-Zd6_ZE5tkQmpsvCIoMVUq58qXF8oHmdVYKJcMdTfri8OyGkBpH8VQplCR4MLUb0nua-upBIMeCd7zYJtX7SNcYuw_Eksy590Kv7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان سبز بورس در سایه خروج ۴ همت سرمایه خرد
🔹
هفته گذشته شاخص کل  بورس تهران با ثبت بازدهی مثبت ۵ درصدی در سطح ۵ میلیون و ۱۸۷ هزار واحد ایستاد.
🔹
شاخص هم‌وزن عملکرد بهتری داشت و با رشد ۱۷ درصدی به یک میلیون و ۳۶۱ هزار واحد رسید.
🔹
با وجود سبزپوشی بازار، خروج سرمایه سهامداران خرد برای دومین هفته متوالی ادامه یافت و حدود ۴ هزار میلیارد تومان پول حقیقی از بازار خارج شد.
🔹
بیشترین خروج نقدینگی از گروه‌های بانکی، صندوق‌های سهامی و فلزات اساسی بود؛ در مقابل، هلدینگ‌ها و دارویی‌ها مقصد اصلی ورود سرمایه حقیقی شدند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/666337" target="_blank">📅 13:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666336">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lY_vHr-2XESGuR1QU8JnDhYbMEtM3NDeANB2wgdyJ8KqNmYKwbIIPKaPMnUYeSW3T4H1g3cw51XRY9YyW4_irRYMXglSoHLtiNpdEB0fQbf9rfaJ1KTKiG4MTy4YaIrRxu00FM7_eSW1pxHL5mIAZ_YCckfNHq_-F77Qt5mqo1cLwkZBVl0fgnfQ7pj6otaWDGsFJ-ADqZ1QH14fBhSlTpx03gX11l2GUUickpJoJ144ONoqFJE9y44CBVVWv24Z49e1KlEqjhB-oR922JFaeL2G9Vc5ZAcxC6VLVFXBM24_IwYA_MT8rBwIcGckEzKf2zXPfEYXmG_cmbCNzyd3Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توصیه‌های سازمان راهداری و حمل و نقل جاده‌ای به عزاداران مراسم تشییع قائد شهید امت
‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/666336" target="_blank">📅 13:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666335">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRJWczQBUU23xAQ8Fl5R-i8DFcHeh7YexpRdN0jm5ie43dMmkJ4C3XIOtV8XZwv1O4Zmr8zlidb3XJkqEK_4vdOL_jXULx5BFYv4rYXahoeoCMFk9nvZIfeRqWQRwow5I7fDE8DCHfrODGDOCh5qBcggnt-zrdSDpB1bcHxnF8CbTPkfpcj8sdRBN4_LFl7WAi1AYhw7v64KgWMr1QG_SH1q-yFcsK2EH9XKvuV_-aW--RV56Ov22Kp9_hsctB_IlCm9TgUyVKd_Wo7lAmXaT1lXj8U8gaGkULigEvuPOE7cX73ZuU3sqPa3bMhsbHKhzuazqyz9t6k4g4WKKLe8SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مطالبه انتقام «Revenge» در مراسم روز وداع
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/666335" target="_blank">📅 13:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666334">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79ddfb277b.mp4?token=LoOncuZULH5-zy7ppVDADNEimFE9Ji9ETr46bDbM3H6_ipOwEhdMNX8RKntoxe9OwJWrwsFtcyfMqTh0MJ5p4Oiz1khihOlJFXqMv7t2PEeD-uJSQ43FPGrpV1X7QoV_XYRAPOtbC-5kg3i6fWyrAQhVhmnhDvGhj9wZlgjwe-qa4u90MZKkg133Gj0-VAF9FiuhNqy6JQhUuXMjPewjYbfPbyE1TXrtWh0EX8OJmhQwMaafUkaWhtuyt9kdD3fzvV2B2wPiR0piZSTK5EGUVdUeZrvxYAUTWMsQEUWfjOhWn3XBK4lU6dzC6s2PjcSVvhxAiVnoscl0hi0tJEYsviqV91CPvYk28PGwp7ZZw959bS1hO0LSLQcTm7AHwbjFzZruJ6blmkXYg_KE4XzfuDil9mlcIiv3aMS4hzGfPV5tvobBcr_CjLxT6FNGpH0_2uRlliOBm4ZU8DrxTWtUBEAK2Q3EfjN-TdTic3j9rLt0QPYaTJp8oIkN01sgcfaRRSd6fbHXlLeqMXuoxJvoE2ANWOv9KhIOcTQV_oUrJtw2Cb55fozGd6m4NIQEsHOj2bWZugnEpa5bOwjUhInowZayhbTul_RtKYRhXf7gPZviyZJajq_Kw1llioNJXGYmkVyD4NemVvkGrU-UhJT1UqW7xKC9G0eecrG19fO6npM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79ddfb277b.mp4?token=LoOncuZULH5-zy7ppVDADNEimFE9Ji9ETr46bDbM3H6_ipOwEhdMNX8RKntoxe9OwJWrwsFtcyfMqTh0MJ5p4Oiz1khihOlJFXqMv7t2PEeD-uJSQ43FPGrpV1X7QoV_XYRAPOtbC-5kg3i6fWyrAQhVhmnhDvGhj9wZlgjwe-qa4u90MZKkg133Gj0-VAF9FiuhNqy6JQhUuXMjPewjYbfPbyE1TXrtWh0EX8OJmhQwMaafUkaWhtuyt9kdD3fzvV2B2wPiR0piZSTK5EGUVdUeZrvxYAUTWMsQEUWfjOhWn3XBK4lU6dzC6s2PjcSVvhxAiVnoscl0hi0tJEYsviqV91CPvYk28PGwp7ZZw959bS1hO0LSLQcTm7AHwbjFzZruJ6blmkXYg_KE4XzfuDil9mlcIiv3aMS4hzGfPV5tvobBcr_CjLxT6FNGpH0_2uRlliOBm4ZU8DrxTWtUBEAK2Q3EfjN-TdTic3j9rLt0QPYaTJp8oIkN01sgcfaRRSd6fbHXlLeqMXuoxJvoE2ANWOv9KhIOcTQV_oUrJtw2Cb55fozGd6m4NIQEsHOj2bWZugnEpa5bOwjUhInowZayhbTul_RtKYRhXf7gPZviyZJajq_Kw1llioNJXGYmkVyD4NemVvkGrU-UhJT1UqW7xKC9G0eecrG19fO6npM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره روحانی از رهبر شهید: رهبر شهید به دکتر شریعتی علاقه‌مند بود
🔹
رهبر شهید به من توصیه کرد «بینوایان» را بخوانم/ رهبر شهید یک متفکر اسلامی بود که در ابعاد مختلف فرهنگ اسلامی تسلط داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/666334" target="_blank">📅 13:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666333">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5419682d06.mp4?token=GvIaCEmVTstAd7EfG5uyAN0-md_4f2OK5FmnfFzhge9U_eYcD1-gTqd9nR2AZzjpjit4vo8CUNVhmPARFo2wBBX4Ene-xyWDYrDLiFhe-PJ5nyAEkrMz2eKkUnRBcIrOfJchrKyy-9lFQkcBKzd58GLbUQamJqrdOeTaauY8oXGlM2H53hjKyBSZbKR3-MPH_tC8mUO2vh3Hz0XZ778BPyfFF0X4UgXF45HT-1LIcrZDWQ8cDVklbvCPehDVjrpUd1N115cxNQdJ0kYeFEyHx88BzZ3cnZUYndg2TJR3mGUGg_MO-JH9Bwld0BvWjGlLlKWaDLshRY3Hy5lkch8lIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5419682d06.mp4?token=GvIaCEmVTstAd7EfG5uyAN0-md_4f2OK5FmnfFzhge9U_eYcD1-gTqd9nR2AZzjpjit4vo8CUNVhmPARFo2wBBX4Ene-xyWDYrDLiFhe-PJ5nyAEkrMz2eKkUnRBcIrOfJchrKyy-9lFQkcBKzd58GLbUQamJqrdOeTaauY8oXGlM2H53hjKyBSZbKR3-MPH_tC8mUO2vh3Hz0XZ778BPyfFF0X4UgXF45HT-1LIcrZDWQ8cDVklbvCPehDVjrpUd1N115cxNQdJ0kYeFEyHx88BzZ3cnZUYndg2TJR3mGUGg_MO-JH9Bwld0BvWjGlLlKWaDLshRY3Hy5lkch8lIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مربی مصر بعد از پیروزی پرچم فلسطین رو برافراشت
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/666333" target="_blank">📅 13:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666332">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
دستگیری ۶ نفر مرتبط با شبکه‌های معاند در پردیس؛ رصد اطلاعاتی منجر به شناسایی متهمان شد
سپاه حضرت سیدالشهدا(ع) استان تهران:
🔹
۶ نفر در شهرستان پردیس به اتهام ارتباط با شبکه‌های معاند و ارسال محتوا به آن‌ها شناسایی و دستگیر شدند. بنابراین اعلام، این افراد همچنین به تلاش برای تشویش افکار عمومی متهم شده‌اند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/666332" target="_blank">📅 13:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666331">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
دانشجوی آمریکایی در اسرائیل با ۱۴۰۰ دلار برای ایران جاسوسی کرد
🔹
دادستانی اسرائیل، الی لاون، شهروند ۲۱ ساله آمریکا و دانشجوی مدرسه علمیه ارتدکس در قدس اشغالی را به جاسوسی برای ایران متهم کرد.
🔹
او در ازای دریافت ۱۴۰۰ دلار ارز دیجیتال، برای مأموران اطلاعاتی ایران اقدام به تهیه عکس و فیلم از مواضع حساس در اسرائیل کرده است.
🔹
بر اساس کیفرخواست، لاون در سفرش به آمریکا (نوامبر ۲۰۲۵) به یک آگهی مشکوک در تلگرام پاسخ داده و یک ماه بعد، پس از بازگشت به اسرائیل، توسط یک مأمور خارجی هدایت شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/666331" target="_blank">📅 13:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666330">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWgmuSjKwt44z8mKtuuzRqLlofHWGQ-glT61RwVWh0ZjEob6kmPNeU8UwDpJzWbIQVZusfmtBeBlx3faegpfT4mr--2p225ugYTOnjEyCJQposOyd026gpFKSN_T_xJOqwNBrmyN2xJ5pk016Ae_tESDbwnzG0HFsdbFD7qU6GOkNaWkAuQ1QNIb1pAlps8lfoNcK4JkSK0nUzCgYleWWwl375Cb1yLLCXpDajHEa6nmP_AuO_aYvTHjmAyBMCQ6Wbaaj5l-W7-sdZKREFLd0VQXsshCf-zsxHJiI9MYOlgBMxEbllAlgkqAoxrwiAmwzhF0riujsNbLQ6xaAKmBuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انتقادات بی پرده از مسئولان و افشاگری پرونده های خط قرمزی
⛔️
🔞
این صفحه دیدت رو عوض می کنه، در آپارات بدون سانسور دنبالش کن
❌
https://www.aparat.com/MADAAR_TV
https://www.aparat.com/MADAAR_TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/666330" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666329">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4417a5e8b.mp4?token=Lccr1tvcQ94KX9cnci4nVpNYFJUWwgr9R54yjUp-9ZFVD2x5xc-IfzEn1gHN-L2874COKPv1_9p1U8J82k2luhqUdznTDjd0xGvBpg5bOzOmluPvBeBFguauvP4SV4u27Cq5uf290Dz58FQDxGWZqDsmm8x_oTGhbLtufY_SOehBpVpmuOl2jBhSiBA5JqoSBajHtZXn6t5vtuPrCQKxwZESO05jVTkDgGjxAvmF6p3c5u2xD-p6rexr4XmlXtMxXHN-xgPJh4r_3ll55jDyjJvUF8tJvOMYdizmmV3RjAEobt_VIk2CSBU-pW_4OSVnGvAqerT3ITdXfDD5O3C2tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4417a5e8b.mp4?token=Lccr1tvcQ94KX9cnci4nVpNYFJUWwgr9R54yjUp-9ZFVD2x5xc-IfzEn1gHN-L2874COKPv1_9p1U8J82k2luhqUdznTDjd0xGvBpg5bOzOmluPvBeBFguauvP4SV4u27Cq5uf290Dz58FQDxGWZqDsmm8x_oTGhbLtufY_SOehBpVpmuOl2jBhSiBA5JqoSBajHtZXn6t5vtuPrCQKxwZESO05jVTkDgGjxAvmF6p3c5u2xD-p6rexr4XmlXtMxXHN-xgPJh4r_3ll55jDyjJvUF8tJvOMYdizmmV3RjAEobt_VIk2CSBU-pW_4OSVnGvAqerT3ITdXfDD5O3C2tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در تأسیسات نفتی سن‌پترزبورگ پس از حمله پهپادی اوکراین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/666329" target="_blank">📅 12:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666328">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0a2f0a68f.mp4?token=N8Z9pKbzL_6PHZ5mx1sb5njWdZBW15dMW4WdK52f9HzC7XKWC4Tj-YZKvdzbuadXhUYnQ_eRtbhw4vDvBL2MmllbvVHVY1sRvvALp_IQ3nbaBjz6CF_vp5dumxI1NjeLdAboNnRvaxBW-RbsKD71daxSb9JQjb1taJeoT_RiOAu-VuxiDGA-YktO7VYf3m5rcXiofE9fOMhAbVW5nOss6NV5I1VNNM_WqndZk4MWmQJIhSOA9SHeFeYmX-Zennp5kRtakWs5xOhGHZRqu9_wKOFWORcxqzKiOgzsYE5EUCxiF-fuw6Fcl_ct65-v0APNN7WzR1cA3TDcVwyS4JtfXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0a2f0a68f.mp4?token=N8Z9pKbzL_6PHZ5mx1sb5njWdZBW15dMW4WdK52f9HzC7XKWC4Tj-YZKvdzbuadXhUYnQ_eRtbhw4vDvBL2MmllbvVHVY1sRvvALp_IQ3nbaBjz6CF_vp5dumxI1NjeLdAboNnRvaxBW-RbsKD71daxSb9JQjb1taJeoT_RiOAu-VuxiDGA-YktO7VYf3m5rcXiofE9fOMhAbVW5nOss6NV5I1VNNM_WqndZk4MWmQJIhSOA9SHeFeYmX-Zennp5kRtakWs5xOhGHZRqu9_wKOFWORcxqzKiOgzsYE5EUCxiF-fuw6Fcl_ct65-v0APNN7WzR1cA3TDcVwyS4JtfXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای محل استقرار خبرنگاران در مصلی تهران/بیش از هزار خبرنگار داخلی و خارجی در حال پوشش مراسم وداع مردم ایران با رهبر شهیدشان هستند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666328" target="_blank">📅 12:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666327">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I11Fxqv3J0tPF-93QBxsXdqjv4b5iMjLmzxW-hkrDl4qkK0D_AESohBpY9PfUvLtY3tLjlbKmG8QZI_xfurBmN8Geg2vaIQb_lpnyyhmio62yqVs9Mcj9WJFAGpsP2gZusD0__CPmLIx_QotBWhEEzzxWgb5l5lhT9pbjsJ9iW2DSOjRekSgTsLbcKJp5sz9pEruWG8SmPIJVnCF0kmp2lAvEz6zv7Jaw3jzdC2tpA2lzS_BoEGhm2crw8QiImh98iIJt3B0I9jvV4_vTwcuAQq_XJs6Usniq6FwwHYNe7FGUHXEQ97nJ5TDWDA4Sr9_oL884jIoYS-K3DDXTqmvqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۳ تیر ۱۴۰۵؛ ساعت ۱۲:۴۰
🔹
نوسان مثبت قیمت‌ها در بازار امروز، سکه بهار آزادی را به مرز ۱۷۲ میلیون تومان نزدیک کرد و هر گرم طلای ۱۸ عیار را در کانال ۱۷ میلیون و ۴۶۲ هزار تومان قرار داد.
🔹
همزمان با معامله دلار آزاد در سطح ۱۷۵ هزار و ۴۰۰ تومان، در بازار مسکوکات ربع‌سکه به ۵۲ میلیون و ۸۶۰ هزار تومان رسید./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/666327" target="_blank">📅 12:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666326">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0QX65DikJxA-ie23Dz1dBtLDHt8eSdinYzTaqnrgLIgc4Q8F4tVrGqoFhvAF56kvfPqLAtaEEAewTHackkLu5zg-xcsB6WQA2ksUtHKWPoVGEDGxTQA6lVezRu6dMHIKZuvt1nJVLcqypJli2uLk3tWX9p_11MimZNo7nFP-C1Kw96AsJw6fpYzV10-px4uQQhhcFFnrJ3ZvE6gb6YgeB5iLp_F5OagGNXGgbu9XNjlaNoyOuj3d0oV3zlhkigM2Y_H4iZxSh_0GR0hulRFENaH4lQc4-WWT827vJMCSFNB0IZApAnmBaq3er3NuWEwBvVmij-9HbUmr9u6hvfAvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آنها این کوچولو را با خونسردی به قتل رساندند
«الیویر ریمل»مدیر اندیشکده‌ی فرانسوی با انتشار عکس تابوت کوچک نوه‌ی رهبر شهید انقلاب نوشت:
🔹
آنها این کوچولو را با خونسردی به قتل رساندند - چه کار بدتری در این دنیا می‌توان انجام داد؟ هیچ.
🔹
آنها بهای بسیار سنگینی برای جنایات خود خواهند پرداخت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/666326" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666318">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWvkEva64hp5mH-snW9cilLZvyX5a_6ARTjDoFDwA1FkAnO-q9T2kw4FU2jPgdZfCuEHjTRTmHbi22jenI4umAyTqusUIPEW2ImTuwvruZaO84TJLd7CTvRbA1WmD4k2LKdO2Wird-stOMjfULBPUYcWUn05CvxzJi64_jRYWce6R5YG9_fiEcj9clv3yhgoT_HVAUDIj3dek3pyOaLwzO_7gNgB69kVlqJ7zIbUQgsHBp7YuQrr_wxi2BZDAbyzXopVY_RQGmnr2I4pBfjoHH57W-UQTs_b66wAsaaq1PgcFZ3S58yM7Pk_a7914yH3I6UJsHptfVykAKFKXEDWQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZwFZFzuhA2lWdkt6Bwfw535o4bLyQYK2Z9mkHJEESeOCsUKZjbQKt28ljH0uzj6ub9qrw4ys_3BCoJRHpy1Em5NHRLCpdIuUV8vWkYUvVr5W8uPw58O-0ZqjdvQ6isD82o5YVDNXmfEhKo_MFs9NzxHZHZDeo7MgwimBYeyYagNrUeqOHaCGCQdYvv-XdlgT-DlQq5VFPQPyFpDIdv6W0gQ7a8DIwerCILGtB086u5XbYkG0uGYSeZt0-MGjLo4sYHCyblE8FbM14YsBrVb8Az_XQSv8xXsAzNyQAjZUTeF84l0XcQdIhZ31TT4xHn4b8hGYwx9SUsg94O6PHyZCxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AnXOwu8IjDL2hIhpYfX0wikZfaRodAF7pKhLRIe7BFvjkTskWcqfIv3WNUpAnHQsMCxAxv1-iQOhcSitu2vStASclhOV3Nn9tBrCtp0JmF0e636kdrvtx_c6WHvTOAu5CKLnzRTL_LLCmV9j39lOG4FgHwr1pVLHYwFJeWUiGugFAKVYP1ANAF2ZJizvUeYZmqkOSyzkG1CHByxZG7-VNmKShBrIi8N019_lRrB8b4S0PrIkuoHJJh0V5Wz1zafLlZK69Ic-OQAtSmTYKDrKtGRsVI38jgZq4YEF0u483c3ImG6iKKGzak82medOQBe3Ff6o0yipVnrXWnHqGMxSSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDw-gGInctz_xQMm2HabrWSTsRflZjqvE-D8132t0B0fbNydCNpuI2ZACZoT7lCm2wqdP4gTq55-yBT7Gkir-ly-hDjU384jBgflJnBQBAW3htgZsE-HmTnyXRTH6SBjURmAbEWNxCzq85-e3QQ1PCQbSW4GosJIPyazawA2k3T2xnjcYoKXxz7jK5QFHNP-tfZ8FnZ7_oc1nLA2UvGdyUgXG8xkRNQKksOGbngJmqtU4dWK4g9ihvwBurhNWd6dkbORMtICYPa2vLRU3JGGgdtPyo-CQoQWO_2XM5PXFuD7o5faEEplHgOZK1KMKUdTseLm1wDnnZ4Oil5uzVU8wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cqwyclzPIQIN4GkqB4pMlDmP4ziRY69Afmly3chaKKsK03-NI58CQSWC3n5kelxcxgT18UwGX7-sLlP0cVK9AJBpaRobLIZMMNMd9HlLXY0p4CKwYGu_nVbo3w-kjw9aMvglNWrqV18w3K3MftpIpSpqE6v7oZDgfv4VaUT7lWDvTOsZkZPC-fyHjNSr2et-DDu8KkrD5LG_0fA0B9hiRdXAzm8k-e66IW1aCsDabslMuee2qnP4RWNEOEW870UlH1dkpmMCocfcwEhRqmZd6Eg0EdN4iaJQR4TCzZhZpIw-_N1T_w9I5Cay9nv0TghHUIrp1ecsrEOTJ5d3quvZ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QLHjpjb_-jjYPHCU3OfK8SDOTsgg0zEL3Noe7w2Ff7Z3kmIbVhgNw69mM_liPahLWzyaLbp9PNL36LqfgUIedtu_-DOtdPVwM3OZWqwjaUrELPGx-nAMpuGbO5_SSSAe2Hh44mYFOheee8bI-7maZexLhI5417vCLmrBKnlghcnzxytHgpraZqc4EEloln1dRLHBCnT0RsxoglukyAyHD3_PAB1zD-EOsKOM_ta35G_Pvp8VcOOMKbFvA_F8U5L3YwLrExLuqzPwIcJKMAItkP1N9F_6GhFh3a-5hpFleP3dPZh4TTtScmWPfA4slk7g1CChz7cSk45y-tWP5sJmRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUKgAfPqIPaS5KpL5iZiw0wdGESWldMDwTtLLse5ghUpu1tVzW18YX1ecDXQ-uVb0ez56Dl_vNSjx54uTgR_s6M3UgmlbFbS3V2BLOen-AtQM8bGsB2atsPxc0epJMC3pZmfpivOpsXbsuRR48YEhPvU-x3BjBf0erntm5LBGLWXzrHnAy0qXzvu5xwvZT5UvAf3-W3BCh6bc7b9DBKCDKpuGZj6jluyvqlvsztZRjWJ4ZwQwSi7NFmKSs4I0CrnOgFrPdGXB5iknScVCk2a7JnGwpbmQBqXVER1Q_yNNGsOOq0arO9r8ljaMpWZHNuy_souByQ5GYal-TjDuCGbqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از دلدادگی و وداع با رهبر شهید در مصلای تهران
🔹
عکاس: زینب سادات اسماعیلی طبا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/666318" target="_blank">📅 12:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666316">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVIJoFoDx5i8xpnHrlEQvMFkjxMbZfFdQxYqOM7R-vo7WeyCl5prfgFrCimFIC1Ud-6QxJJYycHl6vc9isoQ3OGMqAFiYMoFB2v-fXasSlRaHZQJXlEre5a1yoxdy1G-NkCkeqWBNPNaCDFiFe8bITU6fnhGLuiroU1qIZg1QtJ32hy8yiaIm0_omhysoRDu0L6WtEAbQKE2KTlNF1NEuXZMD5adwy7y1y7qnnZ22bL6Ce2hF6fMWHh7HiZx5t2VcwU_6j_pnKLY2KoB8_uW1flz8QKt6HNARjKkAkKTQO3rwOA3jH7-gVFbwKVhhhkORedWVEtPBJMy8f1UM4StdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرچم ۶ تا کشور داخل پرچم نروژ هست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/666316" target="_blank">📅 12:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666315">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-sOpAAFOd07ZA5qqVwJCBpIN3ZYHuxxWTD-qeTXOfGdkWY_azIq8AbZVHrxqJcww91tO40bBsXbJQHc2mOclDY0ERD-TIajSxsDnzw4C9xTcXLYlgiVRwFZFWtCikxU8vAJ4v7aPlHLo5vcDE-5UZ3iqO52ovg6fMSWWJcylNmbxardFIcktDa2iQvMIDyUySK9mtIZJ_vSARHjUKkVzvsKdBTcOCdW8ISkGns8kDKFrb4tIuh1YZE67sWfP_hfpRkBZ6rAiMk9JTnZS4ARQMgvxc6poZ7NaZKORgMc0DFNF5EUSaZpt9bygL5SKUkhHyAL_PjJfjmxvnrAXU-f7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◼️
ستاد رسانه‌ای تشییع رهبر شهید در هلدینگ خبرفوری برگزار می‌کند
کارگاه فشرده «عکاسی با موبایل»
◾️
تصاویر ارسالی شرکت‌کنندگان، در صورت برخورداری از کیفیت و استانداردهای لازم، در رسانه‌های خبرفوری منتشر خواهد شد.
#بدرقه_یار
ثبت نام از طریق لینک زیر
👇
https://survey.porsline.ir/s/3PHWMjxm
@Badragheyar</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/666315" target="_blank">📅 12:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666314">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce35e147dd.mp4?token=S7i-gSWzFPocTr1j3HMAGUjABBtMIETtwb6raRNbF6vNEgnoENlwW9ViY8710OvfosaPQt84hovf1bfZOZDSelNMSoOvFy5HJXvALIsA62kSPwP5QaUcJyKcSkzwFmruolcS9tc86gCnvuzWU9WrWUHqNOLCQyXFf8pamLE7AUdABm02jjcPCbzH7IynCeFXXpuSkaub3mKqsIibrKNK_2_Ckw1mW1aFxd1qeLgfv2yohT3K5PBdI1lDqC6ZiYTWOH1L0_2S94lonEDSBi47zrBsiBCtEB40oTLNV9bnTCKdwVc1JYMHqKxLBZQ42SbtnIOsKgwb2KMeWBH5dPtQ6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce35e147dd.mp4?token=S7i-gSWzFPocTr1j3HMAGUjABBtMIETtwb6raRNbF6vNEgnoENlwW9ViY8710OvfosaPQt84hovf1bfZOZDSelNMSoOvFy5HJXvALIsA62kSPwP5QaUcJyKcSkzwFmruolcS9tc86gCnvuzWU9WrWUHqNOLCQyXFf8pamLE7AUdABm02jjcPCbzH7IynCeFXXpuSkaub3mKqsIibrKNK_2_Ckw1mW1aFxd1qeLgfv2yohT3K5PBdI1lDqC6ZiYTWOH1L0_2S94lonEDSBi47zrBsiBCtEB40oTLNV9bnTCKdwVc1JYMHqKxLBZQ42SbtnIOsKgwb2KMeWBH5dPtQ6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موکب کودکان خردسال عراقی به مناسبت وداع با رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/666314" target="_blank">📅 12:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666313">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1h3ZSZWN6__Aj66ezg5nP1DUylcOks6fSqcd138CmXmdVm8W1ZfLxuUc2r8z0bU1V_w6dsYVbA_pfnJj05_n7NPnuUoiqhPTl4aLUdQWsp7NP2lWFnmODq9xeP2PqU8CJAdIaPHKps8mSGXAlsCH-x81Uerm2wZ90ufFCOO5KR7YpiT8DyXBbkIGQqkGwXUbjB-KRqECix5UFGBm3dZ0tmy0Uwne3qse_morpb-Z2OxaD6mAiytGABznI5nOb0rY2APItEcNgE8kLpk14EJpsnCtUlG9e6d6LsFJxNw-uaspeasLTJ0XFLmINjqfaNWpzcR3_NuoII1931si6r1oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
️فرمانده نیروی دریایی سپاه: انتقام الهی از آمریکا و اسرائیل چندان دور نیست  دریادار پاسدار علی عظمایی:
🔹
اینجانب و همۀ رزمندگان دریادل نیروی دریایی سپاه و حافظین تنگه راهبردی هرمز با خدای خود عهد می بندیم که با پیروی از آرمان شهیدان، راه رهبر شهید امت را…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/666313" target="_blank">📅 12:36 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

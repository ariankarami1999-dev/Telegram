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
<p>@persiana_Soccer • 👥 407K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 23:18:13</div>
<hr>

<div class="tg-post" id="msg-25034">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWPrqp4fHRXz5Kj2YJ6UeZkkO6WIKR-kqToVY53GmPD0Nk0mzL-9Nbrx6jarp1Y40UiwVRC7Up3qkL1I5avA36spCZeJvj7SojlV_iwHIFqn1GsgyPLgfRDMil2jhdp5yyesBcHfWXEMpaH-GjyLaajRfLlL9qPjF2KIMoLSAzlRIRxXebPJvhSLa-Cq02rR3W2i4jjnnrOpLDOWp9o4yHsaymI85lpNAst65a1Ufc7tboNM6edWhfaMndKm7tlXu0iUdoW9a2CjhJQzOzIHl3BfvG6E7-eoSvAWe1kPXNIqpYC_Wj0wOXwaVpESUbRDBq4wsskerhs3uEUY10-J1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/25034" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25033">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHHcjTpDYzkXUslbWD4YCSalGrGAxziDGRga0lxLvGUzCbdbX4wdo5SCYI_d6eFcWk9qmZv5a0x3Kptr-lNNU8IHjJ0iEZySaVkE7s4ocOgrxkmHuzJt4xFPpShAumrlRVlAVyUmVEFE2ziGh6VZVXKvmPO135qkCcghvP95FkDgA8QM0MpmU7xBasPKJCxcuJ3MQDmPkUM0dDi8JAVm4Lytls-vV8Lft0BYt-Cx75n7cyJ31XqdsY-xHrFRACf6XWYpIRaSQCSUcjD0iO4BF6sp4wT0ZBOxAfGUncKa2WfgV1gb6n6tYg8UC1hDrVvS9HdLF-GzWotkpUztEL48hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/25033" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25032">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB4OS9oYQ_TBSardgNxr6uQwd4Kbis2-n9LU8LsClg70zaFsy2CAZUClBsjOrG8Fhg3MDXkMjDCGUgqXBrVJkAMzqJbxksJg9ZhEm0oek7l0clo2yVyTFY1fFwPM6B9mw3Iq3JDMGCXV8Ju7PKC95ZysSld049uMYo24TyO05IE8eWMMfbQCroERiAmZhaP7RHsuMahXQJOAblpfhCqwSNgoDRCoSRYxRVBvMCYJW2iaKAV9l5I2xgLgKMErkGlNcJ8-Z0TLYIxot1AE2GJUdBwiJmjNGa8DEg5klXBPTUG3P_wnV0WCbVpkkwml3BuELKAuHixwCd69xpQB00pOcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
🔥
بلاخره انتظار ها به سر رسید
🚨
👤
نود جورجینا همسر کریس لو رفت
🔥
👇
🚨
👈
گزاشتم تو لینک زیر بگا نریم
👇
https://t.me/+wYDPG2ky70AwODU0</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/25032" target="_blank">📅 22:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25031">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsfiaf36fr0_5dLOzP2E3Pub_wZTotim-ro4kfPk0yDRbmbNL72JyMI2PJBSIrYgim3kUZoOzJYaIl-Wfp6w_KOeKGq7DCj4Gi_MNLajKqs3_XpaJlb6uCiZCqk8MJj4TMLJmDubuu9rQXCL3GeiLNPpvW3os2uGFd6BW9Jzcuxd2X6vud2fPmn3Lg4z2IBNj1BM1bPSk5cqJA7dlc7NtZWGGb4SBRqgYAofnmZIRmz58rDaPiNhb51_6PodyM8fxEtMB6nEiUUNplSmhp3m-k4y8b3MPyvl4lLw7U5uzZlxERp60CoxMAxQTeT3B7uFW37Z-wIVzUAVxs7CfruH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/persiana_Soccer/25031" target="_blank">📅 22:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25030">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDr2qSqbZ3yhciZGS9DicjioVS_5gSwy2nNqQNhL6J5QubOvJtdBnivAv4qA81fVjd1BIINgovDtOBlw8n7Asg6GkJFLEcngUh96odGSg7C0ZCHhDMvpviA-KeopLdrWDiDPQAARwrI2UabDmLooEHZ2LvD70qfDi2i-LlGudGf4r1Nb7CmDKb5gN4A27WCNrmCZNZ7lfxS0W2Vwuuh6FQoEUH6Baq5-z5SB9_X8O8n0r_gisqiOFyaptkmflYLlx6TCYbi6YU-EIZNsd51H2HojbNIrUtEf2GsuPUPZcjEbCUbd14Xh2LyviNO14zmV9qHfqaKnkxgWcL58qCNnFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛دراگان اسکوچیچ سرمربی‌سابق‌تیم‌تراکتور و نماینده رسمی‌اش از شب گذشته بایک‌باشگاه‌لیگ‌برتری در حال انجام مذاکرات نهایی است و به‌احتمال بسیار زیاد فصل جدید او رو درلیگ‌برترایران خواهیم‌دید. مقصد جدید اسکوچیچ فوتبال ایران رو سورپرایز…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/25030" target="_blank">📅 22:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25028">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQiXVQp-dAdY-cseqgXdrJirXhOsw2rL0o2XKN3qaUvcb0QxWz1kpvJ7kNWWZyzvoJ1JRKD03ai-Um-ow_A9bvMEjvsgSfFu3meBppUdWlNnj_u60zkLW2nhnB-bAikPk-1PHrftX7rfqJh69Co8SB3aULcsxjfbXWtLKNgrEw51ZqwUQ09TvEIfY7wqZEMh0n2iZ9MnuvZfqhxE3bckTK4KR96AFfDN1UGEuYRJcJx8s9SrSlEnPmEQD5oedRstk_b3RiSau4idN_AdknsaYSkelhcyFdm43zvP4JcpWhYmim7Cq_NdnOeuLPg8POKHssDUVJpic_yfzfkeI4suCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ALTWGg1Sg-37orXPTRTw-MK5HlDvxWxFqhoq5DVnkLOH-D1RA59hxheE7q1xb0TGhxhz-_xYTPjer1_HKtdvdt1Jnhj-XH5GV0dGiI39OSrRpiOdhKA483_F2lxvreZpvZjHQ51PUs2hYnA5tSgRGqzRkRNTKEXdxRb9TU5JNkHHjEKgdhy_NPPHThnghJMPSGqUbId0QYxXNROWg_pSf_vDp5l2Ztd3Z11XNqxW4CNhRERWomt9k_ee2GM7i5ZCweF-97mVoS-uZ2D1hQojxPaY5n-0bLi9mPFYTvrWSid1np6pRYpYkKhEw4u8Oxl94qnpVk6GrWdjICRBNogdEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی
2026
؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/25028" target="_blank">📅 22:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25027">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWbGRXdQNz_gWibiAp3oK4cAzfo_MU3vTyqxbD8S4Zkekg9YDWUdcTOigkN3-oYCXVamOgk8pou0O93EanwZmU0RiOcQ5nupcHWp3sOMGA3G3h6mc2cBwluTkf1omxi__UDt6sjNG6MWOj1D6seNIwiRe-oHilO57VH0qfWKr68O-y_LNLlkbfH4_0lWOHd2XiU_WECPUyW4AogpbLOGCvWSPpWsuwUpbeUwQ2AsmQXTFJl7bPVwiQOgiTHcHTc_spLyxcUJ-HG0OEOIqa9nzYcXrqckHMqP33yLyHBRtOZQuqoZ8nU-XxtWXj_EhVAiZTBNXBvYpcJbZaLNzzkgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/25027" target="_blank">📅 21:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25026">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ni4EqpumGxf_4WO6DHWETIWTXl-ixxMIHWbfh9K5yIzopLRq8m7Iel2B4R2XJ_YQkzDtzZVW7jmBrY8gcvqvkNe4rkIfv-wdY0keuX541CIzU0jaYoKPCeC5GIjchbWEmnaAqbQ2UfAh9X7JK3iF2yriOw-Ir3JMAvt0XY8YnljrKv3O4xfDNmtgtKjdvSIR3UafQCOtOOuIaMAa4wMwRQzl18tJQwjle2CjQVjDpaNnwQXb8vjW6gXGpidiTsYoycxApuivp9Y92jH_fZEOp14qQ4oMgoesWOZOBaJ5nIW4sLywCKqlpb67QPbPcGxp2we0HZ-AX4BvW1b8ldYV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اقدام انسان دوستانه همسر رونالدو؛
جورجینا برای کمک‌به‌زلزله‌زده‌های‌ ونزوئلا پنج تخت اورژانس به یک بیمارستان اهدا کرد و ۵۰ هزار یورو  پرداخت کرد تا برای خونواده‌های آسیب‌دیده غذا تامین بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/25026" target="_blank">📅 21:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25025">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmxILp82VtwEiRvr_2I-93QhOy2cBdb-1bN0wdQVHeNyTcOtUWlihLf_KiJi3XoEOMdrYPLCbsliXh_JeJO5DwL8mqu_vX5l1MHFpv_zTcFD6-7hoPwQrIZ46FYSzyKlg0Y1sNvWks6qZVoqFoj6KLJrnQX742FdKdN46KarJc6i8SnkjXKEX5-9q-z9gZzxW0SQnaRCyUW5QiXqZ8OmTBcDvxxh2z2pkDEu6kuv0YIvxainnFrcGtrXNyjAAIORI8SPgCOtgo3hmng1iBLb1BRCoro8kd4CTTRsjsH0W48rqQ8cUBpQVKhljIq-jyYgk6vYkcyV7EpDMqKa3021jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوراللهی نامزد جایزه‌بهترین‌بازیکن ماه لیگ امارات شد؛ احمدنوراللهی‌بازیکن‌ایرانی تیم اتحادکلبا امارات بهمراه مهندعلی، تادیچ، کوجو و کریم البرکاوی نامزد دریافت جایزه بهترین بازیکن ماه ادنوک لیگ شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/25025" target="_blank">📅 21:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25024">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hn8GotJOuoA06MNofoTdGrcKO8z9M6-3-GOViPUmCdKWSAC_vAqHm2FdDU0J9zC5pHGCa3frZy08z5G7NqbKP6YWxDbGTypSeFwfSmSM-uN5YJ8XP7Vq8InF7pXUPEXKwJ6DL3up-MZ8kYf2ANqejX_lMajF8mQ924VDAEZw2_iygs0AghLIBriH_CcNrVXaO-hSEyraaLZvR9C6YjOu5YLYn68wnH-N7Yysj8hYHOxqRZU4sS62whMopp_Q6elboc4d5vrAULY4_AIAYmgA-TGOP4mlACE6H2gjRK9xWppeUa5LJ5w5fvuidr6AXTBeGR6OejDY1pFqPT2vlubzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/25024" target="_blank">📅 20:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25023">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lcc0t9k96vliflTKXIpVxoCqQCu1BB89jGCjs0pEvKpmlVbRwhbLy5PCPUfJFU4ZBJqh8U5vl9CstWz4oIXsGMr-3Zvq9dMEUEK--oFIe53ZyZMA9dpXW6Yu0BHOQmzu35s6sEvLelr7Z5uYpXMAYqmJ2jL7_R1BCsAWpIHSJ1fjNsxnnbKpx_qj9JZqtkxE5VslfVrXC2DWHQT_M7am_JDha5GMK1xvjf1-X3dbs07tw_B4PXDG0HUdVQGtkncc2hcFHTCdh8IOOoowsByQ4Zf7Uw8Vyo5mUuneAMEd7cri3f41KQs59EMgyI_p63IUIrHFugf8t4nxi_x9uh6PuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/25023" target="_blank">📅 20:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25022">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=irfEk36vfg0kebpPfkuVUnibF25VbsGLjkBuFItMasl5QBmlhA8FH_GBN0HJ_0g9-TNa8ho7LAdwNkT_g5XNUdPktu4Cpn9TFTD7iwJGr8_uvO0xRjrFYkgkqLDpLrQFEeb3NhXK5LPWFa-YPY4bEvdc6lVtEbdHvUcN5uVypr-YvfMPD8s5IrXsdN9WkqYgYvY5iQDS3Gi9tF8xw28_JBWjieGa1C639O0DDEqARRfqrKNivtD7mEU7zXBb7wZFcc1bR55E8zgrXEgXgzAyk1l8hEAOFAE7YwqVouwqpoKxnBd1NtvreJP-H_y_rWT5tr5vjQMcMLkW-Gasamb5JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=irfEk36vfg0kebpPfkuVUnibF25VbsGLjkBuFItMasl5QBmlhA8FH_GBN0HJ_0g9-TNa8ho7LAdwNkT_g5XNUdPktu4Cpn9TFTD7iwJGr8_uvO0xRjrFYkgkqLDpLrQFEeb3NhXK5LPWFa-YPY4bEvdc6lVtEbdHvUcN5uVypr-YvfMPD8s5IrXsdN9WkqYgYvY5iQDS3Gi9tF8xw28_JBWjieGa1C639O0DDEqARRfqrKNivtD7mEU7zXBb7wZFcc1bR55E8zgrXEgXgzAyk1l8hEAOFAE7YwqVouwqpoKxnBd1NtvreJP-H_y_rWT5tr5vjQMcMLkW-Gasamb5JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/25022" target="_blank">📅 19:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25021">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=HQMfzxYTQ2XPwvBbbzS804laVzynC2GKxHYbYZkDDduLfFo92cejAhy4nw3o0d6upGkvYkElxuRaYbl47NQndd9K0-gULSyVpy_2lacvNvBifAZ7SyBjZ_0zo1GHUe6SF2s3TnRUMR1pli7-c0qCmdEI2-rqY5zS2s5YVLcsvpMhXIOdiq6fuam-2LUEQMsppFDhF6jZ8wdM1mQEaRiZhp8ND1oKF3hUvtJHQ5f5yMN3meFm4fdRjD_3wlhEWzIiBAe0XjLwuOyuj3msjXGF1JaLHhMkRVrVQ8L7NKHQB8bGYx3hspF73EDuI6DN48F3Qe4UfFB_012olkbjsz_P2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=HQMfzxYTQ2XPwvBbbzS804laVzynC2GKxHYbYZkDDduLfFo92cejAhy4nw3o0d6upGkvYkElxuRaYbl47NQndd9K0-gULSyVpy_2lacvNvBifAZ7SyBjZ_0zo1GHUe6SF2s3TnRUMR1pli7-c0qCmdEI2-rqY5zS2s5YVLcsvpMhXIOdiq6fuam-2LUEQMsppFDhF6jZ8wdM1mQEaRiZhp8ND1oKF3hUvtJHQ5f5yMN3meFm4fdRjD_3wlhEWzIiBAe0XjLwuOyuj3msjXGF1JaLHhMkRVrVQ8L7NKHQB8bGYx3hspF73EDuI6DN48F3Qe4UfFB_012olkbjsz_P2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
همراهی‌رایان‌شرکی باکیلیان‌امباپه در پایان بازی با پاراگوئه: لازم باشه توی کثافت، شیرجه میزنیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/25021" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25020">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3BCl6ykH5YGCgxMEh_4K0TRd171MUdj0E5Nl3CivPrkb2CcZMCdV7dG-Jn1ekSj4ciFQn1xA1ZIVyNlv0aiDwXWIW71ByK7H0L6z5RTluj7uQ3ygmcBqg2vrvFs3T7y6jMXLY4pJv50N_fas2PSRrj1mqa9TM7xVimNNoSFB2piEuhfFaTEWGog5SRxZhWxEezfFrIc-l0CvWtIktU9QBC7p_tR43OitQMoRYXWOhLF_Og7UIul-6hbKLz9lf7saq4bIDnfx_BzItMh0L3s3Rs0xttLV2_759qZKHEW9n2IJOtRsPevTiJOppKnZks4tNRSKRtnRP36bHUjDLuqkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیری هانری اسطوره آرسنال:
کیلیان امباپه در سن30سالگی‌به‌رکورد 1000 گل زده خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/25020" target="_blank">📅 19:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25019">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWZn5cqNnz4PNhBh86r-u_sDa5cLG_dfbXVpnifSq--3M9SdgUh8nUGdXeursNUFt3JNVq-D1HkupZSIV4-Z0zAYuu2A1i2uxRpWJDUDW0Qi34Jc7iMN007uF-PK1v5WU6GBnG_x4s0CQTinWdfdxUe23NfxE-8fqmUNy5ofI0MQOmq3KTZ4uHZykDweKFCO9tIJXfLeqgSWiOGYaxzK55I4igj764hta7HJ43Qt6XerCwYf3iIC8V2yjK0YbKxFMGzNhx_6EAD2FeuLkVqAjnE3oNyFZNaBOM4QT3YY2EG1vQobZWz5IDGinkx2UiEHXDeMGwgtul1evWfqytJp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیدار فوق‌العاده‌حساس‌وجذاب فرداشب دو تیم پرتغال
🆚
اسپانیا رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/25019" target="_blank">📅 19:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25017">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4aktiPfGYEJqqqF2zt0OWgDZiblXQ74KbFESfuNmw9oCMbEV8fYssf9cq7ABpQ5ykvFSqfHThuNeUru4xpa1WQUxYGsqm95gmuvRJR5p0FroDmrhWtatHTjVJePehiBcEhydvo2Uif3Lq3mp7RhGEDc9MMokeQIaKadNIo6MvPYHIlBks3ZH1R_KHlHiK5lKd8Ul0uimPuDga3YTZI-4e6gQcmkNFIs32_vdLPBXrQ0SctEWbYilGlV2DpYv53dnEP39Yc20ufD-6VGhyXkgFKG--bzQFCbJXPQ9fgplr3NuW4MRK3OUGjORH6Ye2LzjKBLoTYUTpKxn3wSibFkzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0V-iDXcbPe5_sifhEYA2zmQIg14ir4cdxjhdsadIilaWaq0JhomwLeGeVuRG4vH1KU6stPkXfg7lZNhg376obs6SHl8kWmYmW8W_PoXmkhDD5HXzFB8hVLTSCYBkK8cv9mBrovc3RJodLG7fsfreh5iUH-NaW5SyyXP4Sxx-x7Ml1GWNuEfwWakN6tq30sQs6pHlbggfSv0tB15xgzFNQb0PPnO8yLzTHhqd53H-eSN5a2CMYG1SEv9Wc9Y-TUxtjfJCOhyb6b3Zww4gRAXRzkLrKIqd9XS8G8V9KZv72hN3zlq_nAooFqO-KEOb9trPHvnImgZKbxYz-hRvAaesQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🆚
🇳🇴
🗓️
۱۴ تیر
⏰
۲۳:۳۰
برزیل
🆚
نروژ
📌
صعود برزیل یا شگفتی نروژ؟
⚽
🔥
پرافتخارترین تیم تاریخ جام جهانی برای ادامه مسیر قهرمانی به میدان می‌آید، اما نروژِ آماده رویای حذف یکی از بزرگ‌ترین مدعیان را در سر دارد.
👀
⚡️
برزیل صعود می‌کند یا نروژ تاریخ‌سازی خواهد کرد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/25017" target="_blank">📅 19:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25015">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7yzuM_Vq_11Gi2HwTup0obqume3FrTnnRo2oZNFk3o4oaI88-xF6xGAiNafQFsr43wsbQlaZubkyz1buQ22q1E3ycbJMzP58WVvE-kNmB1osKiZbKqN7Rmh06DKQSLYSozvBqGbg4MLNdR7eDztQa1WIpjq1nmhzWftDRzLnI1iCvzayMZMxykQhgzx7mcqbtwcdsRoVvsyEqBBzevgo1twpN5YNyZf6iY8TyoOocsVGIOWsJhQN7EQUOAoccX9YzIFGRNJCdLePsHX8xc6Jkc439YJon_uO_O7lwJ08w6e3gOs6_79r6kco5FJVFdEEkEAdd4nr03Dq1AgHky-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/25015" target="_blank">📅 19:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25014">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRizUKVIekKdzQ5XNQdGnahA2_5udmQ4AT8JPuzHWKtUQl4FcDQw_4DnKfutsXiwwyCBWCrftOYcpVlTSw0q9m0DhZEN4ZCwjbKBBky2WAzjUF_NT6kSuERWwIseyJTZReTTKntgiesZLjBR812uKm3V49_wenCzlWszyGewPixGVsQtkoOhySCwkv1OV8tZ32R4aDW15SWNJ-FMG9qjvZByQq1saLw8HaW2mRn9mGYvPNzLh8BnUD1qhPUeg2f9ZmCJ9sXsz0pWHojjpufI0BKIKOdoR2oQlgKAdL50wrr-MDwljfmf88-GKZuOPrnCJNY97ZELFyS6ImvGP3Qstg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aparat Sport [3.6.2].apk</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/25014" target="_blank">📅 19:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25013">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUzfQZVh9DeHt4Zqq41m21n9XKP4o27yXG2jqw6H5li6UNkkWODjxUg-qEGM4gFxKKoHHhEER5N_XrtnpiKtlaZkM_1HNyZcEIJ8HyQd5VlnUwq7XGGjO44XoTB2F_-6BxPoDgKrFc4tuAtHD0D955D7BeMV5lWL38P3a_ZRGJj-buD99eYLYEXbcsZqZOUt7Yw6QpZ2AgTMHJ391bQdPBefaC78te0cX_13SCP7sXW1C0y1-Q-93pPeCceFUiEgx2aMJks6ivSHTvzu8Qtxs4rIVJc8RVdMO78-kSRAYzKpoBKikjl0_or4s00PxEVC0g_UHQjGICR09wKN1P0D-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد.. مهدی تیکدری، مدافع راست 29 ساله فصل گذشته گل‌گهر سیرجان، با امضای قراردادی دو ساله رسما به باشگاه پرسپولیس تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/25013" target="_blank">📅 18:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25012">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQEaVbdm8aShl7X1P06dXha9WUZ1p_pDhFu5HZwVMWmvgPJim4jT2CqMVrpM5svmLacD7v3FthiotDs2sYjhVeYAzJHelBRNTyDdCs4tB9DzuD4iOYOj5HwfxS3tUSNzAyGJREwsaoQdgsin-AzS_5Ay3MopQ4chXTqLtOxf9A75zToaoaOCpjsqWZIalNOQq33G1-7dstPalBa8swS8G62fFma_t2MGESxqDzQp9NGnv4GeF2x23fgF38M4mJKp2xtCR4Efvnhy3s99KovjapCcDUj61R-FI-c0tu6WHvKL2l_FZ1EVdD0D0wMyTAEgT0WsoK1aTgqQDERVE3agkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/25012" target="_blank">📅 18:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25011">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZezubLZX1YI8vZR1YoCpCdrG0S6XCF85YnQUpM7dGvyFdbBZRwjViR5f6JIDaYN-jqqy64cMY-KBGYLl76nOC4olzxW2YvS-Q5XaYzvrG1aopqdgnMdt4T6vaCQ4nrmqF-ytFTWdGclde7uyKY6ODIvtLf2S0I2Go7KTow5BaENfV8SzizTupyNMmK9iC-9lk4tj9_voL-T_RTYiX2txxp1fPryD77NzOBBdLcvQnsV0mBXA0whSXHsf66nsMgWHDqf9_SVjwVSvCHyWgi3ebjuPolWXNqZtrvBVSNRJgR-9fWDB_xvvj7eYBkp5_jkKq6paLS6IxwOKuGt5qfz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌آلومینیوم رقم آخرفروش محمد خلیفه رو به باشگاه استقلال اعلام کرد: 60 میلیارد تومان. ایرالکو تخفیفی 10 میلیاردی به آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/25011" target="_blank">📅 18:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25010">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_EqWEh_JmLDbzE64tkTOXEKXnUnkrw0xD6dPvOXxLtQ5OiYnMiEuwAGoN9_09G5ASyXZx5PCuPXLZJdoFImvwYnY7WA1WVi1nib0WAujBXmKpwRRtxasdAcSj-v4gt1SNmjHzDF57bFgW5UZzr9VwoiIvYnbC0ivxog53MRjwV2WRAeSI5qaD2MTcUUSijn3iQL87-sX-3jcYISQXagVMMv3Fphjsm8vYV5_dX2DTSAvOD25ErYwbmROdIBwTVm8rsPlXT-JZAqX93QaXT5dZZUcTkTC0DFcw5AzGOz-HtKwxW7onFOCEY6izxFDT_-GwDq60WPqHVl7OAvwZBFCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
14 روز و 14بازی دیگه‌از جام‌جهانی باقی مونده بعداز اون‌باید 1440 روز برای دوره بعدی صبر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/25010" target="_blank">📅 17:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25009">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=UxizK4zJUGCD4zAarsvMs1LB9Di8piGS0nVVlnfYN6SFQOWRIa6zivZib8jxXCgSj7xDGYHm4PterZXm6dTA4Dq1Rt5DNY8IskQKrQHybaOqYd2m1scpASt7_zT6D9WFVlXyKgbrcjxp_9X33HkG73033z5btisJOa5zlYwPdlqrhsHM34VIjb_iSuo0yemoknyFtyx-Q2TJl94et9zoKT0-6H71R39XZMtWli6c3VrV4GPgi0D4kAjUQ0Sn12GX2fFj3lRKeWpaWXhWRL1J54U5GoqW_J6CfSLAK-S76N6ozGinmOOcKJGfe4UB569geKXO7vqnaMy8GsjLUui8xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=UxizK4zJUGCD4zAarsvMs1LB9Di8piGS0nVVlnfYN6SFQOWRIa6zivZib8jxXCgSj7xDGYHm4PterZXm6dTA4Dq1Rt5DNY8IskQKrQHybaOqYd2m1scpASt7_zT6D9WFVlXyKgbrcjxp_9X33HkG73033z5btisJOa5zlYwPdlqrhsHM34VIjb_iSuo0yemoknyFtyx-Q2TJl94et9zoKT0-6H71R39XZMtWli6c3VrV4GPgi0D4kAjUQ0Sn12GX2fFj3lRKeWpaWXhWRL1J54U5GoqW_J6CfSLAK-S76N6ozGinmOOcKJGfe4UB569geKXO7vqnaMy8GsjLUui8xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ریمیکس امیرقلعه‌نویی هم بالاخره منتشر شد؛
دهنتون سرویس این چه سماییه درست میکنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/25009" target="_blank">📅 17:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25008">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxZ4IV5EWUsh58sYrros-UX0Ritr3l_6gB4cuWzeUWrbcfP0jlB1Z6hIHa6eiAJ0MTKLEPei-1mE8ORJs3iDzswADhkC8mCuqQy0AxehZbbogS7jl36dTbdKzyAPg9_iqU0jnbqpYQta580JyqYVNRT--RB3wOZGdt56w0bL9328811Eo4zD4a3HPlxzLzsHD44z8S70gs8l06XRuNptsJdmmbZ8f7yq0d-6_hT7AZcm9IRXNDEg8WJ69l6MrN-MIcQgFH0XvEAjWC2hDX9GQVxrzCQfRJT5JTsmOq2zxCUcnLdzjvM42QjycchZaKzB0BOgWofoFMpQLDdWxJ_5dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سرمربی تیم‌های مدعی ایران در فصل جدید:
‼️
استقلال: سهراب بختیاری‌زاده، پرسپولیس: مهدی تارتار، تراکتور: محمد ربیعی، سپاهان: محرم نویدکیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/25008" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25007">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=VWDzjInIbLKlUv1p_Gmb3qprY-uhydfsETRXlhMZyayKQwTymow48U-S7TTeE0DttWKZ1RDfiCYkm-0_7uoknCQEGNkJmcCyumtxlkpn5x0AJzAGJ5a8r3yMZ2tqapFkMTbwZs6Crzpz4NExgM45KHZC3AOeNs-UpueKHtAELuYztf6a04NDTD6omUXii8uyMnpNg4Rq8wWXKPp6qKfAxcY0vIWbV2ZuEERV7MQ4WOq6BBWu8LNE5-dV7sf9SZj_eZUcAkdfBTBfQPUkBB9vvsPEt6EbHvpZMWESGOsiz1XfCBXKBhl6sV0Lw1QEwGhIojW78miiSR3yYN-d48B8vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=VWDzjInIbLKlUv1p_Gmb3qprY-uhydfsETRXlhMZyayKQwTymow48U-S7TTeE0DttWKZ1RDfiCYkm-0_7uoknCQEGNkJmcCyumtxlkpn5x0AJzAGJ5a8r3yMZ2tqapFkMTbwZs6Crzpz4NExgM45KHZC3AOeNs-UpueKHtAELuYztf6a04NDTD6omUXii8uyMnpNg4Rq8wWXKPp6qKfAxcY0vIWbV2ZuEERV7MQ4WOq6BBWu8LNE5-dV7sf9SZj_eZUcAkdfBTBfQPUkBB9vvsPEt6EbHvpZMWESGOsiz1XfCBXKBhl6sV0Lw1QEwGhIojW78miiSR3yYN-d48B8vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از تحلیل جذاب گل دیدنی لیونل مسی به کیپ ورد دریک‌شانردهم‌نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/25007" target="_blank">📅 16:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25006">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJ8l-Gq43shIBj7RQVpaYFQGFsEj48mTfOVLOEIaxRITxvO1vpK4jMh2mHnlLFT1CJt47OJPuioUVVRxCZyziMl2rqRo7KAklh_Fi1krLxkKzVEL3V9tdVzrI23C8kC9-JfuOCzyrjWiDClIa37KqPGTp_mO4u1INOsPkBojjtuquhwtUthmGOQuWgHoeujxwNF874OXFCsscZTEaEEQJHcGITEpg2SbD7WKsvGqeSe1pzbPMmaQ5VFFrdLlWTkTPXIwzSkJjcW68ZXET783ywoNLbPq4ncQCZFQLpzSpRf1CZRgMjT1I3oPC-vE_QgqfT70vQhlJf6vZZaIDlNhig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
باشگاه استقلال و تراکتورتبریز امروز صبح با ارسال نامه‌ای به فدراسیون فوتبال خواستار افزایش سهمیه خارجی تیم‌ها از عدد چهار به شش شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/25006" target="_blank">📅 16:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25005">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AODJDe4u_aFVjx7-ok2myBcM2I5f9cCIH5A4TK7-28frk_U18bPa7nblfQNs_yV6EySDokYswDuMA0CEGT9ThHb18LsA_WioYiRylitxnzB8e02GiciEfiFKLVl2LGILsJZA16KMRy5uoHenCAGkABV_s2mJ6BBH0_qMri9aWJl40zk8a2tv0JfVKaoaZHUbQn3E_OK-GOxDsctqP-gsKq9nTFYu6ev-WkdSeFBhJolWB1Zr0a0-Fkfvl19TzXYiz-6e0PI-2Jt7mX2srtdqkr8byim2BviwYsCxYXyASCsOVOSiSoZAsgC1km7y6Qwilg1YB0VkHBPvj3N8Y7aZ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#نقل‌وانتقالات|پیغام پرز برای وینیسیوس جونیور: یا تاقبل‌از اتمام نیم‌فصل قراردادت رو طبق شرایط باشگاه تمدید کن یا قطعا تو رو میفروشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/25005" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25004">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=a7CAgKPtEyGsV7LNn9pWGZcGmjHaNinA95VdSBqKGt6yibHFizIJYp09iiGsEds7tsTEsQo_g10IySlfXX_ja3QbOgFeS5RS_hQXRYs_yWs1jrQgF63HXrJpRKSkiI29BAEaOK2JzAsWLayaFXfa7CoWLJ-FbGB6gFDS_E01Umm9brtNQtFUvdEnlkMiBLMIhD-cfP2YFFZz_XVOSmjbul7a6skiXRl3CTFgWOX7wYRDlgl8X8eEnnWSx6v1q_EgX1Z6Hj_5_nOvioJ0ds7aY_OIvq9ZqS2gb-VNy6dSxT9EdmI7JifsrqhM92JG86_XxNEZEDCudg5jrKROfwaQIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=a7CAgKPtEyGsV7LNn9pWGZcGmjHaNinA95VdSBqKGt6yibHFizIJYp09iiGsEds7tsTEsQo_g10IySlfXX_ja3QbOgFeS5RS_hQXRYs_yWs1jrQgF63HXrJpRKSkiI29BAEaOK2JzAsWLayaFXfa7CoWLJ-FbGB6gFDS_E01Umm9brtNQtFUvdEnlkMiBLMIhD-cfP2YFFZz_XVOSmjbul7a6skiXRl3CTFgWOX7wYRDlgl8X8eEnnWSx6v1q_EgX1Z6Hj_5_nOvioJ0ds7aY_OIvq9ZqS2gb-VNy6dSxT9EdmI7JifsrqhM92JG86_XxNEZEDCudg5jrKROfwaQIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ازهواداران تیم‌ملی‌مکزیک رسیدن جلو هتل بازیکنای‌انگلیس‌که‌نتونن خوب استراحت بکنن: بامداد فردا ساعت 3:30 بازی مکزیک و انگلیسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/25004" target="_blank">📅 16:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25003">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‼️
یه‌ویدیو سه‌دقیقه‌ای‌جالب و تامل برانگیز درباره زندگی شخصی و فوتبالی مدافع تیم ملی کیپ ورد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/25003" target="_blank">📅 16:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25002">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkgYyWrQ-O8DnsFq87QG6yIBRZLxvV2beWPqsEerUDXEtSKPJrdlQpDzLxdIvob9Cqv4NhlNdk-AAOLKAUtZKMqCjZfjqj-qiXldwD_x0bfUtKu7_du92ZXM2a6Kmerm9ytiFgIx28jAvOtWg0wTaSd8MpQxP7yJSUIWADxoWDuq6JsuSNqjM_8wWvbSS8jSBFwfgs0SnXkRZ4Ljul4tPZslch6_7yeUu2ckLEg7PpuO_0LV_XaU4fnme9unOjezrqkm_xy24QgyySr_PTpofZ05ZNUjQZnlXwXUKcottXvGo6v0rGrK3mbPw5n7X8BSWGhzhc3bVFlh4W_512jlug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/25002" target="_blank">📅 15:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25001">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tklkVpWOaM4ptsRVK0BZdUV6bYPY-8nFHQFEgY4R-YxLAX-Eap2lp0MVY2BHiA7dZvGpwAE-n41wJsTbpIHS-FArEi92RZ2oj2xB7hVDgT2MwCj3JR16KVMmbvveB8Ydj7XehVunLC7BFoqI7CGvGkzuOb5OVAiiImYKfn_809mLKUXP32k3Q-FkFLEtlUaE-qNPTGUi3CeWzxUwzsvUxAMvt0gtm3I-Qxl9NtMGm4FGG5HBXOecEk_UshVTl247ZGDuygaYLn_X_gV6WhrbcEbTKP7DlBgcy54AjjkNFyoccWEA4l_KoRR-ypbA8eL7QRfyJs5ihLJ8J-RC6Jokew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/25001" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25000">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQ9DyHBPVfEuJI5-Rvxn-QKC0JWV2uZv-h1IqtDvLc9hn9ryiw_E0tnOrvPgTAnn5pKqjrT63PKGyorcmSKoRQkNzmyJpjKsTsfAooAN7jgdZv9LoJeE_FORmpNRlE7QWxsYU3Np2vBd_8l4nzRl2Wkz_3gbYcKW52r-epg5FTZhJp_a9KA-mUXA-hVVE6WaAkjeZbkOzyzFGbZlBGo_6q6Wf9yfaIfYHT7Yo8fBK_BdmbB7l0xUHcfTenOBrIqMy-TzlrzHxUZTRENB2hGCsULz273oxRfeFIcvUuucZdIxVFEu01ugGX9tOh_rLdisIrbcF2PGOdIAUYJ-NPZfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/25000" target="_blank">📅 15:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24998">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwOUlCQee3CZa9MJ-8-NhmaeCAVTmTtz7etUWoYXew3w3EUO3Axuth0yvOonTXSd4E6p-clXxIYoWPT-tEgD90MGIT64obK2mP3XnMiWaKlAQ9Uw5_ReWORgloC3jcUZedp5yR5wruE4eW4l98G5xgNvkA4sr2-s4bpfGSg7aJkio8iUtWPtJwqlqaX9Z2pmq-IyiU5artox-l-s5nbS4pqYkdALoHUUK3wug3VUr0V0c5Q6NTNiC6eRXJuovjhvUWMgoRpSLZnz22-DsxeZVDNpnWTA94uBg4yNRZdxqapb4eCMIvD9YqRdZEAaUeR9Q3U2SV7AHDoZ1Klma7Ps9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuZm2yWbykqKtGoJ8Bq06cJs6DeZqsrew44_XuZpLzlbMjF-yRzBtczAm4oUbMxxRJ8Hh9iIk2THAVq4Lx9ELdQk8kSlQxeub9spjyGrRs91cXK1evjJAC3sRo8QUom7c9GaKr509Bgyb4jnCbxCYppSn7Rgd8Re8GKxzSInDKLKBMsDe-M6PSNQPh31jMU3Ipfewu4Jibz8BJjfkMqVlCpj84DlXVUW_ShWcv6zPU_xPaO6Iz_KlKpHruMXiRPLAx1zK-HNPkmL00edbeYiSCQ06yS0L5uYk6DWxIVimmIP70zhdJIYE7A0TBjuU3m6C8rTqbu_3s8FbFKwwLOsoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم
؛ سال2006 در چنین‌ روزی؛
جواد نکونام پس از جام‌جهانی 2006 به‌تیم اوساسونا پیوست و به نخستین بازیکن ایرانی لالیگا تبدیل شد. او طی هفت فصل حضور درتیم اوساسونا 197 بازی انجام داد و ۳۱ گل هم به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24998" target="_blank">📅 15:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24997">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erA2C0c0mQlutWJVbIc4emhBPpD4K9RLzQKCqEAdsMW1aPL7jMkhEH75k3-ck_3g67z5mpk8TLUGFG5tGbV_cpC0FlXndiirsSa7TwsGR8hGhwt9idvAwqeLnv0CinSkt2M5LmATVSPb5qLAvslS103ZAFvHS9m7bBcIG1FVGd2punRcy9cHvY-1gnSNOxSaBvtEdFFM2GCnYN-i57eEOAR-CL7m_IPwxkmCXbPF_FAli5i3rFsTbHcG2U5xMOD70Tc0pCWgkFhETMp6vAd1np7CknKgQ2SPhMJw327k01g3tZ6a9M2OB4WpMsjSVwie03whrXCWamojdoYDitVrCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
تایید خبر شب گذشته پرشیانا؛ با اعلام باشگاه‌گلگهر مهدی تارتار از این‌تیم جدا شد و بعنوان سرمربی‌جدید باشگاه پرسپولیس تهران انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24997" target="_blank">📅 15:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24996">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkREMsk_NVSPZAjWqKrMe5dbQEI7bKGRBFBEdtaEOE3TQwhArZwbTHgXax30kQX0mhJ0ymdEdovwg8XZp7PzMf7Ab4NJGuK7VMQyQmW4jAlHCL-hOf02cz6ig-X9DgcDhUHRWqC0IWMKmpiVMfhwlmYqEeZYSKQPgM8F7fgEyBsE2Tj9YFLq-r-6J5FO4dgjbfoCxNFUFIj0oQASwQW5pKrm7vEHx9m4Y_kKbRrKoNDCy8-uOV6OxosKiDLtzKrWGTzp_cxkf-EvDTYFF2YkVZU7vuOXa5vrFjrP2XtYA3k3UcZSLevKchAaTnTPKSZLlYYxO62CYVkxFF16P93-DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24996" target="_blank">📅 14:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24995">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkTTL9H3A8ATOUBeUlPLueUSHEExr6u_ObJ8_Ip23_cJnTJTmIlexPQPcaYhqQ9b_cPHpeHGUsQlRnWCNZSbqa2aq2wKZYhoRd2RMxJJ1RFabcqHm7U-G-HNrwCQgHLJD3Z7Hp060NH9qj0k6CIzlFct8rpuh1SoPJ_pKhNHVMe0O-3a7y8IZW7cxKrPte1kUHN-9_nH4t87WLjkCVYioyz2d4CoFOEkpDYwgaF_mQG4dbXZHGB8CH2AnGZlwAEhXAEK9jDiBvSEGiDugqz1ajZEiBttq05prz7Jv5nbnTY7LTno08u2cxqfAm9vqReXDFXO61-6BhCMoj97Da7uXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛ از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24995" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24994">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPeMUV3F9oFXIGb5VD0TZ3pq__wmu0sCQhPTgjOlqxDijwrJCgXMhUkBaXFlKS0QrtSwMI6n0k2IOfr9bPDvH7vJG4huSj8gIgMClHbje5cR3UCRMuClj_NnpDdxEN46_MEdbYwXCSoAhFCDuQpv_nO60Wob84hFQN8k8FCBWjP_lfoBcu9O4MnjFpZkV4BVUQXQaj27ov23L9l96vcO_6jbRj5s7pmMv6Tbyu3o-1CzcHPvM__QL9bAW-Mu7XjjHok8unv9eM9VU5WYAMqque9AOD-l35LMLdrdl22yEF-6gr9ZfJ60TkuehSPsRftsafg4sllJE5xoYCUxla8lwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24994" target="_blank">📅 14:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24993">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0RXo8VCuH_OBD2rxsQj4gYlnWOt9tVcKkVBQjKVsSd2Lwkz6ZngAfQv15nje7MangedW_FrXThMbizcZFCgKoTHPe1ncCBwwwNePP59tSDqq7kUFHiLwyGl4_qUNlC47jSu3w5zitl5ELcOIg8bY8VxymTEZQmYNJ7amOLSCLccYGRe9c-qluzaQ7mXjfHwfijgkSpx6XLtUCKq7uigNoPNp1yhVgrVQ-79pOLK-WUjuzqfpFzwD0HIQCmDoWvQ60A0PPQFIe8ioyZIlPCyJzU6vkQWjeXPK43jUUt8RgnpImT_2st73zjHoiNneA6HE7ybHsFVPOWn8k1DQpGK3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار عصر امروز مبلغ 20 میلیارد تومان به حساب باشگاه گل گهر سیرجان واریز خواهد کرد و با عقدقراردادی1+1 ساله‌راهی پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24993" target="_blank">📅 13:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24991">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANsSP2zeDSUXjDXCFx2VyTor25XFLG17FcjLd2INR4ZyH9bqNYOpayfHwC2uC4COBVSZ8ifmBFNrBeejyzr6a95jckmwlSCckT_Dk1CRJhOW4SJ_bww95KItuZjg7kNjiKiDCPNTRveZipjRRCJXcn4lstlG8kxLK0mjtRArF6zOuEwUiKHKWDKI5ErtoyiezplN5qD6Zmfv3UWUud5AaByYUR4ldIPo-vTOBC_dvu39jcRxQ1POMqbNfDhafjoLc4aoqzrtK_UD-lkbW5Nmwfta1ElLOC7BR5VWGbgQtNR8kOO4XV7CO9QizaN3Lslnv2Q2m4hKpoMFeTZ21F9wVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24991" target="_blank">📅 13:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24990">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1M1Fw--ZWH4pFeOOx7VcwVxmrJfIzMmmXwXXJraBM1RwOOzSyYCw2Voj11Juh2kr1B-_F_v1rmrrsshLdYilaiMPkBfVm8ZnEBfiGJocQ9rzf1j7QGEndw6XrrH46VUV4qfDsa3qgQiKnYfFO-18wk9rVsu15Av8Px64R2jfaCpz_SiyonfzlRg1AJV0cPBpSL0Mvi6ipraZjBuH8zdbJlYae_ZVemNTF4-1IuJqLN0lOqyWAdUhQbCumPnKF2d_vMX3WuqwYQxaK8s2Pb3WgdlpS1Mml9Pb6jXdkGouTLEZt9gQnJsst8K0unKqKmvztyFfH_oCbunad0c9X2vBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24990" target="_blank">📅 13:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24989">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ2tlEYXw2nSUHl8EMO1Ed9OiOiYKB_en_J94w7ZfFhir_oxkakkpMC6k1S39GIGAuZtjWAqB6cGMuWb4Q-taNrZRlVaHpfWiTByhABnOw6NJubk4aZ3r25UFD9EXiNm2cz61LiloxTBqiWluJymnEACqvB_cG6RdPG__T1UUcAhXabhZE-xrtaqISlypESNaFcqW0X8ACwpaSCvEteLON2IiLdeSprRFBuT_1Hu7TlFgIXJuRJFNr5iiapHWBUn_g3rlgmo2kpduf3uM4t0LMat_T8_S_AVzERk6N5_FGvijKl7fFdjB0KBVFurC6V8QuLKtYbvoD-k67pQeoBGpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رومانو؛فدراسیون‌فوتبال‌آلمان با ناگلزمن سرمربی خود قطع همکاری کرد. یورگن کلوپ اصلی ترین گزینه سکان هدایت ژرمن‌ها در یورو بعدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24989" target="_blank">📅 13:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24988">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0kxJ__E-ZbPsr-jKn06fS7clMJa5TVeoWJXxCuAuftj7TBkUxKLk1XNRV2H9K3RdqVdPCswL3fv_k2UWXhRDto6f1aUqtx6_lhbCMjqUXkI0yvYb26BzpUwQQjLNEs7MzNuKJfF1_-7gL_iGUf69zGpaCap9VPTjby5LbdA9eQqjqHld6NL7NCLhN6ZPV3QifWAe5VhI48uTcf4QFynnCD7xHJQQW3ht57tsmyANyx8XD5wELiPd4-KoLMlrrn73IedbNw8vs7Z-b9qUHt9TMbBtzSZbMkgXLdyniPYI_HaMhy-o_kffRuGugRX7TTEFXxLj186bQrDYKxEnLT6YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار امروزاگه‌بتونه‌رضایت نامه‌اش رو از گل گهر بگیره سرمربی پرسپولیس میشه. در غیر این صورت مدیریت‌سرخهاسراغ مجبی حسینی میروند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24988" target="_blank">📅 13:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24987">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgJSSH-x5CLd4OAUjeJXk0lBOJ3Bc2TlAcWlJst3CljQ02HB_ygQCr0BlHYFUl5wbl9TuLeKBS_Mxj4kCU-vCTRoiwueIHI1xL8FWfSUoGpnmS400MTaK4pnWaEeWvUk0Ta_OsyPAAf1dv2zRcaCtT_kbY6sURr8OOfTfODOiGos9xk2H5-ODyhXA7wBEQAbZBQRMF5Yq-N66R_hlcOGZwDMqdGak7VqcqXXzl_74G9mbN_x12ZE6cjSH7k_Jo4WG66OZ6-5Yz7KXuF4E6UWimT53tdGfCsQsVZ1e_tvOnNLY-02EnH1n3kbz8I2uEwWbWNrh0p0xx9A1zupoYumKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24987" target="_blank">📅 12:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24986">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKAdaKQKkKOb4Ahuiat2EH8_lyH4u4gqZ1zeeAdv6jqmMgI5OHGCM5xLlqf46O70MKH_0VbUlmDJtvkWKC1y9nDV2a7nU85lA9v9XR4Mi-z8t-KesKU-4mZi24SWecvq7yeFKfRNcqZ6FG8fog2mKC_ZS3HLkgNzeALpgS6t6F-iZ0F8IpzikjIB5iBHbwNYK99TvM-EReFdlJKOUAtaUC7iYsb5TrOJtCEsj3aw22-M0XBXjFYR6OHWnj61RCD6dP6BNbGMxLPTYgDMcPdYopoYsldRMTun3OYYqNf2NaTmF5F-IF-Akbc6Qj32YT5XQOM8-jr1_LH2ZQOsrjKSgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#نوستالژی؛ یادی کنیم‌از مصاحبه قدیمی کارول سلیکو، همسر سابق کاکا و علت جدایی‌اش از او:
‼️
کاکا هرگز بهم خیانت نکرد او همیشه با من خوب رفتار میکرد و خانواده‌فوق‌العاده‌ای به من داد اما من خوشحال نبودم چون یک چیزی کم بود. مشکل این بود که او برای من خیلی کامل…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/24986" target="_blank">📅 12:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24985">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoIc95WpIvz7Jf5hlutxIsXfTYFxnm19c8UmPhObG88QqE4SlY2wmhWFlGdvWMtZs-cMF928JQZbwGMG_wAAg4Vwgw8etab87Ac8oxvjDXQSa37R8fL5WhC500CDnLbFS_NZbz_FvDwTub-qIsj80qy3J3Qz9IXuW1YFfhcoRM11Jkm-wVAbWxsleWpuENJu0m0iCrK3nmh9EBiku1kTwpi5MTLX2WGwa830AnxCPKaCVtWIPrzJZlm1uElLLCb1rCfuukYeIOMQ9xVcXi6rYL6whnyUE62YPcBf3DDQDdJNI8cxoWsBLODemcu-lp8bUfnwqCTYFmLgPs1LkNW36g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ طبق‌آخرین اخبار دریافتی پرشیانا؛ عصر امروز جلسه نهایی بین مهدی تارتار و مدیران‌گلگهربرای‌فسخ قرارداد برگزار میشود. همانطور که شب گذشته نیز خبر داد مهدی تارتار به مدیریت تیم پرسپولیس اعلام کرده خودش رضایت نامه‌اش رو از باشگاه سیرجانی…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/24985" target="_blank">📅 12:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24984">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM71gbEVgy64ZRcUaF_XmffXFsRDKmtTIFktf4srkuOiAYBNhZxG69UbLXmmCJIs_TIfnS9T1qr7uVegSjTR906ptOH8M250Mqv6nDSFoXVkf0p3KGLMasTsPhFGsvrcmg96q2FDx0Vhi8isRjbOi7a1ic12BhGIY1KhEDzxq-dHGhaNmoT6q89fK5IHpThjJIXRcfHUI-JrJUP81WCffbJTVvjSs3Vl77scgwT7rjQIgPlt94Kt9vtXAR625SQlHaoBedF37DiaK4UCeqp9ecFEw2OG83_GI065IJ2VRDCHL-337hYytjDD8BcttE2ZE48I1qM4bzf4yoBXWpSQ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/24984" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24983">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSNnL7UR07pDAdwPsygWHEaxcpupBP0PZH2emxm51TsUWZqHtqC9A8cs3gVmqSc4iQNo8r5x38ro54IeyNegOtXBlXStgybO9gf18GcW8JfWzyJAHELPMlJV6Fbn3LwjrwwwuBPa6Mk9uBabbykoYg6Ns4FywiZK9EUE9Vh7aK2eRmVLGRSbIhwlTa82Pah6yPOFvU4Pvl1E0HhAXpVRXFipWgapDNq1qCnO_c9rMdD5m8uyrr_TJ_E862upFqOknC3knPsP0p6s7NfKsrpSQSeUrSqFE7Xx74yztBygkygNWiarOPFV8eq_SDdJR9q692pqaFOr5OhcgrXDobtt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛ فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/24983" target="_blank">📅 10:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24982">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLTm6bhm9hLUWUQp6yc_rscb-8wwRi3asNAZIFXRlrAjrKnbPAAq3xughq937wwAfLptnNQYp7ICKyxEKGK9WvAIpY08s6XjU-5HnKms4HMUV_Yc1Y-iMGWKvaefbw7xL8l6L3tWJRL4MRmTRVjD8SPZ3ROFqOh5QngMm9P7VvAGKKCBvXWJJ5Ky66xZ_Gs7VP_Vt4F5GpOwBMOjbcFCqcy8LcjpQPypfHRk8bYwiZXem7n92VS2gFqiiBnIFLxlHMR1bIytFgseZHFS1O-t0Fi4jsgV99D81hi2MckiA9-z_UGbADq5-UewhlADuPstY9US7UDOXNN1KeTHbE6VsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌داستان: امباپه‌‌کم‌عقل؛ رابطه‌ی کیلیان امپابه ستاره فرانسوی رئال مادرید با دوست دخترش، استر اکسپوزیتو باروشدن‌خیانت امباپه‌ کم عقل تموم شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/24982" target="_blank">📅 09:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24981">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBEILpELPyo_r26RSnSxyuTOplWkHLv_8DVWPsOG4MertXyy-FJzSFsUTwum6bTD8356PSjo5n4dQVs7eholGCTH2Dw-P5hgNZo3CyCPpBZzkofXhCBRZkv8RnvTDpjHc_xdkcleyscgAA1r45mjQVuk84EsgokR8Rfs7mfE1SyPXqbB7mcn9FnTKoEmZ7C6en9pM4UI691viNkMSrRhTEeXyLypyK-LGeEuxV96-hx_up6vRK5FZ__6GWAxmyki0EUVYlyBcjOaUd8znSUypC6Kb2FA53VAy43Yva072DkMFT-KhyTQmtAmwGlNPBM3WH5VAcUghubLNNUnV8mWUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/24981" target="_blank">📅 09:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24980">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=DFzVMDSFFvWI_ChvG2CQkpdHyiyGVsrkTWs6sMmUiX31AR8NUwFpOCLOPDyMlgb1mbXXfT8P_HnD556-TFh1gQKkTTcGGTKgDs6p5g3FYsPKjV3nMbJ0ROQyk_LNPmqh59-5MkgjT1Bvhp8WYh9s2OxltkPz7Mx0ZUQQqidFhBN5BCQvLPwP4suD-dvOPlUkm1kJdrfACMEytI6Gp2-wpK-rcuqxuT5EXl1sHjjVlJ4Oh9bv0s1ko9wyJNJK8AKr5hBnpN6yFxehme4A-en9PhL6exfNQCeMq1Re8yediL1VaGF5mLNKt-igtpXbt_MT8kqOICnWaseQ4FfbIWkgUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=DFzVMDSFFvWI_ChvG2CQkpdHyiyGVsrkTWs6sMmUiX31AR8NUwFpOCLOPDyMlgb1mbXXfT8P_HnD556-TFh1gQKkTTcGGTKgDs6p5g3FYsPKjV3nMbJ0ROQyk_LNPmqh59-5MkgjT1Bvhp8WYh9s2OxltkPz7Mx0ZUQQqidFhBN5BCQvLPwP4suD-dvOPlUkm1kJdrfACMEytI6Gp2-wpK-rcuqxuT5EXl1sHjjVlJ4Oh9bv0s1ko9wyJNJK8AKr5hBnpN6yFxehme4A-en9PhL6exfNQCeMq1Re8yediL1VaGF5mLNKt-igtpXbt_MT8kqOICnWaseQ4FfbIWkgUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24980" target="_blank">📅 09:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24979">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUhVarzB6Gw6xmcvqmGtEhrt_u0abRiiN3DNZKAZoRY-8W77Mdm19YlpuOkTLaVIHrVsiMDPOV3d9SNtbRh7Z_Cp6lF-xZBQIukvCpo0kwzdaFU8KrOV27Qtct04r0pP3Xxfn4Aclnoh6D2O-NEKviqJVCcm9gHGBFLheEBYUfFb9TMg5JFO4DK88M7By7xq4-oIdq4M8EkIFJ-NiRTu67-DhhiMl1pZEsKlfbldK44kG30a8fDvC6Ck9hrA-4lwe93nVgES4o8_HaMN0HqboZ4KNQ7zrqNwNzwfM9am8J_DzBTWbkcgu6w4ggCWouNxwfJH8aixImveeEgRxCpKJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گائل کاکوتا هافبک‌تهاجمی‌سابق‌چلسی و استقلال در سن 35 سالگی از دنیای فوتبال خداحافطی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24979" target="_blank">📅 08:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24978">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=tRyCL1FwPiqMRyJTE2DixcKkiIt2c2WcHKMYzvIMRHhTDakTqOqaQnNs7lK6YMKWAyQM5vIca4LKgOv2U9ZKcuY4QuaIpuh3NxHZj7ETxx0Z83DrwWTPQkZY-T_FVOjKN2comcburXEjFOHBb1Z4C9Xy3TrpUFdHiYE_5yYg6cz0UHcjZNRAenqDgaPD2v8Li6f3fSmlJyolk3U1aPSE3AT8cW43FnU5IjPvqwyIcqCdCN3iHQCi1D3wQ0da62LAjQRruKtlVsORKqYfOv2Q_WnxOIskERnsEJHl_TO9NOx2nStGIAB9JcXODwiV0FjP5n5R2uwHcga0nEQ1c5DQCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=tRyCL1FwPiqMRyJTE2DixcKkiIt2c2WcHKMYzvIMRHhTDakTqOqaQnNs7lK6YMKWAyQM5vIca4LKgOv2U9ZKcuY4QuaIpuh3NxHZj7ETxx0Z83DrwWTPQkZY-T_FVOjKN2comcburXEjFOHBb1Z4C9Xy3TrpUFdHiYE_5yYg6cz0UHcjZNRAenqDgaPD2v8Li6f3fSmlJyolk3U1aPSE3AT8cW43FnU5IjPvqwyIcqCdCN3iHQCi1D3wQ0da62LAjQRruKtlVsORKqYfOv2Q_WnxOIskERnsEJHl_TO9NOx2nStGIAB9JcXODwiV0FjP5n5R2uwHcga0nEQ1c5DQCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه خطاب به تیم پاراگوئه:
اگه لازم باشه دستمون روکثیف‌کنیم و وارد جنگ‌های تن‌به‌تن بشیم، این کار رو هم میکنیم، ببخشید که این‌طوری میگم. ما اصلاً مشکلی با این قضیه نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/24978" target="_blank">📅 07:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24977">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWtDedkFiRp6QhVrOQxfOx8Jp1tLfP7iyWyJqDNpQs_kS9A6BL0AtIQTQAN02HA5ll2R_jEGIZQAjDmcULv-2sFO7OZ2JhMSjneCD0H7CSzZBW9WH0U9Zj0TSMq0OifWOVSJC63Ph2J0vh1R43pUulRAKg8qTZ30Z4d3lvn9MfJbm0x36BAWylftKnJ0yOCmDJahaDmMStMok-YByQxPrqEqaIuukmXR-7pPlqvOEjTOiwu5lmcNNA1YC-yncP2gGtAj5tvmydIt6u0zTvTBa-ZbilJWeRCEU3KTn_KXL3MC49j7KRGAcPxHFGFj2LWfPwiVvQ5qSBCJhXbKLP1zcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛
فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/24977" target="_blank">📅 07:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24976">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=DAndmSMIQ22ke7pOhyeiDJtEbXTBgd3HUnR5dYYjZva4HZxyAZwd7TIjZph2QgGAC4TnAOkWXi9CwmMfN33CPsQBfVivKcOxEnWvcEMyiDqmV-ysnIqckNOSARarGWTe9wSaknqa5CjX5iGMVlMbzEj5xoGd3rdDvC4Y8rCoX0Z2JkmHMujXC27Rr_de-diA_VslOUTMlwT86_JlRAfqMXTXytAUfKdyABy9JXipPSNCnBj7R-P3NyCkmgKaZdcehqSuMZ7EW8CsGIh44AkJvfcglvCQVgpRIklFghttUsOctxoc2k2uTVXSpo3Wq2ZC1wckSYPD1MnUwVfLBXEGhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=DAndmSMIQ22ke7pOhyeiDJtEbXTBgd3HUnR5dYYjZva4HZxyAZwd7TIjZph2QgGAC4TnAOkWXi9CwmMfN33CPsQBfVivKcOxEnWvcEMyiDqmV-ysnIqckNOSARarGWTe9wSaknqa5CjX5iGMVlMbzEj5xoGd3rdDvC4Y8rCoX0Z2JkmHMujXC27Rr_de-diA_VslOUTMlwT86_JlRAfqMXTXytAUfKdyABy9JXipPSNCnBj7R-P3NyCkmgKaZdcehqSuMZ7EW8CsGIh44AkJvfcglvCQVgpRIklFghttUsOctxoc2k2uTVXSpo3Wq2ZC1wckSYPD1MnUwVfLBXEGhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
👤
این‌روزها ترکیب جواد خیابانی و خداداد عزیزی خیلی‌سمه‌خیلی؛ از دست‌ندید. این بار خداداد به جواد گیر داد ولی دهن سرویس کم نیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/24976" target="_blank">📅 00:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24974">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BK3zVwEfrRZzSrxa8cUoAtH0pamR8VOb7mONeWC7FPFHbyJcwUagVofAfPvIX9_ng0lL6P6SmfnIrkXYzQFaJCIJNLkM0p7RMjzQEG1AUGsmVNecMlJEkJvw8AqGisSNp_Cw_ZBdYKCvxrPLCqIyxP2UrtyPce3pVxZesU55q6Q0JYYS5uyuETTpB4rbZMvGGaYWADrLUvFR15EpmoTFfU_CZvjEtqkjZbwBndAQOk2w9XFdopxINKl4mlGyHDWYXS7eLVpEiW5bcpUuoj99M0xlxec-19aHYUlyjGkhKFV_I5ivVAy-EsJ4QLfhJj5dFAgUMZkBFwsaH1Tv-NkLLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/24974" target="_blank">📅 00:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24973">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGy1LO5U8QReayXOKOhgH07iWeim5qpvPXp9CuIUgKJuvF9bfHbMePCQuEvX_dj7nnZqwKGy7sKx5mimko0K1oubgRGiDp6KSa9N8K95dtMFbRr9HhaFsDDUIJ_UmfcESVAEXUmcdAcNWqxU5bCwi_PVb5BkI7bvHq3cHn5C4cHCmSLuxa4nJRtpuzxTGq_zO62TTV5bhW9ZUjJeL5Ov-_u7d6LIsH4tMbsj6kLsRee_tBhP5LenmQ0ZNhZlwfRR5VOt9CRIWXTkcbU15bWfP0HNR5G3wPwrdzN5-3rnTKgqs1nUerEPCl1mpriaMu6SONAR4S9nxkn2eKkvcwRNFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛
از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/24973" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24972">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugr73WrLFQw12c-WNW4MrFB8Wt6nT_qIOibBTGZ0a5X51IcJSQblBzUQuTnfyVv5tFv0Hu6y7CvyFp7fJ3VWraaOej5zg4NyQBp--mt0c3SxxhLEQpLjO1ocl5CPDsIc4X-KD_G-OZ_BXbXQgZ07tBMTCjLBAbGTLSFidf5lTZhSgxBP6O5GQjTWOSihVcrfiyv3QV1pdZyeOmF3beFXfpE0-Fq3lgm6E2nEsZ8n7zECIg9RlGFF45rjxrdEKRYxSeMb5qmQC9NmjzNSjr61Hk2KIcA4WRLnfnpS5rQFLFKLPEuwHOSCda67wnAhgb0mDZBrWMD-SDZyDKeD3bTezg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود دشوار و نفس گیر یاران لیونل مسی در دیداری تماشایی مقابل کیپ‌ ورد و برد قاطعانه مراکشی‌ها برابر کانادا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/24972" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24969">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYANmOvRcHJHVVdrwQGSmhOz2uNMeZFECIDyaCZbGm4d7Y-5pWdoHNwIFsnEEHGS_kNULFtvIfcYCihgIgX_zqw2KfYvODwP1Yt4iUDci1RlMhD7EjZ5Kil5N796BXl-j5-sYI7Ht8RWqAW1mjeAvHEvsG7oHa75wH9wgMZAOAEpnYfUBVlvI1X0-OFhJTfAkgYtfIUPra0jRONhoJADnkKYMg1TFOcwXA28lvzsU-faEXyNB7G1_b8mdD4D9VtkKLMyeLe_rlcJ6IBxhSQWgoUU_c7bQ7piKXCwrNcTqdvhN071gp9mOVIp4V2r4i53VHLppeAkC1asr8OzzZByVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الاهلی عربستان؛
ریاض محرز ستاره 35 ساله تیم‌ملی الجزایر از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/24969" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24968">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnkJrZm96yuduonXvAlKoStW0D3qQYcVzWZMjLTr8u6v1D84BSu0yrhTyUbXH5A7Ck0lcKpysWrO2zucVJTNwMLQXDagfjc14sHVPZiFvsMfOJrF-RiZUh1tzb3zTrZk3oLe1X8l-0TGQabDFHu-WRobdkq8gU8osDT1pcGCRsCKdocoMT6SVIVyKmsW_JZG3zwLnyAb3StxxNNeC1_6CQ_n73HsBnP_4ygiLRsxjui1L3hlqrsW7XWO5sKNkDjNRewP5sNBOjvz2XfuLg16LqhkVLHQ_wwgZLSeZp6GyNeNRdWd4XQSuRGUi62WLEVy9vKjd4bAWwuxRN5QgoyYeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/24968" target="_blank">📅 00:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24966">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMKZj1FS5EWOOUPuwEjVtRAGqTc-Jy2EM2TaLrHh2wIvJYfqe4qwOV7o5WoK8zFD6zGKWxe5Incm1Hw8w4Sv4is0ZH733Ub2QOVjoMFJa_rOzBGr3QpjiqiaoRMYpj_Vfg4ZKlVKKPkSBTM57gZUX50MXOqFjWgFUN6VI4Jpb04MO1-BlRQpQsp5h826RUheAcV6S9zhlwCGnlYupeCc0EIW-sz9T8yw-334tGqTh6h545IZAIiBz7Ibj-NIAtwnJ0k-Al_KqnItEsnBSLGl9JK_-QJD1XcPOA46xEZzRorFPzlGFwIb0OVG-z03NWp0qUBoQ1MwvaSKAXm0S3ZrhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/24966" target="_blank">📅 00:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24965">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCVP1tMoCO-TcUgiJ7I4kPz8psD67XNbYZAHX9KWH9XauQK8zfqe2RqAsYWPQiTLWvV0-8yIaQ4KMJnzw4ZvgkexlSJRPMnv7UdCZ7ttdWb20CqRft8K5ymrExqkO8jFJe1HQgu02v5Hor_UZnsjGuOleNcjpG3Ry6seUzlO9epPoeZ5UT2nFJ5ON3uTXhYNME5-QeL_f1hPFLS2HePeh6-tzGgO70FSBleyj_jReetnkZ_wfOjYnXV6isE3rbgSHO1BXjY2pReIm-Tdk--JilUb0Tcg6vlInNVUdKBEHzwwePxlKPmP_ouv704M3Hntwu1BmRNA_7y9JgzI8rucng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/24965" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24964">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VP8MSD_rRdETUNGof3XdY2PcUPbBVqGWgcB-hrWZq6Lk2ChVAF4gEhzXNHbpsQH0hvcKnWIc3_avOKUiBxzYQq3yqa4r5L9ruF0r-D8h-6wo_nEOW6u975HDaIlhRvZK0ZBd5w3tYyxQmScvx56ReElSODhO-g7PMseuDFHxFthkvDq09jwh1Lxx-Tsrz2Fu823m6cymV6WZhX4WIlHde0lqEBLDqAjSWPQ_JnMEoD3rsUf8-1FEgAmOxlrZfPopsyZpx-bseHpvRcmmYNdml2v9QSLzazSrJL_ZgQtZkQSapLcv6eBrWpf659xhW6a3jXEUw8YJNTAtLO47eSepQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
💰
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس با ارسال نامه‌ای به باشگاه نساجی رسما خواستار جذب دانیال‌ایری مدافع‌ملی پوش 21 ساله این‌باشگاه‌شده‌است. سرخپوشان به مدیریت نساجی اعلام کرده که 90 میلیارد زیاده و تا 55 میلیارد ما حاضریم برای رضایت نامه ایری هزینه…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/24964" target="_blank">📅 23:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24963">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPnfhVGT-I-miPbAamOr76jBSkB0yntgrtadTxARuGxoZ6LC__zomXYpyns-qm-g9aclAxIbs9ywqntR2TzsnZNULFgrHuISx0fAijP_LjBhp8P4gOwl-Ic3CQ9sJEvalTQobpxJVAYxGz5PMESDwbsIQ-N40_Ziob-nyYuTGPEIMKZdBAjule0y-RGVpO_WbsYfROe1YaS6olfNB9v81ld9b6Y8g7OTxIjbDvQjhp8YfRByztkEg1J9gC57wVLkzxeGkLUyKwXddCfmfn2nw9i3qDMXFpIvo-VLdzi6tTIM9xOKiR0MAiqgbZGR9GVbpo1ti85gMrxCCQ7BUBt6Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
در بازی شب گذشته؛ این هوادار آرژانتین کیتش رو میندازه برا لیساندرو مارتینز که براش امضا کنه، مارتینز هم کیت رو برمیداره و با خودش میبره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/24963" target="_blank">📅 22:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24962">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5k3UejPYCb9j59JH4ySDqs2IjN5eQFK2phYySMS8xML7AEBx5DMI3MaUmJoj6mRvCoQPlwuWGDgPVy0YB_9wqSHQZ_qAMZ4XKo58g3B0p3NTwubeU00u5Mwfc138GDg2LR2OfzCR0wBpV2mzGxNUawWAIBLir2WfUWOfkF1T1RlZKKNrDsNzvLN4hl1tgJ0tXec9brcYbWj0G3JxUqlMfVsoT9XGTnok-HfaNO5FydfjbFzys0A8nOowT2zgRzhiFd4WnkAJNTBUlDNV-45r5nNlMsInGw3_xXb1JZCXy5DA0yCpKzksdBI07equsqFIAbB9vV15BOwp1OO37prdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24962" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24961">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rquGbh7mWhgWDiMfTl8hmTlvSVUEukKwTjgEKWJhHVRDFjk_TUTFGmL7AlJWXZ9o8n7-0sezg9BXxuGNXBhdqS7aynyvLCSBUUVQRaaASP2Nw08xCr05WRxuKF36E_s9GOOQXdzR9EzFzl7Ri0H36RZlDhHZ995CcA6DXiKhKtgX4211X7l8KhSkCyrT5wUTFRgKV-X9xEjRZs0UwcYGM_5Sd_4IUfDsSnS8dNhgBkjU7mnF42d7oi10h_ylSkzWQ4KDuJ2cgymsNaHc24Te5YTOI3XaI3VX9OqMisxgXRf2Jb3QVt4N2kQBJRgQA-LnbBMdflbCVD6dWzc1DZZDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/24961" target="_blank">📅 22:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24960">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXRGRg23Sjd8N1mEeJYy8sAoWNm9qj7sSOccHvPTLCAvOKDmRxwk5iy2BEt_V8jdRvvS84500hd60DyunCpaJto71LUu_mwrJTSPLudp8MdYCo0lRH2So2BO4QA3SUvvdtaQJnxdPOdj0Mq0mSntWTsQl4_npZ6KRIeduWPavo4l-1EU979BsZOaxsgboESnzH_qF16vcprEBdJjyCzLIhDzfvSEogYOiIXKzwzN_vv1Rhi4Z2RYYdAFT2M6pSKI0sNcaR20bzc790i4bVber0AjAJzUdl_XmUbJzgeQJKk6-zBCQWfO80JrPTKOw16C81bJfjgY8t_M5GDXmGwhAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروه رنار سرمربی مراکشی تونس بعد از دوباره از عقد قراردادش از این تیم جداشد و در حال حاضر سرمربی آزاد بشمار می‌آید. کاش بشه ایران آوردش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24960" target="_blank">📅 21:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24959">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyLXEbiXlak-qcPto3k0u8FSsUzsKwMOxA4s-QYvHOQSFR_hLmZtcw-70SmPNvFLlsPqPkzSEw5MSq45dfZjok7ETcjTIKU67nV7ldQCafUqZYO0B-PW9DLXAumsRUD6yTB8KxOne7Ykg5AvB_SpdPsJi4108pJVMxk16XY4ascHOjZ7iqqE77bf8Bw9lM9PCmPO_PdTzL_8qyDSVwlWPMOei14uvsm0p5J-2zUiYv1h84oBq8O8qfOARZEu-xy9CNdMWHGwPEgPMJrZ3pcdmQtVTnNtlcDBJDvdYaWKdvsWskjK090lDS9zb9zB5Jkh27wqZB4y6O3XaNYOzdpAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇮🇹
🇧🇷
بااعلام رسانه‌های برزیلی؛
کارلو آنجلوتی تصمیم گرفته بجای پاکتا مصدوم نیمار جونیور رو در بازی‌فرداشب‌مقابل نروژ فیکس کنه. نیمار در تمرینات روزهای اخیر با انگیزه بسیار بالایی حضور داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24959" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24958">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkMzId_YSEGQy9WmXUqWgw2UzPsw5HAV8xqo6MZGlp8Fnj65bz3OBttN9N6-7K4yQMfRzA9t9geif5GnDOeZ1RBMEaP8VX_UK61rF0F1LgKDg4AqkodvOW6XNg2Fac9hw6-GbmTGQb2P1TXRx5XgcnT42MH9ukDl0bQI63HTRC5tTfjqwqlom9hFgmWTQF299tN2bjk9NKdXu1E0bPiSVT7y6xweEh88ak2Bmch9-LAiwIhA0RUiGemvi-HrE55bfDsUUHEF_XCFG6_5yJ75gLsNcNAeEcDzeuCOkSrmnx8U_o_VsMOjYYE7LLT1skAKlzWrljh4TjPnd7YN6GkwWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
منیر الحدادی ستاره مراکشی استقلال امشب در تماس علی‌ تاجرنیا رئیس‌هیات مدیره استقلال اعلام کرده تا روز شنبه با خانواده‌اش به تهران باز خواهد گشت و به تمرینات آبی ها اضافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/24958" target="_blank">📅 20:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24957">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJp78DqcgTYgzDG3kYH0duVhsPS6ZhWWkMV1VpPqKSVCB1Edi2ouOXOpUZwWCmTBYlFc1GI6RLSQm9lGw7YMRr0RqNpJXOG56_SyYC1GZdO6SEnA0Ygr6YRf-pB-1H5kLFbYkgUaxJ1cm-CSCdVh6E8vJbaPFBQri9IIKmmTaxEZQ5gM_RGiByX_s0U7nm2cvWwK4vIy7Xd8DJOQqDXdNnPhOUc4IxYHSM4K4O_4QIaqt6ETT_CBpILwstgTQFTdKsT1tU0uCvxyF5HsD-RrcrRpAqf-C2q3YcxWgz7EyKg4J_XQh4t8SVwdqhmY8uZ4znodxsMJfGioikSaaM9Dkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/24957" target="_blank">📅 19:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24956">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgsxB28-iYEkA4hjdcLSpgOQfs7NFai0banTu8YWvSmEe_tn4svkHHyDTkBItOutsu2QSgEsVK07AP-1KpyNvrR5VbX705mFoSJc1Ffsq-h_FqrzrQx2EyGz-6qNTIkzOlE5mO6xtjSJpiSciCl1BF05IDwEF_x4-fYdr7KMMAt0TAXr2vj1Da_jMivwc3Yg3bscJYFyWVBASc8812qiLB386GCBBXl8rrnXb-NEUrypvVaCXTZ3R0i-cXuHwe3ztwSM2p11hdZg77cTBcPYuWop_-E6V4I6njdC7Va1Ict4V2CxUq6I5lE33yFlWgCfrZp-F6rM5oK_JRKZ5MMAOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گلزنان برتر جام‌جهانی در پایان مرحله یک شانزدهم این‌مسابقات؛ لئو مسی با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24956" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24955">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‼️
خودزنی‌خداداد‌عزیزی روی برنامه زنده جام جهانی از دست جواد خیابانی ؛ میگه اگه زنوزی اینجا نمیبود همین‌الان برنامه رو ترک میکردم و به ارواح خاک پدرم دیگر به‌برنامه برنمیگشتم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24955" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24954">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roUZE8KQ2ki5Y_k4E5pIwhf-_apeVQ2IanwP_Y8qJeEq7UjeIcVIxSdov6WPXVxpggFa4xIzBGmEG88eDcZVv37Y2PJdpB_gOlfbUZoZXEbNMvdRcnKFlPo8QgIlnfKZfl7PL0rFsBHcNKLks7kL0iB3-MQztrddM6NuW4N9BOosvrqafb7wCJgxrT8eHPl6NC2kf-09kymmTLJMpTLO7qHr8eqrxJSkjz6t3PFgwCcdQuhDj-kBPZt_ke7HUWCkQHWVsLp5qHZ10Z_NT3JaKLlTat94SVjifrVeeq3BvYTXJT4trbB7JYwyy8kcpPLZWc3I00ZVRFP1QqwHCOtcDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24954" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24953">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDLhybQjdTjEs87aTd5NeqSNfjN9LPosES0KjJzWiJyZuT5vi4l0C-MGpCSf3zPiTwAPPFSVrCHykUcLjZIuXyqJu1pbMvcVbf5RiWZy7qhxdWSS5JgMpsLPG6S8ChUMcRu6IyppMbj31iAvoFwApJDqELj5fjVOA4isbkMG_ntn8N5iFOFC_E-H1AH5isP48OlKT4g87RlMkiDUHTQilIiV8c395SmY3hHfHVgF8rq0133cFaM8VPZ0e4kUTaX_ZHduQZY4D0_5iPuplpUGJTFJdWk-R_shFzcvB1l3FGZ34_kjKU0dhTXeJDf1Lo7gcmG4DFAhIFi9v9VPIZPzpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24953" target="_blank">📅 18:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24952">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvwhO4z2dDlq2VIHe7EM0UJGV43LyfcYGK1bb0N_11FrTKCiVoiaeIxW4rcxIFadpI59oVSRKwfL8Wi1CRWw2EqhQhW_46ZjIQr3YN9M-xvVOW9npdzhLYYrRWprY7r1TbRqt6G8xKRYIAYWigq57egrAq1yuXaoLxbdA-mG_K7hK0rCxMVPlELD4lTOpGyBa_hjp-cpJc5GwnIMa8JMTrr1trGmHU3iFiwtb1QkuacDzV66f6hI185XrJz7zBdRUVN8BlM3szGYIrUXI6KtFKJO8tKMAvLNZPSXoE6vD_on34crV-280PMcbAsyya06tY4CtsxZjyLVY-6DniD_MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24952" target="_blank">📅 18:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24951">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFzA92Pf2_fYgYBB5gZXIE9p9OGXcjthHWA3jMMtLCX0C2mfUYbdi_Hlw-T0usQVmYsy1EhM1qBhfhpBG48KFSjDmvxfrM3FfKmPgQq_vUepjl_rx1M8huflibRRX3E8VwH9XmJh3-kPgP9KuGUCd4t1W6ZfFpO24r-ZWCmVe-erL7UEUg6rjkzjc6pmyF43KVhRUlX-Glx8MFL4-PyPOBb1at3pEIhprbPy6vnvVEu_mKjE08frbIvM5dG_Zehj1wFFPenC81M_5E0ujMp_QSiQNfSytATWA_6zGoZBe9-GeS0wC9pj1TKbVNJqunQpxZV2gvOPu0nkWBy3ExEJzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا
؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24951" target="_blank">📅 17:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24950">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H184aDYbnDM-HI46nbO21yIoCXBStW1wKmAeq5suyTTwGBjaeKpPMe2uL6CemJH8SRrqsNWvEbkyKqT9kFG6nn5ILDI9IYO3s4USwpuOq0SWzHF9GZlpvtHCj1F3gjJMXcIdAKyBFl1gAwr0vhtnIJ1Vk0VoiV8gfA8DTdjlF4e_igMeKbK1sss0-xiSZjV4fLoi8FicAI6I_7yJZLOLDIy5lNmP0TqOYh0rWWzv0t8LsQET6tfVCxpJ-Hh4P73tpkygihmhLiGZ-lREx0iqPpx_MO6NcdyrAtOxTtRBJVtcx-noqHizePsZuiheZQDh9I_KcWvPItQ__SxyADJ4Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24950" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24949">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuYtCdLoOG4A5wmROV_7M_d-mYBRgnsUDXZO9_oTJShOKPuZJPoA5YdaDODvK4Q-4e-EJhfQ61Wtc3-EMkcsLbt36Pm3-Br8ZmjdhyIvJyOo8CgFkpYBXBqvm3s1JiSGXq3rfZ2y6ifw--b5VBgi9xWYoAqQpASZw37P42DDOqXMCpe_8248vBlWsRhxmUU1HHR1Rie5s9hFECHhh4ytwhFHrWqQptCCS9NNi0eryeJB5Ob2YLG96jWYnXqYZQC7TBM9CPxUn0AyXTvYSEgXMEgKJ665Uoirweh12HwCSPkd-vipd2FUCaL6W9QTlS02ewEUSdTTtgUk-rI8ATlopw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24949" target="_blank">📅 17:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24948">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fy2scoyTpNXbW4-_p6lsCTIFmgd6e9Jj2Wwype1Cj7-RLEuWcbOaOtZrH6Xj1XOfciZSNjrlJnB0Ynl37AKCCEa561wO7L8-3clbX5Hl14UgoHuKx96krSceVq9Cb8p9Toc8qf9zN-gqRsd0uDbxQluuKO_3uoT_f7f5h2glR6qggO7vWaOh0u6IpGUHGyF_cRmNYFhhNW4C7uag-OPNqu1NxNgWpH-1oe-fmpcy6s-9T5piKUN3ZHKK2VwX8z-IsrOnz3N7Zhxo-ZQ38-mE0esgg5tPuVuAhHZDLQW5voBp6PA10xD2gT4jEPvhghSU-Y3TQNhDpwAppevswYk77A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
15 تا سیو مقابل ستارگان اسپانیا و آرژانتین در جام جهانی سرنوشت یک بازیکن 40 ساله که تا قبل از جام جهانی تنها 50 هزار فالور داشت رو تغییر داد و به رکورد خارق العاده 20 میلیون فالور رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24948" target="_blank">📅 16:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24946">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pEceeqMyoQaHUiG5sUNv4BLavNyvnXqA8Zimtqoet8zYh4Xy7Oy1nJ4yYFso_3aR7x2IYVOXlXMpRVcCbaP2lDArP90awKcjGdQ0X5L670GaeM0PHMq5pOyogg_jo049u3Pdp-o3L8H4dnAn_L-VDUzLss9i0GR4O-cR9g5wKa9yM_Gels5NskISosiF8VHlZRUH2Z7_2JCHachb0LKuTu7cKaCIYsBUyoU7yynQyBAx1_I76C8thq5goD9YkoZps9sSUwuscqZcpVYDPnlCcZlfIqpPzVFkJ-DhAf_y7lsOCUSLRggRRJ8GavbHPPOaWRY2Dfhb_H6UOECl27HnpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TsMZasjP7O8Qvfo2-O6PK_EBKDSlFnZyb9h6l_SsCoRFByUnW4FQaDk36VsZRtsr9l3WtfgR7o7yRJ3H_PRaq4xng1fjwBCW09YNXyMLzXK7sSRgJHlR92Z-MOV-3JSeU8neAB3ewCNPInH5TGjysO_Jwh7ti1PrBYn-76LvtbCl2SyXu9S8Y0ESD7mqxar4veH0eUpYjsackCAZISGAtG0AqrhoO2NX14UWuxBO1GgIxQ6wU5q_XPj83uTQ8e5NSHL1bYodUP5ENyblNZUyi7b6DDAlD8vhP1CiH1VQGkZtCCXFAeZQu2txhVP71SjqH3ujU_e_eG8ZZ7sYn7eHDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24946" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24945">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpmtMnzpjjXiHZzW4BEF4ksZA2rghV8mgq4Xr4TnZoWwnfofiFAuk1pHkLQ0n-atf_0TqErQH8niSmFdne1ohA8UMTk1kh5HmTyrUH5TOcBvyYNS0YjdpSftZV01lUh9LQ5-r01jDqg8H1_RWJTp4ZZ-eEr4dcLabkPsGWfm6Ujd7KTrReFsjELJ4s8oe5jqnMQoiTlhFt-tdXv91THlncGt5zVuLaejiK0Ob0kuXD1ovLdevkr9y0wYMLWNind4oI9tKprABCEBDFzIdZprWgurk2XCTG5BQ9Wmi_jVtLjHiX7N0Es3ovKfBwYUiyxdUZ_j1LoqdPd1UvSBQnaOBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مقایسه تعداد گل‌های لیونل مسی با پیراهن تیم‌ملی آرژانتین در دو جام جهانی 2022 و 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24945" target="_blank">📅 16:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24944">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT9HDs2aKnkp-ot5jYmifcNSi88vL_62NSWoIMrkqGcG3ArbF9GWwJtHEUHW7ux3qVd2XoYUKIYHWlPFejkjf3nXT8eI905iR_QosNLRq65K_tE8Pm8_8FDbZ_9n2ifdJTa18R-IFuhr77gCBHTQAWFPW_10kLycQzQGYen3GLmHxhlertlUUfzS2y22yxN3z-4uQ4i4mTQL1B2Qm1zFJxBtwePD-Fy_i1QWOQaGLV6vqqa_Q6JCBdr3y9HXLsnF_-Fg0Y6n6IdYHm7SpAfzf8Ss2AAkKdosH__fHb9Tedw-XCNeJRnLUZaB_jZjMGpSjHyRf8zwdu6q-RsYKPVDtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24944" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24942">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHW02WPrQvgwlni-O48HcCT1MCjVTlQlnB3oWrInlCQYubRQAOLvDdsmC06R309b2tjtwIQy8GMBaRblL9yQA7IlF_Ds53go7AYayoWEdBhEuoMQIen6IfFKqUepLliOBWtqxyP1hoNljFB8NhcIUTq6dLkGRQz-8EreF2Ahyb2YtNdDLqLcWllwoq7j3y-Avo-dRT5OVzB44uVw6o4W2vxgWbAPsGm_puF1CxRUpp-u8DBLiwCP6kMK6lbFhcJkQeOvCOrZcMG-TA05HuKNQAkrHIHbL1jm6cK7mTEQJfjxR7qu2WYXhDsvquRQj2ok8cX_FTR9jP1HD1myBe8vIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات
|امیرحسین جلالی‌وند وینگر جوان فصل گذشته باشگاه استقلال خوزستان با عقد قراردادی به‌مدت ۳ فصل به باشگاه سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24942" target="_blank">📅 15:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24941">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6YrDc2kFb8O17H6Rej9jcPCuSCc8n4gcIWiJoYvjZN24yd2Ttt8btPKXI3iJHrVLTi5WmEPg9BkWoXhHt4SNXB4bbKqWyGmf-7COo_hh0MhZaKg6QZcApj6By7tG7bbZQokWPGpjhy8hFVxo3bfxHFNfSkEMB0e4KWSAn7el9iPx3HRMXfP9lb5B670ZCJve6bcFQRvXK3c3lFrMGb73II9SFbZRPrM2lQGn7nH0rFhmNkMiGJfARdV-JMVzIJy1kWt6AavhLw_R51olP_JKNcnkLfSFqU1mFmZBvCw5u6GRypUTMPwjp_CIoDwMKegFiXkuWDzY-63Ay5RmrsTEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه تیم های حاضر در ⅛ جام جهانی 2026 با تیم های حاضر در ⅛ نهایی جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24941" target="_blank">📅 15:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24940">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vqc_hecUWjDL4KHtxbziE3msWF0Wt9evLtI-H9-z43Ij70Qx-622xfNfrOgYN7q6IxbMMkFiibiwY3yNEoucvjNv0Gfl4aXXwxxrjCB-sUUrqOH8yLthT3hvtzbfnUKUGGsy6sLF3zqowWCGMCEGwBsev3z8UxfXMUTIqB9WPk26jOiRGHf5_4tc-zxyihb4DaHoVeYGl4JcXPGpf-J3WJzbdZXVMXM6ZKV3tCfmtRvwhlLdNNrNPiiqG2hZKp3aXh-lLDPgvTpXpSlgU8eUR1_Z0-D6V_0mzKX15RIzJiWCOPTlzAVj6gw2qLv9RjFjyJcf8mDWNHQfNJubdTAodg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
همه از عملکرد نه چندان درخشان بازیکنان تیم بارسلونا تو تیم‌ملی‌درجام‌جهانی2026 حرف میزنن ولی کسی از این حرف نمیزنه که این نبوغ فلیک رو نشون میده که با این بازیکنان تو دو سال اخیر ۵ تا جام‌برده و تو سال اولشم تا نیمه نهایی چمپ رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24940" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24939">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/it3G7HwunODEbiZOX3GMkQ4lmOLqUTeZm83y56wqsMEAwFYNw2ZNYc-0g1kTs9uVKIrrbXKjhNVqKzDdWAS5_mlIqAKho2a_b4wIPL96dAQxfzeEekozx0y2xvVAWthMLMrZparpMwiDM3sOHKfHp0BBXPt6GZg3fDz4vdY6EWGiTZzmNthhRffdNT_rAlMiNx_hCJ2P4Qp3bBVyZcs8X_L_TEkBqbC1y1dBEi6u8vbxjK3xAb9lDQgVv002zJlWQIkSEID35uuIsfuqGcZMb8iLsi85f9nwtwrhjq9Gcwb6Y1L1o8x49YZOgg72fwikftwa1-dXJt028VPfjCUaYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛ لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24939" target="_blank">📅 14:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24937">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q7an411Sn0RWWownX4vnnXnqn51r1yPgGRywkggGSoPxgOY0kyqQcC5YEowC2mIDFKdtu5dK3cj1Ll7Uim7qReSUGuXMXosXJ0slWwgxrSiQxrcEOiuDPHbjJBkNkzafvAmq6S5jbyu-sdytE8CBoxyqehb_RFPBB5cAaW2_lJz4aQUnCN-KVjJVHDe66iijt8FcDBV3vgkwlMHHqj3QwUlsool2uO08XxUAUIa9GmYCSgn8j4oiDC4rmkvr2K72Z91MtTJuxZuq8zUA8h-4gtaBVIrHniAgMm6bqHHimSbkML8WthawofHgfNqsj1SQsQAAj9NszSZjUFNbUTXicQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AK3DcJwlPEG4Oot7UOxrjWT9tAUJG2q2v0beHBFZ2oOxAbrS0AYaYEpx0o8CPKrEY9-HtMF1Xjr6uFi8QzBKCgXilQJ58QnADqfy3gNpUS13CMkFNXVuF4GgvEjmSshJYtvRuo_oZKw7ANGZ3nttvNkVfMyH2p4I2-K-_oedN8v0Cw5t5HreZpYgMl8S3X1VwV8UVYLL4EoPapDrUbuXIeyFysTdy7ItqXcsZ1n0BQJ5zPOviEJPnYEHzjvR4P63FpgaEw9S6jI7tTetHiGVQkPg2L_MtltbUMPG5XMGBplxF1Cwys3D5Q0BhpMYIrGYEDeMbihRmSHYD3VUEhQvHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
احتمال صعود هر تیم به مرحله یک چهارم طبق میزان شرطبندی ها تو سایت پلی‌مارکت:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24937" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24936">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=m9ZITpFC8jR1g7pGrMmJbfJmYSIQi1XvDhQd__b1jTm1G3ggLuoJoXMfZRXHJaeepWwjLsSETqoJgdrdW2Doy3M-NM4AbUTI0n16kqTW3NBw6P_JK3jgCNyQ2OXq8AigIqok10Ty-R3KsgR1AdfRPLyzL9Ia9l7CzZfG17SWzpTV1UApeNqWscLmjFnZjgTvoDdbc3OW79RQqCn6MmuI5omRKt_xGWvf6zxcGX9VE_BXuZYVkvnATF3ZX_oYh4OR9NHN8TpJvQUxklnEJAlqL0ORK1TghPUpfn5rzjwQpgdEwWHzrEjQllp7151c3XL9-hCzG6fC-KGrg6vNP56-9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=m9ZITpFC8jR1g7pGrMmJbfJmYSIQi1XvDhQd__b1jTm1G3ggLuoJoXMfZRXHJaeepWwjLsSETqoJgdrdW2Doy3M-NM4AbUTI0n16kqTW3NBw6P_JK3jgCNyQ2OXq8AigIqok10Ty-R3KsgR1AdfRPLyzL9Ia9l7CzZfG17SWzpTV1UApeNqWscLmjFnZjgTvoDdbc3OW79RQqCn6MmuI5omRKt_xGWvf6zxcGX9VE_BXuZYVkvnATF3ZX_oYh4OR9NHN8TpJvQUxklnEJAlqL0ORK1TghPUpfn5rzjwQpgdEwWHzrEjQllp7151c3XL9-hCzG6fC-KGrg6vNP56-9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24936" target="_blank">📅 13:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24935">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw9s30bToIlJU26OM2oxiKAEPzpX2Lrs1lucneFad0pG_Mfj_ULZqnAi_JhOvFBDHsTIwb7U1YAAMXYF3tdVrYscqM94yTMHrxGAvLYIQeJHJJImOoZ2KTJC2tjcUM6dtIVDGFXB116jewsHAFJnxdPqaxL4cS0YbMj-JF9RSlFjIuYsxiqbd-AAaGVMfZHZ7bZexqKZuZSJG1zvCT2lthljWoPa5-gcK6GkMYe6nVrbdOnq9m_W_cwKNJnLfpF7k365enXAphn5lhqkAzMLoVQhb5t8fuFfUfgZZ9mtvGRHxzZAeovROhcClntFU_TSYzbyd-U9wYfBkcEopMYfEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دیگه با استوری که‌شخص دراگان اسکوچیچ گذاشت همه‌چی‌برای رفقا مشخص شد که اسکوچیچ دریکقدمی رونمایی با پیراهن پرسپولیس بود و هیچ درخواست جدیدی نداشت اما اختلافات بین مدیران بانک شه  باعث برهم خوردن این انتقال شد.
‼️
کانال مردمی پرشیانا هیچوقت خبر رو از روی…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24935" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24934">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKdhArGZZr7qp9M65gB4KMxOzxVcIZPmmPeetrPD1NvXeA74olNXLIfakogzCCnv6x0dsymGrEkjpkVVtUoLvc1aYwuEw4x0Kc-arQViagKFb-gpfw_GvCDqIOw-qBs9C58lNT3mpo4N-Ia0jOfk3rGP6Hn__zPwZBoYVpnSOeUdeDmRC2u8hE4uYmkShu2hzOHTmprdjCezF0pq4BcRStW4cASqLhLIwSlD7_dQMdQfbwE_PDZljElfRk0AwWNZ2JFbycvsBYH5hZKLGJnqLQIyKwdiSUY1rwIIvXS4VFTes25MHjX8CXGrM_NFxu80mvzL7TsOdu5admJTxjUk3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24934" target="_blank">📅 13:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24933">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELpNqeY3y6D9idYZ181qhOUK0ENOEh2sK5nPAd-N9veAUe95O5hQwn01t8iAj5-ixHeovbb-T0SKos-surd1CxwyhNxO6iZBO6pUu4prutm8p6qvN2EbfAN51j0ypxB7guTYsfsiJlwpFFlwH2vf7xeK2_cw86MO11lISaLzUg5dWTTq2reSJjneZCLGDV-mwRLFRj-NR8vqDdqUqBXRNNrHM3iIHM_kwDuKKkHEHM7t5_NGr1s2I_LqJAjNEFWg7zvNVKptf5Vh9jQ1LnDFy8TedI4ZuBA8KZkdygbu0HPL3uhO3CIbbZDcn2TSDxfBxITStKdTukJ-a87e9dd9iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24933" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24932">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXKsstK5M1bDs4quT84Tj8Ul9voqKAEvKA2sXCRMxKXq9l8YUtHdbgQ-4YFeHbAGhAtH1sWAMp1gLh_rrMsME34Alkml58A77dwUw0XmV2o2graLqROlNcHf8yyNvzZp-O87Ktw956fdB5qubFHjfqGGbz0AacVbkeS7CEF8N7QXeEniUEz_Wpn9jaRXHOFYATv3u-iW7imdJH4Wo6KGKFZ7nJuFreErLSr5ccsYfsRvC0iSAKirTFbqoa2sEQ6UXr6G8vTZL79rQQ8QS4va4UhI24nltOMH1MEfpdT5nCAUc7QkLBf_YrAKx7sRZ87-G3tLHQinFYKakeo3-rBp_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کادرفنی‌ مصر برای‌ضربات‌پنالتی پنالتیای کیلیان امباپه در رئال مادرید رو به بازیکناش نشون میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24932" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24931">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfToiTyY-_9Y46RKyTmJVRrtR5TyACIL-r9cdVbrLux9_pbg466snPDLesE5Nnde1AvW9SWEBsmMKSCPZ0k_mr0d3oT69jU4YkvytCQvLKpjIUB8Cde7rU4H7KDkRwDpiyopCc7x-hl64TlN3aUYuQRI-289P7ea6_VXtRlVoH6AdOyA7K55zkk_SA3f0gEoBaxxw2FkGgup7U16SaA_EjpZkZLutpERQ2c8FQLcztKl2L2ZbH9vmL28Ycm_Ctqq_7qBX2by-dQwGDWHd0uM54uEpb_4ZnLFnHtUKyJuGeW5k_rI563-dtuLsos5DBGLzkBgTUiAvBMEbs8xwEExtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبن‌نوس:
هنوز با ژوتا صحبت‌میکنم، چیزی که افراد کمی از آن‌باخبرند. ما یک گروه واتس‌اپ داریم که من همسرم دبورا و همسر دیگو روته کاردوسو در آن هستیم و همچنان در آنجابااو گفتگو می‌کنیم. هر زمان که اتفاق خاصی رخ میدهد من چت‌های آرشیو شده‌مان را باز می‌کنم و برایش پیام می‌فرستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24931" target="_blank">📅 12:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24929">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=q1kA_x3Hbvy8kZGIvJGGkoNdOPknHFH-JdxjXRpx_8VE8MDMNNsz82ttBWwOjhZtmzzLwRaKo7fjs-0vjmTlq8sbWybXSn928ZRQB0xiekPO5Pi1PXmxua3eDbSFOSmTGZBY8xpLTU8B-u_8pwg6Rcl07dk_c8oTeS_m9UbWjtlcJExHM565idDRHakye3CbjvsOXGgrKasV5iOx7YEFWpRlJ3WfP5kY53vE9adBc-c20fPbuPAp3wAqQe-aCnSejaUZ1I7hJEIBDlB_9cHb9tI-qJfO8WTlVVMFDZsBlZPLT_zjYM-n70P2Js5Y7eT6vF7fjV-S1bhv3nEyMDUzSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=q1kA_x3Hbvy8kZGIvJGGkoNdOPknHFH-JdxjXRpx_8VE8MDMNNsz82ttBWwOjhZtmzzLwRaKo7fjs-0vjmTlq8sbWybXSn928ZRQB0xiekPO5Pi1PXmxua3eDbSFOSmTGZBY8xpLTU8B-u_8pwg6Rcl07dk_c8oTeS_m9UbWjtlcJExHM565idDRHakye3CbjvsOXGgrKasV5iOx7YEFWpRlJ3WfP5kY53vE9adBc-c20fPbuPAp3wAqQe-aCnSejaUZ1I7hJEIBDlB_9cHb9tI-qJfO8WTlVVMFDZsBlZPLT_zjYM-n70P2Js5Y7eT6vF7fjV-S1bhv3nEyMDUzSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
در اقدامی جالب توجه؛ مربی مصر قبل از ضربات پنالتی، خلاصه بازی‌های رئال مادرید رو برای تیمش پخش ‌کرد. مصری‌ها این دیدار رو بردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24929" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24928">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=qMzEcrZccWZFvF7s9HosdyyVEJEpil0sFSeyXZijNrI__R2xJN_M2VclArylJiriZO2evvwpQzkxg2DIbSmJaXxPHaMFDoZM5w00VgdTtr3AGGbVsbKsqMbx5gp1bZKbOFI43U9ZjVInhE4WeizF625-3S68HEZz3KKzk1BhXKkov5zKXqEzVTSvNHE28eMzjnVxdcvvApuE3XismtgbdxMehBn3adlb593gnUdSb3GNoqJirZ6Hlbz3c4E3k4iwUItnThP2g2b7wPEuqYPCvhoYpIpz5u_evexIZ2nqCKc0W9SDVi8vXGuL5lAwvphutZOboRb-rz1jmvF0bOr5mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=qMzEcrZccWZFvF7s9HosdyyVEJEpil0sFSeyXZijNrI__R2xJN_M2VclArylJiriZO2evvwpQzkxg2DIbSmJaXxPHaMFDoZM5w00VgdTtr3AGGbVsbKsqMbx5gp1bZKbOFI43U9ZjVInhE4WeizF625-3S68HEZz3KKzk1BhXKkov5zKXqEzVTSvNHE28eMzjnVxdcvvApuE3XismtgbdxMehBn3adlb593gnUdSb3GNoqJirZ6Hlbz3c4E3k4iwUItnThP2g2b7wPEuqYPCvhoYpIpz5u_evexIZ2nqCKc0W9SDVi8vXGuL5lAwvphutZOboRb-rz1jmvF0bOr5mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛
لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24928" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24927">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LedO8ZgOy7jt72d04v9Fcs-5J0iDwEVTqX49PNjihy50ZF_5tEfzI7E0mBRKxGEEoRGVZU8e1yxe4R80LQzqgsq1ul_549C_3OVcXP5Qpl729BU3EimaOmuezY_YbkXQd4JOBmUrFM5hUYwPuy8Ed7ZTnuXDzzdl9xTTagAMmTROL0-j7-VPFWAV1Su_IikKshzy5pTHT0EGMmmhZfHbj23Zt16ffDYgNAAREg2COcwyX3l5sY7ILGwtvjZ-f3TRDrPCmQh0v3AkxWv1yTy7MHOgjUSlUVoZg0sJHtgDiEgz4Jmh_Ma1Rl0AG_080eMEIzBEuoCpSJxVk9I59oGIZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
طبق اخبار جدید دریافتی رسانه پرشیانا؛
تیوی‌ بیفوما وینگر 34 ساله تیم پرسپولیس با باشگاه فولادخوزستان درحال انجام‌مذاکره‌است تا درصورت توافق نهایی شاگرد حمید مطهری در این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24927" target="_blank">📅 11:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24926">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5dJTzCC2FK_c1ZO0TWHlAeyopLF72GHI4y_i38B-8b5rsQwYW15AIPhiA2Kq7xHOl9nhDicQnAwiK5ErJFrAacMDivZvwQGKmGa1XBZeVAL3d9p-d9qhCJJ9vPcEqagbiIHOh1uR_NujQE3gXRgDx2BOawo-WfRfV-iOM1Grv2s1-A4A5PgaugWoiQRW9BpTqfz_Tl0PmUqjOfm3CrpAhgZ34f1TkhCN6t3dJ9wy6GtjbCKAYCSsaigWAlk0mmhCqQfukIWjbnIHMOfSwn82n59WR5nzZVYdP9V9qzUOhrkJ9V5pij6K_zS5kB0nE4U63q-t-9GBqJ3UQiKNIuw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24926" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24925">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9m4C5id-mc1BlTeYZhJWg0xepA2_sdMyQTqSA7dNa6yBMM2em2ScZU6XluZOILR1HSkM0bbxYMO0PH61GGtxtpReKCyFf18s3zigZwGJGLBZSl5QVohkR7BWitG_LAFlQWukBqFyeSu2AuIgxn3XZGcMmWQLtHs6M5JJZRToxuQ1v-Lyvg7oMu4jPc2-HUMmiQZ6-idHLZN6Lki8Scyrb3RlbCuVhwmiOU-UkhwwKjCa70fDBOgWTkYHikD6476MHkHQVnJbMU_3BQ6vgfzW7evdyqWTlCpcmZhooHImAznbRTm1gvY97ZMfVrPIZHmzuhYqHkE90rqj4QIWHLDyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛ به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24925" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24922">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSts9jDWciKHn1y8g13yXBiHgEFy_GISowX_Q6w_dJzgGP8H_JIe9IXEPr36B7rhhV35sZpCYCqoI8F7V9Y5m_z62uI7RkY8wfAKlzYkc9rtbpol49qT8GIQ5oHLU9dB38kcWFzFwmlVUDykzm-HVRxJegPv0NPZLkk6SENUIBNk-MFrsFfXaVK9C3tRcjWLi1vyBQBhuDssrXWpHJjUD1jAkRc-U2oxG_AfKNs_RukxpOUcW4sLnN7hVfKV55OewAEBUIUiB4gpSzcXKfpWlFJrnrpLbpVTCU1LwyhXI8QvtNLUuw29XvTtT04DO11-unjMgvinqyeVNbXI8ISHvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24922" target="_blank">📅 11:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24921">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNMhuSfN1o99W42FubKRYRpqUPkJ3I6XXHOuy-gduTbiB3Pu9idPjsf-Fr4Yyg3jso4bnNmX0zM8bzT1FKFCrcsnVW9qKlQW5GwI88Rv8M8tqG3ORQnExgks5efK0UCurbcf-JcXo9RaJFxnyE6TfzSgOHPkg6OOGY9rKjA4qw0NOqEDWrZ3lB2i2ZIl26mLLjAhieyGctkecPP8Q6XmIROtmkIdCrtX7B7AkoWOxfe0pbmeDoHfgvVNnsujZ6bJV5jpb0QrHIgoY_sn6jAAfOzCmAju_A5ZGqv3-gLOoW90Wu1yQJ-D7qHtw6HCwC4X7bU7wYBDuULzlQ7_M0uhvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های رسانه پرشیانا؛ آلومینیوم رضایت نامه محمد خلیفه رو به 70 میلیارد تومان کاهش داده اما باشگاه استقلال قصد داره با 55 میلیارد تومان این دروازه‌بان جوان رو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24921" target="_blank">📅 10:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24920">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-HfT4fVEv8OROyPsY6Ugma5nQPeFOr7MtrZvHl3j7r7t0qf29N_-PmSZbTU35zLy-bfHi05-PX3VLCDfH5wCdtDVNIbZJfat9oPeK2ef89fAjOzlRb3gV2HNOVQ2Q8_gGMV8TIt9MUy5KO-WjaQNXwWObuK1ubVDq2m7Y6jlU3ZmCqdJvap_hWUZFqgdcYjSzKmX_oh6nlj3VWS4rAMk4_FWtCOXFfFfV9s0f1-6seZAQ4RYYrnDtt0HY_JakzDAWVIPTBPnUoTIcQdXxSyNM-Mt0cFch9fdb9u6z43DQyDMrUQ_FC_IciXCM0LWfroxKrYHH1N842EV8NCpBCx1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24920" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

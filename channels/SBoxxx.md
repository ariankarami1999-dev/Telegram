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
<img src="https://cdn4.telesco.pe/file/vwjiC215YbqQkyJUV1mMPSEWQV976Tmp5QPArP4xUnM0iFjEaEbsWGDUvsd2A4fmRIudEFhkAcHgxozmqWoNn_SJ9PU4oInEwxACsbPx8co0Yf7qtzOOxKTa9L3scnhbQ8D_F7s1z70IJ-RnwUaRznsjhOpoglfpcRAbg8MbInpDeTlcmIu589_UnNyr1xPvuzZsM7bMEkwjghi8BErWPsWZTngJNmhbG_He_LCc17WsVnwl6zGSqyVEi9cEW_KDYMFjQxbXHwyePVdm_OLW8mm86RMwqDmFpTqIkYFvF7iPUnc3YCg7hzjJL2z_XkwMmbja3V0H1BNWqAxg9imUUw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 03:41:54</div>
<hr>

<div class="tg-post" id="msg-21079">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcvgfXt05GRCsRCZZkJL5aoa42M7QVVT7O3JiFRVMtN4iDYAlzTtKW3NWQkBxYU1vZEZfzBGGGJqkItgjWWtrjQCttsykNwfoMT7GR30lJLFXIlApVpqbihcr2JOebWpAC5Wuy8tme08Yi_WnHZm8Od2Fks6GKRkojGhuWeYTwcF6X9t_R9jlqIaO3rqUE-q5DsLg4LmyztIe5QnwJnhlLi9aMFtg-OlHuNjtlVI62tRnSWylT5Gza04qGljNwWucEULnXovm4s-Mggr1CT2_atzdNr06oOX8vLCOt8MmVOpEGOuQ4IAByAvWuIWKWr50HtFhqG4c5rFF8QTQFCCyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
دلار، نفت و موقعیت های معاملاتی گرید از دید موسسه Danske
موسسه Danske با توجه به رشد اقتصاد آمریکا، سیاست انقباضی فدرال رزرو و اثر شوک نفتی، تداوم قدرت دلار و فشار بر یورو و پوند را پیش‌بینی می‌کند.
در بخش معاملات گرید،
GBP/JPY
به‌عنوان یکی از سناریوهای نزولی مطرح شده و ترکیب تحلیل بنیادی و تکنیکالی، افت قیمت تا محدوده 181 را مورد توجه قرار می‌دهد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/SBoxxx/21079" target="_blank">📅 00:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21078">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">— ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/SBoxxx/21078" target="_blank">📅 00:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21077">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هند نیز‌ به محاصره هوایی آمریکا علیه ایران پیوست؛ گزارش ها از توقف پرواز ها میان ایران و هند!</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SBoxxx/21077" target="_blank">📅 00:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21076">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">هند نیز‌ به محاصره هوایی آمریکا علیه ایران پیوست؛ گزارش ها از توقف پرواز ها میان ایران و هند!</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/21076" target="_blank">📅 22:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21075">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POUhsy3uJCgJV6hOshH1ojLyTCN5a3tAIKmgZeyrQLtLbV2hXVonE5xyqowI6nqT_3VdymvAxb72Nr0f3RXUpPSxROguxbD8o95rDmPhYJBq3ywM85PeyMi_Du_AyOIxq4poP8UN56Y_GEdb9QvqlEKyGWdA7FSty9lWJHVY65fGndg3rVFiRb1ryu3zvSeWC6vlCGWtqPXRA90MLl14RoZZ5SqcPlrnPu8ep4tDugVSCLYsVFXjV1Z7z5A8IEoOeTgqy8P2qJoA0TAkerS1gcEHWAelXvteUjDg-mzqrxxdxCCGGAl2gQCg1onYfPyZCeGN-2GbII1_q_80jz-0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت !  فکر کنید پزشکیان بتواند آن ماموت ۱۵۰ کیلویی را با دستانش خفه کند!  اینها شده اند نخبگان ما!</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/21075" target="_blank">📅 20:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21074">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رئیس خزانه‌داری ایالات متحده می‌گوید تمام خطوط هوایی ایران در ۲۳ سپتامبر «بسته» خواهند شد</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/21074" target="_blank">📅 19:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21073">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgSgmbJpRFGNNqXj2Qyi7MuYKpDNlcg_FpwhINYdN8BEz00Yh-i84lUbQ8c_HyMbCYGrR-cZRVGGaeP-p1Gq3dcxPXIk_ui_L9RTja4iXhdzBkkIH7EHrikIQac76iqixvMQuwiAAagkuwD8MmBFXBmuBEykkKXht45MooM4DPbzHkGtPOAtdRZsIwosKkKH17SHRyUimpM9kPX_g8W9bwRlmm5ZXIgYFaowkFGzEaXA9jrr8LemHPYQLntSEZG0xdNmBaW_ENb1YCVZ_k7Iri5JhREQZUUAkDG6PnaFd2POodQr2cFa-snyba2bV4ftjDYwjZelaF_dEbTRbSmIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت !
فکر کنید پزشکیان بتواند آن ماموت ۱۵۰ کیلویی را با دستانش خفه کند!
اینها شده اند نخبگان ما!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/21073" target="_blank">📅 19:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21072">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اظهارات جِی. دی. ونس درباره قیمت بالای بنزین:
به نظر من، همه ما باید این واقعیت را بپذیریم که تا زمانی که ایران در تلاش برای ایجاد وحشت در حمل و نقل بین‌المللی است، ما طبیعتاً تلاش خواهیم کرد تا در برابر این اقدام مقاومت کنیم. اما به همین دلیل است که قیمت بنزین اینقدر بالاست.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/21072" target="_blank">📅 18:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21071">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RG5WZ6NL3idTOViiJEXeUOjW4kIVmHg-pNGH4Qil9Yo4E1NE7Byq5T3PFjwL2ZE2uxdgW_Fhp8PV9oir8vbywpstkyjtxlQ2NDnpjM9lrgsZirLQAS8dVcBCvW5T9UtB9Y-9iELkS9Sw-eo3R5NNUAD23Qh2DePUzP1Wq4et3Ef3Ryvsix1hWrem8QJcfmEOm4BuoayQjZCoYM0t75XfWw4M94NdySdv0s_S2kAgKMjczFBI0_PCrmqN0y7teZA-1VJi581EoKXqLwMOC5VA31s0vOmrjE7HUPdzmfRNNJxUJxUw2Vm6xZwIjIhDewP0eqx0uWjYj3vntbRGuzeBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/21071" target="_blank">📅 17:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21070">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">درگیری های سنگین میان نیروی انتظامی با جیش العدل در سراوان</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/21070" target="_blank">📅 17:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21069">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رئیس خزانه‌داری ایالات متحده می‌گوید تمام خطوط هوایی ایران در ۲۳ سپتامبر «بسته» خواهند شد</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/21069" target="_blank">📅 17:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21068">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">جان کیریاکو، تحلیلگر سابق سیا:
اسرائیل هزاران افغان را در ایران با ۱۰۰ دلار برای جاسوسی به خدمت گرفت.
کار اسراییلی ها اینطوری بود:
«در این گوشه بایستید و هر بار که این ژنرال را در حال رانندگی دیدید، یادداشت کنید و برای ما بفرستید.» بفرمایید صد دلار.
اسرائیل هزاران نفر از این افراد را استخدام کرد.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21068" target="_blank">📅 13:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21067">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiqBHizN7znU1pEOfK0GJgI2GEaD0XWcIi_lpVaUJJgHQsEker774sScC50u_05HOd_P2_ItwBLQ2g_BsNDO_Zb7HjlyGQFek2XDh7ZGeMTCE4E5hyXPVCItn2k5NWtG28KyaHcuDBQmBw5iWuFRbNIT1wVc1SnaUEbx1GEnelSS6fBTm8MV5BIKINOVxeJz3E7mGp78ZcIXVdLDeU4WMt8wC0PORjfLb0Gqdu3FRhONDZIQ4yrAQwJ8z6ANkXZ1iN8419kgsACMJcKhzaku2E7EkgfTsBmzrzX3hKwh0RrhEH1XUQoC7GqwOhzr6NTbHhnkIy8LdMbFOhFJ_7ielQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در محدوده زیر قیمت منصفانه قرار دارد و لذا فضا برای یک رشد در طلا هموار است.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/21067" target="_blank">📅 11:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21066">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJgrsfgNohLPSNmEl-svHoXgv3UQemYXkaq2toixgTzd3yFYKmaP-KZyqoMQGj995HXdEKWC-nbLkMi_-5c6kXue4CiwC-mqCp0cbQQpVQjM3IuyUotnNU6sBDJYzm1xZAq8GE18MGsYFzU55sNDjIpw7-LPvDpJpJ28MHGPYOFja9_vppy8ix3xCiJ5A5kTmy5fJsPaoHERYN5bJUpreIo_xXDx15GZaYegjf8adnhmdre7n4i2_CwbIAmUHZa83rrPB4j43UophUjXpxdUlH6yxtAjQ0ToqGKsUGeA49doPxlImvlh1xLhmHAKVJQ7l-UNkbp0YIALPD2NMpuy2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد و با توجه به افت بهای طلا، به احتمال زیاد دوباره حمله به سقف جمعه و حتی فراتر رفتن از آن را خواهیم داشت (یعنی بالای 4400)</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/21066" target="_blank">📅 11:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21065">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قیمت متوسط گازوییل در آمریکا برای اولین بار از
۶.۵۰ دلار به ازای هر گالن
گذشت. از ژانویه ۲۰۲۶، سطح عمومی قیمت‌ها (موزون با شاخص بهای مصرف‌کننده)
۴.۸ درصد
افزایش یافته، در حالی که قیمت سوخت خودروها
۱۷ درصد
رشد کرده است؛ این امر احساس بحران توان مالی را تقویت می‌کند. دونالد ترامپ، رئیس‌جمهور آمریکا، تمایل خود را برای دیدار با سید پیش‌وا (پزشکیان)، رئیس‌جمهور ایران، اعلام کرد. با این حال، گفتمان طرفین همچنان منفی است. توافق آمریکا با دانمارک درباره گرینلند می‌تواند گامی مثبت باشد (بازبینی یک توافق موجود می‌تواند یک سابقة مفید باشد)، اما عدم اعتماد بین آمریکا و ایران اوضاع را پیچیده‌تر می‌کند.
مِرتس، صدراعظم آلمان، پس از باخت در انتخابات منطقه‌ای هفته گذشته به چپ رادیکال و راست افراطی، سوگند یاد کرد که در سمت خود بماند. به صورت ساده‌انگارانه، نگرانی‌های اقتصادی به نفع چپ رادیکال و نگرانی‌های اجتماعی به نفع راست افراطی است، و روند جهانی به سوی قطب‌بندی سیاسی پیش می‌رود.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/21065" target="_blank">📅 11:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21064">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgAqa2JMgk8gtw2UzjjNokhmbBT_k8BPjQI3v7DF4Ox_XRBV0g2L3bwBFd4l0-zrkvxzmc3VBmUxPHrhVcPSbI15k2qB1EqLvVQ9M1wYBkvFTFMb3miv9aITbIxACFpE_fhBLWUwSN9Vh1ykQ9b-wD6jsJbfdj9N_LMxnmLDCHLL1TeePzj9bvTV3TIVSOFQsoAelPzaCXI6TozzTge9f8FaEZDbthmCE1Fo2TyBB7DBAexMMHN44eLl78KJzvxd7W3dX1gN7X2M-vZjEZGqwfPr48YI-4VKgDlgB4o_Y5BwoY7EdS1ZL9NaC3JZjD2ld0g7udPwosbhfUIE591Umg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین میزان اوراق خزانه‌داری آمریکا را به پایین‌ترین سطح در 18 سال اخیر کاهش داد.
چین بیش از یک دهه است که میزان دارایی‌های خود را کاهش می‌دهد. این میزان از حدود 1.3 تریلیون دلار در اوایل دهه 2010 به 618 میلیارد دلار در حال حاضر کاهش یافته است.
این کاهش پس از سال 2022 تسریع شد، زیرا چین نگران وابستگی بیش از حد به دارایی‌های آمریکایی شد.
دولت‌های خارجی، خرید اوراق خزانه‌داری آمریکا را کاهش داده‌اند، در حالی که صندوق‌های تامینی و سایر سرمایه‌گذاران، خرید این اوراق را افزایش داده‌اند.
کاهش تقاضای خارجی، به افزایش نرخ بهره اوراق خزانه‌داری کمک می‌کند. نرخ بهره اوراق 30 ساله اخیراً به بالاترین سطح در حدود 20 سال گذشته رسیده است. افزایش نرخ بهره به این معناست که دولت ایالات متحده برای استقراض پول، باید مبلغ بیشتری پرداخت کند.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/21064" target="_blank">📅 10:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21063">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ملونی ممنوعیت پوشیدن بورقا و نقاب را در مدارس ایتالیا اعلام کرد
«هیچ‌کس در ایتالیا نمی‌تواند تصمیم بگیرد که یک زن جوان باید خود را پنهان کند. برابری بین مردان و زنان نه در خیابان‌های ما و نه در مدارس ما قابل مذاکره نیست»</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/21063" target="_blank">📅 10:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21062">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اقدام بی‌سابقه دولت الزیدی:
یک “عراقیِ ارمنی‌تبار” سفیر عراق در آمریکا شد.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/21062" target="_blank">📅 10:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21061">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mp_LAEGePwawdTnNJ-3I--dBjycNdAkWnbcE3_Q1kFw6A1-mY1mT5njqcMN13dIswZseZdg3Tbj0J2YVbX1JnMRibfPUiZpk1Dgo_VPntMVMQhAfLVO6xv5M65-scmLoURwkBJIFKpJUvE3h2vyHbr_1SbsOY2vn_Wb9zeI-NSO0PxZU34XUDii1rXY8tZ06x51nBcCYSUfnp8swS0JMtmWbr1HxbAIS67untfFH6vYokSwYBY7LnuFhBi5_sTpsZXJFTyRla6r3TwhbPp6_8bJXkPm_uypvplhTlsWu6JbFCQzFYpTB6-aO2lG62IHf0uxUNBjUoyTONVyYlU1Jmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21061" target="_blank">📅 01:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21060">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یعنی همه چیز دیدیم جز قهرمانی....
هعیییی</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/21060" target="_blank">📅 01:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21059">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21059" target="_blank">📅 01:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21058">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e029fb89.mp4?token=PB4EDuaJmowBFj1sk0rb6UzGqbvxf6Yvdz_99I-UtxXrioS_xEGwBq6kS2OcF7h1U_CbjIbEO18sulPlRe9rpgPTv_XGDqawV1Bwy9zd40etIk0DIrArre54jmBxhjlKPglr7fqCLjcpsB72q6JDkXvNI-WqW0C3YAgNl49c0wXJsSZOY5GU6tXCTZWmrHeSf4w7_u1Cc0-cli8fwbi2UF9CBRfj_4jdlWLJoDFvKG7JYWWtHkkvVyw5EQoq7eztR4NrlMUUGdZw0WBZEzEAhALSTNSCuMYhxG2tlbI98iAdoOIluNB5Fso85QhR0IIPPI_K4S9VDfRtyfvcLDLHpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e029fb89.mp4?token=PB4EDuaJmowBFj1sk0rb6UzGqbvxf6Yvdz_99I-UtxXrioS_xEGwBq6kS2OcF7h1U_CbjIbEO18sulPlRe9rpgPTv_XGDqawV1Bwy9zd40etIk0DIrArre54jmBxhjlKPglr7fqCLjcpsB72q6JDkXvNI-WqW0C3YAgNl49c0wXJsSZOY5GU6tXCTZWmrHeSf4w7_u1Cc0-cli8fwbi2UF9CBRfj_4jdlWLJoDFvKG7JYWWtHkkvVyw5EQoq7eztR4NrlMUUGdZw0WBZEzEAhALSTNSCuMYhxG2tlbI98iAdoOIluNB5Fso85QhR0IIPPI_K4S9VDfRtyfvcLDLHpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/21058" target="_blank">📅 01:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21057">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304c99ed1e.mp4?token=fkL5L6qmavPE-ecckWCyaeWpMvOdcOy4bmIo5iP2muEvlPidC66t8ZLa5RqwHIl_wggUlDOVyTWa-W7vuriyNC1dYBh0yD-yurUmQLVwKu8BGJxXLQ3XlEvIxQ-dPovksEixM3G_GEWD5ho_nXITi72lEW3X7L9jOdFEtgagEhjCCZFf9uEf8-n4UPOCQHr6NSV4s4pOVx9fH1N6XKzy2Hoy6xiY2LhOFRbL2iAq2HDChrl-Jcn7sc-dkHrOHJtVXp2nqyAmrZgASR3wzmqnLo1-G25EsQVst_1rKjGkxSAZ0_Obas_1C3Nvk3fTacLD1wUlknhARAifkS29XcAwxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304c99ed1e.mp4?token=fkL5L6qmavPE-ecckWCyaeWpMvOdcOy4bmIo5iP2muEvlPidC66t8ZLa5RqwHIl_wggUlDOVyTWa-W7vuriyNC1dYBh0yD-yurUmQLVwKu8BGJxXLQ3XlEvIxQ-dPovksEixM3G_GEWD5ho_nXITi72lEW3X7L9jOdFEtgagEhjCCZFf9uEf8-n4UPOCQHr6NSV4s4pOVx9fH1N6XKzy2Hoy6xiY2LhOFRbL2iAq2HDChrl-Jcn7sc-dkHrOHJtVXp2nqyAmrZgASR3wzmqnLo1-G25EsQVst_1rKjGkxSAZ0_Obas_1C3Nvk3fTacLD1wUlknhARAifkS29XcAwxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مستندی جالب از روند ساخت و امکانات شهر موشکی یزد!
بخش عمده اش به نظرم با واقعیت همخوانی دارد اما در بخش هایی از تخیل استفاده شده مثلاً بخش مربوط به نمایش طبعیت و روز و شب برای کارکنانی که 500 متر زیر زمین حضور دارند.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21057" target="_blank">📅 01:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21056">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9JBCPCdKk3RC41NdkWpgDyiPcum1libS-ncWdI7jUgVxZbHtj-3iQVbc7iLDCxRR0pilUHxrC0zqiv2q1ZaEsVnlU78rRAgWihigNOFliQZS3b-6fGlteyxkNXnLXYXiBvVH0YEuS4u0uMXZ7Dqq92XtEc__5Pv86dYaTYYxL3ICDuxf-VWbd4pBCVdTPwao4byvoVzvFakwwDI6tfPYg4tZ9foPQ3JM4x6-747qiFfcDFHqeaMyz8TTNe_3Ejfo8Pa8pyqnZWRFaiXZzSOsRC6KH1_UFB9Ly05NWvYHRSUraPiXtnJ18esQHO9LUqQbGFqN2AmCNVxft9RQCRZIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21056" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21055">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">واقعا تا حالا کسی رو ندیدم  که با این جدیت کصشر بگه
😂
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21055" target="_blank">📅 00:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21054">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7235f04196.mp4?token=fBTwNXcCjHwttN4BkCxfuJuyakLlYqrlpZ240Dy9n8cNarImxjyvxhGgq5z-kPWhhKy9gvLuYz-Kk1dNr72UD0Dy8J-AsCfpmnRpIkHAExcML_FHVIYT4xyQzWOCfCOEgddUSMCRixP3gVyjQAraflulzwUR19EClk07nSbQksfAFjsZOCdjajExA2ytkFXtYTQ_V-UQf85a0oNfitJXAELGUKSgVwQ74p17DaIWQjewgI6cG1RfZyplJD5hGlaMaci25Mo5xGdqXQyoddTM0sgrort5h5KzCS_AXn8s0D7BcmTK9zmcmkRZVr9f76eAgcS0Mp1CVDnYjYiVEt1Cbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7235f04196.mp4?token=fBTwNXcCjHwttN4BkCxfuJuyakLlYqrlpZ240Dy9n8cNarImxjyvxhGgq5z-kPWhhKy9gvLuYz-Kk1dNr72UD0Dy8J-AsCfpmnRpIkHAExcML_FHVIYT4xyQzWOCfCOEgddUSMCRixP3gVyjQAraflulzwUR19EClk07nSbQksfAFjsZOCdjajExA2ytkFXtYTQ_V-UQf85a0oNfitJXAELGUKSgVwQ74p17DaIWQjewgI6cG1RfZyplJD5hGlaMaci25Mo5xGdqXQyoddTM0sgrort5h5KzCS_AXn8s0D7BcmTK9zmcmkRZVr9f76eAgcS0Mp1CVDnYjYiVEt1Cbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا تا حالا کسی رو ندیدم
که با این جدیت کصشر بگه
😂
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/21054" target="_blank">📅 00:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21053">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEjlHCwnvG2N8GdP_bpbrP02l6ohFYdoJwBCy7ynWe8VjYKu5H-udpQQGwdG_MpCW1lbyWnlQ5gq4_J1zTqMERwQ6LDkp3bn71gWFbe1gDf3pNA0GW3TM4ZwJwe4nHWY1lRIpwpa7MmsMqZR-P8lzXbMazjEFaSJzksP-F_sKHPJpWYAA4_j1PhnckEPbDpJ0hS8ceptxvIcjEdPyRGghbRFa8-Y7TGRpXNYiJW2J_-aqqeWN-sRP-s56uy0B1j8RgeGzTyy42CvO1cn7b3vPJZ4FvJ6mtm4hYVSyVDdtYt6M9clqKBUeFBRYyZKlDO23V8raGRFQA8vmFB2cZWwaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/21053" target="_blank">📅 23:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21052">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/21052" target="_blank">📅 23:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21051">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApOA43L2K_25rTOmKH_u3I6c7OS8XE2g0eSRkr-KsTrKQojWnaOpx4cDr0nwgwVA8lzf8X1AiEY5bS4c07XQCNSlm6jiiyt8MxRsUrddwzEcEiXjU0ohYpn6uyVrMCHL6VOlEHKgAJ6uBtIjnMORFUs1AabMhEnMvcsIuvyl8zsu2IS7FD5sh-rBMcBf62AhdfgY4SpppH1ITwPZQruYv0NvAKLOxHedYSj_SfLwh4Loz2QHJ_YGaqFcmu51p-tO3qH7VPKdMtU4LhOT1BLmy8nngnockmTxGFx2v9BJrMhMRYWs4rL2Dr2DnMqvv8zKxSfS0F9eKlNH6CYPXwdvTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21051" target="_blank">📅 23:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21050">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حریم هوایی اسراییل هم بسته شد.</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SBoxxx/21050" target="_blank">📅 21:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21049">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_Zq9aeRhxoQzfnOvcSMpdBRsSqCyajD5zfodqFtKJItv8fgIhk037xgDI32H40nT7mpP2nsYHI0WkgHLSLwNNsjO_ZUgHPnn2siikek2OWp1jjyUJ54ZZYBJ1cyrama3YlGXEGUB1uz13ByZF1NBGhNQEMpuKZDG3MTemr_X83X-5Vc3hkqwXrWO5OFqmVmieBz-ZYMLlO8RiratzV3jMnN08uAmZAjgY2ll1ozSjmJRGJy5p7V4ROm6ps7ltywnwHY9TBLZTwyrAGPuJB2lMhYYiSd5whpM3tvAXomqF0wyIsAoZP4kPt_GPJrm4p_phEs6brEbAfX1odfl3Thbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان:   صلحی که دشمن تو را به آن دعوت می‌کند، نباید دفع کرد</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SBoxxx/21049" target="_blank">📅 19:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21048">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">قالیباف:   هم میجنگیم هم مذاکره میکنیم</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SBoxxx/21048" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21047">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">📌
تخریب تقاضا در بازار نفت و انرژی های جایگزین  شوک عرضه نفت در کوتاه‌مدت قیمت‌ها را بالا می‌برد، اما تداوم قیمت‌های بالا با کاهش مصرف، افت فعالیت اقتصادی و تغییر رفتار مصرف‌کنندگان باعث «تخریب تقاضا» و کاهش فشار بر بازار می‌شود.  در بلندمدت، اختلال پایدار…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/21047" target="_blank">📅 18:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21046">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-zJHMbyO8DblvPAuIGIDQHvp4kub6KtYIbP859TOSUoBCEqe_QAuKsfYCfDW0QE7IEYBZUzrvL5_VjbJ5c0e1vDpOUtyvlcQ6voFn4DmleXq91pHR5jY2a6ZCpel8XbkHVj_hOLR3BNIGYrsJfEVRGYTdiFcpAIgGLWugh2m7ZS_vYJB9iqtPK9iFLGrUzbpTAyFIxAIahb7o9niifha5HgjptL0tYDHdSQcBW96H5T0uQbSH3H2njb4iATn56YhJaF_2VVqTX3Y2dZQQ8mYaUwyvSvnvJm6RVrkdsfcBxIffio5NdFJ8nNR9tYG_zx7zLBnWbWC7IaimF2aKmclA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تخریب تقاضا در بازار نفت و انرژی های جایگزین
شوک عرضه نفت در کوتاه‌مدت قیمت‌ها را بالا می‌برد، اما تداوم قیمت‌های بالا با کاهش مصرف، افت فعالیت اقتصادی و تغییر رفتار مصرف‌کنندگان باعث «تخریب تقاضا» و کاهش فشار بر بازار می‌شود.
در بلندمدت، اختلال پایدار در عرضه می‌تواند سرمایه‌گذاری در خودروهای برقی و انرژی‌های جایگزین را سرعت دهد و وابستگی به نفت و اهمیت استراتژیک آن را کاهش دهد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21046" target="_blank">📅 18:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21045">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ به فاکس نیوز:  برخی از مقامات ایرانی مانند موش‌ پنهان شده‌اند.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21045" target="_blank">📅 17:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21044">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ به فاکس نیوز:
برخی از مقامات ایرانی مانند موش‌ پنهان شده‌اند.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21044" target="_blank">📅 17:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21043">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21043" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21042">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:   گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی #إيران، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21042" target="_blank">📅 17:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21041">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:   گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی #إيران، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21041" target="_blank">📅 17:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21040">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:
گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی
#إيران
، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21040" target="_blank">📅 17:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21039">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رویترز:  در این ماه، ایران فرماندهان سپاه پاسداران انقلاب اسلامی، مشاوران نظامی و تجهیزات مربوط به موشک‌ها و پهپادها را به یمن تحت کنترل حوثی‌ها منتقل کرد.  یک پرواز شرکت ماهان ایر در تاریخ ۱۳ جولای از تهران به سمت یمن پرواز کرد و بین ۱۰ تا ۲۱ نفر از پرسنل…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/21039" target="_blank">📅 17:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21038">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پوتین:   رهبران اروپایی در روز های گذشته به صورت آشکار اعلام کردند در حال آماده‌سازی برای جنگ قریب‌الوقوع با روسیه هستند.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/21038" target="_blank">📅 17:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21037">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">قرارگاه مرکزی حضرت خاتم‌الانبیا:
براساس اطلاعات دریافتی، آمریکای جنایتکار .... بار دیگر تصمیم گرفته است با چراغ سبز برخی کشورهای منطقه، در نشست مشترکی در یکی از کشورهای اروپایی، اقداماتی علیه ایران اسلامی را از سر بگیرد.
هشدار می‌دهیم چنانچه آمریکا علیه ایران اسلامی خطایی مرتکب شود، تمامی مراکز استقراری و منافع آن کشور در منطقه، بدون هیچ‌گونه محدودیت و ملاحظه‌ای، هدف حملات مستمر، موثر و دردناک قرار خواهد گرفت.
اخطار می‌دهیم چنانچه کشورهای منطقه با تداوم سیاست دوگانه در قبال جمهوری اسلامی ایران، با تجاوز شیطان بزرگ به ایرانِ اسلامی و مقتدر همسو شوند، همگی در این شرارت شریک تلقی شده و دیگر نمی‌توانند از نیروهای مسلح قدرتمند ایران انتظار خویشتنداری یا نجابت را داشته باشند.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/21037" target="_blank">📅 14:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21036">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فایننشال تایمز:   عربستان از برنامه تحت رهبری چین که بخشی از تلاش‌های پکن برای ایجاد یک نظام پرداخت فرامرزی جایگزین دلار است، خارج شد</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21036" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21035">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21035" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21034">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">قالیباف:  جنگ بعدی ناوهای آمریکایی را در هر نقطه اقیانوس هند باشند هدف قرار می‌دهیم!</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21034" target="_blank">📅 13:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21033">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">این تناقض را نمی‌فهمم:   از یک‌سو ناامنی در کشور تا حدی است که رهبر حتی نمی‌تواند یک پیام ویدیویی منتشر کند،   و از سوی دیگر امنیت در نیویورک آنقدر تأمین است که رئیس‌جمهور و مقامات وزارت امور خارجه بی‌دغدغه در خیابان‌های منهتن قدم بزنند.   آمریکا دشمن خونی…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21033" target="_blank">📅 12:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21032">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRaefipourFans</strong></div>
<div class="tg-text">این تناقض را نمی‌فهمم:
از یک‌سو ناامنی در کشور تا حدی است که رهبر حتی نمی‌تواند یک پیام ویدیویی منتشر کند،
و از سوی دیگر امنیت در نیویورک آنقدر تأمین است که رئیس‌جمهور و مقامات وزارت امور خارجه بی‌دغدغه در خیابان‌های منهتن قدم بزنند.
آمریکا دشمن خونی است، اما با بعضی‌ها‌ کم‌تر؟
✍️
پسر سوم‌ خانواده تیبو
@raefipourfans</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21032" target="_blank">📅 12:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21031">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">قالیباف
:
جنگ بعدی ناوهای آمریکایی را در هر نقطه اقیانوس هند باشند هدف قرار می‌دهیم!</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21031" target="_blank">📅 12:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21030">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4vCx2cF16aupNj9rs7r-vk4qd--QEdHvwdhDSrlQWP787NkLdotxMKgxVOa_N2-qNLZvsQk-EBgCGhQ8iYLFtgh1hapEFxnPegsxluveOp8vp9Qvph0oiFQIzl1TwKiVh0Y-X6MCKGmdw3kSU_BZAz1jQDW_3o_Tl6Aug_AIa6Em6nloyvuf_dg7b4MRzod4nxTKlz22G6y-3l6N6B2tGMLIeijk6bWPsSSqXprAhNpq4JAYKDGg6nlwvkRYgs9_OKV_HDsd1GAdRJeLO3h6tBz3SwRuBS3X84JLltqvRfgeQH2vfqBb6QN-NaMP86AXQK35Q_yUyV8FfxJga_FLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC نشانگر نزدیک شدن طلا به محدوده قیمت منصفانه است و لذا از حالت حباب منفی ارزشگذاری فاصله گرفته است (به دلیل رشد سنگین از پریشب) هر چند هنوز تا تشکیل حباب مثبت و بیش خرید بودن فاصله زیادی دارد.  پس بهترین استراتژی برای امروز:  خرید…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21030" target="_blank">📅 11:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21029">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کانال 14 اسرائیل:
آمریکا گزینه‌های حمله احتمالی به یمن را بررسی می‌کند</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21029" target="_blank">📅 11:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21028">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_GPCYxxEQx765jDwyNseVxokCQzRfZ8NtkJotFUU28Mm04yQBXj9trnURvBtyQsO-Ia0-J-sO-B8X_XG53ES4kaoeNO9BroRco6dBeCD4pjQrnfvuhQAq5OH8-9IJcAkYbHNY8DeaOfSd5noeNGuBizWfx_sHpjTbr2t8R3PuH03fR2ZOS7RPESABtXjsMtiQEzcWdSk_9J2AuDyAjBS1yrvooTl5oTmc4O9H8h_DvrmoLDemkMV3kmHdk_4II9ZbmldzP865juvlElK5FcOE9RZ5MnCfXU97wTh-ZiUIjdGAxQ72lnCNn5uv3Cl1qQrMa3ESi8tR1Gg1wW0PdaXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حمله پهپادی گسترده در طول شب به مسکو و منطقه مسکو، در روز پایانی انتخابات پارلمانی روسیه، انجام شد.  یکی از برجسته‌ترین اهداف، پالایشگاه نفت مسکو در کاپوتنیا بود که صبح امروز آتش سوزی بزرگی در آن مشاهده می‌شود.  ظرفیت پردازش این پالایشگاه حدود ۱۲ میلیون…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21028" target="_blank">📅 10:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21027">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یک حمله پهپادی گسترده در طول شب به مسکو و منطقه مسکو، در روز پایانی انتخابات پارلمانی روسیه، انجام شد.
یکی از برجسته‌ترین اهداف، پالایشگاه نفت مسکو در کاپوتنیا بود که صبح امروز آتش سوزی بزرگی در آن مشاهده می‌شود.
ظرفیت پردازش این پالایشگاه حدود ۱۲ میلیون تن نفت در سال است.
آخرین بار در ۱۶ و ۱۸ ژوئن به شدت مورد حمله قرار گرفت، زمانی که هر دو واحد اصلی پردازش نفت خام آن آسیب دیدند و پالایشگاه مجبور به تعطیلی شد.
تا ماه اوت، گزارش شده بود که توانسته بود تنها با حدود یک‌سوم ظرفیت خود مجدداً راه‌اندازی شود.
اکنون دوباره مورد حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/21027" target="_blank">📅 09:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21026">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4607a666c6.mp4?token=nJO2_q2Ua2gwCdrsC3-AnrwXlG5OBCYDOx5FsYAcKlm5NsAUCNE-3zVvin8qRdrw7oAL7lMQ1R2-EWcWSw4UkAs9PNw64_Jv5pEcDWghXxKyGH2KmnP2Z27vap7g_btk4JXmoL07A-0g-xYdJPFekyJs3NVBUfJL5kfTUFMZvV-G1sViGMS6830Z-9kINeQsqm8kPG3C0PBI-ADwQ2XNjUXKF1r1tVnE8W6azQHWmUSDBbpgA-lPfUeK2yZH-YEZLSJ5zexYRvMCu0OMWZDrrk_Ig5UHUNgkLqmyR6Y2XP6wd3FeZVRB-yEi5uDUpMEl6Hhw6jPJHVZk9PB3_kXM6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4607a666c6.mp4?token=nJO2_q2Ua2gwCdrsC3-AnrwXlG5OBCYDOx5FsYAcKlm5NsAUCNE-3zVvin8qRdrw7oAL7lMQ1R2-EWcWSw4UkAs9PNw64_Jv5pEcDWghXxKyGH2KmnP2Z27vap7g_btk4JXmoL07A-0g-xYdJPFekyJs3NVBUfJL5kfTUFMZvV-G1sViGMS6830Z-9kINeQsqm8kPG3C0PBI-ADwQ2XNjUXKF1r1tVnE8W6azQHWmUSDBbpgA-lPfUeK2yZH-YEZLSJ5zexYRvMCu0OMWZDrrk_Ig5UHUNgkLqmyR6Y2XP6wd3FeZVRB-yEi5uDUpMEl6Hhw6jPJHVZk9PB3_kXM6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت امروز من در بازارهای مالی
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/21026" target="_blank">📅 09:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21025">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d8265c9ad.mp4?token=i1fGbQLuEtxTUM94iLcDVZL-DD2Om8DLVGhhU0USN2VoxGq4rZnAnxPcZdjxkgAHMht87WYwFv1CpBRmJ1AttyBxS2UE2eG64RF3vFAnHOzZ1Zc9doPIaCL8JFtw8B7Dw0YPGltSwbV9H2C9LNks8BryK3aBZSi5OgmZmyNVwuwO86EG5JZGhATB0mzPxYn2v1I2tbG_LewH8BQxlMfkyIqo48tSPoYx0KnL0_Nl5RscD0SAIOlJU_q4ixFyLWz7ODPfI-4weodd7wLrqEC5Ny-lvmWJ02aqd5SBC8HZ5V11_v8twzM2xwubOx54hjVINLkrdOHEcMu4_qOqPpUJ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d8265c9ad.mp4?token=i1fGbQLuEtxTUM94iLcDVZL-DD2Om8DLVGhhU0USN2VoxGq4rZnAnxPcZdjxkgAHMht87WYwFv1CpBRmJ1AttyBxS2UE2eG64RF3vFAnHOzZ1Zc9doPIaCL8JFtw8B7Dw0YPGltSwbV9H2C9LNks8BryK3aBZSi5OgmZmyNVwuwO86EG5JZGhATB0mzPxYn2v1I2tbG_LewH8BQxlMfkyIqo48tSPoYx0KnL0_Nl5RscD0SAIOlJU_q4ixFyLWz7ODPfI-4weodd7wLrqEC5Ny-lvmWJ02aqd5SBC8HZ5V11_v8twzM2xwubOx54hjVINLkrdOHEcMu4_qOqPpUJ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله موشکی دیروز حوثی ها به فرودگاه ریاض</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21025" target="_blank">📅 09:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21024">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ecd762d60c.mp4?token=uYEfM02fWjiRZ6LLlh-XIE7xGreNMVJ99nds7lTXJ9DtBOKiFzC9hWtrTSwscVderSfJABEHzPp7bsKm-Mg5VCfRtH3IbDqtuDrzVO3pY0h_NYTErHTz8ZvcOdEy5zQbUo2wX8CfIn7E7EeR8atlZzC8-CW9Okxsd1jXRVMcYiSQ3-NyKuFlejGSwgXyO1_nLicJAWcfYdGCN757S6J94Ss-7i0OO_hEwGlUxNVDkKSToBsd7MGBMZJf0bIfWvADu3iY7iW_gXSkSA2ZE0nsVakVFATFeijVJsll0GRKkk4_L4BBpWlRPXrXwj8mlEMZBKt_R0JMHJGTVQ1rR-THcA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ecd762d60c.mp4?token=uYEfM02fWjiRZ6LLlh-XIE7xGreNMVJ99nds7lTXJ9DtBOKiFzC9hWtrTSwscVderSfJABEHzPp7bsKm-Mg5VCfRtH3IbDqtuDrzVO3pY0h_NYTErHTz8ZvcOdEy5zQbUo2wX8CfIn7E7EeR8atlZzC8-CW9Okxsd1jXRVMcYiSQ3-NyKuFlejGSwgXyO1_nLicJAWcfYdGCN757S6J94Ss-7i0OO_hEwGlUxNVDkKSToBsd7MGBMZJf0bIfWvADu3iY7iW_gXSkSA2ZE0nsVakVFATFeijVJsll0GRKkk4_L4BBpWlRPXrXwj8mlEMZBKt_R0JMHJGTVQ1rR-THcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/21024" target="_blank">📅 08:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21022">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ می‌گوید باسن ملانیا باعث «نجات» هر دوی آن‌ها در پله‌برقی مقر سازمان ملل شد.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21022" target="_blank">📅 08:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21020">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزارت خارجه آمریکا به تمام شهروندان آمریکایی اعلام کرد که سفر هایشان به خاورمیانه را فوراً لغو کنند.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21020" target="_blank">📅 02:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21019">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">محسن رضایی:   محل تپه علی طاهر پیش از حمله تخلیه شده بود و عملیات دشمن شکست خورد</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21019" target="_blank">📅 00:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21018">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران، از آزمایش یک موشک ضدکشتی که به 80 گلوله تقسیم می‌شود، خبر داد.   به گفته ایشان، این آزمایش بر روی یک ناو هواپیمابر آمریکایی انجام شد و با توفیق الهی به نتیجه رسید.</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21018" target="_blank">📅 00:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21017">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران، از آزمایش یک موشک ضدکشتی که به 80 گلوله تقسیم می‌شود، خبر داد.
به گفته ایشان، این آزمایش بر روی یک ناو هواپیمابر آمریکایی انجام شد و با توفیق الهی به نتیجه رسید.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21017" target="_blank">📅 00:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21016">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">موسسه مطالعات جنگ:
طبق اظهارات مقام‌های آمریکایی به Axios در ۱۵ سپتامبر، تعداد عبور روزانه کشتی‌ها از مسیر جنوبی، با انجام موفقیت‌آمیز عملیات نظارت و مین‌روبی آمریکا، به حدود
۴۰ درصد سطح پیش از جنگ
بازگشته است و عبور کشتی‌ها هم در طول روز و هم شب انجام می‌شود.
عربستان سعودی نیز بنا بر گزارش‌ها صادرات نفت خود را بار دیگر از مسیر تنگه هرمز منتقل کرده است. بر اساس اطلاعات منابع تجاری که رویترز در ۱۸ سپتامبر به آنها استناد کرده، عربستان برای بارگیری‌های ماه‌های سپتامبر و اکتبر حدود
۶۰ میلیون بشکه نفت
را در بندر رأس تنوره در شرق عربستان بارگیری کرده که انتقال کشتی به کشتی آن از طریق تنگه هرمز انجام شده است.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21016" target="_blank">📅 00:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21015">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c95cb0fd.mp4?token=QSqZt9BR1jb6EjSJsEjQuLSgvW-oLD52_XVt2XJYEb0i573_5RegtSXQHHcugnBb5rHr2-u9Q7hIpFG32h2FrqdZSgaa3d9jSs3NOvsfip9PAiu3KlaxbHIWwrxzQYgo67GcSRcCBH_9GNuBV_7XfX9OwFjZ9PTqqbzz1jLgXCZT_78w1-j2ieIeh1ykxlsBWkmdHu4BNV1XDR6FA9yQhF9tceYDNz-k17kEz3EKyys57gSKPtwtgybyRo3ma8qnjWGgWBnQsEIpTut3DaksT_pn7vXPydmjrwsr2Hxr4_aiOV_CKZhvQt93wiqBDhLhTx4epV2se1_6Yg-0Z9sIKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c95cb0fd.mp4?token=QSqZt9BR1jb6EjSJsEjQuLSgvW-oLD52_XVt2XJYEb0i573_5RegtSXQHHcugnBb5rHr2-u9Q7hIpFG32h2FrqdZSgaa3d9jSs3NOvsfip9PAiu3KlaxbHIWwrxzQYgo67GcSRcCBH_9GNuBV_7XfX9OwFjZ9PTqqbzz1jLgXCZT_78w1-j2ieIeh1ykxlsBWkmdHu4BNV1XDR6FA9yQhF9tceYDNz-k17kEz3EKyys57gSKPtwtgybyRo3ma8qnjWGgWBnQsEIpTut3DaksT_pn7vXPydmjrwsr2Hxr4_aiOV_CKZhvQt93wiqBDhLhTx4epV2se1_6Yg-0Z9sIKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجه ترکیه گفته که ترکیه می تواند نیازهای نظامی سعودی را برطرف کند!  یعنی در این شرایط که عربستان بشدت به نیروی نظامی نیاز دارد هم ترکیه دست از بازاریابی برای سلاح های ساخت خودش دست برنمیدارد!</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/21015" target="_blank">📅 00:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21014">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/en9R386H7sgkuIvaYn0_LnkoSJ6O88xkpdhqRoq3fyy0PiHBaVoIBcNkaSpesKHikbypL6SOvm8sTAjEI7SwUrx_KHslpCqfqptDfHh8c28vSbv0PQGKj2dpRZ4XcjYpSFn5lYJyrD0QAvxlUKACqERnuNRcDWoddcprxAshV4nroQjeVUJasPMDrts1kP1gy5BIAFwXhknrXWhINNBSjPKEjTSVQbe1uWt1EF9YTCn8Z0FobfKzF6gt7SaeHczkwpA9KA05NSERpGU83H_cAoED0gve-HIlACD0eRVwTRRnT_2JdNTIyMmeAT2jAnEOUCmPVhPz52Po1egacj3q3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو دفتر سیاسی انصارالله:   این پیام به ترکیه و پاکستان ارسال شد که به خودتان احترام بگذارید؛ اگر از عربستان سعودی حمایت کنید، ما به شما حمله خواهیم کرد و شما را تنبیه خواهیم کرد، و دست‌های ما از فولاد خواهد بود</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/21014" target="_blank">📅 00:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21013">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W83FiNUu2NcGyFibL2X1tVSuYgEdYlru-muAPRzX9Ke2kJwYwvxJQO6iiZ9kADQudwNj8L5dBXKLoMo0g4F2ikrOQh4tBombha8WmDY-bFiEG8eVOXyBghtEpqwCF2kh-X2sjQMtOsOVAMJh7cAktCeQSK624y9jUn1JO3A3tkrdl2a9fFBNRD74Ejktc3YNmRFfByj-8z8wTAW8Ow6hbIpNzjCvq0fOsqDucAIjB995ndzNuYaRF1WklRM2m5jyygu2W7AHKDokxUmiZZJDSQX2wOeC2cSAYo_zTUK1ZYYBrSU088PgKK92b8f40Y24pHkCtjC8A94sL_DiufVsWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:   خواهان پایان جنگ میان عربستان سعودی و یمن هستیم و معتقدم یمنی‌ها نیز خواهان دستیابی به توافقی با عربستان هستند</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21013" target="_blank">📅 00:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21012">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">عضو دفتر سیاسی انصارالله:
این پیام به ترکیه و پاکستان ارسال شد که به خودتان احترام بگذارید؛ اگر از عربستان سعودی حمایت کنید، ما به شما حمله خواهیم کرد و شما را تنبیه خواهیم کرد، و دست‌های ما از فولاد خواهد بود</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/21012" target="_blank">📅 00:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21011">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">صداى انفجار در تنگه هرمز شنيده شد
گزارش‌ها حاکی از شلیک موشک‌های کروز ضد کشتی به سمت شناورهای متخلف در تنگه هرمز هستند.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21011" target="_blank">📅 22:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21010">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">درباره دیدار مهم رهبران چین و آمریکا
دیدار دونالد ترامپ و شی جین‌پینگ در ۲۴ سپتامبر در واشنگتن، در ظاهر یک نشست دوجانبه میان دو اقتصاد بزرگ جهان است، اما دامنه پیامدهای آن بسیار فراتر از روابط تجاری آمریکا و چین خواهد بود. در شرایطی که جنگ ایران، بازار انرژی و رقابت فناوری بر اقتصاد جهانی سایه انداخته، این دیدار می‌تواند یکی از مهم‌ترین رویدادهای ژئوپلیتیکی پاییز باشد.
مهم‌ترین موضوع برای بازارها، احتمال تمدید آتش‌بس تجاری آمریکا و چین است؛ توافقی که در ۱۰ نوامبر منقضی می‌شود. مذاکرات مقدماتی اسکات بسنت و هی لیفنگ در نیویورک نیز نشان می‌دهد که دو طرف پیش از دیدار رهبران در حال تلاش برای حل اختلافات مربوط به تعرفه‌ها، مواد معدنی حیاتی و دسترسی به فناوری هستند.
اگر ترامپ و شی بتوانند حداقل یک چارچوب برای ادامه این آتش‌بس ارائه کنند، نخستین واکنش بازار می‌تواند کاهش ریسک تجاری باشد: سهام و دارایی‌های پرریسک حمایت می‌شوند، فشار بر زنجیره تأمین کاهش می‌یابد و بخشی از تقاضا برای دلار به‌عنوان دارایی امن می‌تواند تخلیه شود. در مقابل، شکست مذاکرات یا تهدید به بازگشت تعرفه‌ها می‌تواند مجدداً سناریوی جنگ تجاری، تورم وارداتی و اختلال در تجارت جهانی را فعال کند.
اما مواد معدنی کمیاب شاید از تعرفه‌ها نیز مهم‌تر باشند. چین همچنان اهرم بزرگی در زنجیره تأمین عناصر کمیاب و مواد حیاتی مورد استفاده در خودرو، نیمه‌رساناها، هوافضا و صنایع دفاعی دارد. آمریکا نیز در مقابل، محدودیت دسترسی چین به فناوری پیشرفته را در اختیار دارد. بنابراین این دیدار در واقع مذاکره‌ای بر سر «اهرم‌های استراتژیک» است، نه صرفاً تراز تجاری.
برای بازار طلا، نتیجه اهمیت ویژه‌ای دارد. کاهش تنش تجاری می‌تواند بخشی از صرفه ریسک ژئوپلیتیکی را کاهش دهد؛ اما اگر نشست به بن‌بست برسد، هم ریسک تجاری و هم تقاضای پناهگاه امن می‌تواند افزایش یابد. هم‌زمان باید نرخ‌های آمریکا را در نظر گرفت: اگر توافق تجاری باعث تقویت چشم‌انداز رشد آمریکا شود و بازدهی اوراق بالا بماند، اثر آن بر طلا الزاماً مثبت نخواهد بود.
ایران؛ مهم‌ترین بخش پنهان نشست
ایران احتمالاً یکی از موضوعات حساس مذاکرات خواهد بود. واشنگتن از چین انتظار دارد در فشار اقتصادی علیه تهران همکاری بیشتری داشته باشد، در حالی که چین همچنان بزرگ‌ترین خریدار نفت ایران است و روابط اقتصادی نزدیکی با تهران دارد. گزارش‌ها همچنین از تلاش آمریکا برای اعمال فشار بر شبکه‌های مالی مرتبط با تجارت ایران حکایت دارد، هرچند واشنگتن تاکنون بانک‌های چینی را در موج اخیر فشارهای خود به شکل گسترده هدف قرار نداده است.
برای ایران، اهمیت نشست در این است که چین می‌تواند بخشی از اثربخشی تحریم‌های آمریکا را خنثی یا تشدید کند. اگر پکن حاضر شود در زمینه نفت، شبکه‌های مالی یا دور زدن تحریم‌ها همکاری بیشتری با واشنگتن داشته باشد، فشار اقتصادی بر تهران افزایش خواهد یافت. اگر چین در مقابل، بر ادامه تجارت انرژی با ایران تأکید کند، یکی از مهم‌ترین کانال‌های فشار آمریکا محدودتر می‌شود. همچنین شایعاتی درباره کمک اطلاعاتی چین به ایران در راستای دقیق تر کردن هدفگیری موشکهای ایرانی منتشر شده که احتمال بحث طرفین در خصوص آن می رود.
از منظر بازار انرژی نیز موضوع حساس است. هرگونه توافق آمریکا و چین که به کاهش تنش‌های ژئوپلیتیکی منجر شود، می‌تواند از صرفه ریسک نفت بکاهد. اما اگر ایران در مرکز اختلافات آمریکا و چین قرار گیرد و هم‌زمان اختلال در جریان انرژی منطقه ادامه پیدا کند، نفت می‌تواند دوباره تحت تأثیر ریسک ژئوپلیتیکی قرار گیرد.
در نهایت، اهمیت واقعی دیدار ترامپ و شی شاید در یک «توافق بزرگ» نباشد؛ بلکه در این باشد که آیا دو طرف می‌توانند رقابت استراتژیک خود را مدیریت کنند بدون آنکه وارد مرحله جدیدی از جنگ تجاری و فناوری شوند. برای بازارها، همین تفاوت میان «مدیریت تنش» و «تشدید تنش» می‌تواند مسیر دلار، طلا، نفت، سهام و ارزهای آسیایی را در هفته‌های بعد تغییر دهد. برای ایران نیز سؤال اصلی این است که آیا تهران از رقابت آمریکا و چین فضای بیشتری برای مانور پیدا می‌کند، یا اینکه واشنگتن و پکن در نهایت بر سر اعمال فشار هماهنگ‌تر بر اقتصاد ایران به تفاهم می‌رسند.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21010" target="_blank">📅 21:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21009">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ممکن است برویم یک نایت کلاب اما آنجا شربت بیدمشک سفارش بدهیم !</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21009" target="_blank">📅 21:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21008">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">محسن رضایی :
دکترین هسته‌ای ایران تغییر نکرده، اما خروج از NPT ممکن است</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/21008" target="_blank">📅 21:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21007">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbEmLEzgRFKYsVDdol_7lK6xMmRbCSUoatyzieCmi5aMSO_Epd-GPDHqEroEDAbAtLWn26T68PzZIfqA5GjYgIkRds5ksRf8d7GU6CXEGUOWyNXZ1TNe2doDdFUGYsAzHxcXtC6CwD5liMfINIWkWUhRoLKrnaE7mRv0ti3Fn1o0ZCyKlwFnKX940-s0BwE7CXBc43uzqkV3Bh7imd70ZylJsnji5tQXmLs0Xa3Mx6P8y4fgxJHn9K7WjAEXcMZ6E8OsfoN-EjS9zaSdRsSFMPnAJXKn9aukF70gmpc9p_Mv6uJ86WvdHhrITpnGOOLhQ1Y1IVYNk3lhtENYCYC0Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب امروز و بعد از ۹ ماه تارگت ۲۴۰ هزار تومانی دلار محقق شد.  بعید نیست مدتی رنج بشود.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21007" target="_blank">📅 20:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21006">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21006" target="_blank">📅 20:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21005">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">محسن رضایی:   خواهان پایان جنگ میان عربستان سعودی و یمن هستیم و معتقدم یمنی‌ها نیز خواهان دستیابی به توافقی با عربستان هستند</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21005" target="_blank">📅 19:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21004">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">📌
جنگ ایران؛ رشد و توزیع ثروت و درآمد مصرف‌کننده آمریکایی و چالش فدرال رزرو  با وجود فشار تورمی ناشی از انرژی، درآمد واقعی و ثروت خانوارهای آمریکایی نسبت به سال گذشته افزایش یافته، اما بخش بزرگی از رشد ثروت از افزایش ارزش سهام و املاک ناشی شده است.  این نابرابری،…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/21004" target="_blank">📅 19:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21003">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvNram43RQVuUd0onC_skbyv6pCwi4f6ys2V5WxaCrZfzWyQ7eWmdhq3iOK1nIAcDY1DNqw7q4secMO9nx7DRmtuzbAelLviPIFs4ZjpxwcuGVoMO8kpRjFmizffHkt_Vj_NBWvM76C9FpQwQOe-O5EuS_AFXZZVLwmtqmC77zCDsDL2YqmSdvBGI1QPIGI9S84ALFq49OfTJIWvCFGbnYHJWSyuS_Pbv9_4vDA2XLb5DKHeKzGPyMAyClduvdr8SKD2IzPqdQhTL8PlrU2L8_TtAbivD3E4lMeYQZSs5BHYiGgE7wA-uqtUHWWedhomITWZhlcGrh66ApRdMKecdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جنگ ایران؛ رشد و توزیع ثروت و درآمد مصرف‌کننده آمریکایی و چالش فدرال رزرو
با وجود فشار تورمی ناشی از انرژی، درآمد واقعی و ثروت خانوارهای آمریکایی نسبت به سال گذشته افزایش یافته، اما بخش بزرگی از رشد ثروت از افزایش ارزش سهام و املاک ناشی شده است.
این نابرابری، چالش مهمی برای فدرال رزرو ایجاد می‌کند؛ زیرا رشد دارایی‌ها می‌تواند مصرف را تقویت کند، در حالی که افت بازار سهام می‌تواند همین اثر را معکوس کرده و به کاهش تقاضا منجر شود.
🔗
ادامه یادداشت از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21003" target="_blank">📅 19:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21002">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">محسن
رضایی
:
خواهان
پایان
جنگ
میان
عربستان
سعودی
و
یمن
هستیم
و
معتقدم
یمنی‌ها
نیز
خواهان
دستیابی
به
توافقی
با
عربستان
هستند</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/21002" target="_blank">📅 19:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21001">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKUfsQ_fA6WPSIPWbV_QDAZ8io3v533n3H7MklYxYJx0WW-T3QiDBoL28DxSt6XOmMJ0DtWDP_s6DnJbOlXLOToIGGpBn8WLcmmLg3IysCUVDG2k4xT2AlN2wTbAUPLg0RQ9-AFODk0kzHPoYSgASt0hUQxLsIrlIKsSWRhn6xgwTFriQbamFMwpGTF1HvZ1nvF2D0QTUUx1NAt7X6UF6h4RwaxmbdyqUWHx9r5JLJHsgnte7mUqlbq298NxdjWIIdmCMo7XLtwVzyi9WVDaoJRoteRRXI9IQGFG12A4vc70JqCxpcIUETGWGChdfW6pvevFK3WCjmPIn6GxWYqhtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین وضعیت نتایج احتمالی انتخابات میان دوره ای پیش رو در آمریکا</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21001" target="_blank">📅 16:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21000">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">WW3 is loading....</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21000" target="_blank">📅 16:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20999">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20999" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20998">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:   دخل و خرج زندگی مردم آمریکا با هم نمی‌خواند</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20998" target="_blank">📅 15:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20997">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:
دخل و خرج زندگی مردم آمریکا با هم نمی‌خواند</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SBoxxx/20997" target="_blank">📅 14:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20996">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bI68FiAPssg5Ia40N1uMU7I5UwCRISeMeqSPqU6EcJ6cOjxo60ONQw1K4v3zpzxDK1KdhVCGu9CamqdWLulxAyyyAMDJCsS5Nzp79TpRF7OjZ8NefdAqE1UV8utPIdBlRWGREjPwQqoeTuV1dcPmGp_Zp8bgGmL030gotyR4YH6HarrjoLF_lClBwftTrgzaQxk2YNR8ChuheHYGNeaYbRIuhaQ0wxemkbrOHz0j5YUMLjcSMJjWdb7wScgIdf9_IOrZAeHeiVZ99GoSWVj-4nT99-trDzx0Vki_KaVgft2tsiJfjVIE8KacBsToT46ojXFTZYqIWq0_qifmT0aq7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش های موثق، ترکیه چندین پهپاد رزمی و شناسایی برای کمک به سعودی ها در جنگ یمن ارسال کرده که دستکم یک پهپاد کارایل توسط حوثی ها سرنگون شده است.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20996" target="_blank">📅 12:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20995">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترکیه مجوز فعالیت بانک ملت ایران را لغو کرد</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SBoxxx/20995" target="_blank">📅 10:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20994">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آمریکا بسته دفاع هوایی ۲.۶۸ میلیارد دلاری برای اوکراین را تأیید کرد
وزارت خارجه آمریکا
فروش تجهیزات و پشتیبانی دفاع هوایی به ارزش
۲.۶۸ میلیارد دلار
به اوکراین را تأیید کرده است.
این بسته شامل
سیستم‌های دفاع هوایی برد بلند، پرتابگرهای متحرک، رادارهای ضد پهپاد، قطعات یدکی، نرم‌افزار و پشتیبانی فنی
است.
اوکراین هزینه خرید را از طریق
کمک‌های مالی اروپا
و
کمک‌های نظامی خارجی آمریکا (FMF) که قبلاً تخصیص یافته بود، تأمین خواهد کرد.</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/20994" target="_blank">📅 08:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20993">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حمله موشکی حوثی ها به ریاض پایتخت عربستان</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/20993" target="_blank">📅 06:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20992">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">منابع خبر می‌دهند آمریکا و دانمارک به توافقی درباره گرینلند نزدیک می‌شوند.</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/20992" target="_blank">📅 01:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20991">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">منابع خبر می‌دهند آمریکا و دانمارک به توافقی درباره گرینلند نزدیک می‌شوند.</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/20991" target="_blank">📅 00:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20990">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQHx6k_BG80BLO6NF-HDRVRQEbJVE3W5Cdt14Zv4hPXGHjnFYjnWpWEOUrN2T-AKJf54_i3QHyNu6FQ11a94ryVMq8cVJGi2g7wwa9zSTSbn7NsdGxJ8UWI6x2LK363YGNfcOzchEHyJtrATIQaFG87CfzGCL4QlqhJ-qvtPfrFxkz5DN-pDLXAhuJMrCt398C0hapfwRQATFlnVWqE_8QNUCpL8f4VQKD809Gpip-k_z-K1lLsvxjT6zCsFrfdKyL8hYxi07CL5hX5e_54mdSMrdcMTYrU6v402F6WBiM5CYKnvyGLK09EBLIPLSruWRzMw7ntdCa5WdJVNsME8-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلامتی همه پورن استارهای وطن پرست!</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SBoxxx/20990" target="_blank">📅 00:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20989">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOt7aS2pPnsNFtL0Wc2nHxj7OfFM4ZN1kLqL8hPwhkh5bqgOUAZq7zUu9H365fbDjR52oWTuZQa8Crhcuv8h8R9j43rCGDGylwTUGwmM0w3zaf2rBI1nEEZKVsjtHrhe55dIWNjpURG9CLbyaKWk5mKh_chsbllW9apLp1k_Nkvg2cOy0QbRAiFqPLtI-_PBVKs0XxwgY7yhIhFJB7dVhBRIImHDGW2MmWMuaPHqH80RdQv2nSNcgLERrf5NvTQ1jDiTWFOJk3GRE7DoljbO2pgUL1U23s0G1l_P_pXKpkVw3tmVhiZYPg1efucfbGxDlGfDQTErMzNLnKzDZg3xSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حوثی ها قشنگ دارند خاطرات کتاب های دینی راهنمایی و دبیرستان را برایمان زنده می کنند!  فکر کنید اگر این دوستان ما نبودند چطور یاد طائف، مکه، مدینه میفتادیم؟!  همه شان را زدند.  یا ذی الجلال و الاکرام</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/20989" target="_blank">📅 00:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20988">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAa34dfDslaJmXvANmjhMi9xKukkVulabbcnN3tNBUCh1pKq4GiL86DZBGqmwKVECyZp0Wev6CP-9LY_uvGYaut8J9BLiMsPzZhFXSpcBUESy4oo4jILrZyratOK4CuABYWbERxddPeKvF-i-nbBjt889jHWxwxXYcn5fKgu4mL-16HUsxAE0oN4nNzAn7dIRZ4XE3NsnMjFnJFkqnTR35vSz4NxHvX1eIPpCnhGZx9Wrtk8UWFzT7pCfboHBJjtuzXzOadPgHimsTtM4xhdhpIj5obpEJHZ60K0gABuceuS8RvqY0MURMuw_KbpIYo6IzPc7IH__W1vHBGiSXIMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته‌ی شش مقام آمریکایی که با اطلاعات داخلی وزارت دفاع در مورد آمار تلفات آشنایی دارند، تعداد سربازان آمریکایی که در خاورمیانه و در جریان جنگ جاری با ایران جان خود را از دست داده‌اند، بیشتر از آن است که پنتاگون به طور علنی اعلام کرده است.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20988" target="_blank">📅 00:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20987">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">حوثی ها قشنگ دارند خاطرات کتاب های دینی راهنمایی و دبیرستان را برایمان زنده می کنند!
فکر کنید اگر این دوستان ما نبودند چطور یاد طائف، مکه، مدینه میفتادیم؟!
همه شان را زدند.
یا ذی الجلال و الاکرام</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20987" target="_blank">📅 00:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20986">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انفجار در طائف عربستان!</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20986" target="_blank">📅 00:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20985">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/20985" target="_blank">📅 23:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20984">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">#FairValueCurve  نمایه FVC نشانگر نزدیک شدن طلا به محدوده قیمت منصفانه است و لذا از حالت حباب منفی ارزشگذاری فاصله گرفته است (به دلیل رشد سنگین از پریشب) هر چند هنوز تا تشکیل حباب مثبت و بیش خرید بودن فاصله زیادی دارد.  پس بهترین استراتژی برای امروز:  خرید…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/20984" target="_blank">📅 20:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20983">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">العربیه:
وزیر کشور پاکستان طی ساعات آینده به تهران سفر خواهد کرد.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/20983" target="_blank">📅 18:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20982">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران
انقلاب اسلامی ۴ موشک کروز ضدکشتی به سمت تنگه هرمز شلیک کرد</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/20982" target="_blank">📅 18:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20981">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIefQukemtfOgLBBQXBiUBXso8ndAfR7gEI-3_7ilwjbL0Pl0FII46pSQWmJXXQLRnVzGBNG_2qwq_nwU0y7Vkt3cryI1qBqUGYBV8y3zv72JoZ557jxsa0-zcULc_kuv2fodMNwgJ4vEg3XpnJHMPMDwsWjcNLtBytlyyY-7cfU397runoaOcdCVvQj4gquT4tEA3K7AGRTfQbUQGcsvnoSAXpbIHDwnCVYvfRR_mvYU2JcDx1M134bgVoht2GGcD9AI00WGfVNmII9h14o5dLRJWKfRvODCWV7KSkq_BhZsjWzWOUDZ_vuk90DXUsyiGVp5Xg2P50NUMPr69W2xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توصیه دکتر پزشکیان به جانفدایان:  کمتر مصرف کنید!  (پسر پزشکیان هم دیروز همین را گفته بود)</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SBoxxx/20981" target="_blank">📅 15:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20980">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573e6b119d.mp4?token=GSva-s04EOIjbZ532hvqKmX7WMTG9y4qzoU5wJp8X8oaImyvLf993HhVrKyHfuNilYjAFpqnGKEhiMGNyO3UWeDpBAjk-hLgE6x3LbfuIONbA5cfxbJNwOvi6AuE3t35HGPXuZ-nXZvODBlSy4B3310TfEto8eRHE2CU881YSws9OXK1uVl0qimgKUadyzMCOWot6FadEqcYYlkDhbLCQA3P5feA8n98Yhd72THFV9ZZILoJ3XWpPH_p8uPT664S36zhMAmomQ4f4lXyxZZLrMGQ6EkMJnpG-jhJL8D5BLvPaPhkiVoh6_9N8JPd4h0PqVbZyfubHCozkxtkPeV9Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573e6b119d.mp4?token=GSva-s04EOIjbZ532hvqKmX7WMTG9y4qzoU5wJp8X8oaImyvLf993HhVrKyHfuNilYjAFpqnGKEhiMGNyO3UWeDpBAjk-hLgE6x3LbfuIONbA5cfxbJNwOvi6AuE3t35HGPXuZ-nXZvODBlSy4B3310TfEto8eRHE2CU881YSws9OXK1uVl0qimgKUadyzMCOWot6FadEqcYYlkDhbLCQA3P5feA8n98Yhd72THFV9ZZILoJ3XWpPH_p8uPT664S36zhMAmomQ4f4lXyxZZLrMGQ6EkMJnpG-jhJL8D5BLvPaPhkiVoh6_9N8JPd4h0PqVbZyfubHCozkxtkPeV9Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از اروپایی بودن همین را فهمیده که یک لامپ را خاموش کند!  در حاکمیت قانون و مدیریت عقلانی و کرامت انسان هم اروپایی بشویم یا نه؟!</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/20980" target="_blank">📅 15:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20979">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ضرغامی در سالگرد ⁧مهسا امینی:  امروز همه تصمیم‌گیران و تصمیم‌سازان، بر اشتباه بودن ‏روش  گشت ارشاد  اتفاق نظر دارند‏   ظاهرا همیشه باید مصیبت‌ها و مقاومت‌ها ما را به راه و روش درست هدایت کند</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20979" target="_blank">📅 14:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20977">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ضرغامی در سالگرد ⁧مهسا امینی:
امروز همه تصمیم‌گیران و تصمیم‌سازان، بر اشتباه بودن ‏روش  گشت ارشاد  اتفاق نظر دارند‏
ظاهرا همیشه باید مصیبت‌ها و مقاومت‌ها ما را به راه و روش درست هدایت کند</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/20977" target="_blank">📅 14:13 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

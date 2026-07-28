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
<img src="https://cdn4.telesco.pe/file/ejt3VVXoSgDvPPpmW07oFM56JQwG74UWeY0JkPlKdgbx5pTL9g6N10btAv3H72hW8xpmxdgyykBPbIm1lYM_IGMxYqMQOvgxAYYRU0sFHJamso4J0WscUb_gMvkNR2LOBD_us-4HwySs-q-n12k9NsHL2gwRcj8kR57-apfI30wPH0S9DP6yRq06f23mjDdSj7_wLkU2fOn24kA_9bO1quwCPqJQ5PhHpQhn2RvRbpZAJ96VtUKPgauYjs6wCd9Ju3KLOQHulov7wFkgee3XnJ2NEVuUx8gKb8JWgPONwDLhxRm3_GoUolpSLXpqbEiJdam-T47U4viScELfmWqU-Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 18:42:27</div>
<hr>

<div class="tg-post" id="msg-453146">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/969b353542.mp4?token=YCtee1_TDwezSORp_JWz0bo5LIvrkzxLkpAFL5J_RXXMbKP21Fcs0hX55ynoKNgMkBgjQwpOSCO_t7oRYU5YLaVBEyexib8IJhb3PVEGTX4gpl_UguSxpN0CTweIlW721rBIPn7tbL6abHT6wypWqrsTf-yTnNvdygIfGP7NJF9ZyYHNbw3JClOGUZJ3elnkDN964_gPzxALmb4DzC0VQJhSywurwHQxx7n8ofGLJzBRVQxQFtGrizBtGwG0NOehqPUBPiEmCEWNiZ7OVepFQHIpkCDP3t2L0wae72QIn2ltcmYds4gnuGGrDytHhW1OjQT1Zz-foLnCS6xlajjKag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/969b353542.mp4?token=YCtee1_TDwezSORp_JWz0bo5LIvrkzxLkpAFL5J_RXXMbKP21Fcs0hX55ynoKNgMkBgjQwpOSCO_t7oRYU5YLaVBEyexib8IJhb3PVEGTX4gpl_UguSxpN0CTweIlW721rBIPn7tbL6abHT6wypWqrsTf-yTnNvdygIfGP7NJF9ZyYHNbw3JClOGUZJ3elnkDN964_gPzxALmb4DzC0VQJhSywurwHQxx7n8ofGLJzBRVQxQFtGrizBtGwG0NOehqPUBPiEmCEWNiZ7OVepFQHIpkCDP3t2L0wae72QIn2ltcmYds4gnuGGrDytHhW1OjQT1Zz-foLnCS6xlajjKag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود زائران ایران از مرز خسروی به منذریه عراق
@Farsna</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/farsna/453146" target="_blank">📅 18:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453145">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5691cab0dc.mp4?token=tygRtYJFwUfU0Lcu3erZMzyh_8iP1Lw8x0_KdItweOFhLHMeYP4AXmE4IStkOIFjnb5Tz1dmHb5Zgf70FgO46FDI0i5cNCmpnP0BE2DjFRlQV5_IJgb-96eIydNxge0G6UIUCIRsCaEuh787Diw5Ji9ldrre6M3lWibRL8MELvIRQa1CC4NPdZaKfyWv9HWZ6GTJScdC_hMFv8m37SI06QYbfRvYkF9zTesuQNzTMlj4RXTg-gsXLLoPta2jn6gEZv3zPTTK9I-SnsmUfbnDb5sOa8HV9DpzxWyR5oVVuqlZQEQKkSqGrG6sH5guYP1o5hpETzxe1zGGywsqqcKifA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5691cab0dc.mp4?token=tygRtYJFwUfU0Lcu3erZMzyh_8iP1Lw8x0_KdItweOFhLHMeYP4AXmE4IStkOIFjnb5Tz1dmHb5Zgf70FgO46FDI0i5cNCmpnP0BE2DjFRlQV5_IJgb-96eIydNxge0G6UIUCIRsCaEuh787Diw5Ji9ldrre6M3lWibRL8MELvIRQa1CC4NPdZaKfyWv9HWZ6GTJScdC_hMFv8m37SI06QYbfRvYkF9zTesuQNzTMlj4RXTg-gsXLLoPta2jn6gEZv3zPTTK9I-SnsmUfbnDb5sOa8HV9DpzxWyR5oVVuqlZQEQKkSqGrG6sH5guYP1o5hpETzxe1zGGywsqqcKifA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماینرهای غیرمجاز یکی از عوامل اصلی خاموشی‌ها هستند؛ گزارش‌های مردمی می‌تواند جان بیماران را نجات دهد
🔹
مصرف برق هر دستگاه استخراج غیرمجاز رمز‌ارز معادل مصرف حدود ۱۰ واحد مسکونی است و ادامه فعالیت این دستگاه‌ها، فشار سنگینی بر شبکه برق کشور وارد می‌کند. این موضوع می‌تواند به افزایش خاموشی‌ها منجر شود؛ خاموشی‌هایی که علاوه بر ایجاد مشکلات برای شهروندان، در مراکز درمانی و بیمارستان‌ها نیز تبعات جدی به همراه دارد.
🔹
شرکت توانیر از شهروندان خواست در صورت مشاهده نشانه‌هایی مانند صدای مداوم فن‌های قوی یا مصرف مشکوک برق در همسایگی، کارگاه‌ها یا سایر مناطق، موارد را از طریق پیامک به سامانه ۳۰۰۰۵۱۲۱ گزارش کنند. این شرکت تأکید کرده است که هویت گزارش‌دهندگان به‌طور کامل محرمانه باقی خواهد ماند و مشارکت مردم نقش مهمی در مقابله با استخراج غیرمجاز رمز‌ارز و حفظ پایداری شبکه برق کشور دارد.
@Farsna</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/farsna/453145" target="_blank">📅 18:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453144">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BowcOedkSXEDJMcstp5m814lIiFTfCeE_gYAkiSSyV7eWlA2fjTOqvCyKJlDAlBqnWA5tWD4NuSkpXn5uGR6o_wHdpESrLmTCMRpTEBKAF6hHLnbpVaEBBvI_kWn3guxr0blwG3zFqdk32AynN5jAeQXXJ3LTkAy5TuBs8NtfyNXMTqrLOZKoEF3P7IlC-7fVyDDM8geE-d1ORwbQB3OFGnP8OKR51SjO-30fMhesnD1InCcMbcD9LztmGbry6sE-6zuNbVDTbeMzQjz4d8Ndk1k0XDN5QEt8DQt00VIaQukhhZyrIE2lUxe0V81SmSFr7IOtIIklEHn2xoyeQDhYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه حال خوب بساز...
💦
مرداد، قراره هر بار که به پارک آبی اُپارک میای، یه تجربه متفاوت منتظرت باشه
😍
از بازی‌های گروهی و لحظه‌های پرهیجان کنار دوستات گرفته تا هدیه بلیت آنلاین و برنامه‌های ویژه‌ای که فقط در مرداد تجربه‌شون می‌کنی؛
اگر دنبال هیجان، تفریح و ساختن خاطره‌های خوب هستی، این ماه بهترین فرصت برای اومدن به اُپارکه
🎉
🎟
برای تهیه بلیت، همین حالا وارد سایت شو
👇</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/farsna/453144" target="_blank">📅 18:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453143">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/farsna/453143" target="_blank">📅 18:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453142">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPYUb2E-CmCX2vzl6C6YCybdOQsT0syIar_pWWHk9Yygp8jTSATK56alhdgz90YeBBe2B785TXovEZRbNEvsQDF6IL3BlPYHTJtFPZCJI6fgzaHMSLa0XmPuEI_D482TE6VHG6UHjykarIiTL5149cipjeafE5K_HrwAlgZ-wncsoqamrjr5d202fLH-l3JVZlUM4YzwuHglG985r3SsOiWdJ4YGSjRV-TNK8QOfnOGYPkCQbrO9I_IxDzQ6nl2FQ0tIQZuzRgxeW2BBzkfp242wcr2BkFqsP-RvD8Dw_FjTIfW3QWn7CYHX9nR0q0N-yDhHZgblMCjg0XbSMO7VGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام آمادگی یمن برای گسترش جنگ با عربستان سعودی
🔹
عضو دفتر سیاسی جنبش انصارالله: یمن در حال حاضر عملیات شکستن محاصره را آغاز کرده،‌ ولی آماده است این جنگ را به بالاترین سطح برساند.
🔹
اگر محاصرهٔ یمن برداشته نشود، نه مذاکره را خواهیم پذیرفت، و نه چنین مذاکره‌ای ارزش دارد.
🔹
عربستان باید به حاکمیت و استقلال یمن احترام بگذارد و پیامدهای هرگونه نقض توافق را بپذیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/farsna/453142" target="_blank">📅 18:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453135">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R-3OJDEWcVDmwww73gW6eeAVkcCeWp3CwHpt9mEU82KKUQTggTk67NZlxoMYpQ2o2Q5pI4zJuqvEIZPqrXwfCfjV4dP39uo4w1AtSExkq3shifZkziS899GfN9NdzHnMcluQFGdrE1B7zIXJ04mNSsrZEweGYeICpy182BsML3dAXat_HYHd2bj5nYpbWceSzD9_8K1SJybDhW43R3ag_DrLhDtxxit4QlA6iPZNyFyllnZj5sWLA3oKGCw7SNyxi7jMmumz02GZ2sbWAGsQMeZCzHtIKG-2TmibC2dF3JYmn8pBK8i51KATI0-4ZXAeCunaUTGfaUI8uvSa6bS5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBtbWqV3grw6mGDombmvv4OD3meYXPKziRFTzwzIbJUsD93DbPUAsEuYkhL7iEB2zrDWwVo86Bp-Dzaop_jGwHsuJz5s2kjz0wk9QbsS1h6wNStOA3R1FY2NpOC8eA28IpqoiltVFVyo-q4w_LWT_1aoUckB_nA3xc8Uk7GrHRzb5rnCGQZX83gelzlg5P7NPdCAJxINgWYTrFtNcaJfzp3OsPKfcb3FeF-7pv-oXhbptAq4gFTDv5F-__vzS6wQwZbcoMIpisLskntyBvW33ByVXFMx2ByRKKn4Y_xC4GqN6-DRC_0p65ojq-HwHxoJnvNsXBfAHlJ7dMm2iXUwcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QoWGXjRMDOEkoDeFpDT2XfQRdzpZ-H0mNjnHkjhZsk11McRDeU3PQ9-eWAuO812kA5sf9OjimVBfNHYp6m4i5uBCvSbD6LIJR13ocQPZe-23HEHz8uQ_CUKgoBjYCWlrpTK6oTpF91LSyX6MaKChqdXXnOonrD7Viwkrit8YhR8GlOEMSx51wim_PZ-0mH7RcYRe0pKBS4qcwdfB0mQ4hCCyFpDNG3jjE5sNvQCKZrhEP87R2n9pR7ErDidWfrTsLiQV8k5tc7t8cYXVXQVsBKkBv_kw5T6InEPepNzBya_2KhgwK8cWwwmoZgpTrD_TNS-b9c41G2CKpfz22OuoWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gRzBpQl_eFNN9HIhXLKBpCtlsT4Va5yFBm1sE9BnUC07Qv4j8F8aSteqOjP0SqdpuPKW34elLbOSzLpfBnqQCDYN_ksd5GAjzY7PyqnX79C7ayocghebKCt4erJQ64_QT11vLnlSd4BTH60sFPezJlXQCfQ8gQYsc3Ehh2VJ8WEb2IwgoAdiCwdWAExo6aY8GEjqhRDFybWo-UYMsawmVaNIjFTnyCMR-zmeGAV0S87ewOSo9F7lwVdKjEkpGqeaZsCrjW52K2aB3ELPDPjT1-pvjDi0ZPFaWDlT3OZmEtvMqStuWcB34H0sLC1qYwjuT6L0kQ1ytXtkOBIozVqSew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eTlpD_sNzlUyCTjWD8ALkoGStx-VtXyISSL0R0eQYhpeKZpPsoCln5j-SqE00fce8Y9gkFmaHflULeqiSBCWh9dum1KwInZshSWBZAXdAHq8rEquYJ9FO4W1JTMqaR4FcAR-zv6fxIbVFmcNPcfNV6039_gOHeRdlMyTwVneFwCrc28kaNVNX34xFvIU2uyc61bMmDK8puPu-kGZ_ho4T3BZJekVY69yljWaxztrKZePOu1iKQHr0dRQKT1LWUNkudeWIrzrxOFbqwB4XOj-H07ytceXE0UbEBdTR_lXNiks0PhTPvfIUESRB8wE4arBIBA0noKPAjdPAUTfSNwlYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jjXe3wGprEcN7bljYjEX0ZtiF7xKr6_h8p-QJkVWHmSmAgl99hes2Dgixu10ebfTdw0vrrgBOVlNHZ2n13kKYsg2IAH26mql7EkA-mlcbYr-X6qm4ecNYsHYW4FM51309NVpj2ehgXhOn5qlzMmYvKwhpOFAFE8FKHJkJchj9rPA7e0mvZRl8qhhrKGQTO7DT2EBlkcnPjR77w257tHtqJ8bIAM8xJXXziaIhs1ZAq7wlXzYvuBdy-Tk7ui0fswuiVVCNReeHybb5kuvpUDxQQ6J-fI8cMvQMKoPWsun9G4rjYnU-VGJwhzb2oQTbB81SapJPJoYSMOL35I4Qg5MTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G8ftYq5MJjYSrL8AMK8gFg2PTTzIzWKRZkyhOASXpNU3_O_3PkNvr32lh5gMUdAZiWRRI9ONZgHXEeBMI1v-_Whb11DK-XLlvaH5iXf9jlltKlERttvALkWCEnQLRg3xVhtWSuiTfV7yDysvtp0iYN43WQk4Fw0xSYnGXtWUnnSm4tjXQPRnj7N-eKdCivDoa_QhvrfCgZ9BMw29gyq9kAvff46Kah4zncs8W1InnOZQwHo4OjyXgG5VbBiFK0bDZfc7kqTX3GUXcMFuQddIdJvcPTo0MDesGfpkm71QD3ejoitrE5mVxewyr91X_v9X-FE32QaQ7Bw4qiFCJB490w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قرعه‌کشی رقابت‌های فصل ۲۶ لیگ برتر فوتبال
عکس:
صادق نیک گستر
@Farsna</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/farsna/453135" target="_blank">📅 18:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453134">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdcifSfYQzkorYQ_pYHOmHHNIW5YZI7rXakC9WKD4WfmI6L6jDu23wOpyQalXegYjBzuuuU2KK6ESoIKUeyNKXs1PduZXNnywZASQRpWjD7uog5jWp14vfgRaBajspPymDFusP4ZC1Kub_knpt6Jl1dLYKwwnZwD6DmuDnR2-FBaT50qj9j5QECHoGVwMy4QB86vqHNkANqoQRv1qCOmbrjWus6KZUAgE0UcbmfGnRti7TQ_tSlyakAL8kNI0kRtHBZK1wmdan8g5TryW1P8eio_SmGcBqy4gFngjuPmMkH8jnbhfpOMC-ZnQTCNywtCrfrr7sEIoMXWvMdmonEqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع:
خطوط تولید صنایع دفاعی فعال‌تر از گذشته است
🔹
سردار ابن‌الرضا: کسانی که گمان می‌کردند با هدف قرار دادن مراکز راهبردی دفاعی، صنعت دفاعی جمهوری اسلامی ایران از حرکت بازخواهد ایستاد، امروز با واقعیتی کاملاً متفاوت روبه‌رو هستند.
🔹
توسعه توان دفاع هواپایه و دفاع دریاپایه از اولویت‌های راهبردی وزارت دفاع است؛ باید بالاتر از لبه فناوری بجنگیم و همواره یک گام جلوتر از دشمن حرکت کنیم.
🔹
خطوط تولید فعال‌تر از گذشته، فناوری‌ها پیشرفته‌تر و اراده متخصصان و دانشمندان ایرانی برای ساخت آینده دفاعی کشور مستحکم‌تر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/farsna/453134" target="_blank">📅 18:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453132">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4e97c860.mp4?token=mFOFyjmtKeXCUYmv_rhFQ8xNl_ZJt7rAazUhItprxeBQc_ViifGxaYEscb9Zw215oF2VgX1XJsnN1YT62pqvJXytKUqi1_2-hXscvDDbeDA3gkxoqymmDca2T4MUt4RShJSUJzHXHWODLimA_h9X0aUOwBywtKjH6_YJs89_imjkjW8YBjaS5sZ2Zq9sz-HSvkWzE6xHj0JOVEqSPvTks2JZJXM3xjY-0zfUDecnX-WpIJL6thZxhC9lUijDykN9SKxvPnglnvnXMedAcseZ7J8WqT1qfNMPX-oB0TXLJaGn3fgEjBmw0vloeSWr9PkEce3odQmhtqlJIdZ82GEXWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4e97c860.mp4?token=mFOFyjmtKeXCUYmv_rhFQ8xNl_ZJt7rAazUhItprxeBQc_ViifGxaYEscb9Zw215oF2VgX1XJsnN1YT62pqvJXytKUqi1_2-hXscvDDbeDA3gkxoqymmDca2T4MUt4RShJSUJzHXHWODLimA_h9X0aUOwBywtKjH6_YJs89_imjkjW8YBjaS5sZ2Zq9sz-HSvkWzE6xHj0JOVEqSPvTks2JZJXM3xjY-0zfUDecnX-WpIJL6thZxhC9lUijDykN9SKxvPnglnvnXMedAcseZ7J8WqT1qfNMPX-oB0TXLJaGn3fgEjBmw0vloeSWr9PkEce3odQmhtqlJIdZ82GEXWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی از تصاویر زنده پیاده‌روی در مسیر نجف به کربلا
@Farsna</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/453132" target="_blank">📅 17:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453131">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f7b48f9a4.mp4?token=gYQP7ZhS6JNLzihq4VVnT6QjczzEStO_PmVp7bqHw2SBotRF5Bhks0ehwx87ygHklFMIFB8c5oqOLi1Q5tE-pgKu5vO2GWu5KzARKa-BIte5qVY7U3lg7vqhoo5QyvGJxE5nqnBy-XAHHpFM6SR_z2oxObS81ODsgx2aYB_IpfdWBqsGkJsGOn_qkcKgX-GIZsbTu_8YoghS3D6mhVc2akpKdy8rWp8OfXles29hTau3Ba4lLa8o2NmrN_EwzL9GAXyo-2GKBYsb1yDNcpijzMNWYXEpWQDyW2NZY1cFq2plGxTkoQRueD-M3M5Ees_8X8mmUHp8qXAncXoR0Spltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f7b48f9a4.mp4?token=gYQP7ZhS6JNLzihq4VVnT6QjczzEStO_PmVp7bqHw2SBotRF5Bhks0ehwx87ygHklFMIFB8c5oqOLi1Q5tE-pgKu5vO2GWu5KzARKa-BIte5qVY7U3lg7vqhoo5QyvGJxE5nqnBy-XAHHpFM6SR_z2oxObS81ODsgx2aYB_IpfdWBqsGkJsGOn_qkcKgX-GIZsbTu_8YoghS3D6mhVc2akpKdy8rWp8OfXles29hTau3Ba4lLa8o2NmrN_EwzL9GAXyo-2GKBYsb1yDNcpijzMNWYXEpWQDyW2NZY1cFq2plGxTkoQRueD-M3M5Ees_8X8mmUHp8qXAncXoR0Spltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دانش‌بنیان‌ها چه سهمی از حمایت‌های ستاد اجرایی فرمان امام دارند؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/453131" target="_blank">📅 17:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453130">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">برنامه دوئل‌های ۴ تیم مدعی لیگ برتر
🔹
هفته ۲: سپاهان - تراکتور
🔹
هفته ۳: استقلال - سپاهان
🔹
هفته ۳: تراکتور - پرسپولیس
🔹
هفته ۵: استقلال - پرسپولیس
🔹
هفته ۸: تراکتور - استقلال
🔹
هفته ۱۵: پرسپولیس - سپاهان
@Sportfars</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/453130" target="_blank">📅 17:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453129">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29de00b4ed.mp4?token=i2PUsP_Ln71SULSshXSA9aK9TL84adQKae6UHk6Iat7iI-eey7TjMd1-8djqkOlrgL6SGD2S6bHGPzAtho_YyTh6TXOJE5Xrz_oorPrnDwyE3P_RQcdM3gqTwa6DA1sHVQi07nL-BcPPlR4LozW8BnNxcR9gMqmdqHnMHg7WO_S7-8_6bU7IIIv83N6ONr5qS9fAoVRbgxdH2_ioqLeZKeq_CDZzOQ7bX2MztxymIjTjlKESmZQ0P9f83BWW9MgGJxYxPxV2Z-U-8zd_hlzrwcXrn4juo2FmteyE-JHXq0adArJ4G5I4tgaVTWYiwqm273I0NvcPMX2xMWbPFkIiHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29de00b4ed.mp4?token=i2PUsP_Ln71SULSshXSA9aK9TL84adQKae6UHk6Iat7iI-eey7TjMd1-8djqkOlrgL6SGD2S6bHGPzAtho_YyTh6TXOJE5Xrz_oorPrnDwyE3P_RQcdM3gqTwa6DA1sHVQi07nL-BcPPlR4LozW8BnNxcR9gMqmdqHnMHg7WO_S7-8_6bU7IIIv83N6ONr5qS9fAoVRbgxdH2_ioqLeZKeq_CDZzOQ7bX2MztxymIjTjlKESmZQ0P9f83BWW9MgGJxYxPxV2Z-U-8zd_hlzrwcXrn4juo2FmteyE-JHXq0adArJ4G5I4tgaVTWYiwqm273I0NvcPMX2xMWbPFkIiHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمانده هوافضای سپاه: سوخت پیشران قدرت موشکی، فریاد بلند آحاد ملت غیور و ولایت‌مدار ایران است
🔹
جمعی از کودکان کرج در روزهای گذشته با ارسال نامه‌ها و نقاشی‌هایی برای سردار سیدمجید موسوی از رزمندگان و مدافعان امنیت کشور قدردانی کردند.
سردار موسوی نیز در پاسخ به این ابراز احساسات، پیامی خطاب به این کودکان نوشت:
🔹
قدرت موشکی جمهوری اسلامی ایران، ودیعه قائد شهیدمان و میراث سرداران شهید؛ حسن طهرانی‌مقدم، امیرعلی حاجی‌زاده، محمود باقری و شهدای خونین‌کفن هوافضاست که سوخت پیشران آن فریاد بلند آحاد ملت غیور، بصیر و ولایت‌مدار ایران اسلامی است که به لطف الهی هیچ‌گاه خاموش نمی‌شود.
خداوند نصرت و پیروزی را به ملت ما عنایت فرماید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/453129" target="_blank">📅 17:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453128">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یارانه ۳۰۰ معاند خارج‌نشین قطع شد
🔹
دادستان کل کشور: تاکنون ۳۰۰ تن از معاندین خارج‌نشین که در داخل کشور یارانه دریافت می‌کردند، شناسایی و در کنار شناسایی اموال این افراد، یارانه نقدی این اشخاص قطع شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/453128" target="_blank">📅 17:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453127">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmfwJWw54Bc9hnnHDBgw13stOukoT7WKUIW9sdzYyA8VdseUin1dfqCYrinSMjjLKQvdaWrjKEnwnCUPXTcbt8Dml5W7RhGzJaWRymFErbVjMgywtFb3y3XcwiWhfQY3lw2_w9oS04hqG1ekp9tL_3LCoyhA8Pi_Wfu41ObGb0cNJ-wSWFS4j8YotRBwYEIGP-NhOCaPNqM8Y4lEGr50Kebi91osi9E9Yqek4WvJ8hWmKcSnP7av13Hjq4OlS_jTk70C2SFPUv9JLJ6OUjgLTDRs5UWdVAPgKMKPGvELFv5iwWgxd4SzZ1oE2yp_yDWGS0FbQGrfuwr99mLtGLOERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محبی سرخ‌پوش شد
⚽️
محمدمهدی محبی وینگر ۲۷ سالۀ تیم ملی با قراردادی ۳ ساله به پرسپولیس پیوست.
@Farsna</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/453127" target="_blank">📅 17:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453126">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دادستان تهران: کیفرخواست‌های مربوط به جنگ ۱۲ روزه به‌طور کامل تکمیل و صادر شده است
🔹
تاکنون ۱۴۰ پرونده مربوط به جنگ ۴۰ روزه منتهی به صدور کیفرخواست قانونی شده است؛ از میان این ۱۴۰ پرونده، ۲۳ پرونده مربوط به جنایات رژیم صهیونیستی و در رأس آن شخص نتانیاهو است.
🔹
همچنین ۷۴ پرونده نیز مربوط به اقدامات دولت آمریکا و در رأس آن رئیس‌جمهور این کشور می‌باشد.
🔹
عناوین اتهامی مندرج در این کیفرخواست‌ها شامل افساد فی‌الارض، قتل، تخریب، ایراد ضرب و جرح عمدی و اقدامات تروریستی است.
🔹
پرونده شهادت رهبر شهید انقلاب و خانواده معظم ایشان و همچنین پرونده‌های خاص دیگر مانند جنایات رخ‌داده در لامرد و میناب، حداکثر تا ۲ هفته آینده به دادگاه ارسال خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/453126" target="_blank">📅 17:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453125">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9Y5ZKZKW425vKHHKmRkQYAMgVx8Olz_gzUf8MavP3yfJ98nhMjJkIKKWw9kAz_G0ADaQoGOMpy_mjEtwjiyW_Rra8TIX-BATlhUvAy-e87SlCwsPvTDhB9bxyU7VI7vMXn8SoDMej2YB75Grf_M98NFq7QymecATS_hN16Pse24C5hCEl-hy8ApCb68Ni-s4QNsIv5IOdsdND9xz85zhDVkINr4pzw0NLimOxAXIZsP-B4EvNWZHVGD3kwlRVQKHaeYCUZl5-dJHoZMcYZVC_nelU1Q9IMFgmA2vx0tCwRi-Mv2n8l4PPa_AMVcdIj3b524Mzwe0siPpxea9rMnng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره سراغ تهدید تکراری‌اش رفت
🔹
ترامپ بار دیگر ادعاهای خود علیه ایران را تکرار کرد و مدعی شد: «اگر ایران با ما به توافق نرسد، ظرف دو ساعت بیشتر پل‌های آن نابود می‌شود.»
🔹
این نخستین‌بار نیست که ترامپ چنین ادعاهایی را مطرح می‌کند. او پیش‌تر نیز بارها گفته بود اگر ایران توافق نکند، پل‌ها و زیرساخت‌های کشور را هدف قرار خواهد داد؛ اما پس از مدتی مدعی شد حملات را به درخواست برخی میانجی‌ها به تعویق انداخته است.
🔹
ترامپ چندی پیش نیز تهدید کرده بود در صورت هدف قرار گرفتن کشتی‌های متخلف از سوی ایران، زیرساخت‌ها و پل‌های ایران را هدف قرار می‌دهد؛ اما اندکی بعد گفت اگر چنین اتفاقی رخ دهد، از محل دارایی‌های بلوکه‌شده ایران به مالکان کشتی‌ها غرامت پرداخت خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/453125" target="_blank">📅 17:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453124">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ترامپ: درباره کوه کلنگ نیازی به نظر نتانیاهو ندارم
🔹
رئیس‌جمهور آمریکا دونالد ترامپ در مصاحبه با فاکس‌نیوز تهدیدات خود درباره حمله به کوه کلنگ را تکرار کرد.
🔹
وی با اشاره به ادعاهای: من نیازی ندارم که نتانیاهو این را به من بگوید. نتانیاهو این را به من می‌گوید، چون می‌خواهد که من همچنان درگیر جنگ باقی بمانم.
🔸
شنیدم که نتانیاهو این موضوع را اعلام کرد. گفتم: «چرا فقط به من نگفتی؟ چرا باید آن را به کل دنیا اعلام کنی؟»
🔸
من دقیقاً می‌دانم که در کوه کلنگ چه می‌گذرد. این مشکل بزرگی نیست. اگر به توافق نرسیم، آن را از بین می‌بریم.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/453124" target="_blank">📅 17:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453123">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ey3m7ChFlIKeEyibK0x6FtNZy8VxcmTpSY9aEWTXgoVbzw-vm1f9L5DgXVAcRSWcbyV255b76uM8fbia37x2SISYkANmhirPIA0j2lez4Jh4MO2yhBFKjbWD48YVya6To0xz6EtHr7aLp_IZtLLLTpoEzvFtFQ6mCwIz0MQMJUem_hA-cUQsB9QbLToiL4lu9KAUCDkqRdqz3rRT5JLTsrcfhGAMAd-iNJ-MauT7GlNNWQLM8eZWJXYjRfYTV7IQ6UHCgtss17iqte7UIBRtqla1MuifE-T0TaZjUFHryQa2saCM0ZX8TIeZDc1aU6QcmfywAHT1Rcpi3oeUFEALtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دربی لیگ ۲۶ در هفتۀ پنجم برگزار می‌شود
⚽️
قرعه‌کشی دورۀ جدید لیگ‌برتر که باحضور ۱۸ تیم برگزار خواهد شد از دقایقی قبل آغاز شده.
@Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/453123" target="_blank">📅 16:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453122">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gujTDWiWzofkuDXxjyCEF6fZEn2DbMHayaAVkDJ69XFVKOZq7NsJbp7QBV7xUNBuBfXeSjdGDPo5H2hzgIFvh3AKykQiSHvIwIOo3_805XNZ-8UupGeoyIFNWHZkAbnufl5eZpenWcwA9aPEu7EzSyAz56L5v4phJEP6O1EnLe1Comow8Qnp3Qw0NuXZvTPOYO6vbVSoohscwff6nMFXDtzhfs1ToEC9I1DI5R1JWMgjTPISzk-jyineY-DwlkmGZ14JCFu3lwvf0LjkgzUGIUXVCZbgJWL4LfRr-sLK1uAqBjvmHxmbrQXqE5QHtTVLDhdz96mV4mNCysbTZCkoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر من رئیس‌جمهور آمریکا نمی‌شدم الان اسرائیل وجود نداشت
@Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/453122" target="_blank">📅 16:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453120">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad321b0c7.mp4?token=IVHjd7VaYNAFodDJQtmvOlVV1OqfVpEFC7eWLshChsf4kuSQ9h9T1MTXzuRgYCRMXsu7N5SfemdjO4Rh5-D0KsqJfLMhC0FVCkwWelVQ-RLsHrrUOszosohGpyk9HznpMZOSpde1P4wr2yivnbFCixKqHrEppuBo2490g5riXukfJ7OtvQeR2BjxoH3fEK94jSP9joNAX1moGiiT9o--vv1deyFjaHmlRnbyKqWBRS8oePT3qFxQ_LG2Asb7CFm8GYWmEaE4V1GaTP8RKrUOqxIM22JPZGT46-nyKwhh5ny1EwPCl3nw16lkeSlbKcY2z6IrTabOpubNpavSLofpnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad321b0c7.mp4?token=IVHjd7VaYNAFodDJQtmvOlVV1OqfVpEFC7eWLshChsf4kuSQ9h9T1MTXzuRgYCRMXsu7N5SfemdjO4Rh5-D0KsqJfLMhC0FVCkwWelVQ-RLsHrrUOszosohGpyk9HznpMZOSpde1P4wr2yivnbFCixKqHrEppuBo2490g5riXukfJ7OtvQeR2BjxoH3fEK94jSP9joNAX1moGiiT9o--vv1deyFjaHmlRnbyKqWBRS8oePT3qFxQ_LG2Asb7CFm8GYWmEaE4V1GaTP8RKrUOqxIM22JPZGT46-nyKwhh5ny1EwPCl3nw16lkeSlbKcY2z6IrTabOpubNpavSLofpnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قرارگاه خاتم‌الانبیا: هر کشوری که از دارایی‌های ایران مبلغی دریافت کند اجازهٔ عبور از تنگهٔ هرمز را نخواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/453120" target="_blank">📅 16:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453119">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/030d73d41c.mp4?token=YCDzWaShW2BwyO4-Gi4U2-2Y5090aKMyUxZe7SrC_YvBKYoCzzpJh-Cs9Pfgg6daJGGqdtGF4cjlOaSKkKAfqTDSYbDqROpTskEZHGGNSS89X2Baq3UZxe_gWYbbz5_s1anu5K6pTaKrjKb0e9VIKfoq0_uY7FdHt_PiO6QFsx_TqR25hAfGHwhRwc_7GXoMcVBxtoxmGzG7Nz5nUqpRM2o-m_9LBsPyDYYNYLbmY9KJBtih8slWa2RYAa0l9Yl03L8yQ5-NWP75GspV01KOofug7LPUlLT3U5bthC0YLSBrUVcn--fxn2gq1MmwePZlmUIG11SImnxd1GJCV8OlFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/030d73d41c.mp4?token=YCDzWaShW2BwyO4-Gi4U2-2Y5090aKMyUxZe7SrC_YvBKYoCzzpJh-Cs9Pfgg6daJGGqdtGF4cjlOaSKkKAfqTDSYbDqROpTskEZHGGNSS89X2Baq3UZxe_gWYbbz5_s1anu5K6pTaKrjKb0e9VIKfoq0_uY7FdHt_PiO6QFsx_TqR25hAfGHwhRwc_7GXoMcVBxtoxmGzG7Nz5nUqpRM2o-m_9LBsPyDYYNYLbmY9KJBtih8slWa2RYAa0l9Yl03L8yQ5-NWP75GspV01KOofug7LPUlLT3U5bthC0YLSBrUVcn--fxn2gq1MmwePZlmUIG11SImnxd1GJCV8OlFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«نوید» هم در «محرم شهر» حاضر شد؛ دعوت ویژه عوامل شبکه نهال از خانواده‌های تهرانی برای حضور در میدان آزادی
🔹
همزمان با برگزاری رویداد بزرگ «محرم شهر» در میدان آزادی، عوامل شبکه نهال با دعوت از خانواده‌های تهرانی، از آنان خواستند همراه با کودکان خود در این رویداد فرهنگی و مذهبی حضور پیدا کنند.
🔹
«محرم شهر» هر شب تا اربعین با اجرای برنامه‌های متنوع ویژه کودکان، نوجوانان و خانواده‌ها در میدان آزادی برگزار می‌شود و میزبان شهروندان تهرانی است.
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/453119" target="_blank">📅 16:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453118">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-text">⬅️
با مشارکت شرکت توسعه گردشگری شهرآئین بانک شهر و معاونت فرهنگی جهاد دانشگاهی برگزار شد
🔴
سفر کاروان دانشجویی زیارت عتبات و پیاده‌روی اربعین با مشارکت تی‌تی‌شهر و جهاد دانشگاهی</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/453118" target="_blank">📅 16:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453117">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/453117" target="_blank">📅 16:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453115">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee87d7681f.mp4?token=GWyXLB-ciOkjqnnszF3Tux7hEGZEHkBuAZvpEukNVqIlfEiPLk7UXBF90O05EjXMwzMyXNJVYyEtTWEOtnBRnXkZORVD1ahagQMqlTH3KtG2kb8ElyPORfAAwbp8akYYxar6Irxs_-47E7NQrmH4YcLVr4_8rPHdQXYSDKiedrV2-lDi_8GsoCRGN-cccG7sJ2VinTViST90OSRhwTS1N5ZCPowKE69pCjQJwD91Aqi5r0_vx6Qx1dZ1RRMPRKa0irTP5hpo0QyTK77G0D6caMwQCGw_iDiJ0xXSX87VsDH4xitv5gY9MxpIGgzzFHr7MYu_BfLdeMWn4T0CzgdDrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee87d7681f.mp4?token=GWyXLB-ciOkjqnnszF3Tux7hEGZEHkBuAZvpEukNVqIlfEiPLk7UXBF90O05EjXMwzMyXNJVYyEtTWEOtnBRnXkZORVD1ahagQMqlTH3KtG2kb8ElyPORfAAwbp8akYYxar6Irxs_-47E7NQrmH4YcLVr4_8rPHdQXYSDKiedrV2-lDi_8GsoCRGN-cccG7sJ2VinTViST90OSRhwTS1N5ZCPowKE69pCjQJwD91Aqi5r0_vx6Qx1dZ1RRMPRKa0irTP5hpo0QyTK77G0D6caMwQCGw_iDiJ0xXSX87VsDH4xitv5gY9MxpIGgzzFHr7MYu_BfLdeMWn4T0CzgdDrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش ترامپ به شعار "کودک آزار"
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/453115" target="_blank">📅 16:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453114">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cj7PBjKcfucFkeqmxU00mW5wzwvyK5i3azovbOlx6y2SE9gRPPo8hPqDLq1Kq58dxRw9ctM0Y2Le3IJ5WUOTEPxTzUhw_1PiXb-1jzpZX47axez5izJwDtkekql--oSU9xVFXQQzcSvaxpjbwQu5anc8aTl9DGlYrK_8gj1VHEIBTa5yjmRufuuSKI2qlLXv5MrAo3RrXy7p8vvFkfzBZVbYLKYaeNQ4Pwum0BhSr2pobzhm_ArbTHL-PK8rSCNulxmauqgz3NRnCG1vuqxi9urB5EvdKlfj9tIfgJzyRgAQ-o4trQjFzr-kmeLyEeY5UGk6r_Q0u2Gn6lhDuYVGUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلاش نتانیاهو و زلنسکی برای هماهنگی علیه ایران
🔹
رسانه‌های صهیونیستی گزارش دادند که دفتر نتانیاهو و دفتر زلنسکی در تلاش هستند تا در حاشیهٔ سفرشان به واشنگتن، دیداری دوجانبه در مورد ایران برگزار کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/453114" target="_blank">📅 15:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453113">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نشت فسفر سفید در پایگاه آمریکا در کره‌جنوبی
🔹
رسانه‌های کره‌جنوبی از نشت ماده شیمیایی فسفر سفید در پایگاه هوایی اوسان در جنوب سئول خبر دادند.
🔹
این حادثه‌ به تخلیۀ ساکنان مناطق اطراف این پایگاه منجر شد.
🔹
فسفر سفید ماده‌ای بسیار سمی و آتش‌زا است که در تماس با اکسیژن به‌سرعت شعله‌ور می‌شود، دود غلیظ و گازهای سمی تولید می‌کند و خاموش‌کردن آن بسیار دشوار است. این ماده در عملیات نظامی برای ایجاد پرده دود و روشن‌کردن میدان نبرد استفاده می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/453113" target="_blank">📅 14:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453112">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Znn_25C7iAotfmLLuV4jggeywJmAMnspJhxpV8-ff6VSjGPW2Sb_cDFCZI1SYYcZCh5VbBCuFTMA_YOUqDZU1dQmywfwwqDMv0uDo6d1VjLnweHiWUc1oTpw2PsC2RXrw-q7RUDWng1zpR2A_B1qb5UIem8HbQH5aV3fKKE_24J3zKYRKMZk_qcgsnBprPtNbCYiW2C1bNODIDXC4Dif9eJ8l5KqpaB-GOvDTdRNl9OyHKVGs680gS4P-PwDg53rfWlASma4SwEhz92COPary4fyr492tJwiS9ms_VHOY-sy6CPWywIB8OvK7podXFMak6s56Q2N2HgrRmnlSbqJtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار مقاومت عراق به الجولانی دربارهٔ هرگونه اقدام علیه حزب‌الله
🔹
سازمان رادیو و تلویزیون اسرائیل مدعی شد گروه‌های مقاومت عراق با ارسال پیام‌های تهدیدآمیز به الجولانی، نسبت به هرگونه اقدام نظامی علیه حزب‌الله لبنان هشدار داده و از آمادگی خود برای ورود به سوریه خبر داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/453112" target="_blank">📅 14:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453111">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3czqjhTnEKC5EVRuze-QdDr8sWkzVK-WBOf0wWgkMcydo9h7ARSgs3RmoAeZxTPy92X1tMAafR9KB1DRi2SbBlIJEb3KjOW4sXPUrwnj5KivE2k2eUFfMM-VEbJ5rp9hOjiZy_i6-0a65f2S2_59bgLaiBjhUJ_szlgZbW91ArvjuFqH7VsLdzN42iVpfKJC0Q8xuUSdb1QvGW-T4kTI88bBv-Q8_xc-jaAEP3b_sNc38CHaMpNQIkA5764M_3AOl87RHnUHdcRlVs3uFYbIx1HC1__aNNTCbZhrWOrDlwlFAlAI1fRy6JdDlgRLNCS5tVktxtaTIdzNbLWtqgYkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یک منبع آگاه: در صورت خطای مجدد، زیرساخت نفت و گاز منطقه هدف قرار می‌گیرد
🔹
یک منبع آگاه نظامی به فارس اعلام کرد، در صورت ادامهٔ حملات به زیرساخت‌های انرژی، کلیه تاسیسات نفت و گاز مرتبط اسرائیل، آمریکا و هم‌پیمانانشان از جمله تاسیسات انرژی منطقه‌ای هدف نیروهای…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/453111" target="_blank">📅 14:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453110">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e401075c89.mp4?token=shOXTBGQvsmnFAD6olQ8TFlylk9TIcfhU3TLzthjVs9zqFvaTqbw5fY8YhBuSBU98s3EFJ39quWauLXnexMQzLkhRq8a82uWD1me5xJe6_JrENuu9paH5VB98jSDC-R4k1S8TlG6-wX8mjZqjwAOQEhNeF4n-u4hJTSpGVFIqSWPL_XJN1RPAcp6r9QFxS6-aQL1C8K_7lDzZ2u4HJvmXHmbae_Jcpc_FQpwBtrOR6qmz0g3F5FvZUNkLlXLjQQOz5lNf73qZDQdfAAWDRhAELIW4vopKOeC95H9gmi8YYnj8AnUx0xnKZUyU33tTCokOPxf6mdk57FGQz8x5QFr7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e401075c89.mp4?token=shOXTBGQvsmnFAD6olQ8TFlylk9TIcfhU3TLzthjVs9zqFvaTqbw5fY8YhBuSBU98s3EFJ39quWauLXnexMQzLkhRq8a82uWD1me5xJe6_JrENuu9paH5VB98jSDC-R4k1S8TlG6-wX8mjZqjwAOQEhNeF4n-u4hJTSpGVFIqSWPL_XJN1RPAcp6r9QFxS6-aQL1C8K_7lDzZ2u4HJvmXHmbae_Jcpc_FQpwBtrOR6qmz0g3F5FvZUNkLlXLjQQOz5lNf73qZDQdfAAWDRhAELIW4vopKOeC95H9gmi8YYnj8AnUx0xnKZUyU33tTCokOPxf6mdk57FGQz8x5QFr7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمادگی جان‌فدایان برای اعزام به جزایر خلیج فارس
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/453110" target="_blank">📅 14:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453109">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b9fb72f74.mp4?token=sIemLCaS3VyVpZgYx9nIfWfyqvJE3934-oVEw2TXqwIoiMf5HhI8fIo2j3EdOtvRRLC8nx_W8IlyJuD0o2mjL2D6A1OgXbRYKb15tjM1zgTI3ErWzJKJv6uYYvSOq-ik2AKL65SURi8mkpKb6-5ubc1t1bvmaF4XlGJzKGv8vVBsuYtUuUe4pTf36OyofAkBhHWtmg5XAMIuZ3fw-29QKBWRdDV_knZCOa3BVFiUmF53O7VfyL5B-WBwNBuzSFiZi0302lDThpIGaDeND8HOD_HFSSvo7ZM5AI643umvrBMfu64utLDvEO__DYZ_SnTmiNgnkCAgntJsEbhfW3lACg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b9fb72f74.mp4?token=sIemLCaS3VyVpZgYx9nIfWfyqvJE3934-oVEw2TXqwIoiMf5HhI8fIo2j3EdOtvRRLC8nx_W8IlyJuD0o2mjL2D6A1OgXbRYKb15tjM1zgTI3ErWzJKJv6uYYvSOq-ik2AKL65SURi8mkpKb6-5ubc1t1bvmaF4XlGJzKGv8vVBsuYtUuUe4pTf36OyofAkBhHWtmg5XAMIuZ3fw-29QKBWRdDV_knZCOa3BVFiUmF53O7VfyL5B-WBwNBuzSFiZi0302lDThpIGaDeND8HOD_HFSSvo7ZM5AI643umvrBMfu64utLDvEO__DYZ_SnTmiNgnkCAgntJsEbhfW3lACg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌کاران حادثۀ تروریستی دی‌ماه ۱۴۰۴ ملک‌شهر اصفهان اعدام شدند
🔹
دقایقی پیش حکم اعدام «ابوالفضل سپاهی بادجانی» و «امیرحسین صفری حسین‌آبادی»، دوتن از عوامل جنایت فجیع میدان شهید علیخانی اصفهان در کودتای دی‌ماه ۱۴۰۴ اجرا شد.  جرم مجرمان این پرونده چه بود؟…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/453109" target="_blank">📅 14:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453108">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d42e8d25.mp4?token=YMVY3xwMhnbvBXGXuzK2V12sMEiHDBr9PX0X_Ul_xwhufuptwu1kxHwPGhz0e6hOs9pgG9y3djiWUT3e-rlcm8WtZBeykyR69u_9l4u7gOM4YhOdRLxgz24-VZs5CGuMaS_5Qy_KQv9RFcUUXp-L8f4uCHPDMueSnAuyY20gWxrupLgEldj4U-nmKEie5XkS5cM0JSBVVe3806I8289jASupQaCPRY5bs04vLay061cj7YjTcc15_bf4O54Fx0JWEk9F2OvIz9GQ66AfA-VD5Kfw-1Z7VDgl8sm3rL3fNvrg1OxGnp5F5muxmUCr7kSG2dmqBwhzgim0oCMnpmSbT7NZINCnb71cN3UO4zM4-essle8ymunvMjO0VFx8udKAfZZnqO1zBHSC0FMZUqfaYqVuq-10B6FQJf1dFC74ZfcXEimErHlqQ3xYPgLhztRt_yUsM4DoVtpTsFJp6KK4HsjnrrPEEj0i0mf8Kgqc0j4oWOXLMUvGWUoLviz7TpJRFX1qF4AE_ndtplFRzzu_8tdriDkER8K7oAZ1t6azfxTHiu1M4aQpXraZs1doDK95v4o5cIBFBL0H0Xd8v-roZ4zKslJ6HEEXkxvSG701y2HW9dxmq-etyoPgRMIw-T7uwvhybSAapfvIPAFhMZXOX8Re17oZVwXnjGsJhW-S8OE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d42e8d25.mp4?token=YMVY3xwMhnbvBXGXuzK2V12sMEiHDBr9PX0X_Ul_xwhufuptwu1kxHwPGhz0e6hOs9pgG9y3djiWUT3e-rlcm8WtZBeykyR69u_9l4u7gOM4YhOdRLxgz24-VZs5CGuMaS_5Qy_KQv9RFcUUXp-L8f4uCHPDMueSnAuyY20gWxrupLgEldj4U-nmKEie5XkS5cM0JSBVVe3806I8289jASupQaCPRY5bs04vLay061cj7YjTcc15_bf4O54Fx0JWEk9F2OvIz9GQ66AfA-VD5Kfw-1Z7VDgl8sm3rL3fNvrg1OxGnp5F5muxmUCr7kSG2dmqBwhzgim0oCMnpmSbT7NZINCnb71cN3UO4zM4-essle8ymunvMjO0VFx8udKAfZZnqO1zBHSC0FMZUqfaYqVuq-10B6FQJf1dFC74ZfcXEimErHlqQ3xYPgLhztRt_yUsM4DoVtpTsFJp6KK4HsjnrrPEEj0i0mf8Kgqc0j4oWOXLMUvGWUoLviz7TpJRFX1qF4AE_ndtplFRzzu_8tdriDkER8K7oAZ1t6azfxTHiu1M4aQpXraZs1doDK95v4o5cIBFBL0H0Xd8v-roZ4zKslJ6HEEXkxvSG701y2HW9dxmq-etyoPgRMIw-T7uwvhybSAapfvIPAFhMZXOX8Re17oZVwXnjGsJhW-S8OE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این قدم‌ها صاحب دارند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/453108" target="_blank">📅 14:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453101">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4LDq9r72JnjSQXNC-34PM2em7SawgeDgLdRRvB64xcRpzBiqdR32qhBVFEzBGghc6Et5_Ti2ngb0RaqJ5WYhZ5QeuiK6DsGp3hxj79_-2LqRrcxJsa_ghDDRFmiNAVLLS5y3seb4JT6FJsigaNNaPCOOE6Gepk4ibZ6n1H2VqG2wW4Tu8kLAyqQFUug6qKmM0FXUcJV6-Oc5Ij-dX7O_BhJzv4spSNYIMTVea4STe08kl8EDtAVTs9aoWVdORGReRho_sqSq52BA-N7LTfl2hMY-mJTfPepfyCTqPFByn-jmjKAk6rIgs7LXFcH30ev4csnbHwPjwTALNNhFrtgNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h740hg2_7BuuG6qiLT8EBtVyYYLwNi1xNquvZ_WLVlROWdWtT004X8WUETOFqQvowhbmOqY7c3wbRrlqNXMXEq2zCwHWJvf1AcFrC-swMC1TK1Q8R71dfmix5MCqGYhUU0O5NsHQyGti3VzOkAaNFQd-XPIznZxr644N2BYTram6HX09Fd_m8SPkimAvInHGABGcrX6MeS-20oAm2o6zZ22ntrvIyFeSyA_-xPYadlInpx3K8Th-79Wtv3gCrfcXDZ2gI4U2AMOpah9wxijGHWBcGG-Y7FbGDuQn71ITAqSAb2tT7KgZ1Y4i4bCdVEqaQ7iYm8WUYG-dbLmt8QXFyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTwmkriKgIY5R-oLSvJtcfFvQXQKL4M-nHN1x_HMoaBD8x-Uc2kGEvFxJAPX-ny8W4NAuxA24DlcTxP33zblGY3YSRdIM-ZwbJiwDniXJ3c0PjiPpNF0WG42KipgepYEADQgp8yA5Kly63s5tL7z0UOPEEc8wtHN-qUzpPsFnH40qBd1BJBQc5zlYHUjGJQ_EBMJnywP-NaXu67VYfH7LboRt_N1rLulaJCrOLitIbvAYMI-YoG3C04xEb9kXs8bajRLtOuVTtefq_x8660tTI0XaUtjyb9PBmAC_tBTuhdQXUQ6NlLbdFrtjjyl7SKQVUdW9uddWbyvM9IWUDy4Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cNrfE-KSjM9KM6Z42O5LNzkH5FoUnG-t8TDVMlp5OOugz2OWbVb_Cpp6Py8NztCJ0pd1jilP1NpAAbpatnNKn7IxW_2WvvfDin0J-BAlhUe2c-S5-7CWGL7oUbtSPFrZOx_GeEBYmtL0t8e2BiFXvxTN7FCrfw2fypgyMUwqwWKK-qZ3ldGbR3q0pDZ6_e76GrrxjuTra9lhlKUcjvOAN-HX6fkZtUEbeIevhrpSpxiPjSNmGQbreFanZToqu8tUX8SItOdwgMOWE2V4bGtpavnZqwfZ6C4JXTUYRwe449EHGRvDOQBDdfCan1bvGv_S1honDXUpL5T-ZT4scCKXqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FifrNu_DncMOs7YJjLD2J2N6whGRw1Ll8UNdU3MrVPh9J_aHgrjWECWvr3dkSX-ktwfQN85ay0uRfuJl09ISFF3VYznwnzexlYwnKM4ILjiO7ALXsaNsKpiZWsw3bwEvTEY81VKAStQ9RL2ETY3ACIUnzKeHH_YG6AM-vC2PiWFpw5tbBaPV8L1pXQjt9FBPXex3ZpKTKgxE0emK3W5dhldf00XhcaukJtXfHtjomXpjDLLWh36vetPZ36g0TzWbD1B8k0S9IiV40wCFJBpCzsI1n1iHt-Y_3p4VBD3LB6WwcyMln_R6npBCr7MmdAWm056yOQiQ74meX_lrMUIw6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bpP-6vzruCCSjbExz_FGHX0F-HFPBMS3M53DWHclvlq_6beNp-uLHD2w_ZIWVg2EFNe5UO7YMo8gEzp5pbF5avtjWI5RQUbKiaoGSSTuzQpBHJWs1yu6jCxzXXF6xkyGv0Zk3yOfpHpi34QCoz77BdgLzasIOBNX8w7v9lflUxGOiIcV5mji6_ACs5LO9aCmFA8B5tKIJm_4un6DSpDpe1gpnd4uKAPQ3mvb_GofN2B8mFWBnX6TAzRIFPOSyBgHm1TV6in_bWPkAEBo1ab1TRyxgXB8yKwNaVTauBEevMKgn9BsuI339UhlWPmJyyMqc83MaJKN8R0Zy7RuVsn3uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZYPGR3T45QqjoamqCqv7_gNdxmXqmYWlwHSRTHCEtbmbhJby3nvefdowgOeU_keDN0r92zjxPKNWw1Sl1dN0YHRG1kQhBh4KTVvNZnS9GjT-tdVbK8et7EeDAV40L4ZmrMYBplsa0TV-7-BJuDiiQuaLylLbs6UrQ47FTLFSr6bYTXEB8zXBREBINcWTnPZR9mKE39KD9fkMd1O5GthWWRz-LhLPnE-ruKTu7dSnUurszQkc18P5vfyWbJrAu8nG6z27pPLa9CceCJC3JVmwrZ-V1fJUc8bHBb4knkTyT9OyudM8DmLRo6EMs31YiwvdVd0eniv2-4QQ7gPwt_5PCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خدمت‌رسانی «نیروهای مسلح» در مرز خسروی
عکس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/453101" target="_blank">📅 14:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453100">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIOz6Z5fTckZ_ip4otdMMCJko3BqIA3bo13k6iF0OYjrWRGpukoh3KagyhbWkxU0myfctmAvbdEYd4nuxqhIiRFSYIQh_kqT9FSW2D5eOSjXjPnNNsLv6j375R5iHVsgNtbVVXtm4B4kVepHLZyBuGcjX_C0s4h_fH7dcqrV0WHwL5otseHqHfBbBGa7DqDuRll64KDnD_j4xiQOGpXTnO-qglQF6EHY7JG7CiFCMTWg2PbnnGYJ050_pkclmKEMxHPQ7eYWPHYxLIT9qsEt4x1IEvA46wCNJ6TameKzEZeXaZgU_N5MUZVf8miOmqwKxmMCMdPgjZC_h5Zlf2oR6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: تأمین معیشت مردم در دستورکار حاکمیت است
🔹
لازم است مسائل به‌صورت کاملا تخصصی در کمیسیون‌ها بررسی شود تا خروجی آن به‌صورت یک کار کارشناسی شده به صحن برسد.
🔹
برخی قوانین را نیز می‌توان به‌صورت غیردائمی و برای اجرا در مدت چند سال به تصویب رساند تا در…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/453100" target="_blank">📅 14:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453099">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLxy-KyFFr2Y1APSKYyOanCzHAL0ONkZPjKuzU7vUsIv4-sgk8eyQ98us8riFGx-N33y9MgryWwNr2j3Xl9UfiBDXAdtE9mEjdi-yJXkaLSWcZe5N8XZV8nP-sWocKd7GlFPcT6klkjvwG3Bm_ZElyc9cg554wI3Y3r-EEYUfpGjJKddwUjKzJzmMDnfD0QheOG2NSOw3vnT4rScyeObgt1_iMM2-wjWsX_yrIwPPlNyC_i-AHcMFG5xj18lj8i_r8T58K1TgQ-2G0TIAskK16BriBuHbJz4vokICSGP1RAD4EdzSwJgUOcc94aHseizb2ZFsmCm8fRFPcGqNCjS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزییات جلسۀ شورای هماهنگی مجلس با حضور قالیباف
🔹
جوکار، رئیس کمیسیون شوراهای مجلس: در این جلسه که اعضای هیئت رئیسه، روسای کمیسیون‌ها، رئیس دیوان محاسبات کشور، رئیس مرکز پژوهش‌های مجلس و همچنین معاونین و دستیاران رئیس مجلس حضور داشتند، گزارش‌هایی در خصوص مسائل…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/453099" target="_blank">📅 13:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453098">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8G1T_FrXR7q8nfYBqkGMxNgKgZpNSX5u4Bw25oWM4iXpStxsuXdNYSDUq4PMs1D5bGtzbtVmbILUH8FtAx4MDmAHyjyYZb-xyRbirdkGZ__V3GrjLGfn6zObm795jjII5D1I4HrEwEHX7zbG2AO7JvhGXt3BUFMI_TpFrI8IMNHlJB3Sq7knWyh7wRnMeOVSYhtJpXLfE9A4mrIUqv_Zk2Ks3tJjYPFfCsujXy_oHin7BluyU_b8_I97ZvtdolO9gTSNVKypMzVG-zchF2Je6j-LNUOPJT-BSd-iJ0B1dz4pVPF4ht8uUptsYl2wtaMxBGWiIf6haoYkxTZY-mDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام زمان مسابقه پلی‌آف لیگ برتر
🔴
با اعلام سازمان لیگ، دیدار مس رفسنجان و صنعت نفت آبادان برای تعیین هجدهمین تیم لیگ برتر، ساعت ۱۸:۴۵ روز چهارشنبه ۳۱ تیر در ورزشگاه شهر قدس برگزار می‌شود.  @Sportfars</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/453098" target="_blank">📅 13:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453097">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b178446800.mp4?token=TXAOjN3zn_kFFjTCBtPSxn8bd-M4FoJarxmkA3zFd1OPCzmxTmB8Ixc1gmBM4UwFE4LmVgHiiXciLjrrre9P_DXQP4SkbkUcPYTtLyFsAsdiuWAJlXfN6HwGvO6NuojqpSdgsmKoMDALmoRsim3kqAM_YTbeeDO7iZFSqjwUyRAU3bERhk-znqjX1s7MihQ8H8FimxiDtHmA18l1SSEw_lK_338K_50ypSSuxjrfPcHAHYdT_XRPyWJ74OHJqw9gIvXaOOhHnGcKEjGQpB9DSmHvVtAB5zWSYXRr-WkXsPnRzWQKxsiiQXGEEv_3rHPaDQQ2zPLNs0qs5155cTjFpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b178446800.mp4?token=TXAOjN3zn_kFFjTCBtPSxn8bd-M4FoJarxmkA3zFd1OPCzmxTmB8Ixc1gmBM4UwFE4LmVgHiiXciLjrrre9P_DXQP4SkbkUcPYTtLyFsAsdiuWAJlXfN6HwGvO6NuojqpSdgsmKoMDALmoRsim3kqAM_YTbeeDO7iZFSqjwUyRAU3bERhk-znqjX1s7MihQ8H8FimxiDtHmA18l1SSEw_lK_338K_50ypSSuxjrfPcHAHYdT_XRPyWJ74OHJqw9gIvXaOOhHnGcKEjGQpB9DSmHvVtAB5zWSYXRr-WkXsPnRzWQKxsiiQXGEEv_3rHPaDQQ2zPLNs0qs5155cTjFpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای پیام خصوصی رهبر شهید به فتاح  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/453097" target="_blank">📅 13:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453096">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tR-oKl8Dl27U7KsdfK_LHZM4nbMHekopGRwB4b-74wmcdFTenOOx25fHWm7BuE8DlWa6NJZXLrxJH0AKZxtBB_loPi1TOaCTE4G6uUAi__6iF8tDAWVlu1P5z9lz6QgaWMZw6zSTMlAzmvstJW6nc5D1LNkyhHgp8c3ZhdHsp7IB6mUVUpb__o4y1xdvWtRLZ0CVdniUzznxFcb2h9ERazJ4PpLTLyPFGIwZbZb8a3Y8S3Chyam-F7Yw4hXtmh7HzuAW0fQXxmQ5eXyQ6BfKtMP2xXsjHXEWlmRMKDyBNWK9-hllGgOcCC7-11iPwgbh2bBTiRHdYZrkn1AM6tfzBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فدراسیون فوتبال فرانسه اعلام کرد زیدان سرمربی جدید تیم ملی فرانسه شده و تا ۲۰۳۰ روی نیمکت خروس‌ها خواهد نشست.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/453096" target="_blank">📅 12:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453095">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9fJuO4-2yKnhuIUz11vUY-bakUX_NZHme0zALARyd-IPD89Nq3n6Zl5yDjM3U-HzAh3AwzQDxxr078WjDPnwyfq4p_ow5cy_jL-NYV2OFoq-mXNsRswDO3fskGVjBGn_O0f4gdv0M6BL8j6JZFEhC_CTB2nX2dfyVm8gtfRl54MtZmgL3Fz39V70MjgMCgG5zLXFbCPSHNIiLfUAVFgcXY4XrWj3BMarincI1JiS4S7S0GqhCTrbPHjrwGedNkpwStaEF2ess-so1Q2oopCr6aw4SOtf9h3uNKituctNJl97cZrTsDE59_9canoQ6Kd_KEPa10XGDsW6fup6HHvNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس از ۵ میلیون و ۱۰۰ هزار بالاتر رفت
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۵۷ هزار واحدی به ۵ میلیون و ۱۰۹ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/453095" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453090">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rlcs9MEeBEdgC1WxKswAlWa1AqgguEI_Bp6UMLlTUeKebKxhUEm-tVptn7ti5KJ8DL2Hg-jWBAZ6diVcn71b7D929H8lwV-T-wNUiXwKHSrvx4FV1IeqcNh2PblRVw7pik3xeIqIwVhRN-X6IHatQM0eA5J9tSZH0qtjf4apciWzNXaP2jTU-FwBgCS6HQOOQHmKjR-tS7RphPPbOVn5jR8aAHKX9Ed-NYHBzf4EI9LX5Clp9ItF5zZGsOEhSLtmD_YSlF8psGL1deyGMNYUI6D66WtLRlzdXS7aIMo9KDwB9TEi1PFASpnOMaPhY1UwYBtsINABt2btt0B2uFbNyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JS3gZlPE2bmSXn0sEppaDQKwqk1vP1p-ajX5L8Nr38bYIuJV6WCIbl8IfAIjp1haumzD9l0mobTqyQPJ1jdHDf-PrJD6VDYjjQCaYbdPsphHOztimTTs44Q9Ji4BPxKIWScZ2ZeQZ85crBIQmMjCb8Bhd2Fi65oLYPoFk2TDfvVXGuCkBv-PMgGvhNnJj3i0SaShWc2A53j3Q0CbyVpDglRTA_rwa1HiPnKasJCardfqUFjIJLBBWWjr19ixMeaxWkr15f6iwnlru3CW1N_TZp6cJMxwffmajUxXf93O0gp5Ym2Ojlddol5Q70OWoD7Not3raAC6dzOGEHNpYz9czQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l64KZxuB86xomrqMNznyRze0d2HI6AgFRNVCklkZtX-FfJDKYBCNBey0BtdCuM2xmESoWX15jlGwJ0PHkG7oth1ICqaN7dQ_ahsUTz4Y64yEG1dKpTXb6m-j-1cPOfC0MHqpZI2mW8YbAI1askAvzxxz2ykD3tPxib2nyKhjAuxNHmuWYDEK2PyCu62qICGx9C4whGVRz-TIMfVyaihiEVhsnF_Udj9CvRbw_SB9A1d9sQzXhdtFSsZSRmvtEEDfqEIre7ma9Uy1LT_ai9jchVhEoJLTH6L_Jub3w264T0JNQro2DM6c1Yp5NpTXJMnA65c-TNg0V5MudnwMkKxiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cPE8P68hC8QI_74IC7rSZj6pVEGbeTz6ntiTIfqkArDqVJmU-2A0THN46G5av4O9xw_FK6uPbt4WfzOLYDZdCZ5cWkcmHZEDA-yUo3cnbHd4TFFNbY3mpTDZiCUDhTctdihuLuJJV4VfoHPrPSbPDfBSzOsn7mJcfPGr3qiSl45h-rbN5c-HXPFTu0kibr4btqCiVw36fAou-PbldqS3ioLPXjIqfn7sV736IS9V7Myv-rnNeoylEo8txuhRUgMeyoLLrzqFE91a4z-729AJdgcBE3ALhpPAvXSV1_51xpKcktrEEJzve8DOhLbgpSVU_PrFkDNHx7TMuSaPf87ylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXHSTkjcpvq7zG06P8Qd5hDlYfBQI7-EHQnpFSFVn2jBQlbhrcgtp8dDtoPMl19pBVUSv5dCfZItSIypXS-mfYkgOJ5p9IjXhUAJm2SaOsl6WTNeCtWPwl2jC-Qm0QA4tFuMxBg0fIvrc7AQE2KrfGlDIR_3_4hUJiux5XeaYpqhSNKU8exkbufcbTL9fgea5_J69GHG-Z1gQD6ajmQw9sckyf_iuMWM-cR1lR1kffmqfuiPXn3NLf-3SJHqZ2MteSoRULER21oQaz6YYWfKlmAT7SPLyMkgJykD2bJFNSP6R2PeG_uyrf5zOESOy7mXXLhiaGCF21gCMie81uLx-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
هشتگ
#یالثارات_الحسین
در شبکه‌های اجتماعی ترند شد
🔹
در آستانه اربعین حسینی، کاربران شبکه‌های اجتماعی با داغ‌کردن هشتگ
#یالثارات_الحسین
در شبکه ایکس (توییتر)، فریاد خون‌خواهی سر دادند.
🔹
این هشتگ طی روز جاری به یکی از داغ‌ترین موضوعات شبکه در میان کاربران ایرانی تبدیل شد و کاربران در محورهایی مانند تبیین ماهیت اربعین حسینی، خون‌خواهی رهبر شهید، بیعت با رهبر معظم انقلاب اسلامی، تأکید بر وحدت جهان اسلام و... به تولید و انتشار محتوا پرداختند.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/453090" target="_blank">📅 12:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453089">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0T5NMGbODD7yvgasN-kRTBkGY6vXQIF1fhhYyJgt52th9tCPPGRRyuX3KuB6P3eWm1_nnJDCEnhnXfFJB1dr5yix7NHyKCwPsy_xfNOjNscXtDcMh-o_-N6w1zbA0lyCYE7pnxP7WbqjMGngynxiVs5ehw3ryTvMbo6hDi8iovM6IepziVZAGNQGDVhISG5fub8YSAZBqpQSkPdBDaWNa7snKCVpYfwcilsuLcRr_fuULKeKUbJ6_juyFCGYFJBpDXb-vf3872CFYWYiaJ94WKWIRovGstvUlEKYewQq44mAsR-8iScUzEKdFXMYYzW_qxsLqAs1rFtx-WEvl8oHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دینار تو بازار کمه؟
🤯
هرجایی دینار نباشه، توی دینارز هست!
خرید راحت و بی‌دردسر دینار از دینارز برای سفر اربعین.
🏴
@dinarz_app
🔹
نرخ و ثبت سفارش:
https://dinrz.ir/ix6
🔹
تلفن پشتیبانی
۰۲۱۲۸۴۲۸۴۱۲
🔹
پشتیبانی در بله
@dinarz_support</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/453089" target="_blank">📅 12:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453088">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/453088" target="_blank">📅 12:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453087">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FER0P6RPj4yYA9zJWVWSANPwcebvEKFBlXehOYM-bgyoErQeYvljxxnw_SAH9BJvbXaXhJiWMjnxhfUeUZnSFJsxHklyim318ytX7kwrQfXlfOQu2spJaEC_H7vTSVRHW9KCPnghKvsc2_ZPj9T0dBLNJZGr3nH99zfhdWHvIzKlKWPz1uLRn1tsjlmIaawFSX6xZSBAlrd8Lw2wIEgxm83baihn1jQJfjucE_9m79Hf8aaPP54uBqk-rzRLgEX_EK0VltGI6pVw-xfBwx8XMhm4D1NqJJgvHfqqaHETVahzxLP2ciG5zC2F4AhYooACj1MW8WHAg7bgs-279_TnRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوران وقت‌کشی دروازه‌بان‌ها به پایان رسید
⚽️
فوتبال انگلیس در فصل جدید اجرای آزمایشی قانونی را آغاز می‌کند که هدف آن جلوگیری از استفاده تاکتیکی دروازه‌بان‌ها از مصدومیت برای توقف جریان بازی و برگزاری صحبت‌های تیمی است.
⚽️
براساس این قانون، اگر داور اجازۀ ورود فیزیوتراپ برای مداوای دروازه‌بان را بدهد، مربی تیم ۱۰ ثانیه فرصت دارد یک بازیکن غیر دروازه‌بان را برای خروج از زمین انتخاب کند. این بازیکن پس از شروع دوباره بازی باید یک دقیقه خارج از زمین بماند و تیم در این مدت با یک بازیکن کمتر بازی خواهد کرد.
⚽️
اگر مربی در ۱۰ ثانیه بازیکنی را معرفی نکند، کاپیتان تیم مجبور خواهد بود یک دقیقه زمین مسابقه را ترک کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/453087" target="_blank">📅 12:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453086">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHHS4we30JUyfXsxAhwxC9edlVhZmzvlBLw1YSPqLTRCYUhIS2HTtVt0Nfm9oWreQFgmGEntfQrQgot3xCr7vSChhUyeSizQ9BkjNrV2F2JaKeWA_hCvwAJgzcvhvbUlDDg911gzxjHy4EX0IcxypjJgNIwmbFb4lv_xpIK9OGJbKWJPG5WiwugH_pOj_peRBgDl5oMqt6JC1R-wzQJrTXVx3O5ICQeTIn2HNwp_4ski45Lbz4w0d9MP0DEuJfnUMFi3rONkr1T6c6lyKbfM9dt9yF7AJGLSxZXKOBjSgAhZeqUji1We1-AeYlldtY9M_JKrHT2iH32BC5rU_ULY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو رونالدو تهیه‌کننده و بازیگر یک سریال فوتبالی شد
🔹
فوق‌ستارهٔ فوتبال پرتغال پس‌از پایان حضورش در جام جهانی وارد مرحلهٔ تازه‌ای از فعالیت حرفه‌ای شده و براساس گزارش‌ها، در حال تولید نخستین سریال داستانی‌اش با همکاری متیو وان، کارگردان مجموعهٔ «کینگزمن» است؛ پروژه‌ای که «دیمین لوئیس» نقش اصلی آن را برعهده دارد.
🔹
براساس این گزارش، تصویر‌برداری پروژه در لندن آغاز شده و قرار است چهره‌های شناخته‌شده‌ای از دنیای فوتبال و موسیقی به‌عنوان بازیگر مهمان در آن حضور داشته باشند؛ از جمله تیری آنری، اسطوره فوتبال فرانسه و دیو، رپر سرشناس بریتانیایی.
🔹
این خبر در حالی منتشر شده که چندی پیش وین دیزل، ستاره و تهیه‌کنندهٔ اصلی مجموعه فیلم‌های «سریع و خشن»، تأیید کرد که برای رونالدو نقشی ویژه در قسمت پایانی این فرانچایز نوشته شده است.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/453086" target="_blank">📅 11:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453085">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5oQU4yMXRmpg02rU0d59uW33vmzwAfroxgKP7aazziv9mVVpJ0OcuBbIht34KoykkBvOcc1JIoGO8qUX_zqLzO-ZtHC35xmS-GKZw7hpDMExHZ3wcVR6Ek1J9yFkPWWMoQ_w8qQpj2NKLvoDtDWh2ruzcnuCExD6BwnPAsx01aO0StDgpsn_V0mxflhupLoZG738UVgjAIYR37_bADoTrCjkJCnHDjXoFvi_Thd1JMrItW3tbOE9IbUZP8ribgQB0RCpIo1DBvREf7q0quGnbsx13yzoIUIY2k71JiVt5fjfNWJBGz45_0sZHPhsi1ZUWewOq9wuQUIo_i1eo3eyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین تأسیسات پالایشی عربستان از کار افتاد
🔸
شرکت آرامکوی عربستان پس از حملات پهپادی یمن، فعالیت بزرگ‌ترین مجتمع فرآوری نفت خود در بقیق را متوقف کرد.
🔹
ساعاتی پیش یمن اعلام کرد که با پهپاد خط لولۀ انتقال نفت از شرق عربستان یعنی همان خط لو‌له‌ای نفت را…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/453085" target="_blank">📅 11:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453084">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/907d714173.mp4?token=HKi0uyEOgFlejFC-m5Utn7_pXQy42dGmFsd0aJObqV7ehwwOLa18NwOoVuAmQ16QnYeDdK-GdL2goAI8evJA3nSsVUTLSBInO1VezPv9rGG55XXgkEeboYG8WxFEPg51oD55vJxSpeFHID9-YUuEXJjj7moA2KBxa85pZubdiK0FqxM7NohBlA8fy6s7iXILcXKXWOQIyUYdr_ZapqqTlg0gbFfzTqjALyGqQ4FrERu7SmSREyV8gb9lcrKWbgvBgEvykLW7_TDlvEuK2KJ0CcvdSuryJV-EgCzno54crZVxXFPCSWfQNK3uuRYZqVVV2By01zbzIWqUDo7vXB-HOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/907d714173.mp4?token=HKi0uyEOgFlejFC-m5Utn7_pXQy42dGmFsd0aJObqV7ehwwOLa18NwOoVuAmQ16QnYeDdK-GdL2goAI8evJA3nSsVUTLSBInO1VezPv9rGG55XXgkEeboYG8WxFEPg51oD55vJxSpeFHID9-YUuEXJjj7moA2KBxa85pZubdiK0FqxM7NohBlA8fy6s7iXILcXKXWOQIyUYdr_ZapqqTlg0gbFfzTqjALyGqQ4FrERu7SmSREyV8gb9lcrKWbgvBgEvykLW7_TDlvEuK2KJ0CcvdSuryJV-EgCzno54crZVxXFPCSWfQNK3uuRYZqVVV2By01zbzIWqUDo7vXB-HOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصویری از خدمهٔ کشتی توسکا که ساعتی قبل وارد کشور شدند  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/453084" target="_blank">📅 11:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453081">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugeUHeyh_OS3o5DxR6k6BZuG5dCZpuYxMFzyqtiKrDzHcl3eEBiLgfQkVn4j4jTFgTkok1BeWqUvWHMyTc7lmeCtYy6T9O2_DjT62Khv_BgPB2T9oSkuw5lmqJT6W5D76mtfoxBRGKQnYRtbofAnRpqFmbsKRNTQKpSJn22HYwnFJSYownkGRhWp6x1ablDgDdcZ0ObXofLkzEwlPh5Goz4lC8dFi_Rbb91r0Mb0Fmp048pwVn3sddxWfMkgcmwWRRcZRRuCxu5tzo_Ck6st_5N747EfRA7_QyTQCio7KaDbNfx3qB4eP_aK1SCFrw7ELS_Y69bpfxdCEDraSpRb0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSB4zoyikvDNfE7wDdf3qwrMJjGd8Ajt-B8vBVJd3LCC_0tUsltcUwQiVvT5Z2swgXT5SB0_MGP8iMWOlQfxInnze5TB_2aPfnTPHJPuJ0anjJYLlHbwakrdqaR6Y5NyPbhem-u9eGzDpQYJpLTm0YtdsKCBMV2oGqF9CIdkNs_8RvWex8OTi_XEZAVchAuc8TNGgWIEHTwiORrvOHJBUA0JKQC_RBG6v-tMK-5uKu8nQFQAEny8YUDYFISCJAyyKyePG0jCGbv0q_16BPkMpNJgNV9sF_Rc4KlVUQAFC-R1zNlYGRfIM_i0ZuAr7LmRFwclgsHFhWM7Y7AYZXmPYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H0d9Wtcr70hKXJGgWSdDGWZTqyQU3aqRFLUHkUdzLML07Zpxak44C1N0uIXI5YetYrwUrZWqObUFW_8VL3HqTo4ff04maGk6Uxgc8VmfsOW3vEKMCvTYb2OgNsfuYQYtedKI5feAv3ezlI-tevj18AS6pIro0FdCRrRuAtXOSxI_8jZr9rykKg4_JvPut99fiqCmDRWGbFwIlHdL5CbAicHeuN1zd--s7GOAfu8Obq0OECXFmlDH2oLJsHPpZVZYm0yjCYQVUMnDX5TRwzkiDo2GBXhVH1VHQM6RCqF0i5W_lrptRrLzwj0-17toGtXLmH88SwD4LHZHvyWZPpsXSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جلسۀ شورای هماهنگی مجلس با حضور قالیباف
🔹
سخنگوی هیئت‌رئیسۀ مجلس: صبح امروز جلسۀ شورای هماهنگی مجلس با حضور قالیباف، اعضای هیئت‌رئیسه و رؤسای کمیسیون‌های تخصصی تشکیل شد.  @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/453081" target="_blank">📅 11:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453080">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8elwATrHlDVh9zTKxDpVWaSO_kb8lKn4QuNcOTBvdY7eY8TTAQ4zlGsfIZawW5AUNfaPleGnAhPr8iBfQQJW9u5_Y8hCATMj712axKwlNJicPr81NOoI31Ci5LI9dxp5ACBS7gINpZhq4nJO0uqHdpzkn6sqwrWiMG25TZCgKJgSX6v8-cGwwOHvKiYSR4AV58beMhyFfYY_DrsHPI3K_sG8XL5KVjxsAZPnptAtssfaRSB8aTYW5LiU86nQNHbb-2CbHBIdKhjSEJR5PkxLIrfzAd04Rf0Foj1gX-OsmJg-f7LjZ1KOfgPLsJFIPYdod0H4-Nu_MvDKGLKcIAgQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اژه‌ای: اصل «ممنوعیت هرگونه تجسس مگر به حکم قانون» در همهٔ شرایط لازم‌الاجراست
🔹
ما در همه‌حال باید به حقوق مردم احترام بگذاریم؛ مبادا به بهانهٔ اقتضائات حاکم بر شرایط جنگی، خدا را فراموش کنیم و به حقوق مردم بی‌اعتنایی کنیم!
🔹
معنای تحقق و گسترش عدالت، این است که در همهٔ شرایط، حتی شرایط اضطراری ایام جنگ، پاسدار حقوق مردم باشیم.
🔹
اصل ۲۵ قانون اساسی دربارهٔ «ممنوعیت هرگونه تجسس، مگر به حکم قانون» یک اصل مترقی و لازم‌الاجرا در همهٔ شرایط، حتی شرایط جنگی است.
🔹
این اصل، راه را بر هرگونه تجسس خودسرانه و مداخلهٔ غیرقانونی در زندگی شخصی مردم مسدود می‌کند.
🔹
اولاً نباید بی‌محابا با هر درخواست تجسسی موافقت شود؛ ثانیاً اگر ضرورت اقتضا کرد، باید میزان تجسس و فرد یا افراد مورد وثوقی که قرار است به خروجی این تجسس دسترسی داشته باشند، مشخص و معین باشد.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/453080" target="_blank">📅 11:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453079">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9383d1d6b2.mp4?token=BAtPVDi8XJrF2DQs58MyHqbkV3Ygzuq9C4c41VbiaB0qdMGfNnmZpE_D7IEtlAbsv6BFnwJ2_dPwckilTXm-AKf3IdhUI7pnISVYA2Y_ARjRcdHtaJiS7wQdHpDxb_bVV3CWDSVZHp6JCvgTv3NBp4XpVm_9H2TD76hOKGqz-QTCFNqFcKqJUABKPlAe2FhH2ZjWFmMIngfkT7ZDJfVZTn8ZjNy8pNeabQM5-pTuE3XcWvabe8LtEX1YCHodRYQ0cbU85TNthDsqa040AXm6FTfaCi6Kc1BgO3tca3D42_IS3cyJT8r72GTcvRT0iAg7en1muY-pZ2beo0BjUYWGsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9383d1d6b2.mp4?token=BAtPVDi8XJrF2DQs58MyHqbkV3Ygzuq9C4c41VbiaB0qdMGfNnmZpE_D7IEtlAbsv6BFnwJ2_dPwckilTXm-AKf3IdhUI7pnISVYA2Y_ARjRcdHtaJiS7wQdHpDxb_bVV3CWDSVZHp6JCvgTv3NBp4XpVm_9H2TD76hOKGqz-QTCFNqFcKqJUABKPlAe2FhH2ZjWFmMIngfkT7ZDJfVZTn8ZjNy8pNeabQM5-pTuE3XcWvabe8LtEX1YCHodRYQ0cbU85TNthDsqa040AXm6FTfaCi6Kc1BgO3tca3D42_IS3cyJT8r72GTcvRT0iAg7en1muY-pZ2beo0BjUYWGsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: قیمت بنزین سهمیه‌ای تغییر نمی‌کند
🔹
در بنزین غیرسهمیه‌ای چنانچه تغییری باشد حتما اعلام می‌شود؛ آنچه تاکنون اتفاق افتاده به جهت آسیب‌هایی که دیدیم کاهش سهمیۀ دوم از ۷۰ لیتر به ۵۰ لیتر است.  @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/453079" target="_blank">📅 11:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453078">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0165bcd616.mp4?token=r_znwMqb-du8xptpyR6O6OKzmSYwythpRmcCLzIyoYomNz-P67ubzuCp9YczI3Dzwei2oj0K2juLCBxUybqCLYLrRLoKhle3zWhcmRN7rVmH3SjMueMzLOVGcyWOl_LxSkP1U-LuEaMgiHUT6867s_zhIHvuZCP7DNh1FHSbQT3PljPxrjoN60DZ0l3cE5TkLk4mEZRCxtcOIotl8gyAo7HmvtnvjJd_43_AFf0TB2DUttzNNO-RjIGiEoa_j0ln6HO7Afvcak_bwJh05piLdfkNzZ-428NAV7kcagw2yeM0Wr2_DNWr7kObieuz1D6UVC6lGxLZiLSKO5GjEwqAIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0165bcd616.mp4?token=r_znwMqb-du8xptpyR6O6OKzmSYwythpRmcCLzIyoYomNz-P67ubzuCp9YczI3Dzwei2oj0K2juLCBxUybqCLYLrRLoKhle3zWhcmRN7rVmH3SjMueMzLOVGcyWOl_LxSkP1U-LuEaMgiHUT6867s_zhIHvuZCP7DNh1FHSbQT3PljPxrjoN60DZ0l3cE5TkLk4mEZRCxtcOIotl8gyAo7HmvtnvjJd_43_AFf0TB2DUttzNNO-RjIGiEoa_j0ln6HO7Afvcak_bwJh05piLdfkNzZ-428NAV7kcagw2yeM0Wr2_DNWr7kObieuz1D6UVC6lGxLZiLSKO5GjEwqAIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ناگفته‌های فتاح از عملیات ویژۀ ستاد اجرایی در جنگ رمضان  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/453078" target="_blank">📅 11:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453077">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abe43742e5.mp4?token=ntgUSQpXHhtZWQ_8j9kuEfwULs6YAGwnQ4VhzLwZylIhmlVFZPpIj9NKVSKVLFGjNL2VQ_VgqS47m9fEWsaTQVuP2gr73VXDDuVk5RwdmIMUT1PNmqaHV10Jx4vfSf6pewmPAZw8EfyaMObGo90P64cz5ihozwX273z4xihsJgXdVaOsxXPaIApEFo5deqg7NkJPi15v3tiQSoB2eK-0oI37Ul_Q54jlYFqlLC68wojgH9ZjGhxkBLgD0tuBR0OM6p1VufKnTsMtFGv3iS83pLMVFe8xD_i2xJIe54UifaKm9wKGkgjMCozx5uNMlb0W5cI9cRVubE25tpTl1Xgs0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abe43742e5.mp4?token=ntgUSQpXHhtZWQ_8j9kuEfwULs6YAGwnQ4VhzLwZylIhmlVFZPpIj9NKVSKVLFGjNL2VQ_VgqS47m9fEWsaTQVuP2gr73VXDDuVk5RwdmIMUT1PNmqaHV10Jx4vfSf6pewmPAZw8EfyaMObGo90P64cz5ihozwX273z4xihsJgXdVaOsxXPaIApEFo5deqg7NkJPi15v3tiQSoB2eK-0oI37Ul_Q54jlYFqlLC68wojgH9ZjGhxkBLgD0tuBR0OM6p1VufKnTsMtFGv3iS83pLMVFe8xD_i2xJIe54UifaKm9wKGkgjMCozx5uNMlb0W5cI9cRVubE25tpTl1Xgs0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: در ایام جنگ  ۳۵۰ نفر از کارکنان دولت به شهادت رسیدند
🔹
همچنین مردم عادی که داخل ماشین نه موشک داشتند و نه اورانیوم، و تنها در حال عبور از پل بودند، به شهادت رسیدند. @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/453077" target="_blank">📅 11:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453076">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d30a7839a3.mp4?token=mm43JJ8iFVg96E_nygl8NxQL_WrvYTjAfc23rraM87gNZEe0wgzevRd3zahB16QIkRHzE1vx_SUy636ldRAD85YV9wyO1WvUEov_AZnEPLH3JzJCvlv4CKrh5zIMqCWj6eLtooeJdvEh3TZhhEBRaMTO20fpsqA4VHVwlQ4UG1NsEY503wzDKYhghhfQjiQYL0Li8Ey_SF9fJFI26k3D-MjsJ4PuZNp5flwnYnEQDwox1jiDxHHD0M3fWGkbrdexK0DI-QjDAuK0ZNK4Bq2s5dXpdKkILKdjD_Mo4Kr24iSVoy0Mgb72S_7UD3SIHnWxZNHE0qAljTS_N7M_piCURg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d30a7839a3.mp4?token=mm43JJ8iFVg96E_nygl8NxQL_WrvYTjAfc23rraM87gNZEe0wgzevRd3zahB16QIkRHzE1vx_SUy636ldRAD85YV9wyO1WvUEov_AZnEPLH3JzJCvlv4CKrh5zIMqCWj6eLtooeJdvEh3TZhhEBRaMTO20fpsqA4VHVwlQ4UG1NsEY503wzDKYhghhfQjiQYL0Li8Ey_SF9fJFI26k3D-MjsJ4PuZNp5flwnYnEQDwox1jiDxHHD0M3fWGkbrdexK0DI-QjDAuK0ZNK4Bq2s5dXpdKkILKdjD_Mo4Kr24iSVoy0Mgb72S_7UD3SIHnWxZNHE0qAljTS_N7M_piCURg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قطع سخنرانی ترامپ با شعار علیه کودک‌آزاری
🔹
قطع سخنرانی ترامپ در تجمع انتخاباتی جمهوری‌خواهان در میشیگان با فریادهای معترض آمریکایی دربارهٔ پروندهٔ اپستین، باعث مداخلهٔ نیروهای امنیتی و بازداشت او شد.
🔹
درحالی‌که ترامپ در این سخنرانی مشغول تمجید خودش بود، یک معترض با اشاره به پرونده قاچاق جنسی کودکان توسط اپستین، ترامپ را «محافظ کودک‌آزار» خواند.
🔹
پس‌از قطع سخنرانی ترامپ و بازداشت یک معترض توسط نیروهای امنیتی، رئیس‌جمهور آمریکا به‌سمت او گفت: «او یک کمونیست است؛ او یک کمونیست است.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/453076" target="_blank">📅 10:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453075">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7849caf617.mp4?token=e0kQ1YK5ooZkklrR-Y29rF36TtJziYyIHII9ZmNiqqAVF6dgGN1Wa2VyjY9WUk0-D5PJNaSMmhbYBLZhX8ah9PNU-uYmtrQdRlbgTabRla7UMWewAqr69cDMoz0ONhHGzxXz1oixX4W93AzGGMKbrVYNtp6LudOT_fQ5bGP9wqeGUFnx48lR2cMpBS6flVw8rIg-HLbyFU11Cpv-L6ywZfzDLQDIFhkK7W_kuutQ57X_1IyXrAvBYwBL96X8Pq98eW0GlHZGlfI25L9bp92BUabOp5aOYFAjhCqEzoWQCgSg12LHSBSvys1CJorT8iwzfsgn96IX9Kl1RGsU2TTkIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7849caf617.mp4?token=e0kQ1YK5ooZkklrR-Y29rF36TtJziYyIHII9ZmNiqqAVF6dgGN1Wa2VyjY9WUk0-D5PJNaSMmhbYBLZhX8ah9PNU-uYmtrQdRlbgTabRla7UMWewAqr69cDMoz0ONhHGzxXz1oixX4W93AzGGMKbrVYNtp6LudOT_fQ5bGP9wqeGUFnx48lR2cMpBS6flVw8rIg-HLbyFU11Cpv-L6ywZfzDLQDIFhkK7W_kuutQ57X_1IyXrAvBYwBL96X8Pq98eW0GlHZGlfI25L9bp92BUabOp5aOYFAjhCqEzoWQCgSg12LHSBSvys1CJorT8iwzfsgn96IX9Kl1RGsU2TTkIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است
🔹
فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است و هواپیمایی که به‌تازگی خریداری شده بود مورد اصابت موشک دشمن قرار گرفت و تنها قسمتی از دم آن باقی مانده است.  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/453075" target="_blank">📅 10:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453074">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3db12c4819.mp4?token=UOvTgUV7qGMicGxfr8HkHYQl4NXQhh9wz9Qf2rHzHdYTu3QGg79NQ4SoRndFHjpUEDwru58DtlSxkanh2xBXUh-U6ZwMC0Ld6BGaJgmfX7BC41clqHWDHgtJG9RZi80epapBRMPac4DJs-LMD9Go_8Z7zS_aWpVjc0Jth6enFpqrspLfiiQ4Yyd8x7tyuIhHbiloSFmzmmb39gzzSlTU9aNKp8pLYVJwH0Dk1OVGaJGnGLwyKGl63dv8G6y_d-9TlHOR6WfG4DmExFfolX6ARGtL1t-npTsNCy7nWY1V29Ynwzz0lKS2dq_2PlSp9GNXsc40AVR0FZZnopDo1gM5OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3db12c4819.mp4?token=UOvTgUV7qGMicGxfr8HkHYQl4NXQhh9wz9Qf2rHzHdYTu3QGg79NQ4SoRndFHjpUEDwru58DtlSxkanh2xBXUh-U6ZwMC0Ld6BGaJgmfX7BC41clqHWDHgtJG9RZi80epapBRMPac4DJs-LMD9Go_8Z7zS_aWpVjc0Jth6enFpqrspLfiiQ4Yyd8x7tyuIhHbiloSFmzmmb39gzzSlTU9aNKp8pLYVJwH0Dk1OVGaJGnGLwyKGl63dv8G6y_d-9TlHOR6WfG4DmExFfolX6ARGtL1t-npTsNCy7nWY1V29Ynwzz0lKS2dq_2PlSp9GNXsc40AVR0FZZnopDo1gM5OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است
🔹
فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است و هواپیمایی که به‌تازگی خریداری شده بود مورد اصابت موشک دشمن قرار گرفت و تنها قسمتی از دم آن باقی مانده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/453074" target="_blank">📅 10:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453070">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d321b0eb.mp4?token=KBLr_6E7Rny8eOCbFrtlXhcxtRMUhRrU2WKHcJN25FKZxDloTDmRMrlt7UKUaLGWVQnT6wpZV3MeYkSc6SKD__lTZF_yDh_tTtGzq7oUr1paGIXPPnFqEzav4sWT2YxyifLLHAjBSzWpTWbUCxjSSwcO0qGly5ai-SAtrDH4B0Kfmw2zkK6-lIvfA95X36Zgu4a26YGyW4klUTmu25i06nz_FnetdCu0I8xHAvZ7foe5dAfNlLMXmO05VHimsA10mTLfxyXLF5CUNs_0H3Qr_MCpwd57bLK9p6YuEQut_cB7Yx9Js8Rve14ykoADtWeaMruKcaJ-011gmOUiZojkBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d321b0eb.mp4?token=KBLr_6E7Rny8eOCbFrtlXhcxtRMUhRrU2WKHcJN25FKZxDloTDmRMrlt7UKUaLGWVQnT6wpZV3MeYkSc6SKD__lTZF_yDh_tTtGzq7oUr1paGIXPPnFqEzav4sWT2YxyifLLHAjBSzWpTWbUCxjSSwcO0qGly5ai-SAtrDH4B0Kfmw2zkK6-lIvfA95X36Zgu4a26YGyW4klUTmu25i06nz_FnetdCu0I8xHAvZ7foe5dAfNlLMXmO05VHimsA10mTLfxyXLF5CUNs_0H3Qr_MCpwd57bLK9p6YuEQut_cB7Yx9Js8Rve14ykoADtWeaMruKcaJ-011gmOUiZojkBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ ۴۰۰ پهپاد اوکراینی به مسکو پیش‌از دیدار زلنسکی با ترامپ
🔹
سوبیانین، شهردار مسکو اعلام کرد که «بیش از ۳۹۰ پهپاد دیشب منطقهٔ مسکو را هدف قرار دادند»؛ حمله‌ای که تنها چند ساعت پیش‌از دیدار برنامه‌ریزی‌شدهٔ رئیس‌جمهور اوکراین با ترامپ انجام شد.
🔹
آندری وروبیوف، فرماندار منطقه مسکو، اعلام کرد که حملات پهپادی به چند ساختمان مسکونی در شهر چخوف و روستای واولوو خسارت وارد کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/453070" target="_blank">📅 10:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453069">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انفجارهای کنترل‌شده در امیدیۀ خوزستان
🔹
فرمانداری امیدیه: صدای انفجارهای امروز ناشی از عملیات کنترل‌شدۀ انهدام مهمات عمل‌نکرده است و نگرانی برای شهروندان وجود ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/453069" target="_blank">📅 10:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453068">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/055057e6bb.mp4?token=f6Xd5TISptfFGL7gpott_2lG3oYJ7PnmvyAmPJk2-iCAOF4XHMF1IWWurM4e13N_Yraac_8Gk9DgNZ9jVMrQp7RB7yAyUoq0PM8aHPLn2cQSCH7dw3GRsdVByk_vB0_N0KrcPACFn846L9B0iEzBeFed1PVqWXGUL2lfQUx3Wt-p8a0wYJO_SQp9lknJaxaXdMMuJkWfjSEDeys0h3GeW7ifrEbsUy5s9GYeabF1XLZrSV2Q8dVjhImdiqitiahZaO11gOq_gBq7PZUQ6jJj7nUR6saaaO1u-OG3XmO1EaSA7C2yB7yPeRMR8kKud7JtGpSNzzwTAgKN4JMbtbm0_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/055057e6bb.mp4?token=f6Xd5TISptfFGL7gpott_2lG3oYJ7PnmvyAmPJk2-iCAOF4XHMF1IWWurM4e13N_Yraac_8Gk9DgNZ9jVMrQp7RB7yAyUoq0PM8aHPLn2cQSCH7dw3GRsdVByk_vB0_N0KrcPACFn846L9B0iEzBeFed1PVqWXGUL2lfQUx3Wt-p8a0wYJO_SQp9lknJaxaXdMMuJkWfjSEDeys0h3GeW7ifrEbsUy5s9GYeabF1XLZrSV2Q8dVjhImdiqitiahZaO11gOq_gBq7PZUQ6jJj7nUR6saaaO1u-OG3XmO1EaSA7C2yB7yPeRMR8kKud7JtGpSNzzwTAgKN4JMbtbm0_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شریعتمداری: بی‌تفاوتی به خون‌خواهی، مجوزی برای ادامۀ جنایت دشمنان است
🔹
مدیرمسئول روزنامۀ کیهان: رهبر معظم انقلاب در بیانیه‌های اخیر، خطوط و محورهای اصلی را به‌روشنی تبیین کرده‌اند و برای شناخت این محورها نیازی به دسترسی به مسائل محرمانه نیست، چرا که بخش قابل توجهی از آن به‌صورت شفاف بیان شده است.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/453068" target="_blank">📅 10:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453067">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922699c9bb.mp4?token=vsaWk4xeCyAephYgLv0rGZE5oXf8tPgb9VwrJbXLg9X3ehtDq9njRAfg8PBwA7YIyrkFcQzJ6nnKPmEo9Gcqad0S20CxguVRFc7VoO-0pvSAUmvSnaqgVk-ml0kQc8T-8uSpWVyRxBYf7r0UUf0jlZO3gPFA9sjXc-klVo88SYD-vrdwtSB1xUbWqTUWYrM_M_APJ6S4p1dH86s7ZDvMzIZqfBOBPQi-E0mbTUXXg1W_rBB9erELHiVmbyqB_obhB7xCPt2rQw3dBr_wCb1YY1U9lDbZ7kgl24Mc8qCapFZfQsqzc6FIk5IFYlZrIiJN1sMwEI5TSZa_EmiPkY53UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922699c9bb.mp4?token=vsaWk4xeCyAephYgLv0rGZE5oXf8tPgb9VwrJbXLg9X3ehtDq9njRAfg8PBwA7YIyrkFcQzJ6nnKPmEo9Gcqad0S20CxguVRFc7VoO-0pvSAUmvSnaqgVk-ml0kQc8T-8uSpWVyRxBYf7r0UUf0jlZO3gPFA9sjXc-klVo88SYD-vrdwtSB1xUbWqTUWYrM_M_APJ6S4p1dH86s7ZDvMzIZqfBOBPQi-E0mbTUXXg1W_rBB9erELHiVmbyqB_obhB7xCPt2rQw3dBr_wCb1YY1U9lDbZ7kgl24Mc8qCapFZfQsqzc6FIk5IFYlZrIiJN1sMwEI5TSZa_EmiPkY53UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پوتین جنگ نامتقارن دریایی ایران را تحسین کرد
🔹
رئیس‌جمهور روسیه در دیدار با افسران نیروی دریایی این کشور، از «ناوگان پشه‌ٔ ایران» (اصطلاحی که تحلیلگران غربی به‌کار می‌برند) تمجید کرد و گفت: این ناوگان در منطقهٔ درگیری‌های خاورمیانه «عملکردی بسیار مؤثر» داشته است.
🔹
پوتین در این دیدار گفت: مسئلۀ فناوری‌های جدید است و روسیه هم در حال توسعهٔ توانمندی‌های مشابه است؛ شناورهای کوچکی که به تسلیحات پیشرفته‌ای مانند موشک‌های کالیبر مجهز هستند و می‌توانند ضربات دقیق و سنگینی به هر دشمنی وارد کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453067" target="_blank">📅 10:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453066">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2067ac5a04.mp4?token=vAa5VK8oMHBDW-m8T1JnNJQ6tJYJc_uLmOlHsZ-76FFgXhvnl3ugzm88zwPaKMRwfm2LgqkUX1a1hVfuM97RIVYW0uXGqoibNOk2xooli1Hd4ctXPs5CzTiNdJDretG_n4QJtkWEmYXp15IwEEoOIZfd5LHgOeSiLqWUTPRtpIX5JhKf9-LjAvpHSXESS_KEZvlMrZVivra1UM2PQ2rhviTZDIwo0kbJmY47usgrdLrPMFrWQjwP5v4POMtMJKGFjzg-F-K9M-BE0yfMPBALQThK02tmiR0Pz3_FeNnCikrTBZdGG69hVpakjPEd1rDEDOp1tmnIV5h-Vow0zhb5gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2067ac5a04.mp4?token=vAa5VK8oMHBDW-m8T1JnNJQ6tJYJc_uLmOlHsZ-76FFgXhvnl3ugzm88zwPaKMRwfm2LgqkUX1a1hVfuM97RIVYW0uXGqoibNOk2xooli1Hd4ctXPs5CzTiNdJDretG_n4QJtkWEmYXp15IwEEoOIZfd5LHgOeSiLqWUTPRtpIX5JhKf9-LjAvpHSXESS_KEZvlMrZVivra1UM2PQ2rhviTZDIwo0kbJmY47usgrdLrPMFrWQjwP5v4POMtMJKGFjzg-F-K9M-BE0yfMPBALQThK02tmiR0Pz3_FeNnCikrTBZdGG69hVpakjPEd1rDEDOp1tmnIV5h-Vow0zhb5gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ قلاده خرس قهوه‌ای در ارتفاعات جنگل‌های هیرکانی لنگرود مقابل دوربین‌ها ظاهر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453066" target="_blank">📅 10:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453065">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">جلسۀ شورای هماهنگی مجلس با حضور قالیباف
🔹
سخنگوی هیئت‌رئیسۀ مجلس: صبح امروز جلسۀ شورای هماهنگی مجلس با حضور قالیباف، اعضای هیئت‌رئیسه و رؤسای کمیسیون‌های تخصصی تشکیل شد.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/453065" target="_blank">📅 09:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453064">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4f35d89bb.mp4?token=sVfC5nApamHxKC5pvbcfsNRq2QWkn81ebsNe3d2myWq1TNwoNutKHuer6AvFn5vV08bxwZ_9il2sOkKojzHTYp5jKTNEKbBAfzexxjR9Y3kDz3LiSUnqsTupHD6G5yGP4qcfHTjf16Gvjwv0GH94IxejNDv6Jy7JXmxg7sNyZr9L8CbmVWyh9SzrNeFAi6IHS2toq0bN27yRm-fpZz0mmvGuutonPYYWlPJrwRqjzSnKu4LnhGnJOSHDBxXJ0M6XrxaAOKGQOzt4hA-RxNVfcPt6TU6S1ABYqaj1wnmoJp61VTN-0x1YxCJeSvIotTxQd1SxTS0IN9iT6uzsVtoJpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4f35d89bb.mp4?token=sVfC5nApamHxKC5pvbcfsNRq2QWkn81ebsNe3d2myWq1TNwoNutKHuer6AvFn5vV08bxwZ_9il2sOkKojzHTYp5jKTNEKbBAfzexxjR9Y3kDz3LiSUnqsTupHD6G5yGP4qcfHTjf16Gvjwv0GH94IxejNDv6Jy7JXmxg7sNyZr9L8CbmVWyh9SzrNeFAi6IHS2toq0bN27yRm-fpZz0mmvGuutonPYYWlPJrwRqjzSnKu4LnhGnJOSHDBxXJ0M6XrxaAOKGQOzt4hA-RxNVfcPt6TU6S1ABYqaj1wnmoJp61VTN-0x1YxCJeSvIotTxQd1SxTS0IN9iT6uzsVtoJpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی در مهم‌ترین تاسیسات نفت عربستان
🔹
تصاویر ماهواره‌ای ستون‌هایی از دود و آتش در تاسیسات ابقیق عربستان که ساعاتی پیش هدف حملات پهپادی و موشکی قرار گرفت را نشان می‌دهد.
🔸
تأسیسات ابقیق که توسط شرکت آرامکو اداره می‌شود، تنگهٔ هرمز را دور می‌زند و نفت را…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/453064" target="_blank">📅 09:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453063">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGo-1C_y-Sz_To87ocHmVtmW2WYV-kw44hHqVbw1DiHfPm4qs5o86X_22fEurCSnh2gJsYpSrX1D-jANpLziVM-ib7fvlBB3r5VS0cSmX_rtmXOg3oJ48ua2jn-eGLtv0-i_9KOy5-DYsGxS7TwcfQfz_j5OvSUnY8MZSDhT1pmVcFA91ecexgpN8YGtkWl20_ESMK-RA2xFPX-BswaAE8OLO206Ezu-jufgU3d6fv0IEui9nEmFVs5Jajfqh44GwC0mbO_7Rs07ilJy0nSDHf1dFoF0yAOy7Ey0DrLqp7ybv8O8jM69X6Gq4Nj-aqXNWGXQi6McWVXlhH7OqUP4rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا از جلسهٔ شورای امنیت سازمان ملل قهر کرد و رفت!
🔹
دیپلمات‌های آمریکایی هنگام سخنرانی نمایندهٔ فرانسه در نشست شورای امنیت سازمان ملل دربارهٔ جنگ اوکراین، جلسه را ترک کردند.
🔹
طبق گزارش الجزیره، این خروج تنها ۲ روز پس‌از یک تبادل‌نظر تند مجازی میان مقام‌های آمریکایی و فرانسوی رخ داد. اختلاف بر سر رأی منفی واشنگتن به تمدید دورهٔ چهارسالهٔ مسئول حقوق بشر سازمان ملل بالا گرفته بود.
🔹
هیئت نمایندگی فرانسه در سازمان ملل در ژنو، شنبه در پیامی نوشته بود که «آمریکا دیگر مشعل‌دار حقوق بشر نیست و در کنار کشورهایی چون کره شمالی، نیکاراگوئه، مالی و روسیه در انزوا قرار گرفته است».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/453063" target="_blank">📅 09:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453062">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌
🔴
ارتش اردن مدعی شد که ۲ پهپاد را در آسمان این کشور ساقط کرده و خساراتی در پی نداشته است.  @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/453062" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453061">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWIExjH5E3Rj1Yv6sQSgbTqXnxFM7yIfCq7nafZHYZrqnJFoHIO56IByyqOfXh4KvapDkToAfoeKAk1nSOiTtEZi0lkOzDZ59NLWrrCgcfDQey7VmcaBmrIay-ai7uNGFM_ClliE7Tw0DMY2gDIYdJlIYZIVGeW28bWq3663K25EvhY_wB2Hw6Gvy8OF0uRtr1C3N60HkmWGtQjyQeKtrcKqUMwU--LwliZXLjYQDr-HJozkiUbZj0DyWdNLwNqHAkYEElBoXQGZG6yh02XMeqLHfd9Akvt0OSOByX2iY4HtTghEtQK64ua4DbiACAO0FkHs5gckvpVsZox89gBGrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی با همتایان عربستانی و عمانی گفت‌وگو کرد
🔹
وزیر خارجهٔ کشورمان در تماس‌های جداگانه با البوسعیدی و بن‌فرحان، ضمن بررسی آخرین تحولات دوجانبه و منطقه‌ای بر ضرورت تقویت همکاری و پیشبرد تلاش‌های دیپلماتیک مشترک برای برقراری ثبات در منطقه و رفع ناامنی تحمیلی بر تنگهٔ هرمز ناشی از اقدامات تجاوزکارانهٔ آمریکا تاکید کرد.
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/453061" target="_blank">📅 08:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453060">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">صادرات قند هم آزاد شد
🔹
سازمان توسعه تجارت در نامه‌ای به گمرک با صادرات قند به‌صورت مشروط موافقت کرد.
🔸
۳ روز پیش نیز وزارت صمت ممنوعیت صادرات ۱۵ قلم کالای کشاورزی از جمله کشمش را لغو کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/453060" target="_blank">📅 08:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453059">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df15be6725.mp4?token=pHBQvkZBrhjUXrHapnXC2ymrUdtsTL8Cp0fjcMJNf9wLU_YJel9ZLVfvGC_BC3FAMqrA7ps_O8uPKCcgrymsZMYPmQPVK6iY2HD0ruySaj8oUxpseCr-NkpVvHGsZKuh7fbUCQ0r7q3L_-oZk7nDyWyD2dUz8lnp-wkZqxh6Af-nZC8849QwdSzmnupH4-2VWcqrToxfMIpQrcRWNWjAuBU1ZP87J_bsNwGbdYv4F7TWuzLr4LYp7kZGy0TXAshc26PNQwH5Grzu4piXzVMjkOqdeckAfoTPcBTOm9-RWPQ8ZZVv-F4qerw7PI05d6a-wNtCLBSSuwnZpQkBJJRZLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df15be6725.mp4?token=pHBQvkZBrhjUXrHapnXC2ymrUdtsTL8Cp0fjcMJNf9wLU_YJel9ZLVfvGC_BC3FAMqrA7ps_O8uPKCcgrymsZMYPmQPVK6iY2HD0ruySaj8oUxpseCr-NkpVvHGsZKuh7fbUCQ0r7q3L_-oZk7nDyWyD2dUz8lnp-wkZqxh6Af-nZC8849QwdSzmnupH4-2VWcqrToxfMIpQrcRWNWjAuBU1ZP87J_bsNwGbdYv4F7TWuzLr4LYp7kZGy0TXAshc26PNQwH5Grzu4piXzVMjkOqdeckAfoTPcBTOm9-RWPQ8ZZVv-F4qerw7PI05d6a-wNtCLBSSuwnZpQkBJJRZLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: از امروز دما در نیمۀ شمالی کشور خنک می‌شود
🔹
دما در مرزهای اربعینی کشور از ۳۶ تا ۴۹ درجه در نوسان است.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/453059" target="_blank">📅 08:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453058">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd296c7dad.mp4?token=QZ83QatKDCl0HFSUXIA8f09-QLJRtyKi6JoR0DEH11rC6pXAOt1y6PPqzaSN38dpaNgWSTXecad31IdzG6HKvUTagRKExI0Q1IMg0fiIxuXWtPjCLDix9MCYAvr7-kIaMeGljg6jOHi5PKp_k-CPE9A231KrkIwUBcSjEwrKCWXSokI0awUSccQwa1iyuM0reQJkp2JnKN2F-l_STKC7dMuMTk4DDkqG5WGjaZvhokTbZahewgBQInZgqtHQm3riJwuMM3Ri3HH9SDSHtrgYkedyvfsnVpTKrBP3JQlCh3SgG6SOalTRYRg6qxXp1cpTmVshMEzc6bTb7jluj3anVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd296c7dad.mp4?token=QZ83QatKDCl0HFSUXIA8f09-QLJRtyKi6JoR0DEH11rC6pXAOt1y6PPqzaSN38dpaNgWSTXecad31IdzG6HKvUTagRKExI0Q1IMg0fiIxuXWtPjCLDix9MCYAvr7-kIaMeGljg6jOHi5PKp_k-CPE9A231KrkIwUBcSjEwrKCWXSokI0awUSccQwa1iyuM0reQJkp2JnKN2F-l_STKC7dMuMTk4DDkqG5WGjaZvhokTbZahewgBQInZgqtHQm3riJwuMM3Ri3HH9SDSHtrgYkedyvfsnVpTKrBP3JQlCh3SgG6SOalTRYRg6qxXp1cpTmVshMEzc6bTb7jluj3anVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر رفاه: تمامی فروشگاه‌های زنجیره‌ای و شرکت‌های حقوقی چندشعبه‌ای تا پایان شهریور فرصت دارند به شبکۀ ملی کالابرگ متصل شوند.
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/453058" target="_blank">📅 08:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453057">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9334f5e07.mp4?token=pm9TO-D5GNlBxy_t6ygv4Uu_jnxPNaZx2fx7oTfthj7wgd76RcbeMuoT-h1Ei1x8iWZ2T-yG1dpbPq2p2Ke7dZ3QCqKLWNoLBJtQ7-hyPl2DLxLiEwKCcefmfR21FPl6fMYJIyarsTkseLDDHJrSs0yfG0R0wJ9cHrJURNP-YlpJ1p_jepWpD8JLTYbK3Du61niABqNE9BXUHUVah0ud1lU7eMC5asl72zzdAy2Pi5eJe8jxHM7DMGBOlnehBwITs2HGTdaLYoFYVtBxqJ-tf2P16vqyrnHAO_u8GLkBzij_MbAyYmg_NvGL-5DClJ8ppYEm9vgdIdqMB4W6Dhl_2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9334f5e07.mp4?token=pm9TO-D5GNlBxy_t6ygv4Uu_jnxPNaZx2fx7oTfthj7wgd76RcbeMuoT-h1Ei1x8iWZ2T-yG1dpbPq2p2Ke7dZ3QCqKLWNoLBJtQ7-hyPl2DLxLiEwKCcefmfR21FPl6fMYJIyarsTkseLDDHJrSs0yfG0R0wJ9cHrJURNP-YlpJ1p_jepWpD8JLTYbK3Du61niABqNE9BXUHUVah0ud1lU7eMC5asl72zzdAy2Pi5eJe8jxHM7DMGBOlnehBwITs2HGTdaLYoFYVtBxqJ-tf2P16vqyrnHAO_u8GLkBzij_MbAyYmg_NvGL-5DClJ8ppYEm9vgdIdqMB4W6Dhl_2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خدمت‌رسانی موکب شهدای قدمگاه در جادۀ اراک-بروجرد به زائران اربعین
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/453057" target="_blank">📅 08:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453056">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/324870d146.mp4?token=HbUCPvYTfyd2fOM47VqqogsO3IyvIj00rplktW51ElRpIVS29kom8k9DygIB_G8WzeEIbkuHx7slBMRFGj9cUMcnEJYxdxBhcad_nWYplFM5WtHTLgoUUqwEgbYqZ2GIyt01sOiP1MvYg-PNwBddsOPEQsV2k_rAWoVxfay4XGYe4bKPXezsq3bQeoepv-jqcPxa5bbwQGWS_zsjx_uZMMGTwDzIMyZvVUTJfTwnllsfMsI5Jk0iSOZr9gPY2dY4eI_sTflPeSCiELVeNRimBflGbNjZxjhgFLtJpyATdyfoY0bahO0XWVGaRYGoG36uy106daoYfdAdfxcXLFyBsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/324870d146.mp4?token=HbUCPvYTfyd2fOM47VqqogsO3IyvIj00rplktW51ElRpIVS29kom8k9DygIB_G8WzeEIbkuHx7slBMRFGj9cUMcnEJYxdxBhcad_nWYplFM5WtHTLgoUUqwEgbYqZ2GIyt01sOiP1MvYg-PNwBddsOPEQsV2k_rAWoVxfay4XGYe4bKPXezsq3bQeoepv-jqcPxa5bbwQGWS_zsjx_uZMMGTwDzIMyZvVUTJfTwnllsfMsI5Jk0iSOZr9gPY2dY4eI_sTflPeSCiELVeNRimBflGbNjZxjhgFLtJpyATdyfoY0bahO0XWVGaRYGoG36uy106daoYfdAdfxcXLFyBsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عراقی از حمله به انبار تسلیحات گروهک‌های تروریست تجزیه‌طلب در سلیمانیۀ عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/453056" target="_blank">📅 08:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453055">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8dd86309a.mp4?token=V3hgOBVKtZL4MlQTil4ohKnfWNKQb-xoCbw9xgUBGjkz5ng_8cmFxgkduYdabFppn7-UE0asBNljnvpMfKEcXcDg_Xl8WMusAUYYfM16DbGepYta_Mqr7dSLKXbLkm7H2B3AbdHQV6q19eWKqBXO-15epFrVmKzDflMehQY7QSNwd0We_Y3ldDg_kDjQD3u9tKYAep5ffjsaMoqF_87VV5-RQd7JmhSacga2VnZ0SN2LeOomirUzWV1Wj8qO3qa363diRAQEGBcXI3y7XHbzQ7IKB1yWh9QqPgid2fhILOOfRZV5rzMstjP7-f0Q2mvAXHD4Aw0EmlzSTAfiKrNc0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8dd86309a.mp4?token=V3hgOBVKtZL4MlQTil4ohKnfWNKQb-xoCbw9xgUBGjkz5ng_8cmFxgkduYdabFppn7-UE0asBNljnvpMfKEcXcDg_Xl8WMusAUYYfM16DbGepYta_Mqr7dSLKXbLkm7H2B3AbdHQV6q19eWKqBXO-15epFrVmKzDflMehQY7QSNwd0We_Y3ldDg_kDjQD3u9tKYAep5ffjsaMoqF_87VV5-RQd7JmhSacga2VnZ0SN2LeOomirUzWV1Wj8qO3qa363diRAQEGBcXI3y7XHbzQ7IKB1yWh9QqPgid2fhILOOfRZV5rzMstjP7-f0Q2mvAXHD4Aw0EmlzSTAfiKrNc0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلیل موشک‌‌باران مدرسۀ میناب اینجاست!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/453055" target="_blank">📅 07:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453054">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مدارس از مهر حضوری هستند
🔹
وزیر آموزش‌وپرورش: تلاش ما این است که تمام مدارس کشور سال تحصیلی جدید را به‌صورت حضوری و با کمترین دغدغه و مشکل آغاز کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farsna/453054" target="_blank">📅 06:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453053">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
منابع عراقی از حملۀ پهپادی به مقر تروریست‌های تجزیه‌طلب در سلیمانیه عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farsna/453053" target="_blank">📅 06:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453052">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8aa170910.mp4?token=bHEJyEcGe1rmyGdxmyMq-ngPC9_hqZpWlOxtgUOzolgteDSQcrCS8thBuYxxowgDolZojdIS0EI-8_rZgcLIGaAAG01docFg8bIgA2xdsY85gYQkcNfpA4JeGlw9kl9U1-FyhlWBR2DeYQN5kHsfekTuWsSlaw5BO67meZSErSJ-pHsArigmwN8GF8y0lximuBEo7s-3fMOd8myxBZ6Eh1K3qAmZf11vMLKETOeLmM6lL7UJ_kLGGWO1JSQcOhB0S--lwZYHrwU3KK0OWKKOL6Nn_vtmDBQo7a_GwHOg87gWfpsOnHs1FzgYhMoVuoiZoyb9cTFERgbZtm82SDe47rC89x_goKFBfHUQxgF3P56MLohPSItVDXEDgDDjoXSEwfFPURHnsAIC9bG0X9kRNrkoCS5NvSmDRtCRxCQCh-hkA4jRCyGWJhBzrZAPl5zD_wWFk0_EMPsj3fnUun95du5zQqO6pf9pcStnF47whFx5j9qqX2WHnntu2GU9fFowIfF9CGRTVn-xv-zQh7OzPjVsPPaiWgUtd62LjA5HNHCdycYxOPdztxYGnB-dnX_w6fplzvl9po_dIzpioaOORF8mV0J1-cC_tLP_MdXRtB3VdxVmKTGA0GFERCpMhk4Q5lty3JYrN7hS-yjZMJQr977fCaZzVzpG6ynqzv8cgOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8aa170910.mp4?token=bHEJyEcGe1rmyGdxmyMq-ngPC9_hqZpWlOxtgUOzolgteDSQcrCS8thBuYxxowgDolZojdIS0EI-8_rZgcLIGaAAG01docFg8bIgA2xdsY85gYQkcNfpA4JeGlw9kl9U1-FyhlWBR2DeYQN5kHsfekTuWsSlaw5BO67meZSErSJ-pHsArigmwN8GF8y0lximuBEo7s-3fMOd8myxBZ6Eh1K3qAmZf11vMLKETOeLmM6lL7UJ_kLGGWO1JSQcOhB0S--lwZYHrwU3KK0OWKKOL6Nn_vtmDBQo7a_GwHOg87gWfpsOnHs1FzgYhMoVuoiZoyb9cTFERgbZtm82SDe47rC89x_goKFBfHUQxgF3P56MLohPSItVDXEDgDDjoXSEwfFPURHnsAIC9bG0X9kRNrkoCS5NvSmDRtCRxCQCh-hkA4jRCyGWJhBzrZAPl5zD_wWFk0_EMPsj3fnUun95du5zQqO6pf9pcStnF47whFx5j9qqX2WHnntu2GU9fFowIfF9CGRTVn-xv-zQh7OzPjVsPPaiWgUtd62LjA5HNHCdycYxOPdztxYGnB-dnX_w6fplzvl9po_dIzpioaOORF8mV0J1-cC_tLP_MdXRtB3VdxVmKTGA0GFERCpMhk4Q5lty3JYrN7hS-yjZMJQr977fCaZzVzpG6ynqzv8cgOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از جنایات کودتای ۱۸ دی‌ماه ۱۴۰۴ ملک‌شهر اصفهان چه می‌دانیم؟
⤴️
گوشه‌ای از جنایات صورت گرفته در میدان شهید علیخانی اصفهان توسط تروریست‌هایی که امروز به دار مجازات آویخته شدند.
◾️
این جانیان از صحنهٔ جنایات خود و شهادت مأموران انتظامی فیلم‌برداری و برای شبکه‌های وابسته به دشمن ارسال کرده بودند.
@Farsna</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farsna/453052" target="_blank">📅 05:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453051">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">جنایت‌کاران حادثۀ تروریستی دی‌ماه ۱۴۰۴ ملک‌شهر اصفهان اعدام شدند
🔹
دقایقی پیش حکم اعدام «ابوالفضل سپاهی بادجانی» و «امیرحسین صفری حسین‌آبادی»، دوتن از عوامل جنایت فجیع میدان شهید علیخانی اصفهان در کودتای دی‌ماه ۱۴۰۴ اجرا شد.
جرم مجرمان این پرونده چه بود؟
🔹
این افراد، ماموران انتظامی را با طناب به تابلو بسته و پس از مجروح‌کردن آن‌ها با سنگ، روی آن‌ها بنزین ریخته و آتش زده‌اند.
🔹
سپس در حالی که هنوز ماموران تأمین امنیت زنده بودند، آ‌ن‌ها را روی زمین کشیده و بعد با چاقو و قمه، ضربات متعددی بر پیکر آن‌ها وارد کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/farsna/453051" target="_blank">📅 05:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453050">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎥
وضعیت تردد شبانۀ زائران در مرز چذابه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farsna/453050" target="_blank">📅 03:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453049">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxkIof2bOTSOYwQewsgroddWY_V9Jcb9XS3aZjX30H_krpuk58O5WJ6eTjcEPC88gD47lwQR8pbF99mfZkW8WFmxJKTV_txRtquuR1bgDxBmxth9tFJL4YJELceWMPwB8kfRSTHmOA4HewlKdNGd8yoL_SuIEj973gl1M5CtL-9zv_rQfPXC9VIuXTnCWMASICBvf31HR6ItekDcCRPP3tID6h1A4ZXFDc5IdEe9tuqN0IN6H7eQTrIVpdc99F7FbkW3TyaobN8l5M_Sm0qgJFUVXSK7pYjyT2t7wjWSRtgAEBgyhHn9e7YXHl3Dt8yuHwsulTu38rUTn6dETRt7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین تأسیسات پالایشی عربستان از کار افتاد
🔸
شرکت آرامکوی عربستان پس از حملات پهپادی یمن، فعالیت بزرگ‌ترین مجتمع فرآوری نفت خود در بقیق را متوقف کرد.
🔹
ساعاتی پیش یمن اعلام کرد که با پهپاد خط لولۀ انتقال نفت از شرق عربستان یعنی همان خط لو‌له‌ای نفت را بدون تنگۀ هرمز به بندر ینبع در دریای سرخ می‌رساند، هدف قرار داده است.
🔹
حالا شرکت آرامکوی تمامی فعالیت خود در این تاسیسات را متوقف و در چندین سایت تولید نفت، عملیات مشعل‌سوزی اضطراری را آغاز کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farsna/453049" target="_blank">📅 02:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453047">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0717616cf6.mp4?token=j5OYPsvSopFMUwES5q1rQmEYiDDPZmgiQGzozfWxjY-YsRZ_GYOrS4JwmHkiTUsLAoRL7iIAIwWIfraJpkxSCETMn81qenP8PVCZy1vs6T4sZPUOPyGz7-HKan9siKEImn9kl_wY11EVwVgTftbb-3k6pjHsXzVpK_p86Hk1gdBpzYAvVc2fNMcp21n0p_cHmXq8zVEN1d2UOpfBZu53Tocr_P8Ewg8IJwe67KwtxKGOcDdkn5UWiaNiAUejAj5Ty-um6Z_S643UFWdQubMonkOwmRI99woL-27QWnHi7ORLm_ixiRqUQBq43SU1pnT7a2CgLvkiB0YT6Ry4FuEofg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0717616cf6.mp4?token=j5OYPsvSopFMUwES5q1rQmEYiDDPZmgiQGzozfWxjY-YsRZ_GYOrS4JwmHkiTUsLAoRL7iIAIwWIfraJpkxSCETMn81qenP8PVCZy1vs6T4sZPUOPyGz7-HKan9siKEImn9kl_wY11EVwVgTftbb-3k6pjHsXzVpK_p86Hk1gdBpzYAvVc2fNMcp21n0p_cHmXq8zVEN1d2UOpfBZu53Tocr_P8Ewg8IJwe67KwtxKGOcDdkn5UWiaNiAUejAj5Ty-um6Z_S643UFWdQubMonkOwmRI99woL-27QWnHi7ORLm_ixiRqUQBq43SU1pnT7a2CgLvkiB0YT6Ry4FuEofg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از حمله به مواضع تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farsna/453047" target="_blank">📅 01:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453046">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65ef6bc8b.mp4?token=U4O7bzh9eaDVt9y4BuII99SVWGi13fZ_jjzU_98wTynRxM4dnUFxDBUPzFDp17Z_r2Ke1mzTL6Q9Uqf4iR0fgrA4Z4EMh4l3GYgeaukmNIT7fClL7qcGkw30RHkFxBscfrpBD5WO2c49o8ahajD89a97WM6xDGfWL7oHQppCjb8Fj_ntj-kxXWVHWAVcLhAcTL1IZjXjyN7AonU-FAmnneD8Hpn118Bmc88zQoAIMjY9fLzobsMeVC95Jcn5zieUhB6dCat8mneCmiEev91b16lp8ZboxLreQutxBiHEFI_ik7e22DlCM0s7lRz5PPkH-Kk2QmDfLkYXETCIe-XB1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65ef6bc8b.mp4?token=U4O7bzh9eaDVt9y4BuII99SVWGi13fZ_jjzU_98wTynRxM4dnUFxDBUPzFDp17Z_r2Ke1mzTL6Q9Uqf4iR0fgrA4Z4EMh4l3GYgeaukmNIT7fClL7qcGkw30RHkFxBscfrpBD5WO2c49o8ahajD89a97WM6xDGfWL7oHQppCjb8Fj_ntj-kxXWVHWAVcLhAcTL1IZjXjyN7AonU-FAmnneD8Hpn118Bmc88zQoAIMjY9fLzobsMeVC95Jcn5zieUhB6dCat8mneCmiEev91b16lp8ZboxLreQutxBiHEFI_ik7e22DlCM0s7lRz5PPkH-Kk2QmDfLkYXETCIe-XB1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائران ایرانی در مسیر پیاده‌روی اربعین از نجف تا کربلا هم تجمعات شبانه را ترک نکردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farsna/453046" target="_blank">📅 01:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453045">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گزارش‌ها از حمله به کنسولگری آمریکا در اربیل
🔹
منابع رسانه‌ای عراقی با اشاره به وقوع بیش از ۷ انفجار در حومۀ اربیل، خبر دادند که کنسولگری آمریکا در این شهر نیز هدف قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farsna/453045" target="_blank">📅 00:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453044">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
منابع عربی از حمله به مواضع تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farsna/453044" target="_blank">📅 00:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453042">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
منابع عربی از حمله به مواضع تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farsna/453042" target="_blank">📅 00:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453041">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارش‌ها از حمله به یک میدان گازی در شمال عراق
🔹
منابع محلی از حمله به میدان گازی خورمور در استان سلیمانیه واقع در منطقۀ کردستان عراق خبر دادند.
🔹
همزمان پهپادهای تهاجمی خارجی نیز در آسمان اربیل، مرکز منطقۀ کردستان عراق، به سمت اهداف خود پرواز می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farsna/453041" target="_blank">📅 00:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453039">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27662a2de4.mp4?token=cUqhRIka03w7HrY_TUO-FBAWuegfA_--uk8pSW4A23-9f5rWZBR-19GA3NhJ1UebaIuioIWTEe8t96dK1DVtI1Js5hXDGB3Ayb8xhlRl81mMTNpU2mOmbvUKiPEg_duJrCkbKKwJDsiVNa21mz03oheLrTbaUGpbvcyFIA1mNR5vHpZf5GFTAbJ3He2yBOMJPt4xeOBU9A-uxzLx3ctMfhW57BloI9JAnMoloeYw9zjtxDEMvGgHr0oK2fS2JHYQV13hopo7LULD2To6nVMvIiSRJF56a4Cc-Txtcr3Rk3gD6JP5AHdA9drCJ_SAsnym-0lFF4SueNly6n0LAPfhbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27662a2de4.mp4?token=cUqhRIka03w7HrY_TUO-FBAWuegfA_--uk8pSW4A23-9f5rWZBR-19GA3NhJ1UebaIuioIWTEe8t96dK1DVtI1Js5hXDGB3Ayb8xhlRl81mMTNpU2mOmbvUKiPEg_duJrCkbKKwJDsiVNa21mz03oheLrTbaUGpbvcyFIA1mNR5vHpZf5GFTAbJ3He2yBOMJPt4xeOBU9A-uxzLx3ctMfhW57BloI9JAnMoloeYw9zjtxDEMvGgHr0oK2fS2JHYQV13hopo7LULD2To6nVMvIiSRJF56a4Cc-Txtcr3Rk3gD6JP5AHdA9drCJ_SAsnym-0lFF4SueNly6n0LAPfhbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال و هوای عمود ۳۴۰ مشایه نجف تا کربلا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farsna/453039" target="_blank">📅 00:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453038">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf9d824db.mp4?token=UoY4QKpnJ1SRMgRmm39Hz8VztkPqoEn1tXvrST5JrHJxSq6RzzALjfTnaJ5c_0P0CAyouWr85jET2Bidl3BVm8hwidu_a74qB5jW71i67ZW4XYBB83XJH97y5J_uCKg5rm2bBq5mLCsqj-9Jw_tOwzfpuQ7UoQwlLW8DgazJTRGLSZew3-iB8gcmCkneSg5Jz3vFbgQIpVn8CQfV6XCokc7rFOfxjkjJCSrs-FVGkyRIeq9G93GPXGiLssnpon-BYE2zFaZoMbP-wDsnfKfOiagW0RbEwX1Md56U1Qp-kQMKu8YiNvTiP98HgnoYf3fC0F4V8ij45S8wp_LDlyQA7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf9d824db.mp4?token=UoY4QKpnJ1SRMgRmm39Hz8VztkPqoEn1tXvrST5JrHJxSq6RzzALjfTnaJ5c_0P0CAyouWr85jET2Bidl3BVm8hwidu_a74qB5jW71i67ZW4XYBB83XJH97y5J_uCKg5rm2bBq5mLCsqj-9Jw_tOwzfpuQ7UoQwlLW8DgazJTRGLSZew3-iB8gcmCkneSg5Jz3vFbgQIpVn8CQfV6XCokc7rFOfxjkjJCSrs-FVGkyRIeq9G93GPXGiLssnpon-BYE2zFaZoMbP-wDsnfKfOiagW0RbEwX1Md56U1Qp-kQMKu8YiNvTiP98HgnoYf3fC0F4V8ij45S8wp_LDlyQA7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرهایی از سقوط پهپاد آمریکایی در عراق
🔹
رسانه‌های عراقی تصاویری از سقوط پهپاد آمریکایی در نزدیکی سد حدیثه در استان الانبار منتشر کردند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/453038" target="_blank">📅 00:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453037">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/394406b222.mp4?token=dB-RDE7YXb6juqW1OufHAoXwem6nTTQ49VR360yIeaGKpke11k5xhzx-xChyOKDEgXAkkTK0vVxVGegz9xPac5DBAK5WPQRM-yU4WMDyOaHZb7XGFKc-uvVHcxY-lM4dSr8zfwgjyc2oN5VCD_31K5vqHyETugPHDCBkPdz6FxPQi4LeMdy6srdCiFpKnKSltTMl1IMXputFBMqSsX5eVyz4GOqoPeppgmlDGWzIt4K9tHCmlUtHl_mths8LSrUlDJ7o9SQlfGz25yuoEVKoRJdTnWlgm0CWmY4g99nviM82cwBFYlcQ-A1cQ9Fq5vUZSmOfv0bVmMiviAfhpDpJ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/394406b222.mp4?token=dB-RDE7YXb6juqW1OufHAoXwem6nTTQ49VR360yIeaGKpke11k5xhzx-xChyOKDEgXAkkTK0vVxVGegz9xPac5DBAK5WPQRM-yU4WMDyOaHZb7XGFKc-uvVHcxY-lM4dSr8zfwgjyc2oN5VCD_31K5vqHyETugPHDCBkPdz6FxPQi4LeMdy6srdCiFpKnKSltTMl1IMXputFBMqSsX5eVyz4GOqoPeppgmlDGWzIt4K9tHCmlUtHl_mths8LSrUlDJ7o9SQlfGz25yuoEVKoRJdTnWlgm0CWmY4g99nviM82cwBFYlcQ-A1cQ9Fq5vUZSmOfv0bVmMiviAfhpDpJ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افشاگری مقام عراقی دربارهٔ بازداشت گروه‌ خرابکار وابسته به اوکراین
🔹
مشاور امنیت ملی عراق: هسته‌های اطلاعاتی اوکراینی در عراق حملاتی را اجرا می‌کنند و آن را به گروه‌های مقاومت نسبت می‌دهند.
🔹
نهادهای عراقی افراد و عناصری را بازداشت کرده‌اند که در بازجویی‌ها اعتراف کرده‌اند که هسته‌های اوکراینی‌ حملاتی را علیه تاسیسات حاکمیتی عراق انجام داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/453037" target="_blank">📅 00:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453036">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1387c0f59e.mp4?token=RvMCGI20KqzAWWzJQ3kU2LBnPjhTnOcIUNZjMxLg_PiZfYIQci9NC0KdCIZr2opz4GVwQ9tUC3CG0bh5_sPTEaP71mfTdZywbpTAm3jxlnyCeIYApA9bIKZ_PnkBPTJrgdXNsCpljqaoFMZNlj7NkQ3PQqtcAyxY-rS8qab7tAZKraC8DEAz-Q6Y9mDMkPYO_ol1krTrs9EW_p0iJqzzxP_Ec98z9hwFf55gd8r9-gO1DPo1Ij6hKie9x16tymO9NB4ZCsy_PExPLwCLzSOPUyLcUoJ72eYntUjVHMAwT7Q4aS2VwwIn_-Gznu-3ECZ1kkDsFn7e5zCWwexf9Gwsxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1387c0f59e.mp4?token=RvMCGI20KqzAWWzJQ3kU2LBnPjhTnOcIUNZjMxLg_PiZfYIQci9NC0KdCIZr2opz4GVwQ9tUC3CG0bh5_sPTEaP71mfTdZywbpTAm3jxlnyCeIYApA9bIKZ_PnkBPTJrgdXNsCpljqaoFMZNlj7NkQ3PQqtcAyxY-rS8qab7tAZKraC8DEAz-Q6Y9mDMkPYO_ol1krTrs9EW_p0iJqzzxP_Ec98z9hwFf55gd8r9-gO1DPo1Ij6hKie9x16tymO9NB4ZCsy_PExPLwCLzSOPUyLcUoJ72eYntUjVHMAwT7Q4aS2VwwIn_-Gznu-3ECZ1kkDsFn7e5zCWwexf9Gwsxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد شبانهٔ زائران در مرز خسروی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/453036" target="_blank">📅 23:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453035">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3be59b32e3.mp4?token=XFMXNdKRCfWg-c42mB8KSx8cr5tA85yZQWqAYamyuEpWb7t7pJTxZ7alvt2_hRFarRqmGMTG-RlbUr5GWqDVoq_FC92CfycO0x3OJkj6zOx6M8HIZLLNYks0pa8cLtxyfor_4Q4JaomiVGKszO1sR4A7bh4EUr3HVbLubkGAdANaTqUgCIBcFG8UuSKDBczC6JLM_nRWE6iZhog-EkdhlqontqVS5Y2-of6LPcFfpzg86uhIupGvIziIlV1_QVqOXe38Wht7PJQ0vEwE727PYhthdopNeQ8h_jvUSlIQy5smXPhEwfhjuh6mPo7MXoOOzJeCpge-ZpTEmAktDtD_YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3be59b32e3.mp4?token=XFMXNdKRCfWg-c42mB8KSx8cr5tA85yZQWqAYamyuEpWb7t7pJTxZ7alvt2_hRFarRqmGMTG-RlbUr5GWqDVoq_FC92CfycO0x3OJkj6zOx6M8HIZLLNYks0pa8cLtxyfor_4Q4JaomiVGKszO1sR4A7bh4EUr3HVbLubkGAdANaTqUgCIBcFG8UuSKDBczC6JLM_nRWE6iZhog-EkdhlqontqVS5Y2-of6LPcFfpzg86uhIupGvIziIlV1_QVqOXe38Wht7PJQ0vEwE727PYhthdopNeQ8h_jvUSlIQy5smXPhEwfhjuh6mPo7MXoOOzJeCpge-ZpTEmAktDtD_YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عکس شهدای میناب در شهر امیرالمؤمنین(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/453035" target="_blank">📅 23:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453034">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86351cbbf.mp4?token=mATzoUMKDjdpSKCdg_rNTaq3Mf_nzQkf99jihiPEwfbjF1wz7GzrhTIx6k06QQBJAkAypvMD7KNdQYQPjKnbaWDBNlY8SwVp9GYh2duv4KeJpNlnAjasNREzw24yJdm_-maK3DoqJqzsbaIO0DmODmiAW74a0QyV5zSJ5UWreuKWa7WmWzeV0Ig5p0vm0ANng4YFva7dL1X5_temc0Iu1t8TSMGjMJMMwUjGN2NQi6-uC2N77BjkIRpc0LgHWxzh9bADTs0nHPAEutQUsxR0Dwu2Zh-bzDE8GArR2KUidquxmxeM2uHo8T04QJU-hbdKnksD3Y6HvIeUUlcY-TlsgStdVgvdTbJnaHRLW19Ke6uB1rRtdUD_4EHE_1kypPpBFF3n_wkbbDgnsF8RYt7aLFIG3dPqOSUpqXoDzvlx0ewc91d0H5XZ__Qaz-oG_scH6Y7God-oUi834jfF4ZqmqCGopS6bhtrcB7dTjoxyCGlu-nqoctfUfbh2b_PurLs0VlxcVO5OZK4cS7VR3WfpYhuZpfcUKnHOhByJlEnr2WXQbiZxFS5QbXl7uLCCO8CJkmy1uIJ2C1DTejVuSc-qs7m9h30hQs6yJDPjhgFpGYk8cI8gASuIhsZgxQ8X6SyC7kJ6NI9ePAJte21yl5iK9PrOjAgpiW-Zpt1swHTj91E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86351cbbf.mp4?token=mATzoUMKDjdpSKCdg_rNTaq3Mf_nzQkf99jihiPEwfbjF1wz7GzrhTIx6k06QQBJAkAypvMD7KNdQYQPjKnbaWDBNlY8SwVp9GYh2duv4KeJpNlnAjasNREzw24yJdm_-maK3DoqJqzsbaIO0DmODmiAW74a0QyV5zSJ5UWreuKWa7WmWzeV0Ig5p0vm0ANng4YFva7dL1X5_temc0Iu1t8TSMGjMJMMwUjGN2NQi6-uC2N77BjkIRpc0LgHWxzh9bADTs0nHPAEutQUsxR0Dwu2Zh-bzDE8GArR2KUidquxmxeM2uHo8T04QJU-hbdKnksD3Y6HvIeUUlcY-TlsgStdVgvdTbJnaHRLW19Ke6uB1rRtdUD_4EHE_1kypPpBFF3n_wkbbDgnsF8RYt7aLFIG3dPqOSUpqXoDzvlx0ewc91d0H5XZ__Qaz-oG_scH6Y7God-oUi834jfF4ZqmqCGopS6bhtrcB7dTjoxyCGlu-nqoctfUfbh2b_PurLs0VlxcVO5OZK4cS7VR3WfpYhuZpfcUKnHOhByJlEnr2WXQbiZxFS5QbXl7uLCCO8CJkmy1uIJ2C1DTejVuSc-qs7m9h30hQs6yJDPjhgFpGYk8cI8gASuIhsZgxQ8X6SyC7kJ6NI9ePAJte21yl5iK9PrOjAgpiW-Zpt1swHTj91E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نایب‌رئیس مجلس: نباید اجازه دهیم آمریکا هرموقع دلش خواست حمله کند و هرموقع به مشکل خورد عقب برود
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/453034" target="_blank">📅 23:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453033">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f820943e2.mp4?token=ag1pxXJLwwWBcQgRGiQDXzrDlMyLflUDiN1Q5oaZ7xqmOMutQDmagLiYU09AQeVvuri97tSKKun29lFKzcsnoTgROP8666N1whhDMe-JzZtlPtjO3NxfSVjlxeal0WGwiUPepcrhm52cgkgaWcY2BmCVqTYwYEIW5T-v0lm6Bhpbsi0Zi3Nz4PbWWe9SfZA0KSwspCzJ9vhNcaYM55iXD2k70YQ5NZeXmODberXMEc7LL8sQ1myifleZ2_4dy7FlguFt1AT4ovV5Ec3gTGiJBmkAnjaZL4eiMhvK8ecHzGLiKsPK5EB1SMtnoYb2nd0se-IOLjyWPp64EytUjgntuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f820943e2.mp4?token=ag1pxXJLwwWBcQgRGiQDXzrDlMyLflUDiN1Q5oaZ7xqmOMutQDmagLiYU09AQeVvuri97tSKKun29lFKzcsnoTgROP8666N1whhDMe-JzZtlPtjO3NxfSVjlxeal0WGwiUPepcrhm52cgkgaWcY2BmCVqTYwYEIW5T-v0lm6Bhpbsi0Zi3Nz4PbWWe9SfZA0KSwspCzJ9vhNcaYM55iXD2k70YQ5NZeXmODberXMEc7LL8sQ1myifleZ2_4dy7FlguFt1AT4ovV5Ec3gTGiJBmkAnjaZL4eiMhvK8ecHzGLiKsPK5EB1SMtnoYb2nd0se-IOLjyWPp64EytUjgntuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمایت مردم از رزمندگان اسلام و خون‌خواهی امام شهید به ۱۴۹ شب رسید
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/453033" target="_blank">📅 23:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453032">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e4ffd812c.mp4?token=lcrfid4bfgbXuvfoySyz_K3WKSfxrRVg8qsfne74SdbLDGfLs_X8Q-rMufeKwhlNNaCn3Pp5vwUNglCdMmB0li0n6RnYgI0PLRdCcRicrDoZDe4Ic7uioQLts428xmQ14RE-TXoKlrmw8wB5N1kaXPbkzTZI_gicOMtC1Y9Lgg8EMN2pAIw_zjca726d7WLCy8Hc7GkMmI1rthZ2ob_GdQQNCjenwVhOn43xzNH3uF2ZqzGGNWRgdLGfKsdNaeJR0dX7q--91Q4E5IxYbTGin3zI26Y2ollwRPieTOXHg2ZnHSmvGN7-gK3IPjVi1iNMedNMrWan1msWYKPElaUPqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e4ffd812c.mp4?token=lcrfid4bfgbXuvfoySyz_K3WKSfxrRVg8qsfne74SdbLDGfLs_X8Q-rMufeKwhlNNaCn3Pp5vwUNglCdMmB0li0n6RnYgI0PLRdCcRicrDoZDe4Ic7uioQLts428xmQ14RE-TXoKlrmw8wB5N1kaXPbkzTZI_gicOMtC1Y9Lgg8EMN2pAIw_zjca726d7WLCy8Hc7GkMmI1rthZ2ob_GdQQNCjenwVhOn43xzNH3uF2ZqzGGNWRgdLGfKsdNaeJR0dX7q--91Q4E5IxYbTGin3zI26Y2ollwRPieTOXHg2ZnHSmvGN7-gK3IPjVi1iNMedNMrWan1msWYKPElaUPqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم خون‌خواهی همچنان در میدان سلیمانی کرمان بالاست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/453032" target="_blank">📅 23:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453031">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqT41hv8pqcCXOH48yiW2pYbqqlXtZQ_bVrohJWcWRWkjkYjF5h6YydtujpJK0BOw1yTyWGg5GyDZ_T2dXtjXEakL3kkUYrt5UJpweFSRm5p051y1vNCzYrfIe3JHbu0lbfjvS-VEFzwQtFL68wy4eCgwqgBqLib3ymu7bou6Yz80ykWQHpOV1kjYimQLp1-GdWMduVCTJpOazMLfl6pF_7b4Oh6HIe0tafH99-j_nkXj3sHp5gGQsCzY_uej6r11v1e-KRhYaLvvmWe_oRip5T7D8fUGSMBx6-aTbTJGsAFWHh7Xql3PoTu-FLU2rybnMEVMWrxdVHZZwNZW9_cXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مقاومت اسلامی عراق: هر اقدام احمقانه سعودی‌ها با پاسخی قاطع روبه‌رو می‌شود
🔹
رژیم سعودی ادعا می‌کند که عراق منبع حملاتی به برخی تاسیسات نفتی آن است؛ این ادعاهای بی‌اساس، تلاشی برای توجیه ناتوانی در پاسخ دادن به حملات موثر یمن به زیرساخت‌های عمیق آنهاست.
🔹
ما در مقاومت اسلامی به رژیم سعودی هشدار روشنی می‌دهیم که هر اقدام احمقانۀ آن‌ها با پاسخی قاطع مواجه خواهد شد که آن‌ها را وادار به پشیمانی خواهد کرد.
🔹
شما امروز بیش از هر زمان دیگری به لغو محاصره ظالمانه بر مردم یمن نیاز دارید، به‌جای اینکه به این‌سو و آن‌سو اتهام بزنید تا شکست خود را توجیه کنید.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/453031" target="_blank">📅 23:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453030">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad1f2e048.mp4?token=TdeeFA2Mlj6yZv92zhxVe2I4QW5k9bAbaYZ4OVN47D96ZDubMpuohjvkHbpi5FlO4CTH-prZMSGDwXu2nhQvL_HQ4r1M_YTPh99VyHFyPcXpNttxJ-FUQk5c9dRQF4ori2d0O4_3NOzYjBfXe-FOYDi908JFQ-vH66rH-cdYHxiY6sXGKRpmeet6KKAcfTQAW261R9GSHMcvD6oNKP2Ihz4ZrRdUsLqYmMpWVSyoQj5s98ArhATwVJCuYYJlGW6L6sH_jE5W_QeYCyh-g_Pp43quluy2Sc1Dvc5q7ByZeeUzn1cM1gwd9eOo3G_ZHOPz33gvp9vyIFR8Q3mLoOcMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad1f2e048.mp4?token=TdeeFA2Mlj6yZv92zhxVe2I4QW5k9bAbaYZ4OVN47D96ZDubMpuohjvkHbpi5FlO4CTH-prZMSGDwXu2nhQvL_HQ4r1M_YTPh99VyHFyPcXpNttxJ-FUQk5c9dRQF4ori2d0O4_3NOzYjBfXe-FOYDi908JFQ-vH66rH-cdYHxiY6sXGKRpmeet6KKAcfTQAW261R9GSHMcvD6oNKP2Ihz4ZrRdUsLqYmMpWVSyoQj5s98ArhATwVJCuYYJlGW6L6sH_jE5W_QeYCyh-g_Pp43quluy2Sc1Dvc5q7ByZeeUzn1cM1gwd9eOo3G_ZHOPz33gvp9vyIFR8Q3mLoOcMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایش پایداری بروجردی‌ها در شب ۱۴۹
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/453030" target="_blank">📅 23:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453028">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
منابع عراقی از انهدام یک پهپاد آمریکایی در استان الانبار در غرب عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/453028" target="_blank">📅 23:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453027">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b065ff32e8.mp4?token=BLMWIh3pZMQ6H6qEp6dNdIAtdasuwYOvsKuUxW5A7g67LvqcQJkumTkIs-8uEhdf7wMt16x5wEdRO_5Dvjiv5cJQrKlCG6m6JPMItl8K1AdDaLtwVLFF0aZfjpPMT7eD0wjcxxcrdMSDOUR_0BOSw5vBJhbuXAslbswbm8seofuzFSGBrm3UnUtSUkSZIotdIwIXko-KfYgH8-rV_4-MXO_6kZr9MftFH9GMHHAOZpM8OjhtFJxPKn9TaXxb56UMWqzuGspiXLObfVVnvn13LqgDKnujcZYP1mr9aUOHtpLSIbXol2NbVrtPeXTKfjRG_p6RTiv0bPxjEx3vfSO7Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b065ff32e8.mp4?token=BLMWIh3pZMQ6H6qEp6dNdIAtdasuwYOvsKuUxW5A7g67LvqcQJkumTkIs-8uEhdf7wMt16x5wEdRO_5Dvjiv5cJQrKlCG6m6JPMItl8K1AdDaLtwVLFF0aZfjpPMT7eD0wjcxxcrdMSDOUR_0BOSw5vBJhbuXAslbswbm8seofuzFSGBrm3UnUtSUkSZIotdIwIXko-KfYgH8-rV_4-MXO_6kZr9MftFH9GMHHAOZpM8OjhtFJxPKn9TaXxb56UMWqzuGspiXLObfVVnvn13LqgDKnujcZYP1mr9aUOHtpLSIbXol2NbVrtPeXTKfjRG_p6RTiv0bPxjEx3vfSO7Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما چندین میلیارد دلار از ونزوئلا درآمد به‌دست می‌آوریم؛ این اتفاق دربارۀ ایران هم خواهد افتاد  @Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/453027" target="_blank">📅 23:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453026">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎥
ایستگاه ۱۴۹ تربتی‌ها در قرار شبانۀ خیابان
@Farsna
-
link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453026" target="_blank">📅 22:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453025">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cf4aed0f.mp4?token=GS-vEglauT9x1viZwUwhVI_Ac-ryPVhHVsqQzngPkEt-zZjOJkXYu0HlEEMYisn2KHYxy_YyJq20oULBjIUgb8VSMTqC6mnIeMgZQJD85qimacqDkuHk4HLpiB4eSAYTYJYKNGPwq-Rkku05jchkcUU2ZKi1pvnlRsVeCLHpP6fuTm9h8pA2p7jfst06Qr1j1b4gpAXtNR7OptdxsC3ICn9OybkSRdoZnSTzlmd6a22p6vFYZI2DYmoqFwSS1jY89IxwT9tr5XNfNZlYTSzzENVobbUMy6y0JN25TIsSdL5eD2zZfFm3FNu70ISTmHjZXpPGREY7g6_hsuCzkDTquGv-6v6q1Ek5csTAxFp18k1HEfnz59P7XFQzFdBwbv2lIxYoJofnLPTN5Tr02h8TLAsTVxCfGCz30PEyLWYWQchDfZgKb9cTo2mud3bG9dLL-LwN8giTof9-dT3Zrcl2pMcz_we1nnKpsh2Y_92xmfpGXCotd2nLU3PpBvVXIJpLRmL_Xn8nXa-ChcpkzJT2amUs91f4VUd6RLnN-_abuvvjVrWoB-D_o-3oBLtOGYqorfLQg63LIpH7uwgGTDBX-_74QdEbm9TDrny2xCMAWXi8SNNgUP4tNa5lhRKoQBcp7JUwPKItp3JQLSWsbZgHmbAvb63FDSfzLqjy3t2mRv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cf4aed0f.mp4?token=GS-vEglauT9x1viZwUwhVI_Ac-ryPVhHVsqQzngPkEt-zZjOJkXYu0HlEEMYisn2KHYxy_YyJq20oULBjIUgb8VSMTqC6mnIeMgZQJD85qimacqDkuHk4HLpiB4eSAYTYJYKNGPwq-Rkku05jchkcUU2ZKi1pvnlRsVeCLHpP6fuTm9h8pA2p7jfst06Qr1j1b4gpAXtNR7OptdxsC3ICn9OybkSRdoZnSTzlmd6a22p6vFYZI2DYmoqFwSS1jY89IxwT9tr5XNfNZlYTSzzENVobbUMy6y0JN25TIsSdL5eD2zZfFm3FNu70ISTmHjZXpPGREY7g6_hsuCzkDTquGv-6v6q1Ek5csTAxFp18k1HEfnz59P7XFQzFdBwbv2lIxYoJofnLPTN5Tr02h8TLAsTVxCfGCz30PEyLWYWQchDfZgKb9cTo2mud3bG9dLL-LwN8giTof9-dT3Zrcl2pMcz_we1nnKpsh2Y_92xmfpGXCotd2nLU3PpBvVXIJpLRmL_Xn8nXa-ChcpkzJT2amUs91f4VUd6RLnN-_abuvvjVrWoB-D_o-3oBLtOGYqorfLQg63LIpH7uwgGTDBX-_74QdEbm9TDrny2xCMAWXi8SNNgUP4tNa5lhRKoQBcp7JUwPKItp3JQLSWsbZgHmbAvb63FDSfzLqjy3t2mRv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرزند ارشد شهید سیدحسن نصرالله
:
شهادت امام خامنه‌ای مردم کشورهای عربی را بیدار کرد
🔸
در بعضی کشورهای عربی مردم می‌گفتند ما را فریب دادند، چشممان را بستند و عمداً کاری کردند که رهبر شهید را نشناسیم.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453025" target="_blank">📅 22:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453024">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a9ab4a2b5.mp4?token=na5xRncszAN9DA4vs52C9e4mx4rITP968f6r1b9nvbLYGgAcW3U3NO51ZxNBZFnx05p-WwBuJODPG6qNysN6MAHRhyA92vmI4weBRZ7rMaPTXkYKspvvKGTkX3n9asIq2UGONmRf220nBqW31AmOVkXFJVGv03i0BlmOm-BpDUoJgUrQBcgyjUjW4Db_KjpcOwlStrpKwLw9ZyjWnm34BDCm_KsCWS_oaheRS6vdFvEC6HwAbstmPGIkSwDQ4qKMRIKqy9-xiINbYXKLB903TbvSGinSGZ0nO5DKQ8qYq2B6KQX5I_R8S8-soIhHyOIq-n27QbPNDFttBARE71UTSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a9ab4a2b5.mp4?token=na5xRncszAN9DA4vs52C9e4mx4rITP968f6r1b9nvbLYGgAcW3U3NO51ZxNBZFnx05p-WwBuJODPG6qNysN6MAHRhyA92vmI4weBRZ7rMaPTXkYKspvvKGTkX3n9asIq2UGONmRf220nBqW31AmOVkXFJVGv03i0BlmOm-BpDUoJgUrQBcgyjUjW4Db_KjpcOwlStrpKwLw9ZyjWnm34BDCm_KsCWS_oaheRS6vdFvEC6HwAbstmPGIkSwDQ4qKMRIKqy9-xiINbYXKLB903TbvSGinSGZ0nO5DKQ8qYq2B6KQX5I_R8S8-soIhHyOIq-n27QbPNDFttBARE71UTSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رمی جمرات ۲ شیطان بزرگ در مسیر اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/453024" target="_blank">📅 22:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453023">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eb24ad700.mp4?token=OXX5KsYLXUp1yT1-bBqVTHCnFFfc_j_pTglzzlTL4BTLpSBHERcn9xbNIe-JYp7S4O3_nN_mXB9e-oAAEAFjccglCXAnysqXpo0m5A1TYlvVkZJZPGbG5j2jYdr2IHyOrghuhW8wIYuu4CUvFby-Zb-AAPSWTs21CIJ-OfJ6ofD4ArjR4by7RYZB0VF1ZMPIpjtuErN2jrbutRgGvqx0kJDSgEbaVZKN9j4PEKQoFSoI-5l-uW2icJd3DflzFIZfaUJQK5rthUpSgqrnWI6vtk052YG7BGr_hQfOArAjgORC3oFFnOQg2jhz02Ag2-zt-tje5OymtMuvvNd7zKVdJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eb24ad700.mp4?token=OXX5KsYLXUp1yT1-bBqVTHCnFFfc_j_pTglzzlTL4BTLpSBHERcn9xbNIe-JYp7S4O3_nN_mXB9e-oAAEAFjccglCXAnysqXpo0m5A1TYlvVkZJZPGbG5j2jYdr2IHyOrghuhW8wIYuu4CUvFby-Zb-AAPSWTs21CIJ-OfJ6ofD4ArjR4by7RYZB0VF1ZMPIpjtuErN2jrbutRgGvqx0kJDSgEbaVZKN9j4PEKQoFSoI-5l-uW2icJd3DflzFIZfaUJQK5rthUpSgqrnWI6vtk052YG7BGr_hQfOArAjgORC3oFFnOQg2jhz02Ag2-zt-tje5OymtMuvvNd7zKVdJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار شبانهٔ مردم زرند در شب ۱۴۹
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/453023" target="_blank">📅 22:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453022">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9-HbuXtkpsvjxgymZKwixr64vcfj34wz0PAOKi2Wz1sTFeaiuW102VS3XS7Hj3bQqp7DaDv4JEstMsVNTdZrxmo6UAZ4kHiv4eDssQhf7UowRClmZDDb4W8nI79XUMtBLRmvJjcDZET0OX-n2OcExFn86PA0OyycPDVL-dkeuMeKE3jM-5BTzm5RQKWCsgeRR8wq05kh5TPqZiTe192ygXraiaMy_RbfyNGdnCLvf2oGqNi8ws8bqeCkCXcjttqm7wNPUGX4veu3_U2zvTWIUEdjuWtU359AjkJFn1YbVIQ4yEmI6rfSo5rl2kVa2dPSv59j8UVAE7dqFi5CY_p2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قرارگاه خاتم: تهدیدهای آمریکا را بی‌پاسخ نمی‌گذاریم
🔹
قرارگاه مرکزی حضرت خاتم‌الانبیا : آمریکا در تداوم شرارت و ناامنی در منطقه و به‌دنبال اجرای محاصره غیرقانونی دریایی ایران، طی ۳ روز گذشته اقدام به تهدید شناورها و کشتی های تجاری و نفتکش ایران در آب‌های ساحلی و سرزمینی کشور ما نموده است.
🔹
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می‌گردد و همان‌طور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی‌گذارند و با آن برخورد خواهند نمود.
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/453022" target="_blank">📅 22:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453021">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186282342d.mp4?token=SfSEBDaE6HuyFNzvAjY6NU5Cd84-JB9lZ_vX3xaGUjlMxkgypK0g2xo86H4ZidEOkqPxmDgEVhrd9h4NUHYMRY0l-KyGXtf6-nDkuA6_qo-o0Glm9zJ57Qo93GImCtC5Vt6U0jw2Qi6-lUq4jmx5T0WMOhdu6mZW-LTnmx0MOilDXz_RyHzNTHZv52hmFdb_n6VpVJaxW6soFG8aMlH3xRTTZefSArnAjrmHatLOLKOfhBMoNOLAJ8cHvdJRSpcBu4rubsmTujhDRMM1dLACImBPZwXyNic-_L-Jcp-RIUoHMOusg1hY11eqPJ-9EBiNO1o4tPaxuEFix5-nyEONFTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186282342d.mp4?token=SfSEBDaE6HuyFNzvAjY6NU5Cd84-JB9lZ_vX3xaGUjlMxkgypK0g2xo86H4ZidEOkqPxmDgEVhrd9h4NUHYMRY0l-KyGXtf6-nDkuA6_qo-o0Glm9zJ57Qo93GImCtC5Vt6U0jw2Qi6-lUq4jmx5T0WMOhdu6mZW-LTnmx0MOilDXz_RyHzNTHZv52hmFdb_n6VpVJaxW6soFG8aMlH3xRTTZefSArnAjrmHatLOLKOfhBMoNOLAJ8cHvdJRSpcBu4rubsmTujhDRMM1dLACImBPZwXyNic-_L-Jcp-RIUoHMOusg1hY11eqPJ-9EBiNO1o4tPaxuEFix5-nyEONFTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا تهران است نه کربلا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/453021" target="_blank">📅 22:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453020">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3009ae4044.mp4?token=itStAlEUIrdvOq_ukJomkoE_8waORZR9eoWr2NE6UM_PTDUP02yG-bLngpuI36Q6OibRZW_3Fg7Occwysc8BR9w3zaO3PVACjZlydyWoCgT_2dj7CFX3sIzbL1-9wvNyLAHTnBp5uCGhV7xaTSRJc9x-oRW5GLqxNrTnWQ18Cj3jzGLG-SHoVxXg_-plvoE2Xc0mxdBylFINqGGazcMhQ0Eqdlnay3DbweH3jSzKBDI3pBOb3ELNx8INyRXqIXxc36O9hksETpN8ZmkbExOzfAMEiknanOLltSRlVM3iyAa8q7FGMZoPrLAPcumxpVEZO7uYSP4U6H0LpMsO8AL8Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3009ae4044.mp4?token=itStAlEUIrdvOq_ukJomkoE_8waORZR9eoWr2NE6UM_PTDUP02yG-bLngpuI36Q6OibRZW_3Fg7Occwysc8BR9w3zaO3PVACjZlydyWoCgT_2dj7CFX3sIzbL1-9wvNyLAHTnBp5uCGhV7xaTSRJc9x-oRW5GLqxNrTnWQ18Cj3jzGLG-SHoVxXg_-plvoE2Xc0mxdBylFINqGGazcMhQ0Eqdlnay3DbweH3jSzKBDI3pBOb3ELNx8INyRXqIXxc36O9hksETpN8ZmkbExOzfAMEiknanOLltSRlVM3iyAa8q7FGMZoPrLAPcumxpVEZO7uYSP4U6H0LpMsO8AL8Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماینده ولی‌فقیه در خوزستان برای زائران اربعین نان پخت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/453020" target="_blank">📅 22:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453013">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v_FRW_txJ2mr5ordR7uDXbnrdoF9-OkfTr_XPQwBD1MzXEaeazi2nX4Fbzvw-KWGcib6M50rL7aLzR0WX1xEU2GXw9Nq1pechYkMo5l7M57WkZlCloRijEdANm-__R9xGndwJwn_kkj5113ZSDOadKfdbChTDtRxh1Il9R4Y0GjLG0uOihpZgNfwBXrsMkXKxHsvUcsIGMKb7bBqYZtioLNdVj0NXgSwIJ5sPZxv42QYIxixJ76bY_KE8mwQ40Dhd2qTf33kbsb7crZ6d43jDdqJjaUGoMhh_tmZZdoD0m4LFE40Yn-g7WaNMYjryjgRmluSWuW53Uvfas4s7KF7lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jd5pnphMwcweqQA41RnFiEdiFrTi_udbq0bPs6aTlW7pIAghJgAU6sgbbs2BTvMXZtCpyMovACSOL38rEpSNycAKHNrMy2mTe_jiwOmuU6p67MUfEI-HN9G3ZxyoCzl2n5nr8obNjAWbN9rAU3WS3YC7m3i-zMP_10f866Z_1zuSnZICJmquEFCH4wAVDzy6Vbg81u1U5SSW_V9EbMdOPjb9q25RmlpMMdcOBkmQCDJaxNyLiGrj9LlYJfanqPebpd4wWDZc1C2cfkE-ShvH3uYR3EZS9yeXkmm1b-oVhd9xWCArDUNXSIJup_8fLoEWa8_jkJiGr99RQqAa6_JK9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Md4v4FJIPW_2tYqvzL14Ep74rRRcPXV0tHgLhrWTujDO3IvC9pYH6MVrsykM7aBjOsJCwxCYPINbPTUlcrKGrYI52CCA5lR0YvOfq2_AGgF8Sv1NfUM-Ds34Vs-KO4WJd4-Zo0ony5ZIrk2Ux8F1O-YmSK8-XJ5srIVZJSHi2eBqlb3hHE6fXmvNtML74kvBD_MQkIFJvUo8FDfahyhjU8XbEEigrriCYGolPGwK_2DUF0U9B1622p-s6KI86y4S-EIz0mSxTKAWdtaqaFwkwcDEDmN-T1CBK3dqyDAZyayE-RBtyQQ_BhIUJrMlVIoe3RKfECWX57S9v4AIg_68sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1OXDUeD2YuqBO2kPP8PXzESpKQdj-Cg3ffWXGvbX9JYUchgoL4rh4tahAajSWHLclD0KaKre7iOLGv3YCP8rZPsXMfgPQRk_lae0GmlS0jsHcNJ1PH6qqQSg42f2265ds4cpbrOy2RQSnHGySC_OhEzjXJffx-K6HhHu-sScoT2M84ndfeMjzKvAaKcaa4wOLNm6Ly58bFAJ1VRZpnUmt2nwplt136N0W0znjv370qwcXBEy6HmpmWQYLBC_LLRnrvesBArPg3OvAgwumaLn-u760hS05nKEdD4fjr-1CCpIzFACANxdjbO9AQYFk8qjgZ9jhMlDaPRzlmp61RfBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SbDrr8xQju2KZOPSoSHLHPzrNOnzMCam3dQETlZc2BxGkO0uAkqI4_I_NlhOQI7JiaiZE4VbxSWjFMhu0hWmgwgYQSfpicc8fqan_4VaeIGCkVuqGLy1WfxaDWH2CHwUfAPYELSVgrI_eHh6wMGEE1GCqshZhBMg0Ahw1RmKgAudJcttl6D4kWdLanY7yQltyVOZ3Xy7GIJpH7LXL9aHAIOxHYV8jO-ktP_R9_zd1VTtwGlIzSawNT8ggKrQAVZXlhPWHDmovFugANhjjXGertX4QNCdBOiZARzOVaEAnE2KQ11TmBlS_x2HneHO3ssWHnOx0FFkmyOBVLbxDurtog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/erWyqcXWka971_mFXHGnSDmnWJjwGfWapdvoqicMBYbRWVvpuTvBCk9ZpWIqzGeXgSOqGhELU2LoG7dR4KkA2HKGydEjWXmd2LT9I7qb65DK8lUiP-_p_UztboZERsxWZwJZEhJIr9rKuLWatIT-Fhuo0jwG_TkQAKuINx6fod-Fhg3KoOfdlUADdiBWNjHO3BHSvYkmwaAhQg-TNxyQLS8Kp_IoZ34fqpH_t8cxMpO0nERd1a9-Ssiyaw3_O2XEC5rauXnAPnPhcNlZx53EBxkA_jNQT08MtPY7FhTRE9nOooVyoWaYpHiJeTLge_zy8hSZl0_n_gMyuydwpq5Cow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KA1wmvNlfa_OJaXMndHNtNSxnyspt1QLEJSP7mZlY6QI3Y0HPSDjNzBSO9LKCtRKjyyVjBGxUKyUqW0D032RtBR2JSBc7gZdQMkS6pG4mD7VgBNVZ7fqy__Aqyy_70x2J6jQVPZ1li6GGAC2001r48Q5WoFnFcZcOSU_9eYL1xCC62DAB4C9tcPfEfn1NkCBMxqOVL8Q01Lx_bQXtoC_sBrzULHNi1BjZgESgUBLV_2pw3tiCK8woIXA1eDtgPgKOvTkfX8fW19L1EibFRUozxaahptLl22TzHxoP80LhONvoEWvfXc8NkPZEcJNiQ_UUEzFbCszrjyprHGx2gUuVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تردد شبانۀ زائران از مرز شلمچه
عکس:
فرید حمودی
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/453013" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

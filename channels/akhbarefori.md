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
<img src="https://cdn4.telesco.pe/file/oS3HjtFqTy3dSLsVhC3-wZ0nyoCK7nzk6d5KvLIaAUzgFTRETWuetsMVllhAGVkhPZ4Xmqsf_aKtDA26CpxsEVbm0m4ImNgnqlDdGOSubgyY_jtQlLU0PSoVEINeB-ss6-5lNGNcHcqe0SqGpMgKFwb9l4wvjrlqq0Po-ayclVoe2Kjnj0BVumncU1zR7VLwWe2c3QInj8IEQehpl0AmLOpD0ass51qLrQ9TG7c6ggp1fwqq_2f0tGU0o4J5A2K6jNvI7fBLj8ndpHzSH7lk_0yJg3he8VyU7jQlsTmZFhpwnA5mqvyg96hsLfTV_G00mXzgod2vfbP2CNm1g0HSQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.49M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 22:35:41</div>
<hr>

<div class="tg-post" id="msg-669280">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
رسانه عربی نایا: احتمالا حملات امشب کار کویت و بحرین است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/akhbarefori/669280" target="_blank">📅 22:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669279">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/619ccc9a61.mp4?token=J9aUR2gw0HULGPqPIoy1Rc0dsdqTtD8iXgMdPpR1qtJlTGVy42ioCbslcCYNqHMQajBx3OdTzUH4lcd1wgIygaFuQMjOzKREVGloqyI-AElck-I-h1o1tyP6qwMUJPyc6I6BruwRAy06QkQRpIgMoAzCXJeCAOzcb_PZladjG8K8QSbrq9MQLfQrGwCkXkenuxyWenR1osTamCnxg64QD6V-tK8udAeQeJi4aBLhh6a_8fFOsZzxTM2uQY75CrOXiWepouyKm5phrnpqgexvGVvVYtLFvOTW-N6bRYR_QwQxgpnOSXHrNRBBYeJ-BbwtfIKJZV5wJ5agGWcVP9al1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/619ccc9a61.mp4?token=J9aUR2gw0HULGPqPIoy1Rc0dsdqTtD8iXgMdPpR1qtJlTGVy42ioCbslcCYNqHMQajBx3OdTzUH4lcd1wgIygaFuQMjOzKREVGloqyI-AElck-I-h1o1tyP6qwMUJPyc6I6BruwRAy06QkQRpIgMoAzCXJeCAOzcb_PZladjG8K8QSbrq9MQLfQrGwCkXkenuxyWenR1osTamCnxg64QD6V-tK8udAeQeJi4aBLhh6a_8fFOsZzxTM2uQY75CrOXiWepouyKm5phrnpqgexvGVvVYtLFvOTW-N6bRYR_QwQxgpnOSXHrNRBBYeJ-BbwtfIKJZV5wJ5agGWcVP9al1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرم رضوی در ماتم
🔹
حضور مردم عزادار در حرم رضوی پس از اقامه نماز بر پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/669279" target="_blank">📅 22:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669278">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f0fb62bec.mp4?token=khWpIoQXRJBbpxqYHY7ku6tq_EoA-YpqN4u0ChGh7OdPoRS7qKBkMk6a-pyRhn19fI3LnYUUin3wJvaRvFjPM79Pt8tEmdZ7oDcPeJwH9l5cv76hiB21hw3mIr6bmv4DXNZyh3gDaQZW2IfbOUrOdCcBac9Fa9_4-Sq_nj2E06LqVsAt2wW08YbqattrDtc8kx8r-sTms9FlhVz0nMUu6ZwiwM_2pp-Nwq9JSJcAExcc2PDhXVHjyc_5BnYZvMjUsqUFFm2RJtn5H_RFL2Czgtqj0ipO0zr5wFVQ4OnRd7ncMNQq6lUHAq_Cc8CYuetw_1MyZpI_N8H2_ot-9daQBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f0fb62bec.mp4?token=khWpIoQXRJBbpxqYHY7ku6tq_EoA-YpqN4u0ChGh7OdPoRS7qKBkMk6a-pyRhn19fI3LnYUUin3wJvaRvFjPM79Pt8tEmdZ7oDcPeJwH9l5cv76hiB21hw3mIr6bmv4DXNZyh3gDaQZW2IfbOUrOdCcBac9Fa9_4-Sq_nj2E06LqVsAt2wW08YbqattrDtc8kx8r-sTms9FlhVz0nMUu6ZwiwM_2pp-Nwq9JSJcAExcc2PDhXVHjyc_5BnYZvMjUsqUFFm2RJtn5H_RFL2Czgtqj0ipO0zr5wFVQ4OnRd7ncMNQq6lUHAq_Cc8CYuetw_1MyZpI_N8H2_ot-9daQBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون رونمایی از لگوی غول‌آسای ترامپ در مراسم شام غریبان قائد امت در میدان احمدآباد مشهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/669278" target="_blank">📅 22:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669277">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
یک مقام آمریکایی به CNN گفته است که ارتش ایالات متحده در حال حاضر مشغول انجام حملات نظامی نیست./انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/669277" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669276">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ادعای آکسیوس به نقل از یک مقام آمریکایی: ما در حال حاضر هیچ ارتباطی با هیچ حمله‌ای به ایران نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/669276" target="_blank">📅 22:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669275">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
تاکنون دو انفجار در بوشهر و سه انفجار در چابهار شنیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/669275" target="_blank">📅 22:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669274">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlK04prMMYbXZHFcThXBR3Zio8PUG3E89F1lcG5-C0mY8uj7ym-bE-dGqidrsR_jPUVSufy0c5D_PJmCKlEvM6RsPXR2x6b_JWmoINxsX3uwHEjbuJBUFWwwvja1GWEmd3GDG95Vjc4PU0AkEcrUE7i_yfNOwjViBViyuwlxylNZX1UsulaBKYD-MWQyboN5ZMQbZ1vHfsfVSSWIZxaB-TiUjdkADLSCE37Ov1jAUpdtBlRld61ySj6lS8obQ_Yb5OFg40uvazAgGl7r-6XaZFokcKMfQmysJx1--wLPLKr2Z5mmm8j4tq0gBrCUhSH2TvznvcirRbfo4bcP-rt4Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
نماز لیلةالدفن آقای شهیدمان
...
⚫️
روش خواندن نماز لیلة‌الدفن به این صورت است که در رکعت اول سوره حمد و آية‌الکرسی و در رکعت دوم سوره حمد و ده مرتبه سوره قدر می‌خواند و بعد از نماز می‌گويد:
💬
«اَللّهُمَّ صَلِّ عَلی مُحَمَّدٍ وَ آلِ مُحَمَّدٍ وَ ابْعَثْ ثَوابَها إلی قَبرِ فُلانِ بنِ فُلانْ»
👈
(به جای «فلان بن فلان» اسم هر شهید و پدر ایشان گفته شود)
📝
اسامی شهدا به همراه نام پدر:
👇
🖤
حضرت آیت‌الله العظمی شهید سید علی حسینی خامنه‌ای، نام پدر: سید جواد
▪️
شهید مصباح الهدی باقری کنی، نام پدر: محمدباقر
▪️
شهید زهرا حداد عادل، نام پدر: غلامعلی
▪️
شهید سیده بشری حسینی خامنه‌ای، نام پدر: سید علی
▪️
شهید زهرا محمدی گلپایگانی، نام پدر: محمد جواد
🏴
#باید_برخاست
|
نسخه قابل چاپ
🖥
Farsi.Khamenei.ir</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/669274" target="_blank">📅 22:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669273">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-BKpZGVCsFRNwGrRsDs3qzoyOnHDzLGavZWnnKNP3af9zD52hya2fj-0GxRb6rnItx8Qi8l3TWaAeoC220_xWXWVIHkkNk5P9Z_G3Jeb2GKvLvuuG_PoMFFyFiSluxGtajYdi5s1Tx6GzZxeGpAb4AaHMZKSYrftsvkXHZ5-TsJn9UbVU3dsmseOxJW38UEMRlQUBzv_A4i7E5xCc0Q8XCr6vlaD8VlMRI0w2fVgkEhmgGEto7ba5CvaZtYf_zZbFqFsmNucH_66tNwhkRtrzSMbA9jj3AIjwzXmhAigu0sZ8Ko2mrywJYN5mkMvF-BXWk7haynUZN6bIBs7SFD7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیشترین پنالتی کسب‌شده در ۲ دوره اخیر جام جهانی
🔹
در ۲ دوره اخیر جام جهانی، ۸ پنالتی به سود آرژانتین اعلام شده و پس از آلبی‌سلسته، انگلیس با ۴ مورد در رده دوم قرار گرفته است.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/669273" target="_blank">📅 22:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669271">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
فیلم کامل اقامه نماز بر پیکر «رهبر مسلمانان جهان» حضرت آیت‌الله العظمی سیّدعلی حسینی خامنه‌ای
اعلی‌الله‌مقامه توسط آیت‌الله حاج سیّدمصطفی حسینی خامنه‌ای فرزند ارشد رهبر شهید انقلاب در حرم مطهر امام رضا علیه‌السلام.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/669271" target="_blank">📅 22:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669270">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbf3479c1a.mp4?token=lw5SAqro2l1G6WQXvyfdBQrfag_QvbncSXM_awP3fkWLgeDB3aOfDW7bc2rHoRY1jeI8bTzhbbVjwXoXLjPQMnooKOMrwAcpYxVyKX_HT-UVmM6D24LbpeLm1QAmL9SLUMQwAxET932vWVbmmb7A1D4-FV1dIqp7dlAFybyVeBdOemxGnMHwrV7yPORBoo7vQGBdMtSYkD_VqlEo46hUK13OSuWTY4j2zEbDRhnRmJX9EFnLqU9FuUgywnXZScCrXPmR1MjEFRz2a5W8jcnotvUj9mCLBTlfd4469RXt-8GbYrYK-V2rIf6GEdzzrnhGHtDre38_MigMNCYrKSq1OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbf3479c1a.mp4?token=lw5SAqro2l1G6WQXvyfdBQrfag_QvbncSXM_awP3fkWLgeDB3aOfDW7bc2rHoRY1jeI8bTzhbbVjwXoXLjPQMnooKOMrwAcpYxVyKX_HT-UVmM6D24LbpeLm1QAmL9SLUMQwAxET932vWVbmmb7A1D4-FV1dIqp7dlAFybyVeBdOemxGnMHwrV7yPORBoo7vQGBdMtSYkD_VqlEo46hUK13OSuWTY4j2zEbDRhnRmJX9EFnLqU9FuUgywnXZScCrXPmR1MjEFRz2a5W8jcnotvUj9mCLBTlfd4469RXt-8GbYrYK-V2rIf6GEdzzrnhGHtDre38_MigMNCYrKSq1OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع پیکر امام شهید بر دستان عزاداران پس از اقامه نماز بر پیکر ایشان در حرم مطهر امام رضا
(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/669270" target="_blank">📅 22:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669269">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uisf6GmOfYodrSjX4iF3FF-NkbIyAwuxpuTZ4Ejf3q1S5yFBwqcc6eFlVEVnY7-WP0nrUU-1iYZ0WsF1n1q3kw_PDwFuqOcCBIKNbXeJ4JoLM68CcP5cQL-gsr9wJ55bG4ykDpEpg6iPl0rNHpPSPbhOghxRF38YDW3-F9y2KOXQHJeMQzpzV8QGEdmvV-xVMaEyrm-a35hR3WgLsEjzYtgNB3tKQjK0isjnQnOguFNgZOUWJTCJkQoBFC2u3PxyfTnpdsLq9CDDIQevha23ZEfneNw52DYw1Oqr1wk8AiN3dKAzKd8g5T9nDxUkZYiH4s7bEhAq-QpnzMteswE06g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هدف تنظیم بازار و سهولت دسترسی زائران و مجاوران انجام شد؛ آغاز عرضه مستقیم محصولات در ۱۲ جایگاه ویژه میوه و تره‌بار سطح شهر مشهد
🔹
هم‌زمان با ایام حضور گسترده عزاداران در پایتخت معنوی ایران، سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی شهرداری مشهد با هدف کنترل قیمت‌ها و حذف واسطه‌ها، طرح عرضه مستقیم میوه و تره‌بار را در ۱۲ جایگاه منتخب سطح شهر آغاز کرد.
🔹
به گزارش روابط عمومی سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی شهرداری مشهد، با اشاره به نقش این جایگاه‌ها در تعادل‌بخشی به بازار اظهار داشت: «به‌منظور حمایت از سبد مصرفی خانوار و رفاه حال زائران عزیز در ایام تشییع پیکر مطهر رهبر شهید انقلاب، ۱۲ جایگاه عرضه مستقیم میوه و تره‌بار در نقاط پرتردد و کلیدی شهر مستقر شده‌اند. در این مراکز، محصولات به‌صورت مستقیم و با حذف واسطه‌های غیرضروری عرضه می‌شوند تا ضمن تضمین کیفیت، قیمت نهایی برای مصرف‌کنندگان به‌طور محسوسی کاهش یابد.»
🔹
وی در ادامه با تأکید بر نظارت مستمر بر این ایستگاه‌ها افزود: «این طرح با هدف تنظیم بازار و تسهیل در دسترسی شهروندان به اقلام ضروری طراحی شده است. کارشناسان نظارتی سازمان به‌صورت تمام‌وقت بر روند قیمت‌گذاری و کیفیت محصولات عرضه شده در این جایگاه‌ها نظارت دارند تا اقلام با بهترین شرایط در اختیار عموم قرار گیرد.»
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/669269" target="_blank">📅 22:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669268">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهایی در بندرعباس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/669268" target="_blank">📅 22:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669267">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fa20e8a52.mp4?token=i2HCsrwjTWIteDsPWj66n2QbhcyaoqjS8KODBu7ud4zu4HaG_CjL9xsVWx2DAdgbmTz4z-7Pt4HG0-dYoatqpK6BmfN3VQ2j_NODHVInJYeNhf-hEYmCOOcsU5u5qHKJ2GDXv4YJn1GBJobh89ROhJEeEVjM9AD_cGyDEQ6O2Zh2HL3l9iFOjtPcVWK0wAh3oavd5GhIddlT-OWlTmF8GrBnnclsv7YkfOhR_7FpbLLwLO4rIpRbmpacU6ZcW4lyi1_s1TOcE4cP64PMjQ-hvK1xtW9s-q_dZvVNAdCERvyrDVQr0MgtrZtHjeGR69lf2pQf8zcbBq-i74ZLwrBkiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fa20e8a52.mp4?token=i2HCsrwjTWIteDsPWj66n2QbhcyaoqjS8KODBu7ud4zu4HaG_CjL9xsVWx2DAdgbmTz4z-7Pt4HG0-dYoatqpK6BmfN3VQ2j_NODHVInJYeNhf-hEYmCOOcsU5u5qHKJ2GDXv4YJn1GBJobh89ROhJEeEVjM9AD_cGyDEQ6O2Zh2HL3l9iFOjtPcVWK0wAh3oavd5GhIddlT-OWlTmF8GrBnnclsv7YkfOhR_7FpbLLwLO4rIpRbmpacU6ZcW4lyi1_s1TOcE4cP64PMjQ-hvK1xtW9s-q_dZvVNAdCERvyrDVQr0MgtrZtHjeGR69lf2pQf8zcbBq-i74ZLwrBkiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ آغاز اقامه نماز بر پیکر «آقای شهید ایران» و مرجع عالیقدر شیعیان جهان حضرت آیت‌الله العظمی سیّدعلی حسینی خامنه‌ای توسط آیت‌الله حاج سیدمصطفی حسینی خامنه‌ای در حرم مطهر امام رضا علیه‌السلام #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/669267" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669266">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjVAP2j9_tRr8wgjSaWJMWVBCNdGtxSwzS0ms3T8QVQRyJF6VUxZtCPX9n-GhMNH9LLqbio64LZwpRzmTxNA7blbAaW-D_E2A0YEDpfD_EESx0klZ2Oe-6lq7fcZHSUxnhgK4FE-OC4_Ttt_Ls8IbFC5jkKTMxJsfRZFOHAYT0ot6aQdiGLM2Hw2QsxoKJSDbQoPvZXYSd35WK218szzw7y7WkqKUbuxb2oGsdLCHmMN9tWQd3PuL3lglt0Dq8tIm0HXyvnl3Wtu0Xb00Hzg0gk_Kju6Hd_JlODxscbIIklB8VyIQcNYVTg62s5-_IcE1_ysXSyaSKE4WeK_fzgvDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاده‌ها سالانه جان چند نفر را می‌گیرند؟
🔸
طبق آمار سال ۲۰۲۳، سالانه حدود ۱.۳ میلیون نفر در جهان بر اثر تصادفات جاده‌ای جان می‌بازند؛ رقمی که بیش از ۲ درصد از کل مرگ‌ومیرها را شامل می‌شود.
🔸
در حال حاضر بیشترین سهم قربانیان مربوط به سرنشینان و رانندگان خودروها است.
🔸
در طول سال‌های گذشته، سهم موتورسواران و سرنشینان وسایل نقلیه افزایش یافته، در حالی که سهم عابران پیاده کاهش پیدا کرده است.
@amarfact</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/669266" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669265">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
تاکنون انفجاری در خارگ رخ نداده است
🔹
خبرهای منتشر شده در مورد صدای انفجار در خارگ صحت ندارد./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/669265" target="_blank">📅 21:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669264">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6QA0UCf6RwQnLNkeAhv8fQvLxs5DMp33oeNhdbz6stGqjUOLrUVjCbfrkkJVvWzgl9HVA-Kl2QSCyHAAHvihbWyPINo80RN43DECu3hL9UzTa3tfm5Y08mVWjR0POlU_023CzbgOjKgv2kwo6Nya3AUPtb_Z80sBjZZQ_YVlytmrkchLSXHrcn-dqhVkc50ZZYpIXyUt9NYc2JedNryOyogJcHTHJFdBFh9oJbPV7yuS9I6n3fdEVwH7sfI2Axe_ggr3tSPFNnSFLbelNTEbhZ2RQGG6Ac7UQ4ev_jvurYCvnSFxGY1P4j2syZerUDqKO_gfWXnX0pQC5g4cZv8Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعالیت هواگردهای امریکا در جنوب ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/669264" target="_blank">📅 21:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669263">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏
♦️
گزارش‌های تایید نشده از وقوع انفجار در اهواز و بوشهر/صابرین نیوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/669263" target="_blank">📅 21:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669262">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a88205b172.mp4?token=P1MT3QshH-hBqJFeRDe6Ug61L4-Oi-0tSeBQRseepfPTlyRUrM8oZ5VpFSbTMv-iBApMSDVMtSLi2owiX9bZ0LXaVssIrLFFvIVkl4R37Gr-EbbGiGzfjqzevr71UkV61NAcAostHQ9mPnb_Zqj9LsB3MwcfvoQasGzjB48kVVE4WL4HF4-nEVOpQnUlUgTyLzgGDU2K30ju85deGEqtNkJeBeM54SACJp6ABLcAwox2J7-kF5BT_5vwOrCoyNTcU7BZkWhjgIHM-JJ1DuEy4FYJiDxvZf54mvLGCdEzk65tjL7fXBuxgzgPjh60qfc6AJ1BHkwKJfS_HsAVWXlxOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a88205b172.mp4?token=P1MT3QshH-hBqJFeRDe6Ug61L4-Oi-0tSeBQRseepfPTlyRUrM8oZ5VpFSbTMv-iBApMSDVMtSLi2owiX9bZ0LXaVssIrLFFvIVkl4R37Gr-EbbGiGzfjqzevr71UkV61NAcAostHQ9mPnb_Zqj9LsB3MwcfvoQasGzjB48kVVE4WL4HF4-nEVOpQnUlUgTyLzgGDU2K30ju85deGEqtNkJeBeM54SACJp6ABLcAwox2J7-kF5BT_5vwOrCoyNTcU7BZkWhjgIHM-JJ1DuEy4FYJiDxvZf54mvLGCdEzk65tjL7fXBuxgzgPjh60qfc6AJ1BHkwKJfS_HsAVWXlxOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ آغاز اقامه نماز بر پیکر «آقای شهید ایران» و مرجع عالیقدر شیعیان جهان حضرت آیت‌الله العظمی سیّدعلی حسینی خامنه‌ای توسط آیت‌الله حاج سیدمصطفی حسینی خامنه‌ای در حرم مطهر امام رضا علیه‌السلام
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/669262" target="_blank">📅 21:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669261">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFBiyPHHszBmn0yZ3FK9cLhgsWmrjbIbtagqdzBS-Smctm97mSKgQH1vsRFTjY81rmTwRlyjHZN6pn8rIyNsLGVZsHkd5dMJtGzOQ3Gpgb_-jdcZoHnI6uMVFkx4NrFoiegoPmBaaeEfLDRVsnXEYuXhZI3n77M11ErGgoakaNuzVnFD-nsY0xjQbqvOapH57tnLET1yZIDEhwsM5H_VQibwGEyY81g1RrQnWQP-4QHP6uqYKMQKVDemSap1vf3HR7II06bpzuauZjtBcLH1WRGk02MD5MU5vcN3QAcfKh1Y25bYtK3ytnlr5nuoD4nu9v_aZFMLMToVcPUA57JqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از فرزند ارشد رهبر شهید انقلاب در حرم رضوی #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/669261" target="_blank">📅 21:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669260">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7LE_GaIbPgYpnQBK1dAhUk3K_oePaSb8vc2-9TBAyHZN1B7gzTTGiR4sj1DQruE2_URXBXXYWj8TIGWypGwIZ1fj0ep9SL_WfbQU4a5EgsoY9M95TlQw2okBzBrHH1D1YzG8pHmBlB92XoBSVetnKlXKUZjq72Ly6k6zgj-vxEXI4CJJZKVvIMQWXFIViRX306M4HaHwoqfoqF5gRPyelBNaVUClptkFYaGPr7Ef6qb8X1KE5sn29wwE9UB5oXi0J0-3rzZEqdwYmwsdf7PcC4PrbrJMLBf_0nBZEEl-TrfYpVXA13y6gA4u3i-tUn9hrBltqoxMrTmWMIogvusmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه حملات متقابل آمریکا و ایران در دو روز گذشته
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/669260" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669259">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
شنیده شدن سه انفجار در کنارک
🔹
دقایق قبل سه انفجار  در کنارک شنیده شد.
🔹
از جزئیات و میزان خسارات احتمالی هنوز اطلاعاتی در دست نیست. /مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669259" target="_blank">📅 21:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669258">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏
♦️
گزارش‌های تایید نشده از وقوع انفجار در اهواز و بوشهر
/صابرین نیوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/669258" target="_blank">📅 21:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669257">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naSYNeKYn8jis0zDjCHdP563Vgh23PuNb8SucKbd-LXtN0eHb2k8TnhdcINvp2mwCU5Z1RmQLTcpEdwyVRxJ608t6vmEQ3vylNPVZhFGCl8lt8bySXsL-L43P-tfZVKDjWPut3RZvfpuSa1rcNtTxBLOeYJGpN5kSMwXpTpbLM1QhufOZRQ1lJO-9UBYtW7OTy8xJ8bmo_dBom8I2BJetWbp0o6HsAV7F2Hm8ormvk5c2kRjBBqyepT0zevNuUuSj9a7yY5eubztp128X0Mg9-rSksvsVYqF59RtWz6Q6jZjBoNQPweO-yJllRZ-lQC45I2k-3AOPXuhk-nvR3o9hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری مصطفی راغب خواننده درباره تشییع امروز رهبر آزادگان جهان در مشهد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/669257" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669256">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4473819833.mp4?token=CpiV-zzfTt-yEsl9uON-VKAxGGEJhnK3zCOYge4-eX92L_oXPSr5rfCQ2GlI2s826umArJFdhmAitZjWlSlGZRFSv-jnrvrqgCYbyfymJ8KWaCT9RnkkbGSffplVjYNaLxwvqfs98g5SKYICCk8fMpfyh0pSrslgA2h7RiBaqQjWyye2b_a2GgBk54uBWYMVvC4ttv8FtAGlXKuToJ0gjdvh0YnjH2uaTEQNuJzXa9CzaiNsrnJIk-DG6BC5cQaX0DKCpd_dsM1VLWuG_KQI5WtP5GKFR9Co8IrxwmkB_w5oZPdBI9GSrc299fNNBML5wwgiFiYKheIIOLmODpefoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4473819833.mp4?token=CpiV-zzfTt-yEsl9uON-VKAxGGEJhnK3zCOYge4-eX92L_oXPSr5rfCQ2GlI2s826umArJFdhmAitZjWlSlGZRFSv-jnrvrqgCYbyfymJ8KWaCT9RnkkbGSffplVjYNaLxwvqfs98g5SKYICCk8fMpfyh0pSrslgA2h7RiBaqQjWyye2b_a2GgBk54uBWYMVvC4ttv8FtAGlXKuToJ0gjdvh0YnjH2uaTEQNuJzXa9CzaiNsrnJIk-DG6BC5cQaX0DKCpd_dsM1VLWuG_KQI5WtP5GKFR9Co8IrxwmkB_w5oZPdBI9GSrc299fNNBML5wwgiFiYKheIIOLmODpefoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری از فرزند ارشد رهبر شهید انقلاب در حرم رضوی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/669256" target="_blank">📅 21:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669255">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
پیکر‌ امام شهید تا لحظاتی دیگر وارد صحن پیامبر اعظم میشود
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/669255" target="_blank">📅 21:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669254">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی فیلیمو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59fd2cb492.mp4?token=bkwhh9Ly8N1qUiQf0HYg1ByB6SewB1SQkCU445ihXSK_QdPzFNdIeNwceBflVZ-Ag7a1mCipUFLaqGjg9xQuzq31Pd1pEQG2vaJFzeoDqW5CpLbnvveOxvWRMqHssmspbgxOG98boIBvNvO0hwpBeoOhgIiqHiDMr-NoZxk3v0CgwP5xtiQ-kFWf25x6JuNsmkpD3qQYWqcuu_J0iPJ64F9ptT3xOakzQbsx1_rZ-xJIailhOeV7aXlN3YvP3xlbFPn5GR_KY_5P9AwQZ9n_7oBgjr0c3VljDbsvXERatuI4_U97f52v5zQi9jTjKdlQWe08QGXM6d0BFOu6MNpe5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59fd2cb492.mp4?token=bkwhh9Ly8N1qUiQf0HYg1ByB6SewB1SQkCU445ihXSK_QdPzFNdIeNwceBflVZ-Ag7a1mCipUFLaqGjg9xQuzq31Pd1pEQG2vaJFzeoDqW5CpLbnvveOxvWRMqHssmspbgxOG98boIBvNvO0hwpBeoOhgIiqHiDMr-NoZxk3v0CgwP5xtiQ-kFWf25x6JuNsmkpD3qQYWqcuu_J0iPJ64F9ptT3xOakzQbsx1_rZ-xJIailhOeV7aXlN3YvP3xlbFPn5GR_KY_5P9AwQZ9n_7oBgjr0c3VljDbsvXERatuI4_U97f52v5zQi9jTjKdlQWe08QGXM6d0BFOu6MNpe5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من بهت قول ميدم دخترت به‌زودی بیوه بشه!
قسمت چهاردهم سریال
#بدنام
“آغاز جدال” فردا ساعت ۸ صبح، به‌صورت اختصاصی در فیلیمو
بدنام، جمعه‌ها به‌صورت اختصاصی در
#فیلیمو
کارگردان: احسان سجادی حسینی
@filimo</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/669254" target="_blank">📅 21:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669253">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFphaU1YUtBGcI4rpOTLoSNfJSmW_SaRnNaWHog4GnSU8mmNw0Hd30ONYuh_Bsx-euqPNUJr-2rBrNygYdsJGYhoWWtroDEGfTUi0x0Lw_aiR5tnahX_OVyXV68JK4Khfp8oXpLxg49w2CPHHGCInDkvF1ODlfd6pxQ5tbbYnHBmhND9nLHvkBt_Y5les1NFXa0-MDvPmysuKWElmZBfqvVErrafblO5myGpZs8C24v4UHFR_e7v_tmTmsZI_DxdITRQ0nG7mBEQuMZqXDojkpQit7X_0z_nEtRjYOFMUiDey1IdanhcXQ9vePC1RyaSPD2OyS2nm0goJZQ2ZaKM4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر عراقی: صدام کجاست؟ شاه کجاست؟ رهبران پیشین آمریکا کجا هستند؟
🔹
آنهایی که تلاش کردند میان ایران و عراق بذر تفرقه و دشمنی بکارند، اکنون کجا هستند؟
🔹
این مراسم تشییع سیدعلی حسینی خامنه‌ای در عراق، که پاسخ همه این پرسش‌هاست.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/669253" target="_blank">📅 21:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669252">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b969b303cf.mp4?token=Sl0Lt_Ibt0efkKFqHii-K2bdU5jxFeR8Z8SRUJkT2I_K17HqqSmltGyK_NNYZAqDautny9aRURHsEpLIRiIEcltGatYgtWfEu3orMgKqabC8JDP7hjzLIMe6WlVTOa_mlIXitxoFdKukm2OnS9nFPnic5Yv-N7NRk8j3JiUX9-rJYNKqJU-NfKPDZtmGel1y5pmPeNecldB1qJjJiCjaU70f3ZiBkMVshSzHmtAR-P896gefScTG7VH7HBVfNphdgkDbnR02uBJITEAuc7nP3fN-3UQCfl8PHaYKLMSyFhs4PK3Hdbg49-_gtO9vbxVc53X7rLPzd94-dtNCDje3t7MOF_-fzQWQke2JmMXiGsGn80N_pxCsYbtkwE7cqvBQ1kQ2tx7qiICEIR4vnx2Sya6KIscRYfkyQYPPxCkV982y6WignYJgtVXb-ou58uyZlumHbmafnTWmxVRMgZUv_7I6s5EpUF2NST_uy88LTpoI88iKVlFKDXq5F8NzKN1DHQXDF7iHlEecNRS_7ez68gC04V65s92bUqd835d8ps5SySYRUyQXuB3Pd5C7XRSbjz8GKb65XpGvODSlHkjdnTvt0GkJCOluepBYzvoFQeMk0up2j83cq2aebYaIimPkYU4xXcgIzIaQ69Lo5UdFSZSIAGnJKtfk7JHcf4dYV0k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b969b303cf.mp4?token=Sl0Lt_Ibt0efkKFqHii-K2bdU5jxFeR8Z8SRUJkT2I_K17HqqSmltGyK_NNYZAqDautny9aRURHsEpLIRiIEcltGatYgtWfEu3orMgKqabC8JDP7hjzLIMe6WlVTOa_mlIXitxoFdKukm2OnS9nFPnic5Yv-N7NRk8j3JiUX9-rJYNKqJU-NfKPDZtmGel1y5pmPeNecldB1qJjJiCjaU70f3ZiBkMVshSzHmtAR-P896gefScTG7VH7HBVfNphdgkDbnR02uBJITEAuc7nP3fN-3UQCfl8PHaYKLMSyFhs4PK3Hdbg49-_gtO9vbxVc53X7rLPzd94-dtNCDje3t7MOF_-fzQWQke2JmMXiGsGn80N_pxCsYbtkwE7cqvBQ1kQ2tx7qiICEIR4vnx2Sya6KIscRYfkyQYPPxCkV982y6WignYJgtVXb-ou58uyZlumHbmafnTWmxVRMgZUv_7I6s5EpUF2NST_uy88LTpoI88iKVlFKDXq5F8NzKN1DHQXDF7iHlEecNRS_7ez68gC04V65s92bUqd835d8ps5SySYRUyQXuB3Pd5C7XRSbjz8GKb65XpGvODSlHkjdnTvt0GkJCOluepBYzvoFQeMk0up2j83cq2aebYaIimPkYU4xXcgIzIaQ69Lo5UdFSZSIAGnJKtfk7JHcf4dYV0k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازتاب تشییع تاریخی پیکر ابر مرد شهید تاریخ در قاب رسانه‌های جهان
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/669252" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669251">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b52e080a43.mp4?token=KYlFwnHEPbFzH_BRbd8d6m-bdHWlghj2p67NJj0WW_L3yhHcZrhOfbw6dnKkVm_ujoXf7gl54nHqUzZVsd9iS27Tv5GMKw-igsb3248LbRjxmyQC7hnXR-7c03gB9hMdP65LHK2A78I0Q8KOVgzA5YTgT1rKVEXSrMWd-7ZDanJ7beUL-9kDBVWZeXMRz_9aqszHH6ds7ZvMqQWFlI5XeLZX_zs17kqCWYPEOkmx-PnMyfutLzhtrIW6MjET_NFeIbmVcBSQBxtB7uSZw-3rJztA0jXdUpJzBWAlRv9RpQEqZQfnCmf4fZj00huGpEmgbkC1YqOecBRajXgscGqDaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b52e080a43.mp4?token=KYlFwnHEPbFzH_BRbd8d6m-bdHWlghj2p67NJj0WW_L3yhHcZrhOfbw6dnKkVm_ujoXf7gl54nHqUzZVsd9iS27Tv5GMKw-igsb3248LbRjxmyQC7hnXR-7c03gB9hMdP65LHK2A78I0Q8KOVgzA5YTgT1rKVEXSrMWd-7ZDanJ7beUL-9kDBVWZeXMRz_9aqszHH6ds7ZvMqQWFlI5XeLZX_zs17kqCWYPEOkmx-PnMyfutLzhtrIW6MjET_NFeIbmVcBSQBxtB7uSZw-3rJztA0jXdUpJzBWAlRv9RpQEqZQfnCmf4fZj00huGpEmgbkC1YqOecBRajXgscGqDaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از
غزه، مهد رنج‌ها، درود بر شما، درود بر امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/669251" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669250">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر امور خارجه ترکیه: آتش‌بس میان ایران و آمریکا پایان نیافته است
🔹
نخست‌وزیر بلژیک: جنگ علیه ایران باید متوقف شود.
🔹
یک مقام آمریکایی: طرح ایجاد مناطق آزمایشی در جنوب لبنان ظرف چند روز آینده اجرایی خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/669250" target="_blank">📅 21:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669249">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkGpNRfiK2wK9y2L0V9qq5Rkk8w02zovJaLI6j2MSH55q-rdw4BpydEbmuzzjvAJ790sa38Xqg998W9iTXB_WFZRC8VvE2bK60M1AGM8FXLQiv2hcyYrpC1wGxf4mR1Z27uOx21H8aDhayTvwYV-O6rrop6vWESPDZJKkR-rl9AQnbEIs0NmQ1si7Z4cqYjvlZS2gl_3oRcwxhuy_NsyvITU1wmDNY7c3mjZfsv_sQWLI7_PujycC3UU9RohDx7_9LBVFbhY0tlMYYLFdYW8EhaQUbuiOlkusU-Q9IZxxVCL29FY3wiaVR4H6Sq7yfKtwsiABIJQrqsQsQzJv-rgrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهر، سیاهپوش هم‌گام با حماسه؛
نمایشگرهای شهری مشهد، تریبون زنده مراسم «رهبر شهید»
🔹
هم‌زمان با اعلام برنامه‌های ستاد تشییع و وداع با قائد امت اسلامی، رهبر شهید، آیت‌الله‌العظمی سید علی الحسینی خامنه‌ای، سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی شهرداری مشهد در اقدامی هماهنگ، بخشی از فضای تبلیغات شهری این کلان‌شهر را به پوشش تصویری این رویداد تاریخی اختصاص داد.
🔹
به گزارش روابط عمومی سازمان ساماندهی مشاغل شهری و فرآرورده‌های کشاورزی: «با توجه به برگزاری مراسم‌های برنامه‌ریزی‌شده در بازه زمانی ۱۳ تا ۱۸ تیرماه در سراسر کشور، مدیریت شهری مشهد برای همراهی با آحاد ملت و بازتاب باشکوه این رویداد، پوشش زنده شبکه خبر و پخش تیزرهای هویت بصری را در دستور کار خود قرار داده است.»
🔹
اخذ مجوزهای لازم برای این اکران گسترده از طریق مدیریت محترم افتاء خراسان رضوی در حال انجام است؛ «هدف ما این است که شهروندان در نقاط مختلف شهر، پیوند معنوی خود را با این حماسه حفظ کنند. به همین منظور هشت نقطه استراتژیک در سطح شهر برای استقرار نمایشگرها انتخاب شده است که در این مکان‌ها شاهد اکران پخش زنده شبکه خبر و تیزرهای هویت بصری خواهیم بود: میدان شریعتی (نمایشگر منصوب بر بدنه سینما آفریقا)، بولوار وکیل‌آباد (نمایشگر مستقر در حاشیه بولوار، داخل پارکینگ آزادی)، پارک ملت (نمایشگر مستقر در تقاطع امامت)، بولوار هاشمیه (نمایشگر مستقر در تقاطع صارمی)، منطقه طبرسی (نمایشگر مستقر در چهارراه شهید گمنام)، میدان فلسطین (نمایشگر مستقر در ابتدای احمدآباد)، بولوار سجاد (نمایشگرهای مستقر بر بدنه ملک خصوصی در تقاطع‌های بهار ضلع شمال‌غربی و بزرگمهر ضلع جنوب‌غربی).»
🔹
تمامی زیرساخت‌های لازم برای پوشش منسجم و باکیفیت این رویداد در نقاط مذکور فراهم شده است، این اقدام بتواند فضای شهری مشهد را بیش از پیش با حال‌وهوای این رویداد عظیم ملی هم‌سو کرده و امکان مشارکت بصری شهروندان را در مراسم‌های سراسر کشور فراهم آورد. شایان ذکر است این پوشش تصویری تا پایان برنامه‌های اعلامی ستاد تشییع و وداع ادامه خواهد داشت.
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/669249" target="_blank">📅 21:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669248">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4047b339da.mp4?token=aNZKGrQfpz2IXh63mG0JiL-mrgAxBxMI-u5fyxNMgVPJpxUSljMqUVWdOF1PpU9cY27CHJ8g8g7QcZxQwA5zP3TMTaUa6OD3iNf5EU9FuHsgVW77unB-CSZ4icsnUsVIxc_AVnaOYXjIaqiqJJ8ev46CbBYvwTnwYdy4gxnCYLdKlDLlH6XsPV0qBl_XZNQaWuo_BIbXEyFNO-WKeP15jzm9z_gwY9wAwPM6iduiLP2zec6xwOjuFfR-MVFGkfK18i4UFTcTySuOxwHYffOfbYv1nF5DbmJ_w_4r4IjK4xHU8a_LHRMdalctCbblR6W4-v-o1THHVy6cAGfV0ZFvUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4047b339da.mp4?token=aNZKGrQfpz2IXh63mG0JiL-mrgAxBxMI-u5fyxNMgVPJpxUSljMqUVWdOF1PpU9cY27CHJ8g8g7QcZxQwA5zP3TMTaUa6OD3iNf5EU9FuHsgVW77unB-CSZ4icsnUsVIxc_AVnaOYXjIaqiqJJ8ev46CbBYvwTnwYdy4gxnCYLdKlDLlH6XsPV0qBl_XZNQaWuo_BIbXEyFNO-WKeP15jzm9z_gwY9wAwPM6iduiLP2zec6xwOjuFfR-MVFGkfK18i4UFTcTySuOxwHYffOfbYv1nF5DbmJ_w_4r4IjK4xHU8a_LHRMdalctCbblR6W4-v-o1THHVy6cAGfV0ZFvUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور قالیباف، سیدحسن خمینی و اژه‌ای در حرم مطهر رضوی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669248" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669247">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7qN-yuvSbMJWWjt2Msya9YfrL6qN_ErEt1cQ5eTSNyW7WEdvG2ntkHXimZf4CiWZiAChpvNe-kCBCo5lUV5W242ZoLCMveYXLJreCpFUNSLGevnOUsY7833zrXCHvXH9u9flMZcW5lw23_p7pqGrUaaswyokC9G5PvDMjpg6C4KiVp2oOajxqVtWUkaGp1ZknogvojOFxaGU-tSOMdH7NUNXUSSno1KEdrly42QkDsSJ2z06OZRK0JVlIWY4W_zY3eVU6MVNiW_BsnimawYybDHWU5RhWffs4m-O0YIIURD3t72eSPVPTYz-yGrQ9_5VKE7MZtp1WfGuTBp5saRYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیت رهبری
💔</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669247" target="_blank">📅 21:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669246">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515aa7f7b7.mp4?token=Ix2bIdQKpIUZcnUdCaYfRgnDwlmqP_eP2VlJGLpSwuzOSwTa87Ebae1HK8HH5V5dDcnEYgHghbGMVGYWd_8Fqn7NmNiHeiOOGU5vJMY-CAgk18_C6Zx9DVoYEbbTQypK7VhQu7Y7aHyVePs3TfuUipFMzO9fP9kWydgDGxFhRx-vaKWlwU8UDMxsMj5vQ-mVoudn-FSqiI3Q2oavekdT8rWFCfooD7z9ZKHQZcr93_WEIHbCEPKIJLZZmfMeQpKlOK1Qh7ME7lWwKGIuv6ucOOJuwLYtnbQdqfo4Rjq0x0LPPIfCXNE0w7U_Dd09CqN1l1ZtUT49FdKIP7L9kGkAnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515aa7f7b7.mp4?token=Ix2bIdQKpIUZcnUdCaYfRgnDwlmqP_eP2VlJGLpSwuzOSwTa87Ebae1HK8HH5V5dDcnEYgHghbGMVGYWd_8Fqn7NmNiHeiOOGU5vJMY-CAgk18_C6Zx9DVoYEbbTQypK7VhQu7Y7aHyVePs3TfuUipFMzO9fP9kWydgDGxFhRx-vaKWlwU8UDMxsMj5vQ-mVoudn-FSqiI3Q2oavekdT8rWFCfooD7z9ZKHQZcr93_WEIHbCEPKIJLZZmfMeQpKlOK1Qh7ME7lWwKGIuv6ucOOJuwLYtnbQdqfo4Rjq0x0LPPIfCXNE0w7U_Dd09CqN1l1ZtUT49FdKIP7L9kGkAnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرف ما یک کلام، انتقام انتقام
🔹
هم‌اکنون؛ صحن پیامبر اعظم، حرم مطهر رضوی
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669246" target="_blank">📅 21:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669244">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f65aff7c68.mp4?token=rPd1AGc1nkv4duYWOOLLh2JZpJGX1G-BiKJrW40avMiENHiPuZkN9fMhTiOyE4S1dH0QhvOg2Wx78xY3Lkk-GG1UBdLGyWWYoBjLcAoitxQdnP25g-SOVcMao2vB6PDNwm9qNKqc_7jfVkXjoyUtVdZhYPnbDgCfXhJN_y2clRIxqy1MyJfmCbGHkH3-cNrvjHWUfjHrlltKAYWCZbZChuZBEudgEa1IorWJVzTFbN-dQ_LG8iR-5hPUCADpsDJ8T6RqoHJfBzz3L9SSputWJIC2AsPkxwpnTcT-aO7Onz4IvsxyZvTNrIgDTUKVD1OKQKvar-kTs1QfHE173RQhnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f65aff7c68.mp4?token=rPd1AGc1nkv4duYWOOLLh2JZpJGX1G-BiKJrW40avMiENHiPuZkN9fMhTiOyE4S1dH0QhvOg2Wx78xY3Lkk-GG1UBdLGyWWYoBjLcAoitxQdnP25g-SOVcMao2vB6PDNwm9qNKqc_7jfVkXjoyUtVdZhYPnbDgCfXhJN_y2clRIxqy1MyJfmCbGHkH3-cNrvjHWUfjHrlltKAYWCZbZChuZBEudgEa1IorWJVzTFbN-dQ_LG8iR-5hPUCADpsDJ8T6RqoHJfBzz3L9SSputWJIC2AsPkxwpnTcT-aO7Onz4IvsxyZvTNrIgDTUKVD1OKQKvar-kTs1QfHE173RQhnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه ورود پیکر رهبر شهید انقلاب به همراه خانواده ایشان به حرم مطهر رضوی
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669244" target="_blank">📅 21:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669243">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ejzy3IcZ9-VhFYhzo6_1HmVHpy36tqfT2NsDt09B_O6rx3M34QEivCBUB4VUVs2aS7zu72GvIorgGj8SM9bxwb3POnX5YlHT_19ql9gWDS9mPOKjDDN245ME7l-2iB7DNu6fGkl_0b5_it1C2e5cUg48ECwrC7YKUlT30zcXb4yXtDv-XBYpEVw0f91oH4CH_ZozBaULUrcMOZJC9lAFRJ4s22D1LqnV_FHrOj2GKxz6Ak39XMI0hbGCnR6eyFK0Z1NZlONLzzDtYNkKAiB9uzs1E65O4CN1mw5I1hn7XZr2EgSTpPfXaUbMktqivxM2te8FtDBmht9tqgu0IaszQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قـاتلان رهبرم امنیت را نخواهند دید.
(در حاشیه تشییع رهبر شهید در مشهد مقدس)
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669243" target="_blank">📅 21:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669242">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf5a63ae6f.mp4?token=gWuCkt5vk0vQzndeuhY7xmXDCYHrs9XaSv7NqXqjDSwRilsjvd9p5dJChYpmDq3O2jrC50OaVbBkTLGDbintFOtkFWkCIhuwuzJu3mXZf5ER6ifVVy2fIMDgWWwI_CP2u6GWKh1jeizwMWIOTJdZMgDf8_mhrqkgYrj5TiTAmLhTCDaFdOt6AU5OntynWTNnnnDAGtUARaETi-ieysdLkVLtt46_upDchGwkD9Ei_tXkl2ejlRyPp4DxsfYNsChx-dZFGrU1ll4eTjH3y_EoRk-lJT7UZfPkX6a3AQMGE5T2UdWHrPzHvw0VE4eGQAlDTbA9FkaKyU9GaoJbW2pQbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf5a63ae6f.mp4?token=gWuCkt5vk0vQzndeuhY7xmXDCYHrs9XaSv7NqXqjDSwRilsjvd9p5dJChYpmDq3O2jrC50OaVbBkTLGDbintFOtkFWkCIhuwuzJu3mXZf5ER6ifVVy2fIMDgWWwI_CP2u6GWKh1jeizwMWIOTJdZMgDf8_mhrqkgYrj5TiTAmLhTCDaFdOt6AU5OntynWTNnnnDAGtUARaETi-ieysdLkVLtt46_upDchGwkD9Ei_tXkl2ejlRyPp4DxsfYNsChx-dZFGrU1ll4eTjH3y_EoRk-lJT7UZfPkX6a3AQMGE5T2UdWHrPzHvw0VE4eGQAlDTbA9FkaKyU9GaoJbW2pQbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی بهم بگه دروغه...
🔹
نوحه‌خوانی مهدی رسولی در حرم امام رضا(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/669242" target="_blank">📅 21:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669241">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c8950292.mp4?token=I1oe2CyJaedKFEIMJSbtH6fR_QNMt3YA9qFTXJvzvq7bFfIkoQFbK8d49rGey3b9jfSXB8-g_Cu6sRV68p5ee3ewm4qbheY3vHCjj8Pp_uOf8eS0iMLUeMvzXDWxTR1VHDEUbY3yNjLkQE_KEO1k60Drj9EHlDw0o8I3NxFwkB7lody7M33wd1yf1iOEOhqxg4eNeNyosmngn8YoeL6MOf8gG7DrsJosculiiP3_jVdk2wntLANCwf2ANlYYHAnONemctCoA59r-HgnT0rzMflCG71aI7vipBZPnYAQZuMo5jr_6f8Rat7li6JxLa9_A4M55dXjc_XjYsbJNhkmntQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c8950292.mp4?token=I1oe2CyJaedKFEIMJSbtH6fR_QNMt3YA9qFTXJvzvq7bFfIkoQFbK8d49rGey3b9jfSXB8-g_Cu6sRV68p5ee3ewm4qbheY3vHCjj8Pp_uOf8eS0iMLUeMvzXDWxTR1VHDEUbY3yNjLkQE_KEO1k60Drj9EHlDw0o8I3NxFwkB7lody7M33wd1yf1iOEOhqxg4eNeNyosmngn8YoeL6MOf8gG7DrsJosculiiP3_jVdk2wntLANCwf2ANlYYHAnONemctCoA59r-HgnT0rzMflCG71aI7vipBZPnYAQZuMo5jr_6f8Rat7li6JxLa9_A4M55dXjc_XjYsbJNhkmntQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی محل تدفین پیکر آقای شهیدمان در حرم مطهر رضوی
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/669241" target="_blank">📅 21:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669240">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e45dd1ffb5.mp4?token=r6ql3weWUr0tAD8bxvKcPP4QkSb_CSFUwrRBa_eMg5MLXtVAdL-zqTyA9mY2gCvH6HfJOaND1xE_7DAjvxFIkGEY5ZT-s8zk440U1oc9fpiMYDy_ephlgan08NBRfkcb6KHdBqH6L3vQxvTSt25YsvLmWccjwidRq30tEEiAmNZiwxiutqCK53inL5UmJ6WajwkMMkUZCTDALnKKc7UnuD8dtREtviPCqNuE0YgeJu6hq4umYT65yrOSQZWWZEOH8o1QAeed57PLdI9-pBbBIYpmJouq4PjvelTGh0SD93bUd2h3L0VSmytLAMC2mOSKI62eGqk-7yf6mH6eVpcP1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e45dd1ffb5.mp4?token=r6ql3weWUr0tAD8bxvKcPP4QkSb_CSFUwrRBa_eMg5MLXtVAdL-zqTyA9mY2gCvH6HfJOaND1xE_7DAjvxFIkGEY5ZT-s8zk440U1oc9fpiMYDy_ephlgan08NBRfkcb6KHdBqH6L3vQxvTSt25YsvLmWccjwidRq30tEEiAmNZiwxiutqCK53inL5UmJ6WajwkMMkUZCTDALnKKc7UnuD8dtREtviPCqNuE0YgeJu6hq4umYT65yrOSQZWWZEOH8o1QAeed57PLdI9-pBbBIYpmJouq4PjvelTGh0SD93bUd2h3L0VSmytLAMC2mOSKI62eGqk-7yf6mH6eVpcP1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حتما الان به امام رضا(ع) رسیدی...
🔹
مداحی حاج سیدرضا نریمانی در حرم مطهر رضوی ساعتی مانده به اقامه نماز بر پیکر امام مجاهد شهید حضرت آیت‌الله العظمی سیدعلی خامنه‌ای.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669240" target="_blank">📅 21:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669239">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQIFSsNaPMDvu63jodC9LnUMJK3-VLhfSf90tV3HvCdZjCJf14lX1qtZ5F55pn87qEAP-4Rj5HEOW8TNkbAy_mwYbEWw41ZRcmswEbzyZkuzOGEyKxAAz9U8FhrQhySJStD7l4zimkyS9rEb-19IHreZjC9jIYw9UfkMQp9xj0Ve25SSfftJMvJmOXpQXWJC60Ob_NOzc26FZXfpMBGHRuANt3_CAOsiuvcNRYpdIG-Iipjjf4DJDLdxXRdG_sHx_vg9PtLspdb_feZB_K6PDQqzifDplt08-JUQz7dA3CSuu-IhPIaIeNVvek9_VM9wGTzw0YDmvsscnmMbI_9PTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری از جمعیت بی‌نظیر مردم در صحن‌های حرم رضوی
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669239" target="_blank">📅 21:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669238">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">#باید_برخاست
♦️
آتش‌نشانان مشهد در روز وداع، در کنار مردم ایستادند
🔹
آتش‌پاد امیر حسامی، رئیس کمیته ایمنی ستاد تشییع شهرداری مشهد، از اجرای موفق طرح تأمین ایمنی مراسم تشییع خبر داد و گفت: آتش‌نشانان با استقرار کامل در مسیرها، مسئولیت تأمین ایمنی و خدمت‌رسانی به عزاداران را بر عهده داشتند.
🔹
وی افزود: تمام ظرفیت‌های عملیاتی در آماده‌باش کامل بود و مه‌پاش‌ها با خنک‌سازی مسیر، گرمای هوا را برای عزاداران کاهش دادند.
🔹
حسامی تصریح کرد: نیروها تا پایان مراسم در کنار مردم ماندند و ضمن پایش مسیر، آمادگی کامل برای عملیات امداد و اطفای حریق را حفظ کردند.
🔹
مدیرعامل سازمان آتش‌نشانی مشهد خاطرنشان کرد: خدمت‌رسانی در چنین روزی، فراتر از یک مأموریت، افتخاری بود برای همراهی با مردم در وداع با رهبر شهید و همدلی مردم و تلاش شبانه‌روزی نیروهای خدمت‌رسان، برگزاری منظم و ایمن این مراسم را ممکن ساخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/669238" target="_blank">📅 21:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669237">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de0dee9cb6.mp4?token=FSqTZUotuZ1u2HpeyeYlddAPTQZJ6FYGixIuSU8oci--rX5NVnGNyBPV6LbM87Uo-F7XWrXcnFSUGOAIgLz5BqLLLndX8vAozWUAOD6VRzIl1Op7rJTmkthGhQVVHfM2wvxjMn4NBAIKKwYx6u7uVB8vUbDTsWpotCSM9mGsWdl_ToFIn1BOrO_1VMlanG78E-7yMLtunsi9Hg4sALX6HmqvE509C8M3Dg37cRf4KBcLRcQSqgOdCdkGcRNnMiU78iYugUqzBYDlt_ce_zngmZMSQT1F4TbyPo1FrxNEFpBQSWPTqVOm7j85hTzfTLKEOkHHxd1ayoZd8SaI0t88dIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de0dee9cb6.mp4?token=FSqTZUotuZ1u2HpeyeYlddAPTQZJ6FYGixIuSU8oci--rX5NVnGNyBPV6LbM87Uo-F7XWrXcnFSUGOAIgLz5BqLLLndX8vAozWUAOD6VRzIl1Op7rJTmkthGhQVVHfM2wvxjMn4NBAIKKwYx6u7uVB8vUbDTsWpotCSM9mGsWdl_ToFIn1BOrO_1VMlanG78E-7yMLtunsi9Hg4sALX6HmqvE509C8M3Dg37cRf4KBcLRcQSqgOdCdkGcRNnMiU78iYugUqzBYDlt_ce_zngmZMSQT1F4TbyPo1FrxNEFpBQSWPTqVOm7j85hTzfTLKEOkHHxd1ayoZd8SaI0t88dIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما رهرو امامیم، دنبال انتقامیم...
🔹
هم اکنون، شعار مردم در حرم مطهر امام رضا(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669237" target="_blank">📅 21:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669236">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
تلگراف: مشهد به دریای سیاه و سرخ تبدیل شد
روزنامه انگلیسی:
🔹
جمعیت در مشهد به‌قدری مسیرها را مملو از جمعیت کرده بود، خودروی حامل رهبر شهید انقلاب اسلامی ایران به سختی می‌توانست حرکت کند.
🔹
خیابان‌های مشهد به دریایی از رنگ‌های سیاه و سرخ تبدیل شد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669236" target="_blank">📅 21:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669235">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8791f99083.mp4?token=SXm8rlBBtjZJd4eKCie7XYk_enD73v73MDkOfGpzTvPAqNH7kQEvqfTNoIQV4bMkZKqqqTeaib03NPQkBCDy8zn9NJR1NbymHe_DDdFcFG9TKgmthBn54O21XRimN1JvxflrlRIHqlloBb4NhUm_KLRa0favW2-efX9Iwn7Seg9nI6pHXUuqfe2oipLl3Qtkg42I0BHcPAfl6tTxlJw_diw9I1CJv--_Nt-TCXsNF6FHxoZ1ZCHiK636gw5fYntsTUGYhInJ_7VkuDKccFVwtWX1Yy80iUOSfK4PoQG6Yvs8V2yDo4tsMRaWPr1mHLXN9crifjArCCMrucfKjq9_6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8791f99083.mp4?token=SXm8rlBBtjZJd4eKCie7XYk_enD73v73MDkOfGpzTvPAqNH7kQEvqfTNoIQV4bMkZKqqqTeaib03NPQkBCDy8zn9NJR1NbymHe_DDdFcFG9TKgmthBn54O21XRimN1JvxflrlRIHqlloBb4NhUm_KLRa0favW2-efX9Iwn7Seg9nI6pHXUuqfe2oipLl3Qtkg42I0BHcPAfl6tTxlJw_diw9I1CJv--_Nt-TCXsNF6FHxoZ1ZCHiK636gw5fYntsTUGYhInJ_7VkuDKccFVwtWX1Yy80iUOSfK4PoQG6Yvs8V2yDo4tsMRaWPr1mHLXN9crifjArCCMrucfKjq9_6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار یک‌صدای مردم در حرم رضوی: حرف ما یک کلام، انتقام انتقام
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669235" target="_blank">📅 20:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669225">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aiMWLlT2b5EQ-99ZT9ZUFtDxhXrJpMh7mwZeeSGchKieeZaGe6T9DhMY-Owb-y1g6CnLnO6xtRkcBDptGHVc4et-pspveBNMebUBY5MsmTNsOluTmo_uTXXB7hJj_XH3CIn0OaKatR4BgWvdZ9REtCiffKMqPpmenSSR8Ly6j5HxBTvrB328UJrZQuQrnRVSzz4Ajc44tLegI8BPs2trAbu-o11t2xnVI0I6QR8G-d11KUoX1heBftExvZ38DkG7SfkNdXTbTXcTrZxUGFBlUYA-QPLd012nXah324xxHT5yL7hB9EXZb1ao2s4KTda_pcZTf37npSChuO3SluFRQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAX00ayNoUOUg5KJUCHWGBj8jJVtFms129AmISoPmrTIrVnX4EEArTG1qrWOnDyXzuK09cVTtAQRpMsyRGXGlhxnKkZhHZSPuLAuu9yA3DZrMiIaSa64rGAv_Zu9WiBw9kzp6xV5TJxRf5upSHjtLIObYyfmjCn6YL4MnLHdm4L69CJ4IBY-soAWNPAvTtwAWBjPcqQORHr00mycqbixo6JSadqJi8heLWV0pJcVD4PBN6Fsds1BtDR7rHvzo5ORl4tdNtVO_59VDFq8QMDn8A_KRLHDgnzKfoUQQnnQzShAsxUpjT7vpaBWIm993E0uem28vuNEcwv1LwhhSIcmsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vx8U5AIJlCNQ9wMrv6gK-G7yUvIXVqDX3kdfkVGTJSA7SELGwXUq18XekwDxV-ck28VHmoq7heK3pMdX2bAzZDq_zNbbTneqOq_TOzmAJ1w75OVj4IIm3JcmfnuBF1ITwa7GsprvbY0pJZdT4spdve-ntFlbXPFaLAgkonRYo8Esu2w3lCm6mBIdTQHuaxGUk5yNmo-5HfZ25347Tg_y9ghrDpuKo9woZdtFWNN5U2cBkGrL7cudfw3paLM5MHiUucn3O0DcWhjXyOCOotM1JlidSO4kRSMYVMENamfH3wvD8Nn9gfgV0surNSVu1ZTKhd0H2mlkZgDhKhqk3Q2jtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KjYxAOB_2reTTUyWGo4dA-bIxLK1Ot2f4uug-60B3e4fFWrn9emCD-U88MxitsYffI7Zaqvu-wEKYR0aZJYj4r4uS0z1y2WZT4ocUad2T0bC-2KREpdSWVax_rIDh8xPgHa55q8RccYVLNO-8ajEuwIJiufBIUaPGTNApBzNunTHWZOwOM2ltFtgSpvSEOpFaEjQECgD-vASbQXLDkhcPUDTBsEx1OHg12pih232CqcJ7FcSvqbT2L1erV6OOz52eDfcT1RLuqzzlnVfg85u1RMluojea1EgewfppVpzpHytIeaYSF8Yek1hkbQIl_VE4BcOVDIq0EFEp_vL_Q5h-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OVrJlKPSUwEfl6zm0RqVrcb6sSxsJK0SdHdBsEb6JPffPAvJrchU5parK1m3bWyyZDhEr-Ta5kctJ3NilaX6K3fLsKO0eoFhHY85guP4UPfQq5t3zbMLArO7D7tdx5CEE14uosk6S-2Z38MSNa8kZKirLAnEDp3CbJ1sJ45iUEdeY5KHhnjjyJGg1KjqCb-F4uHmlv4baIjhOqL1FvBbM3tXtIfjYo0HhpK2PnSqmKeTSVbo44aWIfmpecn7tmLMTSHXWhSxRTw0GfW8W5DrdZRRM5QUZz87oyp3RwXXDohhKiGTuRCl0stEJLhG7uF_evMXjGl_SJ_9jdKIxtKgJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lyC8KIVdnIZ08T8_6GDfWVghiX7AJKYiy698dvP1SE2edpaU7YPtTTglF6LjpxyZ7FgDXfeUkysRcYFoIyW5xT6lz_oHJ4HwNgR5wFGY9tbJwlpfBhqlD6lfsv4LzNLdE9HN8frh3by1lesWX_Jvljvjh9MctAXPob8sSga3JmixvrJhc0FF_mbWo8AkA_vZADDWpk5DCQUqY05i-X7OOaqq4pbZXRrjijDyOT17WlF4baEVF81DfFsSl6ks_Vium_yqOmS-fZytf1W7ecuQp9cJ0y8rcCfIISn_Wn9wxHpnCAguEzr46X0mf3UNd0tkaAyDbzb_cCTYu_WAzN75ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2y1y6_NZDt_4xMOjDfDTfPjtvxNoA5DGivEl4aP25icYkjb-YJz36SOuy0z-ZcvWrK_bVvaraS3nBr-RU4WHr2pu161w4pWS6rY7Z2vMgfYF2G7nBgtTXWjQkxX0-2Tu_SIMCZcshJKQPhSu0hp07Vf7pnyqbmue_s_4Ilt23C0cZlKKm3wnB8_aev0R2Gndze5o9bjE4ZZr2o9NN8Zj09sF7Tfl5ifEIh9khzycbrmIpAPIG1lCo1tV18-mQ2KDybJ2unpBxnsfQjd4lVbzP6xmBukgnwSw25HGr7LIVCF0W217ZhvzBLPeN5_q6qEnvK590_lE0pTQmtSQLAN-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pnj8mTrLWukFJUqHFhBlePAaYaU7vxk7cCl3CJMi6PmNaJLBLsAQLCN8qP7ll368ci7qN67d08uRBsU_6kIZJA-cjIAaLazYtjFBaQelYSBy1oJ8Z1b9qPIGRZ2lKBiKX62wuDFIPsze0aAvdMmc6h611sacwqMg5B9i939YZIAfVNmBAoJEqkd6w_xB_QlFKJQIEyW5u9-473dtNI24cQ9_KSLHqdHrkynIox_-N-X6l5tgRpLfHmVZsT1GmvwQcL3LE8eJ-Fxrnme41SyJtt0DhM0ul46Y4F96GmF8eobD_a3C5WEkssGtZExRUiA7rp4UFZjnExPa3bUkgqhMRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iCcFdScAybjmKRpDdKFo15480yP1sffarnVGVQrLgepVs84_gL_LfjusM95End3yI_uJ9Vda65UEudxquLW4MyFRVjuwOxXtiMgbBvSoucrdQ6096QwBHAqAppkAYifbghVHOXYIh7OZOXrZR52L3O9k46ClTWtykEAJyMh-5lPcEehSS-3jnoedlnkhMyT1LDaZjvShyiaVYyNr7fx1uO3EyZLP1CdIhw0ogkBoVcrfRe-MWitPcp7OsEFnYasw_s5GUg7G8fd_tQM7YEnbfbqHesq6fapR8ixnwVy1XPbRqiFA2Dc2d1cr8itCtTSlHGa2HP9l3FL8z1mrN2-rBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TZHK4UOhLCYta9HO5TjGzVt8L-CsaevXfcvnte6fKQ56Y7GN6jydZ5RSTVu1eV4S3JuJMVxLtIoThz-pudCqFOsgjBlT8YWAFi4OmU__oRbikllTPuBntNcoRQ-dO6T1jBAOKFUc7Mz1qO_B5y7CLONmIb8qF-u3HIV_OQkeuw8SgFe1CgTZY-ZyOga1ZvMzA6LyJ73QfGmEKq57WEwBBjP2d-ABPczCCB_GEtsIVZOwv-OCMjHinq__xwgTFzIUYBV5HuD5PtzoF4smvKMePWbe2lSKxGMNVbQTkyFbIvybmqv61DhFUIjQYU0LV_Cjt5llWYScZ8tpJlNxQ5pRTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پویش مچ‌بند و پرچم سرخ
🔹
حضور مردم با مچ‌بند سرخ و پرچم سرخ در مراسم تشییع رهبر شهید، جلوه‌ای از وفاداری به آرمان شهیدان، ایستادگی در مسیر حق و مطالبه خونخواهی رهبر شهید است.
🔸
تصاویر و ویدئوهای خود را از این حضور برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669225" target="_blank">📅 20:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669224">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c208eda68.mp4?token=aFfnO0CwyiDOCeRKeoVIS7q0lIMSLXftnzaAtpRh32oWKKyeP0enVF45pWonPNOr8ZBNbnoFtyM7L3IF-Reb5WsCFYS2gbEIH2X5Swil5yV3QRqX9S9HNHU8VAPBNQWzGz3BcHkFfVkorT44lGN7BfznoW_qWPXARehv_yKRn9MAH3ViJhcI_g_tI8Jb8s5gQ_5FLC4BEazMtS9HhR-Q74Wnq9jlS_88qKk_NiiH-_NEbnIFVqB2JmMbtR8TOnpwxuuykGs-0cOezFduKso6YuBZjgWj6DL6meCg4KYl9K-sy59d4fSMPUsvincrvYEGQJhV3e1cEf9_FAny6A0tpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c208eda68.mp4?token=aFfnO0CwyiDOCeRKeoVIS7q0lIMSLXftnzaAtpRh32oWKKyeP0enVF45pWonPNOr8ZBNbnoFtyM7L3IF-Reb5WsCFYS2gbEIH2X5Swil5yV3QRqX9S9HNHU8VAPBNQWzGz3BcHkFfVkorT44lGN7BfznoW_qWPXARehv_yKRn9MAH3ViJhcI_g_tI8Jb8s5gQ_5FLC4BEazMtS9HhR-Q74Wnq9jlS_88qKk_NiiH-_NEbnIFVqB2JmMbtR8TOnpwxuuykGs-0cOezFduKso6YuBZjgWj6DL6meCg4KYl9K-sy59d4fSMPUsvincrvYEGQJhV3e1cEf9_FAny6A0tpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ای پسر فاطمه(س) منتقم تو هستیم
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669224" target="_blank">📅 20:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669223">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCwCWnbNoE6CVcu6m1Y8PEyTQtFtCru1q_R-QGJP3x6URDCRovyl31DwxKM065WpXZ7falU68tNNvFh-Q2muVOTgwcRMs2Zx618vq_88veJ9JvJRjHYWnGxqdjKQOLEJaiNV9eFGcdBfBFZ1gd_Oz2mtCIC8dv_lDYCxxrffQTBuidiAtR9E1ZJdI0x62JqawwICGYtQENnigWLj7RRl9QyoxAtkRL7IelIKHsfDjncbdkN6axXEpB2eP3fI3eQpAafJWboHA0d9rk-DobFUtjt3Xf9GY2Ng5zJU-1Birv1RwB-wc67PVDPgahRZWeRiGiwZ7HLuAVbP-tFko1DBEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انفجار مهیب در شهرک الطیری لبنان توسط رژیم صهیونیستی
🔹
ارتش رژیم صهیونیستی در ادامه تجاوزات نظامی خود به جنوب لبنان، عملیات تخریب گسترده‌ای را در شهرک «الطیری» انجام داد که منجر به وقوع انفجاری بزرگ در این منطقه شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669223" target="_blank">📅 20:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669222">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXRBSCePKS80x5lkqwLU_S8HQ3ybzRwJC61w988B63-E330vIrdozOkioa088YtzzOCXQzTP6UOH7lyIHQHz-4_oBqGxGYY3tffD7Jyhep4HtGYMea70n2DuIWKVtdSAY_MnjVzQDgs_l_rI-XQZog_zYfwZD8S7SIvWLJb68Ehrz6WjXzNprGc80EmnkJxS4jyq42HfZLUkIM9SwiKK95zy_RoUGQM9qvLYWLbk_SxuOGWCBjZeUYISMedzFAIDgdWeGignaPmGppnSftd5xBVmxuVlx3kg6LznLt4uaKmwfnQRx_WumudMXqM-SeRORlpe5C4FZ_hUy0jQeqo6GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعالیت شبانه‌روزی ۸ نانوایی و ۵۰ کیوسک عرضه نان قدس رضوی در مسیرهای تشییع
🔹
هم‌زمان با آماده‌سازی پایتخت معنوی ایران برای برگزاری آیین تاریخی و باشکوه تشییع پیکر مطهر رهبر شهید انقلاب، سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی شهرداری مشهد با بسیج تمامی امکانات و ظرفیت‌های خود، تمهیدات ویژه‌ای را برای تأمین مایحتاج عمومی زائران و مجاوران اتخاذ کرد.
🔹
به گزارش روابط عمومی سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی شهرداری مشهد، ضمن تسلیت این ایام و تأکید بر لزوم خدمت‌رسانی حداکثری، اظهار داشت: «با توجه به حضور میلیونی عاشقان و سوگواران در مشهد الرضا (ع)، اولویت اصلی ما تأمین نان گرم و ارزاق ضروری در تمامی ساعات شبانه‌روز است. در همین راستا، طرح ویژه استقرار ۸ نانوایی شبانه‌روزی در اطراف حرم مطهر رضوی عملیاتی شده است تا دسترسی زائران به نان با بالاترین کیفیت فراهم باشد.»
🔹
مدیرعامل سازمان در ادامه به تشریح موقعیت این مراکز پرداخت و گفت: «این ۸ جایگاه نانوایی در نقاط استراتژیک اطراف حرم مطهر، شامل خیابان طبرسی ۱۹، خیابان طبرسی ۱۴، خیابان شیرازی ۴، خیابان کاشانی ۸، میدان ۱۷ شهریور، خیابان شوشتری ۱۱، خیابان شهید سید حسن نصرالله ۸ و همچنین تقاطع نواب و شارستان، نبش حسنی کارگر ۱ مستقر شده‌اند و به‌صورت ۲۴ ساعته به پخت و توزیع نان اقدام می‌کنند.»
🔹
وی در ادامه با اشاره به گسترش شبکه توزیع جهت رفاه حال زائران و مجاوران افزود: «علاوه بر نانوایی‌های یادشده، با هماهنگی‌های صورت‌گرفته، ۵۰ کیوسک عرضه نان قدس رضوی نیز در نقاط مختلف شهر و مسیرهای پرتردد مستقر شده‌اند. این کیوسک‌ها با عرضه نان بسته‌بندی، دسترسی سریع، آسان و بهداشتی شهروندان و زائران گرامی را به این کالای اساسی در ایام تشییع بیش از پیش تسهیل می‌نمایند.»
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669222" target="_blank">📅 20:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669221">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284298ac5a.mp4?token=mj4IxqpR0eHcXIbPD6ThHvUvfvhZczHO3sXDkWH6QRQbQHKK6RA8j7alMnBMBgegFMroR2tW-XfMPRjS1kfSegDFtmlhwhLfHtdtphjSesbmglQxNnGhhU3SDvSQQRyDNu9dQErRSyc4XJ4Tb15YqGXZ8XgZUBtfD2FPz_7wM7M0LZnHk2SCyimlhrdfCz5x3lYLZJKlHYnRrYqYDikJJ4gtKlvz5vTPXt9vDLYOHQa0wXvykjSd8pTF_MdEPsMslHqgHjk4x7LJPUUSRyhgJTHe3B5fwVCBxnYAu0TYpBiePasevcBYeStJVRNOAFLM6m1cKF_SjFhJ87CqWEdJgYDpbwAcYHDwAEZZr4s0SaZvQgv2yIFqngCdAgc18Y3SmHS_JZViiu1PBgH2WrY7ThPC-AWxki1Wa0MRnJDO72KAUUpouRcYKjt9I5Xnw2iyoznuACAP6WeMK31MiQDeVNUB79gHKSovBhXBPi1hvYfCO3kiRZC8J2fjlCcs43SQezz8ovB_9KK6Wchi5yW__GE6B3uLj526lbcpksJRrDqZCnWeobyr1qMx-pY_xW8Vude7L3bbo3A5YST2DNa0doqF2I3xs2Q_GJsq81V406TXucQOE9fPgxMm2FDKg0ezuHDKbV7vMVGSGYhyE5fz2J47EA_CEZSfog5CKzvhOHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284298ac5a.mp4?token=mj4IxqpR0eHcXIbPD6ThHvUvfvhZczHO3sXDkWH6QRQbQHKK6RA8j7alMnBMBgegFMroR2tW-XfMPRjS1kfSegDFtmlhwhLfHtdtphjSesbmglQxNnGhhU3SDvSQQRyDNu9dQErRSyc4XJ4Tb15YqGXZ8XgZUBtfD2FPz_7wM7M0LZnHk2SCyimlhrdfCz5x3lYLZJKlHYnRrYqYDikJJ4gtKlvz5vTPXt9vDLYOHQa0wXvykjSd8pTF_MdEPsMslHqgHjk4x7LJPUUSRyhgJTHe3B5fwVCBxnYAu0TYpBiePasevcBYeStJVRNOAFLM6m1cKF_SjFhJ87CqWEdJgYDpbwAcYHDwAEZZr4s0SaZvQgv2yIFqngCdAgc18Y3SmHS_JZViiu1PBgH2WrY7ThPC-AWxki1Wa0MRnJDO72KAUUpouRcYKjt9I5Xnw2iyoznuACAP6WeMK31MiQDeVNUB79gHKSovBhXBPi1hvYfCO3kiRZC8J2fjlCcs43SQezz8ovB_9KK6Wchi5yW__GE6B3uLj526lbcpksJRrDqZCnWeobyr1qMx-pY_xW8Vude7L3bbo3A5YST2DNa0doqF2I3xs2Q_GJsq81V406TXucQOE9fPgxMm2FDKg0ezuHDKbV7vMVGSGYhyE5fz2J47EA_CEZSfog5CKzvhOHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداحافظ آقاجون
آخرش یه کربلا رفت...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/669221" target="_blank">📅 20:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669220">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8208393dc7.mp4?token=hM0_gQ7opPEXVctj-zInQVF5jpHFMsy6_JhEkVhEdm0OgIN2MAA59YVRw0ivG-eV5-EKZRWey1Xyi9WWnvCxHEzPTUEbE-rGwbFPjzfpCbJ7h5qY_nu8CqFo1mO5E8ymLp5et0WxVZC_8u47KfxN2FSOyBONXlu01986eH1e_q4yHxRWsZYGSrzIlc-nXkT-IKFydYeBwDgUlQRSAEl2pJi-2lJrUhKlU5EwCGTrgdR4M3dstpp-459OG0djE5VWc4MuS-jMsRkmLqkdmJ71oQtbmfEm4DRuSixEZnHAbXMWk6BNH4naO0ycZVkOp95zpI88lwNSPwLlAD8B7ULiyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8208393dc7.mp4?token=hM0_gQ7opPEXVctj-zInQVF5jpHFMsy6_JhEkVhEdm0OgIN2MAA59YVRw0ivG-eV5-EKZRWey1Xyi9WWnvCxHEzPTUEbE-rGwbFPjzfpCbJ7h5qY_nu8CqFo1mO5E8ymLp5et0WxVZC_8u47KfxN2FSOyBONXlu01986eH1e_q4yHxRWsZYGSrzIlc-nXkT-IKFydYeBwDgUlQRSAEl2pJi-2lJrUhKlU5EwCGTrgdR4M3dstpp-459OG0djE5VWc4MuS-jMsRkmLqkdmJ71oQtbmfEm4DRuSixEZnHAbXMWk6BNH4naO0ycZVkOp95zpI88lwNSPwLlAD8B7ULiyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرندی، تحلیلگر سیاسی:خروش بی‌سابقه و میلیونی مردم در مراسم تشییع  رهبر شهید چشم غرب را به واقعیت باز کرد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/669220" target="_blank">📅 20:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669219">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sH2h-g25iJP4RCWbTMe10RHBqh8ITk-PTW41w64viQhRMTjoFdGE458apMaLnl4WhpSN78GJNw_ynK5wsSKrdeTHEIe3YhYmYrPLMqQ-zAhFK6a1V0T1ql5XqzDVufCDpXYh5Fdqrgo971x-PihsE0zZQf64qw_QaSg4PnJOwnbuJYvivVSr5FBq61vIC5iHaADSYAoDUO5S8nJww6O6XY1QtMJ3mr3_PJybzYxch4eYgR1tLWGjk_RAX_YM1SFRs3CHF4Z1Yv51oWFHN4hTZMHi0H0Up4v_fPg3LcZEOn8OKBc3NCeFO6vTbSTt2pTcl0Afi_EOp8E8H5yk5DD8UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در آغوش ابدی خورشید...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669219" target="_blank">📅 20:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669218">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
رد پیشنهاد ضدایرانی امارات توسط روسیه و چین در سازمان بین‌المللی دریانوردی
🔹
روسیه و چین در نشست «آیمو»، سند پیشنهادی امارات درباره تنگه هرمز را یک‌جانبه خوانده و رد کردند؛ این دو کشور با تأکید بر اصل ناوبری ایمن و آزاد، با این اقدام علیه ایران مخالفت کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/669218" target="_blank">📅 20:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669217">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57e8dde714.mp4?token=Gd3YCWp1GI_2rrdDMNratWta94CrN7bMdO6qTGKADQrzDnUNKrq4fEcrlAsQLF1O3DuCTqKoOAnxhw3osHQKxCnXCFxBT-zCfGAIJAM2BxL1QQwHvkEw6TO3EZ67-CBL2_Q5ocmbNuAORxeXalFiQtQAZcxg4wGULF8eGqyUtNTaFMvlCvdLbuxCdwdImY2GLXa1riquUnt2q9EOo_AbwCMKtLsyXNYExZmrPK7pKUFaJ5ud21v1yp08OLamV7kARGW5wcMATz1e16iHLkxXl53Osw7BGXzAtqhUqRxrBKCori3DG4-MvwNOcpYS_hauSy_gIYiEl1R-lHNHLGxDPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57e8dde714.mp4?token=Gd3YCWp1GI_2rrdDMNratWta94CrN7bMdO6qTGKADQrzDnUNKrq4fEcrlAsQLF1O3DuCTqKoOAnxhw3osHQKxCnXCFxBT-zCfGAIJAM2BxL1QQwHvkEw6TO3EZ67-CBL2_Q5ocmbNuAORxeXalFiQtQAZcxg4wGULF8eGqyUtNTaFMvlCvdLbuxCdwdImY2GLXa1riquUnt2q9EOo_AbwCMKtLsyXNYExZmrPK7pKUFaJ5ud21v1yp08OLamV7kARGW5wcMATz1e16iHLkxXl53Osw7BGXzAtqhUqRxrBKCori3DG4-MvwNOcpYS_hauSy_gIYiEl1R-lHNHLGxDPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لیبک یا حسین گفتن مردم در حرم امام رضا(ع) برای اعلام آمادگی جهت اقامه نماز بر پیکر رهبری شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669217" target="_blank">📅 20:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669216">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1791ea9a1.mp4?token=Z-xafZIIv4qyMK5HonSacdrQb7dxXHUNqX8MEt93lBAbOB87ujW-ZnT7rjLPTvv6InMY08jsIl4QaFIsPdbqlYQMNCbIq8fF_c5-fdXUa3ZM61QCX9eVd0J2Van5F5frTl39qvp_VyMdAJ0G54gCeMmb3zkn4QJJyV4fC5b-Y9WDHEXGIG-s6Sy5LXhYwQqBa11aSxK25ZaAoWCc72w1JQXXwDPOfzzGcJghG_HBuBcOzReEV57a1geM0TX3k0TByQRWliL5TAnWS0Ign-trBxqkDXE8kMAA35jTnKINM9Uc_LTCHBPwYb-5UL11HdnmLj5xb3ijW7NEKJDPAt4i7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1791ea9a1.mp4?token=Z-xafZIIv4qyMK5HonSacdrQb7dxXHUNqX8MEt93lBAbOB87ujW-ZnT7rjLPTvv6InMY08jsIl4QaFIsPdbqlYQMNCbIq8fF_c5-fdXUa3ZM61QCX9eVd0J2Van5F5frTl39qvp_VyMdAJ0G54gCeMmb3zkn4QJJyV4fC5b-Y9WDHEXGIG-s6Sy5LXhYwQqBa11aSxK25ZaAoWCc72w1JQXXwDPOfzzGcJghG_HBuBcOzReEV57a1geM0TX3k0TByQRWliL5TAnWS0Ign-trBxqkDXE8kMAA35jTnKINM9Uc_LTCHBPwYb-5UL11HdnmLj5xb3ijW7NEKJDPAt4i7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار مردم در حرم امام رضا(ع): این همه لشکر آمده به عشق رهبر آمده
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669216" target="_blank">📅 20:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669215">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
پایان مراسم تشییع و آمادگی برای تدفین در حرم رضوی
🔹
مراسم تشییع به پایان رسید و عزاداران برای اقامه نماز بر پیکر رهبر شهید و همراهان در حرم مطهر گرد آمده‌اند؛ آیین تدفین در رواق «دارالذکر» انجام خواهد شد. زمان اقامه نماز لیلة‌الدفن نیز از پایان تدفین تا اذان صبح است.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/669215" target="_blank">📅 20:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669214">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9sIxAVoJ3R0542czw3tbCcYtdcu-XORONIxkSICXedE5wiuD72W0yPee5OLmfwrfLxFlPkYPEr5A75C9zkRPgxtrRtjfmWqCqyayiLay7hAuzL3VwpTnW-fbo_ErbzyYKxWY1YHdGg3ocgL9scraHTaEPQ2b55CPmBgSTwOMdav6dlCvJKD8-_DlCEFDu1h1UV2mVxDU9uSseWvQ-QpvUI3ET3juXrbogIF8SyvPF2AcZLm37CDlurZOaiq6fxflUj9mvrD5ftd_wuJldFTcJD3bYK8cKwaYx7BEunuL_XgDNCbpmDkthzwzLywgzGvM4ckFq85oOGPF_zKaGUfgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه دیجیتال اخبار مشهد با تیتر "مشهد برخاست" حماسه امروز مردم مشهد را به تصویر کشید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/669214" target="_blank">📅 20:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669213">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
تلاش قطر و پاکستان برای ازسرگیری مذاکرات ایران و آ
مریکا
سی‌ان‌ان به نقل از منابع آگاه:
🔹
دولت‌های قطر و پاکستان در تلاش برای میانجی‌گری جهت بازگرداندن ایران و ایالات متحده به میز مذاکره هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669213" target="_blank">📅 20:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669212">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
لحظاتی از حواشی سه روز وداع با رهبر شهید انقلاب در تهران، قم و مشهد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/669212" target="_blank">📅 20:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669211">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
شیخ ابراهیم زکزاکی، رهبر شیعیان نیجریه در گفتگو با خبرفوری: آیت‌الله خامنه‌ای نماد مقاومت بودند؛ ایشان همانند جدشان امام حسین(ع) خانواده خود‌ ‌را فدا کردند
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/669211" target="_blank">📅 20:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669208">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuihFBZ0r5LFqaw4oBJvaqNRZQvuonF82tUw1zvDEs3l-U60DVLK_71XG_lBmSVORe2hc3LYB-BMnBcFxuUSLU83iZBdAxtfxJSPr6MAIyrYhv9JJSX7qsxwd2jSCSHN_R4Uy5UMYzSosLXMTgSft94ecqEIU-rzQ7irLHMWx_YzItAWmIW8s6qVa9DG2l2pUQ_hr-jhw3yYzpexNiBdoZk4zeyvRU1HLhnP-SaUJqzclyWFX16qDAOTNFH0T1wPR2aGb1h7iA1Ndl99mZZ7a8FCh-OtEJmOJ9tiN4AKUGHY0OLRIcYOHKmfXmZJ0aZVojE2jK0C2b2x3DLiBIJOTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در راستای تسهیل تأمین مایحتاج زائران و مجاوران انجام شد؛ فعالیت ۱۸ بازار میوه و تره‌بار شهرداری مشهد در ایام آیین تشییع رهبر شهید انقلاب
🔹
سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی شهرداری مشهد، هم‌زمان با ایام سوگواری و برگزاری مراسم تشییع پیکر مطهر رهبر شهید انقلاب، لیست ۱۸ بازار منتخب میوه و تره‌بار در سطح شهر را جهت خدمت‌رسانی ویژه به زائران و مجاوران اعلام کرد.
🔹
به گزارش روابط عمومی سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی شهرداری مشهد، ضمن تسلیت عروج ملکوتی مجاهد خستگی‌ناپذیر انقلاب، اظهار داشت: «با توجه به حضور خیل عظیم عزاداران در پایتخت معنوی ایران، تمهیدات گسترده‌ای برای حفظ آرامش بازار و سهولت در دسترسی شهروندان و سوگواران به اقلام مصرفی، به‌ویژه میوه و تره‌بار، در نظر گرفته شده است.»
🔹
با تأکید بر نظارت مستمر بر کیفیت و قیمت عرضه محصولات افزود: «۱۸ بازار میوه و تره‌بار در نقاط مختلف شهر مشهد آمادگی کامل دارند تا نیازهای روزانه مجاوران و زائران علی‌بن‌موسی‌الرضا (ع) را با کیفیت مطلوب تأمین کنند.»
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/669208" target="_blank">📅 20:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669207">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
تکذیب انفجار در زنجان؛ دود حاصل از آتش‌سوزی سوله بازیافت است
🔹
معاون عملیات آتش‌نشانی زنجان گزارش‌ها مبنی بر انفجار در این شهر را رد کرد؛ دود مشاهده‌شده ناشی از حریق در یک سوله بازیافت ضایعات پلاستیکی است و نیروهای امدادی برای اطفای آن به محل اعزام شده‌اند.
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669207" target="_blank">📅 20:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669206">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5Loamh5ffkGd9fkwaHjOSUPP0r6yz_UfS9HBGFKK8Y2DBjb1271uCEEI_loDMWRaNEm_v3uGfV9_uNxlHt1bnMtWA474a_4GafISVq0n2m8Yen-0rWoyU3zQ_-mZX1gZfTvhDRbL4e2JNK2V5YxQX2F2q71f3WskPeSSGhZlwc32f8H3xZuRgrRB6tHxWQcMEPd-Jpneo7uU30eWLg0VizOh_aoSGGrOUwlPajTjINV3LDZy7jgIlSdtqlPMF1soqUXUDyE7OY--rqPlfwvN7qUPSspOiXvrT4_sHxUpmkgdFANWU67ZxegJmp2kCp_gdWjWeBFFYlRcmamGRucSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیکر رهبر شهید و خانواده ایشان پس از آیین تشییع و اقامه نماز، در رواق دارالذکر حرم مطهر رضوی در نزدیکی روضه منوره آرام خواهد گرفت.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669206" target="_blank">📅 20:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669205">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
تردد قطارهای مسیر تهران-مشهد متوقف شد  راه‌آهن جمهوری اسلامی ایران:
🔹
به دنبال حمله جنایتکارانه دشمن صهیونیستی آمریکایی بامداد امروز به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.
🔹
تیم‌های فنی و عملیاتی راه‌آهن…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/669205" target="_blank">📅 19:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669199">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kUy261WUxiaoz7me2pssvCJ8Tzvdly2Hmz2LA3Vz3txxDM4XvzkgWAlpK40ySuMsw6zXBCU1_Xm-lThHV2u_IG42upnW6F293xoWka2tNfnrYo78-OvJLmuhvd4rWLAcePhx6vcpRFzQOG9yV9-39cY33O6RvweFHm8v0S2aSjnV9GfHaTx8d4j5qry-vmTXTipp5F127Z6-1_xXljf0tLz4ojXrxd2z9vlcJtCvhnLqD4Nn6oLAqrYL5UTmGcpXnyWAOL_31xLfHatLLIAopupvzhRGXSosYTrzX6cM-VlmXn9Wkhezp6ilNQt7j-lISsKSmMgkkY1lPwA2Or8yeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nkdOWWo69CraZduRB4qSVOZDcYh1EaJMww9SXsPednxIdvOJRZKuOmpDkjY9xr-WruXoTobp5HaChh3W9YwtWKsVfyzj_8ckr-h-Wyb4Q5DYzAa40cKETc94V3Tvmo0JeCPSVkydZb84fptev2j9Stb_boD0aq-dW76CDlhH_AFHYJciLNMfImnaYBYyRo6Tph72TQTEXfJGAjWx6MZ0Xzerob0bbxPGmKqOi5O2oeg40jlw5EY1xGZLrZxk7OXXjrXI4PDkV6q4mVRKPKkzdiO29wRVCbF22mlHFzNMH9Z_hrjScArGhrXRHWhIW86WotlT3vM51rIK2FdwDvtv9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bmvq3u1SbhRPc497W5Ja3tik3_lv9GhFVq6f8YY_-GqZwgDTX0Opi5GBO1kKzs8pIbBbL6T0g7Eo3QfMSzH9Wl4fb086f9QkRi8zxYxzrHeseCY5cxNYq31WUWjNdUEjIE5BLHVymhxvGmxqjUi-Aj-SNM54ZdDg-nl-GE7p0rRNKLqjpvYB0bvlxCazgrudWT8BA6hEK9O_9r9DY7HVJumnb8dFvECDRJtADR1oeMcafaIRgDNc07n9r_xlTZ2gZAlW9XWHn1fVVkdTOS1_aZ4uqZrTVnmRKs6hXw6SIn-sh29-Mn-tSmQzlSkDK8cJ9IywGEG8_F87HtSOVCVxPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XwteKgnsK6SBO9nxIv_dpbZb46ZJO-4sL0FIAL0Z9ypOLF1can619R2xvxLIvIzot2EVADg34qxcw82hifHgpsKf6tMIiHM3rh7R0nTVTN9P_KI3ZPMbC9VIqTRuGsFiTfX5aHMlsEnnsdud7anFCUbaLs-mKcX_ev7E6D5ku7UQwiOC3oh0H_B1X7HYATSg3pJTE91IZU1sRNOyUMPYO2KGdeYzWbhyN0WhZatUHP4F0Riw0izPZaTQ1cumCArrb4HLCfys9qTNNc5wgWgFAMSaEWZAL3jsQrpHwvnAiPXJ1vX6B1onzm29c_06YTb7tBSDKdqrc7V4Agleqxaxww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YINQJ5XvhTMRKJ_eKZlFMiazVN62ZoisjJBC8VtfniSG3RIG9gqfhDzcuCe5iIi_l51m9uDiqupfoGcmumP-Ox1gpbyZxoyfvEf3Wf7eomKyS5eij7hxjCp_2HoF0qUAKsRrT5XDDq2y1qXjMOEdH556RR58HdjUvatz5o52qpyo1uQ9jGKeyLMDq9MRxIKljpVp61oYcVaZKfCg6g4T0b7XNAM88WRUFEyDLzhUoqbQx7RcbZPfpiPbifZR6cC2mTqcFSdMURd3YqGeIShiKbs73xC50Owhbykq8dqMbd17jo0uuDQ2luNU2vhOpQXWMX3QESQSt4On6JBhZ6NOBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YMyc5OI8cQ_qKT-LtmD0AZYmH8KFJ7xTrUR3T2mX2uEX14X03dcZ4uB_BDn6SOpOTdxplz4FWISgarN3OKhbl0kHwbpuzwnCOelX8r00xJY9THxu4GgRNJkSK4mo9uDy73E_jvxR6Np66GH8yvKz7P8Rra-0bBl9--okOhUW1XGAob3U9n2CoRi0o61JiaUiiwMNh1OAZfhbMl-hmpEl_0cYDJMYFPtVrzQrOD1wXis82cA6DC6hVmEW0qQGc7oLlAAciLe4g6G2jlmAxRx1s074ijLOgYebOvT1YFq38CFMq8HotFtdXAuJcxk0jDvXbDAhXAVd8z3lvKwBb5hpfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر هوایی حوزه هنری انقلاب اسلامی از تشییع پیکر مطهر رهبر شهید در مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/669199" target="_blank">📅 19:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669198">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e45b27eba.mp4?token=DohR5LSp0x_sPs25tw7zB3pXJHLmXff4mIxZgVPEjgD2c1vJafA30ASSO2rIdcgo6YGFNr3eg6EPg7efm20EtOHpyySjIyiOQej1eG7BubKwTLFhnRiEpiZUB2W4Yi5ooeye1s-D3ly0m8zLYVg7Ci3oIk2ASjzZb1mbR4yOuObekSwZOZxU6HFLKbj8KRYYbdBGY9GecQojuVYkWEi0cVpjoie0nriuwFionO8frmF3ku1Fm5-SpkSDeVHf4_7fv0ZBZr_5OKTbAor1cGJM7t77unBKJXl0Rn-atZOhgKzqsh-06sgRPQXMzBpDIzM2ki9dYSa0vMjle9ATwc7-dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e45b27eba.mp4?token=DohR5LSp0x_sPs25tw7zB3pXJHLmXff4mIxZgVPEjgD2c1vJafA30ASSO2rIdcgo6YGFNr3eg6EPg7efm20EtOHpyySjIyiOQej1eG7BubKwTLFhnRiEpiZUB2W4Yi5ooeye1s-D3ly0m8zLYVg7Ci3oIk2ASjzZb1mbR4yOuObekSwZOZxU6HFLKbj8KRYYbdBGY9GecQojuVYkWEi0cVpjoie0nriuwFionO8frmF3ku1Fm5-SpkSDeVHf4_7fv0ZBZr_5OKTbAor1cGJM7t77unBKJXl0Rn-atZOhgKzqsh-06sgRPQXMzBpDIzM2ki9dYSa0vMjle9ATwc7-dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محل تدفین رهبر شهید انقلاب مشخص شد  اخلاقی‌امیری، نماینده مشهد:
🔹
پیکر رهبر شهید انقلاب در رواق دارالذکر حرم مطهر امام رضا (ع) به خاک سپرده می‌شود./ تسنیم #بدرقه_یار  #اخبار_مشهد در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669198" target="_blank">📅 19:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669197">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02f558405c.mp4?token=cbnxUWGFocbhZXMu3iYqPTBD5V2_xHRZtvmfrTbfCm2UA3rnKRt455xcDTQSGN_KC8wwHNy-2-S6J6md2AHvPHSjhTEb56kEobEWc91SUG6OdV_oS9ireZNCwt-J_3Uihzum3L-68LT20Ct_7TNhC7wORJuPYbzC_jvXCduc93kBVUOD6OEjvji9bzGjUUYX8IkfxZ9ZCFSWmuXqDAlZb6qLZTd8OqjWnaN4eyIryTra-7aIecRMX2G1-R_6E5guLPuQzA6TBmFBFTnrrvpdUqgoE1Wd2eIEzI9JrYIZR8LukmMhF6_ew2WUE3k4h6NzUXk3zW6UAvQWDDjiHr2cGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02f558405c.mp4?token=cbnxUWGFocbhZXMu3iYqPTBD5V2_xHRZtvmfrTbfCm2UA3rnKRt455xcDTQSGN_KC8wwHNy-2-S6J6md2AHvPHSjhTEb56kEobEWc91SUG6OdV_oS9ireZNCwt-J_3Uihzum3L-68LT20Ct_7TNhC7wORJuPYbzC_jvXCduc93kBVUOD6OEjvji9bzGjUUYX8IkfxZ9ZCFSWmuXqDAlZb6qLZTd8OqjWnaN4eyIryTra-7aIecRMX2G1-R_6E5guLPuQzA6TBmFBFTnrrvpdUqgoE1Wd2eIEzI9JrYIZR8LukmMhF6_ew2WUE3k4h6NzUXk3zW6UAvQWDDjiHr2cGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غم‌انگیزترین اذان مغرب در فضای حرم مطهر رضوی طنین‌انداز شد</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669197" target="_blank">📅 19:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669190">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p40KYotB6buf8AwqyijQQ_vJWgPhBGdpbSY0wtZy6riq2z1KH1umzdqQu15i9RXJ6yopn9JyV7S4fgmi6I9RZ9nibt0353FspBla1PDrnBevScO9JURDZS7RDmqB3OoDJppBOSLmSwvGWKPzn1Zh1YFQjcUB7Av-WUEPuhONVCPx3v3NZ6hUO1uJj0EDr1wLSEjPb9oTZOoVjnqdzc_w2B50VcIRJZO1wtflr7RvpPlPdNTdRrFEvKKGgznA30e6vA6wTPlw9FLCOoyBG66uFRNV-XC_aN2IBook0sBsevQcgf73f7ij5bdMEZBlr37HGjl09WwpI-bWpNM-SgPgqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMKPhQX75R-u1sW7kjXiEsz0x8wzt4ZH8lKyvJ0c27Hz3hBGe7V0fBaYCYz6FicP2Tz39JQKB6I_RWqFNjcnXBbGfOUyUqgk5BK8OM6iX6U7ofrYpplMzFnFip6-eidPHXHe4ouS-9ktznytnlfJAyiAQH3lSxer1CoukLBkesWsb7WmEIbxLybEvZzSwkesWpv9sma2pdQJFbFSK6Kz4zl_uIBuzdf7PLauApbLvn44VYH4sens7SvlsXrpvgL2AwegTM1AZ30ovyPVY7LScyS_eIVbZPBPD3MaLx7urXeKVi9SrlJTELgBtPSr7mOPmMyXWcduTPmYrF9RSENplw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wm0YZTK2I7g5bDHAg63EKj7k0EudV4fNtPSObeg3NnqCFA5tnG_UIlRRtTodRtr8k-je2WOrCIGCYO-_TZVS-RNzbA-3ixHAZm22svYWLOrXAj9NI_YFUtYW3NLj9yKTmnRTfD3OOQOq-y4IvFNJxdYJWcsK-TG2-ZNLO3cAZh-HrC5dDikgs_gxaRKkeJGq1lwe4RJw2GEMQoDsgw4fyCOvaZiRFk-_ByrMQFzy-IIUWW8LGpGxdxfZTY4b0p63rUCr1eut2f8jq3IhP7gDiO4szVmQ4PNu2z9qc_SHmHnU0RCaw4455gmmowswrDaeDV1b0uJpw3CF1YVmSaTx5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VU5EyWBZM90VtzX4GsvwPjGF0SEvKfSddWpt6IEFbIchckypfoH_eqddg6dV9QnI5MibTkIs8f9946dlm3_x_j9TFW0syVCgBJT1LkPecwPmEl1SB3IzJoV40dzf_71j8QwlrOj_gZ90DPdVCn7Axko3i_Fh-2FYNdwtjFtMh5_O22wCPbR_AhLvmsK5S4eQ3aHMPiTj8JsOfU_S37f7hBBgkK0jlQf7ImUNcpHTtyd53i7BAKHZtuqzSiiBvlAKAHDAC2iaB-5MnQlJFsB7xKWokUWF1fWOf6mViZaOCc-jJJOqQE1BRs90fU-qInVii2aBgZ9moMqaKsRw1r12Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gKbKYTjTXBMp36tGGS518e0FYa8mow1F4_Bf33cXwwadHZ4LtpxfEu2GlwCVPtho6xk9Pucd_z44e46ZFMdhngXQHuiQtijzkrnj-NaaOWPEewDUq1sASx5gE6Yg7iLud1mSpNDzpZCoPO5YQaSD3HxdghYpSuyjcm0nFo1bWw-diy_6UkFezCSdeubnL3gbmN8rqt3BsXHXRd6zW7AXR-g0OBxG51-85xs3Dzxlu9vIHQaasU1qdvaQwCYoYQbHDhvvmEJdwRXIqKCrPjaDY2m-pQ-_slSz3DyVBNd662n9ezMd0AykmU-jT7Gz6ajC8qnJ5YNI7Aqux-S4RFWFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LK4OAPnLi7RE87YgaUJxiV6JppsAcizDWKF2lsKbUjEX3pTJt796XnOXV3kbsBi2Ob_5n9aJsm39k_SxIPDm64aLDmo5WbKJ56ZFUPf57j8H4d8zvaEuLTmwkmLMX4zPjzDCxS_028U5Ls4vLR8goARiLkqUPZylZQ1gvv2aZEk5iQxtsQsyM8fpWYg_pSxzjHimgJEsSwnhS4KIEhceMYGOlRZ5sHhaTFWmzI5GUvZoVvh5WLQKIKIJP9dvLmLpvRpM7sByRhGCgDHYrJW3W8w2AtBkvilKvPnhK0MxS_6PrbHetDMEwf40U0It03EfoKW1JY52lpnreCvXNgKasg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bcuvi4Po3WzPwsnGrG3qj6-Ct1kz8HCeENwPSpdh6_vAX7CmKAZdhc7F4AQMfCmVXV24JgMVu-LjJk7IIYtFQy8v3oRalW3J-9HB1s561aisxKMSLXEyKJw4KnuCsRoG1JTjpAW3qbMJz6fEpgnNvHPcBl9oyclLS3KLjxsPR4IY5jcE4AQfHlle5-SyU55LRzpz3EWgx98biZUCwF6_E4tFIVTtqsgYd1MsNFQuagdT2fsRTgbZajx7QuM18QYnFb1pKFL-BW2Yn3sKcCSNNn6WJ4l7lkva424QG6OwINi3V3VWVbxRj00elavl6vjPgcfRCo2ymUNSgssMmGM4_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دور از آن چهره که آرامشِ جانِ ما بود
روزها می‌گذرد، داغِ نبودش به‌جا بود
🔹
عاشقان رهبر شهید انقلاب امروز از سرتاسر جهان گرد هم آمدند برای وداع با یار همیشگی مظلومان عالم.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669190" target="_blank">📅 19:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669189">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdaabd462f.mp4?token=k8OsipoYTJFwd1-wNdWB4VOw0gd5iHKnfW30aJRFa860whN1SqLAv6MOfxXsPgrL_AnGd-H229nm5O7ap7GSc_LaWDvnqWhnfpaGNZ6nnA-XcoudIABSAJ11iNJwuh3qDiWNdgXOxHg7w-qw4Iz3Wmc9m39RFdLWqivDKgtwylmk_Gnx7fk8wInSpTpGULtHyko56eA8Z_Req12wWANCsQB6W3l8le6lSgH1MnzGNrZQuC95ABkluIE9iVh_z-Jd83pIWT8LWC__VLbWRkx47jKhWXpzGtbdWGZfdTwKwBLjR-laa4ghgJcj1HJCsizpvu2u5C-UIyWHt5O4hetZ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdaabd462f.mp4?token=k8OsipoYTJFwd1-wNdWB4VOw0gd5iHKnfW30aJRFa860whN1SqLAv6MOfxXsPgrL_AnGd-H229nm5O7ap7GSc_LaWDvnqWhnfpaGNZ6nnA-XcoudIABSAJ11iNJwuh3qDiWNdgXOxHg7w-qw4Iz3Wmc9m39RFdLWqivDKgtwylmk_Gnx7fk8wInSpTpGULtHyko56eA8Z_Req12wWANCsQB6W3l8le6lSgH1MnzGNrZQuC95ABkluIE9iVh_z-Jd83pIWT8LWC__VLbWRkx47jKhWXpzGtbdWGZfdTwKwBLjR-laa4ghgJcj1HJCsizpvu2u5C-UIyWHt5O4hetZ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از بالگرد حامل پیکر رهبر شهید انقلاب و خانواده ایشان #بدرقه_یار  #اخبار_مشهد در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669189" target="_blank">📅 19:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669188">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73340ecd2b.mp4?token=S7IF5K0Hp-dSdYCW4V1A9lKiALpXJIkzt06W11LhmvrZOl5mIKLLOe3DMeTrUUKd_NOhQUtBuEl8_4DFIVm5pGrxAWPYWLPW8g1Sfv51bY2S-HPHHb3ar0T3wMNOVmErHkfmPMmDloCUZqybhk9k9BXPg0g4BMs5q6cqxk3kcz1G3D8NasxWL01CBrHOXRwwK5ok2ttQ3Ncn-znV3YGex-gjshDU4Z_I3KPyQ5_a4MI4b6WVC6f24DUKlHUc3GaIViJNerKDBU_kfS1Fk6-pXB7Y0XKtj9zCD5smeWpWIpaOJlMcXZgvTwekpjTPdJ2UI7GZNp7xpO0g5KBPo7qoQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73340ecd2b.mp4?token=S7IF5K0Hp-dSdYCW4V1A9lKiALpXJIkzt06W11LhmvrZOl5mIKLLOe3DMeTrUUKd_NOhQUtBuEl8_4DFIVm5pGrxAWPYWLPW8g1Sfv51bY2S-HPHHb3ar0T3wMNOVmErHkfmPMmDloCUZqybhk9k9BXPg0g4BMs5q6cqxk3kcz1G3D8NasxWL01CBrHOXRwwK5ok2ttQ3Ncn-znV3YGex-gjshDU4Z_I3KPyQ5_a4MI4b6WVC6f24DUKlHUc3GaIViJNerKDBU_kfS1Fk6-pXB7Y0XKtj9zCD5smeWpWIpaOJlMcXZgvTwekpjTPdJ2UI7GZNp7xpO0g5KBPo7qoQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#باید_برخاست
♦️
آتش‌نشانان شهرداری مشهد با اجرای عملیات مه‌پاشی در مسیر مراسم بدرقه آقای ایران ، تلاش می‌کنند تا با کاهش گرمای هوا، فضایی مناسب‌تر و آرام‌تر برای حضور عزاداران و شرکت‌کنندگان فراهم کنند.
خدمت بی‌منت، از جنس ایثار؛ در کنار مردمی که برای بدرقه «آقای شهید ایران» آمده‌اند.
#شهرداری_مشهد
#آتش_نشانی
#مه_پاشی
#خدمت_بی_منت
#تشییع
#مشهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669188" target="_blank">📅 19:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669187">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92f15130be.mp4?token=fRVBuRpVLDfUdps6Zi50pkKx5jg4dGUp66UBhAPaWO6d5ZqKP8Szdd99a5xnoJYUbVKcT0ePxQhc6DTwlSaCQcYPGx3fKzMT_mKzoV7Bb5v2MDOMCJyJydzqgd_xxwjQDe82kkH9PBEK1E3cvQtbr5oWOjs5W1t3ARTuajdnnZZqHrPjdAque7b9gfD0ZUBzVrdfxBtWO-PIIp7C_J7m1QXV0aRhfRFWMrqA2rYzxfEFUn1z1i7s7uXdqLuCEsWphRWR8Xum0oYAsGGgYGvJN7_snYfzohNyPShNUH4019x3iGsBFSCNIAA-iB2TrVeTIzzjR0Ki3AFHr7aE8W0u8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92f15130be.mp4?token=fRVBuRpVLDfUdps6Zi50pkKx5jg4dGUp66UBhAPaWO6d5ZqKP8Szdd99a5xnoJYUbVKcT0ePxQhc6DTwlSaCQcYPGx3fKzMT_mKzoV7Bb5v2MDOMCJyJydzqgd_xxwjQDe82kkH9PBEK1E3cvQtbr5oWOjs5W1t3ARTuajdnnZZqHrPjdAque7b9gfD0ZUBzVrdfxBtWO-PIIp7C_J7m1QXV0aRhfRFWMrqA2rYzxfEFUn1z1i7s7uXdqLuCEsWphRWR8Xum0oYAsGGgYGvJN7_snYfzohNyPShNUH4019x3iGsBFSCNIAA-iB2TrVeTIzzjR0Ki3AFHr7aE8W0u8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عصر امروز؛ شعار «لبیک سیدمجتبی» مردم حاضر در مراسم تشییع حماسی پیکر رهبر شهید انقلاب در مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669187" target="_blank">📅 19:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669186">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
محل تدفین رهبر شهید انقلاب
مشخص شد
اخلاقی‌امیری، نماینده مشهد:
🔹
پیکر رهبر شهید انقلاب در رواق دارالذکر حرم مطهر امام رضا (ع) به خاک سپرده می‌شود./ تسنیم
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/669186" target="_blank">📅 19:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669185">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUnzXE82XQHUB3ucptOCclpzA2nGVgU6ZAhgJPUl3w5x8JrvVzRxVnR-7lOQWtELq8TdsElmIxZmfJ4snUI0q1sCgxyqW7_-F7LwgHfZ_f_M2-U4rlXs0JuqIQuEBkRCCySQVwRq7ljzib7pepI92t-ap192m_yiY1Fu78COqfZQF7FgeqoRRPt6M9_vhTSxECe9uLOPVqyZBty5VlC5RRn4xY8GGIfAJzqp0Thinewnmzo_VSw2nVb7Wmvx6DzHCOioHG0UNZKXWhkou8SPJ4yyqzHj78gpY1Kwp3Wz4jH6b9poy_Za_1ioMtpclpDAoS-MuuzrfUixLCD9wv9XgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یاد آن مشت‌ گره کرده...
🔹
تا ساعاتی دیگر پیکر رهبر شهید مسلمانان جهان پس از تشییع باشکوه و اقامه نماز بر پیکر ایشان در جوار مضجع مطهر امامش، حضرت شمس‌الشموس علیه‌السلام در جایگاه ابدی‌اش آرام می‌گیرد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/669185" target="_blank">📅 19:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669184">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b70f9361a5.mp4?token=NVOf9vvnWAfiO9n7VGz4VlO0wVujVo4BJypdeQU7fqcvhuXHbDCwjuwC7EMWszZqlWsFCi4tKNz0skd0_kaIq7eSNDEeYcNrSOKNKUoHWQ08cf5IhFL5mU9GcLRbADtY4k7I5lIsJ30J8rvJLLUXGlYy1NnwL0KPmeDQEn3qnxlHHxbw2OylxhI0jusnOHHhTklbB3EHIOHoA2xCYQjpY887Dq1aPp8pU0k1wfKackkH-AIr4YDGPbPLWqFYtq5k8P0cndQLuPqYW_GyN-TErx6nWJKpB6OH-3zq1UoHylMb3xrnZ02UbO_LPQ1nZH7wteXlKLlaccMYtPJeyOLd9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b70f9361a5.mp4?token=NVOf9vvnWAfiO9n7VGz4VlO0wVujVo4BJypdeQU7fqcvhuXHbDCwjuwC7EMWszZqlWsFCi4tKNz0skd0_kaIq7eSNDEeYcNrSOKNKUoHWQ08cf5IhFL5mU9GcLRbADtY4k7I5lIsJ30J8rvJLLUXGlYy1NnwL0KPmeDQEn3qnxlHHxbw2OylxhI0jusnOHHhTklbB3EHIOHoA2xCYQjpY887Dq1aPp8pU0k1wfKackkH-AIr4YDGPbPLWqFYtq5k8P0cndQLuPqYW_GyN-TErx6nWJKpB6OH-3zq1UoHylMb3xrnZ02UbO_LPQ1nZH7wteXlKLlaccMYtPJeyOLd9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از بالگرد حامل پیکر رهبر شهید انقلاب و خانواده ایشان
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/669184" target="_blank">📅 19:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669183">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8DAV_e6TEf6STvCtp9JNT5qpw3f2m2NJaeY6dbPCh-06BSz2CqE-tVUiXBCgFS8EdS69E1E0fNC6MSrF0u9fYGvhEh64B6w7w9eScJ1bpwWia5xhwsyIEIhsWeaVGvDrMJzrHbLl1LjgUHxP8GNC4GO-55W5d5pEm_fTV3KL3BjRbGHJ7Y6zTmQaZit_y3xb0XmImHsob68uSOA87XvwPV-Y6NMsaxJQrEaE6VGm7eSVuolCk4klyDsldVDjRs-JJhk7nWfAbGI9C2FK71FPFyC2K39wd1Z6kA6ftRECkehbLUedD_Rpt3iGLyXm15-RO5NYCcTITOKSo3hawEi-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در آستانه برگزاری مراسم تشییع رهبر انقلاب
🔹
تقویت زیرساخت‌های رفاهی مشهد با خرید ۱۴ کانکس سرویس بهداشتی سیار
🔹
سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی مشهد در آستانه برگزاری مراسم تشییع رهبر انقلاب، با هدف خدمت‌رسانی مطلوب به زائران و مجاوران، ظرفیت ناوگان بهداشتی شهر را با خرید و استقرار ۱۴ کانکس جدید به میزان ۷۳ چشمه افزایش داد.
🔹
به گزارش روابط عمومی سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی مشهد، در راستای آمادگی برای برگزاری مراسم تشییع رهبر انقلاب و میزبانی شایسته از زائران و مجاوران، اقدام به تجهیز و ارتقای زیرساخت‌های بهداشتی شهر شد.
🔹
با هدف مدیریت بهتر جریان جمعیت و ارتقای سطح رفاه عمومی در ایام برگزاری مراسم، ۱۴ دستگاه کانکس سرویس بهداشتی جدید با ظرفیت مجموعاً ۷۳ چشمه خریداری و جهت استقرار در نقاط استراتژیک، در اختیار معاونت محیط زیست و خدمات شهری قرار گرفت.
🔹
روابط عمومی سازمان: «با توجه به پیش‌بینی حضور گسترده شهروندان و زائران در مراسم تشییع، اولویت اصلی مدیریت شهری، تقویت زیرساخت‌های خدماتی و رفاهی است. تجهیزات خریداری شده بلافاصله جهت استقرار در نقاط پرتردد شهر، آماده بهره‌برداری شده‌اند.»
🔹
وی همچنین افزود: «این اقدام در قالب برنامه‌ریزی جامع برای تقویت شبکه خدمات شهری انجام شده است تا امکان ارائه خدماتی با کیفیت و متناسب با استانداردهای لازم برای زائران و شرکت‌کنندگان فراهم گردد.»
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/669183" target="_blank">📅 19:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669182">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d478d8f83.mp4?token=UnwxcxeSrhzAW7xeM55SeCpP1bkuLGmCUW4AZ9OY0kza_ZC3dzEBOXXTlArkZFr3VIoeEJZcTZjE2BY6CocB3tCg-hpY15pOsV0i2g9jcPgJ3LM4_xQd2K-TxLeh0nwqTPsWm010Lp53OCDZaO78p-h5Q9FzPpNqNc7s1vMb5hDreQbNWBHRCS_lAzDVBUgdIec28V-KAlW_2-yt8stijvQQTGuANZeD3gaCQs6MYDLWJQt7zlY1bvM6C1dXSW4Q-07ezfD6_6lZTMEsXbaX2bo8t68en47xg-3ssfGykL0AIwp5Ey75RMmBA6zZHPHeJiGkiI1cbmEIMXVpktWOkx4vMM56tQbZKno6ziWz9kq5jTvNyxHJDLWnUOsbiyKJS7dcB8og52LDIwkFYR3fwlWLCMbG6RDRNjGucmppxVL73VF4h1KWdrCvjCYSKazg713OXEdJ5tCZbUYUqMdTaxGQtrSjmWif95m1UR6rIbBDFCs9Us084CmyD1Mn3xgJ8n7t9an8Hrp4NZTB_5uJaEImY8xz1B4a8DebjoEgfBGMdWTSRFaohoJ5YPIWgyVMwO7fyyRYR4QYmtHwHk4AzrKEItE1kuDx505CTzYQaDU0CdN8Ho7ECtH0qlpjDgR_YhuTixEGiOEs0Nv56IYM4E_5cdnVEXZgJ2JgMomCtpc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d478d8f83.mp4?token=UnwxcxeSrhzAW7xeM55SeCpP1bkuLGmCUW4AZ9OY0kza_ZC3dzEBOXXTlArkZFr3VIoeEJZcTZjE2BY6CocB3tCg-hpY15pOsV0i2g9jcPgJ3LM4_xQd2K-TxLeh0nwqTPsWm010Lp53OCDZaO78p-h5Q9FzPpNqNc7s1vMb5hDreQbNWBHRCS_lAzDVBUgdIec28V-KAlW_2-yt8stijvQQTGuANZeD3gaCQs6MYDLWJQt7zlY1bvM6C1dXSW4Q-07ezfD6_6lZTMEsXbaX2bo8t68en47xg-3ssfGykL0AIwp5Ey75RMmBA6zZHPHeJiGkiI1cbmEIMXVpktWOkx4vMM56tQbZKno6ziWz9kq5jTvNyxHJDLWnUOsbiyKJS7dcB8og52LDIwkFYR3fwlWLCMbG6RDRNjGucmppxVL73VF4h1KWdrCvjCYSKazg713OXEdJ5tCZbUYUqMdTaxGQtrSjmWif95m1UR6rIbBDFCs9Us084CmyD1Mn3xgJ8n7t9an8Hrp4NZTB_5uJaEImY8xz1B4a8DebjoEgfBGMdWTSRFaohoJ5YPIWgyVMwO7fyyRYR4QYmtHwHk4AzrKEItE1kuDx505CTzYQaDU0CdN8Ho7ECtH0qlpjDgR_YhuTixEGiOEs0Nv56IYM4E_5cdnVEXZgJ2JgMomCtpc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهدی رسولی خطاب به ترامپ قمارباز: بر هر مسلمانی واجب است که هر کجای عالم باشد جان تورا بگیرد!
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669182" target="_blank">📅 19:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669181">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8f39a9e38.mp4?token=g_8yvffr9p80ts_pOj2skq_uyMnE8huE_PY52eGjxvDDT_bITTFVpgA8ZR3JAhdN91-CIsEGtDaGUxAWzqZMYWxMklSsISF5mT4_XezlymlN9ZpilzTJGFX55Z871tug-7AHTYvf7QFUXj-JbvP1qnzy1T87rLwjn_7aDwzi9Y59OLh42Vule4ROPISxtjiufQvNiP5b_gbPxYBvzNNS28it-njydv5-7gxTLMvZy_QapHObGSBD41n8XbEN4ZHZpMqvuRQJRqN9KlRzFwg2b2EECv6AS1ubC2fyOXtkZg9uhhx4XQ7ooGCRq6mQOXAYCp4w1rOHgYalOwfQWI8oRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8f39a9e38.mp4?token=g_8yvffr9p80ts_pOj2skq_uyMnE8huE_PY52eGjxvDDT_bITTFVpgA8ZR3JAhdN91-CIsEGtDaGUxAWzqZMYWxMklSsISF5mT4_XezlymlN9ZpilzTJGFX55Z871tug-7AHTYvf7QFUXj-JbvP1qnzy1T87rLwjn_7aDwzi9Y59OLh42Vule4ROPISxtjiufQvNiP5b_gbPxYBvzNNS28it-njydv5-7gxTLMvZy_QapHObGSBD41n8XbEN4ZHZpMqvuRQJRqN9KlRzFwg2b2EECv6AS1ubC2fyOXtkZg9uhhx4XQ7ooGCRq6mQOXAYCp4w1rOHgYalOwfQWI8oRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انبوه جمعیت در کوچه‌های منتهی به خیابان امام رضا(ع)
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669181" target="_blank">📅 19:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669180">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe9d8d360.mp4?token=MqYRzPL2e0Or4YIpRLA0pAK6gEe2qYED0nUuHFdhdheT-TtNbQDOqtgBBhQ2Bp2GuVwDSurAHfD6uiu4FzgHEeYsrW5hcwsGKBtXkh0wm50u6qsIjMVURqFCzxcqOs7EvjyGRVSa13PrvZi2y3qYFfT-aYvUwzGMPo-ZOq9snOk9_3-5vgFfuTTWOhi1yMRJyGgzC5fwM08-Assy06joLkA0WdLLoMzsoeyOrxH25XUvjk8YnySkgIzZCW5Q40wTyvidUcm74FhfA6ff61rsIc1bYz_fTaHR2sWYJjDydqY_W-PWv6Fm7KhKsPF_niDxwfce2XufNmfKVO10PKydYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe9d8d360.mp4?token=MqYRzPL2e0Or4YIpRLA0pAK6gEe2qYED0nUuHFdhdheT-TtNbQDOqtgBBhQ2Bp2GuVwDSurAHfD6uiu4FzgHEeYsrW5hcwsGKBtXkh0wm50u6qsIjMVURqFCzxcqOs7EvjyGRVSa13PrvZi2y3qYFfT-aYvUwzGMPo-ZOq9snOk9_3-5vgFfuTTWOhi1yMRJyGgzC5fwM08-Assy06joLkA0WdLLoMzsoeyOrxH25XUvjk8YnySkgIzZCW5Q40wTyvidUcm74FhfA6ff61rsIc1bYz_fTaHR2sWYJjDydqY_W-PWv6Fm7KhKsPF_niDxwfce2XufNmfKVO10PKydYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر خراسانی شهید به خراسان بازگشت
🔹
عزاداری مشهدی‌ها در کنار پیکر رهبر شهید انقلاب.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669180" target="_blank">📅 19:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669179">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f71ba4f091.mp4?token=DxmHhvALw_XAz9oBlR6QdrblOStAXvlE4ESvUrWluymk0RytcCSXuKK_473-k_HH1UVbNhgWhvv-rI9HUvhAVLmVIpklMAqjyjh9-dq6hs4t6fOUMbc-t9RPApmeZ7tYqTTKHeg_G0hpigcZj2KyZFYN2LvQR1Vtp9SrpJ7JCGyFRAOAfIjn3j_tO9y_ub5unXbN5fVgE4T8WpHkGmvpW-tBTljT-aL2T76WXOMhOSd8znHzt9KLgIDp9rF9HcvQX49IohCf8PbdtBOptXB_Pgf62NF-NgaAD_L3fyhDbUnamvtQq9cs1EJDlx_gzVM8_ZBVVxwV1S5c2tl07HlquQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f71ba4f091.mp4?token=DxmHhvALw_XAz9oBlR6QdrblOStAXvlE4ESvUrWluymk0RytcCSXuKK_473-k_HH1UVbNhgWhvv-rI9HUvhAVLmVIpklMAqjyjh9-dq6hs4t6fOUMbc-t9RPApmeZ7tYqTTKHeg_G0hpigcZj2KyZFYN2LvQR1Vtp9SrpJ7JCGyFRAOAfIjn3j_tO9y_ub5unXbN5fVgE4T8WpHkGmvpW-tBTljT-aL2T76WXOMhOSd8znHzt9KLgIDp9rF9HcvQX49IohCf8PbdtBOptXB_Pgf62NF-NgaAD_L3fyhDbUnamvtQq9cs1EJDlx_gzVM8_ZBVVxwV1S5c2tl07HlquQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار مردم در حرم امام رضا(ع): نه سازش، نه تسلیم، انتقام انتقام
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669179" target="_blank">📅 19:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669178">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpWty56P3-FUpDh3uQr7R8n8pIwjwLQJHETxk276k6ArOFEttycuHP7YI4hWw6OM5Kk7lQ55JZ8LTsDcHob6JApmq7LnR_yrSmlbofxVgkzRTe97ecSy_PcVY4knb-YGwTl_FM8QEyuPfTJ1ZoofyNEH2rE9rDXf5d-vw78I3Y_2NXZdPinzfL_mFdO1PyOT5EITl4_UdWPyFWZi3IuWjpr1619pbsyEXid6CbLMd0yd3RLgCXJKchy4McfDNUq5WQDEPgdyMzwahiXx75ZqqqT8ZWojqMtNod7pbVoZgCkG1CKXXeP9PUCEIm7Dx-5lPAzn2YXRQeKdD2AETY78Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرچم بلند مردم عزادار برای انتقام از ترامپ قاتل در تشییع پیکر مطهر رهبر شهید انقلاب اسلامی در خیابان امام رضا علیه‌السلام سمت حرم مطهر رضوی
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669178" target="_blank">📅 19:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669177">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd37352e92.mp4?token=DQdooLJsw0JRvMKSK6lw7PJb1Q5Ct6YD80hiRUKfCyZXo84ISbATOl54hGeGH8pdknGdlJrLiYdRz7PepXG2eMgvrXC6K3y1SK67kl4t0QdTYcfo0DxEm0ERQyEy9V3JULaRNOyvcNb8XqHXBd6H3hoBktGk1l-8d3g2amQDzLJi1VOA4do-_x6sVfGBVomNOxnHLomBpb_lrnVhzZET9-s_IVhSWx88fSrjt-ZB8OPF0TBAky6qNVCLE3IJLA4bwe-Xfo9bG3LLO-IVi_k0QuR4mrAl4Or3AA_ZPej6ocgSdpLfOxupRnQDibrxbAiRuU41kHxytHe8BztRwt3UjjWeBB77V8BCjDmS7pbd0O50XZCFPZnHdQmo2KmaRgrCmNWAWbZyqSbIdLN_NzC8THrTPMRq5vMIaqugNOtCP7pZzpL2JmFUWijgG8WqKiYOrO5gmNCtMUfcmvT35lK70dWlQcJaiupu9m0wW4fkYEArTvI_VopkXESnSdLnC3iOBzWwOE2vJ8R-oJvgN945Zk77P1UTionWVJ0uK-vaKc-6UeAfdVDMSzYYXJtIQDIJ1Hpo-II97NQf6zUa3R8N19jJ7TZKWu6LHLuEbyedEyjPI6pHgEDBSW1xfSuRpnsYgVSEIi-ES2GaEixOLJozXLJ9jhiVnhikDN7gAU2kdeU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd37352e92.mp4?token=DQdooLJsw0JRvMKSK6lw7PJb1Q5Ct6YD80hiRUKfCyZXo84ISbATOl54hGeGH8pdknGdlJrLiYdRz7PepXG2eMgvrXC6K3y1SK67kl4t0QdTYcfo0DxEm0ERQyEy9V3JULaRNOyvcNb8XqHXBd6H3hoBktGk1l-8d3g2amQDzLJi1VOA4do-_x6sVfGBVomNOxnHLomBpb_lrnVhzZET9-s_IVhSWx88fSrjt-ZB8OPF0TBAky6qNVCLE3IJLA4bwe-Xfo9bG3LLO-IVi_k0QuR4mrAl4Or3AA_ZPej6ocgSdpLfOxupRnQDibrxbAiRuU41kHxytHe8BztRwt3UjjWeBB77V8BCjDmS7pbd0O50XZCFPZnHdQmo2KmaRgrCmNWAWbZyqSbIdLN_NzC8THrTPMRq5vMIaqugNOtCP7pZzpL2JmFUWijgG8WqKiYOrO5gmNCtMUfcmvT35lK70dWlQcJaiupu9m0wW4fkYEArTvI_VopkXESnSdLnC3iOBzWwOE2vJ8R-oJvgN945Zk77P1UTionWVJ0uK-vaKc-6UeAfdVDMSzYYXJtIQDIJ1Hpo-II97NQf6zUa3R8N19jJ7TZKWu6LHLuEbyedEyjPI6pHgEDBSW1xfSuRpnsYgVSEIi-ES2GaEixOLJozXLJ9jhiVnhikDN7gAU2kdeU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#باید_برخاست
♦️
آتش پاد امیر حسامی مدیرعامل سازمان آتش‌نشانی مشهد: در اوج گرمای هوا، آتش‌نشانان مشهد با بهره‌گیری از توربوفن‌های تخصصی، مسیر تشییع رهبر شهید ایران را خنک‌سازی کردند تا زائران و عزاداران با آرامش و ایمنی بیشتری در این حماسه ماندگار حضور یابند.
خدمت بی‌وقفه، ایمنی پایدار و همراهی تا آخرین لحظه...
#شهرداری_مشهد
#جهان_شهر_برکت_و_کرامت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669177" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669176">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3BIZMDCC6p_0lGtjsAB29TQ8HbAEnVahQ4r0spUbxLA93PGkU9wMY8g5sVc_z8Dc-_v1bFrdRGtfDWqK_zkOJMgb4rEn_5EFdfEX2GUKtfPPT8_7KRn7aXphCioVudgxfi4Gy9iPundFEDFPIBTm0vjkMuc5pUYFgLeXxUq48mnknVuWkpykWj2eJnFuPpILvq8_8ZNakdWg1Mpef3QS34zkGilyHG7IxrJiQbrb3a70SaohbEY1YKrOCVoKVJTM6TVwCa-pLVa_kEJZxGYt0ygUk1kPcCIg0Vy-PTVADx2DQnmZu7FfsjntDYQaBN13q_gdUcZHPK7azHpqpM9LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تداوم بازگشت خدمات بانک ملی ایران؛ فعال‌سازی خدمات جدید در سامانه بام و شبکه چک
🔹
بانک ملی ایران از تداوم روند بازگشت خدمات بانکی خبر داد و اعلام کرد، مجموعه‌ای از خدمات جدید برای مشتریان فعال شده است.
🔹
بر اساس اعلام این بانک، واریز سود سپرده‌های بلندمدت، امکان مشاهده مانده حساب در سامانه «بام»، فعال‌سازی سامانه چکاوک، رفع محدودیت مبلغ استفاده از رمز دوم ثابت، صدور کارت جدید برای حساب‌های واجد شرایط، انتقال وجه از حساب‌های فاقد کارت در سامانه بام، امکان مشاهده صورت‌حساب در بام و شعب (از ۱۱ تیر) و همچنین وصول چک‌های صادره بانک ملی ایران در صورت وجود موجودی کافی، از جمله خدماتی است که به چرخه ارائه خدمات بازگشته است.
🔹
بانک ملی ایران تأکید کرده است روند بازگشت سایر خدمات نیز به‌صورت تدریجی ادامه خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669176" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669175">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
چه زمانی امکان زیارت مزار رهبر شهید انقلاب فراهم می‌شود؟
استاندار خراسان‌رضوی:
🔹
امیدواریم از فردا حوالی ساعت ۱۰ تا ۱۱ صبح محدودیت‌های حرم برداشته شود و زائران بتوانند به زیارت مشرف شوند.
🔹
به نظر می‌رسد از ظهر جمعه، مقدمات زیارت مردم از محل تدفین فراهم شود.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669175" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669174">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPiPoQ02vILuWVzHWcQ05Rwzoac4rmYgAdTmmivV_OCeZ4pScELBerciRotW6orXum7HWZDdP-wvr3I-Dhlm6W3BNO0dNXzIKl4q9_LE65f548i-TgyvBYm6mh_xJfHv1PXy99ks6f-7F9qm1_9j8KbQElo4fvKcwD4skpMHCfzzLre3U2-UdIER909Ypwkk7E2_wFrywypC3VX3jn63UOwKqfkDI2mKawQzQ7MUwFfktHOSlUxCnxU8lYx3ZxBoPVwidgCituXgfjm9xJlKNP8m4FMsLyVXnTcAJsJY2TL81rbahY04yoUnKMPyl8A98VbQeJa2HjbQAhTHqKz9Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/669174" target="_blank">📅 19:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669173">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
با
توجه به ازدحام جمعیت در حدفاصل چهارراه دانش تا حرم مطهر رضوی، ادامهٔ انتقال پیکر به صورت هوایی به حرم مطهر انجام خواهد شد و نماز در حرم مطهر و خیابان‌های طبرسی، شیرازی و نواب‌صفوی اقامه خواهد شد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/669173" target="_blank">📅 19:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669170">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ff6662941.mp4?token=GqgXTGmPguaKDmxocrweaW42_ZdlDWeJ_UmeBMAYDFlreCu3V_S35fygg-aIFHvqnk-OcrDtaZGUi2_yq-poseCOIMl4Qn82rCBOablxaD9F9t2X4FVCWIKOwiBymHmPTIb1SnHMqDAS33OxuNbZL32Pt1ltJ1bSjarxUYqGo2NhZo-x4LWl3f3TiJHV-ZWejaiUItc9IT_Qyh9s5WVk-nyIUsmzH9kOLp1PgHXzcTL5xgFE3QonHUM6H3Y4uzrIepXkh9I2TAugBSx4eRwn8ISRGGtnnvKbLAHuBt0aHVBSTlI9xOAlXqGAwqoEyPr0tf9fOJt1tFITNoB3Rjiiooi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ff6662941.mp4?token=GqgXTGmPguaKDmxocrweaW42_ZdlDWeJ_UmeBMAYDFlreCu3V_S35fygg-aIFHvqnk-OcrDtaZGUi2_yq-poseCOIMl4Qn82rCBOablxaD9F9t2X4FVCWIKOwiBymHmPTIb1SnHMqDAS33OxuNbZL32Pt1ltJ1bSjarxUYqGo2NhZo-x4LWl3f3TiJHV-ZWejaiUItc9IT_Qyh9s5WVk-nyIUsmzH9kOLp1PgHXzcTL5xgFE3QonHUM6H3Y4uzrIepXkh9I2TAugBSx4eRwn8ISRGGtnnvKbLAHuBt0aHVBSTlI9xOAlXqGAwqoEyPr0tf9fOJt1tFITNoB3Rjiiooi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از ماشین حامل پیکر رهبر شهید انقلاب بین جمعیت عاشق در خیابان منتهی به حرم امام رضا(ع)
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669170" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669169">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtoMqk8biINUm7TsdJA_GI6EAFQxcreqPzcy7e_kF9spbXrdKl0MpZeYqpUbea8Ft8w6wBIuEMBBQI0xYSThvflPaPM-m0cxpNLTvj_Y2MaLadItuf2BW1yUnNbTM-YcfbPxfl_FN1uPHglTsh8bLbjynTY6NOzcevIUDI2VkRgIDfLN57N_tObp7I7bWhuXLhBrLHHhTh0cOr8ikvWDoxi8oSJ4BrR0al7Qa3aBip7HNetcxQYeeZROgOZ4Y3cune1lRFzvrUBvpbT3h2jc3-9MKAoKQKS5pQRLCaz8y2X2xYBh1Ugu6GB27VWkz5MEkRQl6-eJAv3_wQ4PIAWIbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجتماع بزرگ مردم مشهد در مراسم عزاداری شام غریبان قائد امت و شب شهادت امام سجاد(ع)
▪️
با کلام : حجت الاسلام برمایی
▪️
با حضور : دکتر سعید عزیزی
▪️
با شعرخوانی : محمد رسولی
▪️
با نوای: حاج سید رضا نریمانی و کربلایی علی اکبر حائری
▪️
با اجرای :  امیر مهدی باقری
📅
پنجشنبه ۱۸ تیرماه
⏰
ساعت ۲۲:۳۰
📍
مشهد مقدس، چهارراه احمدآباد
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669169" target="_blank">📅 18:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669168">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
گزافه‌گویی‌ تکراری نتانیاهو: در جنوب لبنان می‌مانیم / ایران نباید به سلاح هسته‌ای دست یابد
بنیامین نتانیاهو:
🔹
ارتش این رژیم تا زمان نیاز در «کمربند امنیتی» جنوب لبنان باقی خواهد ماند.
🔹
او با بیان اینکه جنگ پایان نیافته و چالش‌های جدیدی پیش‌رو است، مدعی شد ایران ضربه سختی خورده و اسرائیل اجازه نخواهد داد تهران با توافق یا بدون آن، به سلاح هسته‌ای دست یابد./ خبرفوری
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669168" target="_blank">📅 18:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669167">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba7fc0f1e5.mp4?token=mTSUe85zhw4t6lCCDSu2roWMiKLOaVZPNbb63d5TIxUDO_Yi99VdJtMgarfnS95CpZfz3elmHHOma6P6kSaatoIhrw2nYs6M_8tUJFDLIPjZctSqsLKfLj76LpQUfb_h-efnpgn2nQhGcBwd2RQWW0QaFU9SVfnAX2I11wV2OIYJBeHGVOf8ndmeYXQxLKGcfVIy6C2Q5VAOCqOQmT5KjwkDMZQcuujtKIZlw6qmow4BC-WyWVkk8RgWqlP7MEU_KCovG8u6f7vRo0Grnp-UDwXE2NuWKhc1uxLOLv_Y_EJI7Q4hoEshAzrc1YsgSKcmYxC2ojmPreK0AW6Hhs1YNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba7fc0f1e5.mp4?token=mTSUe85zhw4t6lCCDSu2roWMiKLOaVZPNbb63d5TIxUDO_Yi99VdJtMgarfnS95CpZfz3elmHHOma6P6kSaatoIhrw2nYs6M_8tUJFDLIPjZctSqsLKfLj76LpQUfb_h-efnpgn2nQhGcBwd2RQWW0QaFU9SVfnAX2I11wV2OIYJBeHGVOf8ndmeYXQxLKGcfVIy6C2Q5VAOCqOQmT5KjwkDMZQcuujtKIZlw6qmow4BC-WyWVkk8RgWqlP7MEU_KCovG8u6f7vRo0Grnp-UDwXE2NuWKhc1uxLOLv_Y_EJI7Q4hoEshAzrc1YsgSKcmYxC2ojmPreK0AW6Hhs1YNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع نمادین رهبر ازاده‌گان جهان در کارگیل ھند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669167" target="_blank">📅 18:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669166">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
تماس تلفنی عراقچی و عاصم منیر/ وزیر خارجه به فرمانده ارتش پاکستان: ایران قاطعانه مقابل هرگونه ماجراجویی آمریکا می‌ایستد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/669166" target="_blank">📅 18:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669165">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/322f70a346.mp4?token=RDd_oCLWoI7xkeY3ytUS9fuCs7OeISkPiw5O_HF8aNvBU8o-tEoVsu94Qh5xWure3YFdeOM2xN6O4BcN6w6sFMUeeYSOpNa3WxUaCQ5RYPYvbxxOF3D8qLsGjAS9I42ETHZ536zom93uvCR47-RQcuKiIzSjkGUl2L7RqmXsyWSN_ihzy2yzv5Lh-PA_2CpSrw_6s5tNCXbnirhHDDtC_oj4g_mA0InH5yV-ai99W_d1c2wcA6TfQBhwMkzTEcDhXPu18lUSG_4rexFGb34ILKUEnQFxPSWOslc0TJ1TxdQWUHjJTRHJHKcxks8NQQYhjJNMTxjNo7gifK8ZvQI0hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/322f70a346.mp4?token=RDd_oCLWoI7xkeY3ytUS9fuCs7OeISkPiw5O_HF8aNvBU8o-tEoVsu94Qh5xWure3YFdeOM2xN6O4BcN6w6sFMUeeYSOpNa3WxUaCQ5RYPYvbxxOF3D8qLsGjAS9I42ETHZ536zom93uvCR47-RQcuKiIzSjkGUl2L7RqmXsyWSN_ihzy2yzv5Lh-PA_2CpSrw_6s5tNCXbnirhHDDtC_oj4g_mA0InH5yV-ai99W_d1c2wcA6TfQBhwMkzTEcDhXPu18lUSG_4rexFGb34ILKUEnQFxPSWOslc0TJ1TxdQWUHjJTRHJHKcxks8NQQYhjJNMTxjNo7gifK8ZvQI0hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرم رضوی، شاهد وداع تاریخی با رهبر مسلمانان جهان
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/669165" target="_blank">📅 18:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669164">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdobPnnZF66LLGlU2BcaUDVlryA3P5bgALn1Zv7z9o4fv9u-Cksdq-niNCg5d8ccazfBHbyO0QlX0JzuZORKF2amSXiV93g3jMt5mj4RSyYjASHk_1fCs7K3VzbYKjjO0deHXn6WfRLMXoS1pNfcLDsN_vct5BydwckC7RDn2c4siGfYbhiOsl7PLPkLIYJD_njF9bHx2KfvWVDymK0ejpyZKocXpFDefJUrN65MYO_BHPjeOh-qtJsGeAvlF4V-LEPmjN4zDKWX3KChMG8c9jqZnv_PpfghpOvH3Jdi5wjyjOyMHUizOVd0gVOY5on0dF4Hg6mSfSmZITXISDQ5xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماز شب اول قبر رهبر شهید انقلاب
#بدرقه_یار
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669164" target="_blank">📅 18:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669158">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUKWkKEK1eP34sIhIHnjEZ1EKqDMiFbHlSST87GHNp4jgqZl5yK76kMlV_8-BO-SGGw0LRKqNW0oZDWLspd-TcWhac1z3IpA_9iCA6xhnyyzTKslRNXMPvVOsSbq36vFwCdv231cenkVTBDELnTirE_5Sc6oW_cB5_qOuJ_5Mrq8kc0LvpQBT7llpcGy92oiVNSZvBwPnX6IgvBkM4ZiBzODgSRNV7D8IqSyrMJCBWMCB-uIUyv9f2xpediKScZL_s_dnMrfhvXfQ291K-QG4HwO54QleI3NP439h72m0OFQdR9RKz_mbMAZgmyD7RDr7T7hnjZ8BxKEal7YBhHI3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVpnL6utaQe3yQL6piooyo2i0JmAyQ334AlMV_aevuSO9qjlEFa8NFMTABqRBYhhsLLVFZhhGYz7raLpsW2jhNAYkKqUYQfrJqmrk-yEdmLcMVynJj3O9hkYqHwQZwjGkSYNaioKhRus6N7pk11EJrRBZ9oZTuNGF4Plu7fBPazQRuHT4QOzsihVPm-flSnOrnMrXnD8yd8qTmfNzFp_HvNuoccHWRzuILgWqxt8S8NTP-IqrDWVxWS6wHSVH50lLOgbqYTnXjc40As5aS8UY07ZhLeL2p20CCjqXQcbbESUt7_pTF2k194kB_fMNHuV3TDMylyy6dsKP3M5rP3wCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PndKzRv1xuNMhVXz-WhCV5ajht2IilyPaIDahj8yfWq4xATnCCfmo8AFYdgAOb9uQtWshd2-naAJApI6fGx32VnmK_yE80Cw2WV_nFfe9IVi3tEgU_79WMrjytCdV0R2pH5k7MtnfFRucuLx-D45BEwsxVZFL7c_5aupYhWaLvwOKl988glV0V7rHKq8Lvpqq29P2PEOQpq7TP3tzAozbtScfsSHs1YF0tMRFyiJEubmFp5rEfvBYXK6kmiUAG0KpkmoUEemhq3MopoSwLgGxkSOZoiiJ4drLTjcfqpQQfCsGDEFb9ycP4whBavzvTSKYiaC4ju0XsF11uxM7Tv85Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQW0RU9TIFBlCLsOW_RTFioEvDlGB9ekIDD2TXLj1S9-rKgN0GLBcK8D45IJk3Z2m3jImXxuE2qf77X4SplVqKXKFtDh3DYbn1-JPIeeH-qCyTqrFxOpLVkUwi6kwFxOiOhIbW8AJeNhO9kwsxKBJZaaym2bpixTReRSXr-2VguVNzIHk5SRcPGHdd4HQ-gVndciMu-ET-jn5EAwiRxwuflWCqPFUDgab4Jzx5QHRQr0qeigb59hzTIIVRwMZ5Gw4DYNgPmNutZNo9a1wCGzd6c9b4VJCrNNzaCD9g7-9N2Sqfb4H6kOd4lTXzovULEg8o-11Rl-O9ieW9lJUewqfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GhgjEsjU7Xf76o6hIx5Jvp-6BYBbiANJPPbz5idzJE456AKUdfptlQovhg8GLtq1diRo_6KwdMtONki5Q-wqVQb_48ncOoaL98Q64ma7eEhqtR4qCrHTYKe2YEBydX5IYZGqHNNZa4yE9HjRZx1VVn19aAkmW1ppPw_HJAZ1GOTKidrfWlcoCwPzSbbBqsNAId0ZZ9widjAN7CVoZoJP9OaaOjkbTQ6HzFnPrexOdouS_IwSdkFcvwMSNQbwnhLsBAFiYM_zG0pOWr6o5qWrtrLgRfjcU2E32J_OBNMooqMgF69rSRmMIBh3YQ6sr2Gfm7_bskEFS5njO-b1dd49og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKXTPMAhlm8Y06-wjz1dqJ_1h-lbOJ8p3sRjJz6KLsX8rydZB2foZ1KBHmO8d_MJCLfamqdltx9X1j-F2X4v07ZkSIBIkvSNjBjBc5AZwkSD_lSAD7ztCq8nzYmqbED7z0ODqi1RF8Ysbj2stFe3WZdWYmhax-U9J4u6AgdWNzzPEDLUqgunQpk5TzoDw1pJuUGPl03iNrAE9VN-0hax1RIgjzA3iLDDA04ByYWC43mH_RXKM8v80TmEicVQ9zW1h1tSWSPI-NAKx0ilsVl6mohjbDxiHlOPp3ayFJK4SGmPj-7QuW3livIdEEauqRwHuCXxFCqcSSuwmBugpxI23Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دریای پرچم‌های سرخ؛ تصاویر خبرفوری از حضور ۸ میلیون نفری در تشییع رهبر مسلمانان جهان در مشهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669158" target="_blank">📅 18:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669157">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luLaHjX-1dCBECdTEahglOKtDYw1XU3JPztwmDQN56iSgB7EaadtTqZ3_gFkzaSvbVTlM_Pwb_RTgWsflDN5ewfeJ0CHiNL2OyfbIAve-KKSfwhtw9915IsWqTO70_Qbx2T3QNzanbIZNvtW7WJIWmcA6Ew7xWUsRAr6S_wDwOdhTKdPpYhOO7x8tNbBTOmRcpVuLxizaLSJTuSn2Wy9nDJIa17jMWz46Q3YycWUTb0Zy6BPrNweUMTCHZIcIh06Hy2IQkjSx5ldOAG6SCwQ7BNYmWf2IuCTm6iUgr-0_em4-Lr0sgtu1haECJNZDzo8Ao3uGFHifM2P-2wBEUCBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری پروفسور امیرحسین سام، رئیس دانشکده پزشکی امپریال کالج لندن برای ابرمرد شهید تاریخ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669157" target="_blank">📅 18:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669156">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
خروج خودروی حامل پیکر رهبر شهید از مسیر اصلی
🔹
دقایقی پیش خودروی حامل پیکر رهبر شهید انقلاب از مسیر اصلی تشییع خارج شد تا طبق برنامه، جهت برگزاری مراسم نماز به حرم مطهر رضوی منتقل شود.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669156" target="_blank">📅 18:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669155">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/669eb50532.mp4?token=qn8ZYyFkiMRLH8MIub9Lvjn-6edEQE9WPzm38V69ZOOEaS_kPh_soQHFgf8pliiDbon27p1rKJE9lZMA3hNF6WUklUgIJp7obumGinMTMqpI2_9xnxO38QtX-X8nNZalnMzrQcbFqE26c5savrTJt59FPihyC02RjIbltuYIhXjalUsGjiIoR6pmIV_VOLyteNHtstQGYNO2R5oaZp4KoyNSvOeAxDtocwG7RMD_v9hFRqm0jLz37LS038sI2lDM2FY4JVYayMduKjkqx2EeG5yBNmcuGXTVWUluXyqWUd_QUI_4n-phtS8CJzEIjkyf1jI8TnxPo3IA8tDRf218rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/669eb50532.mp4?token=qn8ZYyFkiMRLH8MIub9Lvjn-6edEQE9WPzm38V69ZOOEaS_kPh_soQHFgf8pliiDbon27p1rKJE9lZMA3hNF6WUklUgIJp7obumGinMTMqpI2_9xnxO38QtX-X8nNZalnMzrQcbFqE26c5savrTJt59FPihyC02RjIbltuYIhXjalUsGjiIoR6pmIV_VOLyteNHtstQGYNO2R5oaZp4KoyNSvOeAxDtocwG7RMD_v9hFRqm0jLz37LS038sI2lDM2FY4JVYayMduKjkqx2EeG5yBNmcuGXTVWUluXyqWUd_QUI_4n-phtS8CJzEIjkyf1jI8TnxPo3IA8tDRf218rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ قاب متفاوت هوایی از تشییع پیکر مطهر رهبر شهید انقلاب در مشهد مقدس. ۱۴۰۵/۰۴/۱۸
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669155" target="_blank">📅 18:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669154">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e31b4d9e.mp4?token=LKBn4loU7HBVIf9XmzNtGdptiN2HymlXecvfJ3iEOFsbKO8HzfgfBKe1xSS8eIWlVnQ01P7j7SKrU87P7WP2iPKnbK-H3UL3LWs0VtmBTZcrf_nJqOL4NCIiFahTjiRncXwOW-gKuI9bsNb8Dl1Qvgn-QnGHY3rhFgZGGHiIl3fQFKgGn8MOiLtb1YULUxr4hSk8rWFXv9J2aRK4e2UTrFAWWwggClfFBCQNNqW-BflkL5E7L1qG_1AnF5U5EIMmx3_33BTIN1iLFIpJr1OV8Pb0DnrPBQ7dfLYd3L4AllRSQYgujfz1ju6svq-mak-rUFHy8awN3eHmPlG7_t8rQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e31b4d9e.mp4?token=LKBn4loU7HBVIf9XmzNtGdptiN2HymlXecvfJ3iEOFsbKO8HzfgfBKe1xSS8eIWlVnQ01P7j7SKrU87P7WP2iPKnbK-H3UL3LWs0VtmBTZcrf_nJqOL4NCIiFahTjiRncXwOW-gKuI9bsNb8Dl1Qvgn-QnGHY3rhFgZGGHiIl3fQFKgGn8MOiLtb1YULUxr4hSk8rWFXv9J2aRK4e2UTrFAWWwggClfFBCQNNqW-BflkL5E7L1qG_1AnF5U5EIMmx3_33BTIN1iLFIpJr1OV8Pb0DnrPBQ7dfLYd3L4AllRSQYgujfz1ju6svq-mak-rUFHy8awN3eHmPlG7_t8rQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قاب هوایی از تشییع پیکر رهبر شهید انقلاب در مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669154" target="_blank">📅 18:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669153">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/195706b1a7.mp4?token=DJtZuAgqW3t43vEOF4z-WDuILnVIOuVjsCsghpzLawTgRfK-nJNkPMyJVsJEpo7Pe7ZZaesaM0JSZDOCpJpH7lGREGmTDjqjTRfT0gGTBwv1ZX527TV1Qo9G_KF-WHGdGADYNMJ7175v6ONX0bs2OYKuhayes6uOYpi5zJlM6BdR0s0x6AT-c9IQjl5lrcr03TRfPr2ORwAH_Cgm5QrPMOzmnmV1gab2h9ORMl3HWcCS8R_No3DFfHrJMQUQBrZviNFykWeL9RGiYOmMnBu5AayoG9iAefFsYdnZVmCs5o7Y1-K7yt0rk8wPv7zc8-W2Z96dfcbcjmT5qjQ0N5bSQ6TslRLVyPTnNVJixHJ-7NNlb5CjN2WVAYqu8dB4QmlBBShXD8mrGWN7b-vh2rcD5AJ4MtrwjPyzekmhaAl1elDC-ZZ0JgcjtTu2gY6ZNtFyOSxQh_xWftSgK6tzv9SmihbIrM4Mk619rLAM9sVK5mfS2jGtUApnC0DjeHpkOby9W--wPOaRHwM6-sHuGB5xSnWOvUfylP4DglePuGO8vYwj6A0PFL73IbIzbNEJrFB8bXlwOpTd441o4ULdB1tswKlYZ7QFyLdcI2X-u7oua8rlQpqkfMmwaZ1SSAvpCPtTWW-jOZl1Nrnat5iAb-Yu3Pu9p31xjYw8bZRfdSME8fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/195706b1a7.mp4?token=DJtZuAgqW3t43vEOF4z-WDuILnVIOuVjsCsghpzLawTgRfK-nJNkPMyJVsJEpo7Pe7ZZaesaM0JSZDOCpJpH7lGREGmTDjqjTRfT0gGTBwv1ZX527TV1Qo9G_KF-WHGdGADYNMJ7175v6ONX0bs2OYKuhayes6uOYpi5zJlM6BdR0s0x6AT-c9IQjl5lrcr03TRfPr2ORwAH_Cgm5QrPMOzmnmV1gab2h9ORMl3HWcCS8R_No3DFfHrJMQUQBrZviNFykWeL9RGiYOmMnBu5AayoG9iAefFsYdnZVmCs5o7Y1-K7yt0rk8wPv7zc8-W2Z96dfcbcjmT5qjQ0N5bSQ6TslRLVyPTnNVJixHJ-7NNlb5CjN2WVAYqu8dB4QmlBBShXD8mrGWN7b-vh2rcD5AJ4MtrwjPyzekmhaAl1elDC-ZZ0JgcjtTu2gY6ZNtFyOSxQh_xWftSgK6tzv9SmihbIrM4Mk619rLAM9sVK5mfS2jGtUApnC0DjeHpkOby9W--wPOaRHwM6-sHuGB5xSnWOvUfylP4DglePuGO8vYwj6A0PFL73IbIzbNEJrFB8bXlwOpTd441o4ULdB1tswKlYZ7QFyLdcI2X-u7oua8rlQpqkfMmwaZ1SSAvpCPtTWW-jOZl1Nrnat5iAb-Yu3Pu9p31xjYw8bZRfdSME8fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر مطهر رهبر شهید انقلاب اسلامی در سیل جمعیت عزاداران درحال حرکت به سمت حرم مطهر رضوی است
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669153" target="_blank">📅 18:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669152">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
عراقچی در گفت‌وگو با وزرای خارجه عمان و ترکیه، آخرین تحولات منطقه به‌ویژه تنگه هرمز را بررسی کرد و بر تداوم رایزنی‌های دیپلماتیک برای جلوگیری از تشدید تنش‌ها تأکید شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669152" target="_blank">📅 18:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669151">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-text">عزیزانی که امشب تمایل دارن برای رهبر شهید انقلاب و اعضای خانواده ایشان نماز لیلة‌الدفن بخونن، اطلاعات زیر رو جایی ذخیره کنن
🏴
سیدعلی‌ فرزند سیدجواد (امام شهید)
🏴
سیده بُشریٰ فرزند سیدعلی (دختر آقا)
🏴
مصباح‌الهدی فرزند محمدباقر (داماد آقا)
🏴
زهرا فرزند غلامعلی (عروس آقا)
🏴
زهرا فرزند محمدجواد (نوه آقا)
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
_ طریقهٔ مشهور در خواندن نماز لیلة‌الدفن:
بنابر این صورت که مشهور است، در رکعت اول بعد از سوره حمد، یک مرتبه آیة الکرسی¹ و در رکعت دوم بعد از حمد، ده مرتبه سوره قدر خوانده شود و بعد از سلام نماز بگوید:
«اَللّهُمَّ صَلِّ عَلی مُحمدٍ وَ آلِ مُحمدٍ وَ ابْعَثْ ثَوابَها اِلی قَبرِ فلان بن فلان». (به جای فلان بن فلان، نام میت و پدرش را ببرد؛ و اگر میّت خانم است، بگوید فلان «بِنْت» فلان؛ مثلاً زهرا بنت محمد جواد)
پی‌نوشت:
۱_ عزیزان دقت کنید، عده‌ای از علما میگن آیت‌الکرسی رو تا «هم فیها خالدون» بخونین، بعضیا هم میگن تا «هو العلی العظیم» کفایت می‌کنه؛ شاید اگه احتیاط کنیم و تا «هم فیها خالدون» بخونیم بهتر باشه.
۲_ یک نماز لیلة‌الدفن رو نمیشه برای چند نفر خوند؛ برای هر شخصی باید جدا خونده بشه، هر نماز هم شاید چیزی حدود ده دقیقه یا کمتر طول بکشه.
۳_ مستحب هست که نماز لیلة‌الدفن بعد از نماز عشاء خونده بشه و تا قبل نماز صبح هم میشه خوند.
۴_ عزیزان، منفعت این نماز فقط برای اموات نیست؛ مطابق حدیث نبوی، یک روزی یقیناً نفعش به خود شما هم می‌رسه.
پیامبر(ص) درباره ثواب خواندن این نماز فرمود:
«بر میت ساعتی سخت‌تر از شب اول قبر نمی‌گذرد. پس بر مردگان خود رحم کنید و برایشان صدقه دهید و اگر نتوانستید، دو رکعت نماز برای شخص درگذشته بخوانید. پس همان لحظه حق تعالی هزار فرشته به سوی قبر او می‌فرستد که با هر فرشته جامه‌ای و حلّه‌ای است، و تنگی قبر او را تا روز نفخ صور وسعت می‌دهد و به نمازگزار به عدد آنچه آفتاب بر آن طلوع می‌کند، حسنه عطا می‌کند و او را چهل درجه بالا می‌برد.»
مستدرک الوسائل، ۱۴۰۸ق، ج۲، ص۱۱۳.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669151" target="_blank">📅 18:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669144">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkXkHVqOyW3TishftSgPNTWTzNmTHuoi2jWrW99H3RhdvgPGX9RQFoKExfMbtWlcFRRncojofySAzQQEDl6RV6IBAZWCSsC-xTLsMwVUBkmj2Umcmc4p5L82AZmB2JRoPQMXszJDTuev8aL_Nxg-QpfGU2FJDjahKApXDvh68uSPtSGbH4AujPyLnGlHu7-1kztpXfU4lWO2tzS70Nvw2aBnzPpUtt2WzjrimcYuH7ErnqdsatJYPAQvyFpKWnJcdvAi23FRs81-xWUvXav9UmKZQfQ9FzvS0W9d9Ny8KvnR2lxp7wGRhVTF98-42TTAC3vLO41x5fYoqUwRQV118A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ilnMB1bi6fVAVyUo5-GlUYrEGLNiiePI7635rIUiZvbIG8VMEpqzDxTiC_59ZM_qS665MYiut66VwnPk7pWvoBTPJCWYIxsBySGR_umndn4uajYYyQlymXPDw0m_tN9SzRx7oyWl1-z7FBvuOncCoYjYm4UYdvqD0GEmrNB_H0_FZs2Gj0DxxPChNNVriOBlnjNvW6dwzxtRyVzzxDfAibdiHTVJ1crJ9iSUs5wNPpKgTVfFfLHUKoD3gvGBxew9OM1n-HSxgACvstg9RZLX3FcjJn_J4n9OAHqGR1AAK1Qfhrh4ehNpzexC-C1dbcxcmXs1W45pw6mcvpFHiFb93g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pbQzMc6F9jRP26hQ33PzSJB1OdmBwc5Si3GnoXCVc89KSDT1PR5JVT1kGS_Dw_ilNPb9a2ARb1gH-4GkjVUboIhSCRgudAxEOONbegk0BchzxdQvAf09B3xZp6qkNEmOS1u8y7j5RdD8ZQLLma4TniXc4VFrGKg053HblEDtqsNZbSNp7POnbw7TPWi5YljOgqFNQiLj4W9eThEBiVhkcM3j2CezN5kegjtG0U72ChKY8BGYH5kXOC92vNhVfo00F1H9r0V2XRSPHv3LTW4pHm_YcdCZdxO1OoXVKpEz51tVa4UZqCsm2VARHo3dreopY39PBhqTv5iKk7prqcO35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfQgQOwzBGwjNFINs9maDJiVprPNug3ycwefdp90E2gzXW22_ehAhtM4C3mkuFJATUwjmMM12lNbC-DErrrg180g5UJQ5lar0qW58zCPy_vtcJqb-AhNauEH0Y1Dvchm_hzrK3sttoeaM_R6ydHm4mq0Ndkzp29bxV_2ZMwS5jUlDbAJpxwq8pTAZjlGRj2qaIDv-lE_x8GYDYCikIO47nNZrhapUhQDR8D_IAMkQVSbE9ZwrU3uL9mlao04ddSrwyp3mB89Bl6sIEQnfvm_xw7zIR1gsoEUcFnjSyF6AUMysv3GOSJjuXVg4Th4mKBPB-sXfDAJhHLHbBHeZ6sFfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q5H-hrGqrHDlO_3RcsnQounx959oAfGnHpsc2V_4o8x-wQMiuKS6aBX_2RXLEtkgbhBFYoVAoNAYgTTQXOUNMDCFO4UK92sphWmJRxwWTFhVC0wHAdW-psIIZaloNM3emF_R0mnis5EGhajvIcWoEtKbwoqx0h-yWhu1tcIRb_D8aZ6TRpoOjAJ3M1xxRdugUqRLQZkm-YtBUa8LSsCuWAtA8GUTH4S3ArPVMivLLOBZqx8raUOgLwY0AF9B0yOR5FmyOQlZnu3EK0SqqqE79ZF_r8-JIcUOYaK2e8UM058TZLve_uH9Pq7A2JQ0LHvbz4TyctPz0_1D4lKeb2fYjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qw3Y7--BmNTuHR7Ix3F6lAEwTEA9euFg4jmufA408ywfcqay6G0CstNF1VEEXy9h2bntRpfWzT3FETlN900ecTPI-Pe_XJuGNhTdYul_JEZgWx4ZGjF_b6Ndfz05sl3FY7f7o_hboD7rs1dLnyTdOFMOYR5d2YBD_8Rl72NIGe7_Atkyp56X2KJuMjgvyCv1YGhBJbmcoBuWzZ6ZMag_9WhCFb5gu8jdBvJTrg-MekuI6BeyjzBBxq_4kF6La8BeEGqZEprQ1OM48wDf6ouHwpt9Dm4VwRWo3HpFzoWgJJZSQEEASFojCx-5BUKNSu8ykRnQbZQR5WrQ8wQnm46XYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4luywFmn6Iq4j5UI2u3BZOSBxu4rBx5gk0N-Bd8LsJuRWMQDQqgj16LtF5UC9FPKq-69sjD55dGdjHJh99X-PWTXWjAM_dmSVToOLz7KOVWNsXMLMcM5mVyPsuFU0YoMBP1mgGJPo3qPUJvgo-QqTyh0Du7Bil-E_1zwBz7Zx4piUVwX9TJeTy7SkktdxooXGinzWQp5DtMio0-0pe51GBLQ1v-0VTmzK1hMkOlO7XcouriqQBas5zqstrLQeiKqOrueP2XJ5grxY4q-blZELRu0RIaJEZpxGDwUHbgdKSzeIrDRb2KOAr94ronxmBv4HiapJyl88skFRJsZT4BzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نظارت مستمر و خدمت رسانی بازارهای میوه و کانکسهای اقلام اساسی و بهداشتی شهرداری مشهد در ایام میزبانی میلیونی مراسم تشییع در مشهد مقدس.
Samesh.mashhad.ir
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/669144" target="_blank">📅 18:13 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

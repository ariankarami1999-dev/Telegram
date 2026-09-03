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
<img src="https://cdn4.telesco.pe/file/Jb42HI13_GB1-vQAD22XDAKGHd9g2tyWdjdl6_CH1-C6_r7sWACWcyPBg_eQiycHQpBCNPfoMKDYlyf7Z4bS--EMjGtH16C_S301xK_E3Qyy4LVRyCPmiKzPvCYm-rCzckq0BmxbAla4HpkytE1IfXBV9vF0G8tAgpAiA7WvwvwkbIcnVSnXtZasSnyubUu7nkHhIglBDCfnJCvRKJcoBBTgMdLSLbey-TMPgvNcJWzKCk8YoiK_SFjVfOx0cqb01GsA2lhpcSuNlLx-KjV5g9NH9ZwUFx97EZQ8lZxGFAwUKD7M63849nEdudS0Rj3ogaq6zvxuJO02J6Gl0rQq6g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.7K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 23:28:45</div>
<hr>

<div class="tg-post" id="msg-20529">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ارتش اسراییل برای دومین بار اعلام کرد بر تپه های راهبردی علی الطاهر مسلط شده است.</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SBoxxx/20529" target="_blank">📅 22:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20528">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNx-awwCmRj7qBpb5imc1mmC5bOSoJTnG32Oberzy8LDfcjPr8jCJtml8QrwGztlw6qI8In7S3WhG1XBvp7R2FxKaUbEmMlYFzNSr1Yn0qGj5_DKB6O_J91G-KtnwurLVe2QAS8AjuwmOhjJ5kCgG9fhyyz5NzF5y5zt3TqXNcUwe1S5Ha4KwqmifSutZcb1ZFWPMvKfiQDbY7ER7M_wsbUEghWvcI-FM76IHKK8xk_LHpouo70hMZyI6mN0PTJvIBC1Go548SaKCB34SWVhQAxqIS79hos58VZE2OFJyYVZhYQdfKYCwYZ5Yr3_fQgQqxQgBy8wc-gr71IIPvYAzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۸ سال بعد از حمله هوایی ، اسرائیل اعتراف می‌کند که مشاور اتمی ارشد اسد را در یک حمله شبیه به سبک مافیا به قتل رسانده است
در ۱ اوت ۲۰۰۸، غواصان اسرائیلی به ساحل سوریه در نزدیکی طرطوس نفوذ کردند، به ویلای تعطیلات سرهنگ‌کل محمد سلیمان، مشاور ویژه رئیس‌جمهور، حمله کردند، او و مهمانانش را در حال شام خوردن یافتند و سه گلوله به پشت سر و گردن او شلیک کردند. این موضوع را اهود اولمرت فاش کرده است.
«در روزی که سلیمان حذف شد، جنگجویان ما از آب بیرون آمدند – تیراندازان چابک ماهر،» نخست‌وزیر سابق در یک خاطره‌نویسی جدید نوشت.
«او را با قطعیت شناسایی کردند. با وجود اینکه تعداد زیادی از افراد روی ساحل حضور داشتند، هیچ‌کس متوجه آن‌ها نشد،» او  مدعی شد و توضیح داد که چگونه کماندوها به‌صورت بی‌صدا به خانه سلیمان نزدیک شدند در حالی که او و مهمانانش روی یک تراس باز نشسته بودند و از فاصله‌ای حدود ۱۵۰ متر به او شلیک کردند.
«سر او به عقب افتاد. بلافاصله پس از آن، جنگجویان به سمت آب عقب‌نشینی کردند و راه خود را به سمت قایقی که آن‌ها را برداشت، باز کردند،» .</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/SBoxxx/20528" target="_blank">📅 22:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20527">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">امروز چند بار تتر تا ۲۰۰ تومان ریزش داشت!  به نظر عده ای دارند نقد می‌کنند   تارگت کماکان ۲۴۰</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SBoxxx/20527" target="_blank">📅 21:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20526">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omOYMT1wbjyTai3ZyXJLHxF3P_knkNwfUeRi1u96cGCvXP_0SxG7lscAXiz3hhTPNhOeWx5uwcJzEpQA62f90MnjdnS9g-n8o6m5IXwOgqMRyY2qlTJl5KZzmn8Ma6c_ux02nbHZWhkM8Vzj-zD2ViPEhct1F8g3w4ckDWR7Znf2hXgQZ3GZihJ6ZrmJgsDempnBJGjg6Da9XzCGpeP_53vAF-E2BCG9YAgCZzE0a6rISMUm3Vv810DH4fhAUS5EgegSjRPloEkEjzckbCdK5hx1wilUYe4D8rYuw5LR5-pWBxEgDWy-i3iMBE4IETEI4PMTrBwSeSUO9ZSz67syqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا یکی به نوید ممدزاده بگه  وقتی روی مواد هست  گوشی دست نگیره  مرسی  @PiknikAnalyst</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SBoxxx/20526" target="_blank">📅 20:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20525">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ایران از طریق عمان پیامی به ایالات متحده ارسال کرده و هشدار داده است که در صورت هرگونه تهاجم اسرائیلی به ارتفاعات علی‌الطاهر در جنوب لبنان، به‌شدت پاسخ خواهد داد؛ جایی که باور بر این است که نیروهای سپاه پاسداران، از جمله دست‌کم دو افسر ارشد ایرانی، در کنار…</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SBoxxx/20525" target="_blank">📅 20:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20524">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سبحان الله این محمدسامسینگ ما چه انگلیسی اش خوب شده!</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/20524" target="_blank">📅 20:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20523">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">قالیباف خطاب به وزیر خزانه‌داری آمریکا</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/20523" target="_blank">📅 20:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20522">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpE48B4SMeva2WNh62hmNHjdHqQwyIYR98zhbwE6JsxHrU8vGj3sBedXX4ZgDiXppNAIN-Ouwdbxj0Xg6ZhI4U683F8Q2uzaWeUvTcESoHqvQBEuN223HFJwjSEqZtDV76mvGWBK7P7uiSr3cBTAcpGNAMPjEjFQQbJ_jPU0OX1_j5IYE7LVMTD--ZcYXmXr7wgjCWIbgy_z0v0qvFDLnmO1IKHSR1-adxkP2qT_Az66kWY5YWgc-0jDFzry-eD96ZwIWbg3IgUnNmI7CDOXpiakpvZ4qAIIVcNTzBcZd1DPR-KM-wl4vuaYlCf_4QCyxWMm3AlV5tvOy-3G1XGB-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف خطاب به وزیر خزانه‌داری آمریکا</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SBoxxx/20522" target="_blank">📅 20:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20521">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">موشک‌های ایرانی به سمت کشتی‌هایی که مقررات تنگه هرمز را نقض کرده بودند، شلیک شدند.</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/20521" target="_blank">📅 20:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20520">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">— نتانیاهو، نخست وزیر اسرائیل، در مورد ایران:   ما با تهدید نابودی توسط رژیمی روبرو هستیم که می‌خواهد از بمب‌های هسته‌ای برای نابودی ما استفاده کند.  من به توانایی خود برای از بین بردن این تهدید برای همیشه، یعنی سرنگونی این رژیم، اطمینان دارم.  این ماموریت…</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SBoxxx/20520" target="_blank">📅 19:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20519">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">— نتانیاهو، نخست وزیر اسرائیل، در مورد ایران:
ما با تهدید نابودی توسط رژیمی روبرو هستیم که می‌خواهد از بمب‌های هسته‌ای برای نابودی ما استفاده کند.
من به توانایی خود برای از بین بردن این تهدید برای همیشه، یعنی سرنگونی این رژیم، اطمینان دارم.
این ماموریت اصلی است که هنوز پیش روی ماست، اما نزدیک است. غیرممکن نیست؛ در دسترس است.
آنها بی‌دلیل از حمله به ما اجتناب نمی‌کنند. آنها به همه حمله می‌کنند، فقط به ما حمله نمی‌کنند. آنها قدرت ما، قدرت بازوی ما و عزم ما را می‌دانند.
من به طور کلی به دشمنانمان می‌گویم: با ما درگیر نشوید. اگر چیزی یاد گرفته‌اید، با ما درگیر نشوید. ما قدرت، عزم و وحدت درونی برای غلبه بر شما را داریم.</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SBoxxx/20519" target="_blank">📅 19:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20518">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">۱۸ سرباز پاکستانی در یک حمله چریکی در منطقه زیارت بلوچستان کشته شدند.   گروه BLA مسئولیت این حمله را بر عهده گرفته است.</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/20518" target="_blank">📅 19:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20517">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">۱۸ سرباز پاکستانی در یک حمله چریکی در منطقه زیارت بلوچستان کشته شدند.
گروه BLA مسئولیت این حمله را بر عهده گرفته است.</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SBoxxx/20517" target="_blank">📅 19:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20516">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بفرمایید:  پنتاگون آزمایش کمبود تستوسترون را روی مردان بالای 30 سال آغاز خواهد کرد.</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/20516" target="_blank">📅 18:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20515">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ولی خداوکیلی این آمریکایی ها ترسناک هستند؛ شما فکر کنید هوموی مفعولشان اینطور خشن است وای به حال هتروی فاعلشان!</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/20515" target="_blank">📅 18:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20514">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCnoYUdewt8a5VpD-4px7ZfxSm-z4CLdOPO-Q5LREvHOx0ML0oD_EdghUft6wDFyr6u7ngO63ssBudRfp5wChOoUyVTO4-w79hupenxNy6lZNnNdNb0gufaxZUm_1jVt41J_GB51aRRucHo0CQy5QdTOlSc96NGQGCXz63FJmauzLxoFJFv8OKcM50YpN0aw5GCaOtOX1rNFcuteO5WeRoatirZErvReJFHuR2gLmOSTZ3NRMBrZT_Nx2Y6sZguvtlu3jP3bosxg7Iiuy9g-p4P_FopZEj33iW09ejAyvyfPvs2hXckI-S5hHs3yOLB8Ta5SUUY8MheRX-HEdXjXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیل دقیقی است. تمایل جناح تندرو تداوم همین وضعیت است تا هم فشار برای بهای نفت و اقتصاد کشورهای منطقه و نرخ های بازدهی اوراق بدهی آمریکا حفط بشود و هم هیچ تعهد جدیدی برای خارج کردن اورانیوم بشدت غنی شده و برنامه موشکی و .... داده نشود.  طبق این  دیدگاه، نهایت…</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SBoxxx/20514" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20513">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ :  برای آن آشغال‌های  خائنی که از گزارش دقیق عملیات نظامی ما در ایران خودداری می‌کند، ما عملاً مقادیر نامحدودی مهمات با درجه متوسط ​​تا بالا داریم، بسیار بیشتر از آنچه که می‌توانیم برای این جنگ یا برای هر جنگ دیگری (که بسیار بعید است!) استفاده کنیم،…</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SBoxxx/20513" target="_blank">📅 18:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20512">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ :
برای آن آشغال‌های  خائنی که از گزارش دقیق عملیات نظامی ما در ایران خودداری می‌کند، ما عملاً مقادیر نامحدودی مهمات با درجه متوسط ​​تا بالا داریم، بسیار بیشتر از آنچه که می‌توانیم برای این جنگ یا برای هر جنگ دیگری (که بسیار بعید است!) استفاده کنیم، جنگی که به احتمال زیاد می‌تواند رخ دهد.
علاوه بر این، ما در حال تولید مهمات در سطوحی هستیم که قبلاً هرگز دیده نشده است. ما در حال ذخیره و آماده شدن برای هرگونه احتمالی هستیم. ما آنها را برای خودمان، ایالات متحده، به جای فروش به دیگران می‌گیریم، اما فروش به متحدان به زودی دوباره آغاز خواهد شد.
همچنین، لطفاً اطلاع دهید که دولت بایدن مهمات بسیار بیشتری را بدون هیچ هزینه‌ای برای آنها، نسبت به آنچه ما در ایران استفاده کرده‌ایم، به اوکراین داده است. صدها میلیارد دلار به اوکراین و ناتو، رایگان، داده شده است که اروپا می‌توانست آن را بپردازد - اگر فقط از آنها درخواست می‌شد، اما ما آن پول را درخواست خواهیم کرد، هرچند کمی دیرهنگام!
از توجه شما به این موضوع متشکرم. رئیس جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/20512" target="_blank">📅 18:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20511">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGq6XFhtmPXi6gev2ALGRrouKgL6HE8E8UvRxBKvdxgEFBrzTCPtfwX5-wRIr-YQecp_drzMgqcl2n3dp9-_pIy7-EQvSeOYL8d3V8QX1OV1BZNYnQ7CH7ggqe_CKQIPydoAT8FTas1EBh4onXNtu5NP0276zoSkx-TtvTBxY55XCaXuFYwMtpjd8GVsIcjsdEcK3GYnnW43B7Fg52GbbP0uO9uHScvwWFzW-woY36PIZoLNQ02Ge78KCpNmc9UQIHP0F_KNpSO9S4s6T90tsuPT4wQq3wqUBjmo3aAZYRb23O_ZsON7A_x9IeQhiNjeOLv44xFPi3ojuBoTcwL9oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار باز دارد پارابولیک رشد می‌کند و من خوشم نمی آید  فکر‌کنم تا ۲۰۰ پولبک بزند.  تارگت کماکان ۲۴۰ در گام نخست</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/20511" target="_blank">📅 18:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20510">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد و پیش بینی می شود دستکم تا 4385 شاهد افت قیمت باشیم.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/20510" target="_blank">📅 16:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20509">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دلار خرید دارد همینجا با تارگت ۲۴۰ الی ۲۶۰ هزار تومان</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/20509" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20508">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">#سکه  عیناً مطابق سناریو ترسیمی رفتار کرده تا کنون. شکسته شدن خط مقاومت مورب یعنی سکه دوباره برای بالای 200 میلیون تومان خیز خواهدبرداشت. (برای موج نهایی صعود)</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/20508" target="_blank">📅 15:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20507">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">در حملات هفته‌ گذشته آمریکا؛ ۳ خلبان و ۶ افسر نیروی دریایی ارتش نیز کشته شدند.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/20507" target="_blank">📅 15:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20506">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ایران از طریق عمان پیامی به ایالات متحده ارسال کرده و هشدار داده است که در صورت هرگونه تهاجم اسرائیلی به ارتفاعات علی‌الطاهر در جنوب لبنان، به‌شدت پاسخ خواهد داد؛ جایی که باور بر این است که نیروهای سپاه پاسداران، از جمله دست‌کم دو افسر ارشد ایرانی، در کنار…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/20506" target="_blank">📅 15:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20505">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ایران از طریق عمان پیامی به ایالات متحده ارسال کرده و هشدار داده است که در صورت هرگونه تهاجم اسرائیلی به ارتفاعات علی‌الطاهر در جنوب لبنان، به‌شدت پاسخ خواهد داد؛ جایی که باور بر این است که نیروهای سپاه پاسداران، از جمله دست‌کم دو افسر ارشد ایرانی، در کنار جنگجویان حزب‌الله مستقر هستند.
— رويترز</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/20505" target="_blank">📅 15:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20504">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDQFw5_PKkWi12can9MzxWcdb5187e6HS1FQEfUappYq8Eq7Tj3fi4xzbUy6e3SGXq2EPLIDt8EhAD7_pX4b-tR2eWGZOKCdsAE1DKNNlwy55mvH5mC7K5EZDlsY7qBxuWsWK3EG2M578lPnhmyr7N_a34fdJ1Z-0Z3F9pdWzOxvfg8ips4uQYT38aQDd7tED4Oy1xViZ_ELKM-YhT5dSZ1vg72o7sgYDvzt_c4EEl4jD3a769eLZqBXGrRIZLX-HduZyxKJ2h911h-sDCX4JQmVS976sWSpmMPBtG_ThhkPFmWZ3RiLbVksB-ZPpu7ZG-0hRkgnBXR0ic2UZVhA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستایش ترامپ از نقش آفرینی جدید سوریه در ارائه مسیر جایگزین برای هرمز !</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20504" target="_blank">📅 15:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20503">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آزمون های  pte و mcq  هم بعد از تافل و GRE برای ایرانیان مقیم ایران لغو شدند.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20503" target="_blank">📅 11:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20502">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آزمون های  pte و mcq  هم بعد از تافل و GRE برای ایرانیان مقیم ایران لغو شدند.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20502" target="_blank">📅 11:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20501">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حمله ایران به پایگاه های آمریکا در کویت!</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20501" target="_blank">📅 11:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20500">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">📌
نرخ بازدهی اوراق آمریکا در آستانه ۵ درصد؛ بازارها آماده یک شوک نرخ بهره می‌شوند؟  افزایش بازدهی اوراق ۱۰ساله آمریکا به محدوده ۵٪ می‌تواند فشار مضاعفی بر سهام، طلا و دارایی‌های پرریسک وارد کند و هم‌زمان دلار را تقویت کند.   اما اگر رشد نرخ‌ها از نگرانی درباره…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/20500" target="_blank">📅 11:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20499">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjUcP8PqE81kNu_H0SD99-UdKtuh4ERIBcyR8A0kdA28Ed3RSIJMNyh0TWO_iMT4W9i7KpQZ0us3Bmce3UOkJ5RcTIMv9UJAZl3keXr625p5N9XT1I2Xqq-YI7Mi4sbXPtFif6Ptz0uWisdK7rZHDV0Oq7Pc-QtOig9L2C1KthGnbrhXhqRQkH1br9vf84VYohLfLGmvjsT16MM392HDz5cXzYitNb1S5J1TcM5CmH5yj2_YO278NgVqHxfOcDuLNoy0v3L1AvUgubFwNFheOE7bu3eDb4bnLPdp5-_oVdsbvnR5SDVe0MOGzd4qKVszuwb5XikOSAEIHTRw7tR7KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/20499" target="_blank">📅 11:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20498">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWRfz47hrY3cbsy3b-FmW9qrxlHEE2ggkRED4iUv2rWtPk79ROJPPtokM_pLstzAqCGYzejDeCcsOmHvr6JpHKCyfTRLdYGJ9EHxNUxqoO53GXvgDJZxGtz-bXCYIDoYVrmQiHT4kHJZm_ch9Tyq1-yv2vivgIBU9KngMnNOlc7ZMBfW1ky79YIOzT7zXzUHtZIRyiKjAkaGchpvLTXi83WCiwvmsHVagVyTLSMna6q7a9YvGrHVCHmvcR8TKC3G6DVWcTxq_OC5g-KmPEF7s22a-NVbuSxBz10R2sbP_e6sbRNwFyfiK47GvYMDQQ9ANzBQci3ewuCZJym0L28yhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نرخ بازدهی اوراق آمریکا در آستانه ۵ درصد؛ بازارها آماده یک شوک نرخ بهره می‌شوند؟
افزایش بازدهی اوراق ۱۰ساله آمریکا به محدوده ۵٪ می‌تواند فشار مضاعفی بر سهام، طلا و دارایی‌های پرریسک وارد کند و هم‌زمان دلار را تقویت کند.
اما اگر رشد نرخ‌ها از نگرانی درباره کسری بودجه و پایداری بدهی آمریکا ناشی شود، معادله می‌تواند تغییر کند؛ طلا به‌عنوان پناهگاه امن تقویت شده و بازارها با ریسک بازقیمت‌گذاری گسترده مواجه می‌شوند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/20498" target="_blank">📅 11:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20497">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bf2OSRw8ZOResD8QYPRHshkCHv2Z8iJAfHHjWmVtelMZKBmvUA0Co6TLhkiuOsQd_JFQHBBOJqjxMvdcmpgvzB2shAuM2Azy3bVbz7nUaZcSeNyBO4I05JRtZKlGhroA3kGI0PMs89-GzHTjQDzjYlNT17v8Pd6Vj_eAjhl4P9vmwFudMEaMQnGoN_qHXHX2Bmgz7aURhtyKSYS2srymvhUt8siKeuqXquI1ayD7rhsuciWP-IokLuoS425_heXT6Ga2txNkuX_EKwFps_GVvWG5GYm27ATlvVatlA0Ej_yUrlc7Ejkl7Y7Ws5MljEJ4IP5CJcip7Cr4EP46y-pqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد و پیش بینی می شود دستکم تا 4385 شاهد افت قیمت باشیم.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20497" target="_blank">📅 10:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20496">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0447727037.mp4?token=CYgSB3bZrdBciu7FyVtZG5TnASum_fyVvf6T_biDUnIYd7ZvkIUZuxI2kwov8Ek54fTuHSH5lMmN5aqnghKkgeVfisN3cvctCRXY0v_QNHbL6fVQgKTBeejheOxFa-ydfyAa2bEvEUdFwiiZ6q7tWVfN-l5AAAzHlVqZIbkbkBAkrBGnVhrHCV9bZF3Xco2-bSxIFuC5PMeVXRfdDyMNokgopg3WxV50SUcRd3AzpY4Y-exU9ZAYoOA6vo068TnCIhwqDMgec2RUkktpykteOvDKbiIKaFk0Ry87TQJ6-IjV4I1OmyHsy6K4xBeL-9ZCcqLX4hJv7enV8MtdHub1aZcqqfhN1WeCZEHlzvST9jpDS32rJJK8jBUZdWMG2UMYdOpRFu-Yp1w0aq0enk6o5_dt-Rzyaf4M-Iq9hXcPkpnGN2pSQX1hrGTSG1GGxf3q7NsBlRMN1JatjszGkwv-WFGNoJ3pGt2_PPl3isl-prwkirg_MjR778NGxM2By4POW-UGc2pVMhsJchfzoJwoUNmvMBIhnHK7RN_pHbIbOXpy_tb62HRArcjN_Vb88eTsRZy_mz5wAnsJPRtTPP2S--_KVFxMWSOSBfRjIzSXx3UM4HcUpHrQkUVf6gQOeHV0oG-wgJ41syz3JebeFP4OBUYP6zg3EquyE2pX-ps7WOc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0447727037.mp4?token=CYgSB3bZrdBciu7FyVtZG5TnASum_fyVvf6T_biDUnIYd7ZvkIUZuxI2kwov8Ek54fTuHSH5lMmN5aqnghKkgeVfisN3cvctCRXY0v_QNHbL6fVQgKTBeejheOxFa-ydfyAa2bEvEUdFwiiZ6q7tWVfN-l5AAAzHlVqZIbkbkBAkrBGnVhrHCV9bZF3Xco2-bSxIFuC5PMeVXRfdDyMNokgopg3WxV50SUcRd3AzpY4Y-exU9ZAYoOA6vo068TnCIhwqDMgec2RUkktpykteOvDKbiIKaFk0Ry87TQJ6-IjV4I1OmyHsy6K4xBeL-9ZCcqLX4hJv7enV8MtdHub1aZcqqfhN1WeCZEHlzvST9jpDS32rJJK8jBUZdWMG2UMYdOpRFu-Yp1w0aq0enk6o5_dt-Rzyaf4M-Iq9hXcPkpnGN2pSQX1hrGTSG1GGxf3q7NsBlRMN1JatjszGkwv-WFGNoJ3pGt2_PPl3isl-prwkirg_MjR778NGxM2By4POW-UGc2pVMhsJchfzoJwoUNmvMBIhnHK7RN_pHbIbOXpy_tb62HRArcjN_Vb88eTsRZy_mz5wAnsJPRtTPP2S--_KVFxMWSOSBfRjIzSXx3UM4HcUpHrQkUVf6gQOeHV0oG-wgJ41syz3JebeFP4OBUYP6zg3EquyE2pX-ps7WOc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صف طولانی بنزین در مملکت دوست و برادر روسیه!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20496" target="_blank">📅 10:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20495">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حمله ایران به پایگاه های آمریکا در کویت!</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/20495" target="_blank">📅 10:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20494">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twjNhn_3gCJ9UMlVUSpi1eURJYsL9HYoLWa4tSw6kdarqVLPyIpuZG45va0_nXSaQnbocbGgl-fnMSwno6Alr1L15aJF3dV_RYTB2bO1ggScF34LM5kmnIdlJSTsCEBSPtLvszS5AHfLObFofD9aJ5eMSeBDBZJXHK4N5_kUOiFUjE6vT_YILjx9i4QcyAbj3uMtGN90NJm9E76doX7VmS7wRN6-zJkGz1VQX_nQ1Kmc7jMmLlbA1Glr3WoeNGalxvm8cmrhA97nG_j4JKADg5eP1K4BpsXdqIJypnt-6FhjnXlEbl3Kr9xaVd4WXLO6JLrysElZEFSykEOBcZGktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20494" target="_blank">📅 01:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20493">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انتشار اخباری از انفجار در میناب!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20493" target="_blank">📅 01:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20492">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انتشار اخباری از انفجار در میناب!</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20492" target="_blank">📅 01:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20491">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جمهوری نظامی ایران.pdf</div>
  <div class="tg-doc-extra">257.6 KB</div>
</div>
<a href="https://t.me/SBoxxx/20491" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">موسسه معتبر مطالعات جنگ (ISW) در
گزارشی
به میلیتاریزه شدن فضای رهبری کلان جمهوری اسلامی پس از جنگ اخیر پرداخته است که ترجمه این گزارش — با اندکی تغییرات اجباری — اینجا ارائه می شود.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20491" target="_blank">📅 01:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20490">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گزارش هایی دال بر پرتاب موشک از سوی سپاه</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20490" target="_blank">📅 01:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20489">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-poll">
<h4>📊 دکترین «دفاع موزاییکی» توسط کدامیک از فرماندهان نظامی جمهوری اسلامی تدوین و تببین شد؟</h4>
<ul>
<li>✓ محسن رضایی</li>
<li>✓ محمدعلی جعفری</li>
<li>✓ رحیم صفوی</li>
<li>✓ احمد کاظمی</li>
</ul>
</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20489" target="_blank">📅 01:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20488">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ: «ما همه کارهایی که در ایران انجام می‌دهند را می‌بینیم.آن‌ها حتی نمی‌توانند بدون دیدن ما به دستشویی بروند»</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20488" target="_blank">📅 22:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20487">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ: «ما همه کارهایی که در ایران انجام می‌دهند را می‌بینیم.آن‌ها حتی نمی‌توانند بدون دیدن ما به دستشویی بروند»</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20487" target="_blank">📅 22:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20486">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔹
خبرنگار: آیا شما سازمان سیا را برای مسلح کردن ایرانیان اعزام خواهید کرد؟
ترامپ: من نمی‌خواهم این را به شما بگویم، مناسب نخواهد بود</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20486" target="_blank">📅 22:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20485">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فوری | ترامپ: ایران در تلاش بود تا موشکی بسازد که بمب‌ها را حمل کند و ما آن را نابود کردیم.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20485" target="_blank">📅 22:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20484">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20484" target="_blank">📅 22:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20483">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">برخی اکانت های مربوط به جریانات تندرو، خبر از احتمال تسلیحاتی شدن برنامه هسته ای ایران بر اساس مواضع دبیر جدید شورای عالی امنیت ملی خبر می دهند</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20483" target="_blank">📅 22:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20482">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">این گزارش های آژانس هسته ای و اظهارات تند ترامپ + نتانیاهو شرایط را به صورت قطعی به سمت جنگ می برد.
مراقب موج‌۳ باشید.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20482" target="_blank">📅 22:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20481">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فوری | ترامپ: ایران در تلاش بود تا سامانه‌های رادار و موشکی خود را بازسازی کند.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20481" target="_blank">📅 22:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20480">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فوری | پیش‌نویس گزارش آژانس بین‌المللی انرژی اتمی: ما تأیید می‌کنیم که قادر به بررسی این موضوع نیستیم که آیا مواد هسته‌ای ایران به اهداف نظامی تغییر یافته‌اند یا خیر.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20480" target="_blank">📅 22:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20479">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فوری | پیش‌نویس گزارش آژانس بین‌المللی انرژی اتمی: از ماه فوریه، هیچ بازرسی از تاسیسات هسته‌ای اعلام‌شده در ایران انجام نداده‌ایم، به جز بوشهر.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20479" target="_blank">📅 22:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20478">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فوری | ترامپ: ایران در تلاش بود تا سامانه‌های رادار و موشکی خود را بازسازی کند.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20478" target="_blank">📅 22:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20477">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فوری | ترامپ: ایران در تلاش بود تا موشکی بسازد که بمب‌ها را حمل کند و ما آن را نابود کردیم.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20477" target="_blank">📅 22:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20476">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فوری | ترامپ: ایران در تلاش بود تا موشکی بسازد که بمب‌ها را حمل کند و ما آن را نابود کردیم.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20476" target="_blank">📅 22:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20475">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">— نخست‌وزیر اسرائیل، نتانیاهو:
«حکومت ایران سقوط خواهد کرد. ما آن را سرنگون خواهیم کرد. این حکومت اکنون در آخرین لحظات خود به سر می‌برد.
تمام سیستم‌های ما، تحت هدایت من، برای سرنگونی این حکومت عمل می‌کنند».</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20475" target="_blank">📅 20:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20474">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تسنیم:
کشته شدن ۱۸ نفر در حملات دیشب آمریکا
وزیر بهداشت: در حملات شب گذشته به استان‌های مختلف کشور ۱۸ تن شهید و ۱۰۸ تن از هموطنانمان مجروح شدند.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20474" target="_blank">📅 20:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20473">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ:
حالا که تنگه هرمز تحت کنترل آمریکاست، آیا باید اسمش را به تنگه ترامپ تغییر بدیم؟؟؟ مثل خود آمریکا، این منطقه «داغ‌تر» (پررونق تر) از همیشه خواهد شد.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20473" target="_blank">📅 19:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20472">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ درباره ایران:
ما اکنون تنگه هرمز را کنترل می‌کنیم. ما آن را کنترل می‌کنیم.
دیروز شب ۲۸ قایق، ۲۸ کشتی آنها را از بین بردیم. ما آن را کنترل می‌کنیم، آن‌ها چیزی به دست نمی‌آورند و ما کشتی‌ها را از بین بردیم.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20472" target="_blank">📅 18:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20471">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رئیس مجلس نمایندگان آمریکا می‌گوید که حمله نظامی به کشور ایران ضروری است.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20471" target="_blank">📅 18:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20470">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بر اساس گزارش شبکه NBC، هکرهای ایرانی در هفته‌های اخیر، سیستم‌های تامین آب، مخابرات، انرژی و سایر زیرساخت‌های ایالات متحده را مورد هدف قرار داده‌اند.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20470" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20469">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SplevmW--A8m-BfPDODOB80vTJGxbnu6P1UIOZUAiZEj9PXs3kuyTV75h8w9Z_rem-hdHIOP1EascYGa8NYa4evKsi8KobyUkgeNHNSkZusSR6ech_T8XHGLIZwNooYYr08W6pRBwIvevqZ4h1B6XuZC1J5G8WPjS233aOsCaKc0zNkPEU87PrlUrcSU-VQeckN2RYZbwDreS0WANSVW2q0iuJiMZxKj9flW4Iy9xpbr2PGtyryyyj4EhudegxyzmDBv1KowrSFvsMQ2TwR_4BQQeKnD4vYnV9fBHQ9HVRDaSA1s0S17b6tU38ULzyQ2qaqWbLtPm0VefJMYT2i7Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه ای قرار دارد و با توجه به بیش-فروش بودن تکنیکالی، امروز احتمالاً یک اصلاح رو به بالا در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20469" target="_blank">📅 18:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20468">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه ای قرار دارد و با توجه به بیش-فروش بودن تکنیکالی، امروز احتمالاً یک اصلاح رو به بالا در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20468" target="_blank">📅 17:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20467">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بِسِنت درباره ایران:  ایران مقداری از ملزومات خود را از روسیه تهیه می‌کند، اما اگر خطوط هوایی ایران را تعطیل کنیم، که این کار را انجام خواهیم داد، میزان واردات به طور قابل توجهی کاهش خواهد یافت.  آنها واقعاً از روسیه حمایت مالی مستقیم دریافت نمی‌کنند.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20467" target="_blank">📅 16:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20466">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeYjRXOkZvx9n7u7QXMH30_n3Km2qheYNyRv49CbLGi_KqpGJCR1bLbuShsniTKvqL1kNG-vSFBslnSgFPNYiW9PwQp0EaR_pgxCT-gdTRb7wQAzgkbjqTY3jnnGbyJR9b-oa9ysiZrzUvsm5-u9zqjnrx9xF8x3IctbNeh8Ktj-NzTw2A56IVxAf00xYwIi-3EOkT5oWGgF_Dd5lY-K4Zo30f-GBysMygbBK0IpNOMDqh0Z1s8RAvvh4G8bOk3_qzfw8Sp0kYw2IuUVW5P0TwhLgMVYwzaHyOFgt_iQJDw9dcmD-Az6ZBgrDMNHdzVvC0vjzpTvZgvxlhfIVrbhIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدانستید این بسنت که اینطوری اقتصاد ما را به خاک سیاه نشانده اساساً Homo است و آن هم مفعول؟!  از دشمن هم شانس نیاوردیم!</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20466" target="_blank">📅 16:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20465">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqYs6qJfuVpZ8WHR5f71xQkCI32YOmLRXPkyhP79U2F0BRzVoL0OShtqZfTXx0KU_IqAzPq_8r06FV8ZgW0O8v4_yZyamrLXyoWXgfUWHbUPrnsUFF37-aWpSPapsyk3rlmzUgXeusGhncsbOFKlC6ghPcTT9ZUWxGShUm-v3v3TVXMA8HCEmynW5XyWPumvbpHimsXjPvGd4aO49etEaSs4lMUaHxyTSEXpFkvyuMXg6vowsezhLq82oW2GWQYgy8-okYu6BE60RoW-LXqNKHrwyDK5PuUR9Rhz3SIPsXideFq_y4oe0PTEYHmOH_y5E30imr-y6FLrCd8MIT5cCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدانستید این بسنت که اینطوری اقتصاد ما را به خاک سیاه نشانده اساساً Homo است و آن هم مفعول؟!  از دشمن هم شانس نیاوردیم!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20465" target="_blank">📅 16:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20464">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">میدانستید این بسنت که اینطوری اقتصاد ما را به خاک سیاه نشانده اساساً Homo است و آن هم مفعول؟!  از دشمن هم شانس نیاوردیم!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20464" target="_blank">📅 16:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20463">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbUgJYnXwhsN3EXD1Q4ehpcg8fSXoOENkiiaZpPFI9jbvfKp-Cur0NphbbW0mmAIPS47FemgxF7IpL1ISDQzaPJ3qoio5g7rasPMlX7H12LRp1LUXyNtj20gEFIIIeaSZcrJcMaIGBDEwlbKIma9OfksFe5g3Q6LreIpTmLtk5e_m8XlUzHtPegChuGnMVWg-DmZSWGlNmU6x-A81CYvFuxgTILyyUPQeyNb4dbBcDN1a2vjqskYlzyknz-Y6STXe7dds0NrQaCsOrfANht4qCzAmCZ2pBlc9x-pdyE7xmqRqbhkY8nfm-InunsvKhMhF8Ak8-YYnp-sO-JGUe62Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی خداوکیلی این آمریکایی ها ترسناک هستند؛ شما فکر کنید هوموی مفعولشان اینطور خشن است وای به حال هتروی فاعلشان!</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20463" target="_blank">📅 16:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20462">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">میدانستید این بسنت که اینطوری اقتصاد ما را به خاک سیاه نشانده اساساً Homo است و آن هم مفعول؟!  از دشمن هم شانس نیاوردیم!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20462" target="_blank">📅 16:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20461">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">میدانستید این بسنت که اینطوری اقتصاد ما را به خاک سیاه نشانده اساساً Homo است و آن هم مفعول؟!
از دشمن هم شانس نیاوردیم!</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20461" target="_blank">📅 16:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20460">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">المیادین به نقل از یه مقام ایرانی:   از ایران برای پیوستن به "توافق مکه" دعوت شده و تهران الان دارد این موضوع را بررسی می‌کند!</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20460" target="_blank">📅 14:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20459">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ارزیابی موسسه ISW  از وضعیت توانایی های ایران برای ادامه اخلال در هرمز:
ایران در اول سپتامبر، در واکنش به حملات آمریکا به اهداف نظامی ایران، از جمله رادارها، در همان روز، به پایگاه‌ها و دارایی‌های آمریکا و متحدانش در منطقه حمله کرد. این رادارها می‌توانستند برای شناسایی و سپس هدف قرار دادن نفتکش‌ها در خلیج فارس مورد استفاده قرار گیرند. فرماندهی مرکزی آمریکا (CENTCOM) اعلام کرد که حملات اول سپتامبر علیه این رادارها پس از حملات ایران به سه نفتکش و همچنین نیروها و پایگاه‌های آمریکا در منطقه انجام شده است. مؤسسه CTP-ISW جزئیات بیشتری درباره حملات تلافی‌جویانه ایران در اول سپتامبر در گزارش دوم سپتامبر ارائه خواهد کرد. فرماندهان ارشد نظامی ایران پیش از انجام این حملات و در همان روز، آمریکا را به پاسخ نظامی تهدید کرده بودند و سخنگوی سپاه پاسداران به‌طور مشخص بحرین و کویت را نیز تهدید کرد.
به نظر می‌رسد حملات CENTCOM عمدتاً دارایی‌هایی را هدف قرار داده باشد که ایران از آنها برای شناسایی کشتی‌ها به‌منظور هدف قرار دادنشان استفاده می‌کند. دونالد ترامپ، رئیس‌جمهور آمریکا، در اول سپتامبر به شبکه فاکس‌نیوز گفت که نیروهای آمریکایی تعدادی نامشخص از رادارهای ایرانی را که ایران در تلاش برای بازسازی آنها بود، منهدم کرده‌اند. ایران از این رادارها برای شناسایی شناورهایی که از تنگه هرمز عبور می‌کنند استفاده می‌کند. CENTCOM اعلام کرد که این حملات پس از «تلاش‌های سپاه پاسداران برای حمله» به کشتی‌های تجاری در تنگه انجام شده است؛ بنابراین، فرماندهی مرکزی آمریکا به‌صراحت میان حملات به کشتی‌رانی و حملات علیه رادارهای ایران ارتباط برقرار کرده است.
حملات ایران در روزهای ۳۰ و ۳۱ اوت نشان می‌دهد که تهران همچنان از ظرفیت‌هایی برای ایجاد اختلال در کشتیرانی از مسیر جنوبی خروجی تنگه هرمز برخوردار است. چندین سازمان اطلاعات دریایی و نهاد ناظر بر کشتیرانی گزارش دادند که در ۳۰ اوت یک پرتابه ناشناس به یک نفتکش اصابت کرده و در ۳۱ اوت نیز سه پرتابه به یک نفتکش بسیار بزرگ حمل نفت خام (VLCC) به نام
Senegal Prosperity
اصابت کرده است. یک شرکت دیگر فعال در حوزه اطلاعات کشتیرانی نیز به رویترز گفت که ایران هم‌زمان با حمله به Senegal Prosperity، یک VLCC دیگر را نیز هدف قرار داده است. رسانه‌های وابسته به حکومت ایران گزارش دادند که این کشتی دوم از مسیر جنوبی تنگه هرمز عبور می‌کرد.
این حملات نشان می‌دهد که ایران همچنان قادر است از سامانه‌های پیشرفته‌تر خود برای هدف قرار دادن کشتی‌هایی که از تنگه هرمز عبور می‌کنند استفاده کند. ایران کشتی‌هایی را که از این مسیر عبور می‌کنند هدف قرار داده است، زیرا مسیر جنوبی جایگزینی برای مسیر تحت کنترل ایران در بخش شمالی تنگه محسوب می‌شود و در نتیجه، برداشت موجود از میزان کنترل ایران بر تنگه هرمز را تضعیف می‌کند. مقام‌های آمریکایی در گفت‌وگو با Axios در ۲۸ اوت اعلام کرده بودند که نیروهای آمریکایی در حال اسکورت کشتی‌ها از خلیج فارس از طریق این مسیر هستند؛ اقدامی که موجب شده حجم کشتیرانی به حدود نیمی از سطح پیش از جنگ بازگردد.
حملات آمریکا به رادارهای ایران احتمالاً محدودیت‌های عملیاتی بیشتری بر نیروهای ایرانی که تلاش می‌کنند کشتیرانی در تنگه هرمز را مختل کنند، تحمیل خواهد کرد. CTP-ISW پیش‌تر در ۳۱ اوت ارزیابی کرده بود که ایران با محدودیت‌های عملیاتی در توانایی خود برای ایجاد اختلال در کشتیرانی در تنگه مواجه است. ایران اکنون مجبور است شیوه عملیات خود را با هدف بازسازی و تقویت برداشت بین‌المللی از کنترل ایران بر تنگه هرمز تطبیق دهد.
مدیر یک شرکت مشاوره و ارزیابی ریسک در ۳۱ اوت اشاره کرد که سپاه پاسداران برای شناسایی کشتی‌هایی که از تنگه عبور می‌کنند، برای مثال، از شناورهای تندرو تهاجمی (FAC) و شناسایی بصری استفاده می‌کند. این روش در مقایسه با استفاده از رادارها و سایر حسگرهای تخصصی، روشی
بسیار ناکارآمدتر
برای شناسایی، تثبیت موقعیت و در نهایت انهدام یک هدف در دریا محسوب می‌شود. اینکه ایران ناچار شده به چنین روش‌های غیربهینه‌ای متوسل شود، نشان می‌دهد که با محدودیت‌های عملیاتی مواجه است.
همچنین، حملات CENTCOM در ۳۰ اوت علیه سامانه‌های پرتاب مین نشان می‌دهد که نیروی دریایی سپاه به‌طور فزاینده‌ای به استفاده از پرتابگرهای راکتی برای کارگذاری مین در تنگه هرمز متکی شده است؛ روشی که در مقایسه با کارگذاری مین از طریق یک شناور، روشی غیربهینه‌تر محسوب می‌شود.
با این حال، سه حمله ایران در روزهای ۳۰ و ۳۱ اوت لزوماً به این معنا نیست که ایران هیچ محدودیت عملیاتی ندارد؛ بلکه صرفاً نشان می‌دهد که تهران در این سه مورد توانسته بر این محدودیت‌ها غلبه کند. CTP-ISW همچنان نرخ حملات و انتخاب‌های تاکتیکی ایران در هر حمله را زیر نظر خواهد گرفت تا مشخص کند آیا ایران هنگام تلاش برای ایجاد اختلال در کشتیرانی در تنگه هرمز با محدودیت‌های تاکتیکی مواجه است یا خیر.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20459" target="_blank">📅 14:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20458">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وال استریت ژورنال:
دو مقام آمریکایی می‌گویند تاکنون هیچ تلفاتی در میان آمریکایی‌ها بر اثر حمله ایران به تأسیسات در اردن گزارش نشده است.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20458" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20457">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آکسیوس:
آمریکا برای نخستین‌بار نفتکش‌های دولتی ایران را هدف قرار داد؛ سیاست «تانکر در برابر تانکر» اجرا شد</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20457" target="_blank">📅 12:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20456">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حملات آمریکا ۴ عضو نیروی قدس سپاه پاسداران را در کرمانشاه کشت - تسنیم|</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20456" target="_blank">📅 12:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20455">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfUQS0iGa2g-16BtgoUjwvud3ly82Dl1HVjB936Qy2nHmrZZLGbetWWH-2op56-hal49jDEUmeHjgOjD_SI1iXo3f-wwLF2RYOhcnmcwUOeGfwv_eIbIQOPRUnov43kOsBT43g9f8PFJExrousVO2TTzbu5YJWxQZb83tdi7Hjy0ip1FtQiKdUGlNw9G4A8wR7NSCmcBSZODZ46hnupyfXc64gB22GcwpVP0icUY01sYkaMm3hfkoyw3J24cY_qGrcJmA35LkkUooHXo7k_2rW6dGUphBFIdVruf7xF3HEKjGlDHyg1cIi-kbIEpLlOMXdslGHlNfGVz32aGBM18RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20455" target="_blank">📅 11:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20454">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">حملات آمریکا ۴ عضو نیروی قدس سپاه پاسداران را در کرمانشاه کشت - تسنیم|</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20454" target="_blank">📅 11:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20453">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMEM5cWUgjE_inPknwxkAsOoqEDxP27i_riZvAsdYjNwZZQcoIZA17X9xUppVYg0UUEJ6Qvj8DVLeb1CDCnw6II6FigUhbdnq5OahoDSEIa_ICT1uGrwd33XfxUPMVmZlwFEHSfDwZXqIf8LI12o1ByqviXqs_T_ZHrJFma3IYSUxGpIhbZkM0fBOE4sQ23DsgV16neSfXL8HDfwEwNHk6Lo8ACZoLE41gl2W4AbJeeUjfx0OFgKbyVyB-SeA6EGQWbO1iET1V5yJd7ZV6kCf7fHoC_F8G1b3B6MsNY7CMsYo3Zch6d4Abckd166w7Bzee59e9Q1s3qcPXHoaH3UqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه ای قرار دارد و با توجه به بیش-فروش بودن تکنیکالی، امروز احتمالاً یک اصلاح رو به بالا در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20453" target="_blank">📅 11:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20452">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حملات ایران به بحرین و کویت1!</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20452" target="_blank">📅 01:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20451">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjzIvXjVWjGXkEkPZ_2PSdm2HOX_Po7O_ImLncwtkYzHaLtQrIiFw6A35QSl0RfjI4lVin58VSlAkRUB8u6P6QZnUL3JPCC5qJsWgx56NIflc6Bt3G6ws-WnKdLp6oNcgXCfkA9o3n_OqHzA1556zqxisWM1ZG8Bf5hOfa-9aJoUHF_YqU-cY4rqMoA8cOq6kwcnGluJssne3Uv9dIiicbCZo76bQskg7D5xYJPQaEXkykL1bz3frOaNeyLRi_b4pfOXuf1DTR9jUzoAH7ab6oYng9PUSO0k6VK4jRV-oMNIooM7ewj-d4YwOLoqcNf-uqNX7TlxVDH2b4m4ANK6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«سپر آشیل»؛ ورود یونان به عصر دفاع هوایی چندلایه   یونان و اسرائیل در ۳۱ اوت ۲۰۲۶ قرارداد تاریخی «سپر آشیل» (Achilles’ Shield) را به ارزش حدود ۳ میلیارد یورو امضا کردند؛ توافقی که آن را می‌توان یکی از مهم‌ترین پروژه‌های دفاعی مشترک دو کشور و نشانه‌ای از تعمیق…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/20451" target="_blank">📅 00:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20450">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">- یونان و اسرائیل در آستانه اجرای توافق‌نامه‌ای به ارزش ۳.۱ میلیارد یورو برای برنامه «سپر آخیل» قرار دارند که در آن سامانه‌های اسپایدر، باراک MX و اسلنگ داوید با زیرساخت‌های دفاعی موجود یونان یکپارچه خواهند شد.  این شبکه مبتنی بر هوش مصنوعی برای مقابله با…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20450" target="_blank">📅 00:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20449">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20449" target="_blank">📅 00:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20448">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بالگردهای ارتش آمریکا برای انتقال زخمی و کشته های خود در اردن به پرواز درآمده اند.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20448" target="_blank">📅 00:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20447">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">#WHEAT — D</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20447" target="_blank">📅 00:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20446">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6L2FMrzW9fW9gqWjQxg1moaEIVt0yrAxoagx8QGNl3FQFZroHDeRRFjLDFmdJJJsx13whSUBW-uhmth3RKPZOzKED16zlcqXwH2rfOLZHQ5ZcGri84rtci7n6uRVjdoJF-bkAYPKK8YyWj6dFkbP5f946XC19NnBm2cER9WhkVjsxHrCCnPWeVfrfhPRUFl7RYFvO047ToVq3G5VR9SV-UzuhVN4-gxqnMO3lwUSIY1_lETvML0fu3U_U_x-D5dRjPzQWJ1tIzB9Be_AIYAyLQKbxECSRSgdm6fYOGcEK9AGLc8Ko_1AYK5APWbBitfiohmCQanKzgKd_lsuFCI1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D  به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20446" target="_blank">📅 00:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20444">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0Eg6gagDv6fsWnFAA0LrxP3ewHrT3FvMIdLOK940e90-8-xqMxkMn61wyGX__BHXwwz7kyBjbnNIPMx2wNvAD4kdskg0kXf5ciP915GEykNZSJFPqs4-Aiyujb8TtI-V1dM56V5y6Ot32yZ2jfT1ECPi_4Ok-GWiqv5kbOHWyY5vnMP1XguCgXR_RAorcpv3dWUoGSwjgppu1Hckaxry2Aku2C_KSaO2PbTnUZQnv3Qy-2CMLhI01a6iehaazFSYPu9OGF2u1TuifHZ91m0EjblrUR1lu9U0ykp8yNAY9hcPKDT0s-3YnM2RdkQFlTIRXzoBiyftMA4hxVU4lzfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42fd12b2d1.mp4?token=vXSwBqaeNZWjaQy_YJquf0cROlo06xusgZvHYGdqHqCbnjVsefP6a6FrmZs3-cfSRXfp54SLpWmG6O151E1oFTO1ACAy_slo-R3OqrfSL2lfcUiUvuMistt75m3DT7CvsCOSUZeOCRoU-eFds4bHf-bzHRfxiHTKook2V8iYJAidU06Pysyo-rce2hFGww98bIk7UrcK_gA57R0IxXNccKfbVfdWsKS9CjgYyRJGimXnla71YosaHeZtvoltcqYrjOSgY5_FwPTZGxBDQ9yYFck0TaiKD9RPlJ759fqzrqiWJ4fsa0jJNwDkTw1Jx1j0HD04ChGbGsSg5Q4kqk45JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42fd12b2d1.mp4?token=vXSwBqaeNZWjaQy_YJquf0cROlo06xusgZvHYGdqHqCbnjVsefP6a6FrmZs3-cfSRXfp54SLpWmG6O151E1oFTO1ACAy_slo-R3OqrfSL2lfcUiUvuMistt75m3DT7CvsCOSUZeOCRoU-eFds4bHf-bzHRfxiHTKook2V8iYJAidU06Pysyo-rce2hFGww98bIk7UrcK_gA57R0IxXNccKfbVfdWsKS9CjgYyRJGimXnla71YosaHeZtvoltcqYrjOSgY5_FwPTZGxBDQ9yYFck0TaiKD9RPlJ759fqzrqiWJ4fsa0jJNwDkTw1Jx1j0HD04ChGbGsSg5Q4kqk45JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20444" target="_blank">📅 00:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20443">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inXT_-1JneoWVtfH3lz1xq9UomZIKcJRO2gPC6w93u7-S5ZHsvEcVTX7a1dqWbz-smfVjG78Ae3f4FjCno13QY379MSJ68MC7xdAeJvYpY2IAkXnQCFhWsgIyGyOEM4uHZ-aAo5SB0Z0YleC56ay85pVLQSGUlEPRPFV1pMsIehcwrM0dLHimuf6ACIYcXPB7JCyD6OouH7apTS5Xpm2AhnH7FObWGU35rM-9sM8Pgm2EyeAJx3xzLzUeQZ1CH3Wcs_JuKR6Qlaa35vH3duWq1BhzARiSEKWYQhEwNhrtVc25GTwDT39G-4zXE9AaK3WdL2kW7ConCsI2yKi2QbL8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفاً یک نفر لفت بدهد میخواهم معنی 10666 را از آرش بپرسم. ممنون</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20443" target="_blank">📅 00:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20442">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crbCMetnxaTzGx1ATNUsRyLrv58OYTuvbSM7sH3jkU3zr9hVS6BQ3Kysz3tMCDeeJ2uCrGSvTh11LclGRSYOiURSSir6DE5r6ySo_JcAvYKfUjUc-qouzXRJx8z3r0BzgGM57kAbcSiazuoNRsBfTOrImeO3m49ocE90wUPGPO7lQNfTBzbI6VqLCEh8ez0KzRdizGZZlB937qlT0s0J5r9Yhs4IUIe7NNeJfiPDaZBM3xSqs6R9xYEwjaEhMpI8OhmX_ZlDay8kt7SQSDH0C-9wFJUCyW9zuTfNhhXnEiH8DqGxR3UItqwLLIHcltSoLq4psKVBeEWvTq00dB1PmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفاً یک نفر لفت بدهد میخواهم معنی 10666 را از آرش بپرسم. ممنون</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20442" target="_blank">📅 00:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20441">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ
🔹
ملت قهرمان و بپاخاسته ایران اسلامی،
ارتش تروریستی و شکست خورده آمریکا، عاجز از رویارویی مستقیم با رزمندگان اسلام با حمله وحشیانه به یک منزل مسکونی در سیریک، محل مجلس عقد دو جوان پاک را به خاک و خون کشیده و با به شهادت رساندن و مجروح کردن نزدیک به پنجاه نفر از مردم عزیزمان خاطره وحشیگری مدرسه میناب و ورزشگاه لامرد را زنده کرد.
🔹
رژیم کودک‌کش آمریکا در این حمله جنایتکارانه یک بار دیگر با به شهادت رساندن چندین نفر از جمله یک کودک، عمق کینه‌توزی و دشمنی خود با مردم ایران را آشکار کرد.
🔹
در پاسخ به این شرارت سبعانه، رزمندگان دلیر نیروی هوافضای سپاه در موج دوم عملیات تنبیه متجاوز "با رمز مقدس یا رسول الله (ص)"
با حمله سنگین موشک های بالستیک به پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تیتین، واقع در سواحل خلیج عقبه
، تعداد زیادی از نیروهای آمریکایی را به درک واصل کرده و چند تاسیسات مهم و بالگردهای هجومی دشمن را منهدم نمودند.
🔹
عملیات انتقامی نیروهای اسلام
ادامه دارد
.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20441" target="_blank">📅 00:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20440">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">باز ما یک سفر آمدیم همه چیز به هم ریخت....حتی سفر درمانی ما هم بی عوارض نیست چه برسد به تفریحی</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20440" target="_blank">📅 00:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20439">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ساعتی قبل یک خودرو وارد تجمعات شبانه در خیابان اقبال لاهوری (مشهد) شد و جمعیت را زیر گرفت، چند تن نیز کشته و زخمی شدند.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20439" target="_blank">📅 00:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20438">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔹
موشک بالستیک سپاه به سمت اردن، که از اسرائیل مشاهده شده است
⭐️
@AkhbareFouri</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20438" target="_blank">📅 23:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20437">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار فوری | اخبار جنگ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10aa2a3f52.mp4?token=WwflGiYDN9loN9dh3z-lBwne3BbLqhShAv5IuHVQdCWVjUyQKgfwNaR6cLz6vELBxBjC9vQc2yx3NsT-qJGHt-j-umdNpyVb2LCtiKs7XTlj7AP-Q7gesQi7u6VH9b1R8okK-rE6ANpQSPRiiZozfKOWdvHIAd2sV6ErdfP1e9xHgmpLePHEAWBHhxngMgBK8U4LmoyV9cupJPnJaV7a0QeGMEeS4IrlHhSFZpkYb4YdQeuOxLdEhQdaL5tGsaZyBjIMFgbanCBDS0ld3rO2s-AzIYpE5dL6yVejC825p93pE8OsGMjnvr8qPUHGgXfI4y9goiBDwxEAvJ0ETOvHjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10aa2a3f52.mp4?token=WwflGiYDN9loN9dh3z-lBwne3BbLqhShAv5IuHVQdCWVjUyQKgfwNaR6cLz6vELBxBjC9vQc2yx3NsT-qJGHt-j-umdNpyVb2LCtiKs7XTlj7AP-Q7gesQi7u6VH9b1R8okK-rE6ANpQSPRiiZozfKOWdvHIAd2sV6ErdfP1e9xHgmpLePHEAWBHhxngMgBK8U4LmoyV9cupJPnJaV7a0QeGMEeS4IrlHhSFZpkYb4YdQeuOxLdEhQdaL5tGsaZyBjIMFgbanCBDS0ld3rO2s-AzIYpE5dL6yVejC825p93pE8OsGMjnvr8qPUHGgXfI4y9goiBDwxEAvJ0ETOvHjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
موشک بالستیک سپاه به سمت اردن، که از اسرائیل مشاهده شده است
⭐️
@AkhbareFouri</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20437" target="_blank">📅 23:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20436">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یه کویت مون نشه؟!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20436" target="_blank">📅 23:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20435">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مرندی ذوالاکتاف:
با توجه به اظهارات ترامپ و بسنت، به نظر می‌رسد که روزهای رژیم‌های خانوادگی عرب در خلیج فارس به شماره افتاده است. آن‌ها نمی‌توانند از جنگ پیشِ رو جان سالم به در ببرند.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20435" target="_blank">📅 23:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20434">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">جهت نوسانات رو شاخص درست تشخیص داد (رو به پایین) اما شدت ریزش قیمت با تحلیل ما سازگار نبود.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20434" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20433">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFe0uL8je375xpDO6j8fQswa4C85W7GI2D1He0ImquMYPpMBKnB4iwr29U0ZG2oN4lSSZEIOjxepaYsMZFnzhzQBodRL1erL4XIkxZ8oGwuA-iycbM8HR35RP5z2KfXpSfUgpL47-3TUyTl4zhbqjR4FbSePcUqxW4IGYA6K2e7UzhSUfk3APUBdiByXcH-P_1wv1Wp6TcCwvswNKs7b8C_skN7Wh9kvnaTAym6lEMC-o8cpD5aS4uPJPpF5-mXIyNXPhtcNNWzbCH2OuktJVoXpq8yYKos-cNMcHwbvOX4styR1u5E9zE4xZ5S7hTllduDvISvOYruWotq1XaJdFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه بالا قرار دارد و بازار رنج و کم نوسان پیش بینی می شود.  با توجه به روند عمومی نزولی در 1-ساعته، فروش در سطوح مقاومتی (4477) بهترین راهبرد است.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20433" target="_blank">📅 23:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20432">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شلیک موشک از تهران!</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20432" target="_blank">📅 23:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20431">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پزشکیان:   همهٔ اعضای شانگهای بدون استثنا تجاوز به ایران را محکوم کردند</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20431" target="_blank">📅 23:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20430">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پزشکیان:
همهٔ اعضای شانگهای بدون استثنا تجاوز به ایران را محکوم کردند</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20430" target="_blank">📅 23:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20429">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یک درس دیگر هم این بود که در جنگ با آمریکا و اسراییل، باید بیشترین موشکها و پهپادها را توی سر‌ همین جهان اسلام زد تا بهتر بشود جلوی شیطان بزرگ ترسمان ریخته بشود.</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SBoxxx/20429" target="_blank">📅 23:09 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/fldyJwPOM5x17hiZWuEO6bH7Wq8f60iZcvc01qljUUbhex_jc_galL05S73ryRqoHxT7bGScSDtOYwttEXmiWO_-Kb82fZB1thcxRkn3Q904gzMShbMrpP_WgOVBJT-828PH716NZ9YZgDLdF2dqPaHFPjn9ffMyE4RuCaf8QY4FxOOYGRPjpyfpwuBJCbepgO4VC4RyMI4_o0XCpcx43ukyLPA36uFJHyqvH1Q8hyjFylwZ3BQn2piKf0-lGYrW4JBtrYlWD4uUEVI0KStxKv-zDJbdEV_OsOU7Xlw-4Jn9ob8u_GrU8Ci4tB1R260yF4-XfaQAf1qNMQU7hwKVxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 13:46:06</div>
<hr>

<div class="tg-post" id="msg-451588">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فعال‌شدن آژیرهای هشدار در قطر
🔹
رسانه‌ها از به‌صدادرآمدن آژیرهای هشدار در قطر و همچنین صدای انفجارها در این کشور خبر دادند.
🔹
منابع خبری گزارش کردند که انفجارها پایگاه آمریکایی العدید در قطر را لرزانده است. برخی منابع همچنین از هدف‌قرارگرفتن کشتی‌های آمریکایی در نزدیکی سواحل قطر خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/farsna/451588" target="_blank">📅 13:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451587">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjSWglgdl6_8ZAYamaBly516E_LtB_wzvloqMVO1ljT_4FqTFydMFTcstlKPQSSBd2UxMCXfvCDJOG85bzJGZxw9QaxIQEscMokPYgpzYJa_NX4ZIAkRtCgMefyu-DuBjQDbV2tIiON_NnzoRxXnWCSdH4koQmRH_0JgSlD9b-QxRpE6r_NRwgJpDqliZrUIwNSSGEMcqcSWrh8QTaSLKPd7ZQRcHOIZ5rMKRGPfgLx2SnFopYj19MSzisVnRq1X5-EkHTpEgfUE3DWcvpVxNlBg8K-r5CqtbuZy_IbJMcP_pLmIxoInSBk2J7VWzazLHmzd0SZThKcOgeTxLXyt9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو حزب اعتماد ملی: نگاه اصلاحات به غرب باید اصلاح شود
🔹
مازیار بالایی: اصلاح‌طلبان باید مفروضات گذشتۀ خود را مورد بازخوانی قرار دهند و با توجه به تحولات داخلی و بین‌المللی تحلیل‌های خود را به‌روزرسانی کنند.
🔹
میان ساختار تصمیم‌گیری این جبهه و بدنۀ اجتماعی اصلاح‌طلبان فاصلۀ قابل توجهی وجود دارد؛ مسئله‌ای که بر کیفیت تصمیمات این جریان اثر گذاشته است.
🔹
تحولات مهمی همچون خروج آمریکا از برجام و جنگ ۱۲ روزه نشان داده نگاه این جریان به غرب و الگوهای گذشته نیازمند اصلاح اساسی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/farsna/451587" target="_blank">📅 13:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451586">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9KDlIR96j2QTHcFgsfzFx-MBB0Pj__0ty8aS7xavdmmMiOpMrGY17PqQybPRMhvL0kL9zWYOFA2GbtJUQXG4FtqrsQP8RFZvR_mHNUCcwAk4Pyyv_YnqBfobtV4oWLK2YSDETPIB6P2bF7KgULjLmj044OWoZs4mMbpDknEkjTK5hFciaiAOVabbDMxSGUItzr_G4nBYO3YCeAQimXr2baF4XKQn5bUllx3hTiFkKRfXc5xFyn1fc1uVMgCYXIzVMGwf9SYXax7m4XlbyU2KpRib9VpXYXcUe3x6sSzPKdJS8TbvZLk9iVKLCGb-UaKFQX9Cgntie1YASf-EGXvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف پل حافظ تهران منتفی شد
🔹
نیم‌قرن پیش پل حافظ در تقاطع خیابان حافظ‌ـ‌طالقانی ساخته شد و قرار بود چند سالی به‌عنوان سازه موقت باشد. از ۲ سال پیش ماجرای حذف این پل کلید خورد.
🔹
اما رئیس کمیتهٔ حمل‌ونقل شورای‌شهر تهران امروز گفت که هزینهٔ احداث زیر گذر به‌جای…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/451586" target="_blank">📅 13:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451585">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای هشدار به‌صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.  @Farsna</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/451585" target="_blank">📅 13:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451584">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای هشدار به‌صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/451584" target="_blank">📅 13:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451583">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRCoq4ClzK7enD08y4PGYTJRdUi8v7W1Pn7Xd7WhRppXLBKtEW9mqF3O6Zk7nbIkE0nQFxgemxuw0pgEMcZw4V7RZOHwRnQHWtggeY96FNZ2r4YYDh6oYKBN-QJeJNTCGdEQeGgCnrh_JOVcPIw8QjSLifyrgyUIv3qhx_qgZSaNFimn1XhlZh3Rnb5ECjiZbLqvGg7djW9YuIGGAmMK5mPOhVWAErPegFTAInCo8DlxlsA3QYKITenCg981R8g7AX9CABsx_SdV080oPqzZxOijqYgWEOAoqFr-jJ9zWUv3lw987uF9G3nv1e8n8XiI-SA0BVd1NucuX7DeiRDYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با جهش ۷۴ هزار واحدی به ۴ میلیون و ۸۸۸ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/451583" target="_blank">📅 12:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451582">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiiYRbng3NaHiAC-GG1EIbVq87xsKuxFOU__MSXy71tY6_0Td1HQZ_CKBxCCmpban3lg7LAL4rJZDrNpWAel4hWWy3fMqioWeDsUBzXJ8zGnR-TjOotzRnPDEAfZXdrpcU5ig8Ksc500eZb6IN29_JD0piys6G2tdlc1qPa-jhMJpVOUTlmdI39Xq8PtgYtjdakx3XGp5YkqCIDQeAKOXmKNTiJddc5tPTeZ7YpAkgCuiUtwp_KsCgfGFgLitY8hR9grf8mUyS2tbk_iMLT2JsSBDLO57pja10FJcApTfGTFVVLbIxlWWoAKai2VmDifRCmL50JB_p-W9YRwr6jS4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرکشی فرمانده نیروی زمینی سپاه از یگان‌های عملیاتی در خلیج فارس
🔹
سردار کرمی در ادامهٔ بازدیدهای میدانی از مناطق ساحلی و جزایر راهبردی خلیج فارس، از یگان‌های عملیاتی تحت‌کنترل «قرارگاه مقدم مدینهٔ منوره» سرکشی و وضعیت عملیاتی یگان‌ها و سطح آمادگی رزمی رزمندگان را بررسی کرد.
🔹
سردار کرمی با اشاره به جایگاه حساس این مناطق در راهبرد دفاعی کشور گفت: آمادگی مستمر، آموزش‌های تخصصی و حضور مقتدرانه یگان‌های نیروی زمینی سپاه، رکن اصلی امنیت پایدار در پهنه آبی خلیج فارس است. رزمندگان سلحشور این خطه با تکیه بر روحیهٔ جهادی و هوشیاری دائمی، سدی مستحکم در برابر طمع‌ورزی دشمنان ایجاد کرده‌اند.
🔹
به‌فضل و عنایت الهی، مردم و نیروهای مسلح آمادگی پاسخ‌گویی به هرگونه شرارت از سوی ارتش متجاوز را دارند و انتقام خون قائد شهید امت و فرماندهان شهید نیز به‌زودی گرفته خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/451582" target="_blank">📅 12:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451581">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار و اصابت موشک در نزدیکی شهر الازرق اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/451581" target="_blank">📅 12:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451580">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a53d40f85.mp4?token=gBFBV8tPoff-YYzzN92p0yAOFTrPA5NP-hJa0Cr0Y0ycQXUSYkNb4x--lBlzBu6aqKOPIwu9rVyZ7wAVqdwsKJyQTJNUtSg2bAoU1gZ8Gu5q3hwS8NhheEiKSxzBPPqTnSgwJQvfPgJZqfdhro-OD0PMp-5CDjQN_78WrgWfauNsuiqIEmIfMt8AiQj1D_jUAVzPidl1iQLuSSj6nBNbYPI05D8b14JaNUzt2NZaxfakzJLh1mtoZ1HmQi1uAQxQwWZBzva5jD7Qyw4jAbNwCtJrlGA7prUNN5rMoP_QY4o_ncTBNbwDNNcpmFWrHVoxTUBeO2KRw5U68U5H9KWo34cfgDao9at29oChbl65bX6P5AaNIO1ln_cTo5NiweZlLJdIDi6T8KqA_h8blWBaHkzQI6Y-p8Dcp27a0zWORne6Jm58Z_UKnKvb0YAytIMjO5CcLq4yQgm52j_9iZ44alb5z85WwKer0KrRpF2PdSXy-2C5aifqffqqX9jHogqttuPUgDPw1CBdrKvcsoVXrgGsxa6y2R8QrOvpvX26yOH2KppiC8DrHCjo5PVJUHNU2wZrbA2dcGU8XqOaLxwqyryoN_9_SpPPnuWP-HOzqtY3bOp9dkXZ5KScEUiCQ7wH69GMP0Epait-Wu92ECHF3MR_1EaR8dAkEJLiJjJiwrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a53d40f85.mp4?token=gBFBV8tPoff-YYzzN92p0yAOFTrPA5NP-hJa0Cr0Y0ycQXUSYkNb4x--lBlzBu6aqKOPIwu9rVyZ7wAVqdwsKJyQTJNUtSg2bAoU1gZ8Gu5q3hwS8NhheEiKSxzBPPqTnSgwJQvfPgJZqfdhro-OD0PMp-5CDjQN_78WrgWfauNsuiqIEmIfMt8AiQj1D_jUAVzPidl1iQLuSSj6nBNbYPI05D8b14JaNUzt2NZaxfakzJLh1mtoZ1HmQi1uAQxQwWZBzva5jD7Qyw4jAbNwCtJrlGA7prUNN5rMoP_QY4o_ncTBNbwDNNcpmFWrHVoxTUBeO2KRw5U68U5H9KWo34cfgDao9at29oChbl65bX6P5AaNIO1ln_cTo5NiweZlLJdIDi6T8KqA_h8blWBaHkzQI6Y-p8Dcp27a0zWORne6Jm58Z_UKnKvb0YAytIMjO5CcLq4yQgm52j_9iZ44alb5z85WwKer0KrRpF2PdSXy-2C5aifqffqqX9jHogqttuPUgDPw1CBdrKvcsoVXrgGsxa6y2R8QrOvpvX26yOH2KppiC8DrHCjo5PVJUHNU2wZrbA2dcGU8XqOaLxwqyryoN_9_SpPPnuWP-HOzqtY3bOp9dkXZ5KScEUiCQ7wH69GMP0Epait-Wu92ECHF3MR_1EaR8dAkEJLiJjJiwrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کادر درمان پای کار جنوب ایران هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/451580" target="_blank">📅 12:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451579">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rxrkt8PHu_hDDS-zelS28FJjLOZzJdB0UdxZehHbkjw3RLNHpxlPxjTlaRdw_yoOsa2gv5f1oml1JSkNibYNx-A1sDYjSh0oSCXsGTdd9Kwn8eG8R-M-Jk4DqlZOmCfycpCXa2an9rDrT3xBRdr7omEnLyGAJli7vPCKsApCCtKkyEz5elAHeok0KsaVNXXlwp2XHt64x8hePOcGT_WTZlBCh65Ms5rBeET3Og3r0rdAf5P9qKhmnhiVb-8oMchtYa2lUdDSd-8i68pwCECWNF1aF259qIrNDaSixItnBt2Tl6ro-zoVOd5-sfuq_mBUqYK6_9_WJSJn5zHe-lUlkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
۱۴ میلیون و ۸۰۰ هزار نفر با مترو</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451579" target="_blank">📅 11:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451578">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XURPvQ-jGwVbroIg3oQ_HkdC4sQbOAtLEYy7lOhEjQIxj8qyCzjeaFO01WK1Y7hwMNP2Cynz2HYapbjwUUKbZy8yjteS68eaua1sZuXNRoyFDSD2TeEQEfBpCj3-qmrpZZvU_5D4rlhhXenZGJiJao6QKJ-px60sVVgGdcXlxdDDyzbSOYme1d7_HuX95w20GlZZvM2lt2M7SCA6a4T3wt5jO-R0xCUBR8bktzj_EQUkAfYkmuT-8m1Q-zaRCnJuyOIW9ZpOc59vHdBcW8FTcLjdZKI5OQt7xK0Mee6pNLojAdvBJ6s-bYyJNZA_U48_LR7r6mJUnRL_ELgCADVUQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بهرام گودرزی مدافع ۲۱ سالۀ فصل پیش آلومینیوم ۵ ساله به استقلال پیوست.
@Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/451578" target="_blank">📅 11:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451577">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nL9x5w3mdAX6rdLuxvJt09I8qD-anh16SmhVYvGzKK7nvHZwiXLdzsUa15hbSqYJ63eMzv2WYBDWsWJ1GhmjJ7zVGt0-vu6PETsfwODfFJS2HxiKWjAE84wD1NNCwop6Gnq2Z8fLRdCdWuAiV5TlcgjtmWOhiZV16m0uFPe94ypA5nEIYJVDQnzhl9r0xykUj3ywSTH-aCW-Wjwd-U3KaxeGReAnXNrILSmwF8v6-2cTkrSE-DAGrlu6U8VJ8UplcLCc238_X71G_N8zq8tBVBb-Liy7jR9OH9wP7ZWO5i90YLgVHiBLs0PhnxrdQsSzzu88IdKCNq-iaEWVA7BUlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حمله به یک کشتی در تنگهٔ هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس گزارش کرد: یک کشتی در ۱۷ مایلی دبای امارات هدف اصابت یک پرتابهٔ ناشناخته قرار گرفته و سیستم هدایت آن از کار افتاده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/451577" target="_blank">📅 11:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451576">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208cb5a281.mp4?token=ErNe3LjrPtjYEoRWRqb12daagWwmI3RPr7QxnpytV5s7XpTHhieK2neE_SmsP0c9DtXUKPea7aXyNGCkA2R0zTw7SVTMq5LGlPqh8cLlZx03kxwpZrLTMwUf0QJwinEdQTFlF0BUONPEANp1YPt2es5G-Z-GnV6xP3CGRh7OdgbUuQAQBh2190in2AEX7Yg93udQRwC436CJpKV-IPfuRXRkPzl9vZmpuHYGm-wConuD_uzwgmdxFvnqoSJ8YozzkXfbYmF5QXmeChkap9xrIT2spdDh0KO45sVdGxgkyrcq8IZwdNM9Minbzy6Sy84hJFE1bh5HLR9LdddR_BmmBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208cb5a281.mp4?token=ErNe3LjrPtjYEoRWRqb12daagWwmI3RPr7QxnpytV5s7XpTHhieK2neE_SmsP0c9DtXUKPea7aXyNGCkA2R0zTw7SVTMq5LGlPqh8cLlZx03kxwpZrLTMwUf0QJwinEdQTFlF0BUONPEANp1YPt2es5G-Z-GnV6xP3CGRh7OdgbUuQAQBh2190in2AEX7Yg93udQRwC436CJpKV-IPfuRXRkPzl9vZmpuHYGm-wConuD_uzwgmdxFvnqoSJ8YozzkXfbYmF5QXmeChkap9xrIT2spdDh0KO45sVdGxgkyrcq8IZwdNM9Minbzy6Sy84hJFE1bh5HLR9LdddR_BmmBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: تعدادی سرباز آمریکایی در منطقه‌ الرُکبان اردن به‌هلاکت رسیدند
🔹
روابط عمومی سپاه: ملت بصیر و همیشه در صحنه ایران اسلامی، با دعای خیر شما عملیات تنبیهی رزمندگان اسلام علیه دشمن آمریکایی با موفقیت ادامه دارد و در ادامه موج ۲۴ عملیات نصر۲ رزمندگان هوافضای…</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/451576" target="_blank">📅 11:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451575">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVI7SHaX6n3GIFUzeHWhmpHzvoR_fWwBJoB0pOvdT8VNLC__WEKsyEh7hrNCoOK89RRHpqcwgj2gCOMtq7wy2OXpubETN1BOjnKUNS8U4Yfwnd2Jx-HuLvbzzsWWyiRnjdnxMv_7xJbGyhd3XmgpcoB0Q2temPAsOj4vCkj0RCVXbTy8iemjj78wJmXC7MhxYGTcKk1tKdMgK3HDCjf_3x_E_kjTM7EACn_38v9ouTi5_4pSLfZvihrIU6TO7X6cp4VoJJOFh0wTUwU-lzGT-cu5lmNlD8kTKJXYRNIe0hFqFhKunVVZ47CMaxSa7OI5XbuOjgqFNEoeR3DA2it7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت و نان عربستان در حلقهٔ محاصرهٔ یمن
🔹
نیروهای مسلح یمن با اعلام محاصرهٔ دریایی عربستان در تنگهٔ باب‌المندب، مسیر جایگزین صادرات نفت این کشور را هدف قرار دادند.
🔹
عربستان که برای دورزدن تنگهٔ هرمز، بخش عمدهٔ صادرات نفت خود را از طریق خط لولهٔ شرق–غرب و بندر ینبع به دریای سرخ منتقل کرده بود، اکنون با تهدید جدی این مسیر روبه‌رو شده است.
🔹
کارشناسان می‌گویند در صورت تداوم این وضعیت، عربستان برای حفظ مشتریان آسیایی ناچار به ارائهٔ تخفیف در فروش نفت خواهد شد؛ موضوعی که می‌تواند سالانه ۳ تا ۴ میلیارد دلار از درآمدهای نفتی این کشور را کاهش دهد.
🔹
همچنین اختلال در این آب‌راه می‌تواند هزینهٔ حمل‌ونقل و بیمه را افزایش داده و قیمت مواد غذایی، دارو و سایر کالاهای وارداتی را در عربستان به‌طور قابل‌توجهی بالا ببرد.
🔹
طبق برآوردها، در صورت دور زدن باب‌المندب، زمان سفر نفتکش‌های سعودی به بازارهای آسیایی از ۲۴ روز به ۵۴ روز افزایش می‌یابد؛ اتفاقی که هزینهٔ حمل، مصرف سوخت و بیمه را به‌شدت افزایش داده و موقعیت صادراتی عربستان را تضعیف می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/451575" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451574">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbc6a1ed87.mp4?token=rFivLev8G1h3_Ng6JvKlTp1De0AusohR4Nwfgv23GfUQYEEJRPFK8-YYpKyjCswTZCJpIC7Wqlf_e-MKCQlnJPbDpAi51Yd_D8_ddJ7P_2Nq7Puorz3YKiEizlWSSy67ZOoxT_-gl_q0JG5AUUOrjId8s-G_cMjED1RFnwjlc-jG2bEeW9AWtCE4k6IHg4ihMw4YqhFQn2SZTkbGuXkJKXZzEo8D_RpFJi6UTKUCSQ03gAV-f2iVnDS4G_Gh0HgCUYybY0H-x0h_cj7r8hSiE3VmeEVzUGJNEe_XQaYdSwvJE9VmWQw48V-ZmdMq1ukRXNaetLqEavShpN8wm-3Kgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbc6a1ed87.mp4?token=rFivLev8G1h3_Ng6JvKlTp1De0AusohR4Nwfgv23GfUQYEEJRPFK8-YYpKyjCswTZCJpIC7Wqlf_e-MKCQlnJPbDpAi51Yd_D8_ddJ7P_2Nq7Puorz3YKiEizlWSSy67ZOoxT_-gl_q0JG5AUUOrjId8s-G_cMjED1RFnwjlc-jG2bEeW9AWtCE4k6IHg4ihMw4YqhFQn2SZTkbGuXkJKXZzEo8D_RpFJi6UTKUCSQ03gAV-f2iVnDS4G_Gh0HgCUYybY0H-x0h_cj7r8hSiE3VmeEVzUGJNEe_XQaYdSwvJE9VmWQw48V-ZmdMq1ukRXNaetLqEavShpN8wm-3Kgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایگاه شیخ عیسی آماج حملات پهپادی ارتش
شد
🔹
ارتش: از بامداد امروز و در مرحلهٔ بیستم عملیات صاعقه، پهپادهای انهدامی آرش در چند مرحله محل اسکان و استقرار نیروهای ارتش تروریستی آمریکا در پایگاه شیخ عیسی بحرین را آماج حملات خود قرار دادند.
🔹
پایگاه شیخ عیسی از کلیدی‌ترین تاسیسات ناوگان پنجم نیروی دریایی آمریکا و مرکز عملیات ارتش متجاوز این کشور است که عملیات هوایی و کنترل پهپادها از این پایگاه هدایت می شوند.
🔹
عملیات‌های تهاجمی تا بازداشتن دشمن از ادامهٔ تجاوز به کشور با قدرت ادامه خواهد یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/451574" target="_blank">📅 10:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451573">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZN1Lc1KDW7hzOLK2MBYg6AvACNTHdycZs-Eah2ycza1J5MmaiEBis3uicdyG_K7sj8FC0kf3moc_NvYIO9e8qxxT0uAkgnx1I3Ubrnu_bhH9tFPfCz-T8dx4VUmoZk3ZqYDMly1mX4J_XzFusRpHySfu52uy3fbrhxIJe-kIMCJ1QapA0pp2Yewp6Cxy5100kuXnGokLMwBjJ_G9FYVbyW2ZfWPWyZpmJmSMtJYk5y9RYEpJ6TD7OiHAPZOLgww8ZacBqjxtQOeX_RML_4np2EEivkbSqXrGAsEbMpJ4vH3yvewKFgTzov5z13BWBEhF844OEvUICWbMkbS7leCogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اعلام کد اضطراری توسط سوخت‌رسان آمریکایی بر فراز خلیج فارس
🔹
یک فروند سوخت‌رسان نیروی هوایی آمریکا که از پایگاه هوایی الظفرهٔ امارات برخاسته بود، بر فراز خلیج فارس و در نزدیکی حریم هوایی ایران کد اضطراری ۷۷۰۰ اعلام کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/451573" target="_blank">📅 10:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451572">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌  شورای نگهبان با برگزاری مجازی جلسات مجلس موافقت کرد
🔹
سخنگوی شورای نگهبان اعلام کرد مصوبۀ اصلاح آیین‌نامه داخلی مجلس دربارۀ برگزاری جلسات در شرایط اضطراری، مغایر شرع و قانون اساسی شناخته نشد.
🔹
براساس این مصوبه، اگر به تشخیص هیئت‌رئیسه، برگزاری جلسات در…</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/451572" target="_blank">📅 10:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451571">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01a320bc1.mp4?token=XHVSY4y1FlMUkINyueW5fUVgB_vxDLHgkvJdfJR0nM9_znj-QCMNXUi3Klokgh67jLlnSd3Hal2S8kPsNp5shd30Fv8KXfb1owJEJMjOQQLUH4OZ2aIJVJH3pWGnUtGxjybbz4_VQ3CSHMoYbHekCTn24ZEV9UBYgbtqKakojQSI1tD_kv-KKQXepl9S1m0AeypytW8_M_GHtZegXG00u9_F_SD8y02q9tb_hX84_gngGi4pxI4geAsMr4KYiSxjOVBetQDfPENwbMMt9K9bRzTqfTTqVyxmZm7NfvDTGqK4nQKpwy8cpyyMFHHwrYS0IAQHWptL_Tw1N2sVpmLI2IwumcXNRTLHYo_q_o6XVmbAu2hFconX28vUXamMqkxBCJFPBNQBO3q7AD084Xn2Bs_t5y2Z2fFcte9tzeHxyDJ4exQfCCrFdnjahzqurKw3I4XrrZoSGFvGvbFrz5Y4kSaB_vrt2vFy1Y6D6zBUX94AYGvdHMjYw6gkFwoaVnlOoraXllpbSjVmdnb0AaLNfzRy5iYDvFx8qF7Tvv5_52ekGv9FF5GEWg7EWyjDmxyWCnpOrG1WxWAU4CEtfXaPdl70Uuj2uLmWjsH-j0FIN-NHQbrqNOLlHPMS4zQyPwiPWlRmW_EpswfmrQ6a3wnlJ-L799xrIFirYKSIbh2Na9Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01a320bc1.mp4?token=XHVSY4y1FlMUkINyueW5fUVgB_vxDLHgkvJdfJR0nM9_znj-QCMNXUi3Klokgh67jLlnSd3Hal2S8kPsNp5shd30Fv8KXfb1owJEJMjOQQLUH4OZ2aIJVJH3pWGnUtGxjybbz4_VQ3CSHMoYbHekCTn24ZEV9UBYgbtqKakojQSI1tD_kv-KKQXepl9S1m0AeypytW8_M_GHtZegXG00u9_F_SD8y02q9tb_hX84_gngGi4pxI4geAsMr4KYiSxjOVBetQDfPENwbMMt9K9bRzTqfTTqVyxmZm7NfvDTGqK4nQKpwy8cpyyMFHHwrYS0IAQHWptL_Tw1N2sVpmLI2IwumcXNRTLHYo_q_o6XVmbAu2hFconX28vUXamMqkxBCJFPBNQBO3q7AD084Xn2Bs_t5y2Z2fFcte9tzeHxyDJ4exQfCCrFdnjahzqurKw3I4XrrZoSGFvGvbFrz5Y4kSaB_vrt2vFy1Y6D6zBUX94AYGvdHMjYw6gkFwoaVnlOoraXllpbSjVmdnb0AaLNfzRy5iYDvFx8qF7Tvv5_52ekGv9FF5GEWg7EWyjDmxyWCnpOrG1WxWAU4CEtfXaPdl70Uuj2uLmWjsH-j0FIN-NHQbrqNOLlHPMS4zQyPwiPWlRmW_EpswfmrQ6a3wnlJ-L799xrIFirYKSIbh2Na9Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهره برداری از ۳.۵ کیلومتر دیگر از بزرگراه جلفا- مرند
به همت سازمان منطقه آزاد ارس و با مشارکت اداره کل راه و شهرسازی آذربایجان شرقی ۳.۵ کیلومتر دیگر از بزرگراه جلفا- مرند به بهره برداری رسید و بدون تشریفات خاصی افتتاح و زیر بار ترافیک رفت.</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/451571" target="_blank">📅 10:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451570">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q96xtvyFeOJVmtALCeeSUrs5rhQz0vG8DmFO-3tEPpswvbtbFn-OgKT5pZjGyQLi8eeMEFjY6bWI_N9duYMSYicvVub7dyQsxIqYmet66bMgxLCTK_YXXU8LrvHEEN_tP1Q2BTXiGXKKaL5Xg4EwTPpjqYj66nUflvDI75gTHyCMZ564-w7DGkkPvfXNt1fI7O24xvTIo1TCjv5FkGMi8MicnWHWHaXGznKT-yPHdmqLS9JpMA-spfBE9Ue270VU5EpuzX8owh7y-ELYGwN2uwvx7_7Jw6odyMJ9s2SfgPItpST3Pa7EAvQsjqc8GNGBiyMtVh71ChZbIEmY8RCw4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیریت هوشمند پرسنل با راهکارهای جامع  کسرا
شرکت دانش‌بنیان کسرا با بیش از 26 سال سابقه درخشان و بیش از ۳۰۰۰ مشتری، ارائه دهنده نرم‌افزارهای تخصصی مدیریت منابع انسانی:
🔹
حضور و غیاب:
قابلیت شیفت‌های پیچیده، قوانین اختصاصی، گزارش‌ساز ‌
🔹
تغذیه و رستوران:
رزرو و توزیع آفلاین و آنلاین غذا
🔹
حراست و انتظامات:
مدیریت ورود و خروج کالا، خودرو و مهمان
🔹
مدیریت پیام:
اطلاع رسانی سازمانی
🔹
ماموریت و مرخصی:
محاسبه هوشمند مأموریت و مرخصی
🔹
کارانه و پاداش:
مدیریت پاداش، کارانه و اضافه‌کاری تشویقی
🔹
ناوگان:
مدیریت سرویس‌های ایاب‌وذهاب و حمل‌ونقل سازمانی
مشاوره و دمو رایگان:
🌐
kasraco.net
☎️
021-41452000
#کسرا
#مدیریت_سازمانی
#مدیریت_هوشمند_پرسنل
#مدیریت_منابع_انسانی
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/451570" target="_blank">📅 10:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451569">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/451569" target="_blank">📅 10:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451568">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4KL87HJIw45_JLd_b9lmswwjH4jDXhRLlH09mnJgSu_hNInZu7QNSTc5JCiFQNe9N682uAynSVnfuhMc0aQt6TZMYprwlPvsjLSCARfuwBxsgLYM1U-6JiJCQBnobdLmy8Ck49ziMYpU3thsgVcKGk7nr_pyHck_7UGHC1lhV2k1atsWCrhmlTRWiQC4dCbzt3S3sEnemCA94DRatqQ0DpDk3a2ZhUBot7D-TdEgG5bpXLBBIDEGRIkS0SZ1HQpYNO5MtL33FMbApY4xCYyZeiku5hUnO1cwDFg4XRA4OdfS_J3qTLAfel59IHtUblK8cRmBui1mOnT1gaRObj-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای اسرائیل درباره انتقال هزاران سانتریفیوژ ایران به اعماق کوه کلنگ
🔹
روزنامه وال‌استریت ژورنال گزارش داد که دستگاه اطلاعاتی اسرائیل ارزیابی کرده که ایران هزاران سانتریفیوژ غنی‌سازی اورانیوم را به کوه کلنگ منتقل کرده که هدف قرار دادن این تجهیزات در حملات هوایی را دشوارتر می‌کند.
🔹
به تحلیل این رسانه آمریکایی، رسیدن به چنین عمقی، حتی برای پیشرفته‌ترین بمب‌های سنگرشکن موجود در زرادخانه آمریکا هم مأموریتی بسیار دشوار محسوب می‌شود. با این حال، همین مصونیت، آن را به یکی از اهداف اصلی آمریکا تبدیل کرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/451568" target="_blank">📅 10:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451567">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWbp3NCe3eWK33zyptYT8ulJXgEXOXrphAOliP7cKVNnxeFzwo3f_ZiC0VMoFjZn81iEucjR2J2KOJqKefRDeMCHceN0ZPvKt82DAYcIYJsw1XLxKQ868H80SvWiqdWAkolSTMb-XYzfBVQZYyi342ZTfsDmMFKCkbJs5QdpHa_8jcEon4fgSr4oEP_ATNohqXHb7HSDduOI0qFodjv1voNH2NpKzk9xO4k3MYfFQIfDQS27Ql9SrpDuODsWwzPLpeXd_gjgHs-2zwfTg9b3OWL9Uia8YqUR5sZhIrNYA7Z9qCF7KwKRWLEirKs4eNNkhz5FoIioQ-WeA2TEWirDJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعزام ۵۰۰ تیم درمانی سیار در مسیر پیاده روی اربعین
🔹
رئیس سازمان بسیج جامعۀ پزشکی: ۵۰۰ نفر در قالب تیم‌های دو نفره با تجهیزات کامل و به صورت پیاده در مسیر راهپیمایی اربعین حضور دارند تا در صورت بروز هرگونه نیاز درمانی، اقدامات لازم را برای زائران انجام دهند.…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/451567" target="_blank">📅 09:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451565">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c74b25a7be.mp4?token=SxV2gMk-n5d2NwTe3p8ZeFHGRcbjHLuWwJ0bCOaDPXYvemuXK5yjIEBcO2ubcyHLWRhVeyONTNrj-d8DTKg4fyQysHPzdL8oEsTpfj1A61XQVWqs3kWH6doPw4KUcMTGnyC4IhoQexmD8Biz-8-2t5bmprIHkRXTvh1UwB7U4fzvsGdhzNEbwQ_-E9kYn69nDZsLo0iAt8OXZwOsFoZ_RZyyRl9fxkJUocpC3jaQst7sFSQpdhsaJ-q2J3JgP0EctUJ6P8dnYS-Z35p648B8Zb8bgPxfoA8xP-d7URb4HIuvw_zD47xZToGj16va-YIxxHq5jGnAD1oj81fFkECTMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c74b25a7be.mp4?token=SxV2gMk-n5d2NwTe3p8ZeFHGRcbjHLuWwJ0bCOaDPXYvemuXK5yjIEBcO2ubcyHLWRhVeyONTNrj-d8DTKg4fyQysHPzdL8oEsTpfj1A61XQVWqs3kWH6doPw4KUcMTGnyC4IhoQexmD8Biz-8-2t5bmprIHkRXTvh1UwB7U4fzvsGdhzNEbwQ_-E9kYn69nDZsLo0iAt8OXZwOsFoZ_RZyyRl9fxkJUocpC3jaQst7sFSQpdhsaJ-q2J3JgP0EctUJ6P8dnYS-Z35p648B8Zb8bgPxfoA8xP-d7URb4HIuvw_zD47xZToGj16va-YIxxHq5jGnAD1oj81fFkECTMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اسپانیایی‌ها از خجالت پرچم رژیم صهیونیستی درآمدند
🔹
مردم اسپانیا در جشن شادی به‌خاطر فتح جام جهانی، پرچم رژیم صهیونیستی را زیرپا گذاشتند تا بار دیگر نفرت خود را از نسل‌کشی رژیم اشغالگر در غزه به دنیا نشان دهند.
🔹
هواداران اسپانیا همچنین با برافراشتن پرچم فلسطین به دنیا نشان دادند که در کنار انسانیت ایستاده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451565" target="_blank">📅 09:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451564">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShyEni06X_rwGOnJ3UlaVdi3nR03J1tBCTAf0JBVcS2q9NhIxn1onytSbffF6_Ikl3RYnJ2RnI_Re7TG7LL9T0Z5eWN5MYtf_CZPK2f8Sk5jGGd_XRAXSdFsi1wUTzbwLg5myPvaIXoXv92OO7uTO1GM-jAewgYdau8oVFo9RuXirAE4Sm9gg9JF1jAFW7VubTD3LKFx5OKYodC1Zl1I7rGzXJ1Du15UBf625BdWwMU3uirfjlkIYQNOzZeUa7rteabCZjCe6MTJo-N8JMMLCc2xXgeK8f9-oFAGCfEVczwTzTCxi21EJUsx4qEF-7mw0OgdRfU5OYOn7DBhke-22Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منبع نظامی: تنگهٔ هرمز همچنان مسدود است
🔹
یک منبع نظامی در گفت‌وگو با فارس: تا زمانی که اقدامات خصمانهٔ آمریکا ادامه دارد، وضعیت تنگهٔ هرمز تغییری نخواهد کرد و هیچ مجوزی برای عبور شناورها از این گذرگاه راهبردی صادر نمی‌شود.
🔹
کنترل کامل تنگهٔ هرمز در اختیار نیروهای مسلح ایران قرار دارد؛ هرگونه تصمیم دربارهٔ بازگشایی یا تداوم محدودیت‌های این گذرگاه، صرفاً براساس ملاحظات امنیتی و منافع ملی اتخاذ می‌شود و تا زمانی که تهدیدات و اقدامات خصمانه آمریکا ادامه داشته باشد، تغییری در این وضعیت ایجاد نخواهد شد.
🔹
مسئولیت هرگونه اختلال در امنیت کشتیرانی و تبعات ناشی از آن، متوجه طرف‌هایی است که با اقدامات نظامی و سیاست‌های تنش‌زا، امنیت منطقه را به مخاطره انداخته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451564" target="_blank">📅 09:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451563">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">امام‌جمعهٔ اهل‌سنت میرجاوهٔ سیستان‌وبلوچستان به شهادت رسید
🔹
سحرگاه امروز «محمد انور ریگی» امام‌جمعهٔ مسجد علی‌بن ابی‌طالب(ع) شهر میرجاوه در استان سیستان‌وبلوچستان توسط افراد ناشناس هدف سوءقصد قرار گرفت و به شهادت رسید. @Farsna - Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451563" target="_blank">📅 09:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451561">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده در اصفهان
🔹
استانداری اصفهان: احتمال شنیدن صدای انفجار کنترل‌شدهٔ ناشی از انهدام مهمات عمل‌نکرده در جنوب و غرب اصفهان، بهارستان و صفه و ابریشم تا بعدازظهر امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/451561" target="_blank">📅 09:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451560">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
سپاه: تعدادی سرباز آمریکایی در منطقه‌ الرُکبان اردن به‌هلاکت رسیدند
🔹
روابط عمومی سپاه: ملت بصیر و همیشه در صحنه ایران اسلامی، با دعای خیر شما عملیات تنبیهی رزمندگان اسلام علیه دشمن آمریکایی با موفقیت ادامه دارد و در ادامه موج ۲۴ عملیات نصر۲ رزمندگان هوافضای سپاه با حمله به یک مجتمع محل استقرار نیروهای ارتش تروریست و کودک‌کش آمریکا در منطقه‌ الرُکبان اردن تعدادی از آنان را به هلاکت رساندند.
🔹
وزیر جنگ آمریکا که خود یک جنایتگر جنگی است، این کشته‌ها را قهرمان و تعدادشان را بسیار کمتر از تعداد واقعی معرفی کرده است.
🔹
بدانند در قاموس هیچ ملتی نظامیان بزدلی را که سلاح‌های پیشرفته را برای کشتن کودکان معصوم استفاده می‌کنند قهرمان نمی‌خوانند.
🔹
آزادی‌خواهان جهان به‌زودی این جنایتکاران جنگی را به سزای عملشان خواهند رساند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451560" target="_blank">📅 09:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451559">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بازداشت ۳ نفر در شهرداری بابلسر به اتهام فساد مالی
🔹
رئیس دادگستری مازندران: در پی دریافت گزارش‌هایی مشخص شد تعدادی از کارکنان سازمان مدیریت حمل‌ونقل شهری شهرداری بابلسر در جرائمی نظیر اختلاس، ارتشا، جعل مهر و فاکتورسازی نقش داشته‌اند.
🔹
پس از تکمیل تحقیقات و جمع‌آوری مستندات، دستور بازداشت ۳ نفر از کارکنان شامل رؤسای سابق و فعلی و همچنین مسئول کارپردازی اجرا شد.
🔹
متهمان با اتهاماتی از جمله اختلاس و ارتشا در بازداشت به‌سر می‌برند. تحقیقات برای شناسایی سایر افراد مرتبط ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/451559" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451558">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون در بحرین ویران
شد
🔹
روابط عمومی سپاه: با توکل به خدای قادر متعال و در هم کوبنده ستمگران، رزمندگان هوافضای سپاه در ادامه موج ۲۴ عملیات نصر ۲ در پاسخ به تجاوز و تعرض روز گذشته ارتش کودک‌کش آمریکا به تاسیسات در دست احداث و غیرنظامی دارخوئین، زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون را در بحرین با چند فروند موشک کروز مورد هجوم قرار دادند و آن را ویران نمودند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/451558" target="_blank">📅 09:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451557">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
سپاه: سامانهٔ راداری دفاع موشکی و یک هواپیمای اف ۱۵ در آشیانه دشمن در اردن منهدم شد
🔹
روابط‌عمومی سپاه: ملت عظیم الشأن ایران اسلامی! با استعانت از خدای متعال، در ادامهٔ عملیات پاکسازی منطقه از رادارها و سامانه‌های پدافندی و هموارکردن مسیر حملات موشکی و پهپادی گسترده‌تر و تکمیل شب سیاه راداری دشمن آمریکایی، رزمندگان غیرتمند نیروی هوافضای سپاه در ادامهٔ موج ۲۴ عملیات نصر ۲ در حملهٔ موشکی به پایگاه آمریکایی در اردن یک سامانهٔ راداری دفاع موشکی را تخریب و یک فروند هواپیمای اف ۱۵ را در داخل آشیانه منهدم کردند.
🔹
این منطقه جای متجاوزان آمریکایی نیست، ارتش کودک کش آمریکا برای پیشگیری از تلفات بیشتر باید منطقه ما را ترک کنند.
📝
گزارش تکمیلی این عملیات تنبیهی به استحضار ملت شریف ایران خواهد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/451557" target="_blank">📅 09:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451556">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32edfad20.mp4?token=uM0HY-cjvIi1uwAIT-eQwpq617yjKh63czSJHr8HGVQXGxLreXflyLfavK0zyNMVLFAGbddOf8yAx-jY6zZaV4ah4-rPfJP_7fjPYmayEHm9gFqBRYrJXdBqo2AyhlvldYhhic1PXGlX1MpSg3m8eHXk81llrPEc3qbL-7FX_zUyjUT-D2D-as_UBNUD_l5vGPG81R4oyJ_fA57NIsQosBELTgwLy0WuTZ1RsH487z6aqosxxfD2WcUi568CsBGQGiR2Q_bAdxVKDKJpI9bk_98CENIkxJc0pqORVTyuCg8ia9aAUwbJ8PWz_i7_lC-ZYa9e45s8lcbsq3hyBN1mDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32edfad20.mp4?token=uM0HY-cjvIi1uwAIT-eQwpq617yjKh63czSJHr8HGVQXGxLreXflyLfavK0zyNMVLFAGbddOf8yAx-jY6zZaV4ah4-rPfJP_7fjPYmayEHm9gFqBRYrJXdBqo2AyhlvldYhhic1PXGlX1MpSg3m8eHXk81llrPEc3qbL-7FX_zUyjUT-D2D-as_UBNUD_l5vGPG81R4oyJ_fA57NIsQosBELTgwLy0WuTZ1RsH487z6aqosxxfD2WcUi568CsBGQGiR2Q_bAdxVKDKJpI9bk_98CENIkxJc0pqORVTyuCg8ia9aAUwbJ8PWz_i7_lC-ZYa9e45s8lcbsq3hyBN1mDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا امسال گرما را بیشتر احساس می‌کنیم؟
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451556" target="_blank">📅 08:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451555">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb851bd1b.mp4?token=JBVug50hTCUD8IMW9WaUVmlIOkBK4eAU1MQNnmY3CqzOI_RNzgu1KjBY7GkoF5Hz4NVKY3o8nXjgyucEIzJM2wVYmkh1otSBHWqOhUSMeumm8Qy-irzCYhBjizHNeCW9yAI6abn9P8xH3zeWGw_miEb-nc5IEo9LEztVDbkfMVjYuyZBHVgVXgdNojVzxGHqyl1434WksBhnRUlgZsKkIj1dbuoUtBWwNEEkpiojSP3tMGt1WsBlNr_9hOmcyHcJemop9Mp-yvVDgbBYJ4xaaj6VO559v3yeDMHLsufNm6ynOGq1y2cNGyU5StwzqW7xB2MFd1uwMPlDvQXOl_j3gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb851bd1b.mp4?token=JBVug50hTCUD8IMW9WaUVmlIOkBK4eAU1MQNnmY3CqzOI_RNzgu1KjBY7GkoF5Hz4NVKY3o8nXjgyucEIzJM2wVYmkh1otSBHWqOhUSMeumm8Qy-irzCYhBjizHNeCW9yAI6abn9P8xH3zeWGw_miEb-nc5IEo9LEztVDbkfMVjYuyZBHVgVXgdNojVzxGHqyl1434WksBhnRUlgZsKkIj1dbuoUtBWwNEEkpiojSP3tMGt1WsBlNr_9hOmcyHcJemop9Mp-yvVDgbBYJ4xaaj6VO559v3yeDMHLsufNm6ynOGq1y2cNGyU5StwzqW7xB2MFd1uwMPlDvQXOl_j3gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آغاز به‌کار چهارمین نخست‌وزیر چهار سال اخیر انگلیس
🔹
برنهام پس از ملاقات با شاه این کشور رسماً نخست‌وزیر انگلیس شد.
🔹
استارمر، اول تیر ماه پس از ماه‌های فشار شدید هم حزبی‌های کارگر خود، رسما از رهبری حزب حاکم و نخست‌وزیر استعفا داد و حالا برنهام چهارمین نفری…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/451555" target="_blank">📅 08:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451554">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ادارات موظف شدند کار مردم را سریعتر انجام دهند
🔹
با ابلاغ بخشنامۀ جدید سازمان اداری و استخدامی کشور، دستگاه‌های اجرایی موظف شدند با بازنگری در شیوۀ ارائه خدمات، زمینۀ ارائه خدمت در نزدیک‌ترین و پایین‌ترین سطح سازمانی ممکن را فراهم کنند.
⤴️
مهم‌ترین محورهای این بخشنامه چیست؟
🔸
ممنوعیت ارجاع غیرضروری مردم به ستاد مرکزی ادارات و سازمان‌ها، مگر در مواردی که قانون صراحتاً چنین الزامی را تعیین کرده باشد.
🔸
ارائه خدمات در پایین‌ترین سطح اداری و نزدیک‌ترین واحد سازمانی به مردم
🔸
واگذاری اختیارات به سطوح استانی، شهرستانی و بخشی
🔗
جزئیات بیشتر این بخشنامه را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/451554" target="_blank">📅 07:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451553">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QV6LhwIgyPO0_uVZ_Uc4uixi6V6-Pg2Smr4965KKlF7V3SPPZRAylWJYl-mae1b1STdii5Z99PhYCq1D5SktFCzADcuQfcQXD6DizuNkiByqSbp4P--Q64vSPG_P8W8LyeCBmGOFk_sV6WdYTMNiYOHz3O096dW1PPPMx_BGe9sOZiUpfg1QEhP7BLp0jj7C3-QefbMfxf90WM7k3qypPo_6huc3471f_vyh694n7hZSaLcRrA9Hj5g5sjYboW68bkPwUL2iiJqAebHfy5MMo7RvcUprhDZd9bv9OaIGEYVDUs3jFlmPoGDvVerHlEi-_oQ85rf5VtvI6T3KIyb0dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژاپن حامی تازه تالاب گاوخونی شد
🔹
معاون سازمان حفاظت محیط زیست اعلام کرد که برنامه احیای تالاب گاوخونی در اولویت طرح‌های بین‌المللی این سازمان قرار گرفته که بخشی از اقدامات اجرایی این برنامه نیز با اعتبارات دولت ژاپن انجام خواهد شد.
🔹
این نخستین‌بار نیست که ژاپن به کمک تالاب‌های ایران می‌آید. دولت ژاپن در ۱۲ سال گذشته با اختصاص ۱۳.۳ میلیون دلار، به یکی از مهم‌ترین شرکای ایران در حوزۀ حفاظت از تالاب‌ها تبدیل شده است.
🔹
پیش از این، تالاب شادگان و دریاچۀ ارومیه از این کمک‌ها بهره‌مند شده بودند.
🔹
اکنون نوبت به تالابی رسیده که از سال ۱۴۰۱ به تدریج آب خود را از دست داد و سال گذشته، خشک شدن ۱۰۰ درصدی آن رسماً اعلام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/451553" target="_blank">📅 06:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451552">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
سامانه‌های موشکی هیمارس در کویت هدف موشک‌های زمین‌به‌زمین ارتش قرار گرفت
🔹
ارتش: در پاسخ به حملات موشکی شیطان بزرگ به مناطقی از کشورمان، ساعتی قبل و در مرحلۀ هجدهم عملیات صاعقه، نیروی زمینی ارتش با موشک‌های زمین‌به‌زمین، سامانه‌های موشکی هیمارس ارتش تروریستی…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/451552" target="_blank">📅 06:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451551">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42c0f762d8.mp4?token=Fo3EsDPEgnXC-rYjqArSsEsAAAvsFxKjxOIUrBvhqPBzXdBb5c-pVdjT_c4pdxEfJ8hfrbp0eOT1y_aT_sOTBdcDzwHP2wyY2U1QGWWQu0IafhBXu-dkPuaUS-mn1Vjuv_kK3tf0kwXBjTNKmduSqvi8Ju--pGh4eqcdnEA5cFbMa-6trEaDI4XgNmiqyg1MdPsA19P5XL4LMUyFuf9Wtiom3098emKewoaRfYM9dUMR-VYptmbNAtF79L1d84V9pm1bAEenfX7x0MBu4Nq8pMotIavs9JZdlP06s-yb_jQ7cxPQj4b_8yBr9ZXl20c8jyglfTle45iYLDHJWFU0iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42c0f762d8.mp4?token=Fo3EsDPEgnXC-rYjqArSsEsAAAvsFxKjxOIUrBvhqPBzXdBb5c-pVdjT_c4pdxEfJ8hfrbp0eOT1y_aT_sOTBdcDzwHP2wyY2U1QGWWQu0IafhBXu-dkPuaUS-mn1Vjuv_kK3tf0kwXBjTNKmduSqvi8Ju--pGh4eqcdnEA5cFbMa-6trEaDI4XgNmiqyg1MdPsA19P5XL4LMUyFuf9Wtiom3098emKewoaRfYM9dUMR-VYptmbNAtF79L1d84V9pm1bAEenfX7x0MBu4Nq8pMotIavs9JZdlP06s-yb_jQ7cxPQj4b_8yBr9ZXl20c8jyglfTle45iYLDHJWFU0iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حماس: ضامنین آتش‌بس، حملات اسرائیل را متوقف کنند
🔹
مقاومت اسلامی فلسطین: حملات وحشیانه‌ای که چادرهای آوارگان و خانه‌های غیرنظامیان بی‌گناه را هدف قرار می‌دهد، تجاوزی سیستماتیک در چارچوب جنگ ویرانگر نتانیاهو است.
🔹
ما از میانجی‌گران و کشورهای ضامن توافق آتش‌بس می‌خواهیم که فوراً برای توقف تجاوزات اشغالگران اقدام کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/451551" target="_blank">📅 05:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451550">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBuRx29Kfy5Fg68obP1xToO7es3KLUct1JSPDfKZLxlTW_EyUXVntXIm2WA7qZFoo8Qm7DXAMByYqvcN8ggl3FL1fhEkDh2BVDwJfiC6cUrhss1YMLF769UAtjp6H5JbnLd7PRSj_kLegp3GnBBx3IGdqP_EytTG5eK2Cz52L92EOC1_YQEzgTTR9wjfzNq5reYZBuK4V6WzgiyISm8Ell2VUSPV7nIUhCHny7rD_L1h-AMG8R-sYm1D3bCPdp_PyrmdvQM482rTrHCuqyjC-R45FuJKTA5LJ7BRWMo2UhfmC7xBA7Y7NdK4sqbnHNmK3CLgk_iunHa487C3ow1vQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دود آخر کارخانۀ قدیمی تهران خوابید؟
🔹
کارخانۀ سیمان ری که سال گذشته برخی از خطوط تولید آن به‌دلیل آلایندگی در فهرست صنایع آلاینده قرار گرفته بود، هنوز نتوانسته مشکل آلایندگی کورۀ شماره ۴ را به‌طور کامل برطرف کند.
🔹
سرپرست ادارۀ حفاظت محیط زیست شهرستان ری به فارس گفت: مطابق مادۀ ۲۷ قانون مالیات بر ارزش افزوده، واحدهای صنعتی که پس از دریافت اخطارهای سازمان حفاظت محیط‌زیست در مهلت مقرر نسبت به رفع آلایندگی اقدام نکنند، مشمول پرداخت عوارض آلایندگی معادل نیم تا دو درصد خواهند شد.
🔹
این مبالغ توسط سازمان امور مالیاتی وصول و به حساب شهرداری‌ها واریز می‌شود تا ۵۰ درصد آن صرف اجرای طرح‌های زیست‌محیطی شهرستان، از جمله توسعۀ حمل‌ونقل عمومی و فضای سبز شود.
🔹
هزینۀ نصب و ارتقای تجهیزات کنترل آلودگی به مراتب کمتر از پرداخت جرایم و عوارض آلایندگی است و کوره‌های فعال کارخانه در حال بهره‌برداری هستند و واحد صنعتی نیز از ضرورت رفع آلایندگی کورۀ شماره ۴ آگاه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/451550" target="_blank">📅 05:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451549">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شب سیاه رادارها و سامانه‌های پدافند هوایی آمریکا در منطقه
🔹
سپاه: فرزندان شما در نیروی هوافضای سپاه شب سیاهی برای رادارها و سامانه‌های پدافند هوایی آمریکا در منطقه رقم زدند، و در موج ۲۴ عملیات نصر۲ به‌منظور هموار کردن راه عملیات گستردۀ آینده و از میان برداشتن…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/451549" target="_blank">📅 05:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451548">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf767c5293.mp4?token=W73Q1fqdHCAVRFZSQ0K8mm7p492uhkjCogEesilItK7fmedWMCfP1qv801r0jYuXfrR_RvlFOFwD66pa22aGrSmoAuyNtF6ts5Dt1LbTwwFqL1rkGmG64bDrN9AB-VnwGa1Cj5tXsfjY0sBmmNI0yiAMHjUR-z-rNj-AIEQ7G0c_BTHjiNq6tgHLY-xg4Ty4xhgODJuvtZZ6zKBU8fNVi6k0YPF8mSOHyiQQVJsDl6y7MrCHDdDouRQrRK9pBUmHgSvGikhINsBFmsx5hn5h8lArGP3bMnOuRGCCDt7GqrGzfYf9fS1qjqKjfTE8OrNV8OStp6RZGsiof55GvlwEBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf767c5293.mp4?token=W73Q1fqdHCAVRFZSQ0K8mm7p492uhkjCogEesilItK7fmedWMCfP1qv801r0jYuXfrR_RvlFOFwD66pa22aGrSmoAuyNtF6ts5Dt1LbTwwFqL1rkGmG64bDrN9AB-VnwGa1Cj5tXsfjY0sBmmNI0yiAMHjUR-z-rNj-AIEQ7G0c_BTHjiNq6tgHLY-xg4Ty4xhgODJuvtZZ6zKBU8fNVi6k0YPF8mSOHyiQQVJsDl6y7MrCHDdDouRQrRK9pBUmHgSvGikhINsBFmsx5hn5h8lArGP3bMnOuRGCCDt7GqrGzfYf9fS1qjqKjfTE8OrNV8OStp6RZGsiof55GvlwEBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای سامرا، دوهفته مانده به اربعین حسینی
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/451548" target="_blank">📅 05:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451546">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شب سیاه رادارها و سامانه‌های پدافند هوایی آمریکا در منطقه
🔹
سپاه: فرزندان شما در نیروی هوافضای سپاه شب سیاهی برای رادارها و سامانه‌های پدافند هوایی آمریکا در منطقه رقم زدند، و در موج ۲۴ عملیات نصر۲ به‌منظور هموار کردن راه عملیات گستردۀ آینده و از میان برداشتن…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/451546" target="_blank">📅 04:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451545">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شب سیاه رادارها و سامانه‌های پدافند هوایی آمریکا در منطقه
🔹
سپاه: فرزندان شما در نیروی هوافضای سپاه شب سیاهی برای رادارها و سامانه‌های پدافند هوایی آمریکا در منطقه رقم زدند، و در موج ۲۴ عملیات نصر۲ به‌منظور هموار کردن راه عملیات گستردۀ آینده و از میان برداشتن موانع اصابت دقیق اهداف، یک سامانۀ پدافندی و یک رادار آمریکایی در المحرق بحرین به طور کامل تخریب شد و از مدار عملیاتی خارج گردید؛ و همچنین یک سامانۀ پدافند هوایی پاتریوت آمریکا در اَلرفاع بحرین هدف حملۀ همزمان موشکی و پهپادی قرار گرفت و نابود شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/451545" target="_blank">📅 04:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451544">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
سپاه: دو نفتکش متخلف با قصد عبور از مسیر ناایمن جنوب تنگۀ هرمز، بر اثر انفجار دچار حریق گسترده شده و متوقف شدند
🔹
ساعتی پیش دو نفتکش متخلف که با فریب ارتش کودک‌کش آمریکا قصد عبور از مسیر خطرناک جنوب تنگۀ هرمز را داشتند، بر اثر انفجار دچار حریق گسترده شده و متوقف شدند. واحدهای امداد و نجات در حال خارج کردن خدمۀ این شناورها از منطقه هستند.
🔹
نیروی دریایی سپاه بار دیگر به شرکت‌های کشتیرانی اخطار می‌کند، مراقب سلامت خدمه و شناورهای خود باشند و به اطلاعات غلط ارتش آمریکا اعتماد نکنند و از مسیرهای آلوده و خطرناک پرهیز کنند.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/451544" target="_blank">📅 04:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451543">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b4cffa3a.mp4?token=sqfktgQlQHl3wylG-BFQKa3YTvYFvGIrFDww7SiiNWJjB9xyZwmMHtc0hscgoUzwDxepxUn3VlMMYEfbd7l0LWnnxB66URaw_X77mwFbqhjmf5vg1kKGzRMn8tnG53TktyzXmT7eV-B2rUjLSFuaMqZ6TZ49ODQJXa1f-cbN6hg1UicM8BdN5fEcNqXwHUXcNREe2Tx8vxTk8rsASzLnV1PUI4I1PQhrsNTqMZcxFU0_Ck9aUhvoSJlSwbpsUzCA6s3nJK_gBf1Y0tr1jp0DIWd6buig9MRsMAhau49-8bGJ62iaY2ay0S8UOe28WVJ8x2HMZIgpw8iNrDaew_-BOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b4cffa3a.mp4?token=sqfktgQlQHl3wylG-BFQKa3YTvYFvGIrFDww7SiiNWJjB9xyZwmMHtc0hscgoUzwDxepxUn3VlMMYEfbd7l0LWnnxB66URaw_X77mwFbqhjmf5vg1kKGzRMn8tnG53TktyzXmT7eV-B2rUjLSFuaMqZ6TZ49ODQJXa1f-cbN6hg1UicM8BdN5fEcNqXwHUXcNREe2Tx8vxTk8rsASzLnV1PUI4I1PQhrsNTqMZcxFU0_Ck9aUhvoSJlSwbpsUzCA6s3nJK_gBf1Y0tr1jp0DIWd6buig9MRsMAhau49-8bGJ62iaY2ay0S8UOe28WVJ8x2HMZIgpw8iNrDaew_-BOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر انرژی آمریکا: به حملات علیه ایران ادامه می‌دهیم
🔹
کاری که ما اکنون انجام می‌دهیم، تضمین جریان نفت، گاز و سایر محصولات از طریق تنگۀ هرمز، با یا بدون همکاری ایران است.
🔹
ما همچنان به تضعیف قابلیت‌های نظامی تهاجمی ایران ادامه می‌دهیم. ترامپ می‌خواهد با یک توافق صلح‌آمیز به این درگیری پایان دهد، اما این امر مستلزم همکاری دو طرف است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/451543" target="_blank">📅 04:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451542">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گزارش‌ها از حادثۀ دریایی نزدیک عمان
🔹
منابع عربی از وقوع یک حادثۀ دریایی نزدیک سواحل عمان خبر دادند.
🔹
سازمان عملیات دریایی انگلیس تایید کرد که این نفتکش مورد اصابت یک پرتابۀ نامشخص قرار گرفته و دچار آتش‌سوزی شده است.  @Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/451542" target="_blank">📅 03:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451541">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOYatqRj1CHuko2XJDgFPfFNh_wPI8IPiRr4A-8lR_A7itAvIaj4ICqLJvWQCQJ1vD2szJ_l1LRq_0Y2AuTTCvcvNEeo6vhPdV1fMwBZGD5oqgOa5NWmgBmiy_lDrSEQuCbQTY_f2iSFbIdadm515YE25eseI8JKc1S9h5tBGwSqr7HFubHJndAKRZqbdtDCt1BemJW0z_jL7juPSIpFDU6mA3KMWQM-AMcNzg6cI8Rb06k7OpeG2ASHoh84UDZqpN5yd4AEgvN96V0LeCKbHNfd4yFo5gqInEnmPoWdnDT3g0YE9zaKnaWW71_FdiCUVAsq33AMMlQJBdKEhdtJ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظار پرسپولیسی‌ها برای معرفی دروازه‌بان جدید
اخباری باز به تارتار رسید
🗣
محمدرضا اخباری، دروازه‌بان پیشین تیم‌های سایپا، سپاهان، تراکتور و گل‌گهر در آستانه پیوستن به پرسپولیس قرار گرفته است.
🗣
پیگیری‌های خبرنگار فارس حاکی از آن است که مذاکرات میان مسئولان باشگاه پرسپولیس و اخباری طی روزهای اخیر با روندی مثبت دنبال شده و طرفین در کلیات به توافق رسیده‌اند. در حال حاضر مانع جدی بر سر راه نهایی‌شدن این انتقال وجود ندارد و اگر اتفاق خاصی رخ ندهد، این دروازه‌بان امروز به‌صورت رسمی به‌عنوان خرید جدید سرخ‌پوشان معرفی خواهد شد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/451541" target="_blank">📅 02:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451540">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">هشدار یمن به عربستان دربارۀ عواقب تداوم محاصره
🔹
وزارت امور خارجۀ یمن در واکنش به بیانیۀ رژیم سعودی، دربارۀ عواقب تداوم محاصرۀ این کشور به ریاض هشدار داد.
🔹
یمن در بیانیه‌ای گفت: رژیم جنایتکار سعودی با جمهوری یمن طوری رفتار می‌کند که گویی سرزمینی تحت کنترل آن است.
🔹
این رژیم جنایتکار باید دست خود را از کشور ما بردارد و به تجاوز و محاصرۀ خود پایان دهد، وگرنه باید منتظر اتفاقات آینده باشد.
🔗
متن کامل بیانیه را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/451540" target="_blank">📅 02:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451539">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44bb724c93.mp4?token=JRhbMeo79wHe1m4BZCCdC-zcIQVZqkeeOTSPqdBW9kdPx6-W7sNDwNXb42Nyc8fV8QbInf8NZrldoo4A7gAHk5BiCBB0AU_EB7UCz3ZzbiJJuoOYjVs1XguJHwDBSCGlti6IUrkWCGw8kllF4oLAIEn5ppXU_HElqxggazkLq8dmemTa4Cctovv1hbBxzBKsN1jsR4rnBP_KvA-3lInSLU-g7Ml5m7hht8sfSe6F8CxmRfZ2kQvrl07kntZ4hWO8R_Fi9HVXOZwsUz5Ttw5hdBaLlwUfKSN5aZ1hrT7dXmxMFZn5LEwNzk4_sD0NpU1jI2VaA9c6VF4GWqQPDNl1SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44bb724c93.mp4?token=JRhbMeo79wHe1m4BZCCdC-zcIQVZqkeeOTSPqdBW9kdPx6-W7sNDwNXb42Nyc8fV8QbInf8NZrldoo4A7gAHk5BiCBB0AU_EB7UCz3ZzbiJJuoOYjVs1XguJHwDBSCGlti6IUrkWCGw8kllF4oLAIEn5ppXU_HElqxggazkLq8dmemTa4Cctovv1hbBxzBKsN1jsR4rnBP_KvA-3lInSLU-g7Ml5m7hht8sfSe6F8CxmRfZ2kQvrl07kntZ4hWO8R_Fi9HVXOZwsUz5Ttw5hdBaLlwUfKSN5aZ1hrT7dXmxMFZn5LEwNzk4_sD0NpU1jI2VaA9c6VF4GWqQPDNl1SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور خانوادۀ شهید جاویدالاثر ماکان نصیری از شهدای دانش‌آموز میناب، در جوار مزار رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/451539" target="_blank">📅 02:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451538">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75bdda04f4.mp4?token=BFHg6sakbr5xyd73FnPU-rnrMDcO2hQTswKm8r62xQUTQfEaVp0PZt15lw3cgKDN06HzejxneQr_IQbQIbSr3c5LxvGMM1KPyxViKD-SN9QCCr-YLGegybJ8dijcNgoNrsBa6QDr8flwmr6QfJlPgIiQL96svllegvFPdQyiMDfSs516gPdZH1TDS9N4C7NRc027p2jS2WmUEcJMeR_wV7_KWvBckEPvP6rbTOXH045M4380qZ-ARyRwW2mfeVemj2B88Hl2_iEOzA2ByIrObnkTA5qXJlAOLmDrrDYJW77tUtVkSIRA5P2htl28GhscsR5GOM6cFbKAZewVus7QaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75bdda04f4.mp4?token=BFHg6sakbr5xyd73FnPU-rnrMDcO2hQTswKm8r62xQUTQfEaVp0PZt15lw3cgKDN06HzejxneQr_IQbQIbSr3c5LxvGMM1KPyxViKD-SN9QCCr-YLGegybJ8dijcNgoNrsBa6QDr8flwmr6QfJlPgIiQL96svllegvFPdQyiMDfSs516gPdZH1TDS9N4C7NRc027p2jS2WmUEcJMeR_wV7_KWvBckEPvP6rbTOXH045M4380qZ-ARyRwW2mfeVemj2B88Hl2_iEOzA2ByIrObnkTA5qXJlAOLmDrrDYJW77tUtVkSIRA5P2htl28GhscsR5GOM6cFbKAZewVus7QaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سامانه‌های موشکی هیمارس در کویت هدف موشک‌های زمین‌به‌زمین ارتش قرار گرفت
🔹
ارتش: در پاسخ به حملات موشکی شیطان بزرگ به مناطقی از کشورمان، ساعتی قبل و در مرحلۀ هجدهم عملیات صاعقه، نیروی زمینی ارتش با موشک‌های زمین‌به‌زمین، سامانه‌های موشکی هیمارس ارتش تروریستی آمریکا مستقر در پایگاه عریفجان کویت را هدف قرار داد.
🔸
هیمارس یک سامانۀ موشکی متحرک با امکان جابه‌جایی سریع علیه اهداف زمینی است که هدف قرار گرفتن آن‌ها، موجب آسیب به لایه‌های آفندی و پدافندی و کاهش قدرت موشکی دشمن در جنایت‌های تجاوزکارانه می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/451538" target="_blank">📅 01:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451537">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
دقایقی پیش صدای چند انفجار در بندرعباس و قشم به‌گوش رسید.
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/451537" target="_blank">📅 01:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451536">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkOntiD47RwnBfIZaNfewfTShx7x9wWFSILv9tvewJIkSd2Agm4FjqVnwRADHPe7fAHM22YMGlGkXg1i0LSvhNVzhXh3CXvPMe9CfOl4LsGDfah_K1Wr9hbStl595GAVBYvUqqPnNYLvdf8j917KsIhGBJ7CKLPCcIF-8fCfOrMtabTZufC2m-4zRvuX-okzGg1smidvL_5uLb761htoIrlP-xP2P_VeqLxx8c2Q1-hBNcmqJBDv7aVjN0RONu_WKoQZcFkjf3ifS3F8H0uiIhIWVgsVNPvPEF7CTaDgOsrps6YF49xwDCc7KN7_3goJ0eJRHxypdt1r4CxLYofi8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها از حادثۀ دریایی نزدیک عمان
🔹
منابع عربی از وقوع یک حادثۀ دریایی نزدیک سواحل عمان خبر دادند.
🔹
سازمان عملیات دریایی انگلیس تایید کرد که این نفتکش مورد اصابت یک پرتابۀ نامشخص قرار گرفته و دچار آتش‌سوزی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/451536" target="_blank">📅 01:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451535">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f38a10e82.mp4?token=EBVnFSjwcC3P7TBaeUUCLpVCVkWQnFZDOBEdjJQFyJzRKP5DS-qW-PHEfNWpmFZtNZukS6lOVX50mOu7-iO9t7PauGGRaDHRRuh9sBKkPEpTSMD9mIA_i0QmqsxJUaNMrdov2pLlfS2xHeGL6t9aGl8XuiXLq1cb4hOF7keGWnR4r37thWvQsJKcooj0Z7tCkMGDX4GYyyKc0ldwOUmutv5S0wDT_c0zMLEbLNNgFShuaB_et387sAll-RZQt5AGNJOzSpBXX7sDwzAkk7K0BwFqeLV3vV2xZErUQmqOkGiZzsI8lg9rQgbrRXf6-WuPsc3o_AdJVSEMscpgJcvmug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f38a10e82.mp4?token=EBVnFSjwcC3P7TBaeUUCLpVCVkWQnFZDOBEdjJQFyJzRKP5DS-qW-PHEfNWpmFZtNZukS6lOVX50mOu7-iO9t7PauGGRaDHRRuh9sBKkPEpTSMD9mIA_i0QmqsxJUaNMrdov2pLlfS2xHeGL6t9aGl8XuiXLq1cb4hOF7keGWnR4r37thWvQsJKcooj0Z7tCkMGDX4GYyyKc0ldwOUmutv5S0wDT_c0zMLEbLNNgFShuaB_et387sAll-RZQt5AGNJOzSpBXX7sDwzAkk7K0BwFqeLV3vV2xZErUQmqOkGiZzsI8lg9rQgbrRXf6-WuPsc3o_AdJVSEMscpgJcvmug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوش‌چشم، ‌تحلیلگر مسائل استراتژیک: هربار که دست ما برتر می‌شود، آمریکا به‌دنبال مذاکره می‌افتد.
🔹
این‌بار دشمن وقیحانه به‌دنبال مذاکره است؛ این‌طور احساس کرده هربار بگوید مذاکره، قبول می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/451535" target="_blank">📅 01:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451534">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31fe786137.mp4?token=XeySX-7bTlWLAJzI8d5ljtBMVGna2UimTIallBcMxApvmjJg5DADb5dq9mgD5y5FiOwStBVKd7VFOovP8vZeH98JadUNpnxWvgCTUw32pW-ly7WTLZviw_5IfTvSSlpEpvkKQ4EbLn2kK7nxe5Sm48BLcRTiu46NnO1Ww79QMNxdDHZXHq7Fef8URrI4zusnofi9_L-AlPFng6hpowXeoNZD7ER2YLDJFz3GV-zIcQhMMP8YOURAfx8YClVI1bXCiV-6IkXaajJQ723ZQqMBWas4BE5d_9Z--zOLJlxtAgu7r4zgROiC-Fk8e-DYzaCo1fRaNGp4Z_R1SWo11nAoiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31fe786137.mp4?token=XeySX-7bTlWLAJzI8d5ljtBMVGna2UimTIallBcMxApvmjJg5DADb5dq9mgD5y5FiOwStBVKd7VFOovP8vZeH98JadUNpnxWvgCTUw32pW-ly7WTLZviw_5IfTvSSlpEpvkKQ4EbLn2kK7nxe5Sm48BLcRTiu46NnO1Ww79QMNxdDHZXHq7Fef8URrI4zusnofi9_L-AlPFng6hpowXeoNZD7ER2YLDJFz3GV-zIcQhMMP8YOURAfx8YClVI1bXCiV-6IkXaajJQ723ZQqMBWas4BE5d_9Z--zOLJlxtAgu7r4zgROiC-Fk8e-DYzaCo1fRaNGp4Z_R1SWo11nAoiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
یمن محاصرۀ دریایی بر عربستان اعمال کرد
🔹
سخنگوی نیروهای مسلح یمن از ممنوعیت کشتی‌رانی و محاصره دریایی بر عربستان براساس معادلۀ محاصره در برابر محاصره خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/451534" target="_blank">📅 01:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451533">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎥
قلعه‌نویی: بی‌وطن‌های ایران‌فروش گفته‌اند که خوب شد تیم ملی صعود نکرد وگرنه ما بیچاره می‌شدیم.  @Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/451533" target="_blank">📅 01:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451532">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در شیراز
🔹
دقایقی پیش یک نقطه از ارتفاعات شهر شیراز هدف حمله دشمن آمریکایی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/451532" target="_blank">📅 01:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451527">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FmEm22ThC7oMHAhGTLbF94vrkTzOuREwdz7i79mdortn86xL3T5-3VQOIbu-iKhODfLewPs146fBhuE9IXmP-jiscj2fI75HBsxjeWkkhjrvW4y7Y1JiTWRERh0DIce8VFRKlUKvBjxucbRluOq5DRWBDaRDJP9VQoyJwRN_fzuH2yVfCQAZIUPD6cw7ziOANdNry5zcG364UfbzAjl1eXrx9W_-jZR6DVw8vXF200Z0vUZMTtVfSWMk1DPvGxpvPGAEhD-PUX13LOSWO3YsH8PUglUNGu35b0oTETrx9PTOB2ci9O4YSQQFH8NHLU-Ad232swRbLDr9P5lu8zUf4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/edO_Bz9hHs6wBXNCcmr3A90M4aK8x2mOFZiQkQREkqxY0ypT2jiI76uCLCzIebyAGRq-I9rbp_hwjPw3gpe43ww5E06OY5Kokxhy4RfGGSdnIIkcQveP4A1hbQmjmasRZZe2dHekCimfBackk0_g-j9pB2yUmWJtwyxKw6rcxL1HnabkPinKdkZDNIl7zC890kA-tZ3gLSg1jb-PzAaYzFqBl10A3ycuHCMEkFlscKBT8Zwcf5zPBPNY7pJjthFDQ7kihU6JYwnSFpG5QHrS67t9d-kBM_Qq1bkshaHbZ96jHtAEXOxsLbuakuEpJw1OqiNOAj9ueYjlDyG0mtOslA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRTitjbesHvvluAM3GrBNf387Gywk8QNDB1fdlhsO4Lr9MZGrbRqjskOgC8MGaMaIv0-rw3ag7z9Z28jHZ2RcvM-JEQ4BLW1rUH3vM_JnCilECj5UcIB_Erfi3XOq8BN19amM8N8E0b8bXDv59KYn7qYf7hFEx3KdG1sSv8KY7ome1YIQyd0DIYMlQQ0zBfptzSQx41K72JgZmv3_841n3E-2lEpbSDAC8LKlcnvUlnDkAhNEt9Y-Qp1kK5HtQFOqyw-2jMlnXvsv7oQ9yEZ-M9ad8RNSFXJ7ct7ivEjDyCq__JMH5Bp4RNhCNCFvuO_s2LL0RshOJhqsZg8DW7zMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mfHQ-gqRpHRqVYV4taOQnZjjahWV-eX-Bg8ewaxF-e2qb5f33FbueZkGdeciCPTC89CXpKecW3n6YE3mip6cG7G1eSMuq7gQozkHPhKU0OfN4Md1DTxPm6u7CoY-dxRVE5bLi3GqI1LjsWRPz98__2jhI7rYP1nRi5B-lUozXuuFpYzLSliF0-qpC6XsYCYwH2_BPjpmsiIXs9R-StqWV8y9cOiECgSBnESVO5w1PvnlBOx84v7tL8pkTEjkrnF3vcjSQXpnr1HiJnZGq4ZzITCAoo37Mwk_2PBvVAn62ksg0UG1lntMeAbu8Ci8Abm4bFzxzsUzZraJydcgyGKGfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VqVGL3GxdHHQP3dW1MowOi3TELIde3tQsBS1dylqpDcfroLbb9vyYY_znnmJNRz48eOSxy0tcuXnICDImvI81GP4RL7nV7nR9iL3m0Ph7iIsNNeDrgR2GxoqWpnLzGgG4zBc2e7qdrFi_tgMLGsProDpFJPJSM32OMhAg7n2O3DkGh3nZk7v_DLpU5bjmeKpzHIviCcnrCtURBSdmWsCNsoRUVpVT-EwqoRVb-kU0tsoP-5i3OeQeTz8L9fW-Riq8tpA8WbKKSTs3M7GKypobMjGfS1_cKPQ5HXa_BoqovYUl0gK2NhtmHCyc1Z0m4T8VUSgsu52di107itEf4CPGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۳۰ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/451527" target="_blank">📅 01:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451517">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAHPBvCD0VKIRkRRV4lh4S3TZBVD7qFQuGJN4-38MhHVr0Sc-aPuojKd8JqVRwWBSwz_IKOQ449p50UpCJ6MMUuSAT_nIQtaXF6DNETqjzpManYMAAPQjr7Ub0KXg74yVLbKiJZpI1D1oO1LuRHZSSZY2IZaFQwMBg2caZHWJfCE7KEvl80asb1qGk0dU4v9Vjlw79gq7q_Ztf2Rlo6jkbRGQyjz14ZDuSgWHmwoqJPPDgbpJpFFaPs8zbR9hRhQSalzBJRDOHXGkz3yTwYbZ_s6Za4rJ1dXEVQIMRQTu8D6GoMq-Edm4p7d4Q669Lowr1pg8rcKUi5aUdHsVLIGow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4klu8mjQbIPL-IVwsTQumfZi1jpIKY0yXQik1IG3k3Dahd3EG8w8kqFQr6iKUj34RmjdI_yFrAGfRCPTv8k3frevVG7otTjttMO7WsxzALSCjblszJdiXsbFahSYTlDmn57n4_W2iDwEd-DfjzfLGj0WcnAA6rJklLsUuIB6uTWlxwpf_uQ0vJW2SWrkfpj66XjvFPWi0WCwlhw1nEbWRgLR5j-qfv6WKok3iYLQaUD1mSaBqcE6OLbf6bvrOhrnNL-MIr3S8c8zpjgKlYNKX4vfi3zKHY1Vu510oF4iMzZpG9etWHRKF1iU1F9BXmCDiRWaZNRhi6o04G22uOpLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lD7QtJlaUaST6BufYKyFeQlXmHfcjUrI_LXo8-2A0Hel51Blz7FLN4TrO49ec1Uxql26CDNtDiIVQiZCfY8B9MnI__pOmaawSSv12HUERmmcr1pWUb8UDNNTAIe8jfA2tufne8kE8gjygRgcROfHfd4pLTSEP_p-u1KF0WKKOItfv5Lp8NhtbiDq3UqzVmEXkWA0c1S5QLwwTzwljtrUen9dKzC5TR0jeNRrlmMlALEsxlntLlOMm8-BGWGLzG_SJGohlSFWN0J740atEaY-o5tjp1Aaze3hyNUJLMM8JuJDKI1wWQj5JD75XT0ktINfEAKf5gZBrVxteDi84F2deQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQa_bkgnw3OEjOboKrsPNW4zalmvG1UK7UmISDfkHxO7eMyNcL-OnDS6eIJFDWqN3AUPVTF7fPHM1TPjJWxUdkbUsQRmF6Bf2t4TJQxIgfChoPRPwQQo5wa2qrTcs1NmW4VVin88zFvgm_hE_OB11KeSpNDrhHZMOjXrS4VzADd9JVmKYPmIQqiNDVffASjWhxILvXKolKbPmpCAijbDmGgl1w39kuy0-mgB3H72aApQJ2fdGSBRC9knJhMJn6ugBL0Wvt-zAudXil2AucxLSYNdmad68d1DpiA2XKawr-hb0_En4o9A3Y-YdtVPQZK2Rf6yn9SxewJYcOxBM09Y0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dzy2BClMEUWxV0NkuS7HMbZOxt3Ct1dBD9BAvUU18-aHG6ckdjq3gRfLjOil9V9MVQA5Uqhc0vCNPg6LoeUkS9dgILgRsBhPoxrURJZnNLiL2htyV4A9IaXTmLFIPR2qQein18JyJTOVZcQB9hZr7b-LWbcsfw4lnF194a6PeNq9R-k7QjjUFYNNqOK5tgkHciIAtolYG8yUNYf5HcBAeM9vr7noukwt5CJEuZopZacp1ZgEOtYh3M119uFagPhdqg0nR50iEkbNb92RA27j5q5_P4KmSV8K4YzE2h9-hciIvOmKOW8Z5L2wf4EGJan2XhzquNf1k1aIcKa7nFECAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9liGWnlbQQL8IS4N4OfC_FwS4cwnu_-A9i9X9UzsRsLRTpxOwMdJBbOuNtTGlQETCSn_Gnz1WEU-uJUvi1WfNrjYbZqdYW6zs8b_AOYacB8QcoRG4KoqBIj2q2n2d8kO33HR9z3ZMOCt_sjFYs5hINDQ0QbDyDaV3y4Om1r0ecrEznlK7GFt6mbJUzJZnfTPh1B_PuUvIZ8tW7o6mPaDwskA40hEUTB1WjAkYjnu6t8nuR0uzw8sjLCaX7jvCkkw-h2sLThIxjqdHVdpJ_zPUAhmrbgjC_cMnecdb95_U9R99hKOlTnR3Zx8Drb1C8xYCCPOVb4DL4vcM5N8oaY1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aMXDedMW2YOvySzD28OmqvfWxtRNshjsXEqxsiI-spIJQruymn8L_4Dt9eO5vSP171juQCBX-fAxeZN9zAq3YH3r5UFr0epComRQYYFL-eJOLbuJeF9jYQhHdcFc2RLeJz2OdBruQqYTFhX0ZEvYrZmjsyL_zANViXNFCTyvyHeDWx_L0o_9tP0usqcOOxT6z6ipvOATi1yTLpDImygZOpxC6GKfNzA1Q73WEu-wPWsDt0DLMqq58y16t-ul8KKMnZJLucISD0q2f1Tfe4jf6LIFjFU1Fy3nSuNecCkEFwBeMZ7SA6wgtH53zURDR9tbnWwrqMZ31vNMeeQave1GNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vXWxPFYdshXk6tJs5tlKOwVW7KbCjdvSDcloIM3pHZ-jHLKOFXGM4liT2bTpoXUh4hiK-RI_wsTUaLHohs2rwhkVQIQic_EZZNnrHBoTLxXTpYff6Jc9gHW6xwUv619B0kNMu4tvNSJ8zB43SA1MwtFJud-Dg-grmnm76cvRJJAde82jt2eHSBxnA3opOpr8pTp-16-2U2Qm1l2TmFyxWtdLmXiAaLuibaUPR8EwDT2UPxwbIHujeSsOTMJsTvSNOfSkRhqy6Qc3ZWUKgEfnfHTJbFeRGrd1m8gk9ndSq7YuC_Tky0zuo-6nyCpD9MlRqJzyeBu51Xjzdud_MP0mXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mC3pHiB-YTGy3x66dZCtC44_lDIdJMZvPTUcaKXPfC789sr5_RtI8HK028Xam0_q3-qqVlGfVq2tcbkrkZMQH9K2g-0sxTm-n2BlGcxrFW5nrR5xidmSbDnUE4_C8ScRN4NCI9WGgWja_UQN70FvgU0F1zVHjiKOGRMe137bVoqZVoWKbHKq9bQbU8Agz3A1mvaD3kE_pdrx7U0dNt6FpmJoRxa0xg2C0_Qy7bWQTokM-HevQUMGAYuW8svbTGiAPfg2ESXA-Ai_GjHLd-T-8jolCI5erIaXS9KJ4peDjP_R4Rm_01h_XzmgHIhERjzgyF2_uXnQzJBfyQ3ORfae0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/klInLFrTU0tfAS24AdhwUcbwEqXCuAfcfFeJ6Wtx2pQOxYpcPPGGpiKz5c5QdR656zZV_1VAJg2G-Lm2EbzTjbck8qw12l9Zz0uEuTQ5uOUShvdVGk5Azzj5oECfQfcanDTpfCwxNlnZSUpx2S3XqmkYkNHe9Y9L6l3rWXNTlu7cDC7V5vAX6gt9poDKFHHmT9HdgdWXpFoVr2qAeh8m6fwDNbC7L2P6W_5DWtjsbhrQ_bnmO1sQaRuAQMQOOqzEH3iWYLfvleOkb7-p3frWS5Rt3NDgVscdLvaR09pxbPSPFGfywonylCeJLc2B_jziN88bIe3Xn6LtzneE0dmgHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/451517" target="_blank">📅 01:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451516">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d630841d55.mp4?token=ko516qgZuRQQk9ceZL-ED82TYxMQvv0krDWpBYLmc3-da-edEq9rZ_I4xlaxRXBRqOg4pmjMHEYcAkKtcQVelLun1QSnVWWjBDknCjhsGcJ2GSsyCs8n9ceBNOc2s2nrO_5yZoWctL7BrZv3Muj7fBawrKmxBRApzRA2y8q1NyJ64DgjQv2NIo-HB6EulgpSDgZqA0TMwcIOARh9yg16tvwS95N7xlzH6YeOBgN57c--Zmc1IyIRv5_z_PzEDazHEMebv1PS-ctlEDAUcFlraA3fUN59hE2yP6J08bA4jRAQGXn3Z17L349xa93B-y4UWo-26N_-JfFywBCbBfPPxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d630841d55.mp4?token=ko516qgZuRQQk9ceZL-ED82TYxMQvv0krDWpBYLmc3-da-edEq9rZ_I4xlaxRXBRqOg4pmjMHEYcAkKtcQVelLun1QSnVWWjBDknCjhsGcJ2GSsyCs8n9ceBNOc2s2nrO_5yZoWctL7BrZv3Muj7fBawrKmxBRApzRA2y8q1NyJ64DgjQv2NIo-HB6EulgpSDgZqA0TMwcIOARh9yg16tvwS95N7xlzH6YeOBgN57c--Zmc1IyIRv5_z_PzEDazHEMebv1PS-ctlEDAUcFlraA3fUN59hE2yP6J08bA4jRAQGXn3Z17L349xa93B-y4UWo-26N_-JfFywBCbBfPPxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌نویی: چه اشکالی داشت که بی‌‌وطن‌های ایران‌فروش می‌گذاشتند جام‌جهانی تمام شود و بعد تیم ملی را نقد می‌کردند؟
🔹
قبل از بازی با بلژیک به سعید عزت‌اللهی گفتم چرا از نظر روحی به‌هم ریخته‌ای؟ او گفت که فضاسازی‌های بی‌وطن‌های ایران‌فروش روح و روانش را به‌هم…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/451516" target="_blank">📅 01:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451515">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
آژیر هشدار و انفجارهای متعدد در کویت
🔹
منابع محلی گزارش دادند که منافع و تأسیسات آمریکایی در کویت، هدف موج جدیدی از حملات موشکی و پهپادی ایران قرار گرفته است.  @Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/451515" target="_blank">📅 01:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451514">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34e0b7a02.mp4?token=stX6RsTBBU2IKzbwcpJ0H5snxecCNxSnzKij5zJfS24iQExkQCeZm7IX0BugKtFE34TlnqBRmvka_HKCFcLPhYeX90FjL1K9ercfeqrs__Ix4Udq2WCy5heBjHTxuBGUuiwdYu1krtMGNclKNYDRyDUwCAzUjzjr6a6LJfRQiNrBPRRmimsbgH1naUVWc-jsBhZlWefsTwS-GXDfvTel2fJOWnRWyppUU4xecjAdNmqpzv-v8S7gkvacMl2ja-WZXol-yl-fb5R5brviaMYAEY2QjunWLxPiUikem-lh6-kXPdK5gGHdXGshg_RJRcK2NVVNCaIBllvtZGgMOzSrGBRqNV6mleNV-gh5NRdG-U-v-fOblRLk-i-A4yjjF4MYb48HLASXLLH65PT7U5ET6fPWASPuAYk07iZRm2Convqr0BEO2C2tN0IClug3ZT91drGhBz5RCYjRqTrL_TILINR_61mkUSjBl16fntpuU_AV0AGrh1SBe3cGNMVIT4D2XoNmRQhzmTII6L3LOdKyN_TjJR-Y2MVrYJIXmzx0J7OleXHsBJkm-CsA5dbI3wiPOznLFwJx4aXs2n9-cIW1D4kVnsSxHzsH8ApLaULx5qTCB9TMzGlxOINLuszyjRollvUp-uPLSDRHTj6MBDjqHPblzkIVJX9pkodcptL2UCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34e0b7a02.mp4?token=stX6RsTBBU2IKzbwcpJ0H5snxecCNxSnzKij5zJfS24iQExkQCeZm7IX0BugKtFE34TlnqBRmvka_HKCFcLPhYeX90FjL1K9ercfeqrs__Ix4Udq2WCy5heBjHTxuBGUuiwdYu1krtMGNclKNYDRyDUwCAzUjzjr6a6LJfRQiNrBPRRmimsbgH1naUVWc-jsBhZlWefsTwS-GXDfvTel2fJOWnRWyppUU4xecjAdNmqpzv-v8S7gkvacMl2ja-WZXol-yl-fb5R5brviaMYAEY2QjunWLxPiUikem-lh6-kXPdK5gGHdXGshg_RJRcK2NVVNCaIBllvtZGgMOzSrGBRqNV6mleNV-gh5NRdG-U-v-fOblRLk-i-A4yjjF4MYb48HLASXLLH65PT7U5ET6fPWASPuAYk07iZRm2Convqr0BEO2C2tN0IClug3ZT91drGhBz5RCYjRqTrL_TILINR_61mkUSjBl16fntpuU_AV0AGrh1SBe3cGNMVIT4D2XoNmRQhzmTII6L3LOdKyN_TjJR-Y2MVrYJIXmzx0J7OleXHsBJkm-CsA5dbI3wiPOznLFwJx4aXs2n9-cIW1D4kVnsSxHzsH8ApLaULx5qTCB9TMzGlxOINLuszyjRollvUp-uPLSDRHTj6MBDjqHPblzkIVJX9pkodcptL2UCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌نویی: یک عکس از چمدان بازیکنان تیم ملی منتشر و بی‌معرفتی کردند اما این بازیکنان آن‌قدر محبت دارند که کار تیم پشتیبانی را انجام می‌دهند
🔹
با همین عکس تبلیغ کردند که ببینید این‌ها چقدر خرید کردند. اما واقعیت این است که در این مدتی که در اردو بودیم بازیکنان…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/451514" target="_blank">📅 01:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451513">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8ebr0xkt_cynyvq0ZADTpNXEdsVKQlOEfXbiSocMtzOhq9X5oRxhKcZROsHiTDRla7DFzWsJ0IcOJxjnCfKbueBbZrD_4tK1LtfyQwmeQ72D8xGgcQ_5jn2N21mZ8vg6Y_APfTOixs46DaqCpIsWOpxgmraGcyRl8QKVcOzYJxSgeSzvia9xxuMrL-XDl-mMz0tJ9ysjjrNbxacR5pIUXJHLX99EOVblraRi6sSeIUeo0n5cyJPp8Wp1hklfABZyKi3TUXAiMx8Iw5cZRqAUzcFXdCEYPsGYrh1o9LAdIJoakdt756Ii0blJKmauECsUGlNM9BQc0ivvmQ7XbI3Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزبانی فردوسی‌پور از کسی که آرزوی عصر حجر برای ایران دارد
🔹
«قرار ما با شما، نه دادگاه، نه بخشش، رقص و پایکوبی روی گور تک‌تک‌تان» این متنی است که علیرضا فغانی در دی‌ماه ۱۴۰۴ منتشر کرد؛ اما این تنها استوری‌ او در دی‌ماه و حوادث بعد آن نبود.
🔹
فغانی که پس از…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/451513" target="_blank">📅 01:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451512">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فرماندار بوشهر: صداهای شنیده‌شده در بوشهر مربوط به فعالیت سامانه‌های پدافندی است.
🔹
تاکنون اصابتی در بوشهر گزارش نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/451512" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451511">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
آژیر هشدار و انفجارهای متعدد در کویت
🔹
منابع محلی گزارش دادند که منافع و تأسیسات آمریکایی در کویت، هدف موج جدیدی از حملات موشکی و پهپادی ایران قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/451511" target="_blank">📅 00:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451510">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OF57_iqMTz1e65bUypDLgbNEsE-xv3wAG58h7i1UoqJK-JyvAOpnuR6kGC91YWCsGo7fLMvrMuHyvYQSh2rP-KplBj3IMJdzpqnNepcWvvh69QQ44KR4dZ6f210hq66gxYXdEy_onf822jVYUABlwAc8rLVfniLHL6AFslCK2c37TTCs5mEg2v8sKSwShXMpUkz-8_GcHBX0eOSZxzJgY3PdOucudYKfuNezD1DlVX8Lu47BSIbdf8vTQRU3-MSk6Xr5OD3sIvKPL6YF4-LiByAH8OegNIhS6MSeFEGqrqIw62pnhPt-DUjZutrFpiI6vV6Ku_UcIjUTbhmpPd5V1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعزام ۵۰۰ تیم درمانی سیار در مسیر پیاده روی اربعین
🔹
رئیس سازمان بسیج جامعۀ پزشکی: ۵۰۰ نفر در قالب تیم‌های دو نفره با تجهیزات کامل و به صورت پیاده در مسیر راهپیمایی اربعین حضور دارند تا در صورت بروز هرگونه نیاز درمانی، اقدامات لازم را برای زائران انجام دهند.
🔹
امسال ۱۸۸ موکب درمانی با هدف ارائه خدمات سلامت به زائران در مرزها و طول مسیر نیز راه‌اندازی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/451510" target="_blank">📅 00:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451509">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d151b2a3c.mp4?token=LlTBIh0UKTPKEcGIzzBNciJb6shotX9maSAZIT7CqqDGyzGg_e7aCJhDHdLsq1_sw3GAuzXNQrzJAOGOOJLbAKmos-DiKCT0W_UYeVuC1AWGomLBAzEbKDIeuxqeZWbYGOETHsENZSprVtu402xWcQjSeuQ3zuxt69FohbA0brLfWW9Yyn7UGvcTmn9yAZrG-l0Zogt4Ge-Vz7tCQt8mHC77Buz7nSbt1ANyBL7wZrDb10AbJfrF7bLTkBRFRi34KH8scH17dRVC7uzyx-fQtoecrNB4JV5CP8zslpMfZ6ShmIHwyrxHAuTjsBBt7m3bblufS8MpcFsxkAt_glxduA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d151b2a3c.mp4?token=LlTBIh0UKTPKEcGIzzBNciJb6shotX9maSAZIT7CqqDGyzGg_e7aCJhDHdLsq1_sw3GAuzXNQrzJAOGOOJLbAKmos-DiKCT0W_UYeVuC1AWGomLBAzEbKDIeuxqeZWbYGOETHsENZSprVtu402xWcQjSeuQ3zuxt69FohbA0brLfWW9Yyn7UGvcTmn9yAZrG-l0Zogt4Ge-Vz7tCQt8mHC77Buz7nSbt1ANyBL7wZrDb10AbJfrF7bLTkBRFRi34KH8scH17dRVC7uzyx-fQtoecrNB4JV5CP8zslpMfZ6ShmIHwyrxHAuTjsBBt7m3bblufS8MpcFsxkAt_glxduA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌نویی: فدراسیون فوتبال حاضر بود برای بازی دوستانه با اسپانیا ۲.۵ میلیون دلار بدهد اما آن‌ها حاضر به بازی نشدند
🔹
حتی برای بازی با پرتغال، پورتوریکو و مقدونیه هم همین موضوع تکرار شد. @Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/451509" target="_blank">📅 00:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451508">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چندین انفجار در چابهار
🔹
دقایقی پیش صدای چند انفجار از حوالی چابهار شنیده شد.
📝
اخبار تکمیلی متعاقبا اعلام خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/451508" target="_blank">📅 00:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451507">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca0a05251e.mp4?token=Slujzz_Tf6JMSJUSGHJzAI5khYuAdqRIEOenYyFINYPhwMuLx8Euvl-88CylTFA6qxCGBBOnq3dZDD4AkFJGJgwuiuMuFu1flBKev9dLKDEfbkSFnA8UXB_fq_JpoiyhFgBPSBtEYVQiw7ytqLb3Hh8mKzArKjwnqWo3czpPkaHdzFsFSjNKeoo7cXhM5cu4EdD2e3WXWCv9ADDiUn-y4zFcTW_9Gl2cWFZ2XZCa6U8RY74LuU8bhooThAsKOd1I5XvwzZNR7FGtuzCGZi-BcHMlX7MaWmbu0FSyRyQyMXCcxuinnotlBlOYpE72DtWtK1bQiWZ22uKAjx1MzFbDIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca0a05251e.mp4?token=Slujzz_Tf6JMSJUSGHJzAI5khYuAdqRIEOenYyFINYPhwMuLx8Euvl-88CylTFA6qxCGBBOnq3dZDD4AkFJGJgwuiuMuFu1flBKev9dLKDEfbkSFnA8UXB_fq_JpoiyhFgBPSBtEYVQiw7ytqLb3Hh8mKzArKjwnqWo3czpPkaHdzFsFSjNKeoo7cXhM5cu4EdD2e3WXWCv9ADDiUn-y4zFcTW_9Gl2cWFZ2XZCa6U8RY74LuU8bhooThAsKOd1I5XvwzZNR7FGtuzCGZi-BcHMlX7MaWmbu0FSyRyQyMXCcxuinnotlBlOYpE72DtWtK1bQiWZ22uKAjx1MzFbDIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌نویی: بعضی‌ها بی‌‌وطنِ ایران‌فروش‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/451507" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451506">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چندین انفجار در چابهار
🔹
دقایقی پیش صدای چند انفجار از حوالی چابهار شنیده شد.
📝
اخبار تکمیلی متعاقبا اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/451506" target="_blank">📅 00:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451505">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbadd4515c.mp4?token=IcMDE9Zc0Y8pU879XoxQ92uGwh0Oyh4YMfeUvQtkgBK1XQ1jqV_eqp-S_wUdHaWCzpcREbqInizIq-M1m4l0fX6LHPoSNzTUWL6zAM57fJxZE40VDLx_T1Wv7Eo4I54A86mgFkRi0c3m5dSFMQ1MqAVhW4pBYRZ58cWZSaSYglkhry4vIgaF4I1LIGoKWqhVptrgSt4So3NViD2e2xmBL7HMJQwM8ToXVMPYnGdutnAZ597hCVzM3IwjwDP0xMkNzeHSCgKwM_B2kufHLb-oHR8Zp3Ix5iakH9d2S3310KRxeQfaSy0ARWRt7TYgFgKlarY_1-yJZrvv6WCtkvEkCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbadd4515c.mp4?token=IcMDE9Zc0Y8pU879XoxQ92uGwh0Oyh4YMfeUvQtkgBK1XQ1jqV_eqp-S_wUdHaWCzpcREbqInizIq-M1m4l0fX6LHPoSNzTUWL6zAM57fJxZE40VDLx_T1Wv7Eo4I54A86mgFkRi0c3m5dSFMQ1MqAVhW4pBYRZ58cWZSaSYglkhry4vIgaF4I1LIGoKWqhVptrgSt4So3NViD2e2xmBL7HMJQwM8ToXVMPYnGdutnAZ597hCVzM3IwjwDP0xMkNzeHSCgKwM_B2kufHLb-oHR8Zp3Ix5iakH9d2S3310KRxeQfaSy0ARWRt7TYgFgKlarY_1-yJZrvv6WCtkvEkCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در بندرعباس و جنوب قشم
🔹
حوالی ساعت ۲۳:۳۰ صدای چند انفجار در بندرعباس به‌گوش رسید.
🔹
صداهای انفجار در جنوب قشم و دریا نیز گزارش شده است.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/451505" target="_blank">📅 00:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451504">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oqi8ElQE4GtlCgxDoTwbZXkMshVCEdvD9zX_Vpn88zC3xp5AWscnXV0hX9eEo8UhpxYOKc7Jf5i1qSAFvoVE7fUDSMiKvjOBRmB_SVWxUf3nhiF9lFCTROs3raIlVVMGBwYZl3fcAAZlH181cLUO2xO4_ANFN8iE5AzAD4FGaTBWG90F33EVgxioJgO6572_wF2VrMfaHWW3wtG5Iwxp7pGondsszaPjE_HF9KNuBFGMCzw8YrQu0pg7EuonocjHUghBSgpw0qVZgh2DpTHRt2OskH5AHmky2rDm1mm5LeSdlGgqNjleczYxLhECCRuVeMDack1FTqPcgZeMwfJQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم تشییع اعضای پیکر شهدای مدرسۀ میناب
◾️
چهارشنبه ۳۱ تیرماه - ساعت ۷:۳۰
🔹
هویت این شهدا از طریق آزمایش‌های DNA احراز شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/451504" target="_blank">📅 00:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451503">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52baf9baca.mp4?token=hww83RpKNyTJAi6JQfkN112eO_Z6mb2Y5Kpiu34JSurAuuB7pADcUVYFWaeWZb3sX9TIaL7qvqkg0zEuK8GstTUwihn3tv35DQLqPkqUVEexNY8_iz-zlRQKBp3mhrvADBXgIznOh3iWFD-DZzALhMoJTcgt8nhf1rOGexGcf7KMyetMCcw6ahYeLWwZTpstu9FJFB3ClOVZksbvMvEd6DGn7iS8nlTRsSFcnZk_dzBEbf03wQZWb_TmXaeoaDi-kMWr9TpYQRxlatlN5MX0FKJlgu1-MXx7oaTKM7Jl8moXJ3x5Zt9Cq50s96PEMu0cNb6pk780eEhN23-AN_toIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52baf9baca.mp4?token=hww83RpKNyTJAi6JQfkN112eO_Z6mb2Y5Kpiu34JSurAuuB7pADcUVYFWaeWZb3sX9TIaL7qvqkg0zEuK8GstTUwihn3tv35DQLqPkqUVEexNY8_iz-zlRQKBp3mhrvADBXgIznOh3iWFD-DZzALhMoJTcgt8nhf1rOGexGcf7KMyetMCcw6ahYeLWwZTpstu9FJFB3ClOVZksbvMvEd6DGn7iS8nlTRsSFcnZk_dzBEbf03wQZWb_TmXaeoaDi-kMWr9TpYQRxlatlN5MX0FKJlgu1-MXx7oaTKM7Jl8moXJ3x5Zt9Cq50s96PEMu0cNb6pk780eEhN23-AN_toIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌نویی: شرمندهٔ مردم و بازیکنان هستم؛ ما می‌توانستیم مردم را در جام‌جهانی بیشتر خوشحال‌ کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/451503" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451502">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c999740c35.mp4?token=OCLMrit14jMaLex5NOJwPYdNQUKhO3yse408Kl-RE3GJpcdUy7xPJz4bQpLgd_I-vvk-5MPpRKoOrYcePt9PVGAT0TLtBsnpQgcWfhlIVUwHMB4wZBtymgfzO4r8h2_J3IUk98LqBqkbM_E_OBXSLCyJ9L63vRHN-EjILku2YsGBRguFjj2Z-0Af7TyXuRhaoCCHLfGKTIY3DKxxeqa1IBPrg3AHtonqD0y6HXPCmb_nC93TEoTRcAWvNIgTUqeHAwaxLAQwrOkFu4OcQk_rqaKajfc4BW0Zyg5qISaIvZXtAqLjeagqS6jMyjMMbgCizgDrHc9vOPa8YSGS9KHKTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c999740c35.mp4?token=OCLMrit14jMaLex5NOJwPYdNQUKhO3yse408Kl-RE3GJpcdUy7xPJz4bQpLgd_I-vvk-5MPpRKoOrYcePt9PVGAT0TLtBsnpQgcWfhlIVUwHMB4wZBtymgfzO4r8h2_J3IUk98LqBqkbM_E_OBXSLCyJ9L63vRHN-EjILku2YsGBRguFjj2Z-0Af7TyXuRhaoCCHLfGKTIY3DKxxeqa1IBPrg3AHtonqD0y6HXPCmb_nC93TEoTRcAWvNIgTUqeHAwaxLAQwrOkFu4OcQk_rqaKajfc4BW0Zyg5qISaIvZXtAqLjeagqS6jMyjMMbgCizgDrHc9vOPa8YSGS9KHKTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌نویی: شرمندهٔ مردم و بازیکنان هستم؛ ما می‌توانستیم مردم را در جام‌جهانی بیشتر خوشحال‌ کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/451502" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451501">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🎥
تصاویری که گفته می‌شود مربوط به شلیک موشک‌های بالستیک اتکمز توسط نیروهای آمریکایی از کویت به‌سمت ایران است.  @Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/451501" target="_blank">📅 00:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451500">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در بندرعباس و جنوب قشم
🔹
حوالی ساعت ۲۳:۳۰ صدای چند انفجار در بندرعباس به‌گوش رسید.
🔹
صداهای انفجار در جنوب قشم و دریا نیز گزارش شده است.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/451500" target="_blank">📅 23:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451499">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAuLYew-8AcASbCpp5uI_pspgVaCEvfArb-piGNkpIbRtrtTXM7YbLY9JMyHB6z9B3BFEiAYPXK9qrPuq73hzYIvBQL-8ZAXkNGg5izlGW4kvmsJatUi_UNIg-7m0216ESRN-XbwkvAPeSAVZa7G0nlyEOuXM_wG3ndOLNJqBJOnnrMTZ3hwEb47yTYsuwQYac-bxPyc9JA-VgQaNlxSfQN03HU7YnyP7enRSXzMAeTANyFouzYXBV3gcMYmL1Qug09MoF7qcnvqt8LiUlKWm5kxckRDybVKrJN25nmGTaY6YGkFh2iS8VEEXlYm3rY-2US4kDT17wiGH4VMdz-hug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: با دستور ترامپ، دور جدید حملات به ایران را‌ آغاز کردیم
.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/451499" target="_blank">📅 23:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451498">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
خليل الحيه رئیس‌دفتر سیاسی حماس شد
🔹
جنبش مقاومت اسلامی حماس از انتخاب خلیل الحیه به‌عنوان رئیس‌دفتر سیاسی این جنبش (عالی‌ترین مقام) و جانشین شهید یحیی السنوار خبر داد. @Farsna - Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/451498" target="_blank">📅 23:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451497">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">امتحان نهایی یازدهم به‌جز هرمزگان در همۀ کشور طبق برنامه برگزار می‌شود؛ امتحان دوازدهم بدون تغییر
🔹
امتحانات نهایی پایۀ یازدهم تمامی رشته‌های تحصیلی، روز چهارشنبه در همه استان‌های کشور، بجز استان هرمزگان، مطابق برنامه ابلاغی برگزار خواهد شد.
🔹
امتحانات نهایی دوازدهم هم روز پنجشنبه در تمامی استان‌های کشور، از جمله در استان هرمزگان مطابق برنامه برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/451497" target="_blank">📅 23:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451495">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca4d55e81f.mp4?token=MtpulGZ78r5IzXAYQFKFjzNzjCi54fVyMnbNp_hcbmQbVe8Q_5sI6l3Q8XTH_0gMoFBE5RMlIpym8GWtF-9Dp_rwZNY8q6Nn6HWQfw3Sy4WP9GmCcqtoCzlLl9e5tjNT1X4iiF5NSY40U6B_R_NZmQddC4DvD8znbrxPZ6cTsx3nnQh3lDu-TEow2Nu-F5iz8u4QYiTV4XeE0sARHnpj8wYF8I-VxWshBM5B3P8ZPoaLO_zJdaEUHjWyUW44kuP8uiHgO6aG8jTnuvfg2Mh5BGXVd031d6FnaoGtwIRpotCZ30hUgqTobdJs8pbkIZyNaA4inkMkQhORIgfrgPY4bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca4d55e81f.mp4?token=MtpulGZ78r5IzXAYQFKFjzNzjCi54fVyMnbNp_hcbmQbVe8Q_5sI6l3Q8XTH_0gMoFBE5RMlIpym8GWtF-9Dp_rwZNY8q6Nn6HWQfw3Sy4WP9GmCcqtoCzlLl9e5tjNT1X4iiF5NSY40U6B_R_NZmQddC4DvD8znbrxPZ6cTsx3nnQh3lDu-TEow2Nu-F5iz8u4QYiTV4XeE0sARHnpj8wYF8I-VxWshBM5B3P8ZPoaLO_zJdaEUHjWyUW44kuP8uiHgO6aG8jTnuvfg2Mh5BGXVd031d6FnaoGtwIRpotCZ30hUgqTobdJs8pbkIZyNaA4inkMkQhORIgfrgPY4bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۴۳ عاشقی در گناباد؛ مردمی که پای عهد خود ایستاده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/451495" target="_blank">📅 23:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451494">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
مقامات آمریکایی در گفت‌وگو با سی‌بی‌اس اعلام کردند که در حملات هوایی ایران به پایگاه‌های آمریکا در ماه اخیر، نزدیک به ۱۰۰ نظامی آمریکایی مجروح شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/451494" target="_blank">📅 23:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451493">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شنیده‌شدن صدای انفجار از حوالی سیریک
🔹
دقایقی پیش صدای چند انفجار از حوالی سیریک در شرق استان هرمزگان شنیده شد.
🔹
هنوز محل دقیق این انفجارها مشخص نیست‌.
🔹
در ساعات گذشته برخی منابع محلی از شنیده شدن انفجار از سمت دریا خبر داده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/451493" target="_blank">📅 23:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451486">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTveuxNOWzWAzDt8g1kWapdhkTfQcsJMoey1RV0-RLamT4cF5lm5wU6kgAOlzXGojq8IAelcDCMdYZuiWE4HxyR6sT_edglIe7ymFrk2FgkdszErRmGp9Ivc6_FdhxguQgdQzwcX1L0lM3sQ8yMRsAK9XoZuodzMKQTX34suFmTTkmPA2yJJD0yP20v8kCaYxPnvvB2xao8xeJyqAGP74Ey6OWHga4ljwJ8sNh4gvHqPLp54jrxWuJc4SpZRPqCjQ2pGmzIaQZlML28b86wGw_Yza21OErhrFhCQ4Ql5NFPDE9dx1-PanQpgi5EVKluGjnYwzT7oclZ7Z06hu_iKSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mvZnerozIIqa8UA5WALnhT9e58wQ3ESkyVTyLlRKW0SHP6-H-agYv_heWvvQ0xvQr__rrtZrSeiSccIZ5c5y_IgnjTINVWied30BOwJkPFxQULXKGbdbzN7YFgIQFq2mIoX7rhhauZibmkX1CQDeNiVyNIetqKzAXunRt8PWoSUHhDjwnkGj6LuNioDTWu-tec43yiXPin_Ja937GFWbiU0MlE5kcIBaM9BMj0P3mETqsrCUogmrJHUmDPQE-OAl28_o5Grj9zxx1HQJ2Npnzw3t91BNv1e1wC0BU5YxbSMw0gS2zbYztq3yX3Yxo7M6xqfXauInztLoPBEr2fUitg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQuHvHnmcSN1QL_PUoLF5FJGVZi1pKfkiw0Azg7iJRPDSnkjjSTmJSbI4WNURemE7BfNft8ndbtlpKZmPN0540xa3d_HO7osqRwDhmXGEK_LBVt2G25TvSvH3AR5IhE4Al1mDw8R6M2sdOHbcjIQVAraO_L6PVHeRrgjQn8Jsl3Z4QPidHyjTfLSlXpHKFBnudRtzBa8Da19H0Eg0RvNIr3N2zjLsGbBBjOC7jDYjk5OnI1uRsa3lfgH0efbECoeNLntXjSUPCruYHpTPQNXqtgxg9JkhT8NTO5B0fPh0_EqznCKDn-IFz7R6bucEe9KW6xynfrTceP2i5eotSwNZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EAmsu0AGeL3uEEHsUfzKMsWlFJtL8t7hlKHZkdi4rFArpWi_FXtlOJ-9byIWc7Xe006NwE_LAYmfrParQK1YyBRKQY5pKBvMRdKlgQff8IUdSIs1LIlOjGaDes0Smc1ZtEbYFGWBecyQpbIv3lDDfm9AQUKehn2LbazktSjYxy7Yb45UAJj_U0eknmiJmxm3AJZ-gxf7g1xw9zeJuPwvdGl1IvNYk4UFf9XWAAR5TsPb2hAzWuVRXXvcS7PNs2Brkxlp9n9KPb-GFTLK78d85v3Kmi8ypgoENCCDSwRm_Q4vurSt9WncWVX3L3CxY55KxaIvAuKdmu8NAk-crsrvUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BVGSS1zQPhB9FRc6BhGH0Z_wGvlZktI17yZigyvMZdrqqFCKOtFnBHYzbwznjxPGtT71PHbrcEaaxhHh5a1kPRJPMoc1MtLZpVf_iUkwqOy7ZxlF9Jec-PzmJmGpz0Ls2jAJKzwGdG5WiVE-do_TUL7S22xR1kxlAzWFRfgOJpJkYISBWr05EccXVvLTM8BgTr3tD_tzgRv5AGwWOO1JkMtZYc5YN9QJdJZrL8dz1BDp2pZD2C18wj7oC7ZW421dwKyPsLZXb3jojoYtlIhxtk66wKSpkMmNmvKk10htBqg-cgym7UXY-7z-giwhMPcoS_yxvwXCJnUkJ3Kug72ABw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLFVYDWjXyZeZLUT0vtpZuyIzJJCJPefUIHd9FxavUrm8enpfd8MJyM6O9oWODLVFwSQ-MqnMIvkqwzFP-yvTAcoS2R5A6V4bonAohWsduGOw0IrVw_sJDjG34ZQhKyMO9LuTRBXHBv84-vFwcUAnyjpSl0A89Jkg_p6wjHyXh2TV5Xn9MQXfGBKly9jw7uTit1GzbPK4HOs2ay9EW6rAdBbzwO1wLT21pu0J9UjcMlTCBK8lK-SaEvgLaVw5_wmpxBr8-cG6RVXu0XH6G2uXApdOXPI95J2tVMMpgXrIoDUR9sjhLof7br0kRwHjCQBmCNLbc3OsBY-lCjUxyMmwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iEWs3dkdkPybUuKHLpPvJzqFI5C59a7q-kaZq39d4vcIGHg42-vg7QUmL9uYWPEYI1d9L86s0-xlBH2xYtPd2_tdI1cPEEfqmHnNf0R7FN1AIxSDBT7fcYlQjcRQAGrGa8CMgQNeU2PPtCuYKvDUODEWBl4GodixdHEfm13n_zLnODmyGZWz9zuCJIS2mJ9pWMwWSOykldMiIYT56wjQZYNfuImg3Tx2BhmoRJVpISB9C5CSGIhxQR5FFOdWRFZnZGnScpHN0VvPrACpmYr_astytucyZTYEFa31CVika0GcuvD3rwu_iypTrlZC2xIciWy6Jn_j-Wd1bHK85cd71Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرواز رنگ‌ها؛ هنرنمایی بیماران پروانه‌ای در مترو تهران
عکس:
دانیال همتی
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/451486" target="_blank">📅 23:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451485">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5895b61c08.mp4?token=SHoqYaJjVJPqY1-h96W0Z1Ae7nt8QNxVfjO8U6QbFjuwUMaxmj5RMuE_fizD_MPPlTQXDDkSRdIsE6MJrV83XWAcKUm9iLHKSXviKFTFofI6RZ5H2uGyGaYK_0I2k2yu7-dETS61E960ay7JOlLY1HFCBxAm0KpszHc09vwg93j9d7ixNqBN7yZQWwFLy7nHqRuvIPw84-dXcRz8HKp1dSl5PBAjp4ORe6uDnyCQbqNuMs32N4c3oWbKNVSth_8tDd0DiaxX_aOsv2zceofOwv5xLXYK6wYvDNbTs5wfB--AKnYGW5AHDo2m_M_UfewfNNMBkPbKoxSfBGBctoSqpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5895b61c08.mp4?token=SHoqYaJjVJPqY1-h96W0Z1Ae7nt8QNxVfjO8U6QbFjuwUMaxmj5RMuE_fizD_MPPlTQXDDkSRdIsE6MJrV83XWAcKUm9iLHKSXviKFTFofI6RZ5H2uGyGaYK_0I2k2yu7-dETS61E960ay7JOlLY1HFCBxAm0KpszHc09vwg93j9d7ixNqBN7yZQWwFLy7nHqRuvIPw84-dXcRz8HKp1dSl5PBAjp4ORe6uDnyCQbqNuMs32N4c3oWbKNVSth_8tDd0DiaxX_aOsv2zceofOwv5xLXYK6wYvDNbTs5wfB--AKnYGW5AHDo2m_M_UfewfNNMBkPbKoxSfBGBctoSqpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهپیمایی پرشکوه مردم بجنورد در میعادگاه ۱۴۲
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/451485" target="_blank">📅 23:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451484">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea6b80764.mp4?token=rR_TSvfkKPBTpCrfm59fX367Xo283fjV4mylUcvqzkLsPyEdq2D4-FX2Vtsis5OGucNjN1s8RbVw3oGL1kMoAMracFMk_KuCdEXJqGpWOaX7QroNMn-yb_MPVGiQQ2xcm04i5b6DXguwJFjm8pCGPHk719P2Tcg_8Mej5GPO7EqKl9Qihew_Ps-GmDIWyJMXu_2mAOz_vW6HeuJjsT3OAo7p-j4Eo0jDcizo2Pm86l85yMrQ6PWAjuplo8lK8LyYU_jhspBbqBZvPS8_zMPDc0CrwC_fJZ5B5jIPvCB_UAN0-40rS68MKUa6GDO1V21wC7ZeD2hxspna0yi5JnD2JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea6b80764.mp4?token=rR_TSvfkKPBTpCrfm59fX367Xo283fjV4mylUcvqzkLsPyEdq2D4-FX2Vtsis5OGucNjN1s8RbVw3oGL1kMoAMracFMk_KuCdEXJqGpWOaX7QroNMn-yb_MPVGiQQ2xcm04i5b6DXguwJFjm8pCGPHk719P2Tcg_8Mej5GPO7EqKl9Qihew_Ps-GmDIWyJMXu_2mAOz_vW6HeuJjsT3OAo7p-j4Eo0jDcizo2Pm86l85yMrQ6PWAjuplo8lK8LyYU_jhspBbqBZvPS8_zMPDc0CrwC_fJZ5B5jIPvCB_UAN0-40rS68MKUa6GDO1V21wC7ZeD2hxspna0yi5JnD2JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهادت ستوان‌دوم مهرداد پاشایی در حملۀ آمریکای جنایتکار به تبریز
🔹
پیکر شهید پاشایی عصر امروز با استقبال مردم وارد زادگاهش مراغه شد و فردا در این شهر تشییع و به خاک سپرده می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/451484" target="_blank">📅 23:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451483">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d61070b2f.mp4?token=A60ln6-8kgzNzhcYpdbAxa22flptUq3lbfP6b0em6z-fVL2S_QW0IheI39QleTve9Ba5oOuYH7XA2ipjEi2hcJKbzXE1xHaQZZw2PNRw6tDd57hgokbn77ktboPsfaLd81esFwdbvA8qApylHIB7eecEXK39ETv3gSg26YYhVWGmtW0-5SlTB9tE2KGDDeip5zhfBv0w_POEnbuCBEp94QnbTsn4uFBLT7z1qZwLaeLOxEiQZnbeHIzzuC6xT8EiRWtw8B_08Y6g6QfAoaGExqpG886MXzUaPXu0GHh4f6WiCpB1lzRIcb6KN5MvYkge-aTrUk4r53KJRQSRAR8WOoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d61070b2f.mp4?token=A60ln6-8kgzNzhcYpdbAxa22flptUq3lbfP6b0em6z-fVL2S_QW0IheI39QleTve9Ba5oOuYH7XA2ipjEi2hcJKbzXE1xHaQZZw2PNRw6tDd57hgokbn77ktboPsfaLd81esFwdbvA8qApylHIB7eecEXK39ETv3gSg26YYhVWGmtW0-5SlTB9tE2KGDDeip5zhfBv0w_POEnbuCBEp94QnbTsn4uFBLT7z1qZwLaeLOxEiQZnbeHIzzuC6xT8EiRWtw8B_08Y6g6QfAoaGExqpG886MXzUaPXu0GHh4f6WiCpB1lzRIcb6KN5MvYkge-aTrUk4r53KJRQSRAR8WOoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون دبیر شورای‌عالی امنیت ملی: آمریکایی‌ها دربارۀ آزادسازی دارایی‌‌های ایران هم کاری انجام ندادند
🔹
نقض تفاهم‌نامه ازسوی آمریکایی‌ها فقط دربارۀ تنگه هرمز نبود. @Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/451483" target="_blank">📅 22:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451482">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">تعطیلی ادارات منطقۀ سیستان و کاهش ساعت کاری در سایر نقاط استان
🔹
به‌دلیل تداوم گرمای شدید هوا و وقوع طوفان گرد و غبار، تمامی ادارات منطقۀ سیستان فردا تعطیل و ساعت پایان کار سایر دستگاه‌های اجرایی استان به ساعت ۱۱ محدود شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/451482" target="_blank">📅 22:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451475">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pB0aIXPsU9YqnrAOvA3LwPNISgHM7DTBabu0LgHRAGWFXQMGmujgriEht8shAzAoqsmQrTJGIwiQK-0KAdZ5FpPMkwx4w_FjlnRXuIPPVN7YMMP5DpJ8J-O7f5I92q1IJP5eFKbrygyknLuSTAl2uQFUWlqaUOs4o_BuJXFiqKn3l1sfGtVUIGh7RcdoTsAAl5MPyXmGwmEDMcw4IbZEfOeSFK65IEJwPYgrS2SFkIca1FRgQeCr2NQSdYn7ecTAe9e_QEbyh1CvaBp1zvD6e93CVbFTrdwkCyGp4t3DQlbgASRfoj6mv1m0Ils1FVvddyQkCMZmOHDU9MHQyeg-sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgAG2gxhKkUHwPRsbAY6u54r-6uqvkWzKFGYqNyg1GTs02BHMLf2hjjpUDOpGckOSOstHWekzP2DacoqRwxXlRBI2NSpPTkf9wHU3W8a_v40mTb8c6Nv0sjKmiUDTzXYvqjh8ThoOuZ27Ie03xQSel4k7u2eF8C64XZeuac5CEKeR8oy6lOtwjLW9B87dnqkYNBzkTAVVJgx6I4mxx8S483sd3j95jL5XAB51cvZ3XCJg9z6xrn4dn_qxuDBZxeqOZ-Ofiw5bfUjTlA_APdh3DzMqEH44fjfX_Tjy_c4CK9PaTNreiNkWNtNtdeKattIKEIAmZa97vWZ8fiouLN_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJAEsYRRnvZzz5Woyi-WqWLnW6MH3H3H7iGsAfOSujlsRmplmLLRJ36L15A67zja-A8ho0pQ0iRnewMnBgMS4ZYpXInc_Zaf8Iazazt7SF-R_ktQRddDMpKKXyQRXOUym-1maJxAaWDjW0dV5nPovVG5F-k94m_TnF3hqk2AgvX-SWs-MfnMf4oRY9jwAZdLLK8OsAnpE_vyi1smkjYKJ3wSPbHxuvBTqpNtKimGDO9dJ7TChUjO2W_-9Ds1ctfq954zTEtamV3pNBvU__Rd56k0KGhzRnD2l04gv9wR_qR75XkNFU1ymFBuIc_NEOCgyfcsYPvmPxGh8FCCJu20iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WQuTtc710k0wdNLCLuCYC2Be61e9_UDQPBvyXGzSjWqYgwmDrW2jh0BR7k-voZ9Lks5vWXMC-0-Mxaj6s02LkQuqWV65URw5q3TiyODC7IZbsR00kTQSeXhXEwqN8wppFb4WTO0o0NSwhy1_NewczLTTyVxP4eE52mU5W3PZ_NEZmc2qju2R5WMsFiWRkWD_r3msb5pxwApf5XoUKaI5PQxbqpf6qoW6cYo_uEpTqMsTj--VPlNXJbQ5ViYQLT4HS4tynu0spcTm0rpHalWpUYD4Cyif2as08In4MU-scvr8DlszSTOWTVrqdBUJ9eijyEEFCozfIe3RX8EoDLXLAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rSmWYnIKDVtwf18Duzu-s2IJuK31SqF-t_zKzi4WNtr4MCchK4bc7XK5o5y45RYPeuvfj6F_NPFI-zcrM04sWsN3ZZneAPJCWr_OnIHDVayrIzICgamYE0LdyynWTAjPnnJG-FMgXaXnn5MMvoyH_RrUyE1vv2MMHRtw74_yO1rOULvRaF63397oACeVLu9GDwaJayjh_vwFRfsVmyrtZtOWwoN1XjsZcJlW1UhEI-Yj84_c_2Vpnj8R1BbIMTbXhke1pPmunBkQbDMSgVOqAa_EHPStnz_NsEvttANq7bzZPqRwBD14tdNb0MMlYdT5u7CG3LXg7RPO9loCREP0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mddzZFleDVPTrkBXXHxZkxN-4T8QreI7e3WN_aKIx51QqYfCVGlfbHw5lZJp3WrjN0iymWnJmip_7gNcPir39H-vZDgWDIGJpau6eBoOIZegwmN0tr8d3T362SFLwUWrnq4NiZ5HIJqx32PPz76cbgQ5P6FH3r1y0FfYnWJN5RzpGz0zSDKdJ6xtXcHo57mmD_q7c_42ImvkNb4XPWl9O_Zo0XGpRpyhUucu5soA8cPcMYYL-CMIvogp84OVyVQA4MfUTTEDXLFYYvUg1QaxjD9-tgqizBKpzjzAcCq1wiXN-3BwhWutcjKzrJ9p_SqkhOp4hKr21umEh9cLqh0lJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UvJjoHsKIsd9CMt3D5OvSUo0mvuVaiFAHf8zqLGaoAw7ohMD4rJC2eX46YpnTVZJKptCByM7f-BAHs8KJHoHeM0fHeCFy7OJAuLoi0mfSVAQF-wfKcH0DeUvyKk5NlF6QtMaoulUhiP_cODp155OqtV1nPMInUgPsBKmko3nyfbxmNpQi7KvwCxO0ofgO21fmnHpyZEwx5VFFcUpM4QaLlRoOrXO0QJ1ej9fg8OBmxrAdYDpNhjRaDJyM82VxL7fXqOI9ayCj1pVc8NiiNRPxl1Zyc8DGTzVFeDc3IPRQXLAHZ67wEyi9k2kzxfc5eTWg43dkgA1TC1zzKW6WhhtTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زنجیرۀ انسانی هرمزگانی‌ها در کرانۀ خلیج همیشه فارس
عکس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/451475" target="_blank">📅 22:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451474">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcae8d7d02.mp4?token=ZMZ6fB7PAVHHjK1oXJUtmj7gqKr1v2AFaQiAhrlx5POZ0EvpeWVvtO_VDCH0bvZquhBocEOvfuA5GqYHs3nfZ8x_EgupL-_CU6TRwOM6qzprWLRITmn_EEw4fW9qpJgNXQHS7YVeZHgknrTI4YsM4ZJ0XBA_0xmplemkzuk33aUFl7DU_L4PWYioPBR8ogC7y3gcG6NQXYx_Ejh3GZ1oZ7wADMGX2p8gaxeOEl-CLH8fzNy6e4hWUv62GilI0DeYo0pxojJXuHBZOaR6at5vSx60jCw1KerIYOT-ZWMF3qdd1Am54Ot9ao9RnlKf3FenplYP_gqv5fNewY-SQueasjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcae8d7d02.mp4?token=ZMZ6fB7PAVHHjK1oXJUtmj7gqKr1v2AFaQiAhrlx5POZ0EvpeWVvtO_VDCH0bvZquhBocEOvfuA5GqYHs3nfZ8x_EgupL-_CU6TRwOM6qzprWLRITmn_EEw4fW9qpJgNXQHS7YVeZHgknrTI4YsM4ZJ0XBA_0xmplemkzuk33aUFl7DU_L4PWYioPBR8ogC7y3gcG6NQXYx_Ejh3GZ1oZ7wADMGX2p8gaxeOEl-CLH8fzNy6e4hWUv62GilI0DeYo0pxojJXuHBZOaR6at5vSx60jCw1KerIYOT-ZWMF3qdd1Am54Ot9ao9RnlKf3FenplYP_gqv5fNewY-SQueasjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باقری، معاون دبیر شورای‌عالی امنیت ملی: ترامپ بچه‌سوسول نیویورکی است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/451474" target="_blank">📅 22:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451473">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6e659fab.mp4?token=W94fXHmj2o7TyD7ADB-_M8CJ9pCh-0dUWE9hdlV9BZjo1z64XtixZp2xtIEZTioccabOPFRsWPV150CK-mnfpiDy208NzyLN-SDbR8zNGvg-PTyD0X1zRWAqdzhkOm_pqqwzSddc_NE-DkQdOjix18VD4TbhvPeKvn7XRfGAO2ZgIb2l44M1nhBidb-VoObJznonlSM00sGwGskeozt3jETXs1XNIg5sUzPEpjvsJESH7lrmukSmS-rEr_CJj4dhzKkhqX4vtrtlUn5LzAi32F7zv4JkH5aVj_8vT3zsQ5MUF78nY-4fRcI_SvzXmL2VbdE_iEkfL3TXCVnShwdNgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6e659fab.mp4?token=W94fXHmj2o7TyD7ADB-_M8CJ9pCh-0dUWE9hdlV9BZjo1z64XtixZp2xtIEZTioccabOPFRsWPV150CK-mnfpiDy208NzyLN-SDbR8zNGvg-PTyD0X1zRWAqdzhkOm_pqqwzSddc_NE-DkQdOjix18VD4TbhvPeKvn7XRfGAO2ZgIb2l44M1nhBidb-VoObJznonlSM00sGwGskeozt3jETXs1XNIg5sUzPEpjvsJESH7lrmukSmS-rEr_CJj4dhzKkhqX4vtrtlUn5LzAi32F7zv4JkH5aVj_8vT3zsQ5MUF78nY-4fRcI_SvzXmL2VbdE_iEkfL3TXCVnShwdNgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اهالی یافت‌آباد تهران امشب در میدان چه گفتند؟
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/451473" target="_blank">📅 22:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451472">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uq99A1NduNsa-TGSGkDm7Ou75tcXODo6oW_5QVqzd7eq6QQeaNyfisRNx9MjPHSNw49mIAe6ZQTlRESyTaah-C5HESltCb58UrI99cDtHk-5sCpEs9Nr8Mj7PKQoqWDSA_u_wY7FQSgNw9zguz9xAb5Mfafj_SUWaBRN9sRCZLFspPj3OTww7Jeui1SyKh338n87BQ3AtLv50OpT6MuE5JF3UUWial_01R2bP4GjtazU7Zm12eAIC225qXnAt7HOf9txFaOdXcsUcx7yZxLl3fQqEw16PdxaxbPxQ7hWuQ4HieeLvDvUz2ljmUboX2mfAuIuYXsfBl8ALHZZ-WL4Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه استان کرمان: یک موشک کروز دشمن آمریکایی در آسمان رودبار جنوب رهگیری و منهدم شد
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/451472" target="_blank">📅 22:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451471">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
منابع عربی از حملۀ پهپادی به مواضع تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/451471" target="_blank">📅 22:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451470">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaf299c7a5.mp4?token=iSVKVMT4MWTnwWwMKWCbNwUNvXKZPBKZ89SUQfMJREUD-BPjlitmkzIBHwXxISf7z8jeDUcutlJInJGo1rvigyHUweJ_WXkfSoWlCqrqlqcs_tmEwhMsjqVWnxNqPelOBgpP3TS_O8R1jDXSA9STZJTT6IHo3ZeP3CgFZJ-YEnG11W6jcIzrs8ZUhYnbOBftQJapBE2oAIs5qCeSF7i0IEUAkt-sD2l6fmlbTEoOSTVXRS81XGB4tARi5Gy6vUCuB7ZtBQLzArhGmBoi8JZ7F0jgScdFHTjZWsmkHVK07RGo_59YUy3ZgMiSXzAyuIqtFRUcJU2d1VS-9_Rg4nyqDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaf299c7a5.mp4?token=iSVKVMT4MWTnwWwMKWCbNwUNvXKZPBKZ89SUQfMJREUD-BPjlitmkzIBHwXxISf7z8jeDUcutlJInJGo1rvigyHUweJ_WXkfSoWlCqrqlqcs_tmEwhMsjqVWnxNqPelOBgpP3TS_O8R1jDXSA9STZJTT6IHo3ZeP3CgFZJ-YEnG11W6jcIzrs8ZUhYnbOBftQJapBE2oAIs5qCeSF7i0IEUAkt-sD2l6fmlbTEoOSTVXRS81XGB4tARi5Gy6vUCuB7ZtBQLzArhGmBoi8JZ7F0jgScdFHTjZWsmkHVK07RGo_59YUy3ZgMiSXzAyuIqtFRUcJU2d1VS-9_Rg4nyqDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوگواری مردم تربت حیدریه در شهادت حضرت رقیه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/451470" target="_blank">📅 22:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451469">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe2ecc4084.mp4?token=DnmHAf84g6Q21aXHcBkfbw_5Aa8vTsw51WU7g45aME6rllEehbUKHh7XnF2305XYFhOUtiyuf38FutiCr1PgOnq5dXqrN8G7UBdOR1UKgZGM3roU6RcWHEPbE8fpClMQ54DWEzvL01EqXpHAPe9_PK6sXizgxMYLZkAI5aI0NnGxvjJpEScUuofJ7eXkvMI1gMPlgLfc9GbnE9svGRWnLVWEOgl2nc8GqdVQoFspDzGtNFl5bWPqgZ_JFfR4I9TDExNhtEkq6nswIoMr1M_6SF9fDmgRWXm3zdsVfnv91ScnTQhjG8dxtG7Vl3aM4c9-fcSinJ4z3dy2bpHDVVaNIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe2ecc4084.mp4?token=DnmHAf84g6Q21aXHcBkfbw_5Aa8vTsw51WU7g45aME6rllEehbUKHh7XnF2305XYFhOUtiyuf38FutiCr1PgOnq5dXqrN8G7UBdOR1UKgZGM3roU6RcWHEPbE8fpClMQ54DWEzvL01EqXpHAPe9_PK6sXizgxMYLZkAI5aI0NnGxvjJpEScUuofJ7eXkvMI1gMPlgLfc9GbnE9svGRWnLVWEOgl2nc8GqdVQoFspDzGtNFl5bWPqgZ_JFfR4I9TDExNhtEkq6nswIoMr1M_6SF9fDmgRWXm3zdsVfnv91ScnTQhjG8dxtG7Vl3aM4c9-fcSinJ4z3dy2bpHDVVaNIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باقری، معاون دبیر شورای‌عالی امنیت ملی: ترامپ بچه‌سوسول نیویورکی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/451469" target="_blank">📅 22:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451463">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-7eH-kHU0uKwfmFihi09u3HCNhQnv6o5SnScNrAJIxpiQp8qblZVfROhWbPvlvYW1cCH31KXSNb2miIBd-JKfkAKvIF5N1tp-7bdpa-XXJ4V3Jkn-8AieQo6ftG6YXQ1TF-JOxmE1t3nTTUc1rXw8k2f2NQTxcC8Hox3zetwRZ_Ro138zF_KGk2-05hJyfhhIIrwQe8zvokcgCCAIRx08sadkZSIuJUyaPvLqsCAmnRwxLg1UjsbZtYj_ylcxai1wN8chx6suLwUWPRaa_lcKi0dDQV5A6vtnL8rKC0veHbh0pG0J0Xadx0ublI3uB4ZsUFy8T_EAOi5YV3Wt5zdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VFm0ZghKM5LOssKGgB8j6AmZP2L3uuHsmw1IYObwYua-XS_MQCYTeaFuHMXozSJ9mXWxZ4w6tb285YSTY-ZQ86BPVEL_Iv3Q9W7niG5RXlKVSaGdjhP7PTb_HJGVR1eBEY1xpxhTfp7o3PWxZlY1ytNvpTtyj0UOdgdpb6XVbfRq_b1g3ihHXQajp_gRCGpDa_VZDre7M-KmjzxatEu5eA1quGU5somQuG27qDuEGW4Q0arEangcm42EreGz01v2qvxVrpTkAtrP995Eo_KSH7hVzGZ_sdBMUT3obHwnRyPKeQZQ4l2FUokoRfL088VJwFWvMdXVJ-mA3llaBOZo7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFBluV5-4ytStd_cI7uMOjIn2pK6SqvYY14BeUs8L9ZAGTYokxHTcPJD2r6ZUtWX04ch99PuKOf94R5fed5imuJE0pV7pw2BOnY_ssR7ij__oTdetZ17RiSeQ5Iyw2R5BkQ-8t9BRpS6vs-VoXoCawnYKe7YFPpk8PY2FZ0KxijZhyK_YEilCsqb1cIIl3xmuYJT4SbsiKUQGt3H26n9QQWzaXXKPjuKWmNXmbrTzV6geU0gcRp4w1yMr1UZQCd3alJsR3MrUr5hFRFnnENjTqgQ8gTg0D1RtEZJOQ7gilc9SsKqMfidzfGTpg14x8ab0Fpon4H6RlXWR-ig7YWvQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHQMK_BcJLHLPwR-aU8Gbw1A6HiiAZL3M04lh1zZh2Cm9mdBqGEOG4-V7ksdp-mfBc307PtZ5pMqA2jCADapb9sBxeD--u7RQe4PTnrMdOTLXZnza3bV5LKxT1jZ7j-tMTN2jSDqSDNh7rVvmW6OaS4Pf1wixmuxCxqDHxVA_Arglcc3RFyD1xXYSEAnSSWwMqiFJ5VzjPhwNSjYgb4Spf_41s5pNbMaV3LwqhDsHHSOaatUfrgbqXBSDRFyPspCeYD69w0hyeBwDiOww9iudHdnXfw_SqSG-UVPy_Y0aP2Y33_g0WXO62r3001HG5k-OiKKJwcUfyQlZQ9laAPwWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-onU2O2GVCkO5gYptr0B4IWVdMhJ96JCDdcnxpM11I4ZxH1RuDg1A-BfwWED-E2A8o2Mefz_kU-LCCNI83P3Zhk9obLA3qkRC6CNtWxCkgRn0-na9jnus5Iiph77wa90kk9JHWof_y5ruQtqSoXR6huz6NTMcVv3KQVoMKKD7qzfI5CnZ6o7UWWFJo1c1cj9XCtAwnJ0kLsApc45YdSWVsPHfkgKKghpFY4s_5rOMhk4dyuSrD30jfrhA-gAy-mfKhP_QqCX3KkFQ9EUiK_781PYITmE59QcM24g9-KZvFTClDEn1SQh1thmjIYDNSmnGiSvTAGFRrg7haifT3zXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ffhb8eCKLQU2GHPsa1PjSvE_QhioaHMcqmb_LiegppVFDKZPyk8LTRA5iumavd-8osX6n0jo_w8LCptbTjp4q7PxuprFp6vVRrLI1ILz9XUAAv1LJtvvgmLIQeV45vMpWeZZA9gHfiy9Wdp8TYle4HrrPrvjtzRwYra4dRvfxUVDYW26VO3ulgWy9P1EnEA8Hb4xqMqfFFn9A6TDxqwHRP6rHDUf4DBRpo_HW6FVYdkPExbCyZgfpuk1cpXqewiu8dEQ6DgZssoz7Ysu1CFurx4mU_WXuinARCLGm2JtKe4YaS54iiR4RBtrMhralG_pR83X7FL0lOefbQJPbwEBCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نصب پرچم عزای امام حسن مجتبی(ع) در ایوان طلای امیرالمؤمنین
🔹
برخی علمای شیعه هفتم ماه صفر را روز شهادت امام مجتبی(ع) می‌دانند.
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/451463" target="_blank">📅 22:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451462">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgGlQjdgAUKwfXctNJPEG5RDy5BcYUIqZQS0hqMmG5U52f4Qak_vElv7niHCXH19SF7T407i9oo-4RtVJaRvzPcJBZ7aaSgak8aBJ14x_REEZN9hPJeF56B1MeON5qb77o3cVb93kWXquqB0B74dd8DP0uk26T-PwZC98bkF-hsu724QMLGoCyzl2D2ZMdcL8MnEKyIV2W4ATa_MYhkdcHJrwJfGI9g2tgVe3wHBKcdmrX1hcP_0Wud7pNhn_yi2cjUvZwcalI2Y8PFc7DwwSZ2hsmQec700xzDAN2DGJA0-UPeIN22ns9SSBlfbIBqD2FBlR90X1p9j6rdotCee5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
منابع عربی از شنیده‌شدن صدای انفجارهای پیاپی در سراسر اردن در نتیجه حملات موشکی ایران خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/451462" target="_blank">📅 22:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451461">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvHJ-dV0LkppUn1WVBsNzbQKOIGpNY1QoUQIrR11eI1217nGs-Bvp4c-QF0syAt7f6eGwrVpb5DYmKmRG5rBe4XcuOhYkuZIgcWF9qH--wK-5w5Ul8tk5V_msQpuQ2kLcBM37Wg60Cq9e_ZgxdsFcaLs569-jkpyX8z7Ap27tnojSeIDmYeuPST9Bcglb6_15W1OI7ggdPY_kP9iDcg8D5KWtMpX7xPB4kkXsMdQB8-V0ANUOik2TRU0R12Lo4DKg2sbFZA2vRb1j2UiavT8k_3Vfg8QEFp5lP1StsbIN1p-i8EeVxUIkdOYg-GdPTg59H4DHBzZ2WbJWPaPx1ztgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر راه: سالن فرودگاه بوشهر در سریع‌ترین زمان بازسازی می‌شود
🔹
دیدن صحنه تخریب سالن مسافری این فرودگاه بسیار آزاردهنده است و بار دیگر نشان می‌دهد ادعای تفکیک مراکز نظامی و غیرنظامی ازسوی دشمن یک گزارۀ اشتباه بوده است.
🔹
با همکاری همه بخش‌ها، بازسازی سالن مسافری فرودگاه بوشهر در سریع‌ترین زمان ممکن آغاز خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/451461" target="_blank">📅 22:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451460">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
منابع رسانه‌ای از شنیده شدن صدای انفجارهایی در بندر عقبه اردن خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/451460" target="_blank">📅 21:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451459">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84a39fa6d7.mp4?token=feZyaSrcHMIWhneDfP2dJx3NmzEwH9TBSueG-jsH7QonDKpJe4ol-w_-tbeedzqglQ8k4kQPNdu9XULTHTaau2MoTkBgInMJIUxWKKPqGkIR2fBPUruRI36wB_7VcWr3uY6IfQrNZ7A6JXx5uSWbo9yfLfuixxIp1UEvRYxhFbsYI_b96VedLrsifh90fz6ZtxXpcybzeuILO9m3ZjxdtoTRZAlwtwX6KsdIowbFPcpEKQbk4kWOrPea4bnn6Jo9aOYzpHXAtWbsu3JSM99YmMhUErAB3yVocTggnzGxf-p479B8py5n43EPKEF95kGwiOmJ1S5X18zRXUjS0qWWoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84a39fa6d7.mp4?token=feZyaSrcHMIWhneDfP2dJx3NmzEwH9TBSueG-jsH7QonDKpJe4ol-w_-tbeedzqglQ8k4kQPNdu9XULTHTaau2MoTkBgInMJIUxWKKPqGkIR2fBPUruRI36wB_7VcWr3uY6IfQrNZ7A6JXx5uSWbo9yfLfuixxIp1UEvRYxhFbsYI_b96VedLrsifh90fz6ZtxXpcybzeuILO9m3ZjxdtoTRZAlwtwX6KsdIowbFPcpEKQbk4kWOrPea4bnn6Jo9aOYzpHXAtWbsu3JSM99YmMhUErAB3yVocTggnzGxf-p479B8py5n43EPKEF95kGwiOmJ1S5X18zRXUjS0qWWoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع رسانه‌ای از شنیده شدن صدای انفجارهایی در بندر عقبه اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/451459" target="_blank">📅 21:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451458">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
منابع عربی از حملۀ پهپادی به مواضع تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/451458" target="_blank">📅 21:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451457">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/850e96d1ea.mp4?token=vdKUENOBc_JUoG2Pnp8IRPUUz_OGtnEgDvraCobqlvZDuAWDhiPK-IK_rXJ8WGsYYdrwNuVsadqFqPEYBw003l4hae8a0S5sINnR77gJ-L_MjhgQNzrppvywZFDxsH63NL9RVlUr3I_XMBPFg1SAX71wBfOWYEyql4TdXOcV2jy6MSXIDv9rVIJ7ngNJ5MhxNUptRsGsIF_EAE7H60NhdYdvJlrq-3uswGCL-RR5_-l5K66ekflzOtJX6o0egRdtuhfHVL488_n2RuikTyBhhTtl_4bZtTAt7uw1AYlal7ccSCxMQwdODYDvZc4IU2bY3E7UD_znGGf1BjF0aDkKJzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/850e96d1ea.mp4?token=vdKUENOBc_JUoG2Pnp8IRPUUz_OGtnEgDvraCobqlvZDuAWDhiPK-IK_rXJ8WGsYYdrwNuVsadqFqPEYBw003l4hae8a0S5sINnR77gJ-L_MjhgQNzrppvywZFDxsH63NL9RVlUr3I_XMBPFg1SAX71wBfOWYEyql4TdXOcV2jy6MSXIDv9rVIJ7ngNJ5MhxNUptRsGsIF_EAE7H60NhdYdvJlrq-3uswGCL-RR5_-l5K66ekflzOtJX6o0egRdtuhfHVL488_n2RuikTyBhhTtl_4bZtTAt7uw1AYlal7ccSCxMQwdODYDvZc4IU2bY3E7UD_znGGf1BjF0aDkKJzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرهنگ بازنشسته آمریکایی: اگر در کویت، بحرین، قطر، امارات یا عربستان هستید آماده [فرار] باشید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/451457" target="_blank">📅 21:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451456">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22b7a458.mp4?token=nP7Blj59k8S86pbh2VuyfAxYkrHnqShwV5PP_kwdnM7Lw6cqcsgSN_ZfN6D-2IRisBaow-B9Zc0aj9YtgQ3tXhSmVO0ekMft2czZ8KkomcnXLkBNSa581XLKUm6MP41738WHNPt43uhBPKUFX8B5LsiTavX8-5d66SI8z4g4tzj9LDHB3RxYivA8WaEyo6s0cIiBJqtOzdfUu446ME7oggPsca1LNGRiW-ODBDxGEf9VqQzncDHxs77ES2lCkQGv6Jq2eyjnMiwfiIOreZnHe3KnmN2x3x_XytKQbIYQgbLI9U7pB_y-An_7AfTkLfP_hbTrdSo7SmRvp99siJELMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22b7a458.mp4?token=nP7Blj59k8S86pbh2VuyfAxYkrHnqShwV5PP_kwdnM7Lw6cqcsgSN_ZfN6D-2IRisBaow-B9Zc0aj9YtgQ3tXhSmVO0ekMft2czZ8KkomcnXLkBNSa581XLKUm6MP41738WHNPt43uhBPKUFX8B5LsiTavX8-5d66SI8z4g4tzj9LDHB3RxYivA8WaEyo6s0cIiBJqtOzdfUu446ME7oggPsca1LNGRiW-ODBDxGEf9VqQzncDHxs77ES2lCkQGv6Jq2eyjnMiwfiIOreZnHe3KnmN2x3x_XytKQbIYQgbLI9U7pB_y-An_7AfTkLfP_hbTrdSo7SmRvp99siJELMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تطبیق تصاویر ماهواره‌ای سایبرالکترونیک سپاه و سایر تصاویر ماهواره‌ای
🔹
گفته می‌شود محل مورد هدف، یک مرکز داده C2 ​​و هوش مصنوعی ارتش آمریکاست.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/451456" target="_blank">📅 21:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451455">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🎥
با شنیدن نام‌های آبادان، بوشهر، چابهار، خارک و سیریک چه حسی پیدا می‌کنید؟
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/451455" target="_blank">📅 21:29 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

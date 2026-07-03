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
<img src="https://cdn1.telesco.pe/file/CWXqhe21GzIUJAtSaCFcy9Es6bPeMCcxfoHqor15vgeyzSTGYvQNhULm67IWehfFz2khW608VJG3mA2laUJ-dU3egw77wpftNg6BzcSyMlNs_nrgRP5TkEZ3txYrlQlXt9d863L6qQiQvnQ1SlEsKLmGDlsVldG9JVsberqzZ_WgjCUSDticif5cBC5Ta-_jVCHGjKkoB3HcPhXghe3GFEimC-mLCpkL2OOF9EmDONL5My-9EjCnjYh_M9ASftnOutKhXtMeiGJ19BJbly3fOl1c57cft8x822YHufTa1_0H6AZSUkPB5NPLdN0LfUPoSo_dkCU1lYDXJe_GEcUaMg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.34M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 00:05:52</div>
<hr>

<div class="tg-post" id="msg-76778">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cmmxlR7a6h9hrUCb7VdYAhCDWNgcp389J9uzIzVE1mvZakxx5UJfWzG3H_218Xq0AWZ9sywOjXKeG057U5-czYYWZJWa79Mp16egTG7Z-u_Lxd4_Bf73zW3oN-1isvnBZGG5xhR-poKePikLOAP620QC_Hv7fFfIGBXK4OHtcOa_-se__2VjQicAEJqOLsO4dH0O9X7a9zChXs7MQoxZtj9P4HWZw3Kz11GCrtzzQlxpJiTk0qHC_tx3zBWTvAs4e9jdy6ZIYxnXo9-W_09Jkh-lhxMQFNCOneEkMYd5674jdfH-8S5pvoZKDvfTb9QdD23OLT_ZZmHtY6BDr4iuiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f3b6da11ae.mp4?token=mealktIrEoTB1pPQKDrDjDElzgFK80HUefPXVTU1TL96M1rzTxdBMwcJ10zqBvqG_L8O1LQ5VgnbwWftrBTomdH8y0lkyGXbz8lb1_uUBMCFZcxW9nLaY8r3biR7ybQhqnGCR0Ns2R-4Oy8e0NQ6PO-hQS8_2r3lpq_Jxq5MInQTowygLn_lwy1LaYudCs5oH9SU3QzW6giNTxwTQKrO07cfrSmMAk0xl3ekKUHQ-DSYv1k7JG5FTGUZc3UU6U0f0fpu-MQYPLYhssw9vx9BLYdzFnar_Qa83OMgTf_hFh911J5FT9y2mFd_6kZMgzgRWjSCT2dP1q_NMjf9OGwsog" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f3b6da11ae.mp4?token=mealktIrEoTB1pPQKDrDjDElzgFK80HUefPXVTU1TL96M1rzTxdBMwcJ10zqBvqG_L8O1LQ5VgnbwWftrBTomdH8y0lkyGXbz8lb1_uUBMCFZcxW9nLaY8r3biR7ybQhqnGCR0Ns2R-4Oy8e0NQ6PO-hQS8_2r3lpq_Jxq5MInQTowygLn_lwy1LaYudCs5oH9SU3QzW6giNTxwTQKrO07cfrSmMAk0xl3ekKUHQ-DSYv1k7JG5FTGUZc3UU6U0f0fpu-MQYPLYhssw9vx9BLYdzFnar_Qa83OMgTf_hFh911J5FT9y2mFd_6kZMgzgRWjSCT2dP1q_NMjf9OGwsog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/76778" target="_blank">📅 19:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76777">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/555882678d.mp4?token=jP5WgvD_AAcM31GhbW2iOSW9nai1pMgCPn1D_O_m6WWloS8VodQlz7dVScf2t-i3FAzUh9RLagfe-bPs2nOs7GZ4j-BR29ieVNzUnM6tP2ABohWDM4-0VOG3kwR-5s1d_nUkgbA1XzP-i-Q4ANB3__tjk_vCZZ4yLUXmWxQ6_XFkV-ipIiDcIkGHk2BrVCFby9A8ecr5Bw4jBqXmr9-thV293c3U4iaLWMkU4DkrsXob1n3guFpnOgH7u1tM6neuaekmCxIq0-UDAefjGK0E3V2r6NkYlbKJRTm95RbUyw_YnpXRBLIzLJuWkJE8_maRGiqqQ76F9ArMqQG9hOi_-g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/555882678d.mp4?token=jP5WgvD_AAcM31GhbW2iOSW9nai1pMgCPn1D_O_m6WWloS8VodQlz7dVScf2t-i3FAzUh9RLagfe-bPs2nOs7GZ4j-BR29ieVNzUnM6tP2ABohWDM4-0VOG3kwR-5s1d_nUkgbA1XzP-i-Q4ANB3__tjk_vCZZ4yLUXmWxQ6_XFkV-ipIiDcIkGHk2BrVCFby9A8ecr5Bw4jBqXmr9-thV293c3U4iaLWMkU4DkrsXob1n3guFpnOgH7u1tM6neuaekmCxIq0-UDAefjGK0E3V2r6NkYlbKJRTm95RbUyw_YnpXRBLIzLJuWkJE8_maRGiqqQ76F9ArMqQG9hOi_-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">[بنا بر تصاویر رسانه‌ها، مقام‌های مختلف در گروه‌های چند نفری در مقابل جعبه‌هایی که گفته می‌شود بقایای علی خامنه‌ای و تعدادی از اعضای خانواده‌اش در آن‌ها قرار دارند حاضر می‌شوند.]
رهبر ترکمنستان، روسای جمهور عراق، تاجیکستان، گرجستان، نخست وزیران پاکستان، ارمنستان، روسای مجلس جمهوری آذربایجان، عمان، قطر، عراق، ازبکستان، قرقیزستان، بنگلادش، مصر، وزراری خارجه نیکاراگوئه و کنگو و معاون رئیس شورای امنیت روسیه، رئیس اقلیم کردستان عراق، به همراه هیئتی از طالبان افغانستان و شبه‌نظامیان مورد حمایت ایران در عراق، یمن و لبنان و همچنین دبیرکل جهاد اسلامی فلسطین در مراسم ادای احترام شرکت کردند.
از نکات قابل توجه عدم حضور مقام بلندمرتبه‌ای از کشورهایی مانند چین، روسیه و ترکیه به عنوان حامیان جمهوری اسلامی ایران در این مراسم بود.
تاکنون تصویری از اعضای خانواده علی خامنه‌ای به جز هادی خامنه‌ای، یکی از برادرانش، در این مراسم منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/76777" target="_blank">📅 18:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76776">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CuItH6D1tdVJqU9gLf9pZIRe6tJIa0SbRe9_bqUHVe8V7izOma5MLquF-fu2QJMwP-_LZ6MmgkfNzlQBBaLSZMrpDcGqkVqZKwhB9NNPID-K-zAuSEEqxWI_ckrJjqhhwu8MPiRn7PCoMbP_kmV_OXQHU4H2kRnbB6hXR7OEurSes_I4q-VUDjO4vpQeId0K28TkXacU_PxfdhCp-i00QpOAKMv4rtrIFbAKGlVC8UdtX6LkBWQSWXCIsPN3DciFaYrgesilC0FM4LJtH4fr9Ofmttna9Zu-jNyYSfErWzkWuKo_SnBHWnHlSnrU-b9DzBR0q98S06PxBunkbV9b6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سایت هرانا الهام زراعت‌پیشه، وکیل دادگستری، از سوی شعبه اول دادگاه انقلاب شیراز به شش سال حبس، دو سال ممنوعیت خروج از کشور و ابطال گذرنامه محکوم شده است.
بر اساس این گزارش، شعبه اول دادگاه انقلاب شیراز الهام زراعت‌پیشه را به اتهام «اجتماع و تبانی علیه امنیت ملی» به پنج سال حبس و به اتهام «تبلیغ علیه نظام» به یک سال حبس محکوم کرده است.
این دادگاه همچنین او را به مدت دو سال از خروج از کشور منع و گذرنامه‌اش را باطل کرده است.
الهام زراعت‌پیشه ۱۴ اردیبهشت ۱۴۰۵ در محدوده دادسرای اجرای احکام شیراز بازداشت شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/76776" target="_blank">📅 18:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76775">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDcFzfHid2kQ4MeLaLiN1_XXKF1LT4-dOwgqL9HVbQpL8L_Kxv2nxxeNLI-HkzuXO11Cjge_NNsD0eeWuWdKnyub-gh8UuAMSwNACd_7iIgZnD3wrKyNfUC7hpMR5fjcqjxuE7sbWWSfLjjDiFdh3i6CdwstfrDWVxalWsWRwgOGhlAbhJ7yly44xrE1dM_hJj3VQ75ohL4Q-FDvveKEqqoVGKaEF2P0bo7oYRRm4o83gj0zTJ1ACt-Tgyw8uNFQeZ0yXa_29NZEW6yvaDb--uokZQIUyaRSrmm4lQP3kYTfR53WN7X11nNyO_y-ewmL-hOo7azJ9mQGVRtnMUHl5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارغوان فلاحی، زندانی سیاسی ۲۴ ساله محبوس در زندان اوین، از سوی شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، به اتهام «بغی» به اعدام محکوم شده است.
خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، با اعلام این خبر نوشت حکم اعدام فلاحی بر اساس ماده ۲۸۷ قانون مجازات اسلامی و با استناد به اتهام «بغی از طریق عضویت در گروه‌های مخالف نظام و اقدام مسلحانه» صادر شده است.
ارغوان فلاحی در جریان پرونده‌ای بازداشت شد که چند متهم سیاسی دیگر نیز در آن حضور دارند. نهادهای امنیتی جمهوری اسلامی او را به عضویت در گروه‌های مخالف حکومت متهم کرده‌اند.
منابع حقوق بشری می‌گویند او این اتهام‌ها را رد کرده و روند رسیدگی به پرونده‌اش با محدودیت در دسترسی به وکیل و برگزاری جلسات غیرعلنی دادگاه همراه بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/76775" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76774">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CXI4j-CVON1pdaNGmgfm4KKTO-JDTiZE7NEPXpDkBLNapEP1vIZcg2a8RPuHJQsNq9ICUFGDqwihIKg40IdKP_dcLgu7BBNxmTKQfJ2Ja31VnktLjGvzUSjfxK99dlZsyYVK5Og2HHp-osp1LSmZzELhbHnmv8o9YhkxDDu32zSMMru_avd6MYjbw50YrM2bZZzaZgASxkXU7N-PzNkxaV2nGPg8DpUXjm7xB8Lwsadk7G9n9quUfjDSciU0J4pMuCY33ggcPC7d4fMXEE3utizs2IikD0gY_26lm1zE4Thtw_Sd1HeCw_EOtPyf9s22Nnthu4deP7nj-ZkCWcnrzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، بامداد جمعه ۱۲ تیرماه در گفتگو با شبکه سی‌ان‌بی‌سی گفت جمهوری اسلامی از نظر نظامی «کاملا شکست خورده» و مذاکرات میان تهران و واشینگتن ادامه دارد. او افزود: «فکر می‌کنم آن‌ها تقریبا با همه چیزهایی که ما نیاز داریم موافقت کرده‌اند» و ابراز امیدواری کرد این مذاکرات به نتیجه برسد.
ترامپ با مقایسه وضعیت کنونی با جنگ‌های گذشته آمریکا گفت برخلاف جنگ ویتنام، افغانستان و کره که سال‌ها ادامه داشتند، در چهار ماه نخست دولتش توانسته جمهوری اسلامی را از نظر نظامی شکست دهد. او گفت: «آن‌ها کاملا از نظر نظامی شکست خورده‌اند. هنوز چند موشک برایشان باقی مانده، اما اگر لازم باشد آن‌ها را هم از بین می‌بریم.»
رئیس‌جمهوری آمریکا همچنین گفت هفته گذشته پس از آنکه جمهوری اسلامی یک پهپاد را به سمت یک کشتی فرستاد، نیروهای آمریکایی سه بار مواضع آن را هدف قرار دادند و هفته پیش از آن نیز دو شب پیاپی حملات مشابهی انجام دادند. او افزود این عملیات‌ها هم‌زمان با ادامه مذاکرات انجام شده است.
ترامپ در بخش دیگری از سخنانش گفت آمریکا با استفاده از نیروی دریایی خود «دیوار فولادی» در اطراف ایران ایجاد کرده و «حتی یک کشتی هم نتوانست به ایران برسد.» او ادامه داد حکومت ایران با تورم ۳۰۰ درصدی، کاهش شدید درآمد و کمبود مواد غذایی روبه‌رو است و در صورت دستیابی به توافق، آمریکا می‌تواند گندم، ذرت و سویا را از طریق کشاورزان آمریکایی در اختیار ایران قرار دهد.
رئیس‌جمهوری آمریکا همچنین گفت «قدرت و جسارت» جمهوری اسلامی از بین رفته و با انتقاد از گزارشی در روزنامه نیویورک تایمز که نوشته بود ایران نسبت به چهار ماه قبل در موقعیت بهتری قرار دارد، افزود: «توان نظامی آن‌ها از بین رفته، رهبرانشان از میان برداشته شده‌اند، فرماندهان رده دوم و حتی برخی فرماندهان رده سوم از بین رفته‌اند، بنابراین نمی‌توان گفت امروز در وضعیت بهتری قرار دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76774" target="_blank">📅 02:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76773">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uNOcAwZnGqBZ6rMbUDKxmKaE-fhsNTy2E66b7msqdy3Crw_6Cjkj28VHWyYSFZGAR6fAHWfMplojYwXBuBOpGeop7FXwLecB1lzTmYLl7Z1a1680ixnurUU--h9skvMjdT_WOcmlNFs_OI7IXWWKf5l23J1fA_woMOALc_aCxD8dOSvdfmZ0FLsT9NGuLO6YJc9LpbWP4V415zYngIA1vbkEzDWZ6NVwveq2lm1djVRAdw94do5cd6ji_vqbtD6F6rasMp50Rm5MOBPb5LMfeLhsbOpxp_LLm10Xz8oR4NqQ2pnPvmAyrUcqtQyZus4OK2Za6HYgHHoiX_biNTUgFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"دارم خواب می‌بینم؟ سلام دنیای جدید!" ویدیو دریافتی از 'شادی جوانان شهر #گله‌دار در شهرستان مُهر استان فارس، یکشنبه ۱۰ اسفند' Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76773" target="_blank">📅 16:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76772">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nOKJJDhKDH7H9HgHySV8uTCFR-Y82Fq0aNC7oLKYFBL009VVJadWS7OWaWnbYSC72LX9UvyepvAgdu564Zhuco8OmFsu-7MuO7EBBJT8kPIXHVr1EUEDMor7HKdatBrgCB7RV3-7QHntcTfYJ-_ICwRn0yfJFLMaleaCxTAjPjVoaBqL3iK8PR8zw3evQGPCZbXksT1-9H0XJ1Htmf3bVYNxBH8FrKThNrWVIG2NrVNZ1zVhB3Sfo42vcCVqD6gBC-FWwHsodPcquTke5IRuDe9RN9Q5vZEbqMYq4yqT0Z5ZA-rKdggl-DFo6Ad0u1qflqrbNzpKI3XNiE0EqC5dkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی کرابی (برسام) شامگاه ۲۱ دی‌ماه ۱۴۰۴ در منطقه سلسبیل تهران هدف شلیک مستقیم قرار گرفت و به کما رفت.
این جوان ۳۰ ساله که متولد سبزوار بود، بر اثر اصابت گلوله دچار مرگ مغزی شد و پس از یک هفته، در ۲۹ دی‌ماه ۱۴۰۴، در بیمارستان امام حسین تهران جان باخت.
پیکر او برای خاکسپاری به سبزوار منتقل شد.
ایران‌وایر مطلع شده است که به دلیل نقش بستن عنوان «جاویدنام» بر سنگ مزار او، مسئولان بنیاد شهید خانواده‌اش را تحت فشار قرار دادند تا این عنوان را به «شهید» تغییر دهند.
پس از آن‌که خانواده از پذیرش این خواسته خودداری کردند، سنگ مزار مجتبی کرابی (برسام) شکسته شد.
خانواده او نیز تصمیم گرفتند تا «روز آزادی» سنگی بر مزار این جوان کشته‌شده نگذارند.
مجتبی کرابی مربی بدنسازی، ورزشکار رشته فیتنس و داور رسمی پاورلیفتینگ بود.
یک منبع نزدیک به خانواده او به ایران‌وایر گفت: «مجتبی چند سال در کنار دایی‌اش، روح‌الله نصیری، از ورزشکاران نام‌آشنای خراسان رضوی، به‌صورت تجربی و آکادمیک آموزش دید و با تلاش و پشتکار توانست به‌عنوان مربی و داور رسمی پاورلیفتینگ، با مدرک معتبر، فعالیت حرفه‌ای خود را آغاز کند.»
او از هواداران تیم پرسپولیس بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/76772" target="_blank">📅 16:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76771">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2c3ad4afb.mp4?token=In2HN8igfbNVuTljxJUN_3qFUUzv6ajZMrL39bKFWe52jM3Ed3koS58ById9RbqY4V2lv_v7LKrVHfNOaJ4opA1mSS9VyEKQ0-Z1LCG6T-USPxNtM1jzzda_V1E5uIu-m3ytInVtTxX3egb-Ih0w5cavNgyqGWqnPag-rJixeCiDWi6bUckJymZAQFOrC-LCz4S6Ag7d7uEJP6I4R8pFY_LyWaiy2qbasOw-SbYQwC8onbRUc1KXFv0dLd5sjKIxUOwfiPa5uM2qxKDdG-hT9mZ1hg5PyFRfJM8yg1MqkvH5N_2b1WJ7RfmVf4KKXOqEZ9HRgxPpM4H0IW8eO00rww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2c3ad4afb.mp4?token=In2HN8igfbNVuTljxJUN_3qFUUzv6ajZMrL39bKFWe52jM3Ed3koS58ById9RbqY4V2lv_v7LKrVHfNOaJ4opA1mSS9VyEKQ0-Z1LCG6T-USPxNtM1jzzda_V1E5uIu-m3ytInVtTxX3egb-Ih0w5cavNgyqGWqnPag-rJixeCiDWi6bUckJymZAQFOrC-LCz4S6Ag7d7uEJP6I4R8pFY_LyWaiy2qbasOw-SbYQwC8onbRUc1KXFv0dLd5sjKIxUOwfiPa5uM2qxKDdG-hT9mZ1hg5PyFRfJM8yg1MqkvH5N_2b1WJ7RfmVf4KKXOqEZ9HRgxPpM4H0IW8eO00rww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی می‌گوید گزارش‌های منتشره دربارۀ موافقت با دسترسی بازرسان آژانس بین‌المللی انرژی اتمی به سایت‌های هسته‌ای آسیب‌دیده «کذب است».
محمد باقر قالیباف در گفت‌وگویی تلویزیونی، که بخش دوم آن، شامگاه چهارشنبه ۱۰ تیر از تلویزیون رسمی جمهوری اسلامی پخش شد، با اشاره به قانون مصوب مجلس و مصوبۀ شورای عالی امنیت ملی جمهوری اسلامی، تأکید کرد که بر اساس قانون، «به هیچ عنوان دسترسی به سایت‌هایی که بمباران شده و آسیب دیده‌اند، داده نمی‌شود».
به گفتۀ مذاکره‌کنندۀ ارشد جمهوری اسلامی تعیین سطح دسترسی‌ها بر عهدۀ شورای عالی امنیت ملی‌ است و فراتر از آن، «هیچ امتیازی داده نخواهد شد».
محمدباقر قالیباف گفت بر اساس مصوبۀ شورای عالی امنیت ملی،‌ دسترسی بازرسان آژانس در حال حاضر به دو مورد نیروگاه هسته‌ای بوشهر و رآکتور تهران محدود است و به سایت دیگری دسترسی ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76771" target="_blank">📅 16:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76769">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OBop2-HMRVtCPaH5h8YiJiOOPAnaHsQ1BPInWgKYBDN_jvxM5Mlydw3qUeckKiU3DFU6ao5y6qlNuCCRAThgWA0ceXXwNvMrsxbPRLk-kMJh_wCGWBXt5J_ZXgot-X9xmQssyn5Ap0LkeqIHsWIyBN-cufqxy0Hr841uSH14IVBOa3jPRWspMBfRAmJjLGmcrv9NcQ7cNDbRsQcSPHw8sH4lojRIkwgD-YZjTa9qawbuf1IOyJgz9dAUgvr-gi1fJ0n57WlPViq2q5DCrV85OU-_sGqibsPrq_FRd3-XFwg6SzGLz-DfCC4M9qY3RvZanN0e6SsFgCyR9FLYYBibnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S4D01dCr9veqQ-qecfGVyixXuEDvD98KsmCBfuAkS6FzbN9Pyg5B4LpqUJ8iOML8MHIdjXlTS_orAObZ4j1FwxD62nI-XYz5VS-l0MPdIONdX5x3cnHjlauUz03wr7wcsJgQ8vfTD_ieyh9rAggri9wjp6rZ6KfmK3F49__JgfCxmlrq2zehvGtfSQDiR0Crp4l4xScFsPrQ94cDucepmqjaF_RD_KZxfBKi6MmXIzSdLS8K-ObRRWB3klGj_j0uhT5A2MkzSeEWwTKknYEkOYrSmRgnFHaBPpC-KsMFcbbpgCpdYXFAOSDij_zgEaDz8LB4sUh31DOm456XtCo5sQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">منابع امنیتی عراق از وقوع یک حملۀ پهپادی به اردوگاه گروه‌های کرد مخالف جمهوری اسلامی در منطقۀ کوی‌سنجاق در شرق اربیل خبر می‌دهند.
هنوز جزئیاتی از این حادثه منتشر نشده، اما طی روزهای اخیر چند عضو سپاه پاسداران و نیروی انتظامی جمهوری اسلامی در استان‌های غربی ایران از جمله کردستان هدف حملاتی قرار گرفته و کشته یا زخمی شده بوده‌اند. یک گروه مسلح کرد هم مسئولیت برخی از این حملات را بر عهده گرفته بود.
مقام‌های امنیتی جمهوری اسلامی طی روزهای اخیر، بار دیگر از مقام‌های عراق و اقلیم کردستان خواسته بودند که به حضور گروه‌های کرد مسلح مخالف جمهوری اسلامی در خاک اقلیم کردستان پایان دهند.
سپاه پاسداران طی ماه‌های اخیر بارها با موشک و پهپاد به پایگاه‌های گروه‌های کرد در اقلیم کردستان و عمدتاً در اطراف اربیل حمله کرده است.
در همین حال خبرگزاری فارس به نقل از «منابع محلی» از وقوع چندین انفجار در اربیل و سلیمانیه، و از جمله هدف قرار گرفتن مقر «حزب آزادی» با موشک بالستیک خبر داده است.
@
VahidHeadline
درگیری‌های مسلحانه میان نیروهای سپاه پاسداران و گروه‌های مسلح مخالف جمهوری اسلامی در اطراف شهرهای سردشت و پیرانشهر، شامگاه چهارشنبه ۱۰ تیر و بامداد پنج‌شنبه ۱۱ تیر، ادامه یافت و به کشته شدن چندین نفر انجامید.
سازمان‌ حقوق بشری هانا اعلام کرد این درگیری‌ها در مناطق مرزی آذربایجان غربی رخ داده است.
رسانه‌های نزدیک به حزب دموکرات کردستان ایران نیز اعلام کردند در جریان درگیری عصر چهارشنبه در نزدیکی روستای «قزقاپان» در اطراف پیرانشهر، پنج عضو این حزب کشته شدند.
خبرگزاری فارس، نزدیک به سپاه پاسداران، بدون ارائه جزئیات اعلام کرد شش عضو حزب دموکرات کردستان ایران در این درگیری‌ها کشته شده‌اند.
کانال تلگرامی صابرین‌نیوز، نزدیک به نهادهای امنیتی جمهوری اسلامی، نیز مدعی شد در دو درگیری جداگانه، ۱۱ نفر از اعضای گروه‌های مسلح مخالف جمهوری اسلامی کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/76769" target="_blank">📅 16:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76768">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VLYpxDo2ZSbBIRclg5ZrmXliYjgnJLdQQ_SoJjlR4iBIBPccsdzRFa-JqIToCIU7Q64XL1voy6lbt54nMAZX7-OwRRVk3AD_CMLibXp4uWxgPsaFcKfWkd_1iqC8-D6z1AoZxLrFdM10aw-Q-LgclAwUwdNjUbhdsRX_0268WtmJ8f0GF2qsd8JiJbeaSasJXTPLRbUBvnuGnmdAn_AmjbO4LH_Dzx46L-oScf88AtOYolkn7f0_IOVr3OwEJpju3wctLou8wfAOjJBqdN8r9Sto9rhhGUm7J3eoQVetRM6P9yS51AgwqAlkxKQR-gBo3YzW9G3esFkU3Be1QWcQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت کرمانی، وکیل دادگستری، از بازداشت دوبارهٔ سپیده کاشانی و هومن جوکار، دو فعال محیط زیست که پیشتر سال‌ها در زندان بودند، خبر داد.
آقای کرمانی به وب‌سایت «امتداد» گفت مأموران امنیتی عصر روز چهارشنبه دهم تیرماه با حضور در منزل این زوج، ضمن ضبط تمام وسایل الکترونیکی، آن‌ها را بازداشت کردند.
به گفته این وکیل دادگستری، نیروهای امنیتی همچنین سیما کاشانی، خواهر سپیده کاشانی را نیز بازداشت کرده‌اند.
او افزود تاکنون مشخص نیست این افراد توسط کدام نهاد امنیتی بازداشت شده‌اند و با توجه به تعطیلات پیش‌رو و بسته بودن مراکز قضایی، نگرانی خانواده‌های آن‌ها افزایش یافته است.
از دلایل بازداشت این زوج گزارشی منتشر نشده است.
سپیده کاشانی و هومن جوکار از اعضای مؤسسه «حیات وحش پارسیان» هستند که به همراه چند فعال دیگر محیط زیست زمستان سال ۱۳۹۶ توسط اطلاعات سپاه بازداشت شدند.
کاووس سیدامامی از بازداشت شدگان این پرونده که تابعیت کانادا را هم داشت، چند روز پس از بازداشت، به طرزی مشکوک در زندان اوین جان خود را از دست داد و مدتی بعد سازمان اطلاعات سپاه پاسداران دیگر فعالان محیط زیست بازداشت شده را به «جاسوسی» و «همکاری با دول متخاصم» متهم کرد.
سپیده کاشانی در طی سال‌های زندان در نامه‌هایی اعلام کرد که در دوره بازداشت تحت «شدیدترین شکنجه‌های روحی و روانی، تهدید به شکنجه فیزیکی و تهدیدهای جنسی» و «تهدید به مرگ» قرار گرفته‌اند.
او در نامه خود نوشته بود که بازجویان این پرونده «ویدئوی جسد» کاووس سید امامی را برای شکنجه به او نشان داده‌اند، و همسرش، هومن جوکار، را برای تهدید و شکنجه به پای چوبه دار ساختگی بردند.
سپیده کاشانی و هومن جوکار پس از سال‌ها زندان، در فروردین ۱۴۰۳ در پی عفو از زندان آزاد شده بودند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/76768" target="_blank">📅 16:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76767">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cccd78df1b.mp4?token=uy85jK9RRzmmZjyk-bLEg4U0wo5TT4okxbqWvOanIuP3clhMwNu74nydGp8MA1DfrRsRgsCidjCQruRKoFbuyfCZutT4xhvE-O5kZy5XF2Qxx37OOwxT0Lb4yFEjyHX8CMHAk72HWyyiCfdKkyY3bEzq2VDa5FDITlnfbYRvyonYcLW3xYilDmSz4Iow4kMnj2mmg0NRDAGnPHFGiaWNHO60fXX97IQJB-Nluj0sjePh4nQveKjd2taF5HheNlfX2bWWea-GZsNNIW5BdfZ5ZEXRp7gCnauj0tJjmeLXjngVkKcTDT6nEWneBR_NL0_oIIsVuk5y2K-0i0DZ5Clh4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cccd78df1b.mp4?token=uy85jK9RRzmmZjyk-bLEg4U0wo5TT4okxbqWvOanIuP3clhMwNu74nydGp8MA1DfrRsRgsCidjCQruRKoFbuyfCZutT4xhvE-O5kZy5XF2Qxx37OOwxT0Lb4yFEjyHX8CMHAk72HWyyiCfdKkyY3bEzq2VDa5FDITlnfbYRvyonYcLW3xYilDmSz4Iow4kMnj2mmg0NRDAGnPHFGiaWNHO60fXX97IQJB-Nluj0sjePh4nQveKjd2taF5HheNlfX2bWWea-GZsNNIW5BdfZ5ZEXRp7gCnauj0tJjmeLXjngVkKcTDT6nEWneBR_NL0_oIIsVuk5y2K-0i0DZ5Clh4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامرضا نوری قزلجه،‌ ؛وزیر جهاد کشاورزی"، با تایید سخنان محمدباقر قالیباف دربارۀ خرید محصولات کشاورزی از شرکت‌های آمریکایی  در دوران ریاست‌جمهوری ابراهیم رئیسی گفت: برخی از قراردادهای کشاورزی از طریق منابع ارزی بلوکه شده ناشی از تحریم‌ها بود و آن‌ها نیز به شرکت‌های آمریکایی مجوز می‌دادند و از آن‌ها خرید می‌شد.
محمدباقر قالیباف شامگاه سه‌شنبه در یک گفت‌وگوی تلویزیونی به خرید محصولات کشاورزی از شرکت‌های آمریکایی در دولت ابراهیم رئیسی اشاره کرده بود. پخش سخنان مذاکره‌کننده ارشد جمهوری اسلامی در همین زمان از سوی تلویزیون حکومتی متوقف شد.
رئیس‌جمهور آمریکا روز دوشنبه اول تیرماه در گفت‌وگو با خبرنگاران در کاخ سفید در مورد آزادسازی دارایی‌های ایران که در تفاهمنامه جدید به آن اشاره شده، گفته بود:
پولی که آزاد می‌شود قرار است برای خرید مواد غذایی استفاده شود... آن هم صرفاً از طریق ایالات متحده و از کشاورزان ما.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76767" target="_blank">📅 18:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76765">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AOUc0-epupBYV0rMQh7_V2CbRYQShk92H0C2bWpCjVZyACmMXxcCzQEAS-5dmLsMOSholrY9UY_aIIG8mzgWJmD9GvzCuKkTYm3ltIpw1B_uqw280Ya3pPB1yC_Gz0FuB47evQ0I4_i6OJKEYEi3BS3A-dN7XF6wt6qQ3C1nqTAayazHZUDT7gy9oQ9VsXb6UslXxzlioZGvS85xOf1k_0j90E4FEEcTbODwp70J1H-aU2XNzm1rqfL9QfANz8bCWxxKOPAS0zGFrn5iIMp3FFn-AXn9Y8TynNH6SlgInDOnB4GCeJ708YjYtaPWXqdKRu2NMUn0fwz-jPPKsp9rPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SFV9Ufus6JAFESFkV7jZy8-Y4roYgPrk6V882umAqTgPiHZYv7Fo6oSK4vYsanKLrzNcj51np9Ztoni4uliS83qwGuapkQccbxVO2e0gt-o4sWm7nGx5v6jgvh8n57gr7mjE1iq7Tw0phJXx2Nqz6VlnTxJSK3H2fgeVOrPHxTnaiAzNTqzvtRl7XByqEB2c3ndVPysejnim3qNscUHfSO6fQ8P3pR-ca6oSQMDrUH-TvWA5SKi3JXGs-ujdS2Sl7M7U0W4iNhZyVddcl1Ex6L5COGkifbSQOsfJyX3jMjmQ7zXuEbRBd4v6PO5ie_-sVdz-yySXUcNuYoCpB_r5xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور آمریکا روز چهارشنبه ۱۰ تیرماه از روند مذاکرات ابراز رضایت کرد و گفت این روند «بسیار خوب» پیش می‌رود.
دونالد ترامپ که در واشینگتن با خبرنگاران صحبت می‌کرد، افزود که آمریکا چند روز پیش حملات شدیدی به ایران انجام داد، اما نشست‌های اخیر دو طرف در قطر به‌خوبی برگزار شده است.
او همچنین اعلام کرد: «روند خلع‌سلاح هسته‌ای ایران به‌خوبی در حال پیشرفت است».
ترامپ افزود: «آن‌ها نشست‌های بسیار خوبی داشته‌اند و باید ببینیم چه خواهد شد».
این اظهارنظر ساعاتی پس از آن بود که رسانه‌ها از برگزاری «مذاکرات فنی» غیرمستقیم ایران و آمریکا در روز چهارشنبه در دوحه، پایتخت قطر، خبر دادند.
این مذاکرات با میانجی‌گری پاکستان و قطر برای اجرای تفاهم‌نامهٔ اخیر میان ایران و آمریکا انجام می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76765" target="_blank">📅 17:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76763">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t3Q2GwWRcf9oTLFIBR5DVUKZHD1fvykvg5-KCLGut9acO8nqJKjdqild1sofY0RyktYwwB5wya4dO6bfyxSBk2mbs8F9nlSnU9homEtBhpaLKdP1DY3zDShZ2U4sjwkv8MHLWh97GSwvl2pxte9mlETR-jYXv7TGrYCLWwlIO-l9xgPQaeflInly5ToAzkOORPbWTkEEfW6ViVtCPnVdK9q_7GxXUqJ1mmGbALeHeWFQmrKNVHjoPhINkIoL-ZW8hGBnukv56AYlOmgvZTWESGQwolMBS_v3TM3QoOV6Tt_YoC-pUJQZVmbOwN2U1mZUseA2PDNn2YfZ1z8RL5uhCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EDVECcqf78FNZKo8BDwku4jDp8csosxieD2EzmtkBrmMxijCZr7VKCOV-aYVFY3aAll0-SxOufMx1MJf1UNOY6pZlUpuBzcK4AGtT4C09dqkRd7A3Q3SkHwyMTqbA61wCvrTBxNVVQkbbqdNzmtNnFWpCnJR4DY2MlnkM5UKegxHSFnM7tgtemQTQHILzCxCMMJKI4Yvd5U9MEJu1UbKF4FGrmlEX8YxD5qMHQQ1PC5D6edkxkWq6pIHznQctzkLneGeBMbJ5WPfn6LIVqsou184nDxhvG2ljIxXOmvLUv6DGAxALr8mxCDU31pyYjYnndTJ7RJY9MbrLEyA4ZK6Vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی که برای شرکت در نشست‌های مرتبط با اجرای تفاهم‌نامه ایران و آمریکا به دوحه سفر کرده است، اعلام کرد کارگروه‌های پیگیری اجرای تفاهم‌نامه و نیز مذاکره برای دستیابی به توافق نهایی تشکیل شده‌ اما هنوز مذاکرات در این قالب آغاز نشده است.
کاظم غریب‌آبادی بعدازظهر چهارشنبه دهم تیرماه، پس از دیدار با شیخ محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر خارجه قطر، به خبرنگاران گفت رایزنی‌ها برای تعیین زمان و محل آغاز مذاکرات از طریق میانجی‌‌ها ادامه دارد و در صورت فراهم شدن شرایط لازم، این گفت‌وگوها آغاز خواهد شد.
به گزارش خبرگزاری ایسنا، پس از این دیدار نیز نشست سه‌جانبهٔ مذاکره‌کنندگان ارشد ایران، قطر و پاکستان برای بررسی روند اجرای تفاهم‌نامه برگزار شد.
@
VahidHeadline
دیوان امیری قطر چهارشنبه در بیانیه‌ای اعلام کرد تمیم بن حمد آل ثانی، امیر قطر، در کاخ لوسیل با استیو ویتکاف و جرد کوشنر، فرستادگان آمریکا، دیدار کرد.
در این دیدار، آخرین تحولات منطقه، به‌ویژه روند مذاکرات میان آمریکا و جمهوری اسلامی در چارچوب یادداشت تفاهم دو طرف، و همچنین وضعیت لبنان بررسی شد. دو طرف بر اهمیت تثبیت آتش‌بس به‌گونه‌ای که وحدت، حاکمیت و ثبات لبنان حفظ شود، تاکید کردند.
در این بیانیه آمده است که امیر قطر بر ادامه تلاش‌های میانجی‌گرانه این کشور با مشارکت پاکستان و حمایت از همه مسیرهای گفت‌وگوهای ناشی از یادداشت تفاهم تا دستیابی به توافقی جامع و پایدار که امنیت منطقه و صلح بین‌المللی را تقویت کند، تاکید کرد.
دو فرستاده آمریکایی نیز از نقش قطر و پاکستان در پیشبرد مذاکرات و نزدیک کردن دیدگاه‌ها قدردانی کردند و بر تعهد آمریکا به ادامه روند مذاکرات و تلاش‌های دیپلماتیک برای دستیابی به توافقی جامع تاکید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/76763" target="_blank">📅 17:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76762">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/moaVea2if616G1l4APVMZisL8Qb24g11o0_48eR6ql-BxJErJajdrNWrSCZcl9ODS0iU0-W6FmYfQqKSdn6MVMPGlmjdGbI7HNEhzwoIQVnGFPIPTcH2OInxIpbDL_RMabG3ycIyZVQIKJ4-sMAbPh8uLigiHI0-WTYgpdSIShnJ9qS6c42-2bKPspC8nLI9CN2lg57WZtGi_a44gIdm-a2q10S4jbtk1Ns580G60oyN9bK4bVddOCtch4cv3yyTF1_o5is3nLA0zhUJjvhhC6oAsQC3LNbOZyywKaT0i_bl9Wq25T7z2YMtBXzLUp14KwH9NeslgxzQYT7ELq1LzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با ادامه برخوردهای قضایی و امنیتی با فعالان صنفی فرهنگیان، سه معلم  با احکام زندان و مجازات‌های تکمیلی روبه‌رو شدند و یک فعال صنفی دیگر نیز در استان فارس بازداشت شد.
بر اساس گزارش شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران، احمد علیزاده، معلم بازنشسته و فعال مدنی اهل آبدانان، از سوی دادگاه انقلاب ایلام به دو سال حبس تعزیری، یک سال ممنوعیت خروج از کشور، ابطال گذرنامه و یک‌هزار و ۸۰ ساعت خدمات عمومی رایگان محکوم شده است.
هم‌زمان، آزاده سالکی، معلم شاغل در شهرستان خواف و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، به پنج سال حبس محکوم شده است. بر اساس خبر منتشر شده، حکم اولیه او ۱۰ سال زندان بود که در مرحله تجدیدنظر به پنج سال کاهش یافت.
آزاده سالکی پس از بازداشت در دی‌ماه ۱۴۰۴، حدود یک ماه در بازداشت به سر برد و سپس با تودیع وثیقه سه میلیارد تومانی به‌طور موقت آزاد شد. گزارش‌ها همچنین حاکی است اجرای این حکم می‌تواند به اخراج او از آموزش و پرورش منجر شود.
این معلم پیش‌تر نیز در سال ۱۴۰۱، زمانی که در شهرستان تربت حیدریه مشغول تدریس بود، به دلیل فعالیت‌های صنفی و اظهاراتش در کلاس درس، به مدت یک ماه از کار تعلیق و سپس به شهرستان خواف منتقل شده بود.
همچنین جان‌محمد احمدی، معلم بازنشسته و رییس انجمن صنفی معلمان نورآباد ممسنی، روز سه‌شنبه ۹ تیرماه توسط نیروهای امنیتی بازداشت شد. تاکنون اطلاعاتی درباره محل نگهداری، نهاد بازداشت‌کننده یا اتهام‌های منتسب به او منتشر نشده است.
آریا نورانی، معلم رسمی آموزش و پرورش در شهرستان مانه خراسان شمالی، نیز در ارتباط با اعتراضات دی‌ماه ۱۴۰۴ به ۱۴ ماه حبس محکوم شد.
شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران با محکوم کردن این اقدامات، خواستار آزادی بازداشت‌شدگان، لغو احکام صادرشده و پایان دادن به برخوردهای قضایی و امنیتی با فعالان صنفی شده است.
در ماه‌های اخیر نیز روند برخورد با فعالان صنفی معلمان تشدید شده است. پیش‌تر شعبه سوم دادگاه انقلاب اهواز پنج فعال صنفی فرهنگی و کارگری خوزستان را به سه سال حبس تعلیقی و دو سال ممنوع‌الخروجی محکوم کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76762" target="_blank">📅 17:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76761">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bX4jvYNpr13tv1O9-4eCmfet33vVF-yr6CRD8wwnfqOBinghwExdRJdviN4cZEf_EtueoHOa0qVAF_FDAuUpFQAiYb2aY92Ad-QxBy5cqrjSjnF8OIm8xhuq4eSpCyqSYR9lBxhRhkfy3EDtNPWs4ImiEbIQ_xr0SnJgL2Q7V59DB7jxNzAukVU9lzhjsrHJKUa2HAlww6KvezygHYyoN77V8KUnFzF04XyHV7E-2ugYyn_DR9jF5oswynFMdEw6lPmLPecUVoLskC8v8p3cBOLPfASqKyATPfxCpjqTEIibe0ZKvg2Ib1-34LC13Zv2_w2vXcnJJYoprC9ggMu1bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس، معاون رییس‌جمهور آمریکا با انتقاد از منتقدان که خواهان حملات بیشتر به جمهوری اسلامی هستند، در یک برنامه تلویزیونی گفت: «دیدگاه آن‌ها این است که فقط بمب بریزید، باز هم بمب بریزید؛ اما واقعا نمی‌توانند توضیح دهند که هدف نهایی از این کار چیست.»
او افزود: «اما چیزی که رییس‌جمهور [ترامپ] می‌گوید این است حاضرم دستور حملات هوایی بدهم، و به‌وضوح هم نشان داده که در صورت لزوم این کار را انجام می‌دهد، اما فقط زمانی که این اقدام در راستای دستیابی به یک هدف مشخص باشد.»
او در بخش دیگری از اظهاراتش گفت: «یکی از چیزهایی که درباره ایرانی‌ها برایم هم جالب و هم آزاردهنده است این است که می‌گویند نه، هیچ گفت‌وگوی صلحی در جریان نیست، اما در همان حال مذاکرات فنی میان واشینگتن و تهران درباره توافق صلح در حال انجام است. این یک تاکتیک مذاکره یا شگرد ایرانی است که من آن را درک نمی‌کنم.»
@
VahidOOnLine
جی‌دی ونس، معاون اول رئیس‌جمهور آمریکا در مصاحبه‌ای با شبکه خبری فاکس گفته است «ایالات متحده در رابطه با ایران در موقعیت بسیار خوبی قرار دارد.»
او گفت: «ایرانی‌ها در هفته‌های گذشته، هیچ نفت‌کشی را هدف قرار ندادند و جریان نفت در تنگه هرمز برقرار است؛ بخشی از آن به این دلیل که رئیس‌جمهور(ترامپ) تصریح کرد که اگر ایرانی‌ها به کشتی‌ها حمله کنند ما مقابله به مثل می‌کنیم.»
آقای ونس همچنین گفت: «اگر مذاکرات موفقیت‌آمیز باشد که ما می‌خواهیم موفقیت‌آمیز باشد، شما ایرانی را خواهید دید که بطور دائمی متحول شده؛ تروریسم منطقه‌ای و بی‌ثباتی را تامین مالی نمی‌کند و جاه‌طلبی‌های هسته‌ای را بطور دائمی کنار می‌گذارد و درنتیجه اقتصاد جهانی دوباره از آن استقبال می‌کند. این نتیجه خوبی برای مردم آمریکا و کل منطقه است.»
او همچنین گفت:«از سوی دیگر اگر آنها رفتار مناسبی نداشته باشند و امتیازاتی را که ما می‌خواهیم ببینیم ندهند، هنوز برنامه هسته‌ای آنها نابود شده، توان متعارف نظامی نابود شده و آمریکا در مقایسه با آنها در وضعیت قوی‌تریست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76761" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76759">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/150c916f8f.mp4?token=AUSo5Nfu3-vuQVrctJnO07rgNwGrMQYzDOAlj6UsqmSEL2rJVd3k8zPdLqUJ2CQbMxcfQ-XgvlS_Fdt-O0OX8HgCrTsuO02Su2Rj5_JU8HGCL2_HaV7S0lM_QYRT2SReTvCxd94RBgL2If7NYLg-s_2STMBnYvyLrv0-dghH371HKz0HeUul0tMslpQMcZjeSp8j7f08ujinP6Keu6WGHvDnxd-fVDegQpOq4X7WZmdwAtiY4gTwIvAkJsdZUE2PWStjSOiD6d5ATorkLMIDMxrNAu1-mn_r08rXAXfSnVYrALJ0Eh7BY-tJ_WjSY4VRZnK8Ll29M5_i2e7lSkFkPA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/150c916f8f.mp4?token=AUSo5Nfu3-vuQVrctJnO07rgNwGrMQYzDOAlj6UsqmSEL2rJVd3k8zPdLqUJ2CQbMxcfQ-XgvlS_Fdt-O0OX8HgCrTsuO02Su2Rj5_JU8HGCL2_HaV7S0lM_QYRT2SReTvCxd94RBgL2If7NYLg-s_2STMBnYvyLrv0-dghH371HKz0HeUul0tMslpQMcZjeSp8j7f08ujinP6Keu6WGHvDnxd-fVDegQpOq4X7WZmdwAtiY4gTwIvAkJsdZUE2PWStjSOiD6d5ATorkLMIDMxrNAu1-mn_r08rXAXfSnVYrALJ0Eh7BY-tJ_WjSY4VRZnK8Ll29M5_i2e7lSkFkPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد جمهوری اسلامی، شامگاه سه‌شنبه اعلام کرد در حال حاضر «اصلا مذاکره‌ای با آمریکا نداریم».
او در گفت‌وگویی با تلویزیون حکومتی ایران محاصره دریایی آمریکا علیه بنادر ایران را که بعد از آتش‌بس و از فروردین‌ماه آغاز شد، «شدیدترین نوع جنگ» خواند که به گفته او «مردم و نان مردم» را محاصره کرده بود.
قالیباف افزود که برداشته شدن این محاصره «از موفقیت‌های بزرگ» تفاهم‌نامه امضا شده بین ایران و آمریکا بود.
او اعلام کرد که مذاکرات فقط تا زمان امضای یادداشت تفاهم ادامه داشت و سفر به سوئیس برای گفت‌وگو درباره «اجرای بندهای» همین تفاهم‌نامه بود که ۲۵ خرداد بین ایران و آمریکا امضا شد.
@
VahidHeadline
قالیباف با طرح ادعای تسلط ایران بر تنگه هرمز در پی جنگ ۴۰ روزه هشدار داد که «نباید تنگه را به ضد خودش تبدیل کنیم».
او افزود: «تنگه هرمز زمانی ارزشمند است که روز‌به‌روز تردد در آن بیشتر شود، نه کمتر.»
@
VahidHeadline
پس از  آن که مصاحبه تلویزیونی محمدباقر قالیباف درباره جنگ، تنگه هرمز و مذاکرات با آمریکا، در میانه آن به طور ناگهانی قطع شد، مرکز رسانه‌ای مجلس شورای اسلامی اطلاعیه‌ای به رسانه‌های داخل این کشور فرستاده و به این موضوع اعتراض کرده است.
در اطلاعیه مرکز رسانه‌ای مجلس آمده است: «به اطلاع هم‌وطنان عزیز می‌رساند در راستای اجرای امر رهبری معظم انقلاب مبنی بر پیگیری شروط مشخص شده در یادداشت تفاهم اسلام آباد، جناب آقای دکتر قالیباف، رئیس قوه مقننه و رئیس هیئت مذاکره‌کننده کشورمان برای ارائه گزارش به مردم، گفتگویی تبیینی را طبق هماهنگی با سازمان صداوسیما انجام دادند که این گفتگو بیش از ۲ ساعت قبل از زمان پخش به آن سازمان تحویل داده شد؛ اما متاسفانه پخش این گفتگو از میانه آن متوقف شد».
در ادامه این اطلاعیه امده است: «این در حالی است که این گفتگو به شکل ضبطی بوده و کمترین وظیفه مسئولین سازمان صداوسیما این بود که اگر خلاف رویه ها تصمیم به عدم پخش بخشی از گفتگو داشتند، آن را با این مرکز هماهنگ می کردند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76759" target="_blank">📅 00:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76758">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QG1EUhhW0Oyq2INEl6w6K6bOaKTtlAQb3Op0WpwHLrgXGew7vAamllWZqURTV4kp3cn9fwqFAglftCYtNkP1Ckq8OciOAFSP_JcYszev-j2xhZPNaLS2ro9CsnzpWlaieeQTW_dvq-t3qHFzI67gdTVh5orAlxvteRoPYGKXY_MVPkYdBAcLBIVqa5Wx--mEcjpgpQnCyeePaD33cPK2y4k7ccfzx84nPNzPAlJECVf4OAc1sjru3zRKfAsliBYYDPlkNKh3uJRU8plWotiuCXRuMnRElgaCY-z9_z1rIfY7iW_EZ_pc5nbeX61ojN-5DufjyDTEkchHYNdGeochzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌دیوان عالی آمریکا تلاش دونالد ترامپ، رئیس جمهور، برای لغو اعطای خودکار تابعیت به کودکانی که از والدین مهاجر فاقد مدارک قانونی در خاک آمریکا متولد می‌شوند را رد کرد.
آقای ترامپ و تیم حقوقی او تفسیری از قانون را درخصوص این اعطای تابعیت مطرح کرده بودند که تا همین اواخر هم در میان سیاست‌گذاران و کارشناسان حقوقی، حمایت چندانی نداشت وتوانستند آن را دیوان عالی آمریکا یعنی عالی‌ترین مرجع قضایی کشور برسانند.
با این حال، در نهایت اکثریت ۹ قاضی دیوان عالی حاضر نشدند سابقه قضایی ۱۵۰ ساله را کنار بگذارند و یا قوانین فدرال دیرینه و متن قانون اساسی آمریکا را به گونه‌ای جدید تفسیر کنند تا به نفع آقای ترامپ رأی صادر شود.
این شکست احتمالا برای آقای ترامپ ناامیدکننده خواهد بود و او را وادار می‌کند به دنبال راه‌های دیگری برای محدود کردن ورود مهاجران فاقد مدارک قانونی به آمریکا باشد؛ زیرا اگر این افراد هرگز به خاک آمریکا نرسند، موضوع اعطای تابعیت به فرزندانشان نیز اساسا مطرح نخواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76758" target="_blank">📅 21:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76757">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLGvm7gBheFoIFC35SeJeuzbwmMQ8b0WnRdRWP8rSlcicpu33VlCc51kMii5V-GIYx-ggOpiBI29GQ95JRsRjJLKq9TU6gnvKyBxn6Au9KKnnDcAXbMT1PLZbQ4oMvMCU6Fq3UMtiSH-HhOwHpi-wWYgKY0dW95NAh_hwV0tcYoHKDIPv7eYFbP1Ta0lDp6Nc2bJZL5YE_AORhMNl4AwohxQU96iFY8p9UY3cfuHYpEzgMMG0pgtj7IUHG7KZdDi2QsrR-mMkQQtbO4BrO3jtc6K1wLX3o6xyV4YGJwlyqMV-Hk1q5vXFJCvt00UJ7vRQASK2Dozcemv8jEyoGjmkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه قطر، اعلام کرد استیو ویتکاف، فرستاده ویژه دونالد ترامپ در امور خاورمیانه، و جرد کوشنر، مشاور ارشد و داماد رییس‌جمهور آمریکا، روز سه‌شنبه برای گفت‌وگو با مقام‌ها و میانجی‌های قطری وارد دوحه شده‌اند.
ماجد الانصاری، سخنگوی وزارت خارجه قطر، گفت این دیدارها با هدف بررسی «تمامی مسائل منطقه‌ای» انجام می‌شود و موضوعاتی از جمله روند مذاکرات با ایران و همچنین لبنان را در بر می‌گیرد.
او با این حال تاکید کرد که ویتکاف و کوشنر برای مذاکره با هیات ایرانی به دوحه سفر نکرده‌اند و برنامه‌ای برای دیدار با نمایندگان تهران ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76757" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76756">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnUlWvcvfc9eM2KkOD5nxk3mAdBdSRBHw3pRvSSh6EPTvqbnvHwM6ol03dJhkg2ms4TpRiZPffGJ5znVhKN5ILAHXxynqU7mBElPU6TUeDpSfLqjXxWQPtDKFDW94t4BVIAeAYDw_G6luIBnY61tp76_Wd4VurfY8rUJAPQJvT-7cUZlAI2mppGWAQWRh5yQO9OxaneKOx2dyFBuRxxVdz_FINfNWlhX6ds4vVZvjLU1Z5oWZU8X4gDaQ8K7yNsCK6y9zgVr8ztr-oKEEjMcUWMpvoBuEJtKAPXHnK7EtuZMiFZLVoLIyJFTrG_v4A8NNtRaYCO0vK5H9DvTjBcn_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه به نقل از چند منبع گزارش داد جمهوری اسلامی تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدودشده خود را دریافت خواهد کرد.
پیش‌تر سخنگوی وزارت خارجه قطر گفت تاکنون ۶ میلیارد دلار از دارایی‌های مسدودشده جمهوری اسلامی به ایران منتقل نشده است.
محمدجعفر قائم‌پناه، معاون اجرایی مسعود پزشکیان، نیز با اشاره به متن تفاهم‌نامه با آمریکا، گفت که چند میلیارد دلار به حساب جمهوری اسلامی در یکی از کشورهای خلیج فارس نشسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/76756" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76754">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K1sUs4kSl4UtTie1wLon6MRV0is1BJJ2ic4_9DRMgOj4E2XcOYR3JDv-Ddyr6Xtsa9HNDqEqXvkKFYj-S4kr6ymWtNuvAQrBtV8zOagUeIR4JzbAPihSXxn3CjstWbebXS2lZMYHIQwNHpKjpwtrlu7kllta4SCqiPpr5oAuS24vDDlmkbsRxoLWnvfwhu7ARGPsle6iqEleEzbFzf0WRrpjcOhdeO495XbKyXf8HfpyuD4AOsUXLkfDXA0EpmEz-ezUsGlK1ge1qMY5523qdbcUnuhrfoM1uarLeGFX6Cz3CTgiwWO5ZFa-CC1_CAI4gdFu74B1BKH2jbN3ZIFcEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Urq14R1BcU43RsQr2GpzEFIE4mhjVz4p4VAkgjtK6z57_PNyWvk72rAMiStOCOHBFTT7A1NNc6qux_jgzyyCvPKv_XskWYesT-SO--VPfavJMVmHc4O67ufgYeAaUHXqZkZ8u-KISIpe2oK9-dxEudRzMSfvK85wZYIs6vIBMyujk9pWJ_Ugq2HaFHsLSj2eqmnN82yaV6reDY9wjfBQ37xN6CkAJbAAuiebtJyjXucixAieFPQ4ylrpA6K1j5nPEt3Zj6PVlby7w6PaoiIaiBx28JYtJBCylg9CbJkR8XSVVfIf97HYyUJ7XdGwd4R8yX4zrUyKnXJkjrHJrzfXIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون اجرایی مسعود پزشکیان تأیید کرد که فرماندهان نظامی عضو شورای عالی امنیت ملی ایران و دو نمایندهٔ رهبر جمهوری اسلامی در این شورا نیز به تفاهم‌نامهٔ ایران و آمریکا رأی مثبت داده‌اند.
محمدجعفر قائم‌پناه روز سه‌شنبه نهم تیرماه اعلام کرد در جلسهٔ‌ شعام برای بررسی این تفاهم‌نامه، رئیس‌جمهور، رؤسای مجلس و قوه قضائیه، جانشین رئیس ستاد کل نیروهای مسلح، وزیر کشور، رئیس سازمان برنامه و بودجه، وزیر خارجه، فرمانده کل سپاه پاسداران، فرمانده ارتش، و دو نماینده رهبر جمهوری اسلامی در شورا،
یعنی سعید جلیلی و محمدباقر ذوالقدر، به این توافق رأی مثبت دادند.
او این را هم تأیید کرد که مجتبی خامنه‌ای، رهبر جمهوری اسلامی، دستور داده بود جلسهٔ شورای عالی امنیت ملی با حضور فرماندهان ارشد نظامی برگزار شود و در صورت رأی موافق سه‌چهارم اعضا تفاهم‌نامه پذیرفته شود.
اظهارات معاون اجرایی رئیس‌جمهور در حالی مطرح می‌شود که در روزهای گذشته، پس از انتشار پیام مکتوب مجتبی خامنه‌ای دربارهٔ تفاهم‌نامه، برخی چهره‌های مخالف مذاکرات از سعید جلیلی به‌عنوان «تنها مخالف» تفاهم‌نامه نام برده بودند.
@
VahidHeadline
به گفته معاون اجرایی رییس‌جمهوری، اعضای موافق این تفاهم عبارت بودند از: مسعود پزشکیان، رییس‌جمهوری، محمدباقر قالیباف، رییس مجلس، غلامحسین محسنی اژه‌ای، رییس قوه قضاییه، رییس ستاد کل نیروهای مسلح (که نام او پس از کشته شدن عبدالرحیم موسوی هنوز به‌طور رسمی اعلام نشده است)، اسکندر مومنی، وزیر کشور، حمید پورمحمدی، رییس سازمان برنامه و بودجه، عباس عراقچی، وزیر امور خارجه، فرمانده کل سپاه پاسداران (که نام او نیز تاکنون به‌طور رسمی اعلام نشده)، امیر حاتمی، فرمانده کل ارتش و دو نماینده رهبر جمهوری اسلامی در شورای عالی امنیت ملی.
قائم‌پناه همچنین از منتقدان داخلی تفاهم‌نامه انتقاد کرد و گفت کسانی که به این توافق رای مثبت داده‌اند، «کمتر از فرماندهان شهید نیستند» و نباید جایگاه یا صلاحیت آنان زیر سؤال برود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76754" target="_blank">📅 16:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76753">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2bjgb3WCPgP6x9J2cDyfwfZ7_mZsJ2S8E5qt4gxcuou2WxT0Ut4X_bdJz_vJpL5nM5BQ-Lhiwab4tV2kFyl0UW5TEgLDEQh1Y_B6IxD46J_5c5jGzZ4Pjy4J_ABH2iKgID0UTGqAXIgpAbLr8Uky0Nxuj0i1vTqMPsaHSA5QPECqe6l8Xi3yDsRNozQ0agMJqA-3lBwhDEurPvpT-A2tc7GYl_v5at84NZ9pZgMfdLSg6-QKtvme70Ja8ePS3Un2Fd9KdykaFDNQ_h6eSiHQCtm7y7NisRpLwOKQrn8Qh4mKP-vXEIXe0LnDzpE8mKAgu3lPE4za6OJOLODRu_Aew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این تصویر، محمدرضا شاه پهلوی در جریان بازدید از بانک ملی ایران، با یوسف خوش‌کیش، رئیس وقت بانک ملی، گفت‌وگو می‌کند.
خوش‌کیش بعدها ریاست بانک مرکزی ایران را عهده‌دار شد و آخرین رئیس‌کل بانک مرکزی پیش از انقلاب ۱۳۵۷ بود.
پس از انقلاب، خوش کیش بازداشت شد و تنها طی سه روز محاکمه، با اتهاماتی از جمله «ثابت نگه داشتن ارزش ریال در برابر دلار آمریکا به مدت پنج سال»، به اعدام محکوم شد و بامداد ۲۴ مرداد ۱۳۵۹ تیرباران گردید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76753" target="_blank">📅 16:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76752">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JC9KyjTCIEdgkErzPfzGEkhrVzCxaz6ZGo3Ma5vZl04SOpNqlmboOi9xId5_T4Tpeq7uqJ879pLeP_QEpN5IoAcnQ00wtKMwhxmmGyBr1sFUR4m7e7P2uO5Z_5Zt3J7Y4Zscl30dhVJmsQVCxiXHXa9fFEg57pDtYjMsupX_A9HEH5cG-ZPzHWhlpu_0eu_lSb1Cdtv39HB2N3SU29u2KV54OWKvfMoN0MlQAyMC4gRMw2ntx0V7XXc5IVdjG2KIRSf3tYJXI2H1RlLZeN7rvAAaYqNu6iyTN8UfnQam_70sYeGU___dXDtDJEUWdFuui9bp3gWUDfFN2MJXduTVaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان مخالفان داخلی تفاهم‌نامهٔ ایران و آمریکا را به «همسویی با عملیات رسانه‌های معاند» متهم کرد و گفت «تمامی مراحل مذاکرات» با «هماهنگی کامل و مستمر» با رهبر جمهوری اسلامی انجام شده است.
رئیس‌جمهور ایران که روز سه‌شنبه ۹ تیر در دیدار با اعضای جامعه مدرسین حوزه علمیه قم همچنین گفت: «با وجود محدودیت‌ها و ملاحظات امنیتی موجود، متن نهایی توافق پس از بررسی‌های کارشناسی و امنیتی در مراجع ذی‌صلاح مورد ارزیابی قرار گرفت و در شورای عالی امنیت ملی نیز از حمایت قاطع اعضا برخوردار شد.»
این در حالی است که در روزهای اخیر مخالفت برخی طیف‌های سیاسی طرفدار حکومت با تفاهم‌نامه بالا گرفته و می‌گویند دولت، محمدباقر قالیباف، رئیس هیئت مذاکره‌کنندگان، و حتی برخی فرماندهان ارشد سپاه برخلاف نظر مجتبی خامنه‌ای این تفاهم‌نامه را تصویب کرده و پیش برده‌اند.
مسعود پزشکیان این دسته از مخالفان «جریان‌های همسو با عملیات روانی رسانه‌ّای معاند» خواند و گفت: «این‌ها تلاش می‌کنند با تخریب تیم مذاکره‌کننده و زیر سؤال بردن تصمیمات ملی، زمینهٔ تضعیف این دستاورد را فراهم کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/76752" target="_blank">📅 16:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76751">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpfVj8MMtfQYg_zUS9_YftOkb8EZCkBPxi_Dfo5dmnVo4k_AZliI77gTx1XwkLW2bUpTh5AvDJWUJkdCLncEfpZL4xgyRfR9hmngzCuVXKCW0CdVKbR-jvCTWOOfmBkg9LRnbxCsR6AX-1ZhbEiSEBup1enAZF3b9LIK-pYUiaEzHGh58J-v3rvEJshzFrhSDN_8tHyv5mnybjlaZKEvEUd-OzFJK3nYt6Rgh0hfH-4VeTOttyg-qqAGm_VTl70MAO5hqRQFjg2mB9LVF5gFO-Ou9krb1gmWa6r3_EfEgPCCmUKIckTNthH4HjgN7WCwFVW0F-IA3RSszbNs-f_QCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۴ روز از آغاز اختلال در شبکه خدمات برخی از بانک‌های کشور از جمله بانک‌های صادرات، تجارت، ملی و توسعه صادرات می‌گذرد؛ اختلالی که همچنان به‌طور کامل برطرف نشده و ارائه خدمات بانکی را با مشکل مواجه کرده است.
در این مدت، گزارش‌های مردمی از تداوم کندی، قطعی و ناپایداری سامانه‌های بانکی حکایت دارد؛ این در حالی است که مسئولان بانکی در روزهای گذشته بارها از رفع یا در آستانه رفع بودن مشکل خبر داده بودند.
ادامه این وضعیت موجب بروز اختلال در انجام تراکنش‌های روزمره از جمله انتقال وجه، دریافت حقوق و پرداخت اقساط برای بسیاری از شهروندان شده است.
هم‌زمان، کسب‌وکارهای خرد و متوسط نیز با مشکلاتی در دریافت مطالبات و انجام پرداخت‌ها مواجه شده‌اند؛ موضوعی که به گفته فعالان اقتصادی، بر روند فعالیت روزانه آن‌ها تأثیر گذاشته است.
در همین ارتباط، محمدرضا عارف، معاون اول رییس جمهوری، در جلسه‌ای با مدیران بانکی با اشاره به اختلال‌های اخیر گفت: «آنچه در بانک‌ها رخ داد نتیجه سهل‌انگاری در حوزه امنیت سایبری است و این موضوع قابل پیش‌بینی بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/76751" target="_blank">📅 16:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76750">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rhnSAsaYGsp8cKoWT6Is340AcApEWJMku49UUlm8CCgpyN2XBWim9RPpSflJPGnRTsv2Un_sOk9F-gdLbgpLoxHR--rg-K1FSFI4HyousBDAbyKTCaL_BCA5rYdv_nkgdGQlJ7Fu3ZCPZ8BogejCz6kyQPsdC3IQpwSFHB_4YQ_DkXP2sKKCBgA-IVcrTyeUhZFEBQLsY_Tf6dIUaLcWDdV3aRn_UkTjUR9mKZkLR58fz3yRMKUI-sabR91yu2dLMmb1AgqlxFrbxt4gPTgn33A-HxvVfQZ12IsNYErVNSLVH8IJ5vjUIxGPh0_bGujBpjFbf4bKbup-p_VujP92xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضوانه احمدخان‌بیگی، فعال مدنی، جهت تحمل ادامه دوران محکومیت حبس، به همراه فرزند خردسال خود راهی زندان اوین شد.
براساس اطلاعات دریافتی هرانا، رضوانه احمدخان‌ بیگی، دوشنبه ۸ تیرماه، به همراه دختر خردسالش، مهفر لاله‌زاری که زیر دو سال سن دارد، برای تحمل ادامه دوران محکومیت حبس خود راهی زندان اوین شد.
این زندانی سیاسی در تاریخ ۲۸ شهریور ۱۴۰۳ جهت زایمان از زندان اوین به مرخصی اعزام شده بود.
رضوانه احمدخان بیگی و همسرش بهفر لاله زاری در دی ماه ۱۴۰۲ به اتهام اجتماع و تبانی علیه امنیت داخلی و تبلیغ علیه نظام به ۱۰ سال زندان محکوم شدند. این حکم در اسفندماه همان سال تأیید شد و بعد از پذیرش اعاده دادرسی و رسیدگی در شعبه هم عرض به ۲۱ ماه حبس کاهش یافت.
hra_news
فرحناز نیکخو، نیره بهنود، میترا برمچ و زهرا (هانا) غلامی، چهار زندانی سیاسی، پس از پایان دوران مرخصی خود به زندان اوین بازگشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76750" target="_blank">📅 16:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76749">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hy_c81y5c7EaS833OnlEkFo1eAX-kafKv88G-INSuSE9c_byLvOpFDwYBmTPZYdV_leu85_Ku1RXJLw5az8i2xNVn6n3nDQMa4JpjW4cI2m4UNavIEPhCjqkVA7JWwNbZINt04y6cxw5xj1kXPJz9Qnu6lqMSuE2nR_uKf9BvkxCMnr5GcewV5I1eXohcsTPUvwW3gmLLkFTw5HcCcBxwm-hH5HdfIiHSctszg4_jMRXkYU0xEMYaAYdGXnQcGps5WHgNri_MrDWm_vNM5ywMkzgCsHEtT0jmiKMZrAidpGI8zQLmfNNAPSSCUFF8iV2Y2oRWjcp1UIEwMV2Mig63A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه استان کرمانشاه اعلام کرد دو تن از نیروهای بومی سپاه در شهرستان پاوه شامگاه دوشنبه در پی تیراندازی افراد مسلح «به درِ منزل‌هایشان» کشته و دو نفر دیگر زخمی شدند.
بر اساس گزارش خبرگزاری مهر به نقل از روابط عمومی سپاه استان کرمانشاه، این حمله مقابل منزل دو تن از نیروهای سپاه در پاوه رخ داده است. در این گزارش، عاملان حمله «افراد مسلح تروریست» معرفی شده‌اند.
منابع رسمی هویت دو عضو کشته‌شده سپاه را برهان کریسانی و خالد خالدی اعلام کرده‌اند.
همزمان، سازمان حقوق بشری هه‌نگاو گزارش داد که این حمله را گروهی تازه‌تأسیس به نام «خوری هیوا» (خورشید امید) بر عهده گرفته است. هه‌نگاو نیز نام دو کشته‌شده را خالد خالدی و برهان کریسانی اعلام کرده و نوشته است دو عضو دیگر سپاه در این حمله به‌شدت زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/76749" target="_blank">📅 08:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76748">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0vXiDRXLVcyg3cW47jynTSo-0b_aFFj1mLYZ__giehqiR6sAsknR88e6gFC1a4umpXKlyoxXCUZEYLUKEG6QK5uSVTGfxoTqj2zqZPtw3sCdRIJkGVoINwO-W8VwUFP0vtZOaIw7BxptCn7-zAFeUD8Dp2VagDNjyAPh4xGKirVekzu5oPVgAktpf_2MEjeHpvGXvsmeIqr5nnj3-AhhXS9l0_pTussZZjaWsl6-FsRSfe1omQL8Z3fuG8A1ETrAo-1wzv-bOHvzp1I0U3p668ss91o_hystH2-5o1UjrHqf7HKrsbBdJIU12a_0pmIMur79aRND9m3RJgND7afPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت امور خارجه جمهوری اسلامی، روز دوشنبه انجام مذاکره با آمریکا در دوحه را رد کرد و گفت در روزهای آینده هیچ مذاکره‌ای انجام نمی‌شود.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، از درخواست ایران برای انجام مذاکره در قطر در روز سه‌شنبه خبر داده و سخنگوی کاخ سفید اعلام کرده استیو ویتکاف و جرد کوشنر به عنوان نمایندگان ایالات متحده عازم قطر می‌شوند.
بقائی در این باره اعلام کرد: «طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و این‌که نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.»
او در ادامه توضیح داد «هیئت کارشناسی» جمهوری اسلامی این هفته برای پیگیری آزادشدن دارایی‌های مسدودشده ایران بر اساس بند ۱۱ تفاهم‌نامه امضا شده میان ایران و آمریکا به قطر می‌‌رود.
ساعاتی پیش مسعود پزشکیان اعلام کرد که «شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76748" target="_blank">📅 21:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76747">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D7LS12BVJXythDzQho7DrAlyIDokJkohIjbbrUrLR5AQzc_iChgGcaGfUNUj5yc707mb0fAtlJG9U_mLdLL05N1jw1JJdZg9ZJyGh-bfxN25TD7LSy4STgIRmner5WakJNIg-SKt3ewWchLVRLVZbqRNKSyGsXWjEV4L-A5Eqk7Q4pjqbjUCX3C8Bs0D0n8rM_xLdorrqfpCTqHDXgBRjFCyTGg8IfC3wawac2VISoEfBNQ6xiY6kA7boxPYuiQ9RdOtjBcccmHUgIHKvvGwC21rH0o0feC41hcha1HL-87P2Htu8rv-79prcnz2zxrF8zA98XQfMuKG43xT4dJNUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، گزارش داد محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه پاسداران، در یک «سانحه رانندگی بر اثر واژگونی خودرو» در یکی از محورهای استان کرمان کشته شد.
فارس نوشت پس از وقوع حادثه، نیروهای پلیس و اورژانس در محل حاضر شدند و اکبرزاده به مرکز درمانی منتقل شد، اما به دلیل شدت جراحات جان باخت.
این رسانه وابسته به سپاه افزود بررسی علت و جزئیات این سانحه از سوی مراجع ذی‌ربط آغاز شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/76747" target="_blank">📅 21:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76746">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1rwe61t00TynH5Gp1LG1O8jnOFeHkPtRKGEvmfRKiKfZCNqrzzqA3NTT0j7HlwlXuD-rHxTKUsZvHz-61_XD8zz-qkkqkrFrv7JVP2KIQClR9BJ9Si9IYTw57gbhbP_k2NVM8FZWW5dYPdvc4kiNX6j7jF5OjYc7mVIHYQTqSG94zrO-vYnNLmB7T0jW4bWDviDruErtOYcsUVyfwtuKl-eqd70GQCkfDpCLmFyweetBxkBCCAShaLN7CE79lKPqIQSJ6rutQI-NjL0Pfv4q-azb96I40xolEC2jT5dCesIDEjAcrw0wfEMWx056bhF-gV5iaZweaLKyyB16XYBjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف میری، ۱۷ ساله شب چهارشنبه سوری در خیابان حافظ اصفهان با اصابت گلوله بسیج به سرش کشته شد.
یوسف میری سه‌شنبه ۲۶ اسفند ۱۴۰۴ هنگامی که در راه بازگشت به خانه بود با مادرش تماس گرفت تا برایش غذا گرم کند اما پیش از آن که به خانه برسد با شلیک گلوله به پشت سرش کشته شد.
یکی از دوستان یوسف به ایران‌وایر می‌گوید: به مادرش گفتند به اشتباه به پسرت شلیک شده و اگر جنازه‌اش را می‌خواهی بهتر است سکوت کنی تا جنازه را تحویل بدهیم.
دوست یوسف همچنین توضیح می‌دهد: مادرش مرتب یک جمله را تکرار می‌کند که بچه‌ام گرسنه و تشنه بود می‌خواست بیاید خانه شام بخورد ولی آن بی‌رحم‌ها نگذاشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76746" target="_blank">📅 17:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76745">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qs3G237NMzosUSCQgDAxcl1In4CKrmKckfGX7PG7MTWiRk0jRIy3qmjZ3HOq55lvwx2VlvhgJLjqffA5D9Rbgz1Oqjo0odk6_Sd9vBy9bGfF_BmZDqAvbmRui-OvP0TuljEj4b1txTFAyM0eW9ujpLnlCoHQixNKnMyJfgpYMdiT-Uu1kM6jfoLnePFfKst1-BD7W864vRKJLtA3RbtN3bN10PnwGkNWVKrfeOLipBCuXfT4cScdkYwgnoI1RhbV3lO-HQnVY_rvrD0AIp74R6mlTG8YktonQQsw74F375H9C8dt0iVTYLDnwTSfhyP--mMdLm5r9XRxRd6vGgCQVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدر البوسعیدی، وزیر امور خارجه عمان، روز دوشنبه در گفتگو با رادیو مونته‌کارلو بین‌المللی اعلام کرد که این کشور به آزادی عبور و مرور در تنگه هرمز و اعمال نکردن هرگونه «عوارض تردد» متعهد است. او تاکید کرد که اعمال چنین هزینه‌هایی به‌طور بین‌المللی ممنوع است و عمان به این مقررات پایبند باقی می‌ماند.
این اظهارات در حالی مطرح می‌شود که ایران نیز از برگزاری جلساتی میان مقامات تهران و مسقط برای بحث در مورد مدیریت آینده این آبراه، طبق مفاد یادداشت تفاهم ایران و آمریکا خبر داده است. با این حال، گزارش‌ها حاکی از آن است که دو کشور تاکنون پیام‌های متناقضی در خصوص عوارض و مسیرهای تردد در این گذرگاه حیاتی ارسال کرده‌اند.
وزیر امور خارجه عمان همچنین تاکید کرد که مسئولیت اصلی تضمین امنیت تنگه هرمز و پاکسازی مسیرهای کشتیرانی بین‌المللی از هرگونه خطر مین‌گذاری، بر عهده جمهوری اسلامی ایران است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76745" target="_blank">📅 17:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76743">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gbkSLUtqCXF2Ii3bLNqagC5RotcYdosHvacZ8rXbvh7kOe71Q-bnmUAi6d_s1_p-8byxPVQlzR4q7ObcgYYItSrwzIxRFvVNbVZSxljny09k_fUMpiukQM7ztVRdB7M_bNIETqZHeUIoqTksyMLfsiZVf7BqtZCBOJjGCzwaTcJdNADf1CYy-EZTkb-BZVSAgbvVUikIb_k5EclECqudJqFvbJiqqIvt5DeORJHNH_sfxVGwpzJAU7B9EK1WjlTf5B6Sx5BcBI446M9KR5Hyv3sUTVVFowuuxwOJ45tTUOjD3yrgaVE1-7wGB5XDOz1Pb0Z3C3193J_cTs7VAW4JKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kZg5EAiIHMbXqm4B9h7NWvxa_anwfJJLVbb36gEj-nxTCFidEU304zm9g1k3-OvIgREMXet-FN_yv6hlC8KcpUQlKdZnwcsQPMbajMDxlYf2ozAnDY04B8pZbXVpApYgZdgRL3Jcp7Loyck9kIaT2mv1c5NWZuUSPEUPC65YP07NjsInMW-oGM5L2feP6KdG3qiUkC79HjuY6i5a6MJH0o65ObEUSiRVm6XSXegs8AX50Fz83xWxDFyL-PX31nfJi2dOM1PXcFMlJLqxVIjv0n-7izMYwSRtDk-KDMrFsQuLtC2-M2_7evT4_447cTu422WgYolcLjK2QnwVBdyXEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست عراقچی با فوتبال، ترجمه ماشین: از زمین فوتبال تا میز مذاکره و تا میدان نبرد، هر گامی که ما ایرانیان برمی‌داریم، بخشی از مبارزه‌ای بزرگ‌تر است: دفاع از شرافت و کرامت مردم عزیزمان. araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76743" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76741">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BnfccTCeKrQ3dBGwGopw7NQi7jOLs079MpBzitqUBW4HBjDm-Ulafcah4nKileWPQ4FBh0uMYjtPKl7A0E4l7wZiI1a5ycPMomNqiE9aPMICIe_r2GUIL2unSLHnbBgBSz2q5bNFtMhqs_VyvbNug-eksdmF3sQ_CPctTndEnBFv7IG5Eqcq9W8rvaDCraUUkTlsWVYDSPZ378oiO8EBYiwNdlKGcpRleYrLk862-pSahozFqpXxR2Y0RGriCEs5e4ZIZNjJuyqg67aRvjI4O-AcdUQEwNu5doQleoqH1gOoaYAU9c_xODuz1Tc5Qd8JTgRVpWMbmfhlfMdtiNYBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/m7p7s0fsZmVzfU57s6VYWH33O_msVyb5ak4bI4sLaMGYtMUQNZc2PoEImCy7pXuPw-HAkrvebcMQ6L3ZO4J8PvR7B-rN1HPAvmdO63gkpViJ_0qxBpOlye2Nf5xFVXiC7jdFlzEULx0wqJzk6WvXRRD4i_XxfN47wg-7mW_nThK3QidP00o9wuKmmRPEX7LHtfG8qZUE5MIXqOdYQjobvdziGptJz5p2G199Pz40FycrC_KpPpHq-fTPC__ZB7UHQPm42Rx0DI7K_sn5b0tTUoRZ2C6DWh2low9V-VuoXkJLGYdfj6mdzBQXylPeUhwG7uvyiYV8sfvRnZW_R_EPWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پستی نوشت: «ایران درخواست دیدار کرده است. (این دیدار) فردا در دوحه خواهد بود.»
پیشتر کاظم غریب‌آبادی، مسئول تیم فنی مذاکره‌کننده جمهوری اسلامی، گزارش برخی رسانه‌ها مبنی بر برنامه تهران و واشنگتن برای مذاکره در روز سه‌شنبه را تکذیب کرده بود.
کاظم غریب‌آبادی، مسئول تیم فنی مذاکره‌کننده ایران، امروز گفت: «هرچند رایزنی‌ها با قطر از جمله در خصوص پیگیری اجرای تعهدات طرف مقابل، طبق روال، در جریان است اما خبر برخی رسانه‌ها مبنی بر برگزاری گفتگوهای فنی کارگروه‌ها در دوحه تایید نمی‌شود.»
او در ادامه گفت که «اولین دور گفتگوهای فنی در چارچوب کارگروه‌های تعیین شده، با فراهم شدن شرایط و پس از توافق در خصوص تاریخ و محل آن، برگزار خواهد شد و رایزنی‌ها در این خصوص از طریق کشورهای میانجی ادامه دارد.»
@
VahidHeadline
«کارولین لیویت»، سخنگوی کاخ سفید اعلام کرد «استیو ویتکاف»، نماینده ویژه رییس‌جمهور آمریکا در امور خاورمیانه، و «جرد کوشنر»، مشاور ارشد پیشین کاخ سفید و مشاور غیررسمی «دونالد ترامپ» در امور خاورمیانه، روز سه‌شنبه در نشست دوحه با نمایندگان جمهوری اسلامی شرکت خواهند کرد.
@
VahidHeadline
ترامپ در پستی دیگر نوشت قیمت نفت خام وست‌تگزاس اینترمدیت به ۶۹ دلار رسیده و رو به کاهش است.
ترامپ در این پیام نوشت این قیمت از سطح پیش از آغاز «خلع سلاح هسته‌ای ایران» پایین‌تر آمده است.
@
VahidOOnLine
🔄
توییت خبرنگار اکسیوس:
به‌روزرسانی: یک مقام کاخ سفید می‌گوید فرستاده ویژه، ویتکاف، و جرد کوشنر امروز به دوحه سفر می‌کنند و روز سه‌شنبه با نخست‌وزیر قطر و دیگر مقام‌ها برای گفت‌وگو درباره توافق ایران دیدار خواهند کرد. روز چهارشنبه، تیم‌های فنی آمریکا و ایران به‌طور جداگانه با میانجی‌های قطری و پاکستانی دیدار خواهند کرد.
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76741" target="_blank">📅 16:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76740">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9Y13GuZR9yxuIzv2DqjXlfaMpMlOSYZDNxaYujDx7jABibG4uAmpgyGhRViJVgyKPnvgMYhebfJihKuscdFfNSUV4ADyssI2dAZSSg1OGjaztIZWUfEf0weBM3JGm8RPQZxRHUGwyDoV7afuJT3AEvTXIJkrr4MThQyH2nlQcpVfjA1FOxkmbi31Fb_ksXgq3qXprEp04-bUjSNHR2-jIpZ2wMk21MVaFzgoy3qiGbU0kVWTWgZHNui7aBoUKa594PpRzFiIfcnF_TMBp82HqQfx04eSi86MRnKAWzIv3nOXt_h8Lph8IAPQiOQg_nUO1Z-TQOaSFJvf1lspbGU_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری اسلامی ایران روز دوشنبه هشتم تیرماه گفت: «براساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد».
مسعود پزشکیان در دیدار با شبیری زنجانی از مراجع تقلید شیعیان در قم گفت: «برای بازگشت بخش باقی‌مانده این منابع نیز پیگیری‌های لازم در حال انجام است».
او زمان مشخصی را برای آزادسازی این رقم اعلام نکرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76740" target="_blank">📅 16:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76736">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5Zv2DG6WYRZlXveZhfYd6tSwvtP6UWCotnXcbMEcYbuG-X9YJULkdxDwfQu55MODtt0nZAowNpAC759hY5IX2QdhAMfrJ4JJLiS8Y6juN49ejhBgDID12g6uTNn0AtVmUDavB1BWkbz9AMP7l_hjr1qqM2ltbYxP_UfiR0JngfwP42ucZPJRyI7mCQqNQwMp_aPw7NZfjP0Q3X4QKTovK0LzdVT7CfqJtrX16-Ns56VHAkqmKX5GYtx7OP2u_pA-YLNyAhrCyTag6OfCu_0eZIH-RVdvn8_O00b7d9MVN0EtUCLHf9evCu26FxGGuqRqqVs6uEX3h4Pd6KSWePKaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gu0OqTRVa3AvjC3V62Vxy0Kw3ctpmbDVRuskq6_KR629m9YsK0ZQ8W64m7jOFku3__ngtaYu2UqlWe6MEcfPSCjTzQGfUvI6zGYadUC3Sp2-h-5jOS5KGugj4U2n4iCx3vluplscFwaUUkHogZhuQuQd7GM6Gm2E0I3uyxqSseNWwM6xvZmqto0v4Qlbp_cvQKw4lQih_Ve6lQnWBbYEqyBCEsG_ATYS8nXazPY_PLd4Ec1BSCymxDHUko51_BOFclg8QccOcoBjpa5wNyjfzGG7sqqYKd9iuF1ht6aDUj1lGa_LMZaPADj2CjstS0QLRQxWtG7vbeg5ZjjcrAb3pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPr_XWiHnjDkc85XIIehx8iYg7C4aF63jmXt0BdvFkFeuNn-MGaMzHh5C8T2HvL1pKMuMFKIzVxYBMKrNR6Onm3LzvRVqrNqeKdli-bIb-vUo9a0msFTCrp-6bSx3hJ-2pNDOcYs24PMqlN2N90mQhtyDSmsraWsnkacVoUmFPSo2zRdezB8tdmZVfYdqfWoBvDQ2pUB3NjMHtWTLpOwCm5EYh2OEBzpxdIK_Dvusk1dIaGZbJkCW0XCcTuw4sbwnLEFKNn0JCUlPA3Qw4U2TginnUqPPRlJx672uQfyxvfXtISxQQdTADhuWbfsfWdgJM2r3gJ0antqor_W9Ywbtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b61d44fd1.mp4?token=TAqWw0D0W3sNXKJDlFYdTSFpWWmx6vE8GqjRcXDWy-kElyzDaRdFQuyQAaGPo9RKoE75yvxUSfdoieTRq9ctPxcMK6Jg43XWI41ybMTfm9lpBRjL1FD_gq8XvWWQHBvUwy5ozA0m8p5bfmtZ_GBD6lnKx1Al9aEIEp9A1hH0w9NNavjXd1ezrj75OgVvuy6JzZ-67NnA0aPb6E0tKxgNihe9nkD4LAI2eQviAwT6uU9tlUur7JBTNXTSgPeiXljltxRRl9N8pZU5cwL62CCDlG0WSXbDj-HLaMRcB7skl3MygDxP-ZAjESXPQTNyJdk6c4AijZ6Xg6j3cnHRx_44noqND9ibAYYnQFqEWuIgY7kmdbrlpCfr_E4yZfr-P2GK-u3lwbsKorokuGBTagVAK7GLCFBtGaEUG1gIijF5ZgUJSgO7FPNDbI9t0siGdSu9z9ozwjEaGhkt6WnFHrH7cZY-AOecdzIdKclXyQaKaMdFtT1Bj-c02seJ4O2h-lRLERd6XsEqNrTUngDy03DQxIvqGyVM8Cygl4fsG6ClvtVOthh5i4cavUwyUhxsbw9FlO3rNCbNHPRGy_vKRntZyyKKigTP6Otwdvco8xv_EQYg3Di_3m66LH9biZIXbmKaR6zRJk25h5Xjja9FGuT0gj59ZCvsNR9a_tfZtureXnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b61d44fd1.mp4?token=TAqWw0D0W3sNXKJDlFYdTSFpWWmx6vE8GqjRcXDWy-kElyzDaRdFQuyQAaGPo9RKoE75yvxUSfdoieTRq9ctPxcMK6Jg43XWI41ybMTfm9lpBRjL1FD_gq8XvWWQHBvUwy5ozA0m8p5bfmtZ_GBD6lnKx1Al9aEIEp9A1hH0w9NNavjXd1ezrj75OgVvuy6JzZ-67NnA0aPb6E0tKxgNihe9nkD4LAI2eQviAwT6uU9tlUur7JBTNXTSgPeiXljltxRRl9N8pZU5cwL62CCDlG0WSXbDj-HLaMRcB7skl3MygDxP-ZAjESXPQTNyJdk6c4AijZ6Xg6j3cnHRx_44noqND9ibAYYnQFqEWuIgY7kmdbrlpCfr_E4yZfr-P2GK-u3lwbsKorokuGBTagVAK7GLCFBtGaEUG1gIijF5ZgUJSgO7FPNDbI9t0siGdSu9z9ozwjEaGhkt6WnFHrH7cZY-AOecdzIdKclXyQaKaMdFtT1Bj-c02seJ4O2h-lRLERd6XsEqNrTUngDy03DQxIvqGyVM8Cygl4fsG6ClvtVOthh5i4cavUwyUhxsbw9FlO3rNCbNHPRGy_vKRntZyyKKigTP6Otwdvco8xv_EQYg3Di_3m66LH9biZIXbmKaR6zRJk25h5Xjja9FGuT0gj59ZCvsNR9a_tfZtureXnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مبین یعقوب‌زاده یک سال بود که مادرش را از دست داده بود، زمانی که  تنها ۱۷ سال داشت، در ۱۷ دی ۱۴۰۴، در اعتراضات خشکبیجار رشت، با شلیک نیروهای امنیتی کشته شد.
🔸
سرگذشت کامل او را در یادبود امید بخوانید:
https://www.iranrights.org/fa/memorial/story/-9117/mobin-yaqubzadeh
@IranRights</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76736" target="_blank">📅 16:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76735">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ac12c0761.mp4?token=p3PxEur9RYVmBgNQsQY7ejZQhAfuQXxnfJKCVZ5TLN_Gryeb2DWfQnusuxCbYfx7Io_OLLKHbK9Gb1afP3vPLw57mbDZEGdMH8K13M2esLNahAobfFPM4IsWXF4tXWWG0yMOwz34uNbB7wKMD3vaV5xmz0isdxMO2j2zfBF-DM1TrX-GdePgLRnYyZWbaRU_xc6ckedw2SWrCJwBaCetwyxx09oQzvn-U2iTX3hjk5Gb0zwU8x48Dh089jSA-AhYz8rCRMOpxVmMYv2RufQQwUhCGtPKnzIcEJM8BzYeUySmkDWQMEW1MvFmRvM_J2Kf-_66i6R_Sawb7q3Jry_aAg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ac12c0761.mp4?token=p3PxEur9RYVmBgNQsQY7ejZQhAfuQXxnfJKCVZ5TLN_Gryeb2DWfQnusuxCbYfx7Io_OLLKHbK9Gb1afP3vPLw57mbDZEGdMH8K13M2esLNahAobfFPM4IsWXF4tXWWG0yMOwz34uNbB7wKMD3vaV5xmz0isdxMO2j2zfBF-DM1TrX-GdePgLRnYyZWbaRU_xc6ckedw2SWrCJwBaCetwyxx09oQzvn-U2iTX3hjk5Gb0zwU8x48Dh089jSA-AhYz8rCRMOpxVmMYv2RufQQwUhCGtPKnzIcEJM8BzYeUySmkDWQMEW1MvFmRvM_J2Kf-_66i6R_Sawb7q3Jry_aAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
صدای بلند)
ویدیوی دریافتی با شرح کلی: "جنوب کشور، جنگ اخیر"
انفجارهای مهیبی در یک اسکله رو نشون میده.
از زمان و مکانش اطلاعات بیشتری ندارم، لینک یک صفحه اینستاگرام رو فرستادند که نسخه اصلی این ویدیو رو دیروز بعد از ظهر بدون هیچ توضیحی منتشر کرده و پست دیگری هم نداره.
Vahid
آپدیت:
در پیام‌ها میگن خرمشهره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/76735" target="_blank">📅 04:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76734">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JuzBkztHIj6qvbzSBjRtAM8bVxlPejfZiX76iNpB8Ec1zfPszPSRP2G-twED8t0_pOLqLpMG6l1fbw_IsZuIFlHT6YufCnqaywupylBHabr45zloGMOBiJ3_RGVMMsTJmwFErCMkLsopdqUPGvj1Zu8j3TIIa0riF0mC7rUXAamJnDK1QmQFnacO0CF70OJKAu9WTVPah34XYNNIeKKFSPnb0n-9GXxzBam-NjCQEIYPNz6hi3Tg-1Q8BsD-BBfrIGg7F2gs1F00S_-1lQollA3aJxVvSllzCC2LwS9Em_lCYuNkSj5vmsFxZq8ez7Vvr2xJRf4fABijLxrzRBAKQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس در نخستین ساعت بامداد دوشنبه هشتم تیرماه به وقت تهران (عصر یکشنبه به وقت آمریکا) به نقل از یک مقام ارشد آمریکایی گزارش کرد که ایالات متحده و ایران موافقت کرده‌اند که حملات علیه یکدیگر را متوقف کنند.
براساس این گزارش دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر دیدار کنند تا به اختلافات خود در مورد تنگه هرمز رسیدگی کنند.
براساس گزارش باراک راوید یک مقام ارشد آمریکایی گفت: «ما تصمیم گرفتیم تمام فعالیت‌های «رزمی» (جنبشی/kinetic) را متوقف کنیم».
همزمان یک مقام دیگر آمریکایی هم به آکسیوس گفت که هر دو طرف «فعلا» عقب‌نشینی خواهند کرد و «شناورها می‌توانند آزادانه حرکت کنند» چرا که قرار است گفتگوهای فنی ادامه یابد.
هر دو مقام آمریکایی و یک منبع سوم آگاه، دیدار برنامه‌ریزی‌شده برای روز سه‌شنبه را تایید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/76734" target="_blank">📅 00:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76733">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P9RMYr2rGX5ejdL0puhYlBuXVoRxIv6SGylAblABUsybvLfZT5kRcwmyEMTH6hht9vLn769wvVqw3FFIj_eoEF5w2zvZXXaz9rBBgLtDj_5rz0YEpCdUeNMbSJm8xbd3Ggu6P4qWZv9sFqe59et5FkmMKenMQ9GVlWtlzYE_9_jgW1_d-KqgKSmwtZ7eRUd9boy0XNUwrtil8GgGN2Dys-gYMm-asCaQ9yzeloMJ97iexfP8t0518Wg7ZxEL1jo2LcKamEyss0O4_zw2RT9j3clzrgLtVb0wj8Fp71Dey1pVbcOmkLAwyVan6UCDzBmBdIy069Sv52LM0vha6MGx6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از آن که روز شنبه - ششم تیر - نزدیک به سه‌چهارم اعضای مجلس ۸۸ نفره خبرگان رهبری در ایران، در بیانیه‌ای شبیه «فتوا» خواستار گرفتن انتقام کشته شدن علی خامنه‌ای، رهبر پیشین جمهوری اسلامی از دونالد ترامپ،‌ رئیس‌جمهور آمریکا و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، شدند، دبیرخانه این مجلس روز یکشنبه - هفتم تیر - در اطلاعیه‌ای، این بیانیه را «نامرسوم» خواند و درباره آن توضیحاتی داد.
در بیانیه روز شنبه که ۶۳ عضو مجلس خبرگان آن را امضاء کرده‌اند، آمده بود که اگر «مسلمانان متدین» به این رهبران آمریکا و اسرائیل دسترسی پیدا کنند، کشتن آن‌ها «وظیفه شرعی» آنان است.
اما در اطلاعیه روز یکشنبه دبیرخانه مجلس خبرگان آمده که هیئت رئیسه این مجلس مفاد منتشرشده را «غیرمعمول و نامرسوم» توصیف کرده و اعلام کرده است که محتوای آن به بررسی و بحث بیشتر نیازمند است.
به نظر می‌رسد،‌ اطلاعیه دبیرخانه مجلس از اختلاف نظر و شکاف میان هیئت رئیسه و بخش مهمی از اعضای این مجلس حکایت دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/76733" target="_blank">📅 20:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76730">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t45Ym6_F48hQF63d4uJ698CKHxyaCSk-jSEZ5EwqmSw5qYmIOsSq6zR1aG3OuFQ5PdIJE2b7-2ZWC8NS94gE0Oqsg2oOrtC8uMwEcFEAi3nhjbm2lt5vzFjzxR6I8hOZ2F8N12KT0VyN9bNQ4QJHPCO7KzCdEVUBxki3XqGxDP6j_XLvesRIvXqAA4LJAsryAknwZUWZsEnM8u-_YzZCbw4dAaQ707cMSRpl48U1vdx4dRPq4lrRPbS4yx3c8cCq9nMPMnMmTIFRTw9t9DUKbEg05DOXpKy6VjeGj79vwM6Qn7ph-fgA8OlbjBLAowx_VlUhuuF8wMf4T4PtqiTLGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iJEW-QR6eHq0AiV62GxnfRWeO85KICIrvMp6vlSVk-w5u-98bcFDmWtsU92ElcvxJ3HUKDlmaPMJj8x2WDoM7D7tChqCd6rjuA4zrcxBol49yKae3UdPKlihiwZnGXr9CawpNZSTFBlD2e7Or8CfY0pUFcNxAbMBtPFzVsZFDlxMu4dxNBWQTGOAwy0lec8hTcHrBAw5VJMIX9NUbGNfv83leoo8eBE0T3Xhsa_kFARwzPtfzvJ_RY573SoShGWPjFLYkhU31B4ociJEOrTJSsRGMXB5nV73K2dwGzNftUPWDH9PysTq7pIwWiK9uL7WtmAWz0AIm2MqatXauFDQYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gQWEWzS9S5ate-F20p9zD5bbtOi2PsYoE2_ji6kViidKl4zxNrFZ0GIhHDmCFLcYuHPhUuZqgvZpsNEuFzfYofQaN9PODx6s4eXN9fAvXgQbHJMj-N6ap9ZEnGnYueudXUyrZZh6zPopwkL4E2aMobqU9Pe-sAS6GRF6CWhxguqN9pNlmq_MhjZy9yrSeJFpDLrSiL0Tkyfg7AJwdpM-MyffY_tOPY1GOGEr7km9NMT-RUCVBeFhE3n5H9eDnXrBaxU_88OPaYoqs6UlVYPnncC2MogNcDbqFTG_oKfzbQh4Mmlpen4oYNyKO92egZxzgk-UrIBZ2iWLIY1hYGHqTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بحرین گفت که یک ساختمان مسکونی در استان محرق هدف پهپاد ایران قرار گرفته است اما مجروح یا مصدومی گزارش نشده است.
تصاویری که دفتر رسانه‌ای پلیس بحرین منتشر کرده است خساراتی را به طبقه فوقانی یک مجتمع آپارتمانی نشان می‌دهد.
ایران بامداد یکشنبه اعلام کرد که به تلافی حملات آمریکا، پایگاه‌های آن کشور در بحرین و کویت را هدف قرار داده است.
بحرین و کویت این حملات را محکوم کردند.
بحرین همچنین خواستار جلسه فوری شورای امنیت برای پاسخگو کردن ایران شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76730" target="_blank">📅 19:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76729">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIqkY80y7GHFsS7BGpoCjO4G0VbO5uSKg9JJXvhw4JoPZSMXVRza7Xky_6z929NzBrBXQ19pbzk-8v3_dKJqFvhIqRRRKMLvmlDJNSH4Y2oyagwfwjw3RXOCu7mTwd9_NOIN7DgtfIczFcB13pQUw3LJGw9g08FDBASXP-gnDtiwnWSVguGx_OnEUyob8ckex6f9EWfpM4vG2iBf_T2N51H_SQXnPx0lDpX_w-RUFj5MF7z-FmTh1qt-8eznd56ux1tao9mztfSAtT-r1WpAEHGEgR6OARywWTOrCJuH2LKPKlDkT--W69UJqybudEfGgV4DuoNDHUomEnRKXGo5wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش قیمت دلار آمریکا و دیگر ارزهای خارجی در بازار آزاد روز یک‌شنبه، هفتم تیرماه، هم ادامه یافت.
روزنامه هم‌میهن خبر داد که قیمت دلار در بازار آزاد در روز یک‌شنبه به ۱۷۲ هزار تومان رسیده است.
این روزنامه قیمت یورو، واحد پول اتحادیه اروپا، را هم ۱۹۴ هزار و صد تومان ثبت کرد.
روز شنبه، ششم تیرماه، قیمت دلار آمریکا در بازار به ۱۶۶ هزار و ۷۰۰ تومان رسیده بود.
این افزایش قیمت بیش از پنج هزار تومانی در بازار دلار در حالی است که در پی امضای تفاهم‌نامه میان ایران و آمریکا، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان هم کاهش پیدا کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/76729" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76728">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDjZPTXQ1SJCrobaDsTsjeS-lTUIoQUGZOURl7zoTkIGdoZez_IiJsBX_TCmQ0x9IMNSuZT_GjP_Rtcb4WAwuCHX8QHpQ76la2bJdbcXKic8nTOUrXNqFYZHS_BUT47M64AH9dyhSKar463gEngL9itqnszWESzeb2LiX59n0UOkrJ9f_qo_9BEOHi_5fbDvDJfhROafmTQEBPOYGfUj0bbbdDL9Q2L9BteyGnQbqgQtBJrXUOmBj7cDmu7ddxE0pkVqqGV_BC-iKyi9j1oQMouULKDHOFSIYW7Zw1agqcxD61wc1f_ObuXFj0IxQitu4EZSt-fZI5V5mXXpjsorqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای، سومین رهبر [اعلام شده] جمهوری اسلامی، در پیامی مکتوب به مناسبت هفته قوه قضاییه، از دستگاه قضایی خواست پرونده‌های مربوط به آنچه «جنایات آمریکا و اسرائیل» در جنگ‌های سال‌های ۱۴۰۴ و ۱۴۰۵ خواند را با جدیت در محاکم داخلی و بین‌المللی پیگیری کند.
او در این پیام که به مناسبت سالگرد هفتم تیر و هفته قوه قضاییه منتشر شد از قوه قضاییه خواست رسیدگی به پرونده‌های مربوط به جنگ را تا صدور و اجرای احکام ادامه دهد و مدعی شد چنین روندی می‌تواند از تکرار این‌گونه اقدامات جلوگیری کند.
مجتبی خامنه‌ای از زمان [اعلام] انتصاب به مقام رهبری جمهوری اسلامی تاکنون در هیچ مراسم عمومی، سخنرانی یا برنامه رسمی حاضر نشده [و صدا و تصویری هم از اون منتشر نشده] است. سایر مقام‌های حکومت تاکنون توضیحی درباره این موضوع ارائه نکرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76728" target="_blank">📅 17:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76727">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dbba8d2b1d.mp4?token=qTSywAbkTreEn4iSfyrp49yhSvbBGkuynHC4WiHgMA63XcVtCFEDfHzOqyeNBQmXIygT0acfX9yV3abG2PrZ0oIn_oJPQuKTD7tmz8S8dDq6XuP3EHbmHzSGwdZyrWMlGiSwkWDU0Q7TVObdJQPwt28JKPE3RWClUKTUyXQDN3zwT4T2X-9jOXIQa0uenM13Fg744NnKs6JoBCfl-x8CmOhggS6BltIO_cU0k4QXsvKr5pqVZf2DxyAagY0PXvfMMriBUs0CqzqqILAKvFHAU7Zd-m_3g5OllJceH-umARnE-NhST7Pl0xrp1BqZkP7zMvE6XECYKWkn7NikEzlijA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dbba8d2b1d.mp4?token=qTSywAbkTreEn4iSfyrp49yhSvbBGkuynHC4WiHgMA63XcVtCFEDfHzOqyeNBQmXIygT0acfX9yV3abG2PrZ0oIn_oJPQuKTD7tmz8S8dDq6XuP3EHbmHzSGwdZyrWMlGiSwkWDU0Q7TVObdJQPwt28JKPE3RWClUKTUyXQDN3zwT4T2X-9jOXIQa0uenM13Fg744NnKs6JoBCfl-x8CmOhggS6BltIO_cU0k4QXsvKr5pqVZf2DxyAagY0PXvfMMriBUs0CqzqqILAKvFHAU7Zd-m_3g5OllJceH-umARnE-NhST7Pl0xrp1BqZkP7zMvE6XECYKWkn7NikEzlijA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یک‌شنبه هفتم تیر در کنار همتای عراقی خود به آمریکا هشدار داد که «ایجاد ترتیبات موازی» برای تنگه هرمز «صرفاً به پیچیدگی اوضاع، افزایش تنش‌ها و تأخیر در بازگشایی این آبراه حیاتی منجر خواهد شد».
در پی امضای تفاهم‌نامه میان تهران و واشینگتن، آمریکا هفته گذشته مسیر دوم را برای عبور کشتی‌ها از تنگه هرمز معرفی کرد، مسیری در نزدیکی سواحل عمان که از دسترس ایران به دور است و می‌تواند رقیبی برای انحضار ایران بر این آبراه باشد.
در واکنش به این اقدام آمریکا، سپاه در دو روز گذشته به دست‌کم دو کشتی حمله پهپادی کرده که بلافاصله پاسخ ارتش آمریکا را به دستور دونالد ترامپ به همراه داشته است.
در واکنش به این رخدادهای تازه در خلیج فارس،‌ عراقچی که برای دیدار با مقام‌های عالی‌رتبه عراق به بغداد سفر کرده روز یک‌شنبه در نشست خبری خود با فواد حسین، همتای عراقی‌اش، چنین گفت: «بر اساس این تفاهم‌نامه و پس از رفع موانع، تنگه هرمز ظرف مدت ۳۰ روز تحت مدیریت انحصاری ایران به ظرفیت پیش از جنگ باز خواهد گشت و مسئولیت اجرای این ترتیبات تنها بر عهده جمهوری اسلامی است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76727" target="_blank">📅 17:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76726">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0pjWBtTsPz2c1VUSEPTe2fauw7YwZiZrfgRuVewx4GBZsI7KTX8GU6ZQ_pfP8pur2pHJjmQlmtFWVlPSREXvc0KhVT6LvaxlwXIYr-cs9ZKgm7ctfWKY6pe9e5lE6ixG_JQdy7G-XV0TTo4Lw4r7ORwrWP4ljmSIxBciAC2HHe8tZGXPhiM0HqLgDDo9N0jURWm3g4EUXhm3glBXO9ExoljwXVEerVuDJAWWD0yra4Kwg_NbVuoUFm0DillQTtNtPGSdArMrcD29THOavm0vN_k92RJ_JdTBM2ZM5PH5eDq3srZYMNwFdo01dBPe6CNhTASGw2HTNAGfgjj1Ko_hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تقی چنگلوایی» فعال محیط‌زیست و داوطلب مردمی اهل بهبهان، در جریان مهار آتش‌سوزی گسترده در «کوه بدیل» زاگرس جان باخت.
تقی چنگلوایی هنگام مشارکت در عملیات مهار آتش‌سوزی، بر اثر شدت آتش و حرارت بالا و در پی انفجار دستگاه دمنده‌ای که به دلیل کمبود امکانات برای اطفای حریق از آن استفاده می‌شد دچار سوختگی شدید شد و جان خود را از دست داده است.
رییس اداره محیط زیست شهرستان بهبهان در گفت‌وگو با شرق نیز تایید کرده است که آتش‌سوزی در منطقه شکار ممنوع بدیل واقع در شمال بهبهان هم مرز با منطقه حفاظت شده خائیز هشت شب جمعه پنجم تیرماه شروع شده و هنوز هم ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76726" target="_blank">📅 17:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76724">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">میثم پیرفلک، پدر کیان پیرفلک، که در جریان اعتراضات «زن،زندگی،آزادی» در ایذه کشته شد روز یکشنبه هفتم تیرماه پس از حذف ایران از جام جهانی در واکنش به حرفهای رامین رضائیان، نوشت: «خدا بخواد نمی‌شه که نمی‌شه آقای رضاییان.»
رامین رضاییان، پیشتر گفته بود: «اگر خدا بخواهد پیروز می‌شویم و دل مردم شاد می‌شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76724" target="_blank">📅 17:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KzkPUKD150Q3ST7DJtN2yjKwQRgv59GTBadg2uWk7L4ScoilPhoascZ-CmOdnY-DDuKe2E_R1dsynmmjX67MWD5e_Oh74UHrWI9uGEAvqgWSk2xJ_L2I2WeABpGVFobsG_9AXDP6EONTXdvy0aFTqzWvsvbDDas2MVRVpKVD6URlbK29ZChI2uql_Qyg87pcut5O6WZjWlTjTTeSfX3FCGhz17ESanM5FGqXtK19CQZKu_QIaHVipn8FexatdolA_fp66hkfQ1mBVDg6ruWoN0TvzKNDXUkjLfeNaW_vKOyIZTeVt5TVewmDh1TLQFNVuoDT7rmr_HkDTetn7bNYGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار الجزایر و اتریش در مرحله گروهی جام جهانی فوتبال با تساوی سه بر سه پایان یافت؛
نتیجه‌ای که آخرین شانس تیم ایران برای صعود به مرحله حذفی را در آخرین ثانیه‌های مرحله گروهی جام از بین برد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/76723" target="_blank">📅 07:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76722">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ibKV5EEWDN2phTx5ywQirhlVfCGOxHqQJuS1Ihz2s6LS9iX6bZvngcJkDD9rlkKlkKzOsqvFzTOjAV_sEQcrgxuhp5fmH2LFd6N1FVrbbx2HA_NoBvDteeZG0zyxkJRsHLpTYlpdjPvqXL5iTX0OCuRVPy9pgH6-F-SJIAZMdF_ai2_cW7TxTHlTe2miDfj3mL4vssHXNy6fiBnIhBnB1UiT9Pq2eTZwHWiWTF3los74rOUiOuRROQSqaJIyX_i-zuRIn2Jzm9TTzfed1YZoKKj2HxkyaCe4X-lxFvnIVI3_T0Ogu8tcvdQwG1EBn5AkoeAoty-P8xuEHMMU_eMCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران، با انتشار بیانیه‌ای از حمله مشترک موشکی و پهپادی به مواضع ارتش ایالات متحده در منطقه خبر داد.
بر اساس این بیانیه، نیروهای دریایی و هوافضای سپاه در ساعت ۲ تا ۳ بامداد یکشنبه، ۷ تیرماه، هشت زیرساخت کلیدی ارتش آمریکا را در پایگاه «علی‌السالم» کویت و ناوگان پنجم دریایی در بندر «سلمان» بحرین هدف قرار داده‌اند.
سپاه این عملیات را «پاسخی قاطع» به حملات هوایی بامداد یکشنبه آمریکا به پنج پست ساحلی ایران در جنوب کشور دانسته و واشنگتن را به «نقض عهد» متهم کرده است.
در بخش دیگری از این بیانیه، با اشاره به اینکه کنترل ترتیبات عبور و مرور در تنگه هرمز بر اساس «تفاهم‌نامه اسلام‌آباد» بر عهده جمهوری اسلامی است، تاکید شده که از این پس با کشتی‌های متخلف قوی‌تر از گذشته برخورد خواهد شد.
سپاه پاسداران با هشدار به ایالات متحده اعلام کرده است که هرگونه تجاوز احتمالی بعدی، حتی اگر علیه اهداف کم‌اهمیت باشد، با پاسخی «خردکننده» مواجه می‌شود.
@
VahidOOnLine
متن خبر منابع حکومتی:
🔸
سپاه پاسداران خبر داد: عملیات قاطع موشکی و پهپادی در پاسخ به تجاوزهای آمریکا/ با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی بامداد یکشنبه با صدور بیانیه ای از پاسخ قاطع نیروهای دریایی و هوا فضای سپاه به تجاوزهای اخیر آمریکا خبر داد و تاکید کرد: من‌بعد با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه‌ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت. دشمن بداند نقض آتش‌بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
در ادامه این بیانیه خطاب به مردم عزیز و شرافتمند ایران اسلامی آمده است:
فرزندان غیرتمند شما در نیروهای دریایی و هوا فضای سپاه طی عملیات مشترک موشکی و پهپادی در ساعت ۲ الی ۳ بامداد امروز یکشنبه هفتم تیر ماه، با پرتاب موشک های بالستیک و پهپاد به سوی هشت زیرساخت مهم ارتش کودک‌کش آمریکا در پایگاه علی السالم کویت و ناوگان پنجم دریایی در بندر سلمان بحرین آنها را منهدم کردند و تجاوزهای اخیر آمریکا را با قاطعیت پاسخ دادند.
دشمن متجاوز که نقض عهد و پیمان شکنی در ذات او است، به بهانه مقابله نیروی دریایی سپاه با کشتی متخلف، اوایل بامداد امروز، به پنج پست ساحلی جمهوری اسلامی حمله کرده بود.
بر اساس تفاهم نامه اسلام آباد ترتیبات کنترل عبور و مرور در تنگه هرمز با جمهوری اسلامی است و من‌بعد با کشتی های متخلف قوی تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت.
دشمن بداند نقض آتش بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
🔹
و ما النصر الا من عند الله العزیز الحکیم
در خبری دیگر:
نیروی دریایی سپاه پاسداران بامداد یکشنبه هفتم تیرماه، با انتشار بیانیه‌ای در واکنش به حملات اخیر آمریکا اعلام کرد «شلیک‌های کور آمریکا به سیریک» معمای اشراف این نیرو بر تنگه هرمز را حل نخواهد کرد.
در این بیانیه آمده است شلیک به «متخلفان» راه عبور را به دیگر شناورها یادآوری می‌کند. همچنین با تهدید پایگاه‌های آمریکایی در منطقه تاکید شده است: «حساب پایگاه‌های آمریکایی منطقه جداست. جهنم را در این روزها تجربه خواهند کرد.»
@
VahidOOnLine
رویترز به نقل از یک مقام آمریکایی گزارش داد در پی حمله‌های موشکی و پهپادی جمهوری اسلامی به کویت و بحرین، هیچ گزارشی از تلفات نیروهای آمریکایی یا وارد آمدن خسارت یا آسیب عمده به تاسیسات آمریکا در خاورمیانه دریافت نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/76722" target="_blank">📅 04:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76721">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=OgZ8T2vhUhwl9tClMzC1aR7U76QEgc9ApFyyMkWeFPxqT7VpjBoY18EeIx5wFhiuXQCYr0DYDwskxUoIU_3-jOvwyE3tbEfvbR7FAq9JiBYEv8Y7KqD6TZPQ1auwijO0IB1i1-4gvqsuSDDBbZcK3bkwbRvFN5O8p9n8BF5K_t0PAmL40n-RKI0oPkGEl2l7lSz2kCVMJWe6bRuA0u7Hsbtm5-STauUwPwc5G5sBdBuXlIBOw_oOE8fCwL_KLMwchwesNFvoslQ9wuuszeG1NFUb_a9AeT4L322-U4NZmdkqU3YB07CD4TVtuAqZTFqRFBEhHBC1dXPvk67_LUGP6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=OgZ8T2vhUhwl9tClMzC1aR7U76QEgc9ApFyyMkWeFPxqT7VpjBoY18EeIx5wFhiuXQCYr0DYDwskxUoIU_3-jOvwyE3tbEfvbR7FAq9JiBYEv8Y7KqD6TZPQ1auwijO0IB1i1-4gvqsuSDDBbZcK3bkwbRvFN5O8p9n8BF5K_t0PAmL40n-RKI0oPkGEl2l7lSz2kCVMJWe6bRuA0u7Hsbtm5-STauUwPwc5G5sBdBuXlIBOw_oOE8fCwL_KLMwchwesNFvoslQ9wuuszeG1NFUb_a9AeT4L322-U4NZmdkqU3YB07CD4TVtuAqZTFqRFBEhHBC1dXPvk67_LUGP6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
سلام آقا وحید از منطقه [...] بندرعباس چندتا موشک بلند شد به سمت دریا رفت
سلام ساعت ۳:۳۹ صدای انفجار بندرعباس
یک دقیقه بعد: الان یکی دیگه هم زدن
درود همین الان اطراف بندرعباس دوتا صدای انفجار
ساعت ۳:۳۶ دقیقه
صدای دوتا انفجار از راه دور تو [...] بندرعباس شنیده شد، فاصله دور بود اما موج انفجار تو [...] حس شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/76721" target="_blank">📅 03:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76719">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y7q9RoYHHAXIG9tscs2ChdVZOElCU9SsTrrq37MskdmL23eHNtB3JY_PHYp6Rziplmj7_QsDBKPoNdSDXsYzKDsgd2yV9q-OUvm_sQgi7OiylFVkDiJUVNT2N_t_7aN1vv-wC0REjadS8bsRj_gMJIsj3sGjf64XBdoqe1LcVzZ291xMLw4mdkG8IeFzS7UJcUuQk4ArLMULGomMobRG4taSPG9-xboAykMjg76_jVNNYRdc0657jEpr6wbjNmR5V8ZnDLUSLFimGtGYsjF51EIVWcA9-eGH2IznfLkBUPxX8UuD2-JNy4c9s6Mxif7k6Hyqbpq4hvqXlMziDnL5yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CJG29Bt12MmlH6ojk7dFiaaQarIlRtyxP1Eu68IsD7-hF7O4_TCX9DcbA2gfqYtjJuAbRSiuVvQ8lAcT2X4vgxDvHibIotA6h3eUA595mbgqJ-LTniYBxeOkiR9AvFiO5_hh6CWaXPVWMYH9J1UYsQ5ffhRlME1Pp5TEya15bBBImcSA7uEBh32SEc6dFwwU4CMzUIn-0CgUKQiJjpQ3j8-Ei8RuIdDtDfjMqtqSzfH22t0-3KSL7fte_OWHsRP43UXN-VDM8xblxBm5n3daxFQ5iLs7u6iGkg7ibG1FxcBW4OZlG1zEgHJXhVM2d1AYr4K2Sfk7ynoLPbfNr3PjXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعلام هشدار در کویت
تصاویر دریافتی
ارتش کویت دقایقی پیش اعلام کرد که پدافند هوایی این کشور در حال حاضر «با حملات موشکی و پهپادی خصمانه» مقابله می‌کند.
@
VahidHeadline
دقایقی پیش‌تر پیام مشابهی درباره بحرین دریافت کرده بودم. الان:
وزارت کشور بحرین، بامداد یکشنبه، با انتشار اطلاعیه‌ای از به صدا درآمدن آژیرهای هشدار خبر داد و از تمامی مردم و ساکنان این کشور خواست تا ضمن حفظ آرامش، فورا به نزدیک‌ترین مکان امن پناه ببرند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76719" target="_blank">📅 03:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76718">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n_Xzo16apbSPCoypsysdHcNhmSfsQ5wFBQPl-XRhtZF2p8s89peuPXD6OCN_Yiy0SRPMAcpxKntuziR_kmUiASuMKU7HGyll8uCCIt6B1WpYoyEyKqWGR94yQwmTWCZ-zzRxE_Kj2rzyB9hYdgYALnuLN7gDs2QzzA186JqjvikHujbonF-mK55lgGHope3vODzpDWttAnWOzPDyAtYU4Q9DtVkdnrZwGoUmh96OjUjg_v3_qK9z8ZvvYKHkCYKZu1Nfd3GlBNXl4uGY3T5UdiBsXt04Zmw2XFta1HvR2-2IADA7fSNk7i1AIG44IudgKq7vlQrg75CYxQ1Y1mVDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: در صورت ادامه نقض آتش‌بس، جمهوری اسلامی ایران دیگر وجود نخواهد داشت
ترجمه ماشین:
هواپیماهای ایالات متحده همین حالا محل‌های نگهداری موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند، چون بار دیگر توافق آتش‌بس را نقض کردند!
بسیار محتمل است که آن‌ها هرگز درس نگیرند!
ممکن است زمانی برسد که دیگر نتوانیم منطقی رفتار کنیم، و مجبور شویم کاری را که با موفقیت بسیار آغاز کردیم، از نظر نظامی به پایان برسانیم.
اگر چنین شود، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
رئیس‌جمهور دونالد ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76718" target="_blank">📅 02:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76717">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=nANfCiv-8rlKTxuJ10PkBW5azAxb0RiYYoiaKQ6R_zkgDBOjCWv9ZbJCrUcTGH2w_o7OLDZpjxVasO8cme3AfNZS_Mc6kVcpoUZwPF0VVld1yp_H5RvHRa8tRSEdUAXhTXnStUICbl-KD5HP3QodV6VNsanCaYTFACBrBXwo7AQ-auCHpO4udnKxQxGu5V0YYeto_JMeA6qiOh9-louOdsVCp9H9g0nkhuaPJ32N6jqF8BE3I0op9O99cgyDJgDRVCOR4VQcpze8q4HgYImRQH9FqAUkxFiB6HO98vL05RcHz4zh__vJEDazufKgrhnzLNgcssp0rtFa4BEKXQqJgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=nANfCiv-8rlKTxuJ10PkBW5azAxb0RiYYoiaKQ6R_zkgDBOjCWv9ZbJCrUcTGH2w_o7OLDZpjxVasO8cme3AfNZS_Mc6kVcpoUZwPF0VVld1yp_H5RvHRa8tRSEdUAXhTXnStUICbl-KD5HP3QodV6VNsanCaYTFACBrBXwo7AQ-auCHpO4udnKxQxGu5V0YYeto_JMeA6qiOh9-louOdsVCp9H9g0nkhuaPJ32N6jqF8BE3I0op9O99cgyDJgDRVCOR4VQcpze8q4HgYImRQH9FqAUkxFiB6HO98vL05RcHz4zh__vJEDazufKgrhnzLNgcssp0rtFa4BEKXQqJgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یارو در «رسانه ملی» جمهوری اسلامی داره میگه چون کشتی‌ها قصد عبور از مسیر «ناایمن» رو داشتند سپاه اون‌ها رو هدف قرار داده بوده!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76717" target="_blank">📅 02:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76716">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=RP93NUWKvZ1KHvAdVzTreIGZ6jwoNBbR20EUEjwzrwwgNKjeJmjvZ_fktDEvnyUDsIFB3oW2APLrthQyJTfMJG5WLn0shzZ9rBx7HzUIIZaUXtte_14EhhoyyOP6o9W03T65CfeRSstpH4Niv3eTl4PSuglUSYilQ3woT2hI0OO2Ow2AKUFbFy5nTnlMeh3kl8wr5s9ctOr3eJYMqnKGSAE2QJ7tN2oSG2Hc2Ykkx3PuYwoOLCAFNYfFIS7W3KOD_Pzpt2tZpbDV_R16A_sF83cusCg4vvM2zumqEwgzdKCCu_LP5CY-7MXes0jazvKU7if96nokejfN8E0ejKsAyw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=RP93NUWKvZ1KHvAdVzTreIGZ6jwoNBbR20EUEjwzrwwgNKjeJmjvZ_fktDEvnyUDsIFB3oW2APLrthQyJTfMJG5WLn0shzZ9rBx7HzUIIZaUXtte_14EhhoyyOP6o9W03T65CfeRSstpH4Niv3eTl4PSuglUSYilQ3woT2hI0OO2Ow2AKUFbFy5nTnlMeh3kl8wr5s9ctOr3eJYMqnKGSAE2QJ7tN2oSG2Hc2Ykkx3PuYwoOLCAFNYfFIS7W3KOD_Pzpt2tZpbDV_R16A_sF83cusCg4vvM2zumqEwgzdKCCu_LP5CY-7MXes0jazvKU7if96nokejfN8E0ejKsAyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکا پس از تازه‌ترین حمله ایران به کشتی تجاری، حملات بیشتری انجام دادند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) به دستور فرمانده کل قوا، روز ۲۷ ژوئن حملات بیشتری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا در پاسخ به حمله ایران به کشتی M/V Ever Lovely،
به ایران فرصت داده شد تا به توافق آتش‌بس پایبند بماند، اما این کشور چنین نکرد
؛ زیرا نیروهایش یک پهپاد تهاجمی یک‌طرفه را شلیک کردند که صبح امروز ساعت ۴:۳۰ به وقت شرق آمریکا به نفتکش M/T Kiku برخورد کرد. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز در حال عبور بود و بیش از دو میلیون بشکه نفت خام حمل می‌کرد.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه تعرض ایران علیه کشتیرانی تجاری، حملاتی انجام دادند. هواپیماهای نظامی آمریکا زیرساخت‌های نظارت نظامی ایران، سامانه‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات نگهداری پهپاد، و توانمندی‌های مین‌گذاری را هدف قرار دادند.
عبور کشتی‌های تجاری از تنگه هرمز ادامه دارد. نیروهای آمریکا همچنان هوشیار، مرگبار و آماده هستند.
CENTCOM
آپدیت:
بعدا ویدیوی بالا رو درباره این حمله منتشر کردند
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76716" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76715">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uud8zAspARvL6nluxls7RTGx6oo7Mt1yn91FMtXOiD_ZK0QwKjdkBCzlLl5gM6-t7tQ4OHkh5nen2ghVAcfUyI9ZZxy6yPPb7ysM9CWY57t5rvYzaDF0xy7JBv8Nk0r7GyWX815KRxuBcsGa0130W5tGdThBjaqJIbMFOdR_8D3OI4N4_hDEDxlbC7VxaDsvlnDtI7OtcWb62rpThI6JJMwLawDrlTnNY-jKrrqfoS2wrv_8Mpw6-Jf7QQaBfzyr2h62lLVQBHeK-3gCRfU54Js19R2btHOGc_MMBtEdx2XFS9sOlj-O1_ym1_w8QL25QwKrXRb_oDrQ14iRV_IpNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام رسمی ایالات متحده در گفتگو با خبرنگار آکسیوس تایید کرد که ارتش آمریکا، بامداد یکشنبه، هفتم تیرماه، در حال انجام حملات تلافی‌جویانه علیه اهدافی در منطقه تنگه هرمز است.
به گفته این مقام مسئول، این اقدام نظامی در پاسخ به حمله صبح شنبه به یک نفت‌کش تجاری در این آبراه حیاتی صورت گرفته است.
@
VahidOOnLine
پیش‌تر:
صدا و سیما: دقایقی پیش صدای چند انفجار در محدوده روستای طاهرویی سیریک شنیده شد
پیام‌هایی که من دریافت کرده بودم:
صدای چند انفجار.
طبق معمول انگار دوباره نیروی دریایی سپاه سیریک رو زدند.
سلام ساعت 12.41 صدای چند انفجار شدید بندرعباس
همین دو دقیقه قبل پایگاه دریایی سیریک هدف حمله موشکی
جوری زد که زمین لرزید
پایگاه دریایی طاهرویی سیریک رو هم زد
دوتا موشک صداش اومد رو دریابانی سیریک
دکل اسکله سپاه سیریک بعد چهار ماه موشک خوردن مداوم بلاخره امشب کج شد
قشم سمت سوزا صدای انفجار شنیده شد حدود ۱۲:۳۰
سلام وحید جان  تقریبا ساعت 00:45 صدای انفجار هرمزگان .قشم
تسنیم:
در اولین ساعات بامداد یکشنبه  صدای انفجارهایی در سیریک شنیده شده است.
برخی منابع مدعی شده‌اند که صدای انفجار در بندر طاهرویه بوده، اما هنوز هیچ منبع رسمی آن را تأیید نکرده است.
🔄
آپدیت ۱:۰۲
خبرنگار صداوسیما در سیریک به نقل از یک منبع آگاه نظامی: صدای انفجارهای شنیده شده مربوط به اصابت چند پرتابه به دکل مخابراتی در محدوده روستای طاهرویی سیریک است
💥
آپدیت ۱:۰۶
خبرنگار اکسیوس: یک مقام آمریکایی می‌گوید ارتش ایالات متحده در تلافی حمله ایران در صبح امروز به یک نفتکش تجاری، در حال انجام حملاتی علیه اهداف ایرانی در محدوده تنگه هرمز است.
آپدیت ۱:۱۲
خبرنگار صداوسیما در قشم به نقل از یک منبع آگاه: چند پرتابه در محدوده روستای مسن شهرستان قشم اصابت کرده است
آپدیت ۱:۱۷
صدا و سیما شنیده‌شدن دو صدای انفجار دیگر در شهرستان سیریک، منشاء صدا مشخص نیست.
آپدیت ۱:۴۱
صدا و سیما:
برخی منابع از شنیده شدن صدای چندین انفجار در بندرلنگه و بندر کنگ خبر می‌دهند
خبرگزاری صدا و سیما هنوز قادر به تایید قطعی این انفجارها نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76715" target="_blank">📅 00:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76713">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GQUymenbU3S8IN_FLMtE8uUrHldLa9HF1seUfRqf613OXGv3x6J55LazDuaraXA_gNlUkL2elPZBL03Tt71lnVzIj-6RC0tA2bWM9qBVWSDCfXJTDn168_uBD_-ug3A7DwShaGMeXZ58e5WNRvYN0xl84nGcOlAL2lYxpRuSkZd61Mp_JFekbs8We82MhZpC-fOD2x7BpOtxjA7uqIt9FjOagPGSFQBz0hgDU-V3llkqRPtejzpTyxCdU4JtgYZL54EYsiOsA5aL9rHXiw-VGbbETwAsPTnQQL2bEr9Gm86psb2UH_b-nivzVqPdPy08JgEDTxn1Wdh6eHBd_6pkZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G2NinRTyY8yYJ8ZYWqDVo19_15PxJNOTRqRfSACchIfLXx44X9SVE_yQJA24FC7hlcQQbjK4twH4Lc60FXYQWktETjmmuVH5tIVGc5PoJcVjG-80nUhxrl1ijYjszY_KroHrMxraOJELwBF3sBkYrBlIxu_svA7g-2IzTgE2VTtE9Bc-AqonLZCSnUr8FJnEJa016XiAS8dbJJW_4F8dywqzOPp5Wbj7zIa6gtnfKEaNw0sj9BEBLiqYjMMJQJoxQiJYeHmOxABuNYLHNWdT0YNp79BX9yvqI9jWruMBYyTczT0xWfT5-bjnEIqIgnvb-DQmg1obLh8_DIVsVgklSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه‌های ایران بیانیه‌ای با امضای جمعی از اعضای مجلس خبرگان را منتشر کردند که در آن می‌گویند بازگشایی تنگه هرمز «خلاف تعهدات مسئولان است و خطایی راهبردی شمرده می‌شود».
بر اساس این بیانیه که خبرگزاری‌های تسنیم و فارس، نزدیک به سپاه، آن را منتشر کرده‌اند، ۶۳ نفر از اعضای مجلس خبرگان تداوم حملات اسرائیل در لبنان و «عدم عقب‌نشینی»‌ ارتش این کشور از مناطق جنوبی لبنان را «نقض آشکار» تفاهم‌نامه ایران و آمریکا خوانده و نوشته‌اند بر این اساس بازگشایی تنگه هرمز «خلاف تعهد مسئولان است».
در بخش دیگری از این بیانیه نیز آمده است «بر هر ملکفی» که به دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، «دسترسی پیدا کند، واجب است آن‌ها را به درک واصل کند».
این گروه از اعضای مجلس خبرگان همچنین «تثبیت مدیریت تنگه هرمز و دریافت غرامت خسارت‌ها و بازگشت اموال بلوکه شده و رفع تحریم‌ها و خروج امریکا از منطقه» را از مطالبات رهبر جمهوری اسلامی برشمرده و هشدار داده‌اند که «هرگونه سهل انگاری در این زمینه» با واکنش مواجه خواهد شد.
این بیانیه در حالی منتشر می‌شود که اختلاف‌ها در درون طیف‌های سیاسی طرفدار حکومت بر سر تفاهم‌نامه در روزهای اخیر بالا گرفته تا جایی که روز شنبه، نمایندهٔ رهبر جمهوری اسلامی در سپاه، از منتقدان این توافق خواست با «ایجاد اختلاف و لغزش» باعث «سوءاستفادهٔ دشمن» نشوند.
تفاهم‌نامه ایران و آمریکا به‌گفتهٔ مسعود پزشکیان، رئیس‌جمور ایران، با رأی «بیش از ۹۰ درصد» اعضای شورای عالی امنیت ملی کشور شامل شماری از فرماندهان ارشد سپاه پاسداران تأیید و تصویب شده و مذاکرات برای اجرای آن آغاز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76713" target="_blank">📅 23:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76712">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=TTrogIF6KBemAInUeUw_ub5XVnZYcvgsY3vMaC6RyiQP1wkjN6AbjdtJKpodhlwZpBF9OaVpbhEI6vf49Uk8Ea_y6bTo2f-LR5G18bwGDdkYx30oxmYzWGsyFQ1RTVxR54sEXD6042EQqLZ8kXrft9eW9mk9_2d5jaJh8jezOgSxiw0xu0kcbY1nWIma914rAwkpbkJZ-oqH2if6Di4em6mUIH4sjVCCO9FONof1r8PhiAycnEo-GS6cFKmikRT5CVFamteLom1Fa1VhbIcozVZNUsL4c95MjPKabuS1N-y5cCWBuc_1uayMPOqzW10JFTLgHo4b3wE6nHaaY2Za2w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=TTrogIF6KBemAInUeUw_ub5XVnZYcvgsY3vMaC6RyiQP1wkjN6AbjdtJKpodhlwZpBF9OaVpbhEI6vf49Uk8Ea_y6bTo2f-LR5G18bwGDdkYx30oxmYzWGsyFQ1RTVxR54sEXD6042EQqLZ8kXrft9eW9mk9_2d5jaJh8jezOgSxiw0xu0kcbY1nWIma914rAwkpbkJZ-oqH2if6Di4em6mUIH4sjVCCO9FONof1r8PhiAycnEo-GS6cFKmikRT5CVFamteLom1Fa1VhbIcozVZNUsL4c95MjPKabuS1N-y5cCWBuc_1uayMPOqzW10JFTLgHo4b3wE6nHaaY2Za2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل در سخنرانی تلویزیونی خود ضمن اشاره به توافق اخیر با لبنان، آن را دستاوردی «بسیار بزرگ» توصیف کرد.
بنیامین نتانیاهو با تاکید بر اینکه اسرائیل در «منطقه امنیتی زرد» باقی می‌ماند و این مسئله ضامن امنیت این کشور است، خاطرنشان کرد که فشارهای مختلف برای خروج اسرائیل از این منطقه به نتیجه نرسیده است.
او با قدردانی از نقش دونالد ترامپ، رئیس‌جمهوری آمریکا و مارکو روبیو، وزیر امور خارجه این کشور، در تحقق این توافق، تصریح کرد که اسرائیل نه تنها "محور تروریسم ایرانی"، بلکه "محور سیاسی ایران" را نیز در هم شکسته است و افزود: «ما به دلیل ساده‌ای به چارچوب این تفاهمات رسیدیم: چون حزب‌الله را به شدت در هم کوبیدیم و حزب‌الله که منتظر کمک ایران بود، آن را دریافت نکرد».
بر اساس طرح پیشنهادی آمریکا که چارچوب توافق لبنان و اسرائیل بر آن بنا شده، نیروهای اسرائیل به‌صورت مرحله‌ای، کنترل مناطق مختلف را به ارتش لبنان واگذار می‌کنند و ارتش لبنان نیز مسئولیت جلوگیری از ورود اعضای مسلح حزب‌الله به این مناطق را برعهده می‌گیرد.
خواسته اولیه لبنان، خروج کامل نیروهای اسرائیل از مناطق جنوبی این کشور بود.
حزب‌الله لبنان، این توافق را «تحقیرآمیز» توصیف کرده و آن را فاقد اعتبار دانسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76712" target="_blank">📅 22:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76711">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W90E7V14QpOwLY1Ud7WscR_I__mOVkgHeppnoqGekvVRn8tl7aajE6yH_TDdL10Z2E9PaKf2oA_n9XlBDx-XpEF2LBYtswBfa_lU5gnvTlNNjSXbHzsNx5t_Gz3TN7upKpfHCVGFz6dCP0h13a2wd4ulHcqa8G84qG5_E1qpZw7f_sr2E57OkmAGJpsJbMrdvDysH4IXeWDH3vyR-bGow93qZu8yxZ7wlayXdyrj1Q7WEHYINk5Xt_V8Bvg42rVzk8zXkJ49KlVtJlfUc1CEOGfFVl2cLjkuA9JMKQ1-W6I-Mzj_FoCTTL4dxa5qpcG6t8-nzA7onosHCv3fhlaMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی درباره قطع شدن برق در مناطق مختلف شرق تهران:
سلام وحید جان
به طور بی سابقه ای کل برق پیروزی و بلوار ابوذر رفته کلا خاموشه محله های این طرفا
توی قطعی برقیا هیچوقت اینجوری سابقه نداشته کل محله ها با هم بره کلا شرق خاموشه
سلام وحید
ما محله نیروی هوایی ، منطقه ۱۳ تهران هستیم. برقا رفته. و اینجور که از دوستان پرسیدم تا  خیلی جاها برق نداره، حتی برق  چراغ راهنمایی  رانندگی هم قطع شده.
مثل یه سری که توی جنگ برق ها قطع شد و حمله کرده بودن شده، چشم چشم رو نمیبینه
سلام وحید جان برق شرق تهران محدوده پیروزی کامل قطع شده
وحید برق  نارمک هم رفته
😐
😑
نارمکاز پشت بوم دیدم تا جایی که افق دید اجازه میده کلا شرق تو تاریکیه
برق سمت نظام آبادم کامل رفته همه جا تاریکه
داداش برق سبلان و نظام آباد و اینام رفته
سلام برق سبلان هم‌رفته
سلام، من میدون رسالت تهرانم، تا چشمم میبینه همه جا تاریکه
بجز مناطق خیلی دورتر
کل نارمک جنوبی بی برقیم
سلام ما نارمکیم ولی برق داریم
نارمک پایین هفت حوض برق هست
سمت رسالت و سرسبز رفته
سلام برق جنوب نارمک هم قطع شده فکر کنم پست دوشان تپه مشکل دار شده
وحیدجان ما نظام آبادیم ولی برق داریم
البته به بیمارستان امام حسین نزدیکیم
وحیدجان برق شهید کلاهدوز هم رفت همی الان
داداش ما کلاهدوزیم دو دقیقه پیش رفت
همه جا تاریکه
سلام وحید جان
محدوده شیخ بهایی تهران خیابان شیراز شمالی هم برق رفت
سلام وحید جان
تهرانپارس فلکه اول
ما برق داریم ولی دارم نگاه میکنم ی سریا ندارن!
برق خیایان شیخ بهایی شمالی رفت
انتهای تهران نو سمت اشتیانی و فلکه اطلاعات برق نداریم.
ما نیروهوایی هستیم برقا تا جایی که میبینیم قطعه
آقا برق وصله چرا الکی میگن شما هم میزارین مردم همه حالشون بده ترو خدا استرس بیخود ندین
برق خیابون مدنی،  نظام آباد همچنان قعطه
نارمک ۴۶ متری غربی برق رفته بود دو سه دقیقه هست که برگشته
نارمک جنوبی، حوالی میدان شقایق هم برق رفت.
سلامت میدان ۷۰ و سمنگان هم رفته بود.
الان بعد ۲۵ دقیقه اومد
وحید جان سبلان شمالی برق قطعه
سلام، زرکش وحیدیه برق قطعه
وحید جان سلام پیروزی چهارراه کوکاکولا برق داره اما کل خیابان نیروی هوایی برق رفته به طوری چشم چشم رو نمیبینه مردم با نور موبایل راه میرن
برق نظام‌آباد اومد
ندیدم مجیدیه رو بگند که برق رفته. اینجام نیست
منتها زنگ زدم و محله بقلی خواجه عبدالله برق هست.
سلام وحیدجان ما پیروزی سمت خیابون شیوا هستیم برق داریم
برق مجیدیه و خیابان کرمان از ۸.۲۰ دقیقه کامل قطع شده . تا چشم میبینه برق اطراف قطع شده
الان. نظام اباد محدوده شرقی امام علی خاموش بود همین الان اومد.
داداش برقا اومد فک کنم یه بانکی چیزی خالی کردن رفتن دیگه
🤣
وحید یرق پیروزی بلوارابوذر اومد
آپدیت: پیام‌هایی از وصل شدن برق در بعضی از مناطق داره میاد.
همز‌مان خبرگزاری فارس:
قطع برق تعدادی از مناطق تهران؛ دلیل مشخص شد
تعدادی از مناطق تهران از ساعاتی پیش با قطعی برق مواجه شدند.
پیگیری فارس از توانیر مشخص کرد، مشکل فنی در یکی از پست‌های ۲۳٠ شرق تهران علت قطعی برق است.
هم‌اکنون تیم‌های عملیاتی و فنی برای رفع مشکل در محل پست حاضر و درحال حل مسئله هستند.
آپدیت:
همچنان که خیلی‌ها پیام میدن که برق ما وصل نشده یک عده که برقشون وصل شده بود هم دارند پیام میدن که دوباره قطع شد. شاید به خاطر همون تعمیراته.
آپدیت ۰۰:۴۰ بامداد یکشنبه:
خبرگزاری تسنیم:
برق شرق تهران وصل شد
رجبی‌مشهدی، معاون وزیر نیرو از رفع خاموشی‌های شرق تهران خبر داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/76711" target="_blank">📅 20:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76710">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDtI0Vp41ePOgFi-giXn1Ldzj4I3p0DjKWjW_2EEt4A-Y1-jZezvPMUft5-m5ACgi4Jcqx4dWFGazFrbmjrP68KV4-eyigGRuIPBIk67BM2b_hzwtUsNbd3kfwqSc91vFyXAeY-wD_A3jROZ3fKT-ED8wcOufYZqtmen7EkLaAq6jUNddc_SS_qSsu8paMMaZHFgj-Ao036GaQ7igWaQsaVeGwYD2iXY3xpLU7q8ku8soGJJ6QkC6HtEFEBzilcrcZZ8mcFLRXA2xr7NM7Mf9C8Hbr9qFUliralENofwI1jzvATokK0T4Kryh85scyLlzvN6ZK5EZpDWux6R7hWjbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رسانه‌های ایران ارائه خدمات بعضی از بانک‌ها از صبح امروز (شنبه، ۶ تیر ۱۴۰۵) دوباره مختل شده است؛ خبرگزاری ایسنا به بانک‌های ملی و صادرات در این زمینه اشاره کرده است.
شرکت خدمات انفورماتیک این اختلال را مرتبط با حمله سایبری دانسته است. در اطلاعیه این شرکت آمده است:
بررسی‌های فنی نشان می‌دهد این اختلال در امتداد آثار حمله سایبری پیشین بر زیرساخت‌های فنی و سامانه‌های متمرکز بانکی پدید آمده است.
هفته گذشته اعلام شد تمامی اختلال‌های پیش آمده در بانک‌های تجارت، ملی و صادرات برطرف شده است.
اختلال هفته پیش باعث شده بود که در بعضی موارد، حتی انجام عملیات خرید با کارت‌های بانکی هم امکان‌پذیر نباشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76710" target="_blank">📅 17:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76709">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRHKkcauf8z0SDTmg1Gddduwvb2bEgC2oYn5NgcOmrybShMGd7u_5_T19mLUA7sii0nmVEmW8t8TBZbpIILSFl-jaXuk3Q8_TELl9Jc2w6vJdMNDi3xnpIJF6kF-qsplGYhMKymFCepECmIix3bDs6ChF_UkmC2Fi5q-9FO1Ee3Ng4n3ddje1_5rSQQnnClGwK-9Ro61pC_qfdPdXGadz7NCescyMwESFmCt7gW-2HVQoF9RdkBHV2tJrUEmvW3-OQdC4hhmgjAJPEAyKzm51z_0u3jmMMi6NC4Rm3GtbpqsKxr9LxsO7CDAk2f58fS8OlsHQ-vBT5SlOGhGljKf9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهنام گلخنی، پدر احمد گلخنی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴، روز چهارشنبه ۴ تیرماه در باغباد‌ران از توابع استان اصفهان بازداشت شده و با وجود وعده آزادی، همچنان در بازداشت به سر می‌برد.
کمیته پیگیری خبر داد آقای گلخنی پس از آن بازداشت شد که
در استوری اینستاگرام خود از مردم دعوت کرده بود تا ظهر عاشورا بر سر مزار جان‌باختگان اعتراضات حضور پیدا کنند.
بنابر این خبر قرار بود او روز شنبه ۶ تیرماه آزاد شود، اما با گذشت این موعد، همچنان در بازداشت است و اطلاعی از وضعیت پرونده یا اتهام‌های احتمالی او منتشر نشده است.
احمدرضا (احمد) گلخنی، شهروند ۳۷ تا ۳۹ ساله اهل باغبادران، در جریان اعتراضات دی‌ماه ۱۴۰۴ جان باخت. او مقابل کلانتری باغبادران هدف شلیک مستقیم قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/76709" target="_blank">📅 17:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76708">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMWwoJb5b6l4pU6l-x8RrhdwlTc1ua2SNHTj1aERtw4-bl1GRLareJwBPo9Ji2iV0O_Sb0kkSNdypoDIhwJ4LcK49KfbyAoTZpxlnvF2LVN0FdrNIOKynSBJLxnvIT_4I11JF8jVSyQwz5Ss96WBqjWhCNc9TRXBzwFvSRu-whcvs5HmJSQ9wAaBl7Fga4587hixqJZFGiMvxjNDoyncpyArreYAobBGvKTGGotx9J2xpsKFP92MpB6Yu0KzEYXf6LwjHXiRvXAtojK_9CHChGeFbTZ1aQsFd1FTqQVd0uSuwVWdAULAR39zHJgLQw_4gg5_aQdeifTw3KLE6taCNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل شرکت شهر فرودگاهی امام خمینی از برقراری دوباره پروازهای میان ایران و امارات تا پایان هفته جاری خبر داد و گفت: ایرلاین‌های داخلی مقدمات راه‌اندازی مجدد مسیر دوبی را فراهم کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76708" target="_blank">📅 17:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76707">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kiYQBZIEUexdTq23rbGpsKD-_5bTyPFG7hSGV8wKveWHD6EbRe9hJ5c_uhI8TDalaxy65PlpkE1fgJfcG1o_-DUu6y8jJcScK1y2K5xd7rTPXqnQt8nJPgQh1MtcapSoD2GaJfdpUqEYa1eT2CZ_OvW-jG7AQToxPrKkHs81Dt0bssJshirop1Ghp5nx1eanrWE-_hprg1AEHUVq9nSc2IuZRvG1y-SWnI3caeoc3Z5ffEDBLuHdLQ4Rsie0MAmvVSGAFuYqKoywLR48apy87sNoiQUXklC9qKAP07jN4Pl8Net5EguA_okFk3i2UmqtyTZ88Y9EAU6D_muMAFR1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه بحرین در بیانیه‌ای اعلام کرد جمهوری اسلامی بامداد شنبه با چند پهپاد به خاک این کشور حمله کرده است. این وزارتخانه با محکوم کردن این حمله، آن را نقض حاکمیت بحرین و تعهدات جمهوری اسلامی بر اساس تفاهم‌نامه اسلام‌آباد با آمریکا دانست.
در این بیانیه آمده است حمله پهپادی، نقض آشکار حاکمیت بحرین، تهدیدی علیه امنیت شهروندان و ساکنان این کشور و مغایر با قوانین و عرف‌های بین‌المللی است. وزارت خارجه بحرین همچنین اعلام کرد ادامه حملات جمهوری اسلامی، هم‌زمان با تلاش‌های منطقه‌ای و بین‌المللی برای کاهش تنش، روند صلح را تضعیف می‌کند و نشان‌دهنده رویکردی برای بی‌ثبات کردن منطقه است.
وزارت خارجه بحرین با اشاره به تفاهم‌نامه اسلام‌آباد افزود جمهوری اسلامی متعهد به توقف دائمی عملیات نظامی و احترام به حاکمیت کشورهای منطقه شده بود، اما حمله اخیر به گفته این وزارتخانه، نشان می‌دهد تهران به تعهدات خود و جامعه بین‌المللی پایبند نبوده است.
بحرین همچنین با تاکید بر حق خود برای دفاع از حاکمیت، امنیت و ثباتش، از شورای امنیت سازمان ملل خواست مسئولیت خود را در اجرای قطعنامه ۲۸۱۷ و پاسخگو کردن عامل این حمله بر عهده بگیرد.
@
VahidOOnLine
یک مقام آمریکایی که نخواست نامش فاش شود، به وال‌استریت ژورنال گفت حمله بامداد شنبه، ششم تیرماه ایران به بحرین شامل دو پهپاد انتحاری (یک‌طرفه) بوده است.
این مقام مسئول اظهار داشت که یکی از پهپادها توسط یک سامانه پدافند هوایی زمین‌پایه سرنگون شد و پهپاد دیگر بدون ایجاد هیچ‌گونه خسارت یا تلفاتی، در محوطه یک فرودگاه دورافتاده فرود آمد.
همچنین گزارش شده است که یک پهپاد انتحاری به نفتکشی حامل دو میلیون بشکه نفت خام اصابت کرده و نیروهای آمریکایی دو پهپاد دیگر را که کشتی‌های تجاری را هدف قرار داده بودند، سرنگون کرده‌اند.
@
VahidOOnLine
پس از اعلام دولت بحرین مبنی بر حمله پهپادی جمهوری اسلامی ایران به خاک این کشور در روز شنبه ششم تیرماه، کشورهای حوزه خلیج فارس این اقدام را به شدت محکوم کردند.
این حمله ساعاتی پس از آن رخ داد که سپاه پاسداران از هدف قرار دادن مواضع نظامی آمریکا در پاسخ به حملات سنتکام در بندر سیریک خبر داده بود.
وزارت امور خارجه امارات با صدور بیانیه‌ای، این حملات را «نقض فاحش» حاکمیت بحرین و تهدیدی برای امنیت منطقه توصیف کرد.
وزارت امور خارجه قطر نیز ضمن محکومیت این اقدام، بر لزوم پرهیز از پیامدهای این حملات «غیرموجه» و تداوم مسیر دیپلماسی برای حفظ دستاوردهای یادداشت تفاهم اخیر تأکید کرد.
در همین حال، وزارت امور خارجه کویت این تجاوزات را تضعیف‌کننده خطرناک تلاش‌ها برای صلح دانست و بر همبستگی کامل خود با بحرین تأکید کرد. جاسم محمد البدیوی، دبیرکل شورای همکاری خلیج فارس (GCC) نیز این حملات «خائنانه» را که به گفته وی زیرساخت‌های غیرنظامی را هدف قرار داده، به شدت محکوم کرد. این تنش‌ها در حالی اوج گرفته که از دو شب پیش و با حمله سپاه به یک کشتی باری سنگاپوری، فضای امنیتی در تنگه هرمز به‌شدت بحرانی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76707" target="_blank">📅 17:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76706">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HS3ZyZzxDcgcUcyl7uDmeaabp-MvtZpoR1eg_pV4livkQ3-mYANM8m2o33qAyPHVLP3LlGStI9J3ukCvc_I48-2qGP5YjIC-6mp3YT3y6I4W0vVTxNTMj4IGp5_ENtsOi0EOkD-0LWLYE1bXJKaT38Dpzm6NcVCFzJRDk5Fzd_3Ha_xg-VNnts51e_zwsW8LU911XPTinzgXjrCWaaJCsgT3LcIKC_2gT8-MNnEin381_Hw_78MbJnF9-snqVhev7zQNoAxyEIMXR3KcbdolR41OLdxBqh_j_ZfNvRDiSYSepwx8zLfyf_CeUbBbLjtJxF-ytpcBVFXSv7t5S-ajQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ می‌گوید بررسی‌های داخلی وزارت دفاع آمریکا نشان می‌دهد مجموعه‌ای از نقص‌ها در سامانه‌های اطلاعاتی و هدف‌گیری ارتش این کشور ممکن است در حملهٔ موشکی به مدرسه میناب نقش داشته باشد.
بر اساس گزارش بلومبرگ که روز جمعه ششم تیر منتشر شد، یک تحلیلگر اطلاعاتی متوجه شده بود ساختمانی که در پایگاه دادهٔ ارتش آمریکا به‌عنوان یک تأسیسات نظامی ثبت شده بود، در واقع به دبستان تبدیل شده است.
به‌نوشتهٔ بلومبرگ، منابع آگاه گفته‌اند این ارزیابی در سال ۲۰۱۹ در یک سامانهٔ دیجیتال ثبت شد، اما آن سامانه به پایگاه دادهٔ رسمی هدف‌گیری ارتش متصل نبود.
مقام‌های رسمی آمریکا تا کنون جزئیات این گزارش را تأیید یا رد نکرده‌اند.
بلومبرگ می‌نویسد تحقیقات پنتاگون همچنین بر ضعف‌های دیرینهٔ سامانه‌های اطلاعاتی ارتش آمریکا از جمله استفاده از پایگاه‌های دادهٔ قدیمی و نبودِ ارتباط کامل میان سامانه‌های مختلف متمرکز است. این گزارش می‌افزاید هنوز مشخص نیست فرماندهی مرکزی ارتش آمریکا، سنتکام، پیش از حمله از فرایند تکمیلی بازبینی اهداف استفاده کرده است یا نه.
وزارت دفاع آمریکا اعلام کرده است تحقیقات دربارهٔ این حمله همچنان ادامه دارد و جزئیات تازه‌ای ارائه نکرده است. دونالد ترامپ نیز گفته است ممکن است هرگز مشخص نشود چه کسی مقصر بوده و خود او هنوز مدرکی ندیده که قانعش کند آمریکا مقصر بوده است.
ایران می‌گوید در حملهٔ هوایی به مدرسهٔ میناب که ۹ اسفند پارسال در نخستین روز حملات آمریکا و اسرائیل به ایران صورت گرفت، دست‌کم ۱۷۵ نفر از جمله ۱۶۸ دانش‌آموز کشته شدند. شورای تشکل‌های صنفی فرهنگیان تأیید کرده که در این حمله بیش از ۱۰۸ دانش‌آموز کشته شده‌اند و گفته است معلمان هم در میان قربانیان این حمله بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76706" target="_blank">📅 17:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76705">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DeupSz6GMCCcWE6sv4KvfMAKQrzFGrk4eCxClRtx04TGhVTMDBTatCQUIfXKFdeMnKz03OosXwkvtbPLP7ynRwK_bNCV7x1AZeKFO99K2zdn1lwdjEX_Y2X-UaF-3fQ90vLzqSptJQJmMFoCBL_ibYcVC_ir5yYNr4igAmw-pRnrZtJmY-99pf4XISLfzqjNK9QXCaSrYXJSqDfXeMIhKHDk_JuXMEnLVc06brqtpNCEfT1NGuuF9nHBu9Vo4c8O6qvJtlA43qn7kTsc449x8NFpVoszIubD_rKWtLKeZ3Wd3AaUWz9dGcVZ30bnOTJk8NJpLNzKpmMil-mt5Z0fpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"یاسین محمودی، نوجوان ۱۶ ساله و اهل رفسنجان در استان کرمان، در جریان اعتراضات مردمی این شهر با شلیک مستقیم نیروهای حکومتی جان خود را از دست داده است.
بنابر اطلاع ایران‌وایر، یاسین محمودی روز جمعه ۱۹ دی‌ماه ۱۴۰۴ در خیابان طالقانی، ابتدای سه‌راه امیرکبیر رفسنجان، هدف شلیک مستقیم نیروهای حکومتی قرار گرفت.
گلوله به ناحیه شکم این نوجوان اصابت کرد و او بر اثر شدت جراحات جان باخت."
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76705" target="_blank">📅 17:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76704">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EPcItoAyXJlZF1o-1L4tFixwcm0tPOr2Tuuik_3UH8TK-ugW_UX9icsHKUI5xCZlgn92nqKCIVeS4D_Pn2T569n3iANnHkFhLFnO7LvG4aiRW8B7YYDAYgmcjzfUchJPzFTUHHJS0dgQuh8ysONOowqOkN0xgqD2p3nFbHuRQ9FPihHW74iOFgw-GGBtufIuqPm0r8rCEoIdAVbsC2kmGPyVMT9Tq3omi00igi6aUj4MruI52Fq9dBj8EwFAURifbPF1S_H3LTotEEAULrQUIwoa9H8ueNq5rNWWUuPlbHX9-LQPQLuYE1BSl8fx-wAcey3jYckM7hhhGWT8d3dwyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسابقه فوتبال ایران و مصر با نتیجه مساوی یک یک به پایان رسید.
بلژیک با پیروزی ۵ به یک بر نیوزیلند و مصر هم با ۵ امتیاز و به‌دلیل تفاضل گل کمتر، به عنوان تیم‌های اول و دوم به مرحله حذفی صعود کردند.
به این ترتیب صعود ایران به نتیجه بازی‌های غنا با کرواسی، ازبکستان با کنگو و الجزایر با اتریش گره خورده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/76704" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76703">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=HLuiSCccZ2SxAHnWHlm_6dqo1h_RBcSCQ4MU5toxqzYJ6DIWjfhx69akQmH43nZXvGT6Cw_-gFr9DjFbeZy4cWT1COyI-IJ5suQjgml8aS-uIblJRrX8sKwZcK2RrIvRXJkZLk-qMK8KhA8HH9eMIEJnxIGf_HFT_ckpxACmJuvl1ORCo7LXVZnSPCjUDr0jkytnQsvOpIvGdneJM5rtEmX1sAY7UyPT4Mch-Vh0Ydb_Upm6_WQfno_ODSyu-njv1-aNbpoBILvCArUCNooLve5CXHK8tbF18ZV-Wtld4IBSMnVc4Fe4ajx61qwotQ3k8Y8viRPKWpVtDp2RGmYjIg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=HLuiSCccZ2SxAHnWHlm_6dqo1h_RBcSCQ4MU5toxqzYJ6DIWjfhx69akQmH43nZXvGT6Cw_-gFr9DjFbeZy4cWT1COyI-IJ5suQjgml8aS-uIblJRrX8sKwZcK2RrIvRXJkZLk-qMK8KhA8HH9eMIEJnxIGf_HFT_ckpxACmJuvl1ORCo7LXVZnSPCjUDr0jkytnQsvOpIvGdneJM5rtEmX1sAY7UyPT4Mch-Vh0Ydb_Upm6_WQfno_ODSyu-njv1-aNbpoBILvCArUCNooLve5CXHK8tbF18ZV-Wtld4IBSMnVc4Fe4ajx61qwotQ3k8Y8viRPKWpVtDp2RGmYjIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم  ترجمه ماشین: حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری  تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی…</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/76703" target="_blank">📅 06:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76702">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EG7xprj7-DlCsRoRKZAfNhzSI5cg_MDxnE1s2e1ilvJxG-PvjCDH2H2L_YgvDdY2vRAQkWsj7ZzuK_1AKd1Xi3TuJ5pP7TFdOQSLEiScSwb4HezidezRuCgWVSAS37Tws7sfN5knVVlJVU0EP9wkDwPqt5GtvU4ve7GhzI4Ehu4y3NurYQtPVWU_tvTBKyL7-jhCmDfteh4j8yv6Jf21WUWzKuuGWevWpbWsJI-SQpD0Je8dPL15B-8d3oYNurLA7tvjztIvPhNRSChHv62HN1rxmAUaNaz2TzwTMzKMPSh39OjQUMRgPOyJJv21O5thw_8po2-P9CYWGM51oEAPfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌سپاه پاسداران اعلام کرد که نیروی دریایی این نهاد در واکنش به حملات آمریکا به سواحل ایران، مواضع ارتش آمریکا در منطقه را هدف قرار داده است.
در بیانیه روابط عمومی سپاه آمده است که آمریکا پس از حمله به یک کشتی تجاری در تنگه هرمز، به بهانه عبور این کشتی از مسیری که ایران آن را «غیرمجاز» می‌داند، حملاتی هوایی به سواحل ایران انجام داده است.
سپاه این حملات را نقض آتش‌بس و تعهدات آمریکا خواند و مدعی شد در پاسخ، «نقاط استقرار ارتش آمریکا در منطقه» هدف قرار گرفته‌اند. جزئیاتی درباره محل این اهداف، نوع حمله یا خسارات احتمالی منتشر نشده است.
در این بیانیه همچنین گفته شده است که بر اساس بند پنجم تفاهم‌نامه اسلام‌آباد، کنترل عبور و مرور در تنگه هرمز بر عهده ایران است.
سپاه هشدار داد که در صورت تکرار حملات آمریکا، پاسخ ایران گسترده‌تر خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/76702" target="_blank">📅 03:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76701">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VhJOZBL5BGEaST9jQW-koIbyk47kg4NuVsq8xpqjSwvxe1F7rQL16ZCTlLXkfOwLFIwdwZgM-PkwcUhlnUnziT33iMoCvwGcv4lqbcPaDeeJf38uAQpCrGaqLQvvGRNSzbfuEcLoKIHYS1XkV23Nuisc-6gw_qGgUT8zILz1Z15-xjnQdh3iD1iXC3iy6XHu1-12ncDdlIdKsLa589n18GjwBYC_MSMp2Qgp4OMAJZPUwqDiir9YzyVLaPNl5zRDA3NYn_kx99l_2QM1cWoAG81XtkzRE8cT8rHYvs0hSnXUt_M8H81UhxH6mqynHrqCHseZ7GVt5uKvsWeiW01O8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
رسانه‌های داخلی در ایران از درگیری مسلحانه میان نیروهای حکومتی و گروه‌های مخالف مسلح در «ایست بازرسی بانه - سقز» خبر دادند. گزارش‌های اولیه آنها حاکی از آن است که دو نفر از نیروهای حکومتی کشته‌ شده‌اند. همچنین گزارش شده است که پنج نفر دیگر نیز مجروح شده‌اند. جزئیات بیشتری منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/76701" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76700">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I-5dBdh_5ykY4XUhnlKjovohX7aINTij4bJ5S7qaY9Hdd7A6QbPQsNUHSCFuvdTQD5Mpbc-Tn5zTeDB8qkjkblHJMSL2ihhsPBVcWMAzZtvZxWPUE1DX4aEFZS4VjjqJJ3MzfsNFE-LhEf6Fos3z7Oo1h-vSAG1RZY7gbVowTorDcVpFR8MJs3MAszEQ_wO_NByuCyhjrNZAx-l2WWiqj3etsmalHckJeWmtqvFLUSx_XjK1F3PCwC7y1WcSxqvCOCVR5e5cKD73sx6sWTkquRcmRb3kHVFJ6mLlluHZ18AvtgUS2Zhcn_OY8Fplo5MZ84vAECmM6ufBxqR847FlAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم
ترجمه ماشین:
حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آن‌که ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک‌طرفه به کشتی M/V Ever Lovely حمله کرد،
انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند.
این کشتی باری با پرچم سنگاپور، هنگام حمله ایران، در امتداد ساحل عمان در حال خروج از تنگه هرمز بود.
این تجاوز بی‌دلیل نیروهای ایرانی علیه کشتیرانی تجاری، آشکارا آتش‌بس را نقض کرد. افزون بر این، رفتار خطرناک ایران آزادی کشتیرانی را تضعیف کرد؛ آن هم در حالی که جریان تجارت به‌طور فزاینده‌ای از این کریدور حیاتی تجارت بین‌المللی عبور می‌کند.
نیروهای CENTCOM همچنان هماهنگی و پشتیبانی برای عبور امن کشتی‌های تجاری از این تنگه را فراهم می‌کنند. ارتش آمریکا همچنان حاضر و هوشیار است تا اطمینان حاصل کند که همه جنبه‌های توافق با ایران رعایت و اجرا می‌شود و کاملاً به قوت خود باقی است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/76700" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76699">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SNemPQvcfpr99fyNf8OE6c9YyxOdUEE8l3Uogsryvr5wEqeW08mlBr-U9q0o8eLkjVm54Fj-tyIbGucPrNSvyDBNy2RQk3CT2i2ii2LEqDbloK68b3ao8SvOhsc9HrnyLiyau11orjrzAgHFHYG-gS8OVKTiCJQhajkSI-fUI4ugZu-6Yd1Oi4tUDZ2Xxj3mdnVX3ULWMbJgoeheibAVRa4d7xzTgWoe-9iwZjOQa2H5YXLHKBLvvEII8xk-oxgZQ9Qm3Dfap7JkGDleHulAJ85bDrXahi4f3LQDZSpo6B6vQtd27pO0REH5KpEgd7X1GK4zIQLK6vAtZ-LHF-J7Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:
دقایقی قبل ؛ شنیده شدن صدای انفجار در طاهرویه سیریک
منشأ صدا هنوز مشخص نمی‌باشد.
اطلاعات تکمیلی متعاقبا اعلام می‌گردد.
من ساعت ۲۳:۳۰ این پیام‌ها رو دریافت کرده بودم:
اسکله طاهرو رو زد  ۳ ،۴ بار
زده بطرف تنگه
سیریک گروگ سه تا صدای انفجار
آپدیت:
تکمیلی| به گزارش خبرنگار صداوسیما در سیریک:
ساعت ۲۳ و پانزده دقیقه امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.
یک منبع آگاه نظامی علت این انفجارها را اصابت پرتابه به محدوده اسکله طاهرویی سیریک بیان کرد.
این منبع آگاه نظامی گفت: حدود ۵ ساعت پیش چند شلیک اخطار از شهرستان سیریک به شناورهای متخلف‌ در تنگه هرمز پرتاب شد.
همچنین شنیده ها از شلیک دو موشک اخطار ساعاتی پیش از حوالی کرپان به سمت تنگه هرمز حکایت دارد.
و
خبرنگار آکسیوس به نقل از یک مقام آمریکایی، جمعه‌شب، پنجم تیرماه، گزارش داد: «ارتش ایالات متحده حملاتی را در منطقه تنگه هرمز انجام داده است». پیش از این، صداوسیما از شنیده‌شدن سه انفجار در طاهرویه سیریک خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/76699" target="_blank">📅 23:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76698">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83b030969e.mp4?token=eYP_tEYlef5B6bKmWYpsINoiBQxHIaeanis2vpWmPnf1oMgeYe6MDWjfySTYKhRuqqJn8hD2LYlXWEQXHfXc17V1s_vlcdqstP1oAV-dSW9UJ-H3gjkjNk4BGunQ3U-vCwoOBmgBZD6aVYjQ7_Q-IxfGLKdHDXIi2BiZ40VN8G_LdyVovc8UEWgWX7iDgHEyF3mtDiGxdu5mIWxEyAGmSKVeqHLRKfaHaPPj-2my8dlgQPVQJjyoA_g8s72ePoshj9nZHD7zOWXRHAAhZTI4mE-4YfaXB1JlkE3vkB-JWEuC2n3N1FwOgKa93QcANP5FoGEYWxozrPSF8x-N97U1OJXt55yOdsA0MaeYG_qRKG0dDYiAunKmAinqnLa5AQM5NIfQ5dA4AngSzTrfTQ7rV830cGJo6DuWZLS5dw0d4vVg9-6cHcgs7DrlLgb23eI3WMXcuwOj41fb_uFrrcnZ_nNHjI1dvX8NFTuo85W5gJJfLGnomYjGsiahWkWXuDmO44_TFg3Hg7gbjehWDtRqNj6f2OQloaW69GmEjUsQjdAeSJWfLNdrIELG3QJQ_4oA4l7HN2dGZ3B1XNyvlpfEbd8NLG5vUqNb5-I_xGqx8SQUShyuRcx6D5EVAW53G_Ced81ylHtk-WgIQ7pHS48wVk-Qs1f0oSATbirrCMHcFP4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83b030969e.mp4?token=eYP_tEYlef5B6bKmWYpsINoiBQxHIaeanis2vpWmPnf1oMgeYe6MDWjfySTYKhRuqqJn8hD2LYlXWEQXHfXc17V1s_vlcdqstP1oAV-dSW9UJ-H3gjkjNk4BGunQ3U-vCwoOBmgBZD6aVYjQ7_Q-IxfGLKdHDXIi2BiZ40VN8G_LdyVovc8UEWgWX7iDgHEyF3mtDiGxdu5mIWxEyAGmSKVeqHLRKfaHaPPj-2my8dlgQPVQJjyoA_g8s72ePoshj9nZHD7zOWXRHAAhZTI4mE-4YfaXB1JlkE3vkB-JWEuC2n3N1FwOgKa93QcANP5FoGEYWxozrPSF8x-N97U1OJXt55yOdsA0MaeYG_qRKG0dDYiAunKmAinqnLa5AQM5NIfQ5dA4AngSzTrfTQ7rV830cGJo6DuWZLS5dw0d4vVg9-6cHcgs7DrlLgb23eI3WMXcuwOj41fb_uFrrcnZ_nNHjI1dvX8NFTuo85W5gJJfLGnomYjGsiahWkWXuDmO44_TFg3Hg7gbjehWDtRqNj6f2OQloaW69GmEjUsQjdAeSJWfLNdrIELG3QJQ_4oA4l7HN2dGZ3B1XNyvlpfEbd8NLG5vUqNb5-I_xGqx8SQUShyuRcx6D5EVAW53G_Ced81ylHtk-WgIQ7pHS48wVk-Qs1f0oSATbirrCMHcFP4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش مرتبط با ایران در سخنرانی ترامپ به تشخیص ماشین
متن  زیرنویس:
https://telegra.ph/trump-06-26-4
بعضی از جملات:
ایران هرگز سلاح هسته‌ای نخواهد داشت. نمی‌گذاریم چنین اتفاقی بیفتد.
و به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، ایران امروز نه نیروی دریایی دارد، نه نیروی هوایی، نه توان پدافند هوایی، نه رادار، و عملا نه تولیدی. ظرفیت پهپادی‌شان ۸۲ درصد کاهش یافته است. ظرفیت موشکی‌شان ۸۰ درصد کاهش یافته است. پرتابگرهای موشکی‌شان ۹۰ درصد کاهش یافته است. رهبری‌شان یک بار کشته شده، و رهبری‌شان برای بار دوم هم کشته شده.
و دیگر هیچ‌کس نمی‌خواهد رهبر ایران شود. گفتند: «چه کسی می‌خواهد رئیس‌جمهور شود؟» بعد همه گفتند: «نه، ممنون.»
این کار باید در دوره ۴۷ ساله‌ای انجام می‌شد که آن‌ها با ترور حکومت کردند. و همین کار را کردند. با ترور حکومت کردند. وقتی مرد یا زن جوانی را می‌بینید که بدون پا یا بدون دست راه می‌رود، یا چهره‌ای که از بین رفته، این به خاطر بمب کنار جاده‌ای بود که ساخته شد؛ ساخته ژنرال سلیمانی، که من در دوره اولم او را کشتم. و آن یک کشتن بزرگ بود.
هنوز می‌توانند شلیک کنند؛ می‌دانید، دیروز یک پهپاد را به سوی یک کشتی بزرگ که وارد تنگه هرمز می‌شد شلیک کردند. چهار تا شلیک کردند. ما سه تای آن‌ها را ساقط کردیم. یکی از آن‌ها؛ فکر کنم؛ ما از دستش ندادیم. کسی آمدنش را ندید و به کشتی خورد و مقداری خسارت زد. اما نمی‌توانند چنین کارهایی بکنند.
و فراموش نکنید وقتی باراک حسین اوباما JCPOA را انجام داد. ببینید، اگر به آن نگاه کنید، باراک حسین اوباما؛ اسمش را شنیده‌اید؟ او فاجعه بود. فاجعه بود. او ۱.۷ میلیارد دلار پول نقد به آن‌ها داد. ۱.۷ میلیارد دلار پول نقد و ده‌ها میلیارد دلار. آن را به ایران داد. فکر می‌کرد می‌تواند دوستی آن‌ها را بخرد. و دقیقا برعکس شد. آن‌ها از پول استفاده کردند و موشک ساختند و هر چیز دیگری.
و من برجام را لغو کردم؛ توافقی که... همان توافق هسته‌ای ایران بود؛ فاجعه بود. ضمنا مدت‌ها پیش منقضی شده بود، اما من مدت‌ها قبل از انقضایش لغوش کردم. اگر این کار را نمی‌کردم، ایران سلاح هسته‌ای داشت. اگر ۱۰ ماه پیش بمب‌افکن‌های B-2 را نفرستاده بودم، آن‌ها سلاح هسته‌ای داشتند. ما آن تأسیسات هسته‌ای را نابود کردیم. بسیار مهم بود.
و آن وقت دیگر اسرائیلی نداشتید. اسرائیل نابود شده بود. می‌دانم در این اتاق طرفداران خوب اسرائیل زیاد دارید. و اسرائیل نابود شده بود و احتمالا خاورمیانه هم نابود شده بود. و ما... آن‌ها می‌توانستند ضربه‌ای بزنند. ما خیلی سریع نابودشان می‌کردیم، اما آن‌ها می‌توانستند به ما هم ضربه‌ای بزنند.
بازار سهام از زمان انتخابات ۷۳ رکورد تاریخی ثبت کرده است. و امروز شمار بیشتری از آمریکایی‌ها نسبت به هر زمان دیگری در تاریخ کشورمان مشغول کارند. این خیلی خوب است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76698" target="_blank">📅 23:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76696">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M1RNO5fCS1azR6p3tPHwoVFBWXI82YSAIBcxnI82D8Gh5p6X7UidSFtmBZIB0J0DCfkAPUIvE7_U_rDhvwM1cGtmJtKLldHu0rc0cb68Y6dC5Qk1O87Qmf6Kb2s79w37rfp-eitFLYdfXi-pWGTDBiV56bqQDukHDe64bJEthWR_g7d-EA96tM5JgLMJbJqaPNqo6cUWjl6WWkbojdlKrn3v-7CjD9ugDe_q68zaL0AGwjMUQZiLJQxQRii9p7cOmNlcHWrMQC-8Hbd-cEPxnEfY6AJ4twB9t5OkWgf5LE5xa58S-9Eiw7MMp162jvE0yHaXDnIn4A8sm0YQqKUOkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TT_hxEnzLegIgTMi7qSMGZADGiZIKhJcTA1Q4_MsNCJsLVLJAXGjewtPfDRiaSS5hMvHKT2aZyZAoZEQffKddLSfSUmsDcolC8WXFZDjxrENdsU6MK1T5VcCjXuHnNf-W9V2sTE6uILg5KCCqAxOoJNZDfdQ9t7kXBTxjWWxwrfgndyaJXnIerKmSXR74pfPPgd5fn2nLUHpRb1Lz2wsQ3ooAiJuWSeX8uSNuwu4nZV9lFArTIsI2EgJ6RUKWzPtx2rf-knutiJi2OUl1RqLaiTjwTy9BJgLweLnLVLJAt88ZyW9W6MvXpi3b4-gJRsZon8mBgrWWvKFGc5zTA40Xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، پس از امضای توافق اسرائیل و لبنان در واشینگتن در بیانیه‌ای اعلام کرد: «این توافق دستاورد بزرگی برای اسرائیل است و مذاکرات طولانی در واشنگتن به نتیجه رسیده است. مهم‌ترین نکته این است که اسرائیل در منطقه امنیتی باقی می‌ماند و تا زمانی که حزب‌الله خلع سلاح نشود این وضعیت ادامه خواهد داشت.»
او افزود: «این توافق ضربه بزرگی به جمهوری اسلامی است و تهران تلاش می‌کند اسرائیل را به عقب‌نشینی وادار کند اما اسرائیل، لبنان و آمریکا تاکید کرده‌اند که جمهوری اسلامی و حزب‌الله در این روند نقشی ندارند.»
نتانیاهو تاکید کرد: «اسرائیل در منطقه امنیتی باقی خواهد ماند و اجازه ورود حزب‌الله یا غیرنظامیان به این گروه داده نخواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76696" target="_blank">📅 22:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76695">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=IVpul463N57yoegJr1E7SMijq8OJg_T4B9t6VgHHWVak8rj9NdwxnIq-WefwvtSgjCPLTE7flNIQ3in6-jix8n8bFoT0I0FJ613I0wEC9nO5guFXj07kuiJz8uHe1HJ463zsEhIjlfYDnod8cBFEYaZg6UThNWetSKurkJ_fMoJtBU2h8DriufC-T2uqKK2HHb-Iaxj6zjuOQgxBRjzKFhZHrV8Skf3sKxCyU34Tr3BrgOUyRk_wSNN4uZ6SXx-EsjO0rgN8Xey0EBS7cniAC5FH051QjosydcTm1_UXOjbSgAEcMgnsKYjqWXXi6QNAKDkasOTTDpgTJ3HiRPmH-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=IVpul463N57yoegJr1E7SMijq8OJg_T4B9t6VgHHWVak8rj9NdwxnIq-WefwvtSgjCPLTE7flNIQ3in6-jix8n8bFoT0I0FJ613I0wEC9nO5guFXj07kuiJz8uHe1HJ463zsEhIjlfYDnod8cBFEYaZg6UThNWetSKurkJ_fMoJtBU2h8DriufC-T2uqKK2HHb-Iaxj6zjuOQgxBRjzKFhZHrV8Skf3sKxCyU34Tr3BrgOUyRk_wSNN4uZ6SXx-EsjO0rgN8Xey0EBS7cniAC5FH051QjosydcTm1_UXOjbSgAEcMgnsKYjqWXXi6QNAKDkasOTTDpgTJ3HiRPmH-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم.
ویدیوی بالا درباره ایران نیست.:
ترجمه ماشین: همان‌طور که دیدید، کمونیست‌هایی که اخیراً در شهر نیویورک انتخاب شدند، سوسیال‌دموکرات نیستند. آن‌ها می‌خواهند شیوه سنتی زندگی آمریکایی را کاملاً نابود کنند.
فروختن کمونیسم خیلی آسان است. همه‌چیز را نابود می‌کند، اما فروختنش خیلی آسان است. صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. می‌گفتم اجاره رایگان است؛ خانم‌ها و آقایان، از این به بعد لازم نیست هیچ اجاره‌ای بدهید. از این به بعد هر کسی خانه می‌خواهد، نگران نباشد؛ فقط خانه‌ای را که می‌خواهد انتخاب کند. همه غذای رایگان می‌گیرند؛ از این لحظه به بعد همه‌چیز رایگان است. همه به من رأی می‌دادند.
مشکل اینجاست که بعد از دو یا سه سال، کشور به منطقه‌ای فاجعه‌زده تبدیل می‌شود. کشور شکست می‌خورد. همیشه همین‌طور می‌شود. فروختنش خیلی آسان است. آن سال اول، آدم فوق‌العاده محبوبی هستید. همین حالا هم این اتفاق در نیویورک و کالیفرنیا دارد می‌افتد.
اما بعد شروع می‌کنید به زندگی در فلاکت. در فلاکت زندگی خواهید کرد. غذایی وجود نخواهد داشت. مسکنی وجود نخواهد داشت. ارتشی وجود نخواهد داشت. قانون و نظمی وجود نخواهد داشت. هیچ‌چیزی وجود نخواهد داشت. از هر نظر به ساکن جهان سوم تبدیل می‌شوید و همه رنج خواهند کشید یا خواهند مرد. رنج می‌کشید یا می‌میرید. این همان چیزی است که اتفاق می‌افتد. هزاران سال است که این اتفاق با نام‌های مختلف افتاده است.
به شما می‌گویم، من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. خیلی آسان بود. لازم نبود کار کنید؛ می‌توانستید در خانه بمانید. مشکل این است که چند سال می‌گذرد و کل آنجا فرو می‌پاشد. همیشه همین‌طور می‌شود؛ همیشه همین‌طور بوده است.
اما متأسفم که بگویم ترور کسانی که با آن‌ها مخالف‌اند، عنصر بسیار مهمی در ایدئولوژی آن‌هاست. ترور برای آن‌ها مسئله بزرگی است. آن‌ها حیوان‌اند. حیوان‌اند.
در خیلی از موارد باهوش نیستند، اما در بعضی موارد هستند. جذب پیرو برایشان آسان است، چون وعده‌هایی می‌دهند که خودشان می‌دانند نمی‌توانند عملی کنند. و دموکرات‌ها هم مقابله نمی‌کنند. برای همین احمق‌اند. مقابله نمی‌کنند. می‌ترسند. من شومر [احتمالاً اشاره به چاک شومر] را می‌بینم؛ از جنگیدن می‌ترسد. آدم‌هایی را می‌بینم که نسبتاً معمولی‌اند و آدم‌هایی که ما با آن‌ها مخالفیم؛ آن‌ها از جنگیدن می‌ترسند.
دموکرات‌ها چرخش عظیمی به چپ داشته‌اند. من به بعضی از کسانی که آن شب در نیویورک انتخاب شدند نگاه کردم. این‌ها از خیلی جهات آدم‌های احمقی‌اند؛ از بعضی جهات از نظر فکری احتمالاً نسبتاً باهوش‌اند، اما آدم‌هایی هستند که می‌خواهند کشور ما را نابود کنند. آن‌ها از کشور ما متنفرند. از مردم ما متنفرند. از حزب دموکرات متنفرند.
حزب دموکرات در دردسر بزرگی است، چون این ماجرا با نیویورک متوقف نمی‌شود. این مسیر، انتخاب شدن را بیش از حد آسان می‌کند. همه‌چیز، به نوعی، برای انتخاب شدن بیش از حد آسان است. بسیار خطرناک است، اما به‌زودی چیزی برایتان باقی نمی‌ماند. مشکل همین است.
از خیلی جهات، آن‌ها اجازه می‌دهند این افراد راه خودشان را بروند و هر کاری می‌خواهند بکنند. می‌گویند نمی‌خواهیم ریسک کنیم و حرف بدی بزنیم، چون می‌ترسیم اگر این کار را بکنیم شغل‌مان را از دست بدهیم. می‌ترسند انتخابات خودشان را ببازند، حتی اگر فقط به گفتن چیزی درباره این نسل تازه آدم‌های بیمار فکر کنند.
آن‌ها آن‌قدر باهوش یا سرسخت نیستند که با طاعونی که در جریان است بجنگند. این دارد درست جلوی چشم شما اتفاق می‌افتد. اگر همان‌طور که با جمهوری‌خواهان می‌جنگند، یا همان‌طور که با من می‌جنگند، با آن‌ها می‌جنگیدند، پیروز می‌شدند. آن‌ها ما را شکست ندادند، اما در برابر کمونیست‌ها پیروز می‌شدند؛ ولی شجاعت این کار را ندارند.
پس خودشان دارند کمونیست می‌شوند و به یک حزب کمونیست تبدیل می‌شوند. این‌ها سوسیال‌دموکرات نیستند. این‌ها کمونیست‌های سرسخت و بی‌خدا هستند. کمونیست‌های بی‌خدا هستند. همه کمونیست‌ها بی‌خدا هستند. به خدا باور ندارند.
به نظر من، این جدی‌ترین تهدید علیه کشور ما از زمان تأسیس آن، حدود ۲۵۰ سال پیش، است. این تهدید بزرگی برای کشور ماست.
درباره ایران هم:
ترامپ در کنفرانس سیاست‌گذاری ۲۰۲۶ ائتلاف ایمان و آزادی، گفت: نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. نمی‌توانیم بگذاریم این اتفاق بیفتد.
آن‌ها دارند از شدت نیاز برای رسیدن به توافق التماس می‌کنند. آن‌ها خیلی چیزها به ما می‌دهند. این باید در طول ۴۷ سالی که با ترور حکومت کرده‌اند انجام می‌شد.
رسانه‌های جعلی می‌گویند آن‌ها امروز خیلی قوی‌تر از چهار ماه پیش است اما آن‌ها اکنون خیلی چیزها به ما می‌دهند.
@
VahidOOnLine
📡
@VahidOnlin</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76695" target="_blank">📅 22:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=EcNh3x8_htjfTO3jhnsc-qSs6KABKeMtlRvq5J9p-E4WreNk7wr2Dvni3-sT05P4TDpNHyXqbchMdiugOVaULTX1oyqK7ny1eprn0MfvNiyBgyB6o2Wfs3yDvO1LUNOkFcrtK0ZfUwvd-JwhrCcRRgiJlGMgpKL5Fr2wixhhi4PnMgGB7qLdfH5bWAa8WgPLMbNapLETvqAzP3O42okneBX_1eCjst3rwCJpuPfhv97-CB0-YuOvXAKuD8jQDk99FJPI1J5S5axcfy-MdQ7UQmbJHpfn-bIPKCkHFimbQCIPwxnQVR3A8I4lBWSIHOmmuRtuKuEGne0LyPwa5Z691Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=EcNh3x8_htjfTO3jhnsc-qSs6KABKeMtlRvq5J9p-E4WreNk7wr2Dvni3-sT05P4TDpNHyXqbchMdiugOVaULTX1oyqK7ny1eprn0MfvNiyBgyB6o2Wfs3yDvO1LUNOkFcrtK0ZfUwvd-JwhrCcRRgiJlGMgpKL5Fr2wixhhi4PnMgGB7qLdfH5bWAa8WgPLMbNapLETvqAzP3O42okneBX_1eCjst3rwCJpuPfhv97-CB0-YuOvXAKuD8jQDk99FJPI1J5S5axcfy-MdQ7UQmbJHpfn-bIPKCkHFimbQCIPwxnQVR3A8I4lBWSIHOmmuRtuKuEGne0LyPwa5Z691Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره‌کنندگان ایالات متحده، اسرائیل و لبنان پس از پنجمین دور از گفتگوهای دیپلماتیک، روز جمعه پنجم تیرماه، یک چارچوب سه‌جانبه را امضا کردند.
این مذاکرات شامل بررسی پیشنهادی با حمایت آمریکا بود که بر اساس آن، نیروهای اسرائیلی بخشی از قلمرو تحت اشغال خود را به ارتش لبنان واگذار کنند.
پیش از آغاز این دور از گفتگوها، لبنان خواهان خروج کامل نیروهای اسرائیلی از خاک این کشور بود؛ در حالی که برای اسرائیل، شرط اصلی هرگونه عقب‌نشینی، خلع سلاح کامل حزب‌الله و دریافت تضمین برای بازنگشتن نظامی این گروه به مناطق مرزی است.
روبیو در مراسم امضای این توافق‌نامه گفت: «این آغازِ آغاز است. کارهای زیادی در پیش داریم. امروز اولین قدم است و گاهی اوقات، اولین قدم سخت‌ترین قدم است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/76694" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76692">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=fe0nxDU87xPJSRb7OJ1Ai3m3I8jQPthyo2aGpkFddVybf47b3l6wDFjXjsygOStgdQIrGQdRJeTmUrulufy91XPqJHm9gmvA7MZ9P_H13m93JLwFRYzZSmGFzAVRmm7yOiDY4ExgmqegK1IuxVlVR09syhNQoNdEaKSyitHS2zVUtuRaa4hO9VK8yJkGa3mM710AzJ4ObUnwa5dHdHQO5Ci99_IdX4e0DBdvj8Bky5xZ4NiUeyqrIjWUVqsQszVWrfpmWLtq8462EnNJE0RcUoEQYmQP13UgxlFQx41s0XlDOVMZXinHdcRJ8DN5V-nK6lYZnzoQd0cW3XgETRU6bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=fe0nxDU87xPJSRb7OJ1Ai3m3I8jQPthyo2aGpkFddVybf47b3l6wDFjXjsygOStgdQIrGQdRJeTmUrulufy91XPqJHm9gmvA7MZ9P_H13m93JLwFRYzZSmGFzAVRmm7yOiDY4ExgmqegK1IuxVlVR09syhNQoNdEaKSyitHS2zVUtuRaa4hO9VK8yJkGa3mM710AzJ4ObUnwa5dHdHQO5Ci99_IdX4e0DBdvj8Bky5xZ4NiUeyqrIjWUVqsQszVWrfpmWLtq8462EnNJE0RcUoEQYmQP13UgxlFQx41s0XlDOVMZXinHdcRJ8DN5V-nK6lYZnzoQd0cW3XgETRU6bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که امدادگران در ونزوئلا همچنان در جستجوی بازماندگان زلزله‌های ویرانگر شامگاه چهارشنبه در میان ساختمان‌های فروریخته هستند، تازه‌ترین گزارش‌ها، حاکی از کشته شدن بیش از ۵۸۰ نفر و زخمی شدن حدود سه هزار نفر بر اثر این حادثه است.
بیم آن می‌رود که شمار قربانیان بسیار بیشتر باشد. بسیاری بی‌خانمان شده‌اند یا به دلیل آسیب‌دیدگی و ناامن بودن ساختمان‌ها، از بازگشت به خانه‌های خود هراس دارند.
در کاراکاس، پایتخت ونزوئلا، و شهر ساحلی نزدیک آن، صدای افرادی که از زیر آوار ساختمان‌های فروریخته درخواست کمک می‌کردند، شنیده می‌شد.
پیش از این مقامات ونزوئلا گفته بودند که حدود ۳۰ پس‌لرزه هم پس از دو زلزله شدید روز چهارشنبه ثبت شده است.
در پی وقوع این زلزله سازمان زمین‌شناسی آمریکا هشدار داده بود که تعداد قربانیان این حادثه ممکن است به هزاران نفر برسد.
@
VahidHeadline
هم‌زمانی این زلزله با بازی برزیل و اسکاتلند در جام جهانی خیلی‌ها رو یاد فاجعه ۰۰:۳۰ بامداد پنج‌شنبه ۳۱ خرداد ۶۹ در استان گیلان انداخت که همزمان با بازی همون دو تیم در جام‌جهانی ۹۰ ایتالیا اتفاق افتاده بود.
زمین‌‌لرزه‌ای که حدود ۴۰ هزار نفر رو کشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76692" target="_blank">📅 19:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76691">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGL76wGF-c_fwRyED9RKIxRYKPcJJ5FTW57swx4MRSRGf0zGaMT5fUOYND10TSSSK2Et4DP04qSh0KUGQ0_bGcsiwcVVepN4XeFmuW80CvYlwDGAhmH9ZYm1__7xjctUQpCxfB83ZsWwynOGr9KfTVnoqOR73IWyedJ-pcHS2lyn6RGD1iSV5inJvtZBBKnJ_1ZlMGC2YG_jG9yY9x1YozIlGkp0WNipqPYIY3ObLfqVtl5PaLf4msol88kGzzvE-ICbTBcEaJbRZMG1a9RFGyCKBBXjjIFTpuIYKbWqG5H-YZx9vOF-7vVEz6516an8DVTaoY1_-MfMG0nqDdWGjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی گزارش داد که روز جمعه، پنجم تیرماه، سپاه پاسداران سه نفت‌کش خارجی را که قصد داشتند از مسیری «غیرمجاز» از تنگه هرمز عبور کنند، بازگرداند. این نفت‌کش‌ها تلاش داشتند از «کریدور جنوبی» استفاده کنند؛ مسیری که اخیرا عمان و سازمان بین‌المللی دریانوردی (IMO) به عنوان یکی از دو مسیر موقت برای تردد در این آبراه پیشنهاد داده‌اند.
جمهوری اسلامی با رد این توافق، مسیر پیشنهادی جدید را «غیرقانونی، غیرقابل‌قبول و بسیار خطرناک» خوانده و تاکید کرده است که تنها مسیر قانونی برای عبور از تنگه هرمز، همان مسیری است که پیش‌تر توسط تهران تعیین شده و از نزدیکی سواحل ایران می‌گذرد.
داده‌های ردیابی «مارین‌ترافیک» نیز نشان می‌دهد که سه نفت‌کش پس از حرکت در مسیر جنوبی تغییر جهت داده و بازگشته‌اند و سه کشتی دیگر نیز مسیر خود را به سمت شمال و آب‌های تحت نظارت ایران تغییر داده‌اند.
این در حالی است که به گزارش «لویدز لیست»، بسیاری از کشتی‌ها در هفته جاری از مسیر پیشنهادی عمان استفاده می‌کردند. این اقدامات همزمان با تنش‌های اخیر پیرامون مدیریت این آبراه راهبردی صورت می‌گیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/76691" target="_blank">📅 19:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76690">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D7H96V6UBInUW8hkvZ7aPPYiTjHLfJyw_xI8KOsO6DgIpA3kPwi35b9saickii6OBP993XCpBx5apLRaFu-RLAeVR4zj70oGxMOj5mCfERxSPcN8WoJvyzAZnfpBxGMj6BrcqqcC4bmU7IA6otUInbbdgmz7X_kPFnh7QpAhjxbHDlT8YwVQPVkvoA20PIv0sMICKHAMX7-PuYWp6F2-_TWxK4brXAZjiocfQj-wSBrQ5AaSUKXdCsX6AZktjsaEDGA9P5eVM01eqFLpaWvDVFOb992zqjMpjRghGCjxidKwAZEZls4QCgryjoPPVECzr7iv5V71mg1YlESq6qqhEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
جمهوری اسلامی ایران دست‌کم چهار پهپاد حمله یک‌طرفه را به سوی کشتی‌هایی که در حال عبور از تنگه هرمز بودند شلیک کرد.
یکی از این پهپادها به‌طور مستقیم به عرشه بالایی یک کشتی بزرگ و بسیار گران‌قیمت حمل بار برخورد کرد. خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این نقض احمقانه توافق آتش‌بس ماست.
رئیس‌جمهور  دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/76690" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76689">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdtXQfPzWV7iNur4CX5xidA1ZiDc6llV0XYYbgQjiZ0Ht276wrdpTZP2TnNiOkuAYVPJh-iUH1KEPwcFnCx44cLzz8DfGm0ET_rE6e6Jo3n32dY0g36Jzh1adTLxMMKButSH-x39kgZwkXtaMW4kW-lYwXME9HSnjfLOz2BaJslmRBSMUDesFrMAkqCeVSV-yLtyCMB7CbrtXsuGmmGWiBT4jviQkDIAmEMI27-mKE8Mbl9voD1e7Kkg_cMgjE4aDHVUBL3vA7Y1R7948SASbGUJ753Bd2UB3-mryAK9jsWUmaZh9sGJ-2QgrLkmOXB4iQbfLRN4bAmxXX8-3Uf9SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرس تی‌وی، شبکه انگلیسی‌زبان صداوسیمای جمهوری اسلامی، روز جمعه خبر داد که میان ایران و ایالات متحده یک «کانال ارتباطی» در تنگه هرمز ایجاد شده تا از وقوع حوادثی که می‌تواند به تشدید تنش‌های نظامی منجر شود، جلوگیری کند.
این گزارش یک روز پس از آن است که جی‌دی ونس، معاون رئیس‌جمهور آمریکا، گفت واشینگتن و تهران قرار است این کانال ارتباطی را راه‌اندازی کنند و این اقدام را «دستاوردی مهم» خواند.
او در گفت‌وگو با وب‌سایت «آنهرد» گفت که ایران موافقت کرده تا یکی از نیروهای سپاه پاسداران را به دوحه، پایتخت قطر، بفرستد تا به گفته او «در کنار یکی از نمایندگان فرماندهی مرکزی ارتش آمریکا، سنتکام، مستقر شود» و از این طریق بخش زیادی از اختلافات حل و فصل شود..
شبکه پرس‌تی‌وی به نقل از یک منبع آگاه گفته است: «بر اساس بیانیه نهایی منتشرشده از سوی دو میانجی پس از مذاکرات هفته گذشته در زوریخ، این کانال ارتباطی با هدف جلوگیری از بروز حوادث در این آبراه راهبردی که ممکن است به درگیری نظامی منجر شود، و نیز برای اجرای مفاد ماده پنجم تفاهم‌نامه اسلام‌آباد ایجاد شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/76689" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76687">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Tc9GNfdRmNNJM1mhQrhhyra3SAfSvSexPzx87g-TY2kf9Gru3VvWrO40BG8rmQMzPIeySzwx72nuQh2SSOESadCAT1voQYR3iApmPr0H6oBh5m7I4rla2wGgggZ7_Bzl0MYm6M7vNyaUh11TpVJUi37yPEP5KaAgNVjNsnGHzIa4La6SMeSIBTS1dD8RyyOpLBbi1PBZDZomkTNGCWi9UEuvuJ7sEQVZD8uafjhrUtQAuErvflQBvzHk4SUoYJQqMvi6xltfKSKXRJP5ATCi-cniq715KpFXizo77euYBHEGz3RzetqAPSwKGVtVNiqsCYR0drzao5fIsZxSOBx-oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Kz4WTRWH_IymqB-XQuxUyLpF0eazgqVP-902s94BxKK2P_EARdp7w3uQAgLHPldVJAqLeoZCcKyWJP8J1urOLYy73gjENN_IF4KDyDxyP5d3g579fAdM4dyhYqTLfVwr-ISn9pGQecx3_DzNojub6w-UHRv2KKEmuH9rvT6igLkE9G9V6R68yAn1m21XsTrHmo2Q8J9uKGX213e9ZQir5iikK03eCq9XMSDZ4ukw3mz38jp9fmbBayQzoVeyay-q26EhOlg9NLb8GAxwIuTrOolaH_7OESFiO7jgnIchNeDv6kzevED3F-PqII86kRp0lJniWQGyIAejsA4kJ8LlqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، می‌گوید عبور ایمن کشتی‌ها از تنگه هرمز بدون هماهنگی با حکومت ایران «قابل تضمین نیست» و هشدار داد که در صورت انجام نشدن این هماهنگی، ممکن است مسیرهای تعیین‌شده برای تردد کشتی‌ها به حالت تعلیق درآید.
این اظهارات یک روز پس از آن بیان می‌شود که سپاه پاسداران اعلام کرد عبور امن کشتی‌ها از تنگه هرمز تنها از مسیرهای مورد تأیید ایران امکان‌پذیر است و هر مسیر دیگری که بدون هماهنگی با تهران اعلام شود، از نظر جمهوری اسلامی «قابل قبول نیست» و یک «ریسک امنیتی» به شمار می‌آید.
عمان روز چهارشنبه اعلام کرده بود که با هماهنگی سازمان بین‌المللی دریانوردی، یک مسیر موقت برای تردد کشتی‌ها در تنگه هرمز تعیین شده و از کشتی‌ها خواسته بود تا اطلاع ثانوی از این مسیر استفاده کنند.
@
VahidHeadline
قرارگاه مرکزی خاتم‌الانبیاء، ستاد فرماندهی جنگ جمهوری اسلامی، روز جمعه پنجم تیرماه با انتشار بیانیه‌ای درباره پرواز هواپیماهای اسرائیلی در آسمان کشورهای همسایه ایران هشدار داد.
دربیانیه قرارگاه خاتم آمده است: «حضور و تحرک هواپیماهای نظامی اسرائیل در آسمان برخی کشورهای همسایه در مسیر ایران را اقدامی خطرناک و تهدیدی علیه جمهوری اسلامی می‌دانیم.»
قرارگاه خانم الانبیاء در این بیانیه با هشدار به دولت ایالات متحده نوشته است: «اگر آمریکا نتواند اسرائیل را مهار و کنترل کند، جمهوری اسلامی هیچ تهدیدی علیه خود را تحمل نخواهد کرد و پاسخ به این اقدامات را حق خود می‌داند.»
این بیانیه در حالی منتشر شده که طی روزهای اخیر تنش‌ میان جمهوری اسلامی ایران و اسرائیل بار دیگر به‌ویژه بر سر ادامه «اقدامات نظامی اسرائیل» افزایش یافته است و تهران اسرائیل را به نقض مکرر مفاد تفاهم‌نامه پایان جنگ متهم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/76687" target="_blank">📅 19:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76682">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aXua3dT92FtgWritVfADmUM5PbezXKboxAjq117FbpSQ2n-g8GRVQA5gDIcEUp2guj5l_Eh0cVFhB_T-MlgyylXwDSkD3_hUsqKA_dsK0iTICKp2IoT0H12bNiZ6Dz9ERePYKuCeCgCxRC-35kUGnRwPh7ueh-ABIx1oNbhT8oO6ToRJEWVASn_haKZXHuxOtHCJWiH9niWb16pbxwK4rz5ZRY8kCeEG13BZL-P-c3JIMVx7O7Uc5C6TZoaRLrRGg2xZY2Aw-OX_r47A0KgU_roH-h0kfEVaqdarCnctXNVEUZixWgEghEig8nM4EQK9jRz-rTTVt3oPGSjw7JDVVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TGnr-O01we63apcZ1JlYanfAKubpAG5fswFKrFn0B1LcV_cHKQqtk9TZG3p0j5W-aKu-_rpZplN5OFTlNJN9JSW502S1dw9kBRjpJ_FLZ9g76n0OmqsbxTkDrOVJTR_DmY8O_Mz1SsewjNyJYDQgK-P1dq1LoJFKulisokSaAMhETU_UwUsbzeFdeI_xm5NdHi-c1zXHTEOsK7H5c9MR0NrZLlWpOQEVZbbM7rQ1MfPvWwY-o5P3vsUbH4ev9bdjfB27g1qkxIBrDOusPAlb5iCgxr1wMqW7zM2abHSC1hg9FQvK1XH26z9XJuQLkSKs-WgCs851gA0ur3XOCimG0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pu6DtppaPsUo_9E_CupH6baS1mKA2K7bhAUQGvYWrWHfto8mI6SNQct3yKjEcxnDqsrVXIzqzeBFw6vw--f_Yf-Oq8XDIjXJitv_omIXFRJtZS0o4gV1aE7i8LgTp3bDe0ohyLLQhI6YErZcooE20nmp4MlVqiBSfs1cK1FrS7SEqxbh4m2QSl2mLLLT_rQyEiat1AqZBilBBD4xS6LROSjx5DXPMBtSImDHWJsosvNaonACyDVKXaS9g5BJ6mv-7ADP75xr5JTRdm4WLlBocozEvyPtaVnyv7Crd-h5L3s0gSIC_gXuGqGJf0-FH-Cl-Xc0bbePx5FZNx2IfaApLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f6zVRavC_I6UefSomBmOnBYk2URcDpN8O6sqRs0sxC45lpKBSV2p47jfbOqsww_rb2EY1TRKstOtGyRFGrCHYdDaJBrI7k4myBHQKztsuweWS0Bav3JB3xSkHpY_mSYWI_TJRe93QUa-fApD0Cr_0crLsvsIP6EWOqtRZVjwuhzzSO2LNG5SbyZWbYOynbYFnB_aXo-lehzXQu1idGjIPhjjZqboDhidjYjNeGzUSzXIM-FUHZsrssr0JKSRI0R30b1337DB274gEgeLn46BzPKjEm5lBKM9Db1c4I10LBsqFoZDFZFghhyXW_JKaEXtlbyaR2XamEa0yEI1HMdqVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cKMCh0MK1W7eKA1WaKJ6VGnMeTHRi6BFq87eYoclBzKOdkkrezHwNePF-Kw9fp47U2Gke0Suq6-3rph5ccRl3CAhMESgR2PllYti_TxSbYnMacEDsgIzL0bRK8_dn75aV99b-T2MTACvsvsJqHh38wv8Uh2lsEuLTJNP5_k28sRpaDRGwH4hviM4bW0EvWPrbRvnJJzJQHzUFLVty5xUbTXN5WpoS_rJhrBAcFq79p9gqps5qLCeS7NDYFNbnu8jO3Ye23oZwlJHSoRVjyzwuewU-ooq0EQQkPdn_FniWfm--YQeGdUyUWmB7PhD8qrbrcYgkrFrbMKUHtNVMCH4zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نعیم قاسم، رهبر حزب‌الله لبنان،در سخنرانی تلویزیونی خود در مراسم عاشورا گفت: «اسرائیل هیچ گزینه‌ای جز عقب‌نشینی کامل از هر وجب از خاک لبنان ما ندارد... اسرائیل باید بدون هیچ شرطی خارج شود.»
در حالی که مقام‌های لبنانی و اسرائیلی در واشنگتن مذاکرات مستقیم برگزار می‌کنند، آقای قاسم گفت گروه او «هیچ عادی‌سازی روابط، هیچ پایان دادن به وضعیت خصومت، هیچ دستاوردی برای اسرائیل و هیچ حضور جزئی در خاک لبنان را نمی‌پذیرد... اسرائیل باید با خواری و شکست خارج شود و این اتفاق خواهد افتاد.»
حزب‌الله لبنان مورد حمایت جمهوری اسلامی ایران است و تهران می گوید در تفاهم اخیر با آمریکا و مذاکرات جاری با این کشور، منافع این گروه را در نظر می‌گیرد.
به مناسبت عاشورا شیعیان لبنان تجمعی در شهر بیروت برگزار کردند و عکس‌هایی از رهبران جمهوری اسلامی ایران هم در این مراسم حمل شد.
@
VahidHeadline
یسرائیل کاتز، وزیر دفاع اسرائیل، در پیامی در شبکه اجتماعی ایکس، در واکنش به تهدیدهای اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران، نوشت: «اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.»
کاتز خطاب به قاآنی گفت: «به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحک تهدید به او می‌آید.»
کاتز افزود: «نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان. هیچ‌چیز ما را متوقف نخواهد کرد. نیروهای ما آماده‌اند تا کار را به پایان برسانند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/76682" target="_blank">📅 19:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76680">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L_4oQzVAJ6ickzeDXDcgpaKMg5k13ha2RgjbtsQ2zwrTzt4ewnoLI2k15G-zjMtHp4kmx-3ejDI5cgqqyYICmuYorUtcaoFIVS-rYMNAbvEuk-D2DmhpAdvV1dDC8G39Dpq1msq-TvqxlUcrQFKkIgCkSL8TAB69johcWM-Y8uLU2rapCdmEyYjq6BvCr4ECDldATPPY-g0jPxyTb9sdcGIelT-jUwqe67CDu1X16-YxTuLaQB0gfzn_Tt2DM1Mg8xEPQHNLvTlbHcIsj1BjqTsQZrGFaq3nMRKINv7-N0rYVWgi4JU_AW3RQbSW_9Eijy16V6SCq3px6hFFOlKzUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aKCZEXlin_E9BRxlaNv5YMcMLNNlyH2lGLH0Bcze3eCvOLTCPK3gHbsnCWg-smxHostmDJjo8VPlEUTLUvARnqZ0NR177CzLMqzKUv9ppbkB33BRpvIhEhWZAf2Be8UJ_m86DRsWSbjglizuIfzutKnQRqHWrHGr-5Ads2_vWF1uMI-a01_QI0ARhyYhCp2V2QjFlrOgfVCaAa8QWAQ4Q5U54HAx6bXWpF2OKwjsDUf1l6bh1ej_mWC3Y2c8-mzs0og4qMoPtHGX3KVcocWJ4D2JrPyEUIhyCGgI7IL9o_ker4Z4LcDCuZnGDfxOtN6McQ7BNkLn85bAKJscRauqQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در نشست وزیران خارجه شورای همکاری خلیج فارس با حضور مارکو روبیو، وزیر خارجه آمریکا، در بحرین، کشورهای عربی حاشیه خلیج فارس بار دیگر بر لزوم مهار تهدیدهای منتسب به جمهوری اسلامی تأکید کردند. در بیانیه پایانی این نشست آمده است که تحقق صلح و ثبات پایدار در منطقه بدون رسیدگی به موضوع برنامه موشک‌های بالستیک، پهپادها و حمایت تهران از گروه‌های نیابتی ممکن نیست.
@
VahidHeadline
وزارت خارجهٔ جمهوری اسلامی ایران با انتقاد از بیانیهٔ اخیر کشورهای عضو شورای همکاری خلیج فارس، آن را «مداخله‌جویانه، غیرمسئولانه و تحریک‌آمیز» خواند و نسبت به آن‌چه «ادامهٔ رفتارهای ستیزه‌جویانه و مداخله‌جویانه در منطقه» نامید، هشدار داد.
در بیانیه‌ وزارت خارجه که روز جمعه پنجم تیرماه منتشر شد، به کشورهای حاشیهٔ خلیج فارس توصیه شده که از همراهی با آمریکا در «تهدیدانگاری» برنامهٔ هسته‌ای ایران خودداری کنند.
این بیانیه همچنین بار دیگر مواضع پیشین مسئولان جمهوری اسلامی دربارهٔ قرار گرفتن تنگه هرمز «در محدودهٔ آب‌های سرزمینی» ایران و عمان را تکرار کرده و می‌گوید همین موضوع «مبنای عمل در رابطه با مدیریت کشتیرانی در این تنگه خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/76680" target="_blank">📅 19:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76679">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awVCYPoXszIV2I9X1JmdXx0Rwy5ed47d28aXVGqDAuGILOb6aaB2aoB9Rxz-yEJfxrYEcU3st7-_x7uvRATJcaINPl80QSmm5SCTw_OJw7PPgbNQk5wE3QytPTl3dYr8OeyOIEIh4BBzdQBR46JQ7BEbf2Heo7f1uwiUyqIMVwkVuxtKdczS2VGoT7w18SLE6mJwYbkttTAiGh83Kff0Fo-vi_4jKPFrXVXDyx2AF23-1DHcpOu9dk4DdXmuoK9_mujKeYiWKTidYAhstN_hczEAxg4G0fRG3nhdlTFEEk9Sb2SBiqJfdmzRBLslf_ae8rARTLtchUCKNpQdcBBqIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، گفته است که پس از جنگ خاورمیانه، برای اطمینان از اینکه ایران به سلاح هسته‌ای دست پیدا نکند، به یک نظام راستی‌آزمایی «بسیار قوی» نیاز است.
آقای گروسی در جمع خبرنگاران در ژاپن گفت: «فکر می‌کنم هدف این تفاهم اخیر [بین میان آمریکا و ایران] این است که اطمینان حاصل شود ایران به سمت توسعه سلاح هسته‌ای نخواهد رفت. دولت ایران هم به‌صراحت اعلام کرده که چنین قصدی ندارد.»
مدیرکل آژانس گفت «اما البته صرفِ اعلام نیت کافی نیست. ما باید هرچه زودتر که از نظر عملی امکان‌پذیر باشد، یک نظام راستی‌آزمایی بسیار قوی برقرار کنیم.»
ایران گفته است که توافق درباره نحوه بازرسی‌ها و حضور مجدد بازرسان آژانس در تاسیساتی که مورد حمله نظامی قرار گرفتند بخشی از مذاکرات جاری و توافق احتمالی نهایی با آمریکا خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/76679" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76678">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F51c1d0Y-HSnSDOeZQ-_nSuFJXAFfXTanVsmcxMAXbdOVoPsSqEVmX_8Y_6YF-wKoegur62nJVxNq2r5t7GZj1uSfE67O-v7MpsaAopSXF-lsQvMTa6o1AqkH1cZTt-KF30SQ7IspyUDZngdRPLS86F7st49zq_ew07iz5Vw4bmtOIbVh4kxSk0nR3L6qse7nqDP3gOdKs4q5TP-4hyI2Yd3fk6jaVFnsivmtaK7aEeOqb2DBFvj4HabsZ74Ac4usxbs1-pNg3ZauFRywlcSfhLTn-CxUjxQHWFNLBfD5shtBNPQeuKyyUI79KU_focpI-sTXTY2ueOTbAHWxGjOoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر کانادا روز پنج‌شنبه گفت کشورش باید سفارتخانه‌های خود در ایران و ونزوئلا را بازگشایی کند.
به گفته مارک کارنی، فقدان حضور دیپلماتیک، توانایی اتاوا را برای کمک به کانادایی‌های خارج از کشور و واکنش به بحران‌های بشردوستانه، به‌رغم اختلافات عمیق با حکومت‌های ایران و ونزوئلا، را مختل می‌کند.
او در توضیح بیشتر گفت: «تعامل به معنای تأیید نیست. داشتن سفارت، داشتن خدمات کنسولی در یک کشور، به این معنی نیست که ما سیاست‌های آن کشور را تأیید می‌کنیم.»
او در عین حال گفت هنوز در این زمینه تصمیمی گرفته نشده، اما تأکید کرد که این شرایط «باید تغییر کند و حرکت به سمت این تصمیم، کاری است که باید انجام دهیم.»
روابط دیپلماتیک ایران و کانادا از سال ۲۰۱۲ میلادی قطع شده و سفارتخانه‌های دو کشور تعطیل هستند. استیون هارپر، نخست وزیر وقت کانادا در آن زمان جمهوری اسلامی را «مهم‌ترین تهدید برای صلح جهانی» خوانده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/76678" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76677">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=BUqfoUjxRhW2kMpmbXHI20gOiIqPGA-g0kPAECUULLDJYhtS-E8EqeeaZpkGtg6qvcD-QRgM3dJdDsVM5uqExSazaVFUiaWp9YQs5A9Yb4uUM3QSJCh0UJxZBDA6ZSq2mBjVTVQlfxD3MCyVQQDngCkErOj_9vEVak1rNOWrYMIWfDFmWZfFfF1JUvq-Jo_0e_vs1URzIIt-PLoNSb51CWCn0hultXbmd4OQO0ryRp-CU_0TgrQ8Scrqsk11aWRRW37DwC43cmLTOGy6l4SapTEJLTeUMB9DTOPnEfjWpkejEcbqJpzBBT3e4_kPXXKIANtW8bOmGyapZoVaII_3Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=BUqfoUjxRhW2kMpmbXHI20gOiIqPGA-g0kPAECUULLDJYhtS-E8EqeeaZpkGtg6qvcD-QRgM3dJdDsVM5uqExSazaVFUiaWp9YQs5A9Yb4uUM3QSJCh0UJxZBDA6ZSq2mBjVTVQlfxD3MCyVQQDngCkErOj_9vEVak1rNOWrYMIWfDFmWZfFfF1JUvq-Jo_0e_vs1URzIIt-PLoNSb51CWCn0hultXbmd4OQO0ryRp-CU_0TgrQ8Scrqsk11aWRRW37DwC43cmLTOGy6l4SapTEJLTeUMB9DTOPnEfjWpkejEcbqJpzBBT3e4_kPXXKIANtW8bOmGyapZoVaII_3Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودداری ساکنان آبدانان به عنوان یکی از محروم‌ترین مناطق ایران، از بردن این کیسه‌ها به منازل نمادِ «شرافت» و «شورش گرسنگانِ آزادی و نه تهی‌دستان» نام برده شده است.</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/76677" target="_blank">📅 18:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76673">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Jfl3ROUa-6BQvY1G7RGAvmySvf_DVCeflDoPZXu6dvfNTINIXj1v3qfD6CYVjTkyO8ZMrL76FITErVbBbEqKmZG6tO8StPQ_w2FvAAPD2ZExl6P4d0VXea5flKQ6xLXLcM6GZB6rzvwqr36OCzPETlRuNg_mMFk9401l39KLGSGd0pzLNi5vzHOgjBDiZtVJFE3IZsNM5HMl6cs6nIPOKr_MHvyxjOQpiGBEltz9ueFVtencnFhPC0MkXZNqVdT-pNwerSYxqvi4xd42GJSeK-_TXeS2XQRec3dJVm7LbhG6OhlMc6DGwkwwGv2wIr_Vfq0ZRTByiQ5fTXxKXsSg6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X5gbzFpSfrKtN3K6wEORBOxRd0n26H4vDwsjHxLimTikuFEuZsuXl14LylTG8CxxlV83KukPMfOEI7m5PRjXia0BH6gv7J9dtTVoTPSWomlRbKAnWWK0-9pR-OxuKQx_KnvPdKWc5wzOZj6lrcolagLD7uQraXy-S0VqTYr8RYJIy_TJcLVn_Cfa5oflDSKCw9ZbTs9QGGNDTQ6iC38b61b_BvyoCukIYXpYGC8LcuYbmU2u9arULgxJeExNtDmnTNhxujhftDF5S3kaq2K72QnRq4GuT-0OX_sO2frUDvhPjZeYvsBO7Ih3FUzHtTA4oHiaUtBn1TK3ri30-Ld8AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rCsNKPc2JjcUC7p55CPzkzP9T-B9IpEBLOp2eUZ9Y6KlAMOW0rXVvSLl5GGvNoYu9MnPDv6obJMGUYTkx9FwEDF3nGevH32yqQ8f0AkRUhS3JA5l6IWHWwOpuyJdypyhMB0YdkQhtw5uFuay1cxjFD3aPUABMqVAz5Idtuwb0Tb5PvLSbfDdDkcFICT34Y9b3XJvcrXTEPT2LU6goBT-60X37AfCoL0PFnDHfyOvsOfNwY08LNj4gF9o5KiRgAlKoZbDg_4-L24oSB7IIZwteA_OQQNl1OQtiU1eK2_YASBBfJ7nXDfOtxwqjJ2wuUbXEx7EJAFD22xpd6Ihmws8HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tsR1c3lZmcWJUxpNgGWoH3-ZzOYP8ydEhjZe8AYYouGlmemjGVDw5N-7XYt_Yk1TSTQIFM9EVQDck31kSfNurmdaCDIeVFoZhxA-PMirmEpympYPy8IPTuj7TTmxV2-SwO06l7OGjPitO3F7lsPS5UaPuw2SEToMdTGFDUY1P6ktiwIeZdhSQBvIMVA0G_5Uo6MYxZjeb98cnwnLh5KwR3cosJVm2RW6Tv1x6k4URtIoaMR-7dmzYtAP4M0Dg-B7j-9dhfph8zGK47mZL2xw288e_9dds8zhq3WihbIaUf-7uki0DxJja3b--FHyqLI5p4OQrh-PuXCRUdOJ-HOazQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
خود امارات الان مسیج زد که اشتباه سیستمی بوده
هشدار دبی اشتباه بوده
دبی ساعت ۵:۱۸ به مدت ۲ دقیقه آژیر زدن ولی گویا تست بوده
اره فکنم دستشون خورده
احتمالا تست پدافند بوده
الرت دبی اشتباه بوده الان مسیج اومد برامون
وحید جان دبی گفت آژیر قبلی رو نادیده بگیرید
🤣
دستشون اشتباه خورده بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/76673" target="_blank">📅 17:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76671">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ewjWAwMaxS9NqtBsyKTEwi5FgLjzSYTTaZXLUAj8hflbgWEMVN-vUiAHc_k1txOSaCTmoRCmlCyQ4c8qXfyIsyz9OovX8K6WHfjFp15dCPwJzZyXebIosn9r1dfrP6Cajz7LLhArtSOS09VilcWM-65F86iTWe1LgpeAR2WqCmrkUj_UbpIXsgbKj4VCJ2C86SFBdnaW2fC_5a6gooR1MR8BdFFbU1bU-x3zMTXAdxeu27etBjm9MjFPHUoKdebGUPXYgQPIP2fypKHm5BmTFj1hSLVFGei2E6EgmRe7fezV6oamNV5EFTeM2p5NIkdwopc-M2kdhMJom05URZ2kKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DWRly9sg9S5rZ9ScxEduRcCado_MXikao4pRjGdoENtJtJAjvx4IkPEgD-QMpaHx3LuXkFZC2YXY2G-kGWIZFmkB3lRuh5UEO8E4Yv8FE_e1EOEcDrgrbOCABvKtIK917WxAFXydM2xsOAIADetuRm8xGlZccXWZAPn0y_BsNeeGNmXj2rvOdaUvRD0oyVzkqjjyD-_RdSO9CVjRztFCwrG1yUFEz8cQHLuhhfKW_MVfx9p66-ZGZNcPTCpW07fgSyb642N45F6G9-pj7PEdvc9fuvhuOecbvO2XmRss0OkA-CuQJWPhzdCLWNFqnTbacuLERuj7XeJlozD1BcaC9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی الان:
سلام وحید جان
الان دبی برای ما آلارم موشک اومد
سلام اقا وحید
همین الان باز اژیر زدن
نمیدونم کجای دبی رو زدند
وحید جان همبن الان دبی آلرت موشک دادن
ما امارات هستیم
هشدار حمله موشکی بهمون دادن
الان امارات دبی دوباره صدا آژیر اومد
🫠
البته خیلی کوتاه بود، و سریع گفتن اکیه
وحید جان همین الان توی دبی برای همه آلارم حمله موشکی اومد
منطقه جمیرا ۲، کایت بیچ ۲ بار صدای انفجار شدید از آسمون اومد
احتمالا رهگیری بوده
📡
@VahidOnline
آپدیت در پست بعدی</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/76671" target="_blank">📅 16:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76670">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=YyitsniVdeV08pxDlJLgf79FsiTmhN6Sce_oQ9OfPyYTeuhG-v0H0pMYRV78az9s4GGdwnwkGtpkRkLHd1prB7MeU96SQ6cv2jIoFyNDrBgDtb_yEegGCpaZBi5ASkkiroYvpObDljSKJj3Vx4JkGLJQxsGYMQ8_nygEt00Oz8XSbP3Xxp-WivecFCQlFL7DB1LQ20grkc4i_ASiogfi10_VhVYmfW8mnW8uYkujcLGqS1xPCFrTquKVU4TUSKAADEwdVSb3t2lX4_9YkYBzY5tI87N-dNnuIb8UKfFIcQJwPkESLtNI5VDVsZ0bvcHPUoG-Kq3KmN7MHuy589ub7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=YyitsniVdeV08pxDlJLgf79FsiTmhN6Sce_oQ9OfPyYTeuhG-v0H0pMYRV78az9s4GGdwnwkGtpkRkLHd1prB7MeU96SQ6cv2jIoFyNDrBgDtb_yEegGCpaZBi5ASkkiroYvpObDljSKJj3Vx4JkGLJQxsGYMQ8_nygEt00Oz8XSbP3Xxp-WivecFCQlFL7DB1LQ20grkc4i_ASiogfi10_VhVYmfW8mnW8uYkujcLGqS1xPCFrTquKVU4TUSKAADEwdVSb3t2lX4_9YkYBzY5tI87N-dNnuIb8UKfFIcQJwPkESLtNI5VDVsZ0bvcHPUoG-Kq3KmN7MHuy589ub7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روز پیش از دیدار تیم‌های فوتبال ایران و مصر در مرحله گروهی جام جهانی ۲۰۲۶، فیفا روز پنجشنبه چهارم تیرماه اعلام کرد تماشاگران می‌توانند پرچم‌های رنگین‌کمان را به ورزشگاه محل برگزاری این مسابقه در سیاتل وارد کنند.
پیش‌تر، فدراسیون فوتبال ایران از فیفا خواسته بود از برگزاری هرگونه مراسم یا فعالیت تبلیغاتی مرتبط با گرایش جنسی و هویت جنسیتی در دیدار ایران و مصر جلوگیری کند. این درخواست پس از آن مطرح شد که کمیته محلی برگزاری جام جهانی در سیاتل این مسابقه را «بازی افتخار» (Pride Match) نام‌گذاری کرد چون هم‌زمان با «هفته افتخار» (Pride Week) برگزار می‌شود.
ایران و مصر پس از قرعه‌کشی با این عنوان مخالفت کرده بودند. همجنس‌گرایی در هر دو کشور جرم‌انگاری شده و قوانین کیفری برای آن وجود دارد.
فیفا در بیانیه‌ای اعلام کرد جام جهانی رویدادی فراگیر است و پرچم‌های رنگین‌کمان و دیگر نمادهای مرتبط با گرایش جنسی و هویت جنسیتی، به‌عنوان نمادهای حقوق بشر، اجازه ورود به ورزشگاه‌ها را دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76670" target="_blank">📅 06:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76669">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cvHlYFzZuEDwljv7OaIqzAC9UdVZ9jcCj_BuYa8ccUfWOJgdPOz9E1kJrICBlq1GRRxRNv-GAHSWY1_ZNhzmTZM7CRXicZf6w6vMDQVWAq8xEir_2N1KQzeQLjlw-fH1OFVAv1ghfN6qac_iY0pTG_gDXQApy5iy54ROOqucz-8iLStrjQOhnMc538vq49Y6Xbe-xzlh5nT57_2P3PyfXPnmpkmjHjaqggSI_Mkv70AX4QB0Z3zL9N7dyHZPVWc4W6mMOb9N44y06sL8KBOxMxkP_TpCPOr4LaQ2Enuq6nFgsB3Xkghki2-tzzNfmb_Zdy9Z6RxgTUkEviOExbQXMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: یک مقام آمریکایی به CNN گفت یک کشتی باری در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛
اتفاقی که باعث شد سازمان بین‌المللی دریانوردی عملیات تخلیه خود را در تنگه و اطراف آن موقتاً متوقف کند.
ترجمه ماشین: یک مقام آمریکایی به CNN گفت یک کشتی باری روز پنج‌شنبه در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛ حمله‌ای که باعث توقف عملیات تخلیه هزاران دریانورد از کشتی‌هایی شد که از زمان آغاز جنگ در خلیج فارس گیر افتاده‌اند.
این مقام آمریکایی جزئیات بیشتری درباره این حمله ارائه نکرد. ایران مسئولیت آن را بر عهده نگرفته است.
سازمان عملیات تجارت دریایی بریتانیا روز پنج‌شنبه اعلام کرد که یک کشتی باری از سمت راست خود با یک پرتابه ناشناس مورد اصابت قرار گرفته و پل فرماندهی آن آسیب دیده است. بر اساس این اطلاعیه، ناخدای کشتی گزارش داده که هیچ تلفات جانی و هیچ پیامد زیست‌محیطی در پی نداشته است. مقام‌ها در حال بررسی هستند و به کشتی‌ها توصیه شده با احتیاط عبور کنند و هرگونه فعالیت مشکوک را گزارش دهند.
‏CNN برای دریافت نظر با کاخ سفید تماس گرفته است.
توقف عملیات تخلیه چند روز پس از آن صورت می‌گیرد که سازمان بین‌المللی دریانوردی (IMO) اعلام کرد توافقی میان ایالات متحده و ایران راه را برای تخلیه بیش از ۱۱ هزار دریانورد گرفتار در منطقه خلیج فارس باز کرده است.
آرسنیو دومینگز، دبیرکل IMO، در بیانیه‌ای گفت: «پس از آغاز طرح تخلیه IMO، که طی آن چندین کشتی تاکنون با موفقیت تخلیه شده‌اند، تصمیم گرفته‌ام اجرای آن را موقتاً متوقف کنم تا دوباره اطمینان حاصل شود که تضمین‌های ایمنی لازم همچنان برای کشتی‌های موجود در فهرست تخلیه ما و همه کشتی‌های حاضر در منطقه برقرار است.»
او گفت از حمله‌ای در روز پنج‌شنبه در دریای عمان به یک کشتی که از تنگه هرمز عبور کرده بود مطلع شده است و افزود که آن کشتی تحت چارچوب تخلیه IMO فعالیت نمی‌کرده است.
دومینگز گفت: «من همیشه تأکید کرده‌ام که ایمنی دریانوردان در اولویت مطلق است. بنابراین، برای تضمین رویکردی هماهنگ و ایمنی دریانوردی، طرح تخلیه تا زمان روشن شدن بیشتر موضوع متوقف خواهد شد.»
دومینگز یادآور شد که پنج‌شنبه «روز دریانورد» است و گفت این لحظه ضرورت اطمینان از ادامه تلاش‌ها برای تخلیه «هزاران دریانورد گرفتار در خلیج فارس» را برجسته می‌کند؛ بدون آنکه آن‌ها در معرض خطر تبدیل شدن به «قربانیان جانبی این درگیری ژئوپلیتیک» قرار بگیرند.
سازمان مدیریت راه‌های دریایی خلیج فارس ایران روز پنج‌شنبه اعلام کرد کشتی‌هایی که خارج از مسیرهای تعیین‌شده آن حرکت کنند، تضمینی برای عبور ایمن نخواهند داشت و مشمول بیمه یا مسئولیت‌های مرتبط نیز نخواهند شد. این سازمان در پستی در X افزود: «پیامدهای حرکت در مسیرهای غیرمجاز بر عهده مالک، بهره‌بردار و فرمانده کشتی خواهد بود.»
این تحول در حالی رخ داد که مارکو روبیو، وزیر خارجه آمریکا، در منطقه خلیج فارس حضور دارد تا توافق با ایران را به سه کشوری عرضه کند که احتمالاً از بزرگ‌ترین بدبینان آن خواهند بود.
هفته گذشته، ایالات متحده متن رسمی یادداشت تفاهمی را که در آخر هفته با ایران به دست آمده بود منتشر کرد.
یک مقام ارشد دولت آمریکا متن سند ۱۴ ماده‌ای را خواند؛ سندی که مفاد مربوط به بازگشایی تنگه هرمز، کاهش برخی محدودیت‌های مالی علیه ایران و انتظارات برای رسیدگی به برنامه هسته‌ای ایران در مذاکرات فنی آینده را تشریح می‌کند.
قیمت نفت آمریکا پس از جهشی که در پی تعطیلی تنگه هرمز به دلیل درگیری‌ها رخ داد، به پایین‌ترین سطح خود از آغاز جنگ ایران رسیده است.
cnn
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76669" target="_blank">📅 03:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76667">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=bSwNxfaMxYqjL65QqPeJXa54doaGw-HV0UKTCFDp8uZ05iTEQ5YacifHKWahXR1q_t2blwwSrn8ZHD1TQvIsQ-TTkXqYmkPUWUz2MmZxEnLIXOoMJmJkhXUzHXoAbvfQa20QCXlyNTGQpkV1AYfQAzc3t7plGiGM3Z9o1pAYuGhrfWpyGR-ZnEIf9ZPygd9mQAG8e3rcTeMdd4lzob7O80NMsRgjvrokhfyBNLs6Pv6QVagnd5XtXd9YRma1K6BmM2eJ1s8caK9cCQlSLfaAiXUmpYBd88zVsz6Zt2WtTwyTwEgq-pVX5Bzpog7CUCJ5LChwWN2SWaXmBufcHgsv_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=bSwNxfaMxYqjL65QqPeJXa54doaGw-HV0UKTCFDp8uZ05iTEQ5YacifHKWahXR1q_t2blwwSrn8ZHD1TQvIsQ-TTkXqYmkPUWUz2MmZxEnLIXOoMJmJkhXUzHXoAbvfQa20QCXlyNTGQpkV1AYfQAzc3t7plGiGM3Z9o1pAYuGhrfWpyGR-ZnEIf9ZPygd9mQAG8e3rcTeMdd4lzob7O80NMsRgjvrokhfyBNLs6Pv6QVagnd5XtXd9YRma1K6BmM2eJ1s8caK9cCQlSLfaAiXUmpYBd88zVsz6Zt2WtTwyTwEgq-pVX5Bzpog7CUCJ5LChwWN2SWaXmBufcHgsv_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل کاتس، وزیر دفاع اسرائیل، در مراسم فارغ‌التحصیلی افسران رزمی در پیامی هشدارآمیز به تهران گفت: «اگر ایران به دلیل فعالیت‌های اسرائیل در لبنان یا به هر دلیل دیگری به اسرائیل حمله کند، با تمام قدرت به آن ضربه خواهیم زد؛ به‌گونه‌ای که برتری قدرت ما را به‌روشنی نشان دهد.»
همزمان، بنیامین نتانیاهو نخست‌وزیر اسرائیل، تأکید کرد، حضور نظامی اسرائیل در مناطق امنیتی جنوب لبنان، سوریه و نوار غزه ادامه خواهد یافت و زمان‌بندی مشخصی برای پایان آن در نظر گرفته نشده است.
این در حالی است که جمهوری اسلامی ایران در جریان مذاکرات اخیر  بر ضرورت جلوگیری از گسترش درگیری‌های اسرائیل در لبنان و خروج نیروهای این کشور از خاک لبنان تأکید کرده است.
همچنین برخی مقام‌های لبنانی و جریان‌های سیاسی منتقد حزب‌الله، تهران را به دخالت در امور داخلی لبنان و تأثیرگذاری بر تصمیم‌های سیاسی و امنیتی این کشور متهم می‌کنند.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روزپنجشنبه چهارم تیرماه  در مراسم فارغ‌التحصیلی افسران نظامی در جنوب این کشور تأکید کرد که نیروهای اسرائیلی «تا هر زمان که لازم باشد» در منطقه امنیتی جنوب لبنان باقی خواهند ماند و قصدی برای عقب‌نشینی ندارند.
او همچنین با اشاره به فشارهای بین‌المللی، از جمله توقف ارسال مهمات در جریان جنگ، گفت اسرائیل در صورت لزوم «حتی با حداقل امکانات» به جنگ ادامه خواهد داد.
نتانیاهو در ادامه با اشاره به ایران گفت: «با توافق یا بدون توافق، تا زمانی که نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76667" target="_blank">📅 22:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76666">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EC77fjnkAK2VfThkgfaozBfbHksXiqCMjJeS-e_8AvLy7f2cjhqRVjyypkGSjiYloXEI8-q7VC0d_jB0EwscGQTnbGpDfuJ8swQPGBoFIHx_mcV0UnIwpzNvafNSnygZp1dnl-JPJJqKE_XxKCfhEXX24n7_7gL5J3Kq8clwd26rT_K7VotcAill57IaSVvq4zjufqHVwfaiGWMq1qUErp3tHp5bZeYJR9zHJPXOoQ6kIWVDDKZKxSDq-PIw9qGPiOP721dmPeiFfGEccBQ3R0Il-F01e1_NDNPo27V0geYd-nz-OdbDzw7UwxuV1IIk_iElGPM1DlZQPBkKgfLdYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی خبرهای منتشر شده در برخی رسانه‌ها و شبکه‌های اجتماعی در خصوص ممنوعیت شعار دادن علیه آمریکا و آتش‌زدن پرچم این کشور پس از امضای تفاهم‌نامه را «جعلی» خواند.
میزان نوشت که ریشه این خبر در «سرویس دشمن و در راستای عملیات روانی دشمن» است و تاکید کرده که انجام چنین کاری جرم‌ نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76666" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76665">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u2h_ecRXlZHf72EDfPz9-tobIYn26blyM1JN0HGWp7YGjMvfru3JEUKXBtN6hEJqqy8a6ef4UwCQEumwQxFTViui76ljiFzMYyyu18WulQweJadNJ5BQ55mbZUw2J-eIQrSSYSl4aClKsZ4dENGIjx9N9s7y8XF3bJb2NSU3HQhHznUTCyCW-1upg4WbFAJ1x6FWFvjNwgD5CX9YJkfPEPoPulExVw8WDkWeciUictQ0Z1g3RnfLaK3msVLK_KTsuTAqyx6CMeYwWnjjEnaODoJOnQRgTfu1exacxz3LJSrwaaDxKN2jEI9ZKIxzjyfiLNC6LuQaMqf1VTsOcvsjvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، گفت یکی از مهم‌ترین دستاوردهای مذاکرات سوئیس، توافق اولیه برای ایجاد یک کانال ارتباطی مستقیم نظامی میان آمریکا و جمهوری اسلامی با هدف جلوگیری از تشدید تنش‌های آینده بوده است.
او افزود: «یکی از چیزهایی که می‌خواستیم از این مذاکرات به دست بیاوریم، ایجاد یک کانال ارتباطی در طرف ایرانی برای کاهش تنش بود.»
ونس گفت طرف ایرانی با این پیشنهاد موافقت کرده و گفته است: «بسیار خب، ما یک نفر از سپاه پاسداران را به دوحه می‌فرستیم تا کنار یک نفر از سنتکام مستقر شود و از این طریق بسیاری از اختلاف‌ها را حل‌وفصل کنیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/76665" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76664">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FilIxC-idr4LwOWbMZlVK8hCYVeNH2lPUirOT8lbbT77BfRIvkeD1zslWxaCv6SzQa-9BpaBnS5RDBfKF7NYQKcgOlF9jrHx9oN6ekAEA4EGFRpiIrDc87ihRvh9ayTPKMxgJL6g6tx_JWO7shYtflV5xQdQGUDidTQfRM0is23MKUTJbFAbkChTaaWRV5gRDc4cJLX_bJe7zSTuVQh5viiqPB9_8OP-HUteKBSsaGNJ2lcysiniX1NK_YMULOo4Unv8pJIrxvuUwl-e3iU70DsAdFWuaLekySUJa4GlkHJL2SqAqOFccCWYNcuuSGbtuCCpjpS-18DNy3zb_9S46A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، روز پنج‌شنبه گفت اظهارنظر مقام‌های ارشد ایالات متحده مبنی بر اینکه ایران دارایی‌های آزادشده خود را برای خرید محصولات کشاورزی آمریکایی هزینه خواهد کرد، «ادعای دروغ» است.
او در شبکه ایکس خطاب به مقام‌های آمریکایی نوشت: «تنها محصولی که ما برداشت می‌کنیم، همان چیزی است که شما سال‌ها پیش کاشته‌اید: دهه‌ها بی‌اعتمادی!»
این در حالی است که بعد از اظهارنظر دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره این که ایران با بخش عمده دارایی‌های آزاد شده خود محصولات آمریکایی خواهد خرید، اسکات بسنت، وزیر خزانه‌داری آمریکا نیز روز چهارشنبه تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای «خرید مواد غذایی و دارویی از آمریکا» استفاده خواهد شد.
پیش‌تر عبدالناصر همتی،‌ رئیس‌کل بانک مرکزی ایران، نیز گفته بود که براساس یادداشت‌های امضا شده بین دو کشور هیچ الزامی برای خرید نهاده‌های کشاورزی از آمریکا وجود ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/76664" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76663">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">(
⚠️
۲۰ دقیقه، ۳۰ مگابایت، با زیرنویس فارسی)
مارکو روبیو، وزیر خارجه آمریکا، پس از نشست وزیران خارجه کشورهای عربی حوزه خلیج فارس در بحرین گفت هیچ‌یک از این کشورها از دریافت عوارض برای عبور کشتی‌ها از تنگه هرمز حمایت نمی‌کنند.
او افزود کشورهای عربی خواستار اطلاع از همه مراحل مذاکرات با ایران هستند و آمریکا نیز مایل است آنها در روند مذاکرات مشارکت داشته باشند.
روبیو تأکید کرد تهدید یا مسدود کردن تنگه هرمز از سوی ایران «مشکل‌ساز» خواهد بود و گفت: «هیچ کشوری در جهان از پرداخت پول برای عبور از تنگه‌ها حمایت نمی‌کند.»
عمان نیز روز پنج‌شنبه تأکید کرد که هیچ‌گونه عوارض ترانزیتی در تنگه هرمز اعمال نخواهد شد.
این اظهارات در حالی بیان شده که مقام‌های جمهوری اسلامی بارها گفته‌اند در حال مذاکره با عمان برای اعمال یک سازوکار نظارتی و دریافت عوارض برای عبور از تنگه هرمز هستند.
@
VahidHeadline
ویدیوی بالا درباره بخش‌های مرتبط با ایرانه و گزارش چت‌جی‌پی‌تی ازش:
https://telegra.ph/Rubio-06-25-4
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/76663" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76662">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHTKxjwRq-I4-yVblCCI5BJ86LaTdIJM8lYTBcWMG-xn3w1X4zDfeQaU0YarQbTN3bmDVmvMExhEom2RBYHZ5PqyNyJFEax6wHwyRoZ3nIWxaC_PuSloEQl4V7We1l7kaLiDFKqmLdjmSaOJX8xmAO4beMu0jZhtQkwWq25rq3wvwZMKTVq-tebxF5JBtQl23S30MTJizsGNuwex2598qxYLww0Oe7PQ2skD7XntLmv3YwYlQ59QwrdfhPTPVAbm4yQl7Fflfm3aNuhpFo6OnOnnAnRg_rUpOO6ZOaAKBPACyb8MBql7fZGbIIsqG3n5-ElL_vP9R7HFzVic8Py20Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
بنیاد عبدالرحمن برومند دست‌کم ۸۰۶ مورد اعدام را از آغاز سال ۲۰۲۶ در ایران مستند کرده است.
‏
🔸
روند اجرای اعدام‌ها در ایران حتی پس از برقراری آتش‌بس میان ایران، ایالات متحده و اسرائیل شتاب گرفته است. به طوری تعداد اعدام‌های ثبت شده از دستکم ۷۴ مورد در ماه گذشته به ۱۰۳ مورد، تنها در ۲۳ روز نخست ماه جاری رسیده است.
‏
🔸
بسیاری از افرادی که اعدام شدند، در پی دادرسی‌هایی نامشروع، شتاب‌زده و فاقد شفافیت به اعدام محکوم شده بودند. متهمان به‌طور معمول از حقوق دادرسی عادلانه، از جمله حق برخورداری از محاکمه منصفانه و دسترسی به وکیل منتخب خود، محروم بودند و بسیاری از آنان به‌صورت مخفیانه و بدون اطلاع‌رسانی به خانواده‌هایشان اعدام شدند.
‏⁧
#نه_به_اعدام
⁩
@IranRights</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/76662" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76661">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سپیده قلیان:
تا نت خوبه براتون بگم که اوضاع زندان سپیدار اهواز از دی‌ماه ۱۴۰۴ تا امروز برای معترضین خیلی بدتر از چیزیه که خودم تجربه کردم.
در دی‌ماه تا امروز، بازداشتی‌ها رو توی نمازخونهٔ زندان نگهداری می‌کردن/ می‌کنن. هیچ حقی برای ملاقات، هواخوری، وسایل گرمایشی یا سرمایشی نداشتن، و حتی دسترسی به توالت بیشتر از سه بار در طول روز نداشتن. گزارش بچه‌ها نشون می‌ده که خیلی‌هاشون آثار ضرب و جرح شدید داشتن. حتی نحوهٔ جلب‌شون هم عجیب بوده؛ مثلاً یکی از بازداشتی‌ها رو بعد از دستگیری با موتور بردن زندان و تحویل دادن.
همون‌طور که می‌دونید، زندان اهواز کانون اصلاح و تربیت برای دخترای زیر ۱۸ سال نداره، برای همین کودکان هم کنار بزرگسالان نگهداری می‌شن. زندانی‌ها آب آشامیدنی کافی و غذای مناسب نداشتن.
الان هم بازداشتی‌های جدید در زندان سپیدار در شرایط مشابهی هستن. این جداسازی که سازمان زندان‌ها از دی‌ماه انجام داده، اصلاً تفکیک جرائم نیست؛ فقط شکلی از کنترل بیشتر و آزار و شکنجهٔ سیستماتیک است. زندانی‌های سیاسی رو به بدترین شکل از بقیه جدا کردن، توی جایی بدون نور طبیعی، بدون آب خوردن کافی، بدون دسترسی ۲۴ ساعته به توالت و حمام. حتی نداشتن این امکانات پایه رو به عنوان بخشی از شکنجه اعمال می‌کنن.
#زندان_سپیدار_اهواز
sepideqoliyan
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/76661" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76660">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GkdfSvmeHsPVBRKIe5tDe2ZHBvSD8rb1FlLV8Jc8f8icL8igpvmaiDe71HgZJOFUEIX6W0pQmQ0O8yG2Yb5a8FniD_Rk4xLiXxs11vtFNwF9nWlOm7s-ggkuaQ3WROzlXwcHT2L3vh_epoKQZhPGR0TvFqqr_LtbzmS4ryLn347PiTkb5swx2dChYkYfh88SfwkxnObHoW1Shw0nee2p7kIiAJh5AETrlWeaO5ldibvH8EtOUhmKslG_zbNg9whNyHJ56qIIDsXUjYXp3AvqA6PE7MrFrBjXoI12DX2dc3GTdgIAWY8gs2S2cQJvqNB1v8yBNc103OEizJJf-JN3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد.
ترامپ، پس از تغییر نتیجه رای‌گیری در سنای آمریکا درباره قطعنامه اختیارات جنگی ایران، از چند سناتور جمهوری‌خواه قدردانی کرد.
پست ترامپ، ترجمه ماشین:
وای! سنا همین حالا رأی خود درباره ایران را از ۵۰ به ۴۸ علیه، به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر موضع دادند.
از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه تشکر می‌کنم.
این رأی به ایران هشدار می‌دهد!
رئیس‌جمهور DJT
realDonaldTrump
سنای آمریکا با ۵۰ رای مخالف، ۴۷ رای موافق و یک رای ممتنع، با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد. این قطعنامه از سوی تیم کین، سناتور دموکرات، ارائه شده بود.
با شکست این رای‌گیری رویه‌ای، بررسی «قطعنامه اختیارات جنگی ایران» عملا متوقف شد.
جمهوری‌خواهان و دونالد ترامپ استدلال کرده بودند تصویب این قطعنامه می‌تواند اهرم فشار آمریکا در مذاکرات جاری با جمهوری اسلامی را تضعیف کند.
رند پال، سناتور جمهوری‌خواه آمریکا، اعلام کرد در رای‌گیری درباره قطعنامه اختیارات جنگی مربوط به ایران، رای «ممتنع» خواهد داد.
او گفت به نظر می‌رسد درگیری‌ها پایان یافته و دونالد ترامپ از او خواسته است تاثیر این رای بر روند مذاکرات را در نظر بگیرد.
رند پال افزود: «رای ممتنع من راهی است برای اینکه به رییس‌جمهوری فضای بیشتر و اهرم قوی‌تری برای مذاکره به منظور دستیابی به صلحی پایدار بدهم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76660" target="_blank">📅 07:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76659">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2898920f34.mp4?token=Fw4IoR9kLDlB-9tUZ_1zODqXDECgc39OTHH_j7F5EEb_NZNjkq1JIQwd-i5Jv2M84a6NK5lz6xvBugMFXjz7V-Q6L9nUN2t8E_SQ_YRuIhXdI8zgH5L_MjqSpOZXijZkm_IEvKiY4NQbxmBjVDVHsgQzEv_X7Umf7klX045hTvVzmUfCn6jCtb9ASv9n_aasTWrSD_vq5PScvkAtKyusIlcuYa08jyZ30uy2mvaAzwXlBWikqBM7GYQ22oMJRriZpI7lNg-06g7EU5Hg7Q6ndVmgMFON9pPalIAqyct_anVVKJrrKiLZX7pR7vb2bXFedq4_Yw3Uq1oOI0-9dP6wegYTgD0yNHVruG0LON4uI5Nr1c3xpAIno0ufv1FXGcz666Trpezapn8Jz3pgqQaQ3WmlNt-7RvmRjxQYtID1fkBhFUhrgu7JgGJjnD5JklYLQ-glHhDkLrOhLm-5jb8hGuHiGCE6ShOOloU2bl6wpn01nUPEseMca4mD2argymPscaofrrGLIDqdLXImJRb9dLGSpNJTyred1eDXVzadPMjQIle4OSU2vQH131y6L3-arhCD6tpvIOstoLJHWiReeZLuiW4_kpfSdfJzQNn7UPJU_UgxQ7aF52314YWiPepR5U531x2shAt1Ka0moFDNbumqCsuETAA6ty47F6246Fs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2898920f34.mp4?token=Fw4IoR9kLDlB-9tUZ_1zODqXDECgc39OTHH_j7F5EEb_NZNjkq1JIQwd-i5Jv2M84a6NK5lz6xvBugMFXjz7V-Q6L9nUN2t8E_SQ_YRuIhXdI8zgH5L_MjqSpOZXijZkm_IEvKiY4NQbxmBjVDVHsgQzEv_X7Umf7klX045hTvVzmUfCn6jCtb9ASv9n_aasTWrSD_vq5PScvkAtKyusIlcuYa08jyZ30uy2mvaAzwXlBWikqBM7GYQ22oMJRriZpI7lNg-06g7EU5Hg7Q6ndVmgMFON9pPalIAqyct_anVVKJrrKiLZX7pR7vb2bXFedq4_Yw3Uq1oOI0-9dP6wegYTgD0yNHVruG0LON4uI5Nr1c3xpAIno0ufv1FXGcz666Trpezapn8Jz3pgqQaQ3WmlNt-7RvmRjxQYtID1fkBhFUhrgu7JgGJjnD5JklYLQ-glHhDkLrOhLm-5jb8hGuHiGCE6ShOOloU2bl6wpn01nUPEseMca4mD2argymPscaofrrGLIDqdLXImJRb9dLGSpNJTyred1eDXVzadPMjQIle4OSU2vQH131y6L3-arhCD6tpvIOstoLJHWiReeZLuiW4_kpfSdfJzQNn7UPJU_UgxQ7aF52314YWiPepR5U531x2shAt1Ka0moFDNbumqCsuETAA6ty47F6246Fs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری ترامپ و دبیر کل ناتو
در بازه‌های زمانی مختلف از این جلسه ۴۵ دقیقه‌ای، در مجموع حدود ۵ دقیقه درباره مسائل مرتبط با ایران حرف زده شده، به تشخیص ماشین البته:
مارک روته، دبیر کل ناتو:
اول از همه، درباره ایران. واقعاً می‌خواهم روشن کنم کاری که شما درباره ایران انجام می‌دهید چقدر مهم است.
این، پیش از هر چیز، درباره توان هسته‌ای است؛ توانی که ایران عملاً در آستانه دستیابی به آن بود. و این می‌توانست تهدیدی برای منطقه باشد. می‌توانست تهدیدی برای کل جهان باشد. این کشوری است که هرج‌ومرج صادر می‌کند. تروریسم صادر می‌کند. و آن‌ها خیلی نزدیک بودند به اینکه به توان هسته‌ای دست پیدا کنند.
هفته گذشته در گروه هفت دیدید که همه رهبران گروه هفت از این واقعیت استقبال کردند که این توان هسته‌ای تضعیف شده است. این فوق‌العاده مهم است.
و فقط می‌خواهم این را روشن کنم، چون گاهی می‌پرسند اصلاً همه این ماجرای ایران برای چه بود؟ این درباره امنیت و ایمنی است. این یعنی رهبر جهان آزاد مسئولیتی را فراتر از سواحل ایالات متحده، برای بقیه جهان، بر عهده می‌گیرد. و این همان کاری است که شما انجام دادید.
می‌دانم بحث‌هایی بوده درباره اینکه آیا متحدان اروپایی‌تان به اندازه کافی کنار شما بودند یا نه. فقط می‌خواهم یک چیز بگویم؛ می‌دانم شما چنین فکری دارید، و ناراحتی شما را از این موضوع می‌دانم.
اما وقتی به اعداد نگاه می‌کنید، چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های اروپا برخاستند؛ در شش هفته‌ای که این جنگ جریان داشت، تا زمانی که آتش‌بس در میانه آوریل برقرار شد. بخارست، فرودگاه رومانی، مجبور شد به روی پروازهای تجاری بسته شود، چون باید مطمئن می‌شدند که شما بتوانید هواپیماهای سوخت‌رسان را در هوا نگه دارید.
پس این ماجرا بزرگ بود. می‌دانم موارد پراکنده‌ای بوده که واقعاً از آن‌ها ناامید شده‌اید. اما به‌طور کلی، متحدان اروپایی شما در کنار شما بوده‌اند. واقعاً می‌خواهم این نکته را بگویم: چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های هوایی اروپا برخاستند.
خبرنگار:
پیام شما به دوست بزرگتان، اردوغان، و مردم ترکیه چیست؟
ترامپ:
من او [اردوغان] را دوست دارم؛ او دوست من است. او وارد جنگ نشد. او یکی از گزینه‌های اصلی برای ورود به جنگ با ایران بود. شاید هم در طرف ایران، چون همان‌طور که می‌دانید طرفدار جدی اسرائیل نیست. و من از او خواستم وارد نشود؛ او هم وارد نشد.
2:11
خبرنگار:
می‌توانم یک سؤال دیگر بپرسم؟ آیا گزارش مربوط به حمله به مدرسه میناب را دیده‌اید، آقا؟ می‌توانید به ما بگویید؟
ترامپ:
نه، آن را ندیده‌ام.
خبرنگار:
چرا نه؟
ترامپ:
خب، باید صبر کنم تا کامل شود. نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند. یعنی می‌توانید حرفم را بشنوید، اما نمی‌دانم اصلاً بتوانند— آن‌ها خواهند گفت یکی از موشک‌های ما بوده.
پیت، نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند؛ از نظر اینکه تقصیر چه کسی بود. چون موشک‌ها از همه طرف در هوا بودند. ببینید، شما انتظار نداشتید— و آنچه رخ داد وحشتناک است. اما موشک‌ها از همه طرف در هوا بودند.
و کسی گفته این موشک ما بوده؟ خب، شاید موشک ما نبوده باشد. اما من چیزی ندیده‌ام که مرا به این نتیجه برساند. موشک‌های زیادی هم از سوی طرف‌های دیگر شلیک می‌شد. پیت، نظر تو چیست؟
پیت:
خب، آقای رئیس‌جمهور، ما این تحقیق را بسیار جدی گرفته‌ایم. و وقتی زمان مناسب برسد، هر نتیجه‌ای که به دست آمده باشد، همان زمان برای اعلامش خواهد بود.
ترامپ:
منظورم این است، اگر به پاسخ درست برسید، فکر نمی‌کنم کار ما بوده باشد. فکر نمی‌کنم ما بوده باشیم. موشک‌های زیادی به سوی آن‌ها شلیک می‌شد.
خبرنگار:
آیا جلوی توافق نهایی ایران را می‌گیرید، اگر شامل هر نوع هزینه‌ای برای کشتیرانی باشد یا [نامفهوم]؟
ترامپ:
بله، برای من غیرقابل قبول خواهد بود. چون تنگه‌های متعددی داریم و اگر برای آن‌ها چنین کاری بکنید، باید برای دیگران هم بکنید. تنگه‌های دیگری هم هست؛ آنجا هم اجازه چنین چیزی را نمی‌دهم. بله، این قواعد بازی را عوض می‌کند.
خبرنگار:
آقای رئیس‌جمهور، فکر می‌کنم رأی کنگره برای پایان دادن به جنگ با ایران، حتی به شکل غیرالزام‌آور، تا حدی بر مذاکرات با ایران اثر می‌گذارد.
ترامپ:
ما در مذاکراتمان با ایران عالی پیش می‌رویم. درست وسط یکی از مسائل کلیدی، که در هر صورت به آن خواهیم رسید، خبر فوری داریم: سنا رأی داده که دوست دارد ترامپ جنگ را متوقف کند. ایران این را می‌بیند و می‌گوید: «این دیگر چیست؟»
حالا، می‌دانید که این بی‌معنی است، درست است؟ اما تعدادشان برای من کمتر بود. چهار سناتور جمهوری‌خواه داشتیم و همه دموکرات‌ها.
دموکرات‌ها می‌خواهند جنگ را ببازند، چون احمق‌اند. برای همین به آن‌ها «داموکرات» می‌گوییم. آن‌ها کودن‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76659" target="_blank">📅 01:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76658">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F86KIApscSBf6Q7KEbFce0Z_B1qnM65gMp6iQN0mHvUKw_5bC3oaOdFG-doBy9rKJj1yba4o-mPzBwEKYZg7ORmXJr9IWCVWbLO7fbG59HvcK-R5cDfxsqJQWcifIXZFZgq8-qXbMidhf8Y5WPARZRd64OGraOaD_0fT1djCi05JIBj7nORwa6iyoDjWm-cPqUGH2yNWSMJR9edTmDjpRxcKA5eCld8Gp2kp6S3tkOzo2A21eTcN_MilK2ESY1H1K-Vni689sGiTUBJVxvJV30qSfAw7Py9dRmIh85X0G6-Pghd_p0iHrXSxUbIwgg8VX3ep3Zm7DXVUuDmt78W_dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رویترز دولت دونالد ترامپ، رئیس‌جمهور آمریکا، قصد دارد طرح فروش ده‌ها موتور جت به ارزش صدها میلیون دلار به ترکیه را پیش ببرد.
چهار منبع آگاه به رویترز گفتند که این کار با وجود مخالفت‌ کنگره صورت می‌گیرد. خرید این موتورهای جت تحولی مهم برای آنکارا پیش از نشست ناتو در ماه آینده است.
این موتورها که تولید جنرال الکتریک هستند، نیروی محرکه قاآن، اولین هواپیمای جنگنده ترکیه، را تأمین خواهند کرد.
ترکیه به عنوان عضو ناتو این پروژه بزرگ را در سال ۲۰۱۶ برای خودکفایی دفاعی بیشتر آغاز کرد.
یکی از این منابع گفته است که این قرارداد بیش از ۷۰۰ میلیون دلار ارزش خواهد داشت و قرار است ظرف چند روز آینده نهایی شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76658" target="_blank">📅 22:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76657">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89b252a095.mp4?token=g4e8V6aUeqfoNnez6mtytp9d_Qc7l28JBt3bWcLNnEMwiKjm7C68pyZWnzktsu2mBIVGkgqZrZEF0xaZ8VInc_PVJyh2kzH8POYY3Bs50Jkjylz-BCBTsNfqqkWhiNmd7KU7Vp7h_oyngxjv0kK3AHwJA5gGcfm3q_lfLLaaYLiE33yrCkI7tPRhnO44uwIWeG8xkiugRB2ed1ZhR2fVXtZ5dJ9EvBQIG-Mr-D5djmJ2lWlo1QaAdotnPtL8REmuIel0VUeYMNtoatOCmsht3Kl-kca3236p3rWT6Ccfaga1-jP_c8D0s4MwgGf67aJ0GpqSbQ2hp6UQbEaB0CJdCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89b252a095.mp4?token=g4e8V6aUeqfoNnez6mtytp9d_Qc7l28JBt3bWcLNnEMwiKjm7C68pyZWnzktsu2mBIVGkgqZrZEF0xaZ8VInc_PVJyh2kzH8POYY3Bs50Jkjylz-BCBTsNfqqkWhiNmd7KU7Vp7h_oyngxjv0kK3AHwJA5gGcfm3q_lfLLaaYLiE33yrCkI7tPRhnO44uwIWeG8xkiugRB2ed1ZhR2fVXtZ5dJ9EvBQIG-Mr-D5djmJ2lWlo1QaAdotnPtL8REmuIel0VUeYMNtoatOCmsht3Kl-kca3236p3rWT6Ccfaga1-jP_c8D0s4MwgGf67aJ0GpqSbQ2hp6UQbEaB0CJdCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا:
«هر زمان که وارد یک مذاکره می‌شوید، با یک روند بده‌بستان و امتیازگیری متقابل روبه‌رو هستید. این یک اقدام موقتی است؛ فقط برای ۶۰ روز در نظر گرفته شده است.
در نتیجه آن، ما انتظار داریم آن‌ها به تعهداتی که در سوئیس پذیرفته‌اند عمل کنند. اگر به آن تعهدات پایبند نباشند، رئیس‌جمهور گزینه‌های زیادی در اختیار دارد.»
USABehFarsi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76657" target="_blank">📅 22:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76656">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=CRES2R3o8xtTG0nAM9_cUhZ9sYvdwpusYnzRhQmTevgUurwGouFfGw8ZKtdFXo-E0u25eR9tDodlIkL6GbnVm3xyw09-yLlweeRoqyID8DqMiSUh5CeqPCl1L3NQWImhwe0iWItrG64BLc2VY7BvRfOnOg-_8_9WG6-StB7wVIlC5WDedXf3hoiSSJXyFH5QdN2IYYvpPp0HHOmUm1taJlXsHUEKde9e9PIWGK3QXmgSsmqYZpGoGYzhFdNCfJM3JXwyaW52ZZAIahqHfF5w9LnZUB_ud06yTdPJhhiT0yzCaSVvco5P6KdGzdn3zqqoyTQPp65-tQGZu6X9CnTgQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=CRES2R3o8xtTG0nAM9_cUhZ9sYvdwpusYnzRhQmTevgUurwGouFfGw8ZKtdFXo-E0u25eR9tDodlIkL6GbnVm3xyw09-yLlweeRoqyID8DqMiSUh5CeqPCl1L3NQWImhwe0iWItrG64BLc2VY7BvRfOnOg-_8_9WG6-StB7wVIlC5WDedXf3hoiSSJXyFH5QdN2IYYvpPp0HHOmUm1taJlXsHUEKde9e9PIWGK3QXmgSsmqYZpGoGYzhFdNCfJM3JXwyaW52ZZAIahqHfF5w9LnZUB_ud06yTdPJhhiT0yzCaSVvco5P6KdGzdn3zqqoyTQPp65-tQGZu6X9CnTgQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه آزادی ملیکا ملک‌محمدی
این نویسنده و دستیار کارگردان تئاتر نیمه‌شب ۲۵ دی ١۴٠۴ در پی اعتراضات مردمی، با یورش خشونت‌بار ماموران امنیتی به منزلش در تهران بازداشت شده بود.
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76656" target="_blank">📅 21:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76655">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=u_wQAOTkdPsLITQVuEFHYN1b3ObUvDyhqgp_W5Y_gda5XGJC8y_iK-_p92qtkonE4zJlSjy4yGisCFR6JoRhBs6Z7o5tiIATbQMwOAk2mGCMbmNcMz1JTCZPwwm6ZafjW62PDpt0uKRhHWBn7V3F187Vzit-jMuuQnFj3ktn_eCfoJDCXmJIzUihMkde2iJ5f-hhlqGpVKXwWD_lcR2yV54vvijtKtZ7F6uZZjQAJ2VbCnm81vUuBToALqppXbH5Co-nb_14lIP4Z0kij08xDK7pC8-yfZE3fBJQbDiwQNHODqWO08sZwPULdhaW8eN54Y_sopvRKscrzdEm7VcvNw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=u_wQAOTkdPsLITQVuEFHYN1b3ObUvDyhqgp_W5Y_gda5XGJC8y_iK-_p92qtkonE4zJlSjy4yGisCFR6JoRhBs6Z7o5tiIATbQMwOAk2mGCMbmNcMz1JTCZPwwm6ZafjW62PDpt0uKRhHWBn7V3F187Vzit-jMuuQnFj3ktn_eCfoJDCXmJIzUihMkde2iJ5f-hhlqGpVKXwWD_lcR2yV54vvijtKtZ7F6uZZjQAJ2VbCnm81vUuBToALqppXbH5Co-nb_14lIP4Z0kij08xDK7pC8-yfZE3fBJQbDiwQNHODqWO08sZwPULdhaW8eN54Y_sopvRKscrzdEm7VcvNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه درباره روند مذاکرات با ایران اعلام کرد که تهران امتیازهای زیادی می‌دهد.
او گفت: «ایران در حال دادن امتیازات بسیار زیادی است و ما با اختلاف زیادی در حال پیروزی هستیم.»
او بدون بیان جزئیات بیشتر خطاب به خبرنگاران گفت خواهیم دید چه اتفاقی می‌افتد.
دونالد ترامپ ساعتی پیش از این اظهارات در گفت‌وگو با شبکه خبری فاکس نیوز گفته بود بازرسان آمریکایی هم با بازرسان آژانس بین‌المللی انرژی اتمی از تاسیسات هسته‌ای ایران بازدید خواهند کرد.
او در واکنش به اظهارات مقام‌های ایران در رد اجازه بازرسی به آژانس گفت: «آنها توافق می‌کنند، آن را کتبی می‌کنند، سپس می‌روند و می‌گویند که این درست نیست.»
رئیس جمهور آمریکا بار دیگر تاکید کرد که جمهوری اسلامی با بازدید بازرسان آژانس موافقت کرده است.
مقام‌های جمهوری اسلامی از زمان حمله آمریکا و اسرائیل به تاسیسات هسته‌ای فردو، نطنز و اصفهان مانع از بازرسی آژانس از این تاسیسات شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76655" target="_blank">📅 21:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76653">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=h4Fjo2jUfGR77ifHzv8yaH9Tvdnrk1cnhJNUjBLatquUt5m3yOIGrS1IQLg3k4O0qtMFUCzDMZvXvVCagCgbduPb98oxfi6jShXUVyc6FLfhD8zTPIJeAGMQJ_n8Sl-CZyAo1IhKWplvAuuf-Bx5DSbD3t_WLwm2c_xkkhoGiuicJSer3g4Vda4r1wR9BRHhOn0C0zkV0095yNCW1YC0kPljc-zanVLi-nsAdA-ZhsZPk1AZs6J2z31-KXh3it3YBexvtB0Rvz0tnh_n12OFbHI3iY9wukYzsTPLRabbFDdckNG5hAcnSJn0O0DDuNhknwdhPwJA8i3bWdcnXzUnug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=h4Fjo2jUfGR77ifHzv8yaH9Tvdnrk1cnhJNUjBLatquUt5m3yOIGrS1IQLg3k4O0qtMFUCzDMZvXvVCagCgbduPb98oxfi6jShXUVyc6FLfhD8zTPIJeAGMQJ_n8Sl-CZyAo1IhKWplvAuuf-Bx5DSbD3t_WLwm2c_xkkhoGiuicJSer3g4Vda4r1wR9BRHhOn0C0zkV0095yNCW1YC0kPljc-zanVLi-nsAdA-ZhsZPk1AZs6J2z31-KXh3it3YBexvtB0Rvz0tnh_n12OFbHI3iY9wukYzsTPLRabbFDdckNG5hAcnSJn0O0DDuNhknwdhPwJA8i3bWdcnXzUnug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به  پزشکیان دوباره بیل دادند، اگه شهباز شریف جلوش رو نمی‌گرفت فکر کنم تمام اسلام‌آباد رو درخت می‌کاشت.
NR2OH
مسعود پزشکیان، رئیس‌جمهوری اسلامی ایران، در جریان سفر خود به اسلام‌آباد به همراه شهباز شریف، نخست‌وزیر پاکستان، در مراسم نمادین کاشت نهال دوستی ایران و پاکستان شرکت کرد.
ویدیوی منتشرشده از این مراسم نشان می‌دهد پزشکیان پس از قرار دادن نهال در محل کاشت، همچنان به بیل زدن و ریختن خاک اطراف آن ادامه می‌دهد؛ در حالی که شهباز شریف چندین بار با اشاره دست تلاش می‌کند پایان مراسم را اعلام کند.
در این میان، لبخندهای شهباز شریف و ادامه بیل زدن پزشکیان توجه کاربران شبکه‌های اجتماعی را جلب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76653" target="_blank">📅 16:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76652">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lo-J2PnQJh1iZ4_ozEHbVNgrJC0DPIVUgF6vKStwySoKqZHfOOWlEZoyyaGqN7Ih5YXhhE9Zz-OmaQP6gEiPxftMFQLX35x9xiz85MjU9Mwd8hSNt-vmmFHXYjs7jggYGrYPOEYuIDsrsPNS7WyqmJRX0DSLka01CB_QUx9PmUAmGJm0BPE4FHokvGFazockN6kuclFWbR_QGEtIs2POWCheuP_14RC7zE60vP_DgsDRr4W5wPYa6jp8-f6sjkhD14MOrjauEGh0AtzG6jYd4boae9sOTcT_0lSmaMe6c5FDRGHOeXBGOffQEHY7V4xS2q6-TZ95KdEhFGuwgt5erw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده روز چهارشنبه گفت واشینگتن بر نحوه مصرف دارایی‌های آزاد شده ایران نظارت خواهد کرد و به همین منظور دفتری در دوحه، پایتخت قطر، برای نظارت بر این وجوه تشکیل خواهد شد.
اسکات بسنت در گفت‌وگویی با شبکه خبری سی‌ان‌بی‌سی، تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای خرید مواد غذایی و دارویی از آمریکا استفاده خواهد شد، حتی اگر ایران گفته باشد که نحوه مصرف این منابع را خودش تعیین خواهد کرد.
او بدون ارائه جزئیات درباره سازوکار نظارت بر مصرف این منابع گفت این وجوه توسط وزارت خزانه‌داری آمریکا در خاورمیانه نظارت خواهد شد.
مفام‌های جمهوری اسلامی در روزهای اخیر با رد اظهارات مسئولان آمریکایی گفته‌اند نحوه استفاده از منابع آزاد شده در اختیار تهران است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/76652" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76651">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyVKzZ59ZEaZIlh-c0kTjNBfuyjpmv92ThHVj8rxYSCmf1qIdZU5vCv-wAcF4EFBpVTjr5e3K9FvHHw3oWOdGV3bhgWKr78MVFNFz4Q2bEiw679YxuODlGkQd3fZXEK55dXj2at_8VkbZAhN0_C54cxE5TXtbDJu6Mni8Teuz-YKUh_xOiZjiwGH20euVKiu5nGHYKEH4VFgtD4hNBLo5yyyq8mBD8P1ZGo7dAZ8-LvcE73O1nM2Kv27pIeH_Jl9R-0YRXlPtb174O3Hu7Tu5-IkGYjnL9X0mhimVnC4HLIzaHZ7LZPWoxTk8lDGUTrEI4cFMMlG2RtoqZv1NeL2eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی اعلام کرد که دسترسی به تاسیسات مورد حمله واقع شده و مواد هسته‌ای صرفا در چارچوب توافق نهایی با آمریکا ممکن خواهد بود.
کاظم غریب‌آبادی روز چهارشنبه در شبکه اجتماعی ایکس با اعلام این که در سوییس هیچ نشستی با رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی «علیرغم درخواست او»، برگزار نشد، نوشت: «هیچ برنامه‌ای نیز برای دسترسی به تاسیساتِ مورد حمله واقع شده و مواد هسته‌ای وجود ندارد.»
او افزود: «این مباحث صرفا در چارچوب توافق نهایی و در نتیجه اقدام عملی طرف مقابل در خاتمه تمامی تحریم‌ها و... بررسی و تعیین تکلیف خواهند شد.»
پیشتر گروسی اعلام کرده بود که سایت‌های غنی‌سازی هسته‌ای جمهوری اسلامی توسط بازرسان آژانس مورد بازدید قرار خواهند گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/76651" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76650">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXNn1tD4CNrXqgZj9yq8IrJsEgSQbQCk7hsjFrKqTG2rlapxxl3HAKBDc4sBLlNlMvAnansFKXP95FOnLN1tQ8fS4EY41YS44OUrCVoo7tdVsqTQpgZMNVH6RBx1hPH6aS_M6usucTKVMavm2hq0ya6GugmsfFU8c4JFGg8CLR4kjl3I1V54jc_0ezD49uY10vsQjrjYIfnaloYXbzOwlXIjITkaEu8QTrdETdX5pLEV9SXbRbOxferZnrq8MbkejcMU-kUXx6wCuA7QZbxVPw6chCMWe2uCqgUVTjyvkC-eu6KXU172lA97HpnYpZMLt1f0WlfFy2m7DjV7dTAaSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، روز چهارشنبه در دیدار با رئیس امارات متحده عربی در ابوظبی درباره تفاهم‌نامه ایالات متحده با ایران گفت‌وگو کرد.
در بیانیه سخنگوی وزات خارجه آمریکا آمده که روبیو در دیدار با محمد بن زاند آل نهیان و دیگر مقام‌های ارشد اماراتی «درباره یادداشت تفاهم رئیس‌جمهور ترامپ با ایران، تلاش‌ها برای تضمین عبور کامل و ایمن کشتی‌ها از ‌تنگه هرمز و اهمیت صلح و ثبات در منطقه» گفت‌وگو کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/76650" target="_blank">📅 16:41 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
